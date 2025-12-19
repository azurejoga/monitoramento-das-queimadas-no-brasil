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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3dd8d79-d460-3bcb-bedb-783ccdc0750c | -32.34275 | -52.36703 | 2025-12-19 03:55:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 4cde0ec0-9d7f-306a-b17b-6cf3e7a005f0 | -2.8608 | -51.58335 | 2025-12-19 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7e1c724-e7e6-3422-8ad2-a0987c74b56b | -2.69544 | -51.64573 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0470df2-e9bb-3d77-be58-fadfe53fe2d6 | -2.81534 | -48.61079 | 2025-12-19 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2a526497-d15e-35b2-b158-dcbd6e4f8388 | -2.74567 | -48.3818 | 2025-12-19 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85895ffd-86ba-3d34-bc2f-2d8ebffdb052 | -2.11184 | -50.91272 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f06b38dc-9870-3eb2-b921-7e3536688a0f | -2.10837 | -50.91217 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 88387b31-9b18-3c5d-b796-027e47deac94 | -4.78024 | -48.42052 | 2025-12-19 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40052841-9029-35b8-b108-fdcf61deb604 | -2.37966 | -51.91594 | 2025-12-19 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37f4fe73-5366-387c-a35a-359915053692 | -3.1859 | -50.23087 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd3532df-f0a6-3fc0-8d2c-d666c88f295a | -3.74909 | -49.72604 | 2025-12-19 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 329c7a14-0bbc-3c5c-b58d-f39cf896a2e7 | -3.18927 | -50.2314 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02b8f988-5bf5-3fd3-a08d-4f28f868d43c | -0.98794 | -52.33949 | 2025-12-19 04:38:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 342b2f9f-7642-39e9-a501-941a6fec0b24 | -3.09162 | -51.27057 | 2025-12-19 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 454cdaa1-1630-32d4-a302-1be8ea394632 | -3.7535 | -49.71961 | 2025-12-19 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3fb5464-38ac-3449-93df-0a046b4f0509 | -2.41443 | -50.35545 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aebcb50f-65d1-3106-a13a-ca45aa6e85fe | -3.75186 | -49.73005 | 2025-12-19 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e80f0e7b-a718-3676-a7e6-2be586b3d489 | -2.99057 | -51.06243 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 272cd07a-48bc-3417-ab12-f429f9c0bb49 | -1.29176 | -53.0549 | 2025-12-19 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1ce91ff4-26a4-3f51-910d-ea9444cab43d | -3.15845 | -51.10704 | 2025-12-19 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cc12d93-a61f-3e87-85b4-cef6349c1945 | -1.28677 | -53.05723 | 2025-12-19 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0cc05fff-816e-391f-a686-49ada0e39067 | -3.08899 | -49.59727 | 2025-12-19 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cbc3a87-f8fd-36bd-93ea-ab5be72a7081 | -2.79088 | -51.40923 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c241747e-6ecf-36ec-b437-92cafba9ff9f | -0.64648 | -52.38714 | 2025-12-19 04:38:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 448dd003-d8b8-3c9a-b952-eee42cbfb30a | -2.67506 | -51.70519 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1ca8e25-b60c-35a7-9467-5b08e31ceb8a | -2.6813 | -51.73557 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b00269d5-61a2-327a-a502-75014faa3ce2 | -3.37512 | -50.02688 | 2025-12-19 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ab3d373-c193-3935-8ed7-063d47ba4526 | -3.08622 | -49.59327 | 2025-12-19 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84354523-fd36-3160-b3ed-ce5b71f8acec | -2.82515 | -51.828 | 2025-12-19 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ce09d29-4a92-34bc-9eff-33b787eb32a4 | -3.08954 | -49.59379 | 2025-12-19 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3f67cc2-0719-340b-baa2-64232f596f80 | -2.97398 | -51.57941 | 2025-12-19 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 25f275d6-6783-327d-b30b-6464d96334fd | -2.80137 | -51.01785 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4109984e-4684-3567-b20e-eeb99a15db44 | -2.39644 | -50.31534 | 2025-12-19 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aae4b28e-c8f0-3b4b-82b3-c1aacc8fcc42 | -4.43859 | -48.45254 | 2025-12-19 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df571559-a5c6-3179-89e1-136b63d0ba6e | -2.70209 | -51.8943 | 2025-12-19 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 159a93a0-a3a6-371a-ad33-93a16f132229 | -2.89009 | -50.23247 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57421e33-cada-3fa8-841b-57afde7368df | -3.23697 | -50.54977 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b9663df-7921-3389-81a9-ee135a615330 | -3.23357 | -50.54924 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb7c08d7-5048-3286-8243-4ddf2d7226ec | -2.73007 | -51.6293 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fce6d39-e7e1-3564-9f71-b3d75b660720 | -2.82625 | -51.27789 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1d84a00-3ece-30ee-bba3-da77414aba5a | -3.02173 | -51.19236 | 2025-12-19 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f95cb503-811f-3d57-bbcf-50c6b884d7a5 | -3.02111 | -51.19623 | 2025-12-19 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e38165db-c783-313f-810f-1e187ae6fc4a | -3.58218 | -49.53282 | 2025-12-19 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c271273-0040-3401-b6c9-10bb303dc15a | -2.10958 | -50.90452 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b790aa20-4abb-37d6-a636-387ec2af2ada | -2.74897 | -48.38231 | 2025-12-19 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ca3e1af-36d2-33f5-8248-a5ded3d5b644 | -3.15498 | -51.1065 | 2025-12-19 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ceb4d002-5a58-31bd-bd41-806193ac6162 | -1.28781 | -53.05433 | 2025-12-19 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7cb16612-d144-34a3-8c3e-769cbab80e39 | -2.23087 | -51.93302 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8158be53-cd29-32bf-86de-05ac7330a538 | -2.97753 | -51.57995 | 2025-12-19 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d320235-511a-3ecd-b801-c53328b2c2b7 | -3.75296 | -49.72308 | 2025-12-19 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56082c93-7650-3471-8a7c-404db9b77052 | -3.23277 | -50.95168 | 2025-12-19 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e126337f-6b17-3f92-a8ec-902a4dbed16a | -3.74522 | -49.72899 | 2025-12-19 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ffac697-61bc-3775-9930-56c7592d03a3 | -1.73136 | -52.05523 | 2025-12-19 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 106d47ec-5f41-3a53-aa4a-30dc7a78733e | -2.10897 | -50.90835 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1adfa6d9-f99b-31b4-8906-7e3e4b5284e9 | -2.90447 | -49.79443 | 2025-12-19 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 049bd9b9-42ac-33a1-8c65-df10ed2df30a | -2.69965 | -51.64224 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 16f55bcf-2236-311f-8799-e1908dc0ad71 | -2.7915 | -51.4053 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93d1d2d0-d8e5-394e-bd33-231216daa9b4 | -2.74844 | -48.38575 | 2025-12-19 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e37055c-d245-34dc-bef6-8140f30f1a37 | -1.29072 | -53.05782 | 2025-12-19 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53fbce19-faca-3d3c-b6f0-3085f1ce06ed | -1.29153 | -53.05283 | 2025-12-19 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a51c7d37-4dee-3dae-b716-521cdc66415d | -2.89847 | -49.46782 | 2025-12-19 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6378dc66-41df-3bfc-a17a-5d86edd48329 | -2.82975 | -51.27843 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a93ce45-0acc-378a-b237-0b1ee640e214 | -2.65259 | -51.73104 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a170ac96-da8f-3b14-8c0f-e367d88a9a9d | -1.14912 | -47.91278 | 2025-12-19 04:38:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05f7d0ec-0588-310e-a22c-9f4c8770bd54 | -2.70932 | -51.89547 | 2025-12-19 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a2a44bb-826f-3554-bbcd-b6677fdcdd77 | -3.74854 | -49.72952 | 2025-12-19 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8778bd93-92da-3bc8-b7c0-cd79b37ac936 | -2.90503 | -49.79091 | 2025-12-19 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 720e0e8a-05ed-3bef-884c-746400f62212 | -3.2762 | -51.57166 | 2025-12-19 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcb4e9a8-bb06-3c77-85c5-94d21030454d | -2.45088 | -51.98713 | 2025-12-19 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcf74572-586e-32b2-a234-d8ff99bf9f28 | -2.7057 | -51.89488 | 2025-12-19 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a52aba38-2fe6-3f71-9fe1-43aa2bdede1e | -2.74513 | -48.38524 | 2025-12-19 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9a70de2-a5fc-3434-9ca3-18c60a47c7ba | -2.45088 | -50.25685 | 2025-12-19 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5127f584-c906-3932-9b99-49f4bc35d859 | -2.23452 | -51.93359 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85af5fa2-88f9-3a99-8b40-8ab78cd3fb6c | -1.28859 | -53.04933 | 2025-12-19 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fcb9c927-42c6-32e8-9689-e77a0d69cb35 | -2.90392 | -49.79794 | 2025-12-19 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7aff7911-ae1d-32f0-8c2f-344b1de42f51 | -3.23229 | -50.93234 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1137a4a8-033a-3dd7-b5a3-405695bc368e | -3.74576 | -49.72552 | 2025-12-19 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b65f0be7-e7a4-3070-9699-10bd35fe226d | -1.28758 | -53.05226 | 2025-12-19 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8dffc619-f537-3b9f-94ef-dbf02a5fb2f9 | -2.70503 | -51.89906 | 2025-12-19 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bba74ca-fd80-3a72-8391-0e04f5bc9c10 | -4.22042 | -48.97625 | 2025-12-19 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7271edf3-3c9a-37ac-9a78-13195eeb57a0 | -2.79504 | -51.40585 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80159f28-e722-3b8b-a2f8-bd2854f35b35 | -3.52241 | -50.87337 | 2025-12-19 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d26598de-212f-3a91-a08f-f9fc54f45c6c | -2.67599 | -51.67608 | 2025-12-19 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03d0d897-5fc6-3099-9ef4-e370b569d599 | -4.4419 | -48.45305 | 2025-12-19 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdafa227-fcd3-39e3-9389-a5b470f2f9d7 | -3.20372 | -51.27165 | 2025-12-19 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c546706-80d3-395b-852c-5cf8aff4afab | -10.4756 | -36.9924 | 2025-12-19 04:40:00 | GOES-19 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| 62f1f22c-5fa0-3512-87b6-31c9f3c319fc | -10.49876 | -44.93019 | 2025-12-19 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af8fa741-af5c-3f7c-8d7c-f2b38b8153d2 | -13.38704 | -41.88209 | 2025-12-19 04:40:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 301cf840-7c63-3e25-8c76-c85c36d0764f | -4.86478 | -50.82259 | 2025-12-19 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5eac3c66-8078-32ba-9890-4d8adfbd8d88 | -9.44276 | -43.21323 | 2025-12-19 04:40:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf85e4c7-a6be-35cd-a6fc-0c9a3d3ede02 | -13.39355 | -41.87283 | 2025-12-19 04:40:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dabeb22a-e201-37c7-a3b3-83b60a2471e3 | -10.47339 | -36.99052 | 2025-12-19 04:40:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 277fd637-56a9-311a-9615-d9ee2a5639e8 | -10.49928 | -44.92638 | 2025-12-19 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 741add62-7ce8-366e-ab17-56a7657bddfb | -9.34369 | -43.07922 | 2025-12-19 04:40:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51929fd9-23cb-3e19-8749-acc38505e985 | -4.8642 | -50.82624 | 2025-12-19 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6986528-86e1-316d-905d-180ddb6776df | -11.91006 | -43.82345 | 2025-12-19 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b24921d-7747-37ce-b934-30f0090857e6 | -11.85098 | -43.73654 | 2025-12-19 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8baef6dd-b00c-3861-9332-52db45842a32 | -9.34307 | -43.08389 | 2025-12-19 04:40:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e0ef28d-3ce8-3a28-b751-64a04aad968a | -13.39245 | -41.88193 | 2025-12-19 04:40:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4a29bc02-73aa-3cde-9992-038f84f24567 | -13.39281 | -41.87898 | 2025-12-19 04:40:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README5.md)
