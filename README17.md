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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 203b9092-c1a0-3b14-9d28-fd3557e521aa | -5.07239 | -37.71786 | 2025-08-28 03:15:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 692cb0e1-0a66-3887-8302-0371f91ea0d8 | -4.66803 | -41.02465 | 2025-08-28 03:15:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c271f5c1-39b5-3f43-be71-523b54a11d0e | -4.67455 | -41.02593 | 2025-08-28 03:15:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c1c1eb1-e2fb-347d-80cf-e8d7b8492ffd | -5.53356 | -36.85094 | 2025-08-28 03:15:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f8d55d05-5e85-3ca4-bfd9-8d200ec3fcdf | -5.53452 | -36.84532 | 2025-08-28 03:15:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a4cfc3b9-07e9-3c10-b468-e110d7f1dd14 | -5.23053 | -39.37337 | 2025-08-28 03:15:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 20f72033-b9e8-3991-8f6f-42461a53c51d | -5.2298 | -39.37757 | 2025-08-28 03:15:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| edac651c-8cb4-338a-957d-225d66c7d3e0 | -7.3922 | -39.69271 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 59.3 |
| e2739a77-fbd4-3d7b-b453-c4297f4bfe1c | -8.4382 | -41.44629 | 2025-08-28 03:17:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 5666f35c-4dab-375f-9a8b-3059daeadf73 | -7.24672 | -39.17936 | 2025-08-28 03:17:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c9b36ee8-9c1d-32c1-9a94-afd478229724 | -7.63535 | -42.67562 | 2025-08-28 03:17:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 83201ee2-3547-392e-bfb3-8d96d71ff5da | -7.39723 | -39.69781 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 2283ab64-a902-3b57-a59a-ad9fafbb22b9 | -7.38792 | -39.68353 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1921ee8d-5726-324f-a72e-98cfa0f2df51 | -7.42218 | -40.08434 | 2025-08-28 03:17:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2a24b3d6-98ef-37cb-9a8f-d221fbdef320 | -7.39872 | -39.68962 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 43.4 |
| 1b58a3db-5ed7-3e49-9abb-6651535d214c | -8.4401 | -41.45618 | 2025-08-28 03:17:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 066003d8-6ff2-36f0-a2bc-60b0ba904837 | -5.68669 | -40.97718 | 2025-08-28 03:17:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5e26dd95-9b28-34aa-aa9a-359525e3785a | -7.63659 | -42.6693 | 2025-08-28 03:17:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a100f60d-f0d4-37e8-9e84-8ba4335df80a | -6.43305 | -37.13604 | 2025-08-28 03:17:00 | NOAA-21 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 75f78545-ea0f-33d8-9a2e-32d98ddfe693 | -7.39946 | -39.68553 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 43.4 |
| 1982310f-c0f6-336f-a470-5597b66bf5a3 | -7.38642 | -39.6917 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 389eec5c-eef1-3681-93dc-be60bed15611 | -7.6267 | -42.68322 | 2025-08-28 03:17:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bf1219a2-6bf6-3395-b297-f4f88aaf0213 | -7.42887 | -40.08111 | 2025-08-28 03:17:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3113296f-29d0-3be4-b004-f2c5845d0736 | -8.44108 | -41.45085 | 2025-08-28 03:17:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 367f124d-1042-383f-90a8-77d6f53f4d26 | -7.41709 | -40.07881 | 2025-08-28 03:17:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b32ca200-d3f8-3089-9855-3173faf52225 | -7.62793 | -42.67675 | 2025-08-28 03:17:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 61844086-b6bd-3310-be45-0cb8d0afa953 | -8.43713 | -41.45182 | 2025-08-28 03:17:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 0c4e4c40-6450-38c8-8f1b-a196a8958b12 | -6.43801 | -37.13685 | 2025-08-28 03:17:00 | NOAA-21 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8fc11296-6029-3b31-b33d-9c6220f4db6e | -7.62723 | -42.68069 | 2025-08-28 03:17:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 634cb397-4908-3fd4-ba50-b57c34e81eb2 | -7.636 | -42.67174 | 2025-08-28 03:17:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b0e82e81-6c64-385b-866a-f855e60a7606 | -7.42331 | -42.05836 | 2025-08-28 03:17:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c3d5b27f-3e0a-3cfd-a56d-6f58cb755bbc | -7.42807 | -40.08549 | 2025-08-28 03:17:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d784c922-7509-3284-8255-96721bef3842 | -7.39444 | -39.68045 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e2d57374-f599-385f-9d7a-ef98f9bb1d38 | -9.31653 | -40.20733 | 2025-08-28 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| adc42487-d05b-32e0-a836-90bba2eb880e | -7.39369 | -39.68452 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 43.4 |
| 3427bd93-e7fa-3e29-bffe-6862a818f02f | -8.44208 | -41.44546 | 2025-08-28 03:17:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 8088ca14-7849-3161-a711-6b3cbf9fa85d | -9.31583 | -40.20848 | 2025-08-28 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0141c7aa-1e52-306d-b103-e2632cb25387 | -7.39145 | -39.6968 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 109bf309-60bf-388a-b961-e12f49355e19 | -7.39573 | -39.70602 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 92a47147-3402-3334-8fb6-e59c3e9cd7e5 | -9.31659 | -40.20435 | 2025-08-28 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| adf023b0-8987-3037-b254-604272c9b8c4 | -7.38995 | -39.705 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 921a83bc-3d44-3f37-b255-16de90c0da98 | -7.38717 | -39.68761 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bbfed4ed-e923-38fb-9109-91f84f13a6ff | -7.3907 | -39.7009 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 24fd22cd-68a1-3fab-9a4a-44335eedf472 | -7.39797 | -39.69371 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 867d377f-ab10-35c8-9e56-b4e5726f1c4a | -7.39648 | -39.70192 | 2025-08-28 03:17:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eda92212-5058-3a4c-99c6-3868a3e2b230 | -8.44344 | -41.45306 | 2025-08-28 03:17:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 84e6dacd-4568-39c3-af6c-7eb65025c21c | -7.42298 | -40.07994 | 2025-08-28 03:17:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8d403832-5699-33b1-b558-2eddeca39d35 | -11.34267 | -43.55025 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 1e4161bc-6543-3597-8d93-5fec9bb42532 | -16.37071 | -43.79367 | 2025-08-28 03:19:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1c2f1b9-b071-34d8-ba3b-e37f76af77b1 | -12.35512 | -38.28148 | 2025-08-28 03:19:00 | NOAA-21 | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b27acd05-f346-310f-b538-6dde8ba76432 | -11.33299 | -43.52884 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b13be3a4-47e4-37f6-a010-3ea44c9bd208 | -12.95279 | -44.58122 | 2025-08-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 97099bfe-5535-347a-ab4c-f27189380587 | -17.76204 | -44.48972 | 2025-08-28 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3d2ef897-9b2d-3aa1-8118-e8387d742ea4 | -11.33035 | -43.54135 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa0729f8-4d8c-3ae1-aee2-107af815759d | -11.34661 | -43.53145 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 78596a7e-d344-3557-bb32-023d6f85e7e4 | -11.33881 | -43.5294 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 52078a80-4d2d-3e4e-b81b-7599cf15b08d | -12.9659 | -44.57735 | 2025-08-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| b337ffeb-f72c-3436-8367-2da6fff2ccd6 | -11.31676 | -43.53856 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdb422cf-b719-3b87-b5d9-ee75e6974377 | -11.33846 | -43.53648 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 34188107-d0a2-3b56-b0db-ef713e422528 | -11.3418 | -43.54955 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| fb60b16f-6348-3662-b524-c855cd5d43ae | -11.32139 | -43.54539 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d43b65c1-2d9e-3734-85c6-069be433416a | -12.95743 | -44.58252 | 2025-08-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| c89dfe6d-5e62-3fbb-86ec-37373db42e83 | -11.32355 | -43.53995 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b3ee424-b8b9-31c3-8bb9-ba41def9ecc9 | -11.33753 | -43.53572 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 18d0ce81-183d-39d8-bd08-f7244d3adbb4 | -12.9582 | -44.59026 | 2025-08-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 08e78d65-1ab8-3267-bca0-364e66f1201d | -12.96267 | -44.56917 | 2025-08-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 832a3094-f792-3cf8-8c7f-4db5806672c2 | -15.70826 | -41.75823 | 2025-08-28 03:19:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6edb674d-6806-3422-ac9c-02b10972df2a | -17.81156 | -44.51147 | 2025-08-28 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82be467a-bfeb-3d49-b4ae-2d7c175951f8 | -11.31841 | -43.52526 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac78af6b-2503-35c4-9b43-0ec2278672bf | -11.34562 | -43.5307 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| ff13eede-b281-3c85-829d-f1079397ca36 | -12.96044 | -44.56876 | 2025-08-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| ea94fbb1-f945-3671-a554-b026c3b50f3f | -11.32649 | -43.5204 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| baffba2f-d51b-3f32-bcc4-0cd7ce41d6fb | -17.81663 | -44.51871 | 2025-08-28 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 556ebee4-c43a-3afe-85ff-9da280668909 | -11.33716 | -43.54271 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 5ae4970a-bd17-31da-9cc2-c93b312c5a69 | -11.34434 | -43.53704 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| fb111442-f56f-38a4-8f75-c18d6ceeb6cd | -11.33201 | -43.52802 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8584b75b-8e32-347c-bf46-d401bb57a1e2 | -11.33073 | -43.53432 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bb8ff5f5-051b-35cf-ad2d-dab1093919a7 | -12.95585 | -44.58974 | 2025-08-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a3f37c82-c5a8-32cc-9c03-69e324d76f72 | -11.33329 | -43.52175 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| da2d1d39-0558-3940-929a-f16c26b521ef | -11.34396 | -43.54406 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 6e8cee87-7252-3c43-8f1e-88fc92b4ca17 | -18.08204 | -44.0657 | 2025-08-28 03:19:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebd274d4-02f5-31dc-b599-31d35bd57637 | -11.33979 | -43.53017 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 0e96ec4f-85f9-371c-9386-7339079e6437 | -11.34528 | -43.53777 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 3e9e6e08-9eeb-360e-88b7-aefe4d4f79eb | -17.76002 | -44.49856 | 2025-08-28 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 28df1a7e-56d8-3b83-be3f-253611bb45cc | -12.95428 | -44.57421 | 2025-08-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 79fb9440-5b3d-30ee-ad2a-08f7338908d1 | -11.335 | -43.54815 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 574a42b2-b8f8-37cd-a35c-69b51b80b4b7 | -16.36434 | -43.79249 | 2025-08-28 03:19:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4427eb9e-b280-3ac4-8d49-2f8c06857326 | -11.3343 | -43.52256 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7659319e-ab17-3eb9-a19a-7d1918c3b92d | -16.54523 | -42.34698 | 2025-08-28 03:19:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93ba9706-d38f-39e4-bc6a-e1af3dbcb0aa | -18.99099 | -40.29123 | 2025-08-28 03:19:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f8fe4c9-14e6-383d-8688-d880b21308e9 | -17.81593 | -44.51966 | 2025-08-28 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 23731557-f249-368d-b23e-9f5595b0fdad | -17.75362 | -44.49706 | 2025-08-28 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5700773c-51bd-3b1b-b282-abed46b8a85c | -11.32905 | -43.54752 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1b93c57-db62-3d2f-a35e-b47a214552e7 | -11.34306 | -43.54334 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 4ea9148a-cab6-3a56-bfe4-4428b31c8fdb | -11.32521 | -43.52665 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95f1de8c-d8dc-3946-9467-a156b69ee102 | -17.81723 | -44.51387 | 2025-08-28 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8cb49551-7b51-3d17-97ac-01c442e1ce74 | -11.32618 | -43.52748 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 84754506-118e-3943-98c1-f563be22582e | -11.32819 | -43.54678 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 50033406-a6b8-3732-bdf8-c86ff709ee3f | -11.33626 | -43.54197 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 307ab2fd-f2ec-3f24-af6b-f5cc8c93feb4 | -11.3207 | -43.5199 | 2025-08-28 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README18.md)
