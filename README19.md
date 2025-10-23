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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd5f19a3-e3bc-35af-8355-bfd985b19b39 | -6.78949 | -45.44017 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afc9f80f-1295-388d-a0db-282febc5d428 | -6.96514 | -46.00483 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efee8064-a3a2-306a-9efb-5235b5fcea14 | -3.9871 | -47.88141 | 2025-10-23 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ff64d28-1904-342c-8c13-4f3cfa0dd5ad | -6.53235 | -44.36254 | 2025-10-23 04:36:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2fcd39fa-bf7e-3caa-b5e2-bab371655b58 | -3.39944 | -51.49679 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1feae3b-3ebe-35c8-9505-459b92b40d4b | -6.79414 | -45.45694 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a72c0e6-afc5-3ea2-aade-89dd2f04483e | -5.37162 | -46.87268 | 2025-10-23 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a0087ae-f4dd-3d9f-bf00-f9f18582ee78 | -2.98173 | -53.99612 | 2025-10-23 04:36:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f03673b4-4cf0-3701-80e3-9198094ca6b8 | -9.62681 | -40.33851 | 2025-10-23 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5a76191a-1c1e-3e31-a763-5366bdee2159 | -7.00285 | -46.99541 | 2025-10-23 04:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5f0622d-cbe8-3114-9f13-7b933f044ff5 | -7.76069 | -44.90327 | 2025-10-23 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b918fb16-b0d9-3abe-a414-0413d9e763aa | -3.69715 | -49.56756 | 2025-10-23 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e070b72-c5d8-3bd9-a270-59e60be6409b | -6.32591 | -43.74409 | 2025-10-23 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cef465cc-3f8d-3f65-809d-9cd61d9e512a | -2.90155 | -49.40213 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 305f9f7e-d3fc-35c8-9ba0-44393d00013f | -2.79522 | -48.89064 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d38b2fd-a9c4-361a-a879-ae039aa5f2c3 | -7.27412 | -46.16514 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10e69dd2-92b2-3d72-91c4-615052112e5b | -5.61822 | -41.11232 | 2025-10-23 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1018d2a3-7091-3510-9a28-7de95d644780 | -7.35954 | -45.02399 | 2025-10-23 04:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26f03201-aaa3-343c-8fd1-bdb8ef0710cb | -6.85449 | -46.28892 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57f4a1df-b1fe-3c6d-9893-d153df3b8731 | -7.62886 | -42.20004 | 2025-10-23 04:36:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4890502-01ed-3d48-a7c7-46086f0dad98 | -7.93319 | -46.015 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d40acdf6-7fe6-31ba-822a-72d0e6de1143 | -6.60436 | -44.21523 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 91420c7b-c35e-3c13-8b23-a4ee98a6b316 | -8.35186 | -46.18244 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a8170085-8e52-3e1c-8de1-315dd4e524fb | -3.04155 | -49.51815 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a46d677b-9870-36ec-9882-ad942df8a378 | -7.32445 | -45.28309 | 2025-10-23 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a4bc7b3-697e-3e48-856b-42c10da5266d | -6.60183 | -44.21274 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e065daa-8d00-3ea5-b88b-c838f7d96ffb | -5.6928 | -45.97419 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f99af807-5059-3a83-b4c1-cd79be9fc1fd | -7.27476 | -44.21834 | 2025-10-23 04:36:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 172c6f2f-1efa-3f5d-974e-1f2842f8278a | -9.62722 | -40.33559 | 2025-10-23 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 88b54f6d-9561-3383-a12e-e7a1dcac31cd | -6.32075 | -43.62203 | 2025-10-23 04:36:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d38b65e1-f43c-3dcd-acd1-95621adcbaac | -9.55733 | -44.87286 | 2025-10-23 04:36:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dbb925a-3ae1-38c5-b875-26f1182a9553 | -4.26607 | -49.01783 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 301ba6f9-52c1-3255-98a7-775324485e56 | -3.02322 | -49.47581 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 868c7eb3-a62a-3c42-b974-b95c8c6a3765 | -2.92646 | -48.30415 | 2025-10-23 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b6d5a1c2-d611-392e-aaed-3aaf407da179 | -2.35423 | -51.98631 | 2025-10-23 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b480b299-78ec-3a8c-b2b3-89bab7bd9779 | -4.30377 | -48.06334 | 2025-10-23 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45b465c0-d025-328a-80b7-7c98f1f36fc4 | -3.25331 | -50.13358 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 432d76ed-1bac-3bf5-90eb-686c06885a82 | -3.48108 | -50.08511 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9dee51a9-5682-35ab-8aba-3c5f2554c2bb | -6.91095 | -46.12717 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e367df6-489d-3508-b0dc-0b88ac15bf2d | -5.61694 | -41.12101 | 2025-10-23 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 55f21c53-b69d-37da-acd3-2648dd6cac87 | -8.3505 | -46.18255 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d07a4ea-3190-3d07-888c-b9bdf5633788 | -2.85824 | -50.74316 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 191efffa-27f6-3ea7-82c0-5be91181788e | -3.15204 | -50.16081 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95083c71-2919-34de-9a0b-e2398b7fc5dd | -3.39427 | -51.49884 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 715e777c-3d8b-3113-b91f-8960e26d00b0 | -9.63057 | -40.33488 | 2025-10-23 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 67d8aba5-0bd3-3dbd-bb77-120a4c9c848e | -6.08414 | -49.3784 | 2025-10-23 04:36:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a73372da-6391-3c6b-995d-3fbf125b2921 | -3.94924 | -46.96822 | 2025-10-23 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cc6dd62-780d-3f5f-bcc5-d24815e3dbe2 | -7.67039 | -46.58451 | 2025-10-23 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4c99727-4695-324f-af12-d1e38ffe90d0 | -3.15819 | -49.17459 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebbd68b9-827e-3066-b0af-9d3d5aeefdad | -2.53046 | -51.17571 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50813705-8460-3be3-b72a-db74ecba6899 | -8.00536 | -45.47442 | 2025-10-23 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cba1dcb8-e320-3ab8-b75c-343392596e51 | -6.64117 | -44.28217 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9afc1727-9c7d-383b-9306-c03f69793015 | -3.24184 | -48.76146 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79d87d69-9b95-3298-acfc-6379ffdde652 | -4.28318 | -48.25704 | 2025-10-23 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66109138-61df-3f72-92ab-b39cec219c98 | -3.59604 | -48.99215 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2a88ddf-897c-3f2a-8f59-5ecee2222794 | -3.11455 | -51.21161 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d2da802-2d36-3bc1-b356-b6f8b5e5389a | -6.48991 | -47.01397 | 2025-10-23 04:36:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ae68277-975b-33fc-9295-b9ca9e820e91 | -7.82701 | -45.38276 | 2025-10-23 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb6c971b-7fed-3a02-942f-ede2b7fcfaa6 | -2.91392 | -48.67313 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f815e2c-1bdd-3ade-8f44-921d90bcb9c4 | -4.19054 | -50.11303 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b958571-4b4b-32fb-acc4-15219bf9e17d | -2.80218 | -51.35255 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 289e7f7e-c02a-3dd6-9502-06cac81fc54e | -3.95256 | -46.96874 | 2025-10-23 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f33ba940-34b9-33e6-a10a-0aea3e939d11 | -4.30322 | -48.06682 | 2025-10-23 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3221042b-9a0e-3e5c-a01b-992b5291d322 | -7.1489 | -42.36351 | 2025-10-23 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 101ca68a-34d7-3acb-8551-cbb5ea41b923 | -5.32201 | -48.17429 | 2025-10-23 04:36:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa314023-f553-3828-9ea4-2e2cb939e32d | -2.875 | -50.71729 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d160d46-1fde-3918-859e-ff708c83f51b | -3.82025 | -51.05558 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a13ff569-bc8c-3188-b0fc-86cb32e97a37 | -3.38489 | -50.27028 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d379518-e008-3eec-86e5-b5e375064b60 | -3.48172 | -50.08107 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ebb0b618-8998-3d03-b66f-bae9e6854403 | -6.60063 | -44.21463 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7a00bead-61c4-3c92-a4da-8193484709d5 | -3.02898 | -49.48457 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| f2e8776d-0b8b-3d42-abf4-3b16fdf555f1 | -6.45422 | -48.75187 | 2025-10-23 04:36:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 200428d6-6950-3b96-8e6e-e59a2160395b | -2.8084 | -54.3799 | 2025-10-23 04:36:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dde4920b-5c0e-36e5-95f7-9bdc67acb6e9 | -3.33689 | -50.74856 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c777b70-db8e-331c-8ce1-17244f723eff | -8.44858 | -48.10718 | 2025-10-23 04:36:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8919f67e-f25a-3b45-8d7d-b28cdc9e7ea6 | -6.89665 | -46.1287 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db570ca9-6f8f-396b-8054-eb53d1aa4c2e | -3.47944 | -50.07246 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2de91dfd-cbef-31fd-a52a-065062579a96 | -3.76702 | -48.929 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1aa21595-e9d8-3c59-a504-a05ceb8ca7dc | -3.02404 | -49.44836 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3484bbfb-9ac0-3dee-aa1e-02f3018b8365 | -3.022 | -49.48346 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| f12fb3df-9b55-3e66-94b3-068e740843ee | -4.90135 | -43.20979 | 2025-10-23 04:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca2ad0b9-f040-3c8f-bf08-1ad0957abd37 | -9.63019 | -40.33781 | 2025-10-23 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 16001d43-6e75-33cb-96c9-51bb18e9da51 | -4.18386 | -46.22991 | 2025-10-23 04:36:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27a7e27e-154f-3955-833c-26d03f1d6a70 | -7.88494 | -43.54601 | 2025-10-23 04:36:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2c8d592-ca88-346f-816a-b86dd7acce87 | -7.36006 | -45.04525 | 2025-10-23 04:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 624e5b63-2bfa-3b93-aa5b-7296411f71d9 | -7.88814 | -43.5517 | 2025-10-23 04:36:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd902e48-56ec-3d08-9b9f-9b7cc1083b0c | -3.0499 | -48.71647 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee16ddd8-a6d6-3186-9c94-648a25e4ce39 | -6.78597 | -45.4396 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8abe0e6c-eb94-33d8-aa8d-c2bf8d5f4fa5 | -6.27754 | -47.00946 | 2025-10-23 04:36:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c343e7a-2ff5-30b1-b495-16617661ca78 | -3.47587 | -50.07192 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22556f4f-2826-3e46-8b44-e26507239da5 | -5.61629 | -41.12543 | 2025-10-23 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 190d4008-7e42-3838-943f-95bd15575e4a | -4.63687 | -49.53744 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 387c5f61-85f4-302f-94d4-0943f60dd815 | -6.96208 | -44.01262 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e1d9f8b-ca8d-3751-9fb1-3085a4a447c3 | -6.7337 | -44.15206 | 2025-10-23 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfa07a2f-5bcc-34b7-9e0e-9396de692be4 | -6.9652 | -44.01786 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba55d0c7-509d-384e-8604-64f172fcd625 | -3.11531 | -51.20698 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fcc9fa8-e8d8-3cf5-924b-b01f19f33188 | -3.02342 | -49.45219 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9657c4b6-3ae6-38d3-b4c0-fdfa83b7b7f2 | -6.30628 | -41.88456 | 2025-10-23 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 153587c6-ffdf-3495-89a0-6259fd16bbfa | -7.94538 | -45.25437 | 2025-10-23 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed7f3eb8-1a26-33b6-b0b7-c3cbf6adb63c | -6.85449 | -46.28891 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README20.md)
