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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fa4b3f3-0982-3f9f-b26f-ccb8d8059bf4 | -14.68681 | -45.13963 | 2024-10-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfe4ef6a-bf40-326e-98eb-8927396d82ab | -14.6864 | -45.14322 | 2024-10-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2a881c9-b820-3c33-aeae-3c7336e4f2e6 | -14.48853 | -44.96341 | 2024-10-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e5cb976-7617-3500-b1f5-1be6d4f5edde | -14.48315 | -44.96258 | 2024-10-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2150ef06-df1c-32eb-92f1-71140a93aafd | -13.8584 | -44.59378 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c46b803-ef7c-3e4c-bfb2-ac089b8ff597 | -13.85735 | -44.59398 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0cafcbfa-65c8-3202-80af-8816be4a4fd5 | -13.85294 | -44.5929 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03776f57-b0a0-325f-a853-9cdd0567c4f9 | -13.85253 | -44.59653 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c72bbdd-f2ba-36f9-ba95-bb5bd8e3dd8e | -13.85145 | -44.59673 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca509a7c-d2f1-312e-88f8-77985e23cf52 | -13.84707 | -44.59559 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1000d0cb-c8b8-367c-ba80-8542b9c89af2 | -13.84303 | -44.63138 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 146e11c6-23fa-3165-86a1-2fd1bca53e8a | -13.84262 | -44.63499 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 33e2e631-b0a9-3eb4-a111-d9f46c6f175e | -13.84127 | -44.63515 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f0c17af5-5103-39d7-947e-7bc147c264d0 | -13.83716 | -44.6342 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88b30596-c1a9-3c9a-9f49-a60d9a2d801e | -13.83581 | -44.63439 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 43368376-fd3c-3a0d-b16a-22755c0f8618 | -13.83451 | -44.64526 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbee3237-b737-3ce9-9911-5e0b044c169c | -13.82949 | -44.64083 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5565ba15-009d-3c88-84c6-6447383cecab | -13.82905 | -44.64449 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fde839f-e053-3392-b8c5-c786ba487056 | -13.82699 | -44.61535 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d91f8a61-1bcc-35a9-b068-0a359a60a3c9 | -13.82657 | -44.61886 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b0fdadd-dabd-3f08-9761-de19ef3076ae | -13.82404 | -44.64008 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5408506f-3278-3825-899c-d075155ca24e | -13.81943 | -44.63222 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c592e6f6-1c75-3ef9-9026-60ca98fe5fd1 | -13.81901 | -44.63571 | 2024-10-07 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64e73819-1a61-3036-8a81-362f8b626d3e | -14.07161 | -45.46309 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bb940123-eb4b-30c5-84cb-7d6a662332ff | -13.09309 | -46.34315 | 2024-10-07 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9050b462-3d84-331f-97c9-df3c42b1d56f | -13.09247 | -46.34793 | 2024-10-07 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a495816-871a-3c32-9fdf-7ad1ce17e365 | -13.09235 | -46.34349 | 2024-10-07 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 890a68c7-5bfc-3551-9a97-322095bb9f75 | -13.09175 | -46.34837 | 2024-10-07 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5dd9d20f-c715-36e5-930d-3e822d097444 | -13.23542 | -45.58014 | 2024-10-07 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c4ca3be-030b-3b71-85ea-5978529e5247 | -13.23505 | -45.58319 | 2024-10-07 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97dc05f6-b6ff-388d-bbc9-145f5b32a86d | -14.21427 | -46.45499 | 2024-10-07 04:53:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55f8ad70-6c20-303e-b6ca-f1061416a046 | -14.21364 | -46.46008 | 2024-10-07 04:53:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94932648-21d9-3b3a-97ec-0cb3fa864140 | -14.21011 | -46.44861 | 2024-10-07 04:53:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 716dbfed-4362-3b9a-9e26-bbdb0fcf499e | -14.20944 | -46.45412 | 2024-10-07 04:53:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4cbcae0e-761b-333b-872a-4df172a9160b | -9.35656 | -63.80756 | 2024-10-07 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 292b77c6-5f5b-3e85-bb80-9aa037e6208d | -11.66262 | -65.20975 | 2024-10-07 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07f66c9b-3f6a-3f98-b6c9-bdd58893959a | -11.52909 | -65.14096 | 2024-10-07 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8eaf3f72-b311-3c4a-8b97-b3108896e547 | -11.52835 | -65.04999 | 2024-10-07 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2431a502-8398-31f6-9954-241c0525257a | -11.5231 | -65.13957 | 2024-10-07 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98b750a5-e2a6-34fe-b63f-64ee8ff38b65 | -11.52217 | -65.14427 | 2024-10-07 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4583695e-ced9-31b3-a14f-4ec359b34faf | -14.20879 | -46.45936 | 2024-10-07 04:53:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4871d4bb-9f98-3178-8e2f-57b8ba43af6a | -14.20814 | -46.46464 | 2024-10-07 04:53:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7555410f-a048-3dc7-9bfd-3945241c36be | -14.20527 | -46.44782 | 2024-10-07 04:53:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eebef4aa-8979-3673-9025-360e185482b0 | -14.08241 | -45.47205 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15c97ab7-6584-3d9f-a966-b493f5f10dc7 | -14.07836 | -45.46159 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| da6c7d93-2014-3e4e-8273-e3e365c3f07c | -14.07797 | -45.46494 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 48002fbb-16d1-3e42-90a5-256f86853467 | -14.07758 | -45.46828 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ccfb1c9b-aff3-352a-9e94-62f2a997afaf | -14.07314 | -45.46116 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98144762-10f3-34a6-9e14-ea6af7f14749 | -14.07276 | -45.46448 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1f9fe7d4-a9ee-3a69-b4fb-0ed7f1db5d42 | -14.07202 | -45.45974 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 200ba21c-b2e2-398b-a87d-c043a1566bb2 | -14.06795 | -45.46051 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 643731ef-d1f1-369d-afc2-a1dc78afb127 | -14.06542 | -45.52755 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3cd97c4f-fb8b-3de8-81dc-9bdc0f1d7418 | -14.06505 | -45.53071 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5c3bb0d-e080-3017-bc42-232f10b864a4 | -14.06383 | -45.52597 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 678ad8d9-78cb-3ff1-9d96-802ee0dc01c2 | -14.06344 | -45.52914 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72adbf96-ae47-359b-b8c3-104d98ff2942 | -14.05989 | -45.53003 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 874478ae-5e4b-321b-aed9-4e3873fb5532 | -14.05827 | -45.52851 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f088a7e6-9489-3715-8f42-dc99b852326a | -14.05787 | -45.53172 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2158d32-8ddb-3814-8c11-171c5c04898e | -14.12775 | -45.53296 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9398b8c3-f737-3cac-af25-bcda5ca62ffd | -14.12735 | -45.53622 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5a00f096-1fc9-360e-a25e-60ac545ad11b | -14.12257 | -45.53239 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 696bd2b8-883d-39f9-aed6-8d9361ba4f94 | -14.12217 | -45.53569 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fa3c4e43-20f0-3bf8-8469-5b0fc5ed5e87 | -14.12178 | -45.53899 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8723700c-f5a4-3210-b059-0a3dcf45f4ba | -14.12119 | -45.58733 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4577c713-3130-398e-b41f-7e82bcbd86b9 | -14.12081 | -45.59041 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 929b4ccc-4d81-3c04-889b-43449084cd5a | -14.11778 | -45.52857 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| eba123c7-f724-3ac5-ba1f-d211e16641bd | -14.11738 | -45.53185 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c8769879-9143-3a5f-99e6-fb9847463346 | -14.11699 | -45.53514 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ffac3a2-bfde-3d27-9dfd-4cc2c6e9ca20 | -14.11606 | -45.58646 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed1a6c26-8891-310b-b6a3-98f4ce5c1ca2 | -14.11569 | -45.58956 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef746639-cb69-319c-9b0a-af8469a0be6c | -14.11415 | -45.51496 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 138022f4-1b5e-3fe5-869c-577cbb2ca6a3 | -14.11375 | -45.51833 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7f9f718f-3f93-3c89-aee0-93b80a3cca0b | -14.11336 | -45.52165 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| f3046d51-535b-3f1a-9de5-a22b16e8c099 | -14.11297 | -45.52488 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 9e757e84-4a04-3c25-8533-7652be97c0c8 | -14.11259 | -45.52809 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f99e1e66-0d57-368b-a470-06a3ce35c085 | -14.10974 | -45.50792 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9550cc3-3021-3eed-83fd-1318e49f0cc7 | -14.10935 | -45.51122 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa369e94-9509-37a6-b4fb-c5b2c2c0b9aa | -14.10895 | -45.51454 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc6db315-c3e6-3ed4-b192-90bfe0334a4d | -14.10855 | -45.51788 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a57f9090-574d-3b53-b71e-f66aef2cabc2 | -14.10816 | -45.52116 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c5ac309-abac-3e46-85b2-d8c6d485b9ad | -14.10779 | -45.52435 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4be4653e-834d-3e5c-902a-11b6fd704a06 | -14.1061 | -45.4943 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df9bb3a5-01c8-3ae7-a64e-78fee52b73b7 | -14.10128 | -45.49055 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 97bd7e6b-ccfe-388d-bd57-f1a3da4f5121 | -14.10089 | -45.49387 | 2024-10-07 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 54c10cd6-82a1-31ad-a8a4-1920e6b69a06 | -16.91451 | -46.94702 | 2024-10-07 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca280cf1-51e1-3943-8a6f-77ec4cacdbf3 | -16.9107 | -47.14953 | 2024-10-07 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7700653f-144b-3b13-87cb-1497f32d512d | -16.9059 | -47.14875 | 2024-10-07 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25e2cc32-7f95-30a9-82f8-de0165482e5f | -16.90527 | -47.15412 | 2024-10-07 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 375ffa52-f9ea-398f-a2d1-f5b349ac6b82 | -16.89019 | -47.15776 | 2024-10-07 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ec591851-977f-3d7c-b02e-ea237de4678c | -16.88763 | -47.17985 | 2024-10-07 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7f0b3b95-fff2-397c-b6d5-2d0983e53f8f | -16.88537 | -47.15725 | 2024-10-07 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1f6a830-99bc-300d-be2e-2b72912abe67 | -16.88408 | -47.16839 | 2024-10-07 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 126d2d60-d230-3b12-9209-92a5cdb3130d | -16.87927 | -47.16785 | 2024-10-07 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3787a3b-eb64-3da0-9b9b-a05d8a2bea70 | -15.1713 | -47.07867 | 2024-10-07 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9987bc13-d9c3-3ca8-90bc-feefee31bf83 | -15.17072 | -47.08345 | 2024-10-07 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1d46381a-e31d-3fd1-9763-5ada7cb4e0f5 | -15.16599 | -47.08292 | 2024-10-07 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2370e02a-940d-37eb-b312-81cff4086a62 | -14.28651 | -47.40995 | 2024-10-07 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 183128e8-edb2-356f-ace5-b04ec09d47d2 | -14.04205 | -47.27355 | 2024-10-07 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c1fa02e-d4c2-3901-9532-20d65f4e6b7c | -14.03671 | -47.2788 | 2024-10-07 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79b0171b-6837-34fa-93ec-efdebead42fd | -14.03615 | -47.28312 | 2024-10-07 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README84.md)
