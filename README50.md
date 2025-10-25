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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ac05cb3-61ae-38b2-9b78-e333105ed416 | -3.16085 | -49.17255 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73ce0581-edd0-39f6-972e-7d710bba09ac | 1.6301 | -55.74878 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4913636f-a429-3960-a208-fa3277f3918b | -2.80874 | -49.13456 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 8b1e4757-20a7-3406-abdd-61ad4825cd44 | -1.34574 | -54.61345 | 2025-10-25 05:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa1e3976-b669-3510-8b63-d6c75b81ad40 | -2.80849 | -51.3483 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04839886-c9bc-32a8-9a35-554e2c105793 | -2.2674 | -47.85505 | 2025-10-25 05:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bda66011-214b-385b-9836-450d5fb4c529 | -3.11668 | -51.21288 | 2025-10-25 05:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce26b5da-c546-3262-9643-e1b5decc2398 | -2.8039 | -51.35125 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf4f67ae-12e2-3f25-b1b7-0c92f3bab912 | 1.62343 | -55.77084 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b3bf9f4-29a1-3918-8b23-4508e6ebf5d9 | -2.72489 | -49.16634 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 718d4a24-da24-35fa-a52c-d5acd995df3c | -3.23732 | -48.75835 | 2025-10-25 05:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b02cf7a-6eb9-37c1-ae91-961dfbe04aa2 | -1.18811 | -53.40508 | 2025-10-25 05:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f6f5788-d930-3778-a588-1cd2706c3f44 | -3.08998 | -49.25896 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0f1db68-e02e-324c-8a0d-f364e3d8d5f9 | -2.86699 | -50.7147 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88caee19-7c56-326c-8cfe-05732258ce57 | -3.13966 | -50.15928 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da85dcc5-138d-31c3-a5ee-3359d9a27ae6 | 1.6373 | -55.73014 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf157be8-e269-34c6-bb19-ce71b88373d7 | -3.10904 | -51.20786 | 2025-10-25 05:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6254849-91de-3b4a-aa00-bc377f0a7046 | -2.25664 | -56.85869 | 2025-10-25 05:08:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cfbbdee-cb52-3d6d-bdc3-d197817939d3 | -2.60354 | -54.23147 | 2025-10-25 05:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c4d53cd-be3b-38e3-9051-1dced6037fd3 | -3.11779 | -51.20553 | 2025-10-25 05:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c5079b0-d5f6-3545-bd63-9a69b1759e26 | -3.12348 | -49.09951 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8c9fc989-c9a0-3f09-a9a0-44eb2e0012f6 | -1.5941 | -54.30867 | 2025-10-25 05:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d771320-e094-383f-810e-c990de43f66d | -2.87063 | -50.71927 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6107eb51-9ac0-33e5-a0b0-563edae57af6 | -3.16205 | -49.174 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48d9aa18-7b2d-3b2e-8d80-f36f42e2d212 | 0.3665 | -50.85723 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 021cd4f3-bcfc-314b-92fb-d69bb87edf43 | -3.29713 | -50.19092 | 2025-10-25 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a63f4bf1-a23a-354e-88d5-1fd35888e9e9 | -2.80226 | -51.36192 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f955d926-de3b-336f-a79e-b311fed399bc | -2.72829 | -49.15778 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f8e4aa8-b426-33a3-91f9-5f4b17763d47 | -2.26025 | -47.84764 | 2025-10-25 05:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8d34ff4-8972-3b43-8995-dea1e0c2f200 | -1.8192 | -57.10825 | 2025-10-25 05:08:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7d085d1-3cd8-3061-82b0-06f3c3964978 | -1.5113 | -55.86024 | 2025-10-25 05:08:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7e75481-9fc4-3e1b-9aa5-344ae4f48b24 | 1.54713 | -56.00055 | 2025-10-25 05:08:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f109738-9161-3771-8b6e-a5d3f6c7e129 | -2.81664 | -49.14602 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6e705f1-f957-38fe-9f15-9eca366cf86e | 3.84391 | -51.77405 | 2025-10-25 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd02cfdc-27d1-3b55-b97f-50744b44a4c2 | 1.63561 | -55.74092 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c4385aef-c244-3de2-944d-84f164662c3e | 4.66541 | -60.5105 | 2025-10-25 05:08:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eea9bbe0-ec7f-3d78-ab3f-7c6a3f58da64 | -2.72269 | -48.34649 | 2025-10-25 05:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2197d745-45ab-36fa-9f7a-0951fcda184f | -2.72767 | -48.34719 | 2025-10-25 05:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f372ffd-445f-36cd-881f-b59636947dcf | -2.86514 | -52.79529 | 2025-10-25 05:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e5f1e28-30c1-3f08-b20e-7157ebcc9f74 | 0.47075 | -51.0041 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b21df7b-4b2d-3e68-a34c-eca1aa4471d2 | 2.08257 | -55.72651 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce9c1e8f-cddd-36b4-8147-e3d73cd08f4f | -3.58343 | -44.87998 | 2025-10-25 05:08:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60b1197f-5846-3f8e-99b4-408f9df339ae | -1.51459 | -55.86075 | 2025-10-25 05:08:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f21899c0-7104-37dc-89cf-5a22ed2c555c | -3.12189 | -51.20618 | 2025-10-25 05:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a5af164-72c2-3b96-bdd7-7071aa981647 | -2.80648 | -49.14951 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a9316a9c-f7d0-38a4-a489-9e5dcc677da7 | 0.44236 | -51.02934 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5cb532f0-cc82-36ce-b2e0-97dd072b6b6e | -1.49109 | -47.80905 | 2025-10-25 05:08:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bd0726f3-15c6-3411-8744-de0d2aee99de | 0.44788 | -51.01291 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b368152b-b6f4-3e49-af0f-ec119d28bd6c | -1.49614 | -47.80984 | 2025-10-25 05:08:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d211cf55-f7d1-357d-a94b-1be3a44719b2 | -2.22759 | -48.36849 | 2025-10-25 05:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3de2fcc8-5350-3cb8-8f3a-8b8ba3f32eb5 | -3.14848 | -50.16061 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68c639fb-02d2-38a8-b6ce-e07f33815810 | -2.15276 | -54.44465 | 2025-10-25 05:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 746910cb-a016-3df7-a649-f385bf362718 | -2.80404 | -49.13382 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| dd9134af-1b08-3935-96dd-b0cbe6191f95 | -2.8028 | -51.35836 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e2f430e-d94b-363a-8bf9-a953fa1271f9 | -2.85442 | -50.74083 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19746130-f4ae-3091-b643-e990c62b910a | 0.47469 | -51.00349 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63c77a8b-d9d7-33be-b9fa-de96300f9e82 | 1.64059 | -55.72964 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d4be8dd-2332-38a3-9a82-3e373bdda1db | -2.72755 | -49.16287 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 236f0691-bbee-3900-8bbe-83d056409ba9 | 1.64557 | -55.71836 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d01b382-d5d3-33ab-a470-f2d1041d43ae | -3.15732 | -49.17331 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25f97242-b869-3025-a153-ff0d7077e8f1 | -1.49064 | -47.81197 | 2025-10-25 05:08:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 982a95fb-1f0a-38e9-a12a-9ebf688caa9c | -3.19095 | -49.04232 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 478fab0f-e1d7-3f28-a502-7eafa83880f1 | 0.35779 | -50.92178 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66bf53cf-e2b9-33dd-9399-eab2767f2641 | -2.26905 | -47.85837 | 2025-10-25 05:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afc772ad-8b16-3a51-9f50-f09d6313dc83 | -3.09072 | -49.25402 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9fcbb7e-00b9-36b2-9983-e7c7f79f5a12 | 1.64281 | -55.72229 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa3a844a-0b17-318b-8ea8-cd98acaee1b7 | 1.56255 | -55.99114 | 2025-10-25 05:08:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0068b6e-f7da-3807-a857-b1513fa64d88 | -1.74219 | -55.25286 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a4f2943-29b9-36c9-ac41-3cc3655e17b4 | -2.15617 | -54.44517 | 2025-10-25 05:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f52149f3-7cee-37e0-b1cb-f3ac68e87c24 | -2.85383 | -50.74475 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dec4f620-99a6-3897-a47e-98e3628fb639 | -2.3012 | -48.56487 | 2025-10-25 05:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbfbc2f2-382b-3e36-a0e8-2343d2b62d6d | -1.30242 | -49.34317 | 2025-10-25 05:08:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49cd76ef-164c-3f62-a32b-67fdca18836c | -1.74551 | -55.25339 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 966eaa34-fbf2-3d40-a365-c90f27b8db26 | -2.81194 | -49.14524 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe882c98-b349-3d51-8276-4f21bfa6f721 | -2.58405 | -51.34315 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b5c5f43-8ac0-3077-ae6a-91f83d53cadb | -1.30138 | -49.34044 | 2025-10-25 05:08:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f04d2e8-3974-33f8-8238-2eaf13ded895 | -2.85501 | -50.7369 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad9eebd7-dac3-32cc-84a6-6a6285cdb9aa | -3.23812 | -48.75288 | 2025-10-25 05:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 814e55ca-cc6f-31bc-a850-17a73fafbce5 | -2.80253 | -49.14378 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c47110a1-42ff-3775-ba01-f31ed63dd574 | -3.10192 | -50.20176 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 498db8d6-a3fe-3b63-9c3c-f022578bb39f | -3.14142 | -50.61957 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c7eefce-cdc1-332e-9774-4a225ae3a30c | 0.36177 | -50.92116 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53eb6297-13a4-35e6-b6ac-8d21afb64001 | -2.8664 | -50.71863 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5673c278-0241-3cc2-819c-ddf0d795d8f6 | -3.11314 | -51.20854 | 2025-10-25 05:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ec505e1-868c-34c8-895d-5e249435c852 | 1.43038 | -50.89208 | 2025-10-25 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 429b9aa8-b51e-3bd2-8223-d71b69a8d1ef | -1.36786 | -53.02291 | 2025-10-25 05:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8018d9aa-58a9-3eb5-b091-b3d5e76a5b05 | 1.63615 | -55.74434 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e9883e29-3bf3-3577-894c-bbc7feadc016 | -3.12134 | -51.20985 | 2025-10-25 05:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34a589eb-f851-3e5f-aa91-9f98913ea5dc | -3.14344 | -50.16423 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bfbf84f-93b6-33c2-870d-3e5ea7c78cd4 | -2.89787 | -48.06328 | 2025-10-25 05:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1f446cc-0537-3534-831f-d41175342294 | -3.58011 | -44.87953 | 2025-10-25 05:08:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4cc54ed3-d29d-3807-8689-b83eae2d427e | -2.89779 | -49.16467 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 090d4979-19e4-33b0-9e41-1b318ba5b2ea | -1.77085 | -55.52747 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d9df558-1dc0-3ef0-a3c6-ffb593c4ebcc | -2.89703 | -49.1697 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9e84360-bd90-307c-bf18-abb6aa665f5d | -2.86277 | -50.71405 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d6b7ba3-f71b-3ec4-9315-f8acb6d360fe | -2.96305 | -49.57291 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b86edd4-a175-371a-8bc4-84cde1cc685b | -3.12273 | -49.10457 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e1af54e6-8e0a-3e69-925c-6fdbbe1ca618 | -1.5907 | -54.30812 | 2025-10-25 05:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5e9bcea-6a73-32f4-9a38-ef8ec6a0e435 | -3.22682 | -49.35212 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47b4be71-acf7-3ae7-a6b3-3fb3760e04f2 | 0.36443 | -50.92091 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README51.md)
