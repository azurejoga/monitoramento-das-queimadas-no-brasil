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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd14ec49-996a-3b08-a7f9-bca5e5f75863 | -1.8799 | -52.65845 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b947473-c25d-3d7d-b231-56a1c9e936f4 | -1.08844 | -54.03856 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 876a4c27-0bc3-3279-9e03-95f107cb3338 | -1.88339 | -53.31962 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d98cda2a-ebf0-33ee-aa8f-472a75f73a5c | -1.08994 | -53.38194 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a51561d-cb0e-3559-b840-e5261b44e3f1 | -2.87436 | -46.85072 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b586ad13-3e6d-3041-850f-64281b9624af | -2.86317 | -46.8714 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b59a6c9f-a505-3e05-b523-fb5207b27fdc | -1.60795 | -52.27973 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 815c88cc-ccf7-3092-9b72-d1a9f4be625f | -1.46295 | -52.69342 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c8ec6e-a970-3d35-9f84-85bf7cf10f50 | -2.86735 | -46.85485 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d57d0ea8-2b8b-3947-84a5-984b8175f92c | -0.99961 | -51.72892 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3fe9390-35bc-39ee-9316-e685af0482e2 | -1.20077 | -53.8893 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb3891ea-5cb7-36e0-906f-e9692688ebe8 | -1.30299 | -51.92532 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6446067d-71cf-3465-8f9c-d5a1ce3a551d | -0.99215 | -51.71912 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cbe4040-2b5a-3911-8657-4d87e3233faa | -1.20152 | -53.88446 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 36809f4c-fd59-3a0f-bff9-135e8ddffc67 | -1.58668 | -52.27644 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 8dae1b40-26e7-376b-bacb-dcfb392a0344 | -1.56725 | -55.78609 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db050bb6-18c1-3fba-874b-6a59149c7aca | -1.06418 | -53.20813 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b238c91-ce8a-3c74-859d-fb7388ad0d94 | -0.95322 | -51.6499 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31db750b-43f4-3f4e-a5bb-a735f67f6ed4 | -1.08316 | -53.63947 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 643152bb-f1c9-3dfb-a4fb-b530152657c0 | -0.5868 | -51.71474 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ba842ca-6245-3b49-81bc-b19339730c6c | -1.60369 | -52.27908 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fa86278-af5d-3e6a-8edc-a811572e23d8 | -1.65982 | -55.23477 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6b307d8-dc0b-3ed0-bb9e-81793068e35d | -1.80143 | -52.7436 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6d2a1e8e-4ca5-3a0f-9076-ad120f5991ed | -1.64389 | -52.46816 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3a0a5c33-c274-37fa-b930-cede132b515a | 0.17041 | -51.22465 | 2024-11-28 05:16:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d0f714d1-3db3-3ca8-a774-e3af2cda2bf3 | -2.47503 | -47.04203 | 2024-11-28 05:16:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e116b98-c7a8-3dae-8d53-295433226ee9 | -1.62229 | -52.46875 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f09d6d9-7088-3fe4-97c9-9e540f89af57 | -1.08833 | -53.36646 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5c41650-af90-3c46-9d67-de361244f79b | -1.64027 | -52.46364 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fd2affc2-89ae-3db4-a9da-608cec77af5e | -1.27451 | -52.16665 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 955c15b3-7ee8-33c7-945d-dbde02487330 | -1.60447 | -55.38195 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a6b87bb-2154-33ef-9c15-c1f6d9497c67 | -1.63078 | -52.4977 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e908fdc-e28a-32a3-9895-ec88b9e87ab5 | -1.6831 | -52.49763 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81c51493-3f95-3281-95f6-b3cabafdcf4f | -2.59997 | -46.83285 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 415ea0fa-fd45-3411-8475-5babd5cd9146 | -1.27086 | -52.16202 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb78d389-234d-391c-8adb-5fc085a876ba | -1.6751 | -52.43332 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4935a87a-644a-3384-a7b9-e6a2523949fc | -1.69408 | -52.62442 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33d2a9e7-64ea-354d-b239-d86932710c9f | -2.15644 | -48.71117 | 2024-11-28 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c700fc48-1c75-3401-aae2-dc955df45c33 | 1.47878 | -56.04728 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fead0631-cb52-3c42-8fc2-39da78cddee0 | -1.58304 | -52.2718 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| da5a5f93-d85a-34cc-a6bb-279159bd7bfd | -2.83953 | -46.8701 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 51475dc8-96ac-3ac8-962c-1630afc12e15 | 0.33716 | -51.07364 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 38b9d102-8d8d-3ebe-8da9-77c67a0f7d9d | 1.31053 | -60.41273 | 2024-11-28 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17d9672f-57d4-3491-a1ee-b04f784be32f | 0.6098 | -51.965 | 2024-11-28 05:16:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7abb1443-1300-3af0-86d1-60358eb38f83 | 1.44278 | -55.91777 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5bc7bdca-370e-397e-acec-f3f0af599481 | -1.28957 | -53.01539 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66de4a1a-76bc-34a6-87cc-639d9050c09a | -1.65627 | -55.23421 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dac45149-e9b7-3335-bb99-0aee1b9063b7 | 1.25773 | -55.98284 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0b0ddb4-5871-3807-b77f-15029e915655 | -1.04358 | -52.42406 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93558993-c568-3ff1-85c3-6359de19069d | -1.64514 | -52.73582 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 341c0c60-d0a3-3dd1-812e-9ee2e33db79a | -1.19549 | -53.89831 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc5ef94d-c793-3361-ae8e-fb95f4bb5662 | -1.15188 | -53.68074 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea93106b-0733-3cb1-972e-7136d2eec408 | -1.0639 | -53.01048 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3835c8ab-4d99-3128-b0db-2a3185972935 | -2.85561 | -46.83498 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4b193b6-d6a2-3d33-a49e-6b568f0c29d4 | -1.60094 | -55.38139 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c1eb52e-c82d-3c16-97d5-c76c57354cc0 | -2.00691 | -51.16773 | 2024-11-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa98fa36-e4e4-3a5c-a2f9-d9bf8111eb9c | -1.52437 | -54.41098 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c59501d-e723-3a40-9631-7a6fc8561932 | -1.10403 | -53.39462 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8dbbabc1-3cf8-3a63-9791-5039983e2a79 | -1.69825 | -52.62507 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5ab4c25-9bd2-300d-8e57-0fbcfacc1088 | -1.66641 | -52.72387 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f9669147-286d-391b-ab12-9e1ca9b3ce85 | -1.73149 | -52.04025 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e08c76d4-e155-33b5-aff5-91fccedbe6b3 | -2.59924 | -46.83779 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b711ff94-42fc-3db8-865b-51b1577071c3 | -2.85696 | -46.87024 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a73fe731-4340-35ad-be91-9b5a7ffb6b95 | -2.10989 | -47.89322 | 2024-11-28 05:16:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16614d56-f794-31de-a39e-c48e7deb4944 | -0.95292 | -51.65198 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27270d1a-1da6-34c4-87a8-fb45740b6ade | -1.37146 | -53.61365 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d41cfde2-2bc2-3617-a25f-f267a73d7f86 | -1.36483 | -51.96685 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2262e0b2-889a-388d-99fa-28a4d3e9c305 | -1.58365 | -52.26784 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9927e7c3-7a86-30e8-a44c-6d92b699a3f7 | -2.8597 | -46.85106 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e98ccbd-8c3e-39fc-bdf3-3da0bf83c8ad | -1.33272 | -51.93415 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 54207bd9-2f2c-3b14-b4f8-be899ca4dcb2 | -0.88435 | -51.71735 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4acce4d7-49be-3b5a-8b90-5e530effed09 | -1.37212 | -52.55011 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60dfaff6-52f7-3f74-a795-e1dcb53ad163 | -1.6456 | -52.11098 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5ad44b63-f33d-3f80-b4c0-93fdfa623d56 | -1.04604 | -52.41644 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dd93175-bf6c-3a4f-b9de-174aacefb9fc | -1.44663 | -47.11893 | 2024-11-28 05:16:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dfb7841-8098-3c25-9e8f-645e7702e7bf | -2.86184 | -46.84905 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df3e6de3-4426-3faf-9a6b-7cda3059ba56 | -1.77338 | -52.70478 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94ec6c57-93c4-3d82-bd8f-6254949d109a | 0.17173 | -51.2261 | 2024-11-28 05:16:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c308802-1aba-34c1-a952-912a320d3d4c | -1.89431 | -53.28991 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 352eabe5-4f48-3531-8211-d2d66b556b8f | -2.8494 | -46.84679 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4156aa42-1871-3381-b101-2d495fb89221 | -1.06218 | -52.42287 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f8b9af3-1860-383f-a6c0-dbac92d13271 | -1.71959 | -52.48356 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e217eae7-2142-337c-a948-e95f2e8ff63f | -1.50149 | -54.46191 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a1261461-ad47-3f70-ae63-4cc07e9f766f | -1.48849 | -52.52401 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8087a9ad-d1c0-3e31-9e88-c23d9cfc17db | -0.97566 | -53.68598 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ac9e2734-e784-33ee-a5c8-0dafb85a33aa | -0.99653 | -51.7198 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3194a6a0-ff51-312f-8d62-7fcbaa2eee9c | -0.95732 | -51.65268 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 949f0ea7-74b0-3b34-94f8-237d96d72ac0 | -2.87364 | -46.84296 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8695c04-be86-3702-8f9e-5cd4afa5cf3b | -1.68951 | -52.47918 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4677f92d-dd1a-3f0a-83a7-722a0535e87e | -1.07087 | -53.64237 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 658f89e1-e30d-3c5c-9a85-620335343ec4 | -2.86864 | -46.87768 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb69b46d-01da-3022-87bf-61f1a2878f43 | -1.33447 | -51.95134 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d6659da4-0890-38d8-94c0-94a79dd2e10e | 4.25822 | -59.9886 | 2024-11-28 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05f502d6-5823-3099-8fa9-511f9fd64f24 | -1.04547 | -52.42026 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a47bf51-d264-3815-850e-e4df92abed85 | -0.98713 | -51.72264 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00e6cb79-c1da-335e-a30c-aad107da12ca | -1.08565 | -53.63797 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60a84d79-9c41-38d5-a39e-fad7fd1dcf55 | -1.15959 | -53.68194 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daa98f07-2e02-3f92-bbf1-a74b8ef14934 | -1.47099 | -52.35264 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea756532-aed6-347f-99c7-0790daff626d | 0.9841 | -50.25914 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0085f2d9-1070-374b-96a6-902f64e28536 | -1.27024 | -52.166 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README78.md)
