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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5923f4d6-b2ef-3d8b-9a1c-ae48a0005024 | -4.04238 | -54.01685 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9535ecc3-aae6-3a3d-85da-92489c3dc5b0 | -3.99485 | -54.14864 | 2024-09-29 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7de6e6f0-74a9-3358-90d3-a88dde26f131 | -3.99383 | -54.14777 | 2024-09-29 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfd47dbe-992d-3657-9184-90be023fd58a | -3.98906 | -54.14729 | 2024-09-29 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b46889b7-6ca0-3fb0-b899-212ec336dc90 | -3.87041 | -54.35102 | 2024-09-29 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f41ab929-3af4-32ea-9390-b0056b7c5efd | -8.09543 | -55.38923 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 546e1cef-df89-30eb-8af0-4ba5cf9b2f14 | -8.0949 | -55.39339 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0834c29c-bf9b-31b0-937d-45982b75192c | -8.09438 | -55.39748 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40aef6c8-63ba-3240-aeeb-af89c2fa2545 | -8.09389 | -55.3895 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b7545c1-836d-3e73-9c54-fb5fbc494e62 | -8.09333 | -55.39365 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5b6dc5a-0603-3f0b-9d58-8d9487508eea | -8.09278 | -55.39774 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56620e25-8e4e-3075-9fb0-820221efa8b6 | -8.0897 | -55.38841 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70792831-3b57-31a6-8fe4-d7c56ec69c25 | -8.08917 | -55.39259 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b2c1585f-c4cc-3021-9060-a84716a626c9 | -8.08864 | -55.39672 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47d4ca53-6ce5-3d91-90b5-1cd7035acb88 | -8.08816 | -55.38869 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f33f9646-fefb-3a47-9ef6-bb8d5469c269 | -8.08813 | -55.40077 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3100e923-fad4-3198-8650-021443392396 | -8.0876 | -55.39286 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 07527d6c-b35c-321a-b5f6-44206e322f37 | -8.08704 | -55.397 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30e1fccd-ccaf-3de1-b1fa-bd4386212074 | -8.0865 | -55.40103 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 795155e0-e08f-378f-9a7f-9d4ee8cd464d | -8.08343 | -55.39177 | 2024-09-29 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f66c786-9e5a-3aa0-9651-bf48e2c3d823 | -3.54224 | -55.49324 | 2024-09-29 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1f3ce56-d05a-3158-b753-7920d540e112 | -3.54173 | -55.49671 | 2024-09-29 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 791d6b7b-7c76-3d6b-80af-f912ee20adbc | -2.68384 | -57.5092 | 2024-09-29 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d79f5b16-5cc5-3a69-9b26-e2bf27bc1f6e | -2.67538 | -57.50307 | 2024-09-29 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1112d44f-6b56-33bd-8a5c-296aed363c09 | -2.6715 | -57.49767 | 2024-09-29 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3527bd3f-f0da-3c9a-b2f3-276e5eb84eb0 | -2.6708 | -57.50237 | 2024-09-29 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2d3d55e1-12fb-392b-a983-21c689af11e4 | -2.66622 | -57.50166 | 2024-09-29 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d4f526e-3192-3cbe-9542-a289dfc34628 | -2.66165 | -57.50094 | 2024-09-29 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d15aa36-4b17-3de7-9ae1-1c8c2cbfc851 | -2.66095 | -57.50564 | 2024-09-29 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d3dfba7-61b7-3fc3-9545-54bc347c4a6a | -2.65707 | -57.50023 | 2024-09-29 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88f40610-224f-3596-be8e-38e573ee8707 | -2.65637 | -57.50493 | 2024-09-29 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41bca30f-362f-3af7-a781-f5355c005276 | -2.65111 | -57.5073 | 2024-09-29 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fed1269-289e-323b-aef0-01e9baa8d377 | -2.6511 | -57.50891 | 2024-09-29 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e1131c3-dea6-34e9-b63a-d963898084c1 | -3.76303 | -57.17937 | 2024-09-29 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ee00b00-42c8-34a6-b687-b142558ff39a | -3.76263 | -57.17828 | 2024-09-29 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc1da95f-1c4a-3048-9b18-363d377e83c5 | -1.50486 | -61.59061 | 2024-09-29 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27c81ef2-7dce-3125-81c7-556fafa30cf1 | -1.50426 | -61.5945 | 2024-09-29 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7494a256-186f-3c1d-94b0-1f4082e74433 | -1.50136 | -61.59006 | 2024-09-29 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c80a040-f96b-31d4-8a03-7bf73b9b93f2 | -1.49725 | -61.59342 | 2024-09-29 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2aeb4d9-5b1c-31aa-88eb-c0630bba7bcb | -1.49315 | -61.59678 | 2024-09-29 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 942a0086-90b1-37a4-861d-566ca9e20b7b | -1.49256 | -61.60067 | 2024-09-29 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4468b86-8528-3078-a4e7-fa93f8990497 | -2.88802 | -61.88157 | 2024-09-29 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da55c4c1-a59f-395f-9537-6d93935d81db | -3.02852 | -61.6753 | 2024-09-29 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53cd89c2-fca5-308f-8ab4-68439df21d9e | -3.02791 | -61.6793 | 2024-09-29 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40d475d3-89c4-375e-ba76-144bcd16d6f3 | -3.0273 | -61.6833 | 2024-09-29 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3afe4648-1c72-37f7-8c0c-14d1297fef44 | -3.0179 | -61.67365 | 2024-09-29 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b351613-4dd0-3434-99c3-aaefec78d6ed | -3.01728 | -61.67766 | 2024-09-29 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6774686f-4a60-3008-a467-9c7883b56425 | -8.71462 | -66.64651 | 2024-09-29 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e81a9472-1255-35e2-8eb3-474798752df8 | -8.71407 | -66.65003 | 2024-09-29 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf0c2980-bc3f-3af5-9b22-f288ca389cae | -9.87613 | -67.32325 | 2024-09-29 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb7cf70-06c3-3f5a-8b8b-2288d4a23447 | -9.8751 | -67.30836 | 2024-09-29 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9074d351-816e-3775-a43e-4b3df73619ca | -9.59138 | -66.1836 | 2024-09-29 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8fe00c6-8e15-3562-bd05-1d5b055ea9c8 | -7.70376 | -67.04596 | 2024-09-29 05:44:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 849eb9ae-a9c6-3a66-89a1-e39f28860733 | -9.39087 | -68.16847 | 2024-09-29 05:44:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 631f1bcc-5090-319e-9962-8279698a6a16 | -9.39025 | -68.17227 | 2024-09-29 05:44:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db80e2e7-d33f-30d6-be92-9315c273875c | -9.36787 | -67.41848 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5bc31ee4-7770-33a0-9edd-402a94eaf87b | -9.3645 | -67.41794 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23c94230-9c97-3e07-9c1a-b97e0bd99628 | -9.35702 | -67.70913 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a542391-20d8-3418-95d8-0b2467447484 | -9.35642 | -67.71281 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d15c520d-4770-3623-b00e-13716a5a886e | -9.35363 | -67.70857 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee1c8089-6c6a-3e55-a537-52bb3eea1c39 | -9.35303 | -67.71227 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cbc8fa2-ff5a-3f08-8b4f-02bab0b24850 | -9.29853 | -68.74851 | 2024-09-29 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e826a80b-3425-37ae-a806-72d810e284ad | -9.21137 | -67.93401 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9c3284d-b6f7-32e8-b916-061af65e22cd | -9.19069 | -68.29849 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79f9391f-7bee-396d-a512-dbce25184570 | -9.15296 | -68.37618 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b27ff3c6-de70-3cd0-af5e-d5a8c2993416 | -9.14948 | -68.37562 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b5df1fe-3c4a-36f1-ad91-ad93512e3be8 | -9.14225 | -68.20352 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d00db26b-e08a-3a9c-9669-069cc11dc269 | -9.13989 | -68.20313 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 534c5071-5f48-31a7-ae7a-76a542afb243 | -9.11293 | -67.89083 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 240bd50c-abb8-3524-9350-cfdf7d2b02ab | -9.1117 | -67.89834 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 714834a9-cdcd-3f93-9828-8f105c099712 | -9.10971 | -68.21402 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7117abb-794a-3f8c-8f0f-5510e0b5616f | -9.10951 | -67.89027 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60e370bd-f93c-3b2a-8bfa-95de7210b981 | -9.10889 | -67.89403 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43af83ef-b650-3b64-8f65-2391a5eb4c40 | -9.10828 | -67.89779 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 984f55d6-1d11-3abb-93a7-4b6b90c92e6d | -9.10547 | -67.89347 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16ebf659-08c9-3edc-88bf-f1a60f68644a | -9.10141 | -67.50576 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 271c89f0-7044-367a-b918-a742c7b11e55 | -9.06956 | -67.81123 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b97f7ac-c1ef-3af2-87e5-e1c6335e6be6 | -9.06615 | -67.81067 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9e677c9-836c-37be-84b3-d523ead0c3c7 | -9.06555 | -67.81441 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b32cb417-1f53-3e73-ac94-ff936a9f4cf2 | -9.06274 | -67.81012 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31ea07ff-3036-386c-a07e-5db2b00ce86b | -9.06213 | -67.81385 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39b21bb4-3677-3b0d-8aa1-cf253eac71b2 | -9.06153 | -67.81758 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ab4d48c5-1847-3698-9616-6a4e32aa9acc | -9.04196 | -67.89513 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a72c262-5a78-31e3-a270-908c8ad0f116 | -9.04136 | -67.89889 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d04a28e-78be-3140-b962-380e85513094 | -8.97796 | -68.46511 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f2e8f96-64b7-335f-9640-d3c46a00af3c | -8.94421 | -67.63135 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c325dba8-380a-35c8-a518-d39226b401db | -8.94082 | -67.6308 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1db0c68-a337-3e99-85a3-48d4a12d03a2 | -8.94022 | -67.63449 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42bcdc3a-ddc5-3bb4-a496-7c0faca1f556 | -8.93021 | -68.55902 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4369712-06c3-3d1b-a681-bf5b4ebd70bd | -8.86208 | -68.6424 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c62bf614-ce08-31a3-b036-0636bcb1e3d1 | -8.8614 | -68.64644 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81ddad31-770a-33e1-b3e4-f395491e3457 | -8.81656 | -67.68224 | 2024-09-29 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c8872eb-1d54-3cf2-9cca-637482ac9d3f | -9.89828 | -67.58301 | 2024-09-29 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61a24a16-be14-3230-8800-f454809f7ae0 | -9.89657 | -67.58236 | 2024-09-29 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cea7b4d-5c67-32d4-93bb-ae7ef9a2eef4 | -9.77466 | -68.42001 | 2024-09-29 05:44:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f27fc9b-0783-3997-b64e-30cce03068c7 | -9.6636 | -68.56185 | 2024-09-29 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd9e025a-5419-32a1-a9cd-89ed42d3bbb6 | -9.66011 | -68.56129 | 2024-09-29 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 250e1773-f03c-3096-864d-16a4c2cb5c25 | -9.65946 | -68.56521 | 2024-09-29 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9eb33047-8df2-3542-aabd-51b90abec857 | -9.51917 | -68.24473 | 2024-09-29 05:44:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04e6ceeb-6d65-3a9c-8e16-30c0e55f48e6 | -9.51855 | -68.24856 | 2024-09-29 05:44:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README65.md)
