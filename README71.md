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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaf8d2c3-e805-34cf-99c4-9c93171a5608 | -3.74928 | -47.36118 | 2024-11-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f9e3c16b-5396-339b-b908-88ab501eaeb2 | -3.76884 | -50.7043 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90a3a85e-d4f8-3697-b0d9-c82576981a86 | -2.78886 | -51.71863 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e202eb60-ade1-3094-b646-de71499c1e5f | -2.44351 | -54.77086 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb7f5755-afb9-3eeb-b834-9794e2c28469 | -3.24047 | -53.51595 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63b221c4-6c80-3b3a-9ac6-a205760d501b | -3.57177 | -54.68768 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 786d294c-dd9b-32e9-91bb-e0d1feeb8ddd | -2.41976 | -53.67989 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afdb41c7-9793-3ffe-81ef-17a4758a79d3 | -3.41582 | -49.2293 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21b10c9c-15b7-3671-9eca-e9cf76b9eb9f | -3.42588 | -54.60368 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1619cd9-cbd8-3ccc-887f-13b9531c029f | -3.46697 | -50.01244 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c374911f-5566-34f3-940b-87605a5e4745 | -3.56663 | -53.2579 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32ddcdf5-05cc-3ac7-8e39-7cb2c5901d28 | -4.3879 | -47.77404 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f097951c-3064-34d0-999b-c3f10b6136a7 | -3.75054 | -52.66947 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05baff72-6923-302b-a2fb-99f98163fcb4 | -6.06905 | -44.15252 | 2024-11-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ce7321a-ab1a-3869-bad4-e6a4dfa88ad7 | -2.83638 | -51.82122 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9a5a182b-11fc-3af4-9446-cf5e35cbb4da | -2.61978 | -54.26486 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3d76100-ffd1-3d34-9be1-d2c55c89c1b1 | -3.86446 | -52.32959 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a809daec-068d-3690-b50b-456e4bb01dcb | -3.0402 | -49.46279 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84b78edd-1ff6-337a-9925-311ad7f57163 | -5.52109 | -43.33114 | 2024-11-21 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dfc1452-14f2-3a0d-8955-f9de8716ef46 | -2.85296 | -53.9704 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5863d42-bbb1-349a-92e2-6d7acfc4138a | -3.68528 | -50.22125 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 84b744e9-fa89-317c-bbd0-decdd595cdfd | -2.90231 | -51.7759 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d6fc2a6-54b1-3755-94f6-42570d8f3bca | -2.76962 | -52.11795 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ed3b144-7a16-37f9-af1a-99a9314a4666 | -3.83169 | -50.29262 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 083b44d7-4100-3be4-b12e-cf0c9511a793 | -4.38362 | -47.77339 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4aa7d305-ae2f-3fb9-a0c3-90a09c96ba79 | -2.61557 | -54.05364 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ef44085-2362-3937-ade1-e694d1562a95 | -3.07695 | -54.5522 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e9524ac-99c2-3b9d-bbc7-c9b7f94c7312 | -4.00362 | -49.92381 | 2024-11-21 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0df14387-b2cc-3fb6-aae0-1f3d125aac99 | -2.95923 | -51.41359 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b3a6dd48-2967-31b1-b3f2-b3767725dd7e | -2.79891 | -54.01159 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0428d883-61de-3ee2-b5c0-db69d4160c7f | -4.10987 | -51.05343 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2718ee7f-277d-3d13-a3f5-f48c7f7d16a7 | -3.57527 | -54.51522 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b2b2ea2-0532-34c8-b58a-da7ab7136875 | -3.56164 | -52.15969 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c24dcfd-eee1-31ae-b095-22c8279c90d7 | -3.0687 | -53.22543 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35fc0e10-ad13-36f2-a72d-db6e91c8d3a3 | -3.5209 | -53.80702 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 670241f0-9a6d-3c5d-99f5-d472f176bf51 | -3.46854 | -54.54491 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 328c7e81-c696-31a7-bed2-c0f1f1a433d8 | -6.93711 | -42.82213 | 2024-11-21 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d29e1e1b-00c8-3cff-ad0b-d371da0d0bb5 | -2.82488 | -54.0192 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32d245f0-6b87-39f1-a3f7-408907bdcc73 | -4.05994 | -54.05046 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90d93105-7c83-38b2-82e1-c0497119e0a7 | -3.17168 | -53.97412 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79a6b2d9-281e-3311-aab9-a13d61e43a46 | -3.49324 | -50.44975 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9b9959f-0d0f-3065-ac2f-394ed76001f8 | -2.58445 | -51.72438 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b082621c-fe47-392d-b80f-222671ecabbe | -4.2527 | -46.11726 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1aa7f41-b481-3a6b-aaf9-ec6a339bf2ad | -3.49746 | -50.44619 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 975387a9-3924-383e-8ea8-03ba8c245497 | -3.11912 | -54.30713 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b20ba485-26d5-34b7-8909-742e9909ebc3 | -8.10602 | -55.02287 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a23f7350-bb8c-3857-a19c-55a9a88d984a | -2.92868 | -53.08034 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a813a53d-40bb-3d4a-91da-b32beb9703c8 | -3.21911 | -50.5845 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 484b5984-699e-33ab-9f61-262c878549e2 | -2.74769 | -54.12054 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b858ae13-8728-379b-a94f-6901f794fc10 | -3.89492 | -50.07494 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ffdbaa9-ccc2-3769-9c97-8fa2fb4c1dd5 | -3.3564 | -54.0955 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 175f58f6-930a-3e88-8769-a1e1a41f3946 | -3.2753 | -53.83518 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 65c0d7c4-dc99-3bbf-8c66-05560f9e2b4b | -4.24306 | -46.11617 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 56e21d69-b43e-32cf-96a0-411408e71d29 | -3.28799 | -53.84068 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 61511d8d-ec25-3c0f-8af1-7734a884923b | -3.61022 | -54.74811 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7c00196-ef68-3dcf-8265-3fd6710885df | -4.57023 | -48.02517 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2863ce35-92a7-37d6-a893-d14c515994be | -3.07114 | -51.25851 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93a18eea-8c82-34e9-bd90-a276cebb2654 | -2.85573 | -53.97437 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d1d6716-7e00-392d-a881-5b88f7d94e0f | -11.03764 | -44.5731 | 2024-11-21 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3cacae59-038c-32a3-a73c-d49e39772cc2 | -3.9142 | -55.6855 | 2024-11-21 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d116756e-3e2d-3fb3-956a-7413843e4c87 | -2.75861 | -54.05109 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 932e6445-dc83-363f-9fac-7058f2003c78 | -4.56997 | -48.02552 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6a9c46b-8299-3669-abee-230ab7e70446 | -3.50877 | -53.79804 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d91618a6-04b2-3999-a303-1b5cddbfc733 | -6.37941 | -44.74682 | 2024-11-21 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8caf374-a39f-337e-beef-19a77ce2dc35 | 1.79037 | -50.42878 | 2024-11-21 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cef861b3-e844-30f7-be1f-9e4cb2e25cbb | -4.15329 | -42.01849 | 2024-11-21 04:55:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 0928e094-689b-358a-a676-748fae36111e | -3.11234 | -53.09843 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d38a022-6993-3626-a110-2b5e2bffe833 | -2.76525 | -54.05213 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0019a8e-09a9-340b-a8f0-7fa13b6b3516 | -2.75568 | -52.11937 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fa64c12-6520-3ee9-8d6e-74220b7c6a9b | -3.27476 | -53.83862 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3599f941-3d8a-3532-bd67-89d773580c01 | -2.83976 | -51.82173 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ffb93f21-eb1d-3bef-a7ea-70ee5000b74d | -4.1232 | -53.82384 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7add1e48-67f1-324b-bfa8-a06751ab325d | -2.60945 | -51.79437 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74e037fe-ff02-35d6-a341-95d8cc680147 | -2.75233 | -52.11884 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ceec1d2-c02a-3ef4-a189-87824331d451 | -3.64643 | -51.45527 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8213d8c0-e78c-33c0-b228-06f44b3ffb4d | -4.08787 | -54.0476 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bde7f207-e238-3f23-91df-f231de9ddba3 | -3.28636 | -53.85101 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d92205b9-5a29-366d-ab0e-b783d879bbd0 | -3.31482 | -54.91391 | 2024-11-21 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a696274d-e2c8-3b1a-92fa-ce95fc6cd4cf | -3.00673 | -51.31006 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fe0b4e24-6eb6-3a98-bcf2-d89e05367fd8 | -3.458 | -53.32156 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40e245f3-11e6-383e-a1e0-2e058fc52fe0 | -2.82334 | -54.09355 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4b0634b-ce91-3ba6-9245-783e095b7b2b | -3.61579 | -49.41856 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01dd86b7-c5b3-32b1-bc3b-74147242ae45 | -4.09009 | -51.08285 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dd573fb-238f-363e-847d-9a779941ee89 | -4.21425 | -48.71917 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89cd7022-a40a-39d9-a2a2-031e81c70853 | -4.96403 | -49.84252 | 2024-11-21 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bd37cc9-f719-3910-8587-a095222966e4 | -2.62183 | -51.80364 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95ce0202-9372-3e38-88e9-5008818b19f9 | -2.85137 | -54.00205 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93a0cd4a-b94e-3641-9bf6-fc1315dabec8 | -3.00731 | -51.30632 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9b16b3d9-c060-3de4-9ca9-bd176546f0dc | -2.4014 | -53.88208 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70662fc9-2fac-3105-8070-8bb50caedd12 | -3.1942 | -54.32646 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c09c1599-db71-394c-bee6-c78af60e86c0 | -2.59447 | -53.99347 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a2bc473-16b2-31b2-8473-6ab97c4e47d0 | -2.82611 | -54.09754 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae14b0ad-42e8-33a0-814a-abed376b8de4 | -4.17864 | -53.57893 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f12e7d92-3662-3810-96e1-64a695318b63 | -3.4401 | -50.77178 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1c94efc-8d9a-365c-ac78-1138f309f1e6 | -2.3898 | -53.71719 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99e854cc-2dda-3ec6-970e-3dee43ca14d8 | -3.67495 | -45.24491 | 2024-11-21 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1481ab3-89b1-381f-8f24-d35ad5a869b0 | -3.46241 | -54.56194 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9bce58b-0033-3fca-8e9f-6e7038605b15 | -3.3013 | -51.28901 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 610c8aeb-4e85-3f25-a418-eb2cad4fc2fa | -3.5175 | -54.6897 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a931610-aa27-3070-8225-f1e4f7ce19e4 | -2.66792 | -51.8842 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README72.md)
