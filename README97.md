# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57f8fd50-1c79-3db9-90da-86c10cb85ca8 | -11.4125 | -50.3955 | 2025-09-08 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 180.6 |
| fe0ba383-ec5f-3c7c-b282-8e00e23d9649 | -6.6197 | -53.378 | 2025-09-08 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5eaf4bd3-16fc-3cf5-94f2-c4f695e45818 | -7.7296 | -44.735 | 2025-09-08 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 899dc5b4-3145-3bc4-9e38-8ba2357a0ba0 | -12.8411 | -52.8994 | 2025-09-08 13:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 272.6 |
| 962ebf17-cca4-3ab2-b60e-515cd23a56e4 | -16.3345 | -52.9387 | 2025-09-08 13:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 73565563-3702-37a7-9e1b-b98b81b5b4e8 | -14.4364 | -48.4421 | 2025-09-08 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| dccd99c6-f400-3820-a6dc-fd69d80423e5 | -6.6198 | -53.3576 | 2025-09-08 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ae911174-65e7-3636-ab2e-37b8073460c2 | -15.8393 | -52.2845 | 2025-09-08 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 054bd047-35a6-3cf3-a391-b8b5010cd6f8 | -7.9928 | -46.3388 | 2025-09-08 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| afdcffe4-a674-3e50-b71c-ce36804e07d8 | -10.8911 | -55.7131 | 2025-09-08 13:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| f42c191d-c972-354d-8647-279b49fe9c82 | -14.4359 | -48.4644 | 2025-09-08 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 374.7 |
| 7978add0-14b3-3e28-b2d8-0ed80046be67 | -16.3349 | -52.9173 | 2025-09-08 13:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 237a981f-123a-32b0-b4b8-4ca2fdd59c41 | -8.0592 | -45.4998 | 2025-09-08 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 23c81a5a-8c0a-3e87-b8a0-8ebdab7dbdb3 | -11.2007 | -54.9992 | 2025-09-08 13:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8806bf62-922d-37bf-8ff6-d479c1aad009 | -6.6382 | -53.377 | 2025-09-08 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 4bc7b3ec-49af-326c-b8a0-13743c7363fb | -12.822 | -52.9016 | 2025-09-08 13:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| eb3f3eb6-42c1-3534-86d7-1033eab9cc52 | -14.5266 | -48.7833 | 2025-09-08 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 690382c8-a465-3e2c-a90b-c5579353d641 | -14.714 | -60.2551 | 2025-09-08 13:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f1114d5e-93d5-3ab4-9b20-1e092020b78d | -5.211 | -43.2833 | 2025-09-08 13:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 910dfb5b-f1d2-35dd-8a10-f588dc1180a0 | -11.1568 | -48.4323 | 2025-09-08 13:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| cdaa7792-5871-3509-993b-dd5b75257823 | -15.8197 | -52.2873 | 2025-09-08 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c5988348-ec23-3d67-a972-ab58e27274aa | -11.4128 | -50.374 | 2025-09-08 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 48c8e0c8-fe9f-339b-914a-b7fc07cb8ba3 | -15.044 | -50.1118 | 2025-09-08 13:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 0b3fa931-8158-3d5e-a028-e114ab46c985 | -14.527 | -48.7611 | 2025-09-08 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| f04615fa-0dba-34ff-80cd-5258c630fd64 | -8.3179 | -47.4621 | 2025-09-08 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 051b721a-3886-3ec4-adf7-444a0075b530 | -12.8223 | -52.8806 | 2025-09-08 13:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 17c4453d-6764-321d-968b-c724037dc32b | -11.3742 | -50.4212 | 2025-09-08 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 4fe6a0f5-0efa-3cfb-b46e-91e5a68eb3d5 | -11.1758 | -48.43 | 2025-09-08 13:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 8a1f7bfe-3f96-38d1-9cc5-471c97b9ff59 | -14.3681 | -60.3228 | 2025-09-08 13:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 17a9ccaa-11b4-3f5e-96a7-cf492ff781d9 | -9.74 | -51.14 | 2025-09-08 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| ef324a7c-e2c9-3080-a1ed-4503cb30ebd6 | -11.2823 | -46.5043 | 2025-09-08 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 341152ad-edae-3e8e-970b-c585ef45ce35 | -11.0234 | -46.0184 | 2025-09-08 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c1fe9e37-aba4-3c0e-8c69-57db1ddd29df | -12.2941 | -49.9904 | 2025-09-08 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| b1d08a01-a555-33ec-8ce0-6d5301c981c7 | -7.7484 | -44.7332 | 2025-09-08 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 279.1 |
| 21a4c386-f253-3911-b6ee-eed0d0a7466e | -15.0635 | -50.1089 | 2025-09-08 13:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 216.4 |
| 346f503d-7972-3df4-be17-47e105e2bc1d | -7.7484 | -44.7332 | 2025-09-08 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 3a2ddef9-4e54-3c82-befb-9ee0813f22d4 | -6.6384 | -53.3566 | 2025-09-08 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 638e0eda-469a-3e66-9a3e-b3fbdf7f3691 | -11.4089 | -43.581 | 2025-09-08 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| c8d4a6bb-352c-3c27-bd3e-dc8de378a976 | -14.5266 | -48.7833 | 2025-09-08 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| f1586463-3ffd-3db8-909d-eaee5ea0d6c7 | -12.8223 | -52.8806 | 2025-09-08 13:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| dc47a391-f700-37d8-813f-496a917b05c9 | -6.4683 | -43.1848 | 2025-09-08 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 9b449094-fdde-374e-8ae3-1853777b28ca | -16.3345 | -52.9387 | 2025-09-08 13:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| ea761123-016a-383e-be89-7bc64f2837a4 | -19.1697 | -47.6729 | 2025-09-08 13:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 70.3 |
| bb2258db-c902-3a6f-a589-124e27683f58 | -11.2007 | -54.9992 | 2025-09-08 13:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| ffe565ca-682d-3814-95be-de382a6a9d9a | -9.74 | -51.14 | 2025-09-08 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4eb221bb-b00e-38f6-ac17-bdc04bf9fe82 | -8.0592 | -45.4998 | 2025-09-08 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 56d2071d-c879-32f6-9595-471c2bfecbbd | -12.822 | -52.9016 | 2025-09-08 13:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 8464dbbf-954e-3079-85e3-2ea161e6ae9c | -11.0234 | -46.0184 | 2025-09-08 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 611cdb96-0771-33f1-98b3-03beccf30c1c | -14.4359 | -48.4644 | 2025-09-08 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 192.9 |
| 0b65c16a-9cc8-30b6-aecd-89ba7f67b57e | -15.044 | -50.1118 | 2025-09-08 13:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 186.8 |
| f00af44b-2837-32d4-b3ac-34f56da56d74 | -10.8722 | -55.7147 | 2025-09-08 13:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 82ab1b10-6a0f-3601-83e9-004e76dafc80 | -7.6559 | -47.9593 | 2025-09-08 13:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 0126253a-8cf5-3c71-a49e-f24a6aa78668 | -14.349 | -60.3243 | 2025-09-08 13:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 9f667f2a-83c3-38f8-a5e4-d2cd2605e0b9 | -6.6198 | -53.3576 | 2025-09-08 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 1008dc27-746b-3f26-a8cb-efcda333c783 | -9.805 | -46.2152 | 2025-09-08 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 4166ba1a-4b42-3d19-8d7d-279e25a9d766 | -6.6382 | -53.377 | 2025-09-08 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 44112629-d2bf-37f7-b3d5-6f36de780766 | -16.3349 | -52.9173 | 2025-09-08 13:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d5f5a26b-7569-3803-90c4-fcede33443b1 | -11.282 | -46.5269 | 2025-09-08 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 8deb2356-7cb5-3cfc-b26e-7221432d1f01 | -9.481 | -60.4902 | 2025-09-08 13:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9a189bc0-a695-3f33-9a31-534530ff9ee0 | -16.9422 | -45.8217 | 2025-09-08 13:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 00d65b52-8518-39c6-8d74-67fd64e0611c | -6.1024 | -44.144 | 2025-09-08 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 724836c5-60f2-3e28-829f-ce161e029454 | -8.4697 | -47.3376 | 2025-09-08 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 8dca392e-067b-3db8-a547-134af0a2e12a | -7.7296 | -44.735 | 2025-09-08 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| ced7a399-8701-31e1-b6a9-7bc2e55d79f8 | -14.714 | -60.2551 | 2025-09-08 13:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 51f90fd7-9782-3df7-b21b-441717dc19a4 | -11.4268 | -43.649 | 2025-09-08 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| e7c6328b-8d1d-390c-b1b0-2a3af2740e19 | -10.8911 | -55.7131 | 2025-09-08 13:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 182.6 |
| 8b4f9aee-3777-3026-b2ce-1e18b3d7f8ec | -14.4165 | -48.4674 | 2025-09-08 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 0839716f-5234-353f-90a3-6e10405e2855 | -7.4367 | -49.2747 | 2025-09-08 13:20:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a5daca7c-acac-3e07-bccc-a4074f67786e | -5.211 | -43.2833 | 2025-09-08 13:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 53ea5b0c-2335-3599-b146-b2ee1bb62996 | -12.8411 | -52.8994 | 2025-09-08 13:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 253.2 |
| 8db7d5c5-033c-306b-9175-25f1a767659f | -11.2823 | -46.5043 | 2025-09-08 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 6ca26d88-f6eb-390b-a8c9-c858a02f8827 | -14.3681 | -60.3228 | 2025-09-08 13:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 186.2 |
| 95708f51-df49-394d-9970-1f0ba6a0cd34 | -9.8047 | -46.2378 | 2025-09-08 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 294b78a4-a9e1-334f-abff-74864258b34e | -7.9928 | -46.3388 | 2025-09-08 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c1052013-7400-3bee-8566-90b7d17868af | -6.4683 | -43.1848 | 2025-09-08 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 6f938890-1552-3f24-9aff-202d7c33e2ab | -14.3492 | -60.3046 | 2025-09-08 13:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3f7d4ed5-56c8-3b0e-a1df-6f7aa4559d52 | -5.7113 | -43.8972 | 2025-09-08 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| ce9fa3f2-49cc-3351-857c-44178fd01860 | -5.8672 | -45.3024 | 2025-09-08 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 06771e57-517b-3faa-a852-bf5f704ec090 | -5.9565 | -45.769 | 2025-09-08 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 7c37a48e-dfbe-3f8c-b9ed-d3857268200c | -14.527 | -48.7611 | 2025-09-08 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ffdfd678-8e9f-3def-8b4d-85070740ab2d | -5.8774 | -44.1614 | 2025-09-08 13:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| fc52ca0b-aab0-3e7b-992b-53ab8668ece6 | -15.044 | -50.1118 | 2025-09-08 13:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 4f005739-6db7-3b95-8821-95355ac47812 | -6.6198 | -53.3576 | 2025-09-08 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 22b5d772-3fd1-3bd0-b555-b30f1a66a977 | -5.938 | -45.7479 | 2025-09-08 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 5c9d4db9-aba9-3b4f-a009-474ded0f45cc | -11.2007 | -54.9992 | 2025-09-08 13:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| b6564459-e760-3f76-b7b5-96c78442a564 | -8.0592 | -45.4998 | 2025-09-08 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| c6bcfd08-89f7-3a37-93e6-5e0a65553e76 | -8.3179 | -47.4621 | 2025-09-08 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b91463a3-26ce-379f-b720-c08933371e40 | -7.7484 | -44.7332 | 2025-09-08 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 7057fff6-5d71-333b-9eeb-bdc56bb80003 | -9.74 | -51.14 | 2025-09-08 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e3e68612-c746-3f81-8b94-bfa49412d986 | -7.7296 | -44.735 | 2025-09-08 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| e2608277-fdc0-3955-8ffb-1812cc44677b | -14.4359 | -48.4644 | 2025-09-08 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 8c848fd9-25b3-3bfb-9d96-4976e3143996 | -10.0993 | -48.1595 | 2025-09-08 13:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 416a738e-a8c5-358a-9055-176f928b5e09 | -5.9567 | -45.7465 | 2025-09-08 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| da5ec42d-e208-32a2-9bd7-452ee632a8c1 | -9.481 | -60.4902 | 2025-09-08 13:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 14371231-d504-3b91-9611-3828ae48f51c | -9.7408 | -51.0767 | 2025-09-08 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| c828470b-e6a7-356f-bc3f-958318c75a53 | -14.4165 | -48.4674 | 2025-09-08 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 3e1220dd-026d-3933-b96b-e3357ff0a468 | -14.3681 | -60.3228 | 2025-09-08 13:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| af8f751f-61dd-3643-aed9-4e24b40af23e | -16.3345 | -52.9387 | 2025-09-08 13:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 6fa02123-e393-3c06-a845-38fb4d02cfd7 | -6.6197 | -53.378 | 2025-09-08 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| fbc0879b-374a-38b7-9efd-ce425243ed88 | -15.0635 | -50.1089 | 2025-09-08 13:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 150.3 |


[Clique aqui para ver as próximas entradas](README98.md)
