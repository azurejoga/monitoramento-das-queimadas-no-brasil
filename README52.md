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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 363bb97f-e216-356f-8b4a-f51055d1aaf2 | -3.07417 | -51.26801 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad11a8ee-2d19-3346-819b-3bd411495331 | -3.07359 | -51.27192 | 2024-10-21 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5b66052-bf91-3907-8884-79b0b8ca64b1 | -3.03965 | -51.0222 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc7181ff-1fa5-34ba-b866-c86144449217 | -2.94697 | -51.03822 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf2e5998-0f69-3526-9173-3b36b93ecf1d | -2.85653 | -51.29011 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44348574-6e3f-35ce-b717-751194bca275 | -2.85088 | -51.28917 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a923408c-6808-31d3-8efc-5e08ab659ea5 | -2.83729 | -51.30281 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1d029b5-d991-3714-a491-b6dd8f0a28c0 | -2.83672 | -51.30665 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbe12aeb-65d2-34fa-b017-a69a8ecec421 | -2.81979 | -51.34325 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| defea12b-b1fa-3b9b-9a1f-33cbd1b89b61 | -2.81923 | -51.34707 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6977a53c-fa4f-3bc9-a9fe-c4fc9b5116a1 | -2.81416 | -51.34234 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1aeff86b-e9d7-3cc9-84f9-cad46de8d522 | -2.8136 | -51.34616 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29fdd584-18c3-3d99-9f88-e96b90a2ff0e | -2.81305 | -51.34997 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f196378-9d5f-3e9e-b390-4a3f734f8e66 | -2.81249 | -51.35378 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 174d71fd-f3f7-33ae-9d51-c7c3e8873cf4 | -2.80012 | -51.3596 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 69ef32ba-2aff-37f2-b585-cfb72a612411 | -2.79957 | -51.3634 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bdaaf8ba-84e9-38ef-a601-9d55b84544e7 | -2.79902 | -51.3672 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a2deacf8-525c-3b56-959a-8b0c01fece80 | -2.7965 | -51.35943 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e1f4f7e0-351d-3ed5-921e-3d958509d950 | -2.79592 | -51.36324 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f8e9420-9ef4-3bd4-a463-526d629bb0d8 | -2.79534 | -51.36704 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 58b432a2-8b2e-3495-b0a9-8efa7fdb9a58 | -2.79476 | -51.37083 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 59ccdee1-36d9-3cb7-910c-4b26803d863d | -2.7945 | -51.35868 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 27b4fd26-e1ca-3219-8299-72ba77a35245 | -2.79395 | -51.36249 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a1c0ba7-b3ae-373e-a222-f91cb98bcbe8 | -2.7934 | -51.36629 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 305a0847-cb8d-3cae-822f-fe336cb45270 | -2.79285 | -51.37008 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 675f09cf-cc52-355a-9c10-3a31f00370d1 | -2.7903 | -51.36236 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ba5bc0cc-4ce3-3655-924b-f4d0bd6fcc3a | -2.78972 | -51.36612 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f687ecc4-90a3-321e-bb28-46d94a77203a | -2.78832 | -51.3616 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ae12469-0ab9-3de7-8552-d4c0b7f264be | -2.78778 | -51.36538 | 2024-10-21 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3401af7a-0b0d-3642-bedf-5d353c04784d | 2.91446 | -50.99982 | 2024-10-21 05:27:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19942e16-2178-35d9-a719-c247118d9caf | 1.01063 | -52.21959 | 2024-10-21 05:27:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84964322-1df0-3dd2-a05d-46580a47e847 | 1.01018 | -52.21668 | 2024-10-21 05:27:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6784aef1-bc1c-3bb9-835d-b6160d34e082 | -0.59677 | -52.15656 | 2024-10-21 05:27:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70923948-c77f-33c0-996e-11437117f789 | -0.18325 | -51.53793 | 2024-10-21 05:27:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 624a43cf-4635-3b21-b768-5016636d4272 | -0.18271 | -51.54128 | 2024-10-21 05:27:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f904bf60-ef00-3c54-8bdb-b5edc765c5df | -0.18141 | -51.53813 | 2024-10-21 05:27:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d38a74c5-c5ab-3c3d-a955-53f666a147f1 | -0.1809 | -51.54149 | 2024-10-21 05:27:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c51fa23f-9b9e-3992-a988-f995ca493dc6 | -2.02212 | -52.1262 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abca2dde-3b2b-3fae-a270-291f970341da | -1.99006 | -52.12715 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 033eee90-fa50-3810-b069-eff925fdb7ed | -1.98957 | -52.13039 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e347ad5a-6a7a-3c74-b4eb-1e278f9c655c | -1.93872 | -52.1091 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6be68f69-b646-342a-91e0-55c72410c2b3 | -1.93823 | -52.11241 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee76408a-de9b-3475-8ec3-d5b4a25e274d | -1.93441 | -52.10173 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 76d36508-dd91-37b2-9ffb-11efb1b95061 | -1.93393 | -52.10498 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 337d7f3d-1c61-379a-85f3-c4df065b1b7c | -1.93344 | -52.1083 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50c04f44-389f-31d4-947d-97f250f44430 | -1.93295 | -52.1116 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a76ec84-ddf7-3302-882b-5af9c8c08756 | -1.92922 | -52.10502 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f445894-d5c4-3508-acac-526f7942dfa3 | -1.92871 | -52.10828 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bb32a44-e0d2-3da9-b8bf-895ea42639ed | -1.92863 | -52.10425 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af5a1f9b-889b-3397-b888-d2d1849f570a | -1.80158 | -52.05872 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c03fd90-c8e5-3b3d-abce-dbcf40252635 | -1.78618 | -52.05325 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 428a5cc6-cbd3-3e36-a234-6bb3ec893e39 | -1.70412 | -52.68938 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c1f304e-50c3-3951-a610-1966551e08ac | -1.63732 | -52.65151 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fa31e47-32a2-33f2-9f48-dff2147f9082 | -1.63358 | -52.6418 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5267f57-1c96-3ba2-bf35-be8a1f5cf299 | -1.63314 | -52.64476 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b405df97-ab7b-3fd7-9cb3-acb18960c0c6 | -1.41379 | -52.67233 | 2024-10-21 05:27:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2548bc7b-29ae-3c2d-a2f4-8e5d8b795256 | -2.69091 | -52.06939 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1a4ca28-0c8c-3b15-9d87-7be326f04ba0 | -2.69042 | -52.07278 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0841413-dece-39a8-8b4f-12cf39f6e1aa | -2.68772 | -52.06843 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e22d1817-39c7-3671-abf9-3b114a8ced97 | -2.68721 | -52.07176 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 652edeb8-f385-336f-9d2c-3f2fa675491d | -3.11549 | -53.12192 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04cb02d9-edb8-3fb4-b104-28e8aabd9c75 | -2.99853 | -53.04671 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48c953cf-6983-318b-999e-0163a0d10649 | -2.99391 | -53.04313 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e815edc1-8b2f-3d9a-9077-9f94563314ed | -2.99349 | -53.04599 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fdd31d43-7743-3c08-a99a-c76701bf94ad | -2.95357 | -52.90379 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a436dfe-ffd8-3076-8966-4051d7302dbd | -2.95264 | -52.90997 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93c67fbc-7f53-3ca4-84a1-f97a2981efc2 | -2.85365 | -53.33204 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ded76dd5-4adc-3612-b4a4-2120ccfba7c1 | -2.85283 | -53.33761 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7bbd713d-27b7-3ee9-a248-30b9389ad982 | -2.84791 | -53.33682 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c0084ee7-3c30-3478-83a6-f6f6c18a0741 | -2.84381 | -53.33048 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3bbaac1-fa50-3e0c-893b-3e01fe8b5ef0 | -2.84298 | -53.33604 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6068b018-2e1c-3261-b1ed-7e2bd1d0a993 | -2.84217 | -53.34153 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 019f83ff-c23b-3131-b528-77bee24fbca6 | -2.8397 | -53.32415 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f89695d-a5d8-3344-b811-408ffd7b0363 | -2.83888 | -53.32969 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04722d8c-a2a5-3377-9ce0-22dec5d1cf27 | -2.82597 | -53.00252 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d055f0a0-ef81-3d4a-af07-e5c5a14abe98 | -2.82505 | -53.00867 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a37c7ebd-e34e-3cb4-9797-9e8bcad0e149 | -2.73913 | -53.20805 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2796cdac-7f2d-3ee9-80a1-a30e7cd61d5a | -3.11505 | -53.12489 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27f48172-9ff9-33d1-8329-459dc5f4f000 | -3.11461 | -53.12787 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff678aad-7fae-3073-aced-dc81c1214652 | -3.11048 | -53.12108 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 441f5150-d977-3827-af5b-e6f92785196b | -3.11004 | -53.12407 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d1a45eb4-2cfb-399a-b96e-14d39920678f | -3.06251 | -53.27306 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ad59a15b-1fba-3ad1-a96f-7215d1693136 | -3.04093 | -53.03893 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee4042fa-2714-3874-b85f-03dd7d99d113 | -2.99811 | -53.04956 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 652dfd07-d8fa-3baf-bec4-e91a0fd02d2f | -2.99769 | -53.05241 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff6aaf46-cdae-3e04-b8ac-47abc100eefc | -2.99307 | -53.04885 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 698d508e-f708-3322-9a57-7912ee7fd05e | -2.99264 | -53.05172 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f79e978-c641-3d2e-88f2-ed282c7edfb9 | -2.97752 | -52.84879 | 2024-10-21 05:27:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb7cfef8-87a6-3ff5-bb02-f98fad04b49d | -2.97707 | -52.85176 | 2024-10-21 05:27:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 227874e1-a201-3624-ad2c-15875ee025b0 | -2.95311 | -52.90688 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0cebc5e-207c-3507-9f08-ab48f0c5efb1 | -2.94804 | -52.90599 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1499d48e-200b-352b-814d-0a36187d1ca9 | -2.94758 | -52.90905 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7df4dae-7877-39fb-bd9d-8b648bcd33d7 | -2.85775 | -53.33836 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a298306-22ec-3241-b171-11c1ea069714 | -2.84873 | -53.33126 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77d4e8aa-9a68-32e2-8345-dbf3dc7eac1a | -2.84709 | -53.3423 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9779b20d-7c6e-3162-8ed6-c7000d059104 | -2.83806 | -53.33527 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 164ccaf1-ad84-3528-98fe-f8078b65d9f5 | -2.82551 | -53.00563 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f50886a-d790-3782-806c-8d4a66d64db3 | -2.82093 | -53.00181 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 603b78fb-8b81-3028-af12-e3b9afcac819 | -2.73783 | -53.20776 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf77a14c-8436-3009-adbe-e9e575b98d42 | -2.36584 | -52.5198 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README53.md)
