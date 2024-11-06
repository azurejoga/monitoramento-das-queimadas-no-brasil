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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd32359d-fd0b-329d-afb2-fa848d306645 | -3.14929 | -51.33519 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb64b8f3-e314-35da-baef-d702d3e11575 | -2.97248 | -53.87282 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1d90c0c-21d7-3e84-8b96-896c0271121b | -2.60946 | -48.32028 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e1ff995-280d-33d3-a72a-259d5665c0ba | -3.82146 | -46.46125 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d6466f6-9343-35fa-baa3-7f522924fb19 | -2.85546 | -51.77449 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| ca76d922-a9ef-38bf-88aa-2dfd9f8c193b | -2.88046 | -51.31584 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26374b22-aaed-326f-a053-8d2b3409eb42 | -3.2466 | -52.21375 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7358e94d-1ba8-3196-9cdf-892f8ea5d924 | -2.93186 | -47.86818 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef3fc805-eae5-3cba-8406-872cb77e59d8 | -3.24216 | -53.40331 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50d04d42-368a-359e-9b9a-e060ddfb542b | -2.81372 | -52.92337 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 45f0acca-35ea-31a8-9e82-5060c9df3ce0 | -5.00305 | -46.46894 | 2024-11-06 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f70f19b9-d6fb-3d4e-9af7-78946d82bee0 | -3.67135 | -50.22536 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 333bc178-3765-3d34-80c6-b6bd88da590f | -3.53735 | -47.3884 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| abc3b095-549d-38e6-a228-e74bd613b60a | -3.61798 | -52.2112 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c3bd95a-bf3e-3913-81c1-7997d8c030f5 | -3.09225 | -50.26447 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c57a17d-442f-38c7-aec1-4e29fe008abe | -3.12293 | -53.12239 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc8b70eb-20c2-3f31-b14a-ef06c75a8c1f | -3.21032 | -50.62952 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69265191-c0d2-3289-9188-b89c9932c3cd | -2.97193 | -53.26196 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d0d96bd-6b71-39c3-b94c-fe331d576ae0 | -3.274 | -50.35885 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4626fcf6-11d5-3a32-b09b-2064d2b1eb90 | -3.1769 | -50.59779 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18ef92ef-6b3f-34f8-9e83-6a26a5a63ff9 | -2.81603 | -52.93347 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b14aeed9-a149-374e-84ce-9d8e93d77852 | -5.40774 | -44.79892 | 2024-11-06 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf0e7279-5261-36ed-aad9-f7ea41776757 | -3.85401 | -46.61882 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d63ea2cf-d644-35a3-9020-808a27ab3691 | -4.49949 | -46.6354 | 2024-11-06 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a33e4e4-4ef5-341b-8add-ea379320b0a4 | -2.50005 | -49.0808 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9db6c4d-0629-31d7-9fb7-dad445e25d65 | -3.97025 | -48.1577 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a1e7f2b-c385-3fd7-926e-a3cc2daeebb0 | -2.67615 | -51.82363 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| eee58221-9012-30ed-aaea-3c7e3d895fa8 | -2.70649 | -46.67407 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 77b2fce5-a62d-38b7-82e1-a3aced21145f | -1.34694 | -51.4188 | 2024-11-06 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65e36923-bc7f-3ca5-af36-ace35f5b18d9 | -3.00963 | -54.08531 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09dc2950-6a7e-3cc4-a275-e0fab8b87060 | -3.82726 | -51.69352 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9a5b48e-8eb1-3e9b-8e4f-afa3c88dc7b0 | -3.77748 | -51.2996 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 457b87e3-46cb-330b-b0a0-0f0fbbddecb4 | -3.8865 | -52.28835 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d593895b-51b0-32e3-830e-284cb2d411bb | -2.39406 | -46.74413 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13e60e09-835b-3800-93c1-47212b163884 | -3.147 | -48.72834 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62b2ddbb-4fd2-3b06-b428-19368a0aaf5c | -3.17761 | -49.09598 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec4fc7fa-4518-35c2-b339-82149ec7b4e1 | -3.872 | -52.37764 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3f30115-8f65-35a9-ad37-08fa1f68e055 | -2.91266 | -48.59634 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13d85b84-cb29-354d-ab79-f804a9f41640 | -1.38891 | -52.18871 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ec3669be-1296-35a1-8824-cb419224bad3 | -3.04007 | -50.41969 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddb74b03-e587-36fc-95af-063d35a60cc0 | -2.82373 | -52.93462 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fc2fd900-dde5-3150-8e54-b407b060b845 | -0.04053 | -50.79299 | 2024-11-06 04:36:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00296ba6-8192-37de-8734-2f166a98d5a1 | -3.47717 | -50.38328 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b50696c8-e574-3dd2-9369-a9981bbe325d | -4.37492 | -48.58994 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af34df51-7783-3371-a221-fec4430ddc9d | -3.22542 | -50.3809 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f580d82a-34ad-39c4-ad4b-e38c9b8abd54 | -3.00491 | -54.08836 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| baf591cd-15b6-322d-bc9c-b81d91e0e62a | -4.11266 | -46.89211 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b98ee2da-0eaf-39a2-9337-3bb9b4b90d3e | -4.13234 | -48.87954 | 2024-11-06 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f56ddf9d-76b7-39e7-b68c-39d3c1974994 | -2.82474 | -48.46333 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6c62619-8973-374c-a393-2d25aa9ac34d | -3.62728 | -50.25184 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50fe4308-8248-3989-9b4d-485a7b7d8823 | -4.36243 | -48.64805 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f496a1e-0c3c-3ef6-8f23-680ce00ac6c6 | -2.78215 | -51.61173 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d315632-8e2e-3db9-bf37-9859eb8e6629 | -3.04016 | -49.53482 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80d551a9-43a1-36e9-ad52-511eb1a59f8e | -4.34476 | -48.63118 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d71f428-22d3-306f-9515-9c95a883cb65 | -2.8461 | -51.79631 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbf5b688-ee7a-3f36-b499-b8b1ea237c42 | -2.67254 | -51.82306 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cb794df6-9685-3a96-adf3-ba57fa282254 | -2.67415 | -51.83616 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6176fe1-879e-3da2-9cd3-0dcebc9fcd0f | -2.87468 | -51.30686 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6445f5d7-c43e-33ec-94f1-c3a5ec9aff80 | -3.96852 | -48.147 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0de2839c-2b60-3901-93a2-737ab7d3bbe2 | -3.67974 | -49.85368 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e7bc85c8-97d6-37c4-87b4-461c412ded90 | -2.57673 | -51.33486 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4a6829b-7b15-312f-92ee-f81c21d054f1 | -0.12261 | -51.39576 | 2024-11-06 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27aab9aa-8c6c-39a6-b7fe-7c3cc32f0d77 | -2.84826 | -51.77333 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9ff3ad70-90f5-3d5c-b633-8e54140361e3 | -4.13125 | -43.57722 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c450c94a-74d2-3a63-84ee-741baacfad8f | -3.47098 | -50.37859 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50a022f9-aef9-3110-9e04-802f67cb542f | -3.59079 | -50.26447 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddf382a5-0a29-35ba-a29c-7ee478efbab0 | -3.1742 | -46.61807 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f409010-15fe-3ccf-a16f-76e6534c10a5 | -2.80881 | -51.49187 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b605f919-b454-3a62-8277-1eedb1b88be9 | -2.62131 | -51.76519 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 185b6c30-05eb-399e-9ad3-5e657ee32880 | -2.4247 | -50.49741 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 7adcd4cf-95c8-3a19-8579-8dc415f58012 | -2.80461 | -51.49531 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b384ed33-79b6-3f90-b521-4204afef951d | -2.45032 | -49.03068 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 2e093d20-3ece-35e6-8ae0-d51d26846ca8 | -3.79918 | -51.41754 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1cea5946-0c7e-31f6-887d-68e5d8a05e5e | -2.91487 | -51.05441 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 65a59f76-2d49-34eb-82c3-d947f47b6f2d | -3.04212 | -53.27514 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73666305-7eb0-3228-9eb6-045aa682bb02 | -4.09595 | -51.10152 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be0660c4-8c79-3223-a28c-42b473d9512a | -2.60784 | -54.5429 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73285ccb-22ee-3ff0-a240-09d2306799c6 | -2.17925 | -48.37609 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 102e6038-e2f7-30f8-b998-8f37b0442589 | -2.34414 | -48.95058 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d001f331-16e6-3848-b263-cb2d0ba6283a | -3.10937 | -51.13071 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 126fd242-23be-3166-82cf-f95bb05ecdad | -3.32874 | -50.07714 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8c4cf276-095c-3e81-8581-d5b428bb78fc | -4.06386 | -48.254 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb4c14bd-df48-3d67-93e2-862a3c0be957 | -3.49752 | -52.94061 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd21cd44-1951-3652-919a-983d413e48c5 | -4.09776 | -48.31954 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c37cef6e-1dd8-342b-9d55-c53f3d984ed9 | -2.44682 | -48.94551 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5794b3ce-d7ba-3615-8e25-bed447030dc2 | -2.97505 | -51.02328 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3374451-7e00-3d48-9fc9-548e51231fc3 | -4.68352 | -45.80869 | 2024-11-06 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4320d0ae-f487-3900-bf88-faa47df066ea | -4.4491 | -50.69421 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baea0bc6-3cf3-3f9c-b44c-5bd42d4040fe | -2.83211 | -48.35187 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c995d18a-bf36-3bcd-b52f-6513f9a7d9f7 | -2.89849 | -49.33445 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5d03b25-0d03-3c24-9110-5ebecd8991cf | -4.07456 | -48.31599 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1506d3fa-d94b-3288-ad52-4c00becef345 | -4.60948 | -48.06704 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45dd1b57-7f7f-31a8-bdcf-cb9ae7f2a9e5 | -4.56099 | -48.00577 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e0e5fa09-52cb-3e43-b20b-52c51ebbc3ff | -2.43417 | -53.92702 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4252ed66-924d-3b0e-8e4f-df96f25fbc25 | -2.51595 | -49.19685 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b9561ed-2ea6-3dbe-b7f8-03e7cef9047d | -4.06848 | -48.31149 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aabad204-d8f4-3162-b1ff-263923b84e32 | -2.49517 | -49.11184 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2527d2f-cd12-3e71-bad2-482cba7a7f28 | -2.36446 | -48.92907 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b460a693-ae17-3662-868b-0243f34a2de3 | -3.97573 | -48.14431 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec42ae8b-d422-3b66-929d-2f5b1ba11337 | -2.91735 | -49.34486 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README38.md)
