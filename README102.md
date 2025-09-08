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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c76644b-5cd8-3ff1-8d8d-4c500e0b1597 | -14.5648 | -53.0925 | 2025-09-08 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 123c4b24-bb49-3e96-968a-853c4504b940 | -14.3492 | -60.3046 | 2025-09-08 14:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| c209ae60-dd74-3023-804a-0decdd9d0ea4 | -6.1904 | -40.9668 | 2025-09-08 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 6a6adae9-9dc1-30db-bd67-967e094b0a2c | -15.7583 | -53.5268 | 2025-09-08 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 2e6a5e31-5d1f-3a93-912f-8e3ebfd2ad67 | -11.864 | -50.7075 | 2025-09-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| aead9e26-3cd7-31a3-8d54-39275fe0a83c | -12.1316 | -50.6335 | 2025-09-08 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 7b50c723-4bb3-3538-9259-ca8873258b91 | -5.5437 | -43.7939 | 2025-09-08 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 05688adc-9355-3196-8bcf-f3af818cbb52 | -15.2302 | -53.7641 | 2025-09-08 14:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 994a411c-4599-3428-9020-07f7ec48bae9 | -15.0635 | -50.1089 | 2025-09-08 14:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| b8be2565-fdea-3afe-a69a-962fa05e296e | -11.4268 | -43.649 | 2025-09-08 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 8dbe6354-bafc-3048-9089-65128c96d5f5 | -14.3681 | -60.3228 | 2025-09-08 14:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 171.6 |
| a1a33177-7459-37f0-8c15-9220827fd7fd | -5.9567 | -45.7465 | 2025-09-08 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 05682c64-bb2f-3516-a496-1aa74b3b3921 | -8.1998 | -44.7794 | 2025-09-08 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 0581e47b-5d04-359e-a49d-d7a2787e5f54 | -5.211 | -43.2833 | 2025-09-08 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 174735a7-2e7f-3018-b4dd-9ae7ebb8c17b | -12.967 | -54.7705 | 2025-09-08 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 192.7 |
| 46d226f3-194e-3026-ba88-77e774955842 | -12.8411 | -52.8994 | 2025-09-08 14:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 03cec3e7-5c9d-301f-a09c-f5ad0d7117d3 | -6.62 | -53.3373 | 2025-09-08 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 635826c4-ef06-3e0d-9ddd-546ae898d014 | -12.8223 | -52.8806 | 2025-09-08 14:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 114.2 |
| da0c557c-d9e2-33d6-bd4b-911b49abf28a | -14.349 | -60.3243 | 2025-09-08 14:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| ea666e98-1792-3897-a213-1d5cf10c560c | -5.9752 | -45.7677 | 2025-09-08 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2b494ee4-bbcb-304a-adb7-3bdc9e3b69ee | -12.8214 | -52.9434 | 2025-09-08 14:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| f3bd374e-cf0f-3a5d-a112-7c76d08669bc | -8.4697 | -47.3376 | 2025-09-08 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 3543e6b4-11b6-3004-b353-df24a77bdf39 | -15.2545 | -52.3666 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 736b3acf-faa0-390e-a086-f217a32130f1 | -12.6343 | -56.9725 | 2025-09-08 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| a77db4ff-eeeb-351c-89d9-696667158fa5 | -11.2827 | -46.4817 | 2025-09-08 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 4bb3ce16-602a-3ce5-a283-34e64e39ee73 | -5.7113 | -43.8972 | 2025-09-08 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| de2df227-acb4-37bb-b80f-a41afdf7148b | -6.1904 | -44.7331 | 2025-09-08 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 4a5ad080-1c7f-3788-916c-c0a8ee11d08a | -11.2831 | -46.4591 | 2025-09-08 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 0345750f-3fca-3526-a27d-2bd23fff15e6 | -7.5035 | -48.2116 | 2025-09-08 14:30:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 7e70c0fb-0a49-3203-bc50-ba7ebfafe0cc | -5.6603 | -45.4525 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| bdf33b18-f910-3141-ada3-71915f4f4a5e | -5.6106 | -44.7078 | 2025-09-08 14:30:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 290.6 |
| ba1da937-2961-387d-b4c4-e60e52cc4eaa | -5.7725 | -45.4447 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 886bef2c-f89e-3ea3-b879-c7eebc2c4059 | -9.4624 | -60.4912 | 2025-09-08 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 9bd79faf-d9d7-3439-be7f-52c49e04e334 | -6.2036 | -43.3709 | 2025-09-08 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 9af17686-19ec-354f-9391-a0617c5db77c | -6.2092 | -40.965 | 2025-09-08 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 132.0 |
| c326e2e9-10a4-33ae-a47f-60fa90d93f0c | -11.4093 | -43.5573 | 2025-09-08 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f1a142e8-e30d-376b-b483-5f19c55fc6d3 | -16.3403 | -43.0394 | 2025-09-08 14:30:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 145ffa8a-f961-3001-8cdc-ff0f343e04de | -12.1319 | -50.6121 | 2025-09-08 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| bbe9b370-ce49-3be1-8489-de92172df405 | -5.679 | -45.4512 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 136.7 |
| b8c40f16-991f-3bbe-ba4f-f52c76ddbdb4 | -11.2007 | -54.9992 | 2025-09-08 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9b721dc4-53ba-30e8-b791-54481ddf875b | -14.4359 | -48.4644 | 2025-09-08 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 134.8 |
| d5ee1056-5811-3a4e-a8de-0db6f74c3b28 | -9.9971 | -51.6629 | 2025-09-08 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 56312584-f9b3-3b1a-9960-8ca7ddc53cb3 | -5.6293 | -44.7065 | 2025-09-08 14:30:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0b446e94-a4ce-3197-b94b-e03497545583 | -15.8197 | -52.2873 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 3afeb8c8-ef15-3fc5-9c0a-b7bbb62a4589 | -7.9928 | -46.3388 | 2025-09-08 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 60207330-f6a2-34cb-8c40-f3c5004f2205 | -12.948 | -54.7724 | 2025-09-08 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 265.4 |
| e193bf2e-aac9-34cf-864a-448fb6c6a99f | -15.8393 | -52.2845 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 995fd04d-161a-3465-9c3c-d43c49b37434 | -14.741 | -47.7668 | 2025-09-08 14:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d872eea7-a4dd-331a-b58d-4da5fa2d226e | -9.74 | -51.14 | 2025-09-08 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| d7d94541-6bb9-340b-b661-552f4a4e530d | -9.481 | -60.4902 | 2025-09-08 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 147.8 |
| ea61fc6b-786b-353c-9473-ef7dfb438f72 | -5.453 | -43.4525 | 2025-09-08 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 164dfadc-0b01-3377-9b24-180d538fc72b | -5.7113 | -43.8972 | 2025-09-08 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 353f44f2-3aca-38b0-9cec-a4a8cf82655d | -14.714 | -60.2551 | 2025-09-08 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 7cdef395-807d-3614-971f-75f887c4dba0 | -6.2929 | -43.8284 | 2025-09-08 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 66369992-036a-3ba2-b15f-ef7c9c3dfd08 | -5.3671 | -44.7703 | 2025-09-08 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 8a923345-089d-3caf-915c-019e144d4837 | -15.2496 | -53.7616 | 2025-09-08 14:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 59012c9d-62e9-33a1-b895-412fac039dcb | -15.8393 | -52.2845 | 2025-09-08 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 9064ac8a-2abc-3c07-9a13-58306149961c | -9.74 | -51.14 | 2025-09-08 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 28f2df09-4799-3b50-8550-a78823b52c2a | -9.7408 | -51.0767 | 2025-09-08 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 333ffdfe-b9c7-3e40-b2f6-cffeb66d1a2e | -11.2827 | -46.4817 | 2025-09-08 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 69d36a08-7e79-3ea0-8a6f-6ac9c0eabc1a | -14.349 | -60.3243 | 2025-09-08 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 98b337f3-9d57-3dc9-898e-764c6503eef5 | -11.8637 | -50.7289 | 2025-09-08 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 6d37397c-2ee8-3b3d-8859-8a18439c4901 | -15.7377 | -53.5928 | 2025-09-08 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 045526fb-057b-3c21-bd8b-902a6c00bfd0 | -9.6846 | -51.0608 | 2025-09-08 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d13a5bc7-420b-3989-9826-78dbeb23967a | -15.7381 | -53.5717 | 2025-09-08 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 6de1b030-9598-3fe9-b60a-a523f7d35ced | -14.3681 | -60.3228 | 2025-09-08 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 26871ea1-a0c9-376a-af1f-6c4d285c29f5 | -15.0635 | -50.1089 | 2025-09-08 14:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| d292e49a-0d94-353c-bc20-760402778196 | -12.6153 | -56.9742 | 2025-09-08 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 227571b6-0682-3321-a5e4-41344fd0ec6e | -9.4623 | -60.5104 | 2025-09-08 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 9add3b64-90b3-341a-8505-5b14c43f4d50 | -11.2196 | -54.9975 | 2025-09-08 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 178c5489-ae11-3048-bc34-5700c1dda319 | -7.5035 | -48.2116 | 2025-09-08 14:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| e8a484ab-f750-3f73-b28c-65b9a72201d5 | -8.0594 | -45.4771 | 2025-09-08 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| a52b116d-1eac-382c-9616-d9cb674910eb | -16.3403 | -43.0394 | 2025-09-08 14:40:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 151.1 |
| cca8e006-e28b-3c9f-82c4-f4a04c2dd531 | -6.4978 | -43.9732 | 2025-09-08 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 4e2df184-6d89-32f1-aea7-2ec4855421ef | -11.3905 | -43.5365 | 2025-09-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 69affa26-7f9a-3c47-b3be-0bb7f79f7eee | -16.9223 | -45.8258 | 2025-09-08 14:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 104.2 |
| a17a813c-4687-317e-ba92-028f14314260 | -9.4624 | -60.4912 | 2025-09-08 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 9d0801e5-c6f5-3c14-9ee1-496fa63132b9 | -5.9563 | -45.7915 | 2025-09-08 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 643226e2-d4a0-3fd0-9e84-3104d81ccc97 | -5.7727 | -45.4221 | 2025-09-08 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 83262dc6-eb19-358d-95d9-7ac0aea9cd08 | -12.6151 | -56.9943 | 2025-09-08 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| bf07f0ed-59d9-3044-8743-1c56f0aa054d | -11.0298 | -52.0454 | 2025-09-08 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 3f585dc2-57d7-3819-b0d7-d8737e8682f0 | -16.307 | -58.1055 | 2025-09-08 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.4 |
| efc54dd2-cb9c-32e7-a01c-3ab881a72e89 | -14.741 | -47.7668 | 2025-09-08 14:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 9e24c3ca-0ce9-37d1-965f-7310c17de2ec | -11.4268 | -43.649 | 2025-09-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| a8cfda3d-6c63-3972-8fa3-a173ffdeedd0 | -11.883 | -50.7053 | 2025-09-08 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 7dde2288-bb11-31b4-a692-8bcea7056785 | -14.4359 | -48.4644 | 2025-09-08 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 0f008f9a-56ed-3873-991b-cb9ddd59b83c | -6.209 | -40.9894 | 2025-09-08 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 162.2 |
| b7193751-a4f3-3a99-8baf-18d2146bd4ae | -5.7914 | -45.4208 | 2025-09-08 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 9fb47858-0039-3acd-ba58-364876f435f4 | -6.1848 | -43.3724 | 2025-09-08 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 95721fdb-70e3-30d6-aa5d-f6ec2611f459 | -10.7686 | -47.7302 | 2025-09-08 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 20d1c2c0-aca7-3371-a89f-105da73e07e6 | -9.7591 | -51.1172 | 2025-09-08 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 373.9 |
| 0f53d48d-10a2-3c2a-b07e-1f3e9f4cd5d2 | -14.527 | -48.7611 | 2025-09-08 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 4fe1c4a7-ecd6-3008-aa1b-26c2fb0ecf99 | -16.3073 | -58.0852 | 2025-09-08 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| fd75d2e9-dae3-3fda-a806-d83c577f6740 | -14.3492 | -60.3046 | 2025-09-08 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 502ab02f-b5c4-3392-8b1a-87e5f0dffd96 | -5.6106 | -44.7078 | 2025-09-08 14:40:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 215.0 |
| 23e29d0f-0264-3a01-a04b-3464b0bb960e | -6.2087 | -41.0137 | 2025-09-08 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 132.4 |
| 8931436e-4fd9-3f53-b3e3-3cb5b18b14e6 | -9.7403 | -51.1189 | 2025-09-08 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 2eeb86e0-7cc0-3300-8457-78cb30c8ed36 | -12.884 | -62.1062 | 2025-09-08 14:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 102.8 |
| dfc4e15e-6c90-3344-a143-f36160a6e7fa | -5.8354 | -42.6265 | 2025-09-08 14:40:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 86c97d1f-4602-3976-a3cb-05fd55767170 | -12.948 | -54.7724 | 2025-09-08 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 231.0 |


[Clique aqui para ver as próximas entradas](README103.md)
