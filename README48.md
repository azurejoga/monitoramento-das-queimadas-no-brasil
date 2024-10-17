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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5edd6150-5ef6-3b8b-ba1c-57c014db79fd | -17.1677 | -56.83586 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e3aa5142-062a-3f4a-953e-fb5e28d844ba | -17.16714 | -56.83959 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cf1831d3-db76-3d69-8335-969925e7d8a3 | -17.16658 | -56.84333 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4c2a6c67-7234-373a-9eb3-4bd2bb56d0f7 | -17.16601 | -56.8241 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c7ed77d6-2d46-3d2c-8c1a-61f2619d4d73 | -17.16545 | -56.82784 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3216f581-23e9-3968-a701-26ef7ad9ecb6 | -17.16265 | -56.84651 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8f36b94f-8bec-3de7-855d-70d8cdce074e | -17.16208 | -56.82729 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 78fda658-7ea2-32cf-a352-6e218be461a9 | -17.15928 | -56.84597 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8586fb33-2d41-3b6b-83a5-463fbecadeb8 | -17.15872 | -56.8497 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b5ced12f-520a-3c77-b017-bfae28fff32c | -17.15872 | -56.82675 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b2d409e5-9618-3984-bfbb-7d15ca15f6c8 | -17.15816 | -56.83049 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 63ea6542-d445-3865-9c1a-7fd7a97ab4d1 | -17.1548 | -56.85289 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a60b8368-8bd4-333e-b044-33e3e4778fde | -17.15424 | -56.85662 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 78f052ba-7c0c-3d07-8610-e6e3f35e2833 | -17.15032 | -56.8598 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 04e4b2b5-c66c-3d86-a921-0cd2c075b83c | -17.10998 | -56.87615 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8fb37edb-221d-3a69-a7dd-f556827199fd | -17.06161 | -56.86507 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 20421a50-cf02-3a4b-877b-445b909ac465 | -17.02966 | -56.84844 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0f14f4a2-6ac3-3b1c-9c0f-fb4257b6eb27 | -17.02519 | -56.85534 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3197ddb8-258a-3e34-b5bc-c8cbcc956f7c | -17.02183 | -56.85479 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5c49f59e-7043-378f-b3e2-89f0151975dd | -17.01566 | -56.84997 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 76562011-035f-368b-aab6-2c431e25a38e | -17.0151 | -56.85369 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f09403c9-4f10-37b7-98b9-b8bdd4be8f01 | -16.97384 | -56.81725 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 245958b4-15ed-3005-ae3b-60f2a6e14907 | -16.97327 | -56.82097 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4ddabcf0-afd9-3c39-8aa3-dcca7b192af1 | -16.97047 | -56.8167 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 49ccb365-d753-30cc-8b5f-852622b5125c | -16.96991 | -56.82043 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0208bc7a-87d0-3e33-a181-e0acefc4265d | -16.96655 | -56.81988 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f6b22334-b0d4-37fe-8f7e-b146e7a8052f | -16.96094 | -56.78843 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 70a3be2b-8efc-3604-bd93-1024a6c60f8c | -16.95645 | -56.79534 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e27b9497-b42c-37ff-b8c1-bfb213a8fb14 | -16.95589 | -56.79907 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 66387e0f-bbbd-3d83-9173-f26a058b775c | -16.95533 | -56.8028 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 49d27fd8-3ab7-3cbe-b2b1-d8b213e981ee | -16.95309 | -56.7948 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| eca6e234-dad6-3ad0-93e3-680cb6b938c9 | -16.95253 | -56.79852 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0dc13eca-18f6-3894-82a4-b4e62b09d6af | -16.94972 | -56.79425 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 12c64876-7ffa-3138-bf71-8b1e90e6bfcb | -16.94916 | -56.79798 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 42aaad9e-e01b-3343-b87a-b5228cd877cb | -16.89031 | -56.74249 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 11177a03-3931-3462-ad9f-d1f3f28927f7 | -16.8875 | -56.73821 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e209b482-8057-3a17-b3d5-be9f3aa5cfba | -16.88694 | -56.74195 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1be7a045-c069-35fd-85b6-f08d43c753a8 | -16.88357 | -56.7414 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cdbd4bd1-56da-38d2-bf3d-2831057006e9 | -16.83916 | -56.66911 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 6bd5472c-2c40-398f-96ec-ff1b753395c4 | -16.8386 | -56.67285 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 368327bb-7ef6-3df0-8069-c483b85d0e33 | -16.83693 | -56.68409 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a9d9a72e-92df-3cb5-ba9c-5dedb7ec4ea0 | -16.83637 | -56.68784 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2e4eca60-9b23-3624-b679-83fb9e8bef4a | -16.73351 | -56.69492 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 78cdf3d0-8916-3875-bd8d-a0e969a740bd | -17.91051 | -57.44828 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| a1ef02cb-b88e-33ab-9512-49d03a41c7d1 | -17.90995 | -57.45196 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 361955fc-c056-31b7-bfce-a049cd203308 | -17.90661 | -57.4514 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e5e5c240-c65f-3e23-abff-5f556a9d1995 | -17.90383 | -57.44717 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 56d5074d-6636-3ef3-a3b3-c7152caa9107 | -17.90328 | -57.45085 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 4055598b-cf46-332b-80c0-a5ded7941627 | -17.89994 | -57.4503 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 75a00ec5-1086-3f11-abea-efc756c5584f | -17.89644 | -57.25348 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7eb147b2-8304-35ef-82b3-a5fd155f3474 | -17.89087 | -57.24496 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ed18b629-f7d6-3b39-830d-9e6130d0309b | -17.88752 | -57.24441 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f11f4135-424f-37e7-8c2c-86a8a114fe73 | -17.88696 | -57.24812 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3efd138e-ea33-3df4-aefc-47c31bc956eb | -17.88474 | -57.24016 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 294adea9-02ec-302d-ba95-0532d4bbe48b | -17.88418 | -57.24386 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b178b0d9-1068-375c-ac14-8b4152390ef2 | -17.88361 | -57.24757 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cc59e525-36d1-3771-9c77-fa9e80c0d3fb | -17.88139 | -57.2396 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8c700a8b-4962-3b38-9ca7-fca48b0a8c41 | -17.88083 | -57.24331 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6886dbc8-cc5a-348d-b0b8-b1ff2b62fa62 | -17.88027 | -57.24702 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b867ffac-371c-36ab-8ffa-5474af877bde | -17.87748 | -57.24276 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 06d9ceca-91dc-3de3-80d7-2fa02516ba12 | -17.87469 | -57.2385 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e8666c04-4949-3591-b28d-797934036ce0 | -17.87413 | -57.24221 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2825524d-91b7-3f68-8c2c-675257915f3b | -17.87357 | -57.24591 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 921359fe-fdc2-358d-a59c-fc9eb44ef306 | -17.87301 | -57.24962 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f15c0c14-3f30-3d4c-8105-1a15c75ee13b | -17.87022 | -57.24537 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 98866910-9f92-328a-9ac0-2b0402350c55 | -17.86966 | -57.24907 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0859b7ce-b322-3151-9c94-f1f93e5e7bb0 | -17.86632 | -57.24852 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4973cdbb-dc50-38f6-b538-10e04c645bb9 | -17.86576 | -57.25222 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 191b1048-1925-3ead-9eb8-676cc3e20ec0 | -17.86241 | -57.25167 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9718937e-e55a-3dee-a673-969a232fd9ca | -17.86185 | -57.25537 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 35c49003-ff13-34b3-8630-a2b51ec37f3f | -17.86129 | -57.25908 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e3e118d2-ca0a-3222-9412-60b43ad08bba | -17.86073 | -57.26278 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 60e8c74b-549a-3679-b4c8-cf5d2a2693d5 | -17.81501 | -57.29316 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7e6face6-21b3-3ab5-b74b-9334f67480b1 | -17.89661 | -57.44975 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 91dea8b8-efea-3479-befa-8918fffe5302 | -17.89605 | -57.45342 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 8eed8a2b-96fa-3fcf-b071-35c9d6ecbc5d | -17.89327 | -57.44919 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bc6852c7-62bb-3e7f-8979-7addc6d69618 | -17.89272 | -57.45287 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b2782fd1-8fed-379d-a040-eb2d93ef5dd7 | -17.88938 | -57.45231 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| fc0f53ce-38d1-3b7b-8bf7-b5e68a435f25 | -17.82448 | -57.41186 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 32f41b55-e867-328b-88b8-4330b13dad1c | -17.82114 | -57.4113 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 67594f9b-f6d3-3771-b6b5-7e5a85a9d73b | -17.8178 | -57.41075 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 52cccab5-39ed-3098-9820-b374469e2fd6 | -17.81447 | -57.4102 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| efdc47d2-d3e1-3057-b054-3da27422be06 | -17.80724 | -57.41277 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 026a7bd3-f4f7-3553-8b89-a64191b1d803 | -17.80668 | -57.41644 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 15862d76-f06d-36cf-b525-e70515909079 | -17.80334 | -57.4385 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3f56dd2e-2be0-3725-8c3d-ca979d051343 | -17.80279 | -57.44218 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9a3caffa-0131-34e1-84e4-283432f2318c | -17.80163 | -57.29095 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 56dd5ce9-fe53-3752-92b9-2263b9308b23 | -17.80057 | -57.43427 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| a17f7957-8b08-3edf-8978-754056868441 | -17.80001 | -57.43795 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 34c055fa-eb18-3bb0-ab11-c1f667733212 | -17.79945 | -57.44162 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7abc1ee5-ed81-367b-97fa-e6498dc4a1a1 | -17.79889 | -57.4453 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5f35ed95-129c-3359-bb1d-057b3283dda3 | -17.79834 | -57.44897 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 643626df-0120-3571-9f77-f67f0625e02f | -17.79778 | -57.45264 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 860fc14e-d1a4-3226-a25a-fdda61c6effa | -17.79723 | -57.45632 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e32b125e-cbf8-3d10-a9ba-81af3c00b6b4 | -17.79667 | -57.4374 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fea166ce-0895-3069-97b9-0851eb24f442 | -17.79612 | -57.44107 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 913b152f-c90e-3566-be2f-c6037d5fd391 | -17.79556 | -57.44474 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1566297e-2db0-3d98-8017-20d2430ddba4 | -17.79501 | -57.44841 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f1acec3c-0c32-35c5-a2c6-078d1908bc9a | -17.79445 | -57.45209 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8b2e16ca-8f3e-38f3-8b06-574bc00474ee | -17.74232 | -57.12167 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README49.md)
