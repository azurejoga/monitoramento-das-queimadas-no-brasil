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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0c2485d-5bf4-3420-b382-8194eeebefbf | -1.942 | -56.65458 | 2025-10-18 04:27:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3df8340a-c767-3ff4-a356-e6913761f8e4 | -3.12966 | -50.21617 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf56006b-d0d5-3f56-bab6-c9d1b390fb9c | 1.77002 | -55.94487 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dd0ec57-f805-3ac1-ab9f-8d569c9d58d2 | 1.76051 | -55.98763 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 75d00049-f7ad-3710-b8a4-4d973491e408 | -2.95263 | -49.33885 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 65f2e95d-40cd-3a1c-adc5-8da8bd64fda0 | -4.40454 | -44.08499 | 2025-10-18 04:27:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a792903-bbdf-35c9-94dc-284c37da7da5 | -3.14138 | -50.24365 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ec86cb11-e2ea-3064-b8a6-81fa8a828c55 | -2.87834 | -50.73873 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1806f6a0-33dc-33c3-96be-d393d5abd3f4 | -3.51881 | -45.98736 | 2025-10-18 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10357a6c-446f-3495-87ba-8bfbb8befb80 | -4.70161 | -45.19987 | 2025-10-18 04:27:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f410c766-96bf-3bf4-aa33-2446477407e2 | -2.70825 | -49.41516 | 2025-10-18 04:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bd4a5c9-5eca-3215-83dc-50eaed8ee9f5 | -4.00144 | -45.50013 | 2025-10-18 04:27:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e0db4ba-e790-3f0b-aa46-c55c24371e63 | -3.25037 | -45.96976 | 2025-10-18 04:27:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5f561f8-49e8-3005-be4d-d205422af6c6 | -3.1578 | -49.1652 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| daa5131d-25dd-3db5-86e7-91414c4d112c | -1.94817 | -56.65575 | 2025-10-18 04:27:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4f8e75cf-75e9-31e6-bc57-0dd6b5c98742 | -4.39897 | -43.43422 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9b49030-eaba-3175-8523-8be2a8557506 | -2.87308 | -50.71925 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68895dbd-7a07-3398-824c-99ec4cca1419 | -3.75496 | -49.03884 | 2025-10-18 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1a71fae-fb37-3037-81e1-40589f7309b7 | -2.65996 | -47.87116 | 2025-10-18 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a74ee26b-6310-30e7-a8da-943b3b47edf6 | -3.14056 | -50.2487 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 19ac3cb7-db8e-3d29-85fe-6961e89e5a6a | -4.2194 | -48.35811 | 2025-10-18 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f36862bc-26cb-36e3-8157-6fc56004d79e | -3.68316 | -45.63434 | 2025-10-18 04:27:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4339992-33e9-38d3-8f57-fde53cac4262 | -4.39896 | -43.43105 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df035952-7d70-3131-a304-5071a2db2982 | -3.24522 | -45.96555 | 2025-10-18 04:27:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de890f2a-14ce-3b81-9990-021e62e77f84 | -2.88303 | -50.73576 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 324a5bc9-7d9e-3a4e-b788-da6ab2a6079c | -3.752 | -49.034 | 2025-10-18 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01c0e277-ef48-3313-ac83-494219598008 | -2.25437 | -47.02267 | 2025-10-18 04:27:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7fa78e6f-2471-3747-9bbe-d3c2deb92d0c | 0.98065 | -51.18126 | 2025-10-18 04:27:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32439fd7-26c6-328c-aae9-e293bd3739c3 | -4.45242 | -43.22561 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 02be7523-ab68-3de2-8ea1-906838b8f363 | -3.34985 | -40.4262 | 2025-10-18 04:27:00 | NPP-375D | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ae8c0099-7209-37ff-8a48-0813490d9692 | -4.05854 | -43.21342 | 2025-10-18 04:27:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7f319fc-42d7-3285-864f-dc216b77bacb | 1.75637 | -55.98237 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f871748d-d802-34d1-b45b-2a1ee50574c2 | -3.5378 | -41.71135 | 2025-10-18 04:27:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 85ebbb93-2a15-3955-8870-5dea9816ee41 | -3.47301 | -50.02472 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e33a683b-ec38-3300-bc54-03f4e84e959c | -1.61562 | -46.6682 | 2025-10-18 04:27:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 027db9c1-73f4-361d-ac21-21318f68218a | 2.16393 | -50.91628 | 2025-10-18 04:27:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e2a76b4-6271-3b44-991d-a3f27d42a52d | -1.93986 | -56.65509 | 2025-10-18 04:27:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c16b809d-478d-3806-a67e-9cdfc9c766f7 | -2.79079 | -49.59729 | 2025-10-18 04:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 121cb475-5fde-3a5d-a254-4c41fab701f2 | -4.40125 | -43.43937 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07cbb531-5f7a-3ac7-895b-c326b9083e2e | -3.14369 | -50.25439 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2ddad223-9ca9-3db8-a124-efe9284ff193 | -4.49836 | -46.48679 | 2025-10-18 04:27:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aff0a54f-d34b-3875-953c-95be2c2f0db6 | -4.40249 | -43.43473 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1c11793-1f17-38e4-a51a-f04c5e28d850 | -2.91266 | -52.72912 | 2025-10-18 04:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be1853bc-a425-3185-a42e-953f876b5c64 | -3.59413 | -43.0449 | 2025-10-18 04:27:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ec409ea-f22e-3a5f-87f9-3c7ad40db486 | -2.96259 | -48.58917 | 2025-10-18 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebc40898-88f1-37fc-8c94-546e84598e8c | -2.92442 | -49.17695 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a20df225-07f4-389d-83e5-d23d535150a1 | 1.7619 | -55.97641 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2578728-7186-35a2-b370-4258979a66d5 | -4.58482 | -45.64506 | 2025-10-18 04:27:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4190448-7756-3835-a4a5-45a18095866a | -3.59079 | -43.04547 | 2025-10-18 04:27:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e08c850-2f2f-3fa9-89a9-09e8447df63c | -3.94155 | -48.08933 | 2025-10-18 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce22a8ba-7cc0-3b2d-a454-5c9ef6ee629e | -3.43949 | -52.82689 | 2025-10-18 04:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3dbeaa7-957a-32fd-aed8-2d3b2ec1df15 | 1.76891 | -55.98043 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c19ff86d-92c1-31e7-aa3f-a22f9dc17d42 | -4.17167 | -42.20752 | 2025-10-18 04:27:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 760ff0b7-e9e3-300f-8cbb-44cce1667a3b | -3.81208 | -47.45886 | 2025-10-18 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa6eb9c8-42c5-38d0-b9b1-6ff6621d683f | -3.52699 | -50.31161 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72e81c61-626e-3691-bf42-21eef36b0861 | -0.9014 | -47.54285 | 2025-10-18 04:27:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d6c142d5-8a59-3547-b854-c6a1efab9d0a | -2.36889 | -48.29192 | 2025-10-18 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c4ca2ce-81be-367d-bd21-8cfc70591fe1 | -2.79737 | -48.93883 | 2025-10-18 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1a14439-276a-38a0-9629-fd1d117f7d09 | -3.46934 | -50.02227 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 750a6e89-a468-3b41-9178-7af107b65b8d | -4.11624 | -42.9114 | 2025-10-18 04:27:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28b1bfc0-c63a-3774-b6bb-5306133272eb | -3.34897 | -40.42514 | 2025-10-18 04:27:00 | NPP-375D | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ab8364d1-297d-30a4-88d6-f9ac9342c204 | -3.46913 | -50.02409 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9f25ec33-ab8a-3dca-96fe-3f50b3b7432a | -3.16151 | -49.16579 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9a16f274-c199-34c4-b2ae-e50959d61c96 | -2.87073 | -50.73376 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd7f39c4-8598-3b64-ba4e-0d1ea10cf892 | -2.87776 | -50.74235 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcc87ef3-ec5c-3b9a-97fe-6554f2ef2e78 | -3.86364 | -42.83826 | 2025-10-18 04:27:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 070fd17a-ecaa-346d-a2c1-4d14e0803876 | -3.59248 | -45.97069 | 2025-10-18 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5b4f59f-3cf0-3e37-b212-2da148268480 | -8.08578 | -45.44817 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ab8fda2-78a6-3cf9-a1cf-55b9f0a3e6c3 | -10.62132 | -45.23858 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98545b5e-2877-387a-81f5-147a93dbd9d4 | -10.49201 | -43.43858 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 1939633d-7f0d-34cf-9c56-1a36a40d97e5 | -10.25231 | -44.03282 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88c7946f-249b-39c6-a1ce-75ff65bc8995 | -5.59434 | -46.38219 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85d3058e-23cf-3ca2-9395-ab3c2e71ce61 | -5.59822 | -46.37924 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7bfee48-8112-3601-a67c-6f90e044ee14 | -8.2304 | -39.03763 | 2025-10-18 04:29:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 78fa59aa-877a-3ccb-a234-ef274c551d3d | -10.43098 | -47.73664 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5be7527f-4244-3660-b9f8-0b071f2eb8c6 | -8.8243 | -49.68147 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3189922-9822-3269-983f-87a51c532c42 | -10.48646 | -43.42394 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31bb650d-bfed-33bc-b4c8-9526450e0860 | -5.2128 | -45.23988 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4feb4edf-dd0d-3a72-bdf7-866a9dc5f472 | -4.00949 | -50.22268 | 2025-10-18 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4db18b9a-fb43-3953-9bc2-751b296a70aa | -8.04737 | -41.11472 | 2025-10-18 04:29:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6b5c9017-4271-36f4-9e1c-020aed0fbcd9 | -9.12592 | -46.61826 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 910bc453-33df-3665-808b-1e0a1a26fe3f | -10.33703 | -47.76831 | 2025-10-18 04:29:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e8001d76-55d8-3c66-8d37-b8cc9d90b9b5 | -9.16328 | -45.2501 | 2025-10-18 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4349d573-62bb-3699-b03e-a6bde5a23d55 | -5.92634 | -45.44115 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d7676a6a-55a5-3c01-8ca7-1e3a65c2ebc9 | -7.89558 | -55.42404 | 2025-10-18 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70046277-6fc8-3768-92d6-12d956c4cf40 | -10.14389 | -44.58055 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ff3fa07-af9c-3ac5-8465-43005e0ae56a | -9.22991 | -46.88167 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65d5628c-3f78-3063-8cb5-231d0ee902bb | -10.25263 | -44.03096 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97fb1f0c-8705-3e55-949b-b5d71f9c8b52 | -5.87082 | -44.21304 | 2025-10-18 04:29:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 129c6ea9-5c6e-3896-b03a-8aab1c3f1e0f | -9.37422 | -43.76125 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f4397b6-bf87-3a47-b62d-7f0b5a4d9abf | -6.8579 | -46.92872 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10c317c6-cfc6-3ed4-a08c-ef3d791424fb | -5.76192 | -46.69054 | 2025-10-18 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6839663e-fdc0-31f6-83f3-70a476fdf992 | -8.82362 | -49.68551 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad7a6468-79b9-310f-bc24-beff2b0ab5a7 | -8.85961 | -49.889 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e238ad2-eee1-3e7d-b40b-6869c653c167 | -5.37172 | -45.95341 | 2025-10-18 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f377bbe3-fefb-3cb5-96b6-78c91b3e84a6 | -10.49004 | -43.45215 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 86b2f9fe-3542-3aa0-b72d-cab75853a7ea | -5.00961 | -46.01664 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f737b54d-096c-32c9-98da-937b0086faf7 | -6.13886 | -44.27971 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a68295a4-3218-3562-8aee-9788ef9379a0 | -7.75068 | -42.50696 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 493d9b74-9487-31cc-a6f4-749d66862e48 | -8.82854 | -49.67802 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
