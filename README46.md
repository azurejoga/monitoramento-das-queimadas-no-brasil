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
| e2cc4cdc-9fb2-35f8-aa6d-09729d153a6f | -4.32933 | -50.67791 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e66a4e60-1365-309c-abb7-d4deda1e272a | -1.33598 | -47.6853 | 2024-11-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eae80870-7b29-3992-8af3-63d39e0a95a9 | -3.80514 | -44.68393 | 2024-11-10 04:14:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58bb55b6-732d-3b6e-8bc4-7a0c98a0c4fa | -5.2637 | -44.87528 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55a85af7-4c5d-32ef-a6a9-4591f1c2864a | -6.1568 | -41.14547 | 2024-11-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90b4cebc-5151-35be-8677-79925787930c | -3.14945 | -45.94245 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dca45be-755c-38ca-92d5-2f09ef6a6c58 | -4.6861 | -48.75877 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d24b41b-564d-34d4-9b2a-4d9a91272b1e | -2.86555 | -49.39381 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3dd27ad-2355-398b-9c82-7547982834f5 | -4.15961 | -45.74541 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0226341e-87c8-3ef8-8b97-b1788c4afaf3 | -2.8658 | -47.90773 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63227eaa-2a88-3234-8694-1ce0c794f317 | -2.60324 | -46.12689 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11e59827-c2bd-36e0-a1dd-cd9702b50220 | -3.23821 | -50.44969 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f4bfde91-0f55-3f73-832a-7dec01dfb251 | -6.51923 | -41.43879 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0180f68f-ff99-3d35-ba8a-2614dd10a784 | -3.23781 | -50.31799 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9141329f-4a48-3ed7-b5c4-805e46717f2e | -3.80384 | -41.27283 | 2024-11-10 04:14:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d037a007-40d0-31fc-8e01-5dc0e0d5176f | -2.93862 | -52.77404 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f8e2e53e-e0a6-33a9-b7e9-57f0ef43a063 | -1.15481 | -53.78706 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b9e5d30-c167-3396-860f-111769048e93 | -4.90971 | -48.55745 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 460df430-5586-3601-a929-c2ebea083e7a | -3.21876 | -50.29096 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 4ff17b62-6a3f-3fde-bd82-a0c2791c29da | -3.94729 | -48.15475 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 126760db-4982-39b7-92b6-863a12e84e04 | -3.96232 | -48.99141 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b24e92b-b2f7-321e-9485-8e375ef3e398 | -1.39535 | -52.36462 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e7536a0-2e0e-3d0b-8463-251985a831d6 | -5.11956 | -49.91805 | 2024-11-10 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0326c173-a87b-307c-b9e2-fbf57e0b99bc | -3.17869 | -50.59964 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4891f790-5558-3d47-a844-0d47093f36f5 | -3.69747 | -54.62098 | 2024-11-10 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 714e2a82-2d4f-38fe-997a-7d604f257a56 | -2.91771 | -51.6789 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fa4ad01-001c-31a4-85e4-1d1a045bf9f7 | -1.87525 | -50.96403 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b6607d6-bac2-383f-91a5-aee0bee6c58c | -2.4707 | -49.3616 | 2024-11-10 04:14:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcd515fb-8e8c-364a-8c3b-c1238fc7a4a0 | -3.30548 | -50.09146 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f35a9e2-3894-3e25-96c2-51295d115e82 | -1.58439 | -48.03028 | 2024-11-10 04:14:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6d7c8a4-d904-3abd-a42f-7a7d7dbfde21 | -3.20469 | -46.49678 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59bddb12-dc38-3e93-b067-6f457dbcdbfc | -3.84799 | -44.12564 | 2024-11-10 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 831d90fb-1fb3-3b8d-9bba-49fcdfb7add4 | -3.95497 | -48.15969 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70844dd1-0413-3f12-b661-63777936f75d | -5.45209 | -43.27042 | 2024-11-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a398dd2-b07d-302a-b0af-ec0c72173e02 | -2.63104 | -46.15658 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f4fcb77-8057-3a47-9ab5-206249ab864b | -2.65706 | -48.48604 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16d28c12-dc59-3135-9f29-45d0292a91a1 | -1.93907 | -52.1671 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec89062c-b3bb-3f7b-b597-4dec62737ce0 | -3.25674 | -48.74632 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 023b3e97-549c-3f9c-9cc8-69849e3be44c | -1.52244 | -52.21117 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b5444b8e-b6bc-3d67-b3d7-f68e20787717 | -3.57752 | -45.82314 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 06cff6ca-d05c-3cb7-bdd3-84eb9fee8e38 | -3.82165 | -44.84359 | 2024-11-10 04:14:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 762c9efe-7f68-38e4-b924-d4f31dcd69e4 | -1.43748 | -48.14446 | 2024-11-10 04:14:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06fa59b0-4dfd-30cd-8645-b7707c0dc164 | -2.55151 | -45.38958 | 2024-11-10 04:14:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c749655-bc45-343e-bdcf-2b05e49d5b10 | -3.25098 | -50.30719 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9f7bf327-ce03-3532-b230-dc94b7cea557 | -4.11974 | -48.50446 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6dc9ae7-0341-3972-bbcc-436444e0eb34 | -3.24669 | -50.33398 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2b9aeb5-d704-313c-94af-84670ba438db | -2.20727 | -47.74318 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 172288ea-7118-3809-83b1-508264380af3 | -2.21139 | -48.36863 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b58e9256-d8fc-3466-8110-bd11d2ae5a1a | -3.45743 | -50.18306 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b6ce1dc0-f93b-3d76-b577-2a18b8a61df2 | -2.04718 | -48.98864 | 2024-11-10 04:14:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e7246fa-f04c-3eb4-b45f-a6cb9a7ba871 | -4.08262 | -42.93484 | 2024-11-10 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54f4997e-c373-3016-8446-cdc67e739204 | -3.18748 | -50.58552 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 824c6cbe-ab1e-3e8a-9408-8570f62736ed | -2.87385 | -49.51563 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ef1537a-0ee1-3579-bc66-c6c55d91ed03 | -3.09827 | -49.41066 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c0480d3f-5001-3b5a-9982-229dc73bf6b0 | -3.19078 | -48.65887 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 309de1be-c3ec-3728-afb1-e08230367ce0 | -4.84656 | -48.62645 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3fe72e9c-61c2-391b-95e3-d08fea423351 | -2.92064 | -51.67992 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a121b727-2b2c-3e82-88e9-8ea1ee9feb38 | -3.94938 | -46.38138 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32f8f6ea-b6bd-3a3c-b883-c8393410a3e3 | -2.94314 | -49.49714 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c9f680c9-057b-39ae-ab74-563413542a4d | -5.56664 | -47.78416 | 2024-11-10 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 098828b9-c034-3530-b3b0-993378c428e9 | -4.08813 | -48.51188 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 769e7d21-30e9-3bb6-bb61-b1c5382bf79a | -2.90925 | -49.24263 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e58957f9-7250-3392-8bbf-0a7ac8870640 | -3.32738 | -43.99663 | 2024-11-10 04:14:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ecd3d4a-5107-3824-a1a6-8d88412a5722 | -3.11528 | -50.14212 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 883332b6-5a25-3f48-a9d6-e050b5354860 | -2.59673 | -48.31416 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c5adb8d-dd83-309b-9794-fb90f7121651 | -2.65476 | -51.8793 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e2905e9-fa23-3a8b-9e98-8101c755743c | -4.10364 | -49.12148 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| beef5b9d-b0d7-386f-871b-bae95227e8d9 | -2.34804 | -46.63516 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2b50f3e-cfae-3926-8bf8-74432743c27d | -5.56355 | -43.97094 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3b74b728-afbe-32fb-af9e-69a53848f4d1 | -2.23532 | -53.79353 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cec4ff19-aa54-3f11-a813-d6aa5f31597a | -4.02455 | -43.60993 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71147078-e05d-3b2b-99e6-2f10dcb346c9 | -3.69969 | -43.51236 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8e2c576-40f8-3fb1-a312-20a84e6d8ec2 | -1.52026 | -54.99988 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 326a6f47-dc36-3876-8f5e-54996d5ea0df | -4.10148 | -49.13439 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58380c56-acd7-36c9-bb65-10947668cf5e | -2.21021 | -47.75137 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0faad378-03af-31fe-ba49-2487def31fb3 | -2.29849 | -46.74556 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc78b615-de85-37fd-9487-94d257a5983b | -3.99564 | -46.41468 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44be0d44-e5ae-3f41-9254-37ded936fcb6 | -4.68659 | -45.14745 | 2024-11-10 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16e690c5-edf7-3318-a5aa-f48c21b1e25b | -3.24267 | -50.31874 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a064e551-28cf-3d71-b2da-31ead16c819b | -4.27868 | -48.19917 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c556c0f4-29ae-32db-80d3-d61e43bd9f9f | -3.04237 | -50.32416 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ebe597f-c4e0-327b-9adf-e4a4b548abf7 | -1.52876 | -52.20819 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19b0eb98-c374-3a48-9c01-517834453f04 | -2.59351 | -48.20395 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40314d5c-dacd-3652-a04b-d5c07ab8308f | -2.92755 | -48.31216 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd4cc529-278a-32e4-b136-c083c0eb4927 | -3.59711 | -43.40726 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01f14595-44d7-3de9-ab86-01a77bc5ee49 | -3.46139 | -50.18896 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 77b4b787-2c0a-3315-a24a-2b43406d1600 | -1.72299 | -52.46752 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1b08de4-6980-3126-974b-4a04cdb318dd | -4.93139 | -48.24387 | 2024-11-10 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5eb1b52-d42d-34f6-beba-fadf170763d9 | -3.10776 | -48.61281 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fe6ac49-a180-3186-adac-42e9961662a6 | -3.70984 | -53.75379 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e45658b-ddc2-343c-a45d-d65c017c1e7f | -6.40747 | -42.48611 | 2024-11-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e52761cf-0597-38fd-a8cd-386a4059d584 | -4.10839 | -48.27751 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0bc48a3c-11a6-3af5-bbfc-dddd00bedb91 | -4.79788 | -48.4724 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63420b1a-5e88-3699-bd86-9f3198962abc | -2.8863 | -48.29752 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf9f0d93-46ab-3251-9260-d997afe9cc83 | -4.41664 | -45.70401 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34874212-69c6-39cb-8d81-5b681f906460 | -4.28281 | -48.19984 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d645947d-ef26-3107-b583-07de6f4b233a | -4.06194 | -50.01305 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b14aa1f-0192-3f3a-bdaf-ae2d0621987e | -2.08492 | -46.78974 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4d9a73c-06e3-337e-bd13-30b95a506872 | -3.95626 | -46.99168 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce8fa19e-4152-3614-8815-3cc95cc86ddf | -4.10192 | -49.10491 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README47.md)
