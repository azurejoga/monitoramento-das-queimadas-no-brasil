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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 810d5749-15a4-3163-8a8e-967beb271d43 | -4.10726 | -46.94304 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b022f9d-b5e9-3f19-8576-9de26886753b | -4.05614 | -46.83318 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d3ce45a-d8ff-3ecc-9aa9-4f1783b26155 | -3.6547 | -50.23927 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbda5cd8-8b15-3e25-9d50-6dbd86bf297e | -2.57577 | -48.07502 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79c2fdb4-54f0-3a5f-9f47-e8c00abb7a06 | -3.0887 | -51.02703 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 027c71c9-a73c-3a17-aff4-0802a5a72ffa | -3.71563 | -51.80523 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aa6a799-d5e7-3dba-90d6-2d714a2633c3 | -3.93086 | -48.14978 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9df2a7a6-9972-31db-ba0c-5da8b970b200 | -2.61236 | -54.06779 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4b59581a-5006-34de-8f81-54f4d60c9108 | -2.44506 | -46.27422 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6a21d20-13eb-338e-b9fe-612ffedf7ee6 | -3.1011 | -50.36697 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 696b2704-9670-390b-a160-2b028da505b6 | -3.15383 | -50.61525 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8c8eecb-6e40-3312-8e9d-5677a9866266 | -1.23403 | -51.79575 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c06ce35-c549-3d7d-8184-aa6554e135a5 | -2.78341 | -49.21056 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0207ce1d-7197-3b45-b9c3-f0b6c280c3d3 | -3.39305 | -44.16971 | 2024-11-27 04:42:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb5c56bc-7d9b-357b-99f3-29a02ea7e669 | -4.29774 | -48.19574 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26dd65a7-8726-398d-bb54-3e9c409f321e | -1.15524 | -53.67791 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8379e629-d3b3-3fa3-abf7-b63f4cd29578 | -3.97147 | -48.06141 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4d4dee4-616b-3c04-af64-35c62650cd90 | -1.46615 | -52.68271 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e847d0eb-6639-3bb2-9da6-29a902578ec9 | -1.65131 | -47.71127 | 2024-11-27 04:42:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3de90cc5-9c5b-3949-9799-f2186d63e36d | -4.05938 | -48.33421 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c00b13a-c70f-3a3e-a002-5e1ade15379a | -3.69705 | -50.22825 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d4dd9cb-9414-399b-9826-90248e9a664d | -3.48334 | -50.80853 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80408994-db21-3c04-831e-888bf578cd07 | -3.74715 | -51.78078 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2304574b-f2ee-3728-a9f0-09460b5eef48 | -3.43836 | -50.12469 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad03fc49-72ca-3b3c-a6fc-4985d6c21532 | -3.78256 | -51.75331 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39f956e8-0e03-3020-9a05-ba70feae6c51 | -2.11063 | -47.89137 | 2024-11-27 04:42:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72fe2cfa-b031-369e-92b4-e0318651db19 | -0.88076 | -47.95571 | 2024-11-27 04:42:00 | NOAA-20 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 135b61ff-f54e-399e-b551-3e644700a05b | -3.12999 | -50.26939 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c31c1740-9f42-3639-96b3-4debc44345ff | -3.08496 | -53.24848 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4676cd66-ad50-375c-b7ab-33794b3c279a | -4.21866 | -47.21781 | 2024-11-27 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2571cf04-6660-3b42-a3fb-fd5b799e0c8e | -3.73037 | -49.95134 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33e23ab8-52d6-37c5-b561-8fce7a800c6a | -1.04298 | -51.74047 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d81b036-c67c-3ab2-9851-366f1e35fa58 | -3.24725 | -50.66876 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a6a505a-f50a-3ce2-94a4-655d8bbb927b | -4.40881 | -44.11246 | 2024-11-27 04:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c0c851b-b080-3a24-9919-d1d81fe54394 | -3.46176 | -51.58972 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95ef68e8-0ecc-3bc0-8c09-4b0f394101dc | -1.7173 | -52.35334 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d16e705-bae2-3326-a65c-ee8bd2b561d7 | -3.69375 | -50.22773 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b6c1364-dc36-3bfc-b1e7-bc699882047e | -4.25953 | -48.5359 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81b9775f-e395-336d-a2fb-1e3419d1c7e8 | -4.37259 | -48.50745 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbccd430-e72b-32b3-bfed-3d6030662792 | -4.29307 | -48.22622 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b399c16-a143-38df-933b-a896a2415757 | -1.94205 | -45.72621 | 2024-11-27 04:42:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c23a6b3d-e539-3e43-ad1c-27cd332fc771 | -1.29991 | -51.73391 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89e80fc3-19cb-3f43-934e-d5123d4d40ec | -3.2521 | -50.61656 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48ce4903-e70a-3ba4-bd07-97d80327c1a8 | -2.2473 | -48.4719 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca32f5d3-dd50-38fd-aa2b-9333bd2f6de8 | -3.29475 | -49.15285 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ade9366-ad5a-35bf-84d2-37a3329bc8d2 | -1.06164 | -51.80058 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a845f0b4-a02d-35de-81d4-6cdef8e5183f | -3.50226 | -53.82109 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d999926-47c0-3bc2-9ef2-48c0c909b9e8 | -3.54733 | -50.20864 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6140dce-8551-311f-8d4d-f61e288fe496 | -4.36532 | -48.0805 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ebe2cd66-e0e3-395e-846a-aabe2bab4adb | -3.33562 | -46.68191 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ade5d3ab-385d-357d-abfa-e09119198e31 | -3.05048 | -53.7221 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3bbf0ae3-1e04-36b9-9e85-83c61941684d | -1.78338 | -52.73771 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3eef166-9632-3811-a9db-21a94063e04b | -1.23001 | -51.79892 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e4bf322-0f74-37fb-a2e1-c478512219d9 | -2.77005 | -52.90786 | 2024-11-27 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25f39e89-7551-3a3c-b78c-745414d523fd | -2.84824 | -49.40258 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d294534-559c-3808-bc63-a109483d740c | -3.97132 | -46.72796 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9f54201-3ba5-38c1-899d-2f8131f7a1a5 | -3.24403 | -53.63441 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6aa7b169-f985-34c2-b68b-ce076dc1a8a5 | -3.06984 | -49.20134 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01874581-d546-3249-bd6e-34a41c212e49 | -4.12798 | -51.07255 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 523eb814-6c0c-32f7-8274-8ddb89de950a | -4.14451 | -43.80711 | 2024-11-27 04:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| e7c8155f-a3a9-3f8b-8fd3-b437e1c5c3cf | -1.79402 | -52.73939 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9129459-5b6f-3f4a-8a3f-3c47f9c1153b | -2.97671 | -51.57991 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3d98992-23fa-3df0-8177-c88d9b74235e | -5.38707 | -42.96114 | 2024-11-27 04:42:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f947e396-ade7-3543-a0aa-ff8794b2d91b | -3.06109 | -53.28253 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8314120d-ec42-31fa-abf5-90d58cfe991f | -1.69123 | -52.60964 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1b1bf9b-ab34-3bc2-8fe5-17af27030e9c | -3.44294 | -50.00913 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f78d351-60ad-3740-a262-ce040563c6b4 | -2.17777 | -53.25505 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60c6ee8b-489e-33f6-bc3c-81b807b4723c | -1.15592 | -53.67365 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e07451c1-6eca-3f8d-8e82-7a8d120fd45d | -1.82961 | -47.21243 | 2024-11-27 04:42:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87513d1d-045d-3979-85e9-82bb5b0667b4 | -3.06595 | -49.20433 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0880fc1-a45e-36d1-bc82-59de50577ff1 | -2.83235 | -46.84164 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cef7ba7-f5ae-3b73-8b15-062713e6a9b7 | -3.58356 | -50.60509 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf4c420d-e7d9-34d6-98fb-e0181f74386d | -3.96739 | -48.08816 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2cf52f2e-41cd-38df-b5f8-8d0d42dc1ffb | -3.05815 | -53.27788 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d1b373c-f0cd-3598-a5e9-1bfb8359d713 | -5.75621 | -46.26199 | 2024-11-27 04:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 053c9bb8-661c-3976-abe2-853e1e346a8e | -2.60718 | -48.36658 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dde5ac2-44fb-32aa-accf-16867daf3750 | -2.27294 | -51.24109 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be8b60e3-3b92-329a-b6e8-416fd47cd94d | -2.25245 | -53.62941 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 119fbade-67d9-39ba-b034-c8c787bfeed7 | -1.73101 | -52.04324 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e719b47-a476-3fa7-99bd-c3cf48190fd7 | -3.94064 | -46.90635 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdbbc430-23a7-35c1-af6a-f0e1aabdc462 | -4.04619 | -48.32833 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebb6267c-ca47-3387-9667-98dae50969e0 | -1.548 | -51.27399 | 2024-11-27 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a21e081-b7d1-3d49-a837-9ff392cb9bba | -5.7676 | -45.94686 | 2024-11-27 04:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb64cee1-ae50-3769-8994-21d7b7d85d42 | -3.67939 | -50.21141 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86c8920a-4cbc-375c-b573-67d460da0224 | -1.87829 | -48.54716 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 017c570b-753d-32a1-b243-1bf1c5991453 | -3.0931 | -53.26655 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f2e7ee4-ede5-3d3f-a26f-32b962ca8ab3 | -1.65376 | -52.41481 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e962276a-9e21-38a3-bd9f-6b4222fc2eb8 | -3.9376 | -46.71094 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bf222a9-635e-3c48-9d3e-f740efc74658 | -0.23849 | -53.7623 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e94dc9f0-f016-3e83-bd87-921091e2c9e2 | -1.7863 | -52.74228 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60a9a087-e14d-35c8-aff9-630a8f5c00f1 | -1.072 | -53.37615 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26c0c370-d5bc-3ce1-bff0-426ecf6f74ac | -4.21178 | -48.66438 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75119dcb-9179-3993-99db-696de81d38cd | -1.69998 | -52.76231 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6623b80e-1b57-353b-9a1c-091e3c0f35a8 | -3.11953 | -53.26226 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d8366f5-d5b9-31cd-a668-f14dbac0fb20 | -1.59425 | -52.26439 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9df6866-fd5b-31db-86c8-c0a1fed9ceef | -3.45263 | -50.29239 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88b53b39-b4be-3f3b-a152-dd1ec558b814 | -5.98417 | -45.36368 | 2024-11-27 04:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 608eb76b-f639-3ea2-8d0f-cfff19c605a1 | -4.65891 | -45.04248 | 2024-11-27 04:42:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f5e3aeb-638d-38c9-8c8b-05ab72d3f9e0 | -1.72449 | -52.48988 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed2b4df3-77f7-33b6-88bb-eef561f10e6c | -3.72006 | -47.12735 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README61.md)
