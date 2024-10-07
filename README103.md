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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7417a90-e1e2-37c9-907b-352008c4d961 | -16.92425 | -57.69339 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| b7b6607a-e658-333a-9fc0-e841287c559b | -16.92144 | -57.68869 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 29437eb0-78db-3299-ad22-feda8b65cb18 | -16.92075 | -57.69275 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4e4257ba-e124-31d9-9d8c-a8ebb5f0c76d | -16.91795 | -57.68806 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| f15ea26e-6305-3115-8db9-cb076111e8a6 | -16.91445 | -57.68742 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cb412b6a-5d02-3067-bf92-dfd0dcf26559 | -16.91027 | -57.69084 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| cf8add72-f5e4-30c2-8d9f-ed5e3e304a85 | -16.89634 | -57.73019 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b3d77a4e-9bb6-3efe-9dd7-48759b3f381f | -16.89278 | -57.68766 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6ff06417-431b-3d86-a5da-a17508e5d7c2 | -16.88999 | -57.68296 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 884c5f70-d58a-3cc6-83e2-fccc79a3ebba | -16.87811 | -57.68916 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 89438f9b-f385-3f84-9d53-cf1517fa39e0 | -16.87741 | -57.69322 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 14026d25-4d1d-3a67-94fb-4a6f4c2c5928 | -16.82347 | -57.3706 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| fd10edc5-ba06-3c8a-9f6f-235d2a885365 | -16.8228 | -57.37455 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 97dbc583-fcad-335d-af36-c7bbaa2d4001 | -16.82212 | -57.37851 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 9d13794b-97f2-38b6-9687-f3c4bb0ad533 | -16.82078 | -57.38643 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 50511a80-e1e2-32ce-acf7-d510bd95cb16 | -16.82069 | -57.36602 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 585657fa-95e2-3071-a80d-e7c3bf6d9ae2 | -16.82001 | -57.36998 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 75cf4cac-b5c8-3213-a4e7-fc6ad017418c | -16.81934 | -57.37393 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 603d3791-1007-3104-aa50-4268fbdb4ae0 | -16.81867 | -57.37788 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| ab40ba06-8c5c-32d1-be8e-e5dc97e42a47 | -16.818 | -57.38184 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 80e7834b-58b8-3337-828c-429caf7dd995 | -16.81732 | -57.3858 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| c2ecbcab-4ee1-3614-8d94-501b3ed9287d | -16.81723 | -57.3654 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0afd6ea7-dade-32ed-88ab-6a813d3d5a71 | -16.81665 | -57.38976 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 2f220bdf-54db-325d-8064-a129c442514c | -16.81597 | -57.39372 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 908bf501-223e-3fce-834f-3c72fe4e5c61 | -16.8153 | -57.39767 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 1a3516c7-eb64-38af-969b-de199541f454 | -16.81521 | -57.37726 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 52a42ae8-93ea-32a8-ab54-33720b3fa362 | -16.81454 | -57.38122 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 2bbf5f14-2f83-3c53-bd1f-1b080dce7732 | -16.81386 | -57.38517 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c51194b4-7a84-3d7c-ae37-01a8c14c33ae | -16.81319 | -57.38913 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9dd52035-5d4a-34e5-9fea-c2d39540ccbc | -16.81251 | -57.39309 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| afbffdec-d6fa-3cc3-b5d7-fd8adb543e6f | -16.80973 | -57.38851 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b5047a02-0c49-3a61-8e06-9772687e6cd5 | -16.8077 | -57.40038 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 112b8090-d183-3578-9cc3-191c45ccbfad | -16.80703 | -57.40435 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 8c5431b2-c9b7-3ebe-bdf6-e9fffffbd274 | -16.80357 | -57.40372 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 3a0ed61e-c8c1-385f-930d-59be59bb67f4 | -16.80197 | -57.40028 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 0d3dd541-5cbc-3b06-b7d6-579d8ac49957 | -16.79851 | -57.39966 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 9023abb3-276a-3258-bab3-8d60c2247fa7 | -16.79785 | -57.40363 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 48db8cd2-11a2-3d1b-88f8-50e49888fe84 | -16.79572 | -57.39506 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c12911f3-823c-3c1a-afc7-2df8b6be7025 | -16.79505 | -57.39903 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 122cc0f6-9404-3a59-b45e-69bc563bc89b | -16.79226 | -57.39444 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 348eae0f-9ea3-3517-9c29-55f0086cb421 | -16.79027 | -57.40635 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 2ab341a1-b4f9-3ae7-92f4-b4ed5335e35d | -16.7888 | -57.39381 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d073f76c-ec46-3a56-abc0-815beb9dbd16 | -16.78747 | -57.40175 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 9d4f1815-fa75-3d27-befd-f8bf897dc063 | -16.78681 | -57.40572 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 5454c82a-f1b6-382f-917f-ef7c94163e4b | -16.78614 | -57.40969 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a73d0418-8148-3e45-93c6-af4d0424bcae | -16.78548 | -57.41365 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c6ac26bd-63e9-3412-acea-266861545d71 | -16.78334 | -57.4051 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 5aef8fca-f7e5-3442-b075-4de470b021db | -16.78268 | -57.40907 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 6d54f66e-cc10-3905-ba30-a7c4b06b31da | -16.78201 | -57.41303 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f796ff5b-f4e7-3c57-aa13-468309e9181e | -17.15579 | -56.75415 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1f48fbca-7c71-34f1-b82c-6ecf2278cf46 | -17.15517 | -56.75792 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f6609ab7-88b4-33cc-944d-a61a110c9cbf | -17.15454 | -56.7617 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b6c6e45e-9012-3e9f-bea1-0f9a044187fe | -17.15304 | -56.74978 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.7 |
| 73ad5155-1f84-3cd8-8dec-62534ba79924 | -17.15241 | -56.75355 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| bf7f263d-8056-3617-b486-f88a8851b8bc | -17.15116 | -56.7611 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0f47d14b-a417-395a-9a97-2c18cc8f271d | -17.14966 | -56.74918 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.7 |
| fb62b716-5b21-3d17-8f68-3bcd7fe3ed13 | -17.14628 | -56.74858 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 499b8c8e-b165-3e5a-8293-070fa0b9a143 | -17.14314 | -56.76745 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 41c854d3-b167-3465-97e9-25c29c474d56 | -17.14291 | -56.74798 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 84e9d7b9-aa55-3a05-b67d-80160320aeeb | -17.14252 | -56.77122 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e3b02b87-995d-399f-abc8-2c45f17f026b | -17.13976 | -56.76685 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fb233729-1683-3175-b433-9e8a8e633a38 | -17.13914 | -56.77062 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 31a99dd9-a0ca-3d1b-93b4-5dabbbda2719 | -17.13639 | -56.76625 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fc5e8a41-d662-3973-9f32-71626627a76e | -17.13576 | -56.77002 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a399c1b4-2a3e-3f3b-a1fd-cc911a1de2b9 | -17.13238 | -56.76942 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 26dd09d4-60bd-36c7-867f-56c208b1ce2c | -17.12986 | -56.78453 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 36467227-fcf6-3266-bb42-53046227c7ca | -17.129 | -56.76882 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 52a4ff9b-950a-336a-b114-a906a98cd0d4 | -17.12876 | -56.74157 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d73b5307-cb80-396c-b2e3-cfd910d8e1b5 | -17.1271 | -56.78015 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 16d227a4-89c2-3f8f-8ea4-4a7a4e35ecf7 | -17.1267 | -56.80344 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.0 |
| 1f41990b-439c-3429-abce-11a40f164397 | -17.12647 | -56.78392 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 5c292b1f-0ace-3e2f-980c-1aa89c7c48a9 | -17.12625 | -56.76445 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 95004ec1-4a4d-3f63-a48d-3ab0bfcfb177 | -17.12584 | -56.7877 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 027af126-165d-3095-a712-b11a57cc9dcd | -17.12561 | -56.76822 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 025a0add-8b97-3b47-9d4e-9d9efd50a82c | -17.12521 | -56.79148 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 4b571cf9-622f-3432-bf06-c09d80d50a3d | -17.12506 | -56.76422 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8c699799-ec34-38d3-8230-8f995ee6fc1c | -17.12458 | -56.79527 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e0eba303-a583-301b-b316-1a826bb6f4d9 | -17.12444 | -56.76799 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0e52ba6f-8375-3845-9b53-ecea671381de | -17.12436 | -56.77577 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 03237be9-abdb-34b1-85ab-914e16fc0616 | -17.12395 | -56.79905 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a988c898-2f29-33a1-a73f-863ca7d26885 | -17.12382 | -56.77177 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 7ca29233-b939-3c84-9e77-7720e053193b | -17.12372 | -56.77955 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 9967ee2d-86af-378d-850b-7c1ef08dcbed | -17.12332 | -56.80283 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 3e9b9872-2d5a-3185-95f7-233f0c6ad3e9 | -17.1232 | -56.77555 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 206026e0-fb15-36e9-a4cb-336e002c6009 | -17.12309 | -56.78333 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d1dfb21f-442b-35d0-8a3e-3f06da40f8ca | -17.12258 | -56.77933 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 89d19bed-3d0d-3beb-a27f-4b5ac5cc5dab | -17.1212 | -56.79467 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| dee09011-d8f8-3d50-bd9c-0b03271f6f67 | -17.12106 | -56.76739 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f384e2c4-2a7b-3b5a-981e-060212621700 | -17.12057 | -56.79845 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 072a9c25-4dd5-34cc-afef-2dc624d6cf23 | -17.12044 | -56.77117 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 65491080-eb06-3e3f-adf6-46595331720e | -17.1201 | -56.79446 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6b599bd8-e0d2-3a4e-b931-084d7731bc4b | -17.11993 | -56.80223 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 5b05a55f-24dc-3fdb-ada3-5104022f0b10 | -17.11948 | -56.79825 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| db3b98d5-182b-391b-aecb-4ff804b1cfa8 | -17.11886 | -56.80204 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| fbc3d930-0f71-3baf-b8b3-6ffc105390a3 | -17.11671 | -56.79386 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 34b75e4d-7053-302f-bf94-d0ae18d4b5f2 | -17.11615 | -56.75486 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4affda6f-1c56-3408-a2a5-a2ab908add4c | -17.11609 | -56.79764 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e469255b-d017-3e10-8d3a-7d1804b960ba | -16.82374 | -57.4319 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8c8eecbc-2657-3abf-a376-16027218cbce | -16.82096 | -57.4273 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.4 |
| 3a0eeee5-6b03-341e-88bf-a57d2995cf3a | -16.82028 | -57.43128 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.4 |


[Clique aqui para ver as próximas entradas](README104.md)
