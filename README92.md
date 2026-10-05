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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92d2f60e-22b6-3e28-98ff-41ec81bd2bbe | -0.38613 | -52.07977 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ed2bccf8-e962-3b7e-85e8-fa8c2d0ee576 | -3.06136 | -54.16983 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fa1943f8-9fb3-38f1-82d2-82f386d19d76 | -7.22854 | -55.18017 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 74640543-12ac-321f-b21c-317e43fe1330 | -2.02226 | -56.43031 | 2026-10-05 16:39:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 524ee7b2-4f8d-31c0-8b86-0f712f81f72c | -5.21905 | -39.56245 | 2026-10-05 16:39:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 1bf0eaf5-e4c8-3fb8-83f7-fc611fa3312b | -6.07808 | -47.65888 | 2026-10-05 16:39:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08d54129-4771-322b-8c8b-bc665a123193 | -0.78507 | -49.26036 | 2026-10-05 16:39:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0402cbbf-2f80-37d9-85cd-7ff0090a81bb | -4.62344 | -38.93915 | 2026-10-05 16:39:00 | NOAA-21 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b33228f9-97db-3310-b514-02390b07b6c7 | -2.90483 | -54.07893 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8f1f098d-5783-3077-924e-3559b84e722c | -1.52539 | -54.83088 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| dedaab6e-cc8a-3905-a5d9-b8a9e6d68994 | -1.59848 | -57.57265 | 2026-10-05 16:39:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 15aa7249-1e58-34f6-a9ae-621a2d2eb43f | -3.80896 | -47.49004 | 2026-10-05 16:39:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4b2f9148-1846-3ebc-b97d-029caee9b0f3 | -2.13164 | -56.68967 | 2026-10-05 16:39:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7c455fd-c531-3a9a-b785-7d0bf016d577 | -5.94167 | -41.35229 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 3ed5cac8-af3c-3ea0-ad17-422e1556db40 | -0.25375 | -48.67248 | 2026-10-05 16:39:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 14c5e1ad-c4fc-343b-985d-48b050bfcb42 | -1.723 | -47.65268 | 2026-10-05 16:39:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e743787-9f12-3327-b20c-1dd80f2a2b10 | -3.05651 | -54.16648 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a1fbd084-cc0f-3b42-8397-c8bf21465682 | -3.16135 | -58.9048 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bdda0451-090b-33b3-b210-a15bbfb88c49 | -4.48993 | -39.36243 | 2026-10-05 16:39:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 421795c9-c1ec-3fa1-834a-ca45eaa4f4b0 | -1.52156 | -54.80579 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 0d53c56e-c99c-35e8-a032-703ceec79e20 | -4.49046 | -39.36559 | 2026-10-05 16:39:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5b7a8929-eb77-346b-8af8-e19162e57c3e | -5.14677 | -37.41364 | 2026-10-05 16:39:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 16.9 |
| cd456448-464e-344c-95ea-8c1a103d3b26 | -1.85514 | -50.62209 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 85a318fe-9d39-368f-a997-f6608419a7dd | -3.37974 | -58.20271 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 2ceb203e-6e9f-3585-9c8d-cdf587f15caf | -6.46568 | -55.45121 | 2026-10-05 16:39:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 303a44a2-9e8c-3041-a9d4-74f0a7f6db40 | -4.85271 | -42.19635 | 2026-10-05 16:39:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| e1c5a78f-7f86-361d-95f1-06232f290444 | -6.1496 | -45.46399 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2be887d7-e5f7-3fe3-9cbd-03ac81360349 | -2.87617 | -54.11892 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 30c0f653-b74e-3c69-acc5-4e89ce4c8224 | -1.00328 | -57.50923 | 2026-10-05 16:39:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9894d378-8820-3547-88cb-378ab267894a | -2.77792 | -57.67025 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 9a9648d9-ce4c-396a-a48d-884da1dcd458 | -3.79567 | -41.76299 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 42ea79b3-b5e8-3ca7-91b3-c9a4e31b31ba | -1.10516 | -46.64317 | 2026-10-05 16:39:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2249e137-edc3-3098-a2b0-bc89fc6d0330 | -2.95538 | -59.15823 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| eb4980e2-fd27-3afc-b171-a5756db8d10e | -3.09654 | -53.71322 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 46e1bfec-e6fa-3a57-a8ff-32489925b660 | -2.9189 | -57.52581 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 60658299-557d-3f64-9461-6832cc8c024e | -4.27185 | -38.55362 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRA | CEARÁ | Brasil | 2301950 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 63e8f31b-2e1d-34c4-b0c7-c41fcd525bc2 | -5.11317 | -42.63576 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8812e9dd-8eff-39a0-9dcc-ceefb81b5c9f | -3.64755 | -58.6221 | 2026-10-05 16:39:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 59e55e8f-cc19-3ec7-8d3f-ff64ae6725b7 | -6.00208 | -43.78718 | 2026-10-05 16:39:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5904c6b5-c319-3b3a-9b36-ba65c8ad29f2 | -4.55337 | -43.71318 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4c67b066-a523-3c4b-b894-7043472b5fcb | -5.85137 | -45.02281 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| cd8db4ca-a686-3f6c-928b-641cd08d9564 | -3.37866 | -58.19518 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 36fc87f3-f2f5-3db4-8b3c-5e34dea001f8 | -4.13898 | -44.99155 | 2026-10-05 16:39:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e7428618-99fd-3c6e-ad40-b93a0fa6a36d | -4.93904 | -38.99023 | 2026-10-05 16:39:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 48f90e19-57e4-33a1-95b4-85382e2d4cb6 | -5.74425 | -45.05569 | 2026-10-05 16:39:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6dabd3b4-91d9-35cc-8f65-d04be6a6417d | -3.2539 | -57.87777 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2dd5f248-0517-31bd-a0f9-bb509a0c882e | -3.53465 | -39.8883 | 2026-10-05 16:39:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| ebf09cc9-45e9-38ad-a174-8dda4b6d8179 | -3.65386 | -39.66972 | 2026-10-05 16:39:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d3a72520-0a25-3708-a6bf-61d18da1cc7a | -1.18095 | -49.24756 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 46f8f4a3-2298-3228-9967-b8ea769b4d7b | -5.73246 | -45.05334 | 2026-10-05 16:39:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b4d2634f-9114-3849-96a4-9a04af0d5ded | -1.17433 | -49.24855 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3d3fb363-9c33-3918-a78f-f6b5290ed18a | -3.16029 | -50.44284 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 307d1fce-ae3a-3797-ab04-c6325be84ba3 | -3.11699 | -40.16166 | 2026-10-05 16:39:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 620ffbd2-f03a-36c2-839a-a72bd33c69cb | -6.04027 | -45.23425 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| afd7e1a1-c9ed-3eda-896e-c5bf419333e6 | -1.26242 | -54.55457 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2a684d62-3c61-3e10-9e35-7c38b53c210f | -1.67404 | -55.06646 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cb5a4f07-583b-3112-9db5-d2cd0f6e5054 | -5.99183 | -53.63359 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| dfd38dbb-219e-3574-ba76-85e3332fa3f8 | -2.99762 | -42.04715 | 2026-10-05 16:39:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2d3d6ff8-fdd7-315e-9132-41503c8626be | -5.71675 | -40.12583 | 2026-10-05 16:39:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 65fa2f9d-f9be-3898-adbb-16a4eb8b5215 | -4.14383 | -46.83392 | 2026-10-05 16:39:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 76caae67-d6dc-3d58-ad37-22140f1dabce | -3.49016 | -54.65854 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 347f4129-e526-3258-805f-4b7e87db0cd0 | -3.95635 | -42.47725 | 2026-10-05 16:39:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 34376e92-1460-3577-9b7c-c22cb8c94609 | -5.11259 | -42.63212 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 904fc772-3eb5-3637-b3e0-0ab0c451d782 | -4.18167 | -44.30548 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 35148791-2307-3384-be49-10fa74c9e42e | -6.20847 | -44.8046 | 2026-10-05 16:39:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 6e082dda-7c5a-302c-925e-e678dbf65b92 | -2.77737 | -54.09342 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 1ce21a2c-1f36-39b4-b13d-9cb131cb2eb6 | -3.5334 | -59.40793 | 2026-10-05 16:39:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e518eecf-4553-3445-adff-9ebd3b648081 | -3.20911 | -42.44134 | 2026-10-05 16:39:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0b7d7621-7710-39f6-ac1a-6574ec70d549 | -4.35907 | -43.83183 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aa1ee151-66c4-313a-86e0-44f97195e70b | -3.37952 | -42.83266 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e104287a-8ba8-3893-bb1b-df9b8e0284b5 | -7.22776 | -55.19963 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 19002b3a-1f42-3014-8d34-a934ec796442 | -1.19193 | -49.25296 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0ef5dd49-2a3e-3838-80c9-422c6c924558 | -3.2144 | -42.77041 | 2026-10-05 16:39:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5527bb9b-8fd7-380c-a6c6-c5a6844e4118 | -3.66663 | -44.80005 | 2026-10-05 16:39:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b417740d-0494-33f3-8fe4-dfd72fb70a48 | -5.3696 | -45.5887 | 2026-10-05 16:39:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 96006db5-76ee-36ca-b505-cd36b65c9299 | -2.537 | -58.02851 | 2026-10-05 16:39:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3ccc2f1e-f6ab-3d67-be6f-0798bef6bca6 | -2.9314 | -53.94115 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 290159e1-4e68-383c-9302-af2e48c1016e | -3.09878 | -53.7281 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 887c10bd-2422-3a35-8b44-0661156cd4e0 | -6.22953 | -43.17884 | 2026-10-05 16:39:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 11.2 |
| e77814ad-cdf2-32d3-904b-4dc3a3359333 | -3.50286 | -54.62131 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 92ce0660-820a-3d2d-b537-2d2608e7e2a5 | -3.37409 | -58.20344 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 1da8b56f-5ab9-3f76-b363-be5983e27144 | -4.51441 | -42.06705 | 2026-10-05 16:39:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 915d2eb0-d816-3010-aa20-06051ac48488 | -3.98408 | -55.81941 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7d4b60c4-09d2-3f0a-89ab-ed94a045de92 | -6.25274 | -43.96978 | 2026-10-05 16:39:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00b1979c-e57e-36de-a5a6-80a9dcf863f6 | -4.34203 | -44.37875 | 2026-10-05 16:39:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e3e436bc-2d33-3699-b5f3-3ff6b6482665 | -5.46948 | -41.23054 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 3a809767-2c81-3355-b9ff-a781e7a2ff2d | -3.51174 | -59.56408 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 6bb8ab6d-e954-3997-8b62-eefe3e7a31f4 | -1.17869 | -49.25495 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6b38cf14-b356-3329-8db8-7dae723b5666 | -3.46252 | -54.59161 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 190e021d-0505-37b2-839d-b5bcbf0e5cf6 | -3.84279 | -59.55386 | 2026-10-05 16:39:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cbea32a5-c10e-3d85-9c25-c43b7844e0e5 | -1.66582 | -47.63269 | 2026-10-05 16:39:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 68bb5025-3f72-3f08-b1ee-737fe31363d3 | -4.30019 | -42.18567 | 2026-10-05 16:39:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 18a46ff1-9df9-3ef2-899f-7fa6d1e72447 | -1.87614 | -50.04404 | 2026-10-05 16:39:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 15eb7610-6333-3abe-aff2-be869e6d5f2a | -3.13387 | -53.71852 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9fad846c-c852-3c16-a104-879fc194e9e8 | -3.62246 | -44.42299 | 2026-10-05 16:39:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 56b5a04e-67d7-3dde-acce-1f02ade01217 | -3.25353 | -59.55679 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 266b27c4-6485-34da-9dc4-c0c45480cd7b | -7.11219 | -55.72258 | 2026-10-05 16:39:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 03a069fb-4769-3589-a480-d9e4c01c5505 | -2.77202 | -57.66759 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 15e08677-0554-353c-b54c-bc3f103daca2 | -6.19496 | -42.61466 | 2026-10-05 16:39:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5b88f3dd-32f1-39fe-af9c-365f0056a97e | -2.87421 | -40.12456 | 2026-10-05 16:39:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README93.md)
