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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d0d2309-1021-3b26-be59-1cfd8b2ca988 | 0.24 | -50.83622 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11f6e6ab-56bb-3454-b839-1d282a2bf599 | -3.91392 | -46.52073 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee08d9ba-b4a9-3401-beaf-a32cc232a093 | -1.5855 | -50.44307 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7376659c-2310-3148-8ca0-38e72bc253b3 | -1.81294 | -46.96002 | 2024-11-16 04:48:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cef73eb5-bdf8-3e8e-aaaf-f63bb7058f42 | -3.65098 | -45.49898 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 061fa965-9fd7-34b9-936d-3451d9c11f9d | -2.35593 | -49.12132 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| da8ea990-fc8d-3fbe-92c6-1e09b78a07db | -1.0863 | -53.17768 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73581dca-a941-35e4-a791-80d3851a9e05 | -2.14541 | -46.40941 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9274fdc3-0c82-34f1-8172-f30ecf52e977 | -1.99209 | -47.97447 | 2024-11-16 04:48:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 713f1ba7-ca66-3776-845d-a8e5ecc0511a | -3.99568 | -46.49687 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 729843e0-2480-32f0-814a-9ea7212cb88f | -2.35252 | -49.11395 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0edf669-be64-3b12-92e3-2df0a31a6d44 | -3.87762 | -44.49405 | 2024-11-16 04:48:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43d06139-4912-39e8-818c-6de9529f708b | -2.16355 | -48.91283 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ca4cb49-42ca-3958-bbd2-93fbba52ec05 | -1.23047 | -53.7055 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c5a2ef8-6b95-3444-a823-cf31373345b7 | -2.22373 | -53.61124 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| f9166565-d90c-32ad-bdc1-88c81349d4c9 | -2.56287 | -53.99763 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4be2ab6-90be-30b6-9648-f1c689e108f8 | -1.33293 | -54.17639 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba0b9923-666c-3087-816a-64a5ac1394ee | 0.10185 | -49.87212 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f30d9759-fe7c-379c-8f8c-2f8d9c74e74b | -2.10151 | -46.58973 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9ad2637-8c7f-3acd-81ef-146aaded3d82 | -3.03131 | -47.98439 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91196308-03c2-34c2-90e1-0b28ce5ac64a | -2.13046 | -50.19287 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e9f3faf-1111-379a-867f-1f8b62592d80 | -3.94282 | -46.70858 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3df622c7-c9d7-33ef-820d-786f5aabd603 | -2.54615 | -53.99116 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4ce7487-e633-3876-8f62-12f1a3e48e89 | -4.15403 | -45.43656 | 2024-11-16 04:48:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 173dc500-90c1-3548-88a8-fbda79ffae81 | -2.11216 | -48.8934 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b16b1c1f-52c2-3c6b-80d8-257342c4ad75 | -2.45807 | -53.92732 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bd6e266-d525-388a-a066-95615091f9e2 | -2.65297 | -46.16801 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edac7fb9-70d2-3f9f-a6fd-648d7ea551bd | -1.15701 | -53.50504 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac36db3d-66ff-362e-a7c3-219238334e42 | -3.04396 | -47.97703 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8d12355-3375-3ec0-941a-6c1a5eae46ef | -2.6264 | -54.26975 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1308a00-ffe3-3a94-9da0-ac9307b44e73 | 0.63744 | -51.85182 | 2024-11-16 04:48:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8590c28e-91ed-3d77-9c7e-a7f6f4cdaec0 | -2.30877 | -48.46929 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6e8fcab-04b8-35b1-baeb-feceeb624171 | -2.7108 | -47.72686 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b97b7e2a-34f2-3c79-83f5-6a54cd4599fa | -3.74296 | -45.66158 | 2024-11-16 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9066d794-2119-379e-a31e-94fb842536c4 | -1.68009 | -48.4653 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aacc1ba-50cb-3815-9881-343f836fcfcd | -2.13819 | -48.95811 | 2024-11-16 04:48:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb23452a-cb2e-3023-80a7-93ffd52081aa | -2.66676 | -46.18965 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fb56e5e-3069-37c3-b393-61b9fd56d41f | -1.8126 | -46.96238 | 2024-11-16 04:48:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1912509d-be7d-3c02-a711-246704bd9988 | -2.6465 | -48.48623 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cb2c8af2-edb2-3337-8b89-73acaaac05b3 | -3.43242 | -50.31711 | 2024-11-16 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e09d2940-cf4c-3016-9f3d-70ea6d4394a2 | -2.37237 | -48.91939 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea6d6352-c542-3fab-accd-b58d657e5b8d | -2.19214 | -46.61786 | 2024-11-16 04:48:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 882f244b-b3ff-3159-929b-d3043c02879b | -1.8674 | -54.27807 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7208f6fb-aba7-3e4c-a17d-7c17948a9e92 | -3.7393 | -45.65544 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4eae1521-69cb-3565-b66a-a1a595b09b74 | -2.22715 | -53.61176 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 043f6e97-085c-3012-ad75-7ed9e58329f2 | -2.34105 | -48.84101 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 778c5c87-92a7-3699-a8ab-37b1c70aa6c2 | -3.01632 | -47.98209 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff65570c-9659-331a-a3a8-6a3edfd1a340 | -1.21526 | -53.5605 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c53a42d9-6412-3131-b727-054963b1419c | -0.64965 | -49.39609 | 2024-11-16 04:48:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbcfedef-71b9-3e59-bd0b-4457bc6b7d4f | -2.07218 | -46.47947 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6617cbce-2e2a-3f28-aa2b-c98ed125c562 | -1.90272 | -48.09682 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 303e4dca-d7a4-3117-80d9-2ed634cd9f37 | -2.29229 | -46.45639 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae31b48c-ad93-3b66-88a1-1b3bc04ef0a9 | -2.2163 | -50.51465 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1c744d1-bee8-378c-8c88-1eafe962f918 | -3.51682 | -44.71451 | 2024-11-16 04:48:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bc76001-1115-3471-bd69-ebc1675594b8 | -0.25682 | -48.51136 | 2024-11-16 04:48:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79df05c1-8bba-3763-8dbc-ed4c961adf5c | -2.11982 | -50.84713 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f84be02-027e-3cc4-bdf9-b0917e40ab4d | -4.01481 | -46.53958 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4adec31-a514-3697-8051-9db82d0311c3 | -3.26775 | -45.50095 | 2024-11-16 04:48:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9cefd926-ed63-3620-b906-83ad3198a205 | -2.28877 | -46.45214 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c04ebbe-daf4-308e-ac36-a29c80dd222f | -3.91608 | -45.85406 | 2024-11-16 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1468a78e-d14f-3894-8216-c447f7af8d00 | -3.49548 | -47.21154 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 959d36d1-a0c6-3fd1-b85b-2ffbcade7cb0 | -2.65664 | -46.19983 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab4dec82-a4dc-3591-b166-7c0f7d7dad17 | -3.74371 | -45.65605 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d2ec1628-6a3e-37a2-9b37-58ded32bdd7f | -2.94505 | -48.3231 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7a9ab21-708c-3dad-84aa-9647b5b7edac | -2.45461 | -53.92678 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 941e69a0-dcff-3b9c-be6d-21dd93283567 | -1.99465 | -46.5801 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad9d78a1-cf65-3ca0-a257-194dc2467e1b | -3.84902 | -46.6418 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 937a7826-d4e0-3ce1-a846-e36bd736b0b2 | -3.79091 | -43.91099 | 2024-11-16 04:48:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e5d37025-e11c-3506-9829-98565525637f | -3.78594 | -43.9102 | 2024-11-16 04:48:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5b6c708b-83b0-361d-91cc-aee7e551d036 | 0.11807 | -49.84422 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b8aa32b-2300-325f-bef6-a6c273d478d9 | -0.78341 | -49.48346 | 2024-11-16 04:48:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87ab56d8-fb17-3cb2-b7c4-0b9902455b85 | -2.92302 | -48.3197 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 405fda5e-8c30-396d-8f25-dbcfa5b706b8 | -3.94337 | -46.41202 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eece5bc8-27ee-3b7d-a322-6b3c67174fcf | -2.64996 | -46.15972 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9937de76-7afa-3780-bfa3-489d1b2a8873 | -3.0177 | -47.97306 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea0c453d-0cc2-36a8-bb43-fd5204bf67e2 | 1.20197 | -49.97488 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 892d473d-7141-3168-b7f8-7f70e95070db | -2.46638 | -44.83997 | 2024-11-16 04:48:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 520b09e2-7654-31ee-ba2d-2c653728d3ae | -2.66016 | -46.17693 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66003a23-4cec-3770-b2f3-472f6b6669f5 | -3.12681 | -45.89713 | 2024-11-16 04:48:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5df8c4cf-45e2-34ab-866b-2ff910ff5766 | -0.75336 | -49.47135 | 2024-11-16 04:48:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eff40788-1d47-3ce6-bc61-c989351bc8f7 | 0.79221 | -50.73912 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5daf93a0-9230-3afa-98c7-efda45c66db2 | -1.63445 | -53.2803 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c166c537-6390-3cdf-aa72-cc9567b96f07 | -2.64886 | -46.19483 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a36f6eed-4d87-392f-9b69-7fc47d75c839 | -1.2333 | -53.70996 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5f5b33a-9dfc-3581-9950-16311b4a3f5a | -3.36732 | -46.50256 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08ad1c1b-3562-3c89-903c-6494aba4f0b7 | -3.08038 | -47.7674 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20b13fed-cf50-3182-a4e6-b74eb7277bf4 | 0.04729 | -49.52535 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af7a75ab-f0c3-3971-be4c-817ae9f82fa2 | -2.77911 | -48.57675 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c286471d-38ea-3fa5-98f7-6b74371238f8 | -2.6736 | -46.84428 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d72399a-bbaa-3b0a-ad00-919571a7d136 | -3.56983 | -45.67692 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 445fc74d-d200-3eb1-99a8-236b13e6ec91 | -2.57638 | -54.42018 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3a61d40-9e88-3a58-baae-dfd3685fdac2 | -2.15657 | -46.4185 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1f1ce8f-dd5d-3a44-b31f-5a20b1735d24 | -3.73039 | -45.65539 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b218bd11-5d49-394e-b537-930be5fff99e | -2.95307 | -48.01102 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09a775e1-1493-3c87-aa35-7f05fed55d08 | -2.4602 | -53.97394 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4802f3ab-3de3-349e-bdb1-b44d396c490f | -1.64061 | -50.52273 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 731f418b-8a1e-38b3-950d-7c53d7bf37da | -2.07912 | -50.34546 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da467308-ec67-3d0e-b53b-5e9502b9cdfa | -2.15618 | -50.527 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76e177f0-6b5f-3e15-abc8-142a02408756 | -1.57772 | -50.44906 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc94147f-23f7-3a08-8b9e-57936269f57e | -2.57506 | -53.97947 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README47.md)
