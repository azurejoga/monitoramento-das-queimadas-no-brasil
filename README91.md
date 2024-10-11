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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de4d8213-6794-3ea5-84db-f4617e2e17d8 | -11.16847 | -54.78188 | 2024-10-11 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 018bebd0-c2e5-3531-b1df-61b1ca74daef | -11.16083 | -54.777 | 2024-10-11 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc514730-3a6d-327f-98d2-fe2e5b17270c | -11.15319 | -54.77206 | 2024-10-11 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86ab0b84-435d-3ac4-981d-6ef4d394e007 | -11.14316 | -54.01848 | 2024-10-11 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abcd12fa-26b1-3655-ae0c-fd043a83a7a1 | -11.1426 | -54.02252 | 2024-10-11 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa02992e-a1d4-38bc-9d32-d9f2df796f6c | -11.1414 | -54.02149 | 2024-10-11 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d514bc9-5a69-3dda-a214-07278c4cada9 | -11.0893 | -54.78284 | 2024-10-11 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9841d371-436e-34e4-bf49-7f91c0eaccd7 | -6.16338 | -55.47628 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 503606c6-ef8f-3e27-a883-98643d2e8b6d | -5.80511 | -55.75005 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c42ac6e3-5adb-3679-afe3-92a113b45024 | -5.80448 | -55.73903 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 21216116-4d00-398a-a1fa-832263ccce0d | -5.80335 | -55.73719 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ac7e42c1-5bd8-3108-bb9b-14daad300554 | -5.80274 | -55.7413 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ee367ad9-d929-3281-8ff6-924e8de6d6f5 | -5.80213 | -55.74542 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 68110936-78ae-38d5-ac6b-d6c015f1c3a4 | -5.80089 | -55.73848 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e799b56c-9da1-35ae-a477-ff8d7f1d2506 | -5.79963 | -55.74669 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f281adc1-1bfd-382f-af08-cde6ccd339a2 | -6.29628 | -55.36604 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69f6859f-45d6-32e7-b4c9-cc5d6226c94a | -6.29598 | -55.36456 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cfcf07d-6f7c-3d72-a99b-02aad831357a | -6.16979 | -55.51033 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b2f2f52-2bea-30fa-aeab-4ae50a40d9cc | -6.16908 | -55.51217 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 278794c0-24c3-3048-a171-94b560ae3efc | -6.02307 | -55.63459 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66171487-37d5-395b-be21-cd8ee8bdc072 | -5.80385 | -55.74313 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 168c9cb0-6960-3a26-9d1f-770a503a8698 | -5.80322 | -55.74723 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| dd0aff1e-99d3-3ed2-b9b9-ebfd0bbf2c1e | -5.80153 | -55.74952 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d064b8ff-40fc-306d-b920-21c9e6f476b1 | -7.39991 | -55.48946 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c3b8db6-d259-3217-855a-b6e4561013fe | -7.39926 | -55.49388 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| faff6a5f-e7e5-35b6-99cf-9fc363b3c179 | -7.39555 | -55.49331 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 265e1efc-7024-3b21-b1d1-afde1dabaa00 | -7.364 | -55.50204 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dbf93990-ab2c-3d5f-875d-17038f1333ae | -7.33303 | -55.07367 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08ce24ad-3536-3e0e-a1c9-bf9dc68b05d0 | -7.17054 | -55.54839 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8512e288-8821-3872-b22b-9169bfc76a07 | -7.10419 | -55.64251 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 256393d2-b37d-3654-8df5-30b559850ee9 | -7.09113 | -55.45324 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f4081f0-51ae-36c8-93c9-ac55d30384c1 | -6.8997 | -55.0461 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8cf5536-12e0-387c-91ed-aae96a06b055 | -6.89592 | -55.04557 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c272538d-8118-3499-89a2-5a119b83bc96 | -6.8908 | -55.05208 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11315d73-524e-341a-9260-2c4225cff429 | -6.88502 | -55.14693 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e6218b7-ca22-3d8a-95c3-d0041f1f0c1e | -6.88436 | -55.15147 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fadb8f85-3bfe-33ed-889b-304223b8c439 | -6.8804 | -55.09938 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| faaacfd5-edef-3da0-a58f-428cb9780fd5 | -6.8801 | -55.09721 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 496df91b-6485-32e2-bde7-eb95ddafe01f | -6.87664 | -55.09882 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5be45269-f985-3d0c-abc1-29f7c8d1f711 | -6.87633 | -55.09665 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57827040-0673-3ddb-a9fc-d42afd1d8177 | -6.87622 | -55.31129 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff8b4177-8428-3274-92d8-74e3a8ce3d2d | -6.87564 | -55.10123 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d17a340a-ecf7-32e9-9e97-b772c8a29ef4 | -6.87178 | -55.15886 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fb5b969-1c6b-32be-9813-facc34ff5300 | -6.87109 | -55.15662 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2797e069-b1ec-3511-a659-e9aa5183c68b | -6.87041 | -55.16113 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b2d61d4-77c6-3c73-8edc-e1a26268e48b | -6.86803 | -55.15832 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 200cba13-e191-3e5d-8939-1eb1511431f0 | -6.86493 | -55.15324 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 209dcca1-da37-30bd-af11-e65ec1241d3d | -6.86359 | -55.15553 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 917bd621-7b0f-3708-ba2a-22906d028ffd | -6.86095 | -55.07099 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e710ed64-c270-3f5a-9cd9-1b48c06c4184 | -6.85678 | -55.14981 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e29608d-115b-3cf2-a001-55a160ca8aeb | -6.85609 | -55.15438 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 771d046c-bd2e-37eb-90f6-8203f434151f | -6.64744 | -54.94452 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a09ea02a-b697-33a4-afe2-b205899e41dd | -6.64365 | -54.94393 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4127f25-b301-3281-8343-4b1977749d9d | -6.63919 | -54.94791 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68ad9a5c-3d77-360e-be97-8f246b8b769b | -6.63851 | -54.95248 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 089a6afb-931e-3319-a9b7-57f1f4d4513f | -6.58915 | -55.40916 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbc1f726-a429-3d7c-86d7-84e08f7f1993 | -6.5731 | -55.41567 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 596097fe-f358-3a0a-ac2d-4f45bf4b9a87 | -7.96697 | -54.7914 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ec86519-9f54-32f3-8fa2-e2edc0b1f926 | -7.96644 | -54.74049 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae84c507-d847-3729-925f-1c4ceb7d36e8 | -7.96599 | -54.77088 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42c3b3eb-ee61-31ae-8ea0-f16bf21b23dd | -7.96282 | -54.76532 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bca4563-ad3e-3a5f-be3b-2abaf68b3ca3 | -7.96254 | -54.73988 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f4f3387-25ab-3849-ba90-8836883131f9 | -7.96209 | -54.77028 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7cfd020-9d55-321a-9550-a8496ef64c0f | -7.95964 | -54.75978 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 899b55d8-2aa5-3df8-9c10-68a9721ed815 | -7.95892 | -54.76475 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6a33a81-f9c8-39de-a526-092d81fa0cef | -7.91083 | -54.87788 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 150d74a6-e55a-3c39-bb4d-9393a3da59b0 | -7.91012 | -54.88277 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03629100-c55d-3ada-af1a-9243e5abd15d | -7.90296 | -54.76656 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e447a7f7-9cfb-3484-b38b-e078fd3a842b | -7.90142 | -54.76989 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c57bd10a-b2b4-350a-a0a7-5cd0b9ac283d | -7.90007 | -54.73074 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7caa679-878e-3354-9ef7-cf56bb5f92a6 | -7.8995 | -54.72926 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cef056a5-e0f0-304e-b87d-77daa428f8f0 | -7.84706 | -54.89638 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4609666-3cb4-34f4-8b2f-0eaf4108e079 | -7.84249 | -54.90065 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95486dbf-4198-38bd-add2-5a1b041f67ef | -7.8285 | -54.72427 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 01ca6a4f-c25d-370b-9b9f-cbd40a0779bc | -7.82781 | -54.72909 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| de8afcc3-e73b-3c97-af65-4461482e58de | -7.81042 | -54.71141 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbb0c0d0-c6d9-3a30-9a60-ae5ecd3e589c | -7.81004 | -54.70963 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d30049d0-57f4-36a6-a9c9-a040c4be7b0e | -7.80655 | -54.71062 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59fc8254-6b7f-3891-a0c8-e47814d85210 | -7.80617 | -54.70887 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5838892a-3931-32ff-8549-74873efcf925 | -7.79128 | -55.22216 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f82f426a-53fd-3190-9c1d-09b3437e4081 | -7.73155 | -55.72693 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a98f380-ba7a-3d6a-80f3-b88133db2cd9 | -7.70309 | -55.16419 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13b416bd-7777-3f53-bfa4-cf33e4c3111e | -7.7024 | -55.16882 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b91ccf8e-cda5-3783-9cfc-37b87de051ee | -7.60243 | -55.56139 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c4c3dc5-793f-3234-ba1f-7f25daa7834c | -7.40231 | -55.49887 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00da6c1f-0b58-399f-bf02-f4fe729ee3cd | -7.3611 | -55.50393 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46af2b7b-0284-38c7-b9c9-0cc8682a49a1 | -7.17468 | -55.04489 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf8d8e60-8eaf-3ec4-92e5-a6f1983921fd | -9.29012 | -56.21725 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0acdf8ff-33b9-34fe-a3c4-19cbad7f141c | -7.89962 | -56.02942 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28912a81-5c9d-347a-94a0-e69656a83647 | -8.49583 | -55.165 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4adbe7c0-c9da-36f8-a299-84fbe9fff64b | -8.49336 | -55.16289 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d79795c5-d91e-3eff-89aa-06f9a310888e | -8.49267 | -55.15966 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dd1898b-7eb5-367f-b0aa-8cd3f437949d | -8.49264 | -55.16769 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bda98c21-3a17-35c5-aa16-f9e8e540c88a | -8.49199 | -55.16445 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb767224-aaa6-3a69-a9d4-85a513878af7 | -8.49131 | -55.16926 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7f9b819-babd-327e-b2e1-4364cb919e74 | -8.48953 | -55.16233 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d981b6a-0ff3-366b-bf2d-b792aa724e3f | -8.44571 | -55.4567 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fe07d94-4699-35ff-8274-7268faa11fd8 | -8.44194 | -55.45615 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27472c18-e5c3-377a-867d-7d723eb080f9 | -8.44127 | -55.46069 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f914674a-8f89-3351-b862-648cf2ed8f90 | -8.43991 | -55.4698 | 2024-10-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README92.md)
