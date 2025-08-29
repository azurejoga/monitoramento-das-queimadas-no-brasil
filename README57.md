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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bd1b215-b366-32ba-8a29-2361a9ade890 | -13.62885 | -48.20198 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8305cd8-9f11-3888-99a9-9256dc4e5297 | -15.6495 | -56.01888 | 2025-08-29 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e59d0186-a770-3258-8c4a-3af14f7616af | -13.00239 | -56.9055 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2874b609-6cd4-3703-b7b7-fd55df13f4ae | -14.34593 | -53.26236 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa02fa21-49dc-3f6a-846c-99204bb11514 | -13.45731 | -46.9591 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03a14e73-4998-379f-a4a4-c46be37bfc03 | -13.40799 | -46.84378 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2106f9c4-a3d9-3ead-a89a-e77565761c14 | -13.56345 | -46.89771 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13262c71-65a3-331b-aee7-6a60d362f72d | -13.5182 | -46.85634 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 190fd6e9-2395-35fa-a38f-e4f4e57d3016 | -13.67428 | -46.87938 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9714178-dc21-3bb6-baa3-e20c99cc5beb | -18.18567 | -45.60196 | 2025-08-29 04:42:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95655eb1-d090-3811-ba5d-ff66438155fa | -13.55329 | -46.88627 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9209bb1-b83e-3679-8d76-6e0b44015149 | -13.56273 | -46.90279 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8fd123b1-7fd5-342b-abbd-8902d6bd6887 | -13.66511 | -46.91671 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e701361-0f8d-3b3d-92d4-08277736638c | -13.43586 | -46.95301 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2ba62e7-c24e-3a20-a53f-7285442dfa43 | -15.66501 | -52.76439 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 886b60f2-5f83-3c56-b2f0-b7dbc05ae1c2 | -13.55603 | -46.86668 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a689230-9e73-3a37-91b9-99d4ba319da6 | -13.99304 | -46.3309 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 447ed2ea-118f-30a9-a43b-d1e7e4055444 | -13.64507 | -48.16497 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea143d64-f3d3-3565-9121-7e9acf59d54d | -13.67793 | -46.90924 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56dcdcd2-272f-3ba7-bca9-836e3a64f6b9 | -13.37344 | -46.87741 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10937ccd-6ff4-3fc7-bb22-23c04dec3745 | -14.5266 | -53.00055 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 952b7398-be6c-361d-945f-d0868dfaccc8 | -15.17556 | -52.33676 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12762afd-a96f-3cb0-98ae-ca95f9d4c28b | -13.64149 | -48.16437 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f697f839-bd26-3a6a-aeca-9ddf2163a120 | -17.76761 | -44.49451 | 2025-08-29 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21a381cc-94d1-33ce-820e-9441cda418bd | -16.42283 | -51.10011 | 2025-08-29 04:42:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65f71554-b3ef-3e38-b447-696d139db7cd | -15.12099 | -49.11311 | 2025-08-29 04:42:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 381996de-9268-3183-b9e4-399d010fe436 | -18.21942 | -45.58439 | 2025-08-29 04:42:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69a3be70-be82-3b34-9f29-4017ee90df6d | -13.67048 | -46.87841 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 74d67142-1eb9-3f6e-9216-37751d2cbe8c | -15.1822 | -52.33789 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a9366c3-b1d8-3b2c-a3c0-63be7cace088 | -13.37259 | -51.75716 | 2025-08-29 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 710ed84c-529b-3337-b426-6d7f147d5e20 | -15.29106 | -51.43018 | 2025-08-29 04:42:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17716d39-beff-3b05-9c12-00437715d544 | -13.59961 | -48.15999 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4fcaf3e-73e6-3b1c-ae5c-d19d9aaf0a63 | -15.85049 | -48.19974 | 2025-08-29 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af7b069d-6301-36a3-b9e4-2c20f37c5d72 | -15.12959 | -48.12214 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 76c9f5a9-4cc3-34d3-babd-64582eed320c | -13.36958 | -46.87702 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22908059-cfea-31fc-a743-bdaf2f7934e4 | -13.63074 | -48.13659 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7abceb0f-2218-349c-bda6-8ea90959a9e7 | -13.00517 | -56.91403 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b6cbf1d-6eb6-3e3e-9bdc-7338bce919e2 | -10.2912 | -64.49603 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2cd25f8d-8967-3f4d-bf0d-c10fe11eb52b | -13.41669 | -46.9786 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| dc7198f6-e6fe-3ed8-8843-8520a4c4adf2 | -18.08724 | -44.7248 | 2025-08-29 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 063d15d3-6db3-3eab-8a8a-99ed965eb35f | -13.01772 | -56.91634 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c102dd84-ecd4-3b75-bd53-eda798d81270 | -13.48229 | -46.84582 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9e80eda-e5fd-3567-b5f5-c668d34f933a | -13.41605 | -46.98309 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8ddf66d9-bfbb-3e24-8a85-f54334882007 | -13.51113 | -46.93627 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85e85027-7ee0-3084-8dc3-1e9d38c8bac6 | -13.37032 | -46.87183 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d997314-fafc-39b0-b07f-a97ead62253d | -15.03878 | -48.13139 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6769210-7298-3ec1-a9c4-d5ed987bbab6 | -17.39403 | -49.00706 | 2025-08-29 04:42:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a808331-8b50-36cc-b9a7-7357226036fd | -15.13021 | -48.11777 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e7d5a978-edf6-3ca5-9e75-caa10a656846 | -14.60549 | -54.50248 | 2025-08-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cae753d7-be5a-3a92-b30d-dfcda0511baa | -13.41028 | -46.96872 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1781677e-7425-3a43-9c28-884bd382e478 | -15.6285 | -56.31418 | 2025-08-29 04:42:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a60bfe8c-1a6f-34a7-906b-eb179c94262c | -14.34503 | -53.33237 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 597e5329-23fa-3ea8-b024-22c8f1aa3d58 | -13.97877 | -46.33207 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fca6ae4-a334-3d5e-9523-67c172af6bd3 | -13.54697 | -46.87535 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d30ac287-8ebc-3eb0-a8db-779547e17f57 | -14.60122 | -54.50598 | 2025-08-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4478c106-b1bd-31c5-9fd8-d0b485118629 | -15.67345 | -52.7546 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4decdc73-2e57-3b00-88bf-139f5d4e3430 | -15.84006 | -41.85286 | 2025-08-29 04:42:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76161ea2-2b57-3760-9501-98a715383078 | -12.63166 | -60.24546 | 2025-08-29 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 251c8d1d-1826-3efb-b3e1-6f7ce6f830db | -15.6707 | -52.75038 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39cafeda-59b9-34ab-b1f6-714bd3762e59 | -13.00446 | -56.91796 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e76f2e09-6675-3c0c-b07f-982afc3181e6 | -13.99657 | -46.33505 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fe3ab27-3309-3f70-b9c5-876b935f54e2 | -12.99678 | -56.91261 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69302c43-5856-3787-a722-f5972b52e5e4 | -15.19068 | -53.78963 | 2025-08-29 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e974fcd-d48f-3720-bc62-c8df0c1335a8 | -13.00306 | -56.92573 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 564593a6-cf3f-38fc-a226-fe62704ce454 | -13.66256 | -46.907 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22243aab-e35b-352a-a8e4-9eba3605b209 | -13.55082 | -46.87584 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31e7a923-52dd-3f44-bf6f-1f273980dc1c | -18.25182 | -45.15477 | 2025-08-29 04:42:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2d04c2e-4b7d-36af-ab0f-27023c8bde6a | -15.84045 | -41.84926 | 2025-08-29 04:42:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7a26464-8f8a-39aa-a325-1faf73ca740a | -15.66442 | -52.76804 | 2025-08-29 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23327f96-1e49-3a4b-8165-bbaa69e4b85a | -13.83594 | -46.70044 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00ab517e-22dc-38df-9af5-60ad01bbacaa | -13.66191 | -46.91157 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c602140f-f7a5-31e7-8a5d-c9c14dca68b4 | -17.04918 | -45.8834 | 2025-08-29 04:42:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a985549-a1d3-3400-ba33-5926689d3e66 | -15.83967 | -41.85645 | 2025-08-29 04:42:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 366893d3-4862-3c84-9748-c30418debe38 | -13.40779 | -46.98656 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b2e95d9c-1afd-3870-8713-e001253684bd | -13.55645 | -46.89174 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c92cdae-3e7c-3231-aa12-2f386cd05c6f | -13.58296 | -46.87064 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0293a9e5-3040-31c4-b45d-586b6db01ddb | -13.5607 | -46.91726 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 176c41ca-5a6b-33aa-9c6b-e8f8d984fb38 | -13.44797 | -46.95009 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c870a58c-f028-3e58-b877-7b03d0ea6736 | -17.76843 | -44.49483 | 2025-08-29 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13f0402b-409a-3a8a-85d8-09e406e2043c | -15.12531 | -48.12595 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0e7d8b8d-0542-3f98-b7a4-212ca3c5c2db | -13.02259 | -56.91326 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25ab8cb0-3692-3caf-bb18-da006c74fea3 | -13.61585 | -48.24213 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 288829ca-76e1-31a6-841f-5f3e95daf9d1 | -14.79352 | -59.71239 | 2025-08-29 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ad50f5d-a654-3320-b3d3-33fe933f71df | -14.62589 | -41.74282 | 2025-08-29 04:42:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d024d5d2-779e-3148-b7b7-947a763e65e7 | -15.04243 | -48.13195 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fd488988-8434-36f5-a047-56842e00670e | -13.5721 | -46.8641 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d556366c-f072-390d-a606-050df6bdcff4 | -13.51423 | -46.94209 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31e6ab43-818f-3c48-81f7-b876fb55db0e | -13.57527 | -46.86945 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed5c43d9-c4f1-3bc7-b39f-5a02d6284083 | -17.75637 | -44.5077 | 2025-08-29 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 18711a53-323c-3594-b0fd-5fe4456e5b1d | -24.17365 | -49.5643 | 2025-08-29 04:44:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 803e2540-e850-360e-9533-ff0cb1756cfb | -24.17678 | -49.56985 | 2025-08-29 04:44:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fe902e01-1e42-3865-8913-2805f827daf8 | -19.1474 | -57.78875 | 2025-08-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5e523848-c85b-32fa-8b76-433af101ff64 | -18.98197 | -52.94271 | 2025-08-29 04:44:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ac2aa7dc-a9ee-364d-98a2-e1c3e0763d1f | -21.02447 | -44.79627 | 2025-08-29 04:44:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bf0c02af-6fd6-3bbb-9263-e822ae828f52 | -20.49056 | -53.72595 | 2025-08-29 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01ca8e79-d757-3fc6-a57e-4e24066018c2 | -19.73901 | -45.8429 | 2025-08-29 04:44:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f45b87f-09a1-3a54-b88c-8aded0a08957 | -20.08817 | -44.34128 | 2025-08-29 04:44:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5f1632ec-e0d0-3a54-8628-489c4c282c99 | -24.16921 | -49.56895 | 2025-08-29 04:44:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 676ce5fa-5c63-3ccb-8f7d-42814025d344 | -20.28429 | -41.30274 | 2025-08-29 04:44:00 | NOAA-21 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d3bc91e6-cd5f-3644-8022-de622cc20d4a | -21.01421 | -45.06504 | 2025-08-29 04:44:00 | NOAA-21 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README58.md)
