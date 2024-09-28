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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c5e1d15-d875-3082-b64f-9bf4efbee017 | -6.13115 | -51.25421 | 2024-09-28 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a30d6e3-0200-397a-81f2-f5d62a5cfc79 | -5.70817 | -51.33525 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1856e780-6abb-3bf0-bde6-66cb080c834e | -5.70738 | -51.33985 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49a47328-49ef-3bd1-903d-6ae3519b26c6 | -5.7068 | -51.33691 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00602cdf-da84-38cd-94f6-edf8f2585e2c | -5.62463 | -51.38065 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90cbdcdf-9ae9-358e-a7a8-02a4fb09e8a5 | -5.41376 | -51.1548 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca6bd64c-e6c9-3798-bfc5-90949885c68a | -5.41147 | -51.15642 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fb2be473-00e4-3660-b22a-632e380bf5bb | -5.40926 | -51.15404 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4c8d3b7-9a5d-317e-a8a0-3777fd8bc8a3 | -5.3054 | -51.45492 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7409e668-7b1c-33cc-9bef-f0e340645046 | -5.3016 | -51.44941 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd243711-8dc3-3df5-b62f-ccc46d502bfd | -2.07349 | -52.01804 | 2024-09-28 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a96e2821-3bd7-3f8e-a87a-007a7e280cec | -2.06843 | -52.01727 | 2024-09-28 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76996bd4-d243-3f04-a7bb-54add81e790f | -1.62228 | -52.57057 | 2024-09-28 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca06edac-8934-3943-ae13-92d92c5ab605 | -1.62177 | -52.57384 | 2024-09-28 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 453dfcf0-4815-315b-8d19-6b09ceea12b5 | -1.62149 | -52.57123 | 2024-09-28 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 78a06911-49ae-3061-923a-afb96bd632d7 | -3.313 | -53.36975 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7850dc5-e86a-3325-8d92-f738fd3651d8 | -3.30702 | -53.37225 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7be23089-54dc-3839-851e-2a32291b959e | -3.30429 | -53.69746 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec7b8bad-154c-386b-b14d-9cab3441b3e7 | -3.30364 | -53.70128 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43a7fadf-eb2c-397c-bba7-b9cfe0a622a1 | -3.29874 | -53.69654 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8af5a8e0-f425-3c50-95a4-2a7effbdf595 | -3.29811 | -53.70026 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a58c46e1-f477-3598-976d-c4c92de565f2 | -3.29749 | -53.70398 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c94cfb89-ecbd-3ec9-8b74-92340237f026 | -3.21259 | -53.39451 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a8f3e9e5-e56a-34a8-8f93-42d207d544b2 | -3.21203 | -53.39793 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e010070d-2329-3f25-9fca-efd2bc1f9444 | -3.20877 | -53.39229 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6eed4fc6-5a5f-3b9f-8308-19cea7399ff1 | -3.20819 | -53.39572 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 91fd459a-4ac7-3e56-afdb-a6b9474a1e53 | -3.2076 | -53.39916 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6073ebbe-7364-3e3b-9ad2-e3d3be62e678 | -3.20716 | -53.39351 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 97619f07-1a93-3b5a-9fd3-d64fdef7a1e6 | -3.2066 | -53.39695 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b04ce34a-7190-3791-9aac-ec6673dee07c | -3.20335 | -53.3913 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c7cce9f7-7443-3747-bd22-478be30b10ab | -3.2023 | -53.38905 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c31b1a9-8091-3a19-8a98-80ec412381ec | -3.20173 | -53.39253 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32a0f7c8-7672-3356-bc68-e0ced9f70824 | -2.8582 | -53.31265 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5c6de38-ca42-33e0-b117-890e127636d0 | -2.85762 | -53.31618 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11f7490f-79aa-351b-a041-56ddda749aad | -2.85704 | -53.31971 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13173a90-be65-30a9-a6ef-1162dd5224ae | -2.85218 | -53.31529 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b9f905a-8b0d-3807-9a99-8b4c12b731da | -3.84691 | -52.36707 | 2024-09-28 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c4fe5db-4b42-317d-9aae-4a29d5cb211b | -3.84641 | -52.37006 | 2024-09-28 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca34a783-c6bc-3c83-bed1-49551fe4a402 | -3.84188 | -52.36631 | 2024-09-28 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ab7f3f5-f4a4-3874-b55e-ec62fdf2610d | -7.99894 | -55.024 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5158002e-925b-354c-a5da-5f6b3de6b9c3 | -7.99826 | -55.02779 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 321e9d27-8d62-3041-9d8f-fe1d20df2150 | -7.99738 | -55.02316 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0e487b4-6745-33c0-8256-02af03a61077 | -7.99668 | -55.02693 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48ebbf41-1d30-35e8-b675-065091b1a7fe | -7.99334 | -55.02302 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f37b51e-1186-310b-8a67-c0a4d08f8fbe | -7.97959 | -55.06754 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 785639bb-04dc-3bd9-aa5f-e1de1a3d8d9c | -7.9789 | -55.07138 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 825b3a49-deee-357e-93ba-de2bd4eecb10 | -7.97699 | -55.07042 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d9ce91a-4d64-347e-9d34-bb8c5d1264a9 | -8.52448 | -55.18743 | 2024-09-28 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fe6a2d6-55af-37ea-8fe1-9aaadf148684 | -8.51962 | -55.18244 | 2024-09-28 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b80c10f-14e2-3d0d-b314-37ec95b081fd | -8.5189 | -55.18629 | 2024-09-28 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63a6f887-071e-3b7f-a666-07bddd4c9a2d | -8.51818 | -55.19017 | 2024-09-28 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9c2f7ee-cc4f-3899-86f9-26b9a59d6738 | -8.51745 | -55.19405 | 2024-09-28 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41ba54ed-f1cb-31b0-9c2e-45cd41208875 | -8.5133 | -55.18529 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce0a321c-358e-345b-ac33-b6b15160f9a2 | -8.29477 | -55.38652 | 2024-09-28 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 519bce01-b438-3fab-a147-07eabba8b8f6 | -8.29402 | -55.39056 | 2024-09-28 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15841f41-8568-320d-a683-8da4da507ad3 | -8.28081 | -56.48059 | 2024-09-28 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80d3848f-f885-3162-9483-dbdd166a19ca | -9.37784 | -56.84328 | 2024-09-28 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 69c7d61c-21f6-31ec-8904-6c2dab14e1e8 | -9.37731 | -56.84577 | 2024-09-28 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e22e5c86-6084-3aa3-b216-05d09c24cc05 | -9.2927 | -57.15708 | 2024-09-28 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d86486e6-f66e-3b50-854c-d23fb52c8b3d | -9.29095 | -57.1539 | 2024-09-28 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8cbb8733-84d3-398f-8e15-acf1d4b657fc | -9.28991 | -57.15913 | 2024-09-28 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9616381d-68e0-37e4-83c5-312059e554bd | -9.27817 | -57.16526 | 2024-09-28 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e46f305c-e678-3545-b764-c2bfe1b54c67 | -9.27726 | -57.17 | 2024-09-28 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16d8809c-a9ae-3919-b53a-940cd7c1aa71 | -9.25003 | -56.91684 | 2024-09-28 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88c9611a-2551-3982-9ee3-b8c76f8da6c0 | -9.24911 | -56.9217 | 2024-09-28 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1332682-fd66-3c91-bd8d-d2b1df45d480 | -9.24865 | -56.91911 | 2024-09-28 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce24db1e-275d-3b46-be4c-a6b1a6482a95 | -13.28655 | -58.19092 | 2024-09-28 04:21:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eeaef153-cba9-31c8-b61f-85deccab6959 | -9.12387 | -58.94933 | 2024-09-28 04:21:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f348ab8-fd24-3a1f-9c81-8447343e4d2c | -10.25956 | -43.56622 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5ad5037-4c6f-37f2-8cb5-977b9ba7e004 | -13.47683 | -48.5905 | 2024-09-28 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a822f2a-7ec3-3efa-8276-7491a14c8a7e | -14.8196 | -40.46018 | 2024-09-28 04:21:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| efe4b575-8efc-37f6-a015-a6ce617339f5 | -15.09123 | -42.09581 | 2024-09-28 04:21:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a81ec37c-efbb-3719-849c-ccf0cd72365b | -16.63114 | -42.45976 | 2024-09-28 04:21:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5964a4c9-1642-3a34-b51b-25c869584d87 | -10.38687 | -42.57999 | 2024-09-28 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84886708-06bd-347e-b69f-80c6c8070586 | -11.83051 | -42.80227 | 2024-09-28 04:21:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dfd2dbb6-cba8-377b-947c-f3ddf137f22a | -11.36085 | -42.9213 | 2024-09-28 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f34c390-3671-33d4-a938-3cd2c91ffb04 | -13.37901 | -42.04181 | 2024-09-28 04:21:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0bba1c16-6e09-3c65-834a-59a4f731274c | -13.3789 | -42.04515 | 2024-09-28 04:21:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cf3121fc-b891-32e4-ae25-a8802e968e6b | -13.37837 | -42.04653 | 2024-09-28 04:21:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74998657-e957-3702-b098-9c4f27d6f608 | -13.37507 | -42.04478 | 2024-09-28 04:21:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8e20b439-ac78-380e-b2dd-e216bd1d7d7c | -13.37 | -42.0532 | 2024-09-28 04:21:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f36a522-e6a8-38aa-97e9-29ded2b08210 | -13.34645 | -42.05523 | 2024-09-28 04:21:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 843b7f18-35ad-3831-9749-856f610baf08 | -13.34582 | -42.05968 | 2024-09-28 04:21:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 36f521df-4d34-3794-b3fe-b9e79248e4b7 | -13.33949 | -42.04959 | 2024-09-28 04:21:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c119a2ea-327b-3cfe-8239-24a80360d522 | -13.33821 | -42.05871 | 2024-09-28 04:21:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fcb6e157-7a39-3a72-92a4-492e38672f75 | -13.01385 | -42.21925 | 2024-09-28 04:21:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5221e777-c376-358a-8e48-d299c4f57f39 | -13.01046 | -42.6842 | 2024-09-28 04:21:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 17a2d2b9-7b6b-33bf-b1c0-9f7269d8f151 | -13.57103 | -43.46188 | 2024-09-28 04:21:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b009197c-0167-32c5-bfdb-6274aea9127a | -13.57044 | -43.46596 | 2024-09-28 04:21:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba0b304a-27d3-3a6a-87bf-13bf0ef6f665 | -13.55158 | -43.44636 | 2024-09-28 04:21:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d1e752b-8a71-3262-b98c-849f79a94ec5 | -13.54804 | -43.44581 | 2024-09-28 04:21:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46eda1e2-b6e8-3b06-9d6f-cee3403df3b8 | -13.8663 | -42.62553 | 2024-09-28 04:21:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 73bade39-a070-32da-975b-e13be649ccf6 | -14.72728 | -42.87743 | 2024-09-28 04:21:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 04ef0750-8254-3322-96d3-9d6a98ed0929 | -14.73097 | -42.87798 | 2024-09-28 04:21:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ac99d07d-4d51-363f-a51f-d85b04b287d6 | -15.10926 | -42.46573 | 2024-09-28 04:21:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8a2b489e-d3db-38e7-a9af-8ff777c10475 | -16.26593 | -43.86824 | 2024-09-28 04:21:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceee7bb3-ddbd-334c-b9ec-2d186ddf2ae7 | -16.26325 | -43.8698 | 2024-09-28 04:21:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7496a648-f481-3197-ba5a-fb109e1512f3 | -16.04656 | -43.61296 | 2024-09-28 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2742c623-7a36-3a57-9c2a-8e5c35cde751 | -16.04296 | -43.61241 | 2024-09-28 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17214e8d-9967-35b8-988a-318d6467a8bb | -16.03935 | -43.61185 | 2024-09-28 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README48.md)
