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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a7a150f-8380-33ce-9c64-dd37eeb2aeb9 | -11.60594 | -54.69276 | 2024-10-10 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f96c8fa2-61fd-3d20-b8fe-a02862d19e26 | -11.60071 | -54.68823 | 2024-10-10 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3daca4f5-5a14-3e64-a58f-0821155036bd | -11.60024 | -54.69213 | 2024-10-10 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f53514b-ce5f-3ad6-8986-109c5224df72 | -11.35992 | -55.42377 | 2024-10-10 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a4ab0c8-271f-328c-8c62-7e5b37cf4a5b | -11.3578 | -55.42123 | 2024-10-10 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| babde080-043d-3bfd-a37b-71130ca64985 | -11.35736 | -55.42467 | 2024-10-10 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 093fe3dd-ecc2-32af-a92e-53235798617d | -11.17468 | -54.78102 | 2024-10-10 05:38:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b98c519c-a591-39d4-9025-f65df9cfd5ee | -11.17422 | -54.78476 | 2024-10-10 05:38:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96cc804c-5c1f-36e3-8486-99841770c2c8 | -11.16954 | -54.77641 | 2024-10-10 05:38:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67253c9c-7d7e-3d46-bd3b-54d3b7869c47 | -11.16907 | -54.78027 | 2024-10-10 05:38:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d97edbed-11ae-3ae8-b286-98cde015618d | -11.16393 | -54.77559 | 2024-10-10 05:38:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3ed1690-6b6a-3a6b-aac9-527379d37dd0 | -11.13799 | -54.01327 | 2024-10-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1c8d381-9487-38dc-a52b-6474d37dccce | -11.13748 | -54.01748 | 2024-10-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 474aea1a-177d-3117-b31e-6a4e1b2e4073 | -11.1331 | -54.00395 | 2024-10-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e012700-5950-3a93-b966-e17bdd613f2d | -11.11613 | -54.29324 | 2024-10-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 060c8303-85d6-30f0-a176-c8a54a255c86 | -11.11035 | -54.29235 | 2024-10-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 978f780b-23fd-3b1a-b2cc-32c83b28e147 | -10.97929 | -54.00152 | 2024-10-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2779c6c7-7ad7-3849-b9a3-56933f952306 | -13.4318 | -54.69255 | 2024-10-10 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66221b43-f804-318c-a361-37fc03f5f140 | -13.42598 | -54.69188 | 2024-10-10 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43dfb437-15de-3730-aa64-5ff6c67d4a35 | -12.67302 | -54.71865 | 2024-10-10 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42f8e24c-788c-32e5-86ab-49d0c49aa343 | -12.67255 | -54.72267 | 2024-10-10 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a02ef9f1-3f6a-3137-b69f-55ef32bbe12e | -12.66872 | -54.70557 | 2024-10-10 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1aeefcf-4e9b-3879-9ed8-17b96ef10e5b | -12.66823 | -54.70971 | 2024-10-10 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f554f9b2-3d76-321f-96f7-033644f1f0e3 | -12.66775 | -54.71381 | 2024-10-10 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1572a4fb-b432-3548-a801-00423c14306a | -12.66727 | -54.71785 | 2024-10-10 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92d2698b-ef17-3926-a46a-042604423757 | -12.60238 | -55.21825 | 2024-10-10 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc89fe37-ebf1-39ef-973c-85f5080b3cd8 | -12.60194 | -55.22196 | 2024-10-10 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 142b2db4-72a0-36ee-8c22-2be0a3edd073 | -12.59639 | -55.22118 | 2024-10-10 05:38:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 163dcbf1-f72d-32fc-83e3-0d630b247f5e | -12.59594 | -55.22493 | 2024-10-10 05:38:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39374006-5980-3f6c-86e5-9a5de7ddabfd | -12.59082 | -55.22052 | 2024-10-10 05:38:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eadf10e6-fcf8-3567-849a-bc60c731e061 | -12.59037 | -55.22429 | 2024-10-10 05:38:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92b34e97-1507-3a00-8ce7-eaa45ae64776 | -12.4072 | -54.56978 | 2024-10-10 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6af1156a-fb1c-37f2-a7ca-8f07f3111758 | -12.40673 | -54.57391 | 2024-10-10 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 30d37db9-1e40-36e4-abaf-8a6126028243 | -12.40667 | -54.5689 | 2024-10-10 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efa4cbc2-6c2a-3502-bc2f-ef87d0fa1260 | -12.40626 | -54.57808 | 2024-10-10 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1dca82c7-2a60-3fd0-b7a6-2edb2831d26d | -12.40617 | -54.573 | 2024-10-10 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 43d25a71-09d7-3a95-b79d-41de130acd5c | -12.40567 | -54.57715 | 2024-10-10 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4fd525f3-015b-3dd8-bb63-a949c01e17ad | -12.40516 | -54.58134 | 2024-10-10 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 82438776-ce8e-30fc-9d35-af134bd20ed5 | -8.62802 | -55.26121 | 2024-10-10 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0515ff66-6b1a-35c4-a608-a8e1b5bd87fd | -9.49025 | -56.07944 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c9ff719-178f-3e80-8d1a-aab72a894c91 | -10.6292 | -55.88309 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26fb6e0d-fee5-355a-ad7d-7555d72ecdd8 | -10.62879 | -55.88625 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3dfafdc-379a-3a2f-a14a-8b8ebf42de82 | -10.62839 | -55.88931 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17ef9078-b22b-322e-a62f-03492bbd61c0 | -10.62799 | -55.89234 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 11232721-23b8-3796-be6b-9c7f57cf7c8c | -10.6276 | -55.89537 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cac81f4b-98ac-3ef9-a7de-8ba7f90398eb | -10.62429 | -55.92074 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41dc6a62-ccda-3a8f-8c3e-0483b8832959 | -10.62388 | -55.9239 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f1af791-15ef-3053-a914-9c651728a7a6 | -10.62364 | -55.8853 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39578f74-75fe-3b70-862b-764ae3aec459 | -10.62324 | -55.88838 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b252a716-6dc6-3fdf-9f63-56dc359dec69 | -10.62284 | -55.89146 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce5bfe27-2fa2-39da-8a22-cbd5b05fe945 | -10.62243 | -55.89457 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f91e23e-cf74-3ac1-99cf-1346fd1eb273 | -10.48671 | -55.61953 | 2024-10-10 05:38:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb04a19c-cd6a-3981-95b8-34f9c5b342fb | -10.48201 | -55.61638 | 2024-10-10 05:38:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfc7d01b-9a6e-3322-85b2-6dc8438b7409 | -10.48185 | -55.61552 | 2024-10-10 05:38:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5dc1338-5737-3c04-a633-2f60c0257de2 | -10.48158 | -55.61968 | 2024-10-10 05:38:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef72e2b3-d7b3-3ed5-a516-105315862132 | -10.48144 | -55.61884 | 2024-10-10 05:38:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90dc5454-f1a7-3053-8855-475666970c9c | -10.3601 | -55.86053 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 1037a6c3-e246-3266-a183-3b20877df779 | -10.3597 | -55.86367 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d673ba93-80c0-39c7-a1e3-fe6264643a1e | -10.35931 | -55.86679 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| d3e46969-63af-39cd-af44-d7ef1212c363 | -10.35493 | -55.8598 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8cf5e7ae-def6-3ed3-a77f-cbbfff074c9a | -10.35453 | -55.86296 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c5c8daca-26d3-32f0-bf1d-e42e2ce78b7e | -10.35414 | -55.8661 | 2024-10-10 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d1bc97fa-6147-3b1f-a275-143d39c5148c | -11.89483 | -56.21131 | 2024-10-10 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1421fa90-58d0-3e8f-9b50-51648c172886 | -11.89445 | -56.21446 | 2024-10-10 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56b6f442-42ab-3d5d-b341-5b685c637d26 | -11.89359 | -56.20528 | 2024-10-10 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4726381b-89b1-39e3-ab8b-3a193a14ff65 | -11.89319 | -56.20842 | 2024-10-10 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83e43e0f-cf7a-3a53-83e9-1fcc84880350 | -11.89278 | -56.21156 | 2024-10-10 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 137bc6b2-4819-31b0-8764-6f749ac6aa07 | -11.89238 | -56.21469 | 2024-10-10 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5221cfd-c918-314d-9c47-a835f253b12b | -11.89045 | -56.20423 | 2024-10-10 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0660915-85c7-34f3-b796-cd4aadd55e1e | -11.88968 | -56.21053 | 2024-10-10 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccb6dea6-fddb-389c-b321-e8ef6c13a6ae | -11.9344 | -56.96595 | 2024-10-10 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f96cd64-2d6c-3e46-887d-133d7b44b37e | -11.9288 | -56.93095 | 2024-10-10 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39b4b6dd-a9aa-3575-8f17-e6a22037979a | -11.92459 | -56.92464 | 2024-10-10 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| efc5f3de-80c0-36b9-9533-4c94d4bb4af8 | -13.06375 | -57.26117 | 2024-10-10 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4976ed85-736a-386e-ab4e-472b421bb1c5 | -9.94783 | -58.11664 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93ff3696-57c2-3ed2-a30a-f4aad929d8f1 | -9.94725 | -58.12094 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bd7cd21-4143-32b1-95c0-d9a6505613cd | -9.94667 | -58.12529 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d8bf1a4-5d17-3990-9bf1-0659240614eb | -9.92079 | -57.47871 | 2024-10-10 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b7e30e96-e5d6-3a6f-b633-82c6a2225e7e | -9.9164 | -57.4769 | 2024-10-10 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a5791fed-29ea-327d-8763-d072c9debec0 | -9.91624 | -58.11766 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65ee82af-7872-389e-8255-afe70b49fa26 | -9.91619 | -57.47806 | 2024-10-10 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9b7e57a3-349d-35d8-9dfb-59b24223777c | -9.91573 | -57.48172 | 2024-10-10 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6dfd4c8e-9ad1-32a0-bc79-a4238fc40147 | -9.91564 | -58.12199 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e6dda99-b713-3f8b-8ef9-e1ed152c8f9c | -9.91556 | -57.48288 | 2024-10-10 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1ffc302d-c407-340c-9c0c-b8ce779232c9 | -9.91503 | -58.12632 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a06aebd2-ae95-3841-991b-5f1cf2fbc4ad | -9.91442 | -58.13064 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f1eb451-231a-341c-aae8-e1ce2431bdfe | -9.91185 | -58.11702 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f9ed6f1-2498-3acf-8bae-42da0f063421 | -9.91124 | -58.12135 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33c58264-ed36-3c2e-a55e-68d20e27c5c1 | -9.91064 | -58.12568 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc8e8968-314f-39c2-a1f5-f3a618e21153 | -9.90684 | -58.12075 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3f235e8-2270-3bba-9913-67a99f2f4128 | -9.90624 | -58.12509 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efb8e49c-e347-3fb6-a1a2-aa9a1f493bb8 | -9.90563 | -58.12942 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47928612-fc44-3c33-aea5-545a0ef17a9b | -9.90503 | -58.1337 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23c8ad96-0a07-3d27-a3e7-67be39677b3d | -9.90244 | -58.12016 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f4e3244-af51-3b1a-a025-c3a1abff9c3a | -9.90184 | -58.12449 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92db6c4d-c51f-302e-b2e9-2a37cbb82d3d | -9.90123 | -58.12883 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 138785ee-03f5-33df-aad5-931752830c35 | -9.89804 | -58.11957 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65cb0b45-8839-3dfe-8f0d-ed4111404411 | -9.89743 | -58.12391 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d2f619a-30ab-3564-a822-e5a99bb8e902 | -9.89683 | -58.12824 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f757b372-a0ef-3ba8-9801-27d7feb2e8d2 | -9.89364 | -58.11897 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README135.md)
