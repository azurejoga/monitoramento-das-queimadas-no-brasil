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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d4d514a-84a5-3c4b-ad7c-f5aec8be73e3 | -8.82915 | -62.36734 | 2025-10-06 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aab87335-1445-37ef-b028-47030291c9e4 | -11.1621 | -47.93702 | 2025-10-06 05:16:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eec899d4-cca0-3056-ad09-96d6bc4745b1 | -10.04588 | -49.21001 | 2025-10-06 05:16:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdfd94cf-10ee-3426-b277-a45030040fbe | -5.62795 | -51.0903 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee2f167c-1b4f-3880-ba7b-41fa5e5ae65c | -9.25166 | -51.81297 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ad19a89-4fd0-3ddc-8eea-c925cfe35725 | -12.41014 | -51.12529 | 2025-10-06 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cf6177f-8301-3fa9-bfb9-84b9cc91cecc | -14.71504 | -48.35768 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6cfa1be6-37cd-3f38-8668-4468bed8a556 | -15.35141 | -47.99625 | 2025-10-06 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b35daebc-495e-3dba-9b9b-04693470d061 | -15.34844 | -47.99635 | 2025-10-06 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b98c1c8a-74a4-324f-a421-9a335ad89b5b | -18.17036 | -53.36922 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4438c720-f8bc-3769-9a94-47c349e5e43f | -16.03668 | -50.95625 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9f3b9f5c-3490-3770-b867-42240928f613 | -14.68555 | -48.3855 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a03460a8-3653-350f-862f-6be8e20cfe0b | -14.69436 | -48.30327 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31404d89-e5d8-3f4d-93bb-749a37755571 | -15.22718 | -49.28061 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8565dbe-cb71-3368-a401-d4c8026604ef | -16.0561 | -50.93446 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 502bf169-a9d7-3950-a0cd-73ce3f587287 | -14.48658 | -47.5527 | 2025-10-06 05:18:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b386fbe1-c504-39e2-bf17-45657f60529b | -14.88291 | -51.52072 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56e3fa3a-6edb-3ec5-884a-f26bf5c98230 | -14.55213 | -46.66112 | 2025-10-06 05:18:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81d0bfca-ca1f-3ae2-9ba2-d5683421c7fa | -16.95852 | -52.68032 | 2025-10-06 05:18:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c477a67f-9309-363d-ba77-c22917c881dd | -13.30433 | -48.07016 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6d57475-61e2-31ad-ae56-b9bff52583f5 | -15.21986 | -49.28594 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| aee46134-034f-3f10-825d-e4ea3733e25d | -16.00567 | -50.84211 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21d8e926-5d90-331c-a10b-fa816d9f724c | -13.35842 | -47.24135 | 2025-10-06 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85caf733-0fa7-3fbf-8691-4cff86b1ca07 | -14.91354 | -46.86921 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb58c569-e76b-3718-8a69-ab472a511bab | -12.30328 | -55.11367 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05b156df-6726-3d6b-9d9e-d8d4a6f6416a | -17.84353 | -57.61554 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 10b884a7-5f2a-3f0b-909b-70a13d1a0ae9 | -13.05322 | -47.90296 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12bdbaa9-9f81-3600-8000-191f6d29210a | -14.54889 | -46.95359 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5a5647db-1f1a-37a9-b109-553557eead66 | -14.55854 | -46.66894 | 2025-10-06 05:18:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2460c1af-b30f-360f-9e5b-a39d4043e7a2 | -15.50024 | -46.8404 | 2025-10-06 05:18:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78637152-0991-3abc-a7e9-fe542de3782d | -13.08844 | -47.82695 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a999605-f007-3b5e-9794-95580aa14d06 | -14.93655 | -47.13279 | 2025-10-06 05:18:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa995c40-5326-32df-bc5a-762fc9da868a | -16.04962 | -50.94172 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 608ffd93-ed95-35c0-8210-c2350d415ef4 | -13.24062 | -48.47091 | 2025-10-06 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc419319-23ea-3344-8b35-c62490b48b9a | -11.48148 | -59.08904 | 2025-10-06 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b89b16fc-961b-3a6b-b896-76e5f9c747b7 | -13.63541 | -48.71927 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7fdb491-9e2f-3d76-acef-d644d8630de1 | -16.01315 | -50.8265 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f126f6c-2c8e-38b4-be83-30e19e23d1d1 | -15.34435 | -47.31068 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2ae8d995-d3e4-3752-9e40-a59e150c980a | -14.67789 | -48.40115 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 805b5fee-d03b-3648-8de9-bb3b40382865 | -16.34368 | -51.45934 | 2025-10-06 05:18:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19e63b92-6b13-373b-95ff-7f3fd04d082d | -16.02669 | -51.04712 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8ece7f7-925a-3bc5-947f-91586fed8353 | -12.29523 | -55.11251 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90fad8c1-a98a-3a94-9458-3f127e26f255 | -13.08701 | -47.83945 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f666d3bb-33d8-3a68-8ad6-9e53d099d52c | -18.1393 | -53.404 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1e79f53f-0106-3699-b749-ca967ca15f70 | -13.27104 | -47.63524 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd9f4537-41f0-3ef4-8eef-85d60610d9f3 | -14.36329 | -47.72226 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d899c74e-06a7-31e1-81b5-ff4cc2abbdde | -18.18899 | -53.38048 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 701d2cbd-6c25-38d8-b406-27002da46dab | -14.54314 | -46.95507 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6ab10622-6d77-3528-8144-daf8038c864d | -17.7039 | -56.77536 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cf8190c8-82a0-382d-aace-b3945c43cdd0 | -14.88463 | -50.12941 | 2025-10-06 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80e751c9-e94e-3e75-9c02-c4336720bde4 | -14.36033 | -47.71682 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4e61d50-e404-37d6-a647-15b706e35981 | -13.28169 | -47.62513 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f4709222-8c6e-30c8-a6fa-2704a98eb524 | -14.70046 | -48.37217 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bb034586-d82a-37a0-a380-97255fcd0338 | -16.03535 | -50.96832 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13a1ee64-2d73-3ad3-99b1-05184d5328f6 | -17.67505 | -52.24286 | 2025-10-06 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e97ced24-61b5-3fb2-a8d6-ad9bbc2605d0 | -12.89664 | -47.3044 | 2025-10-06 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34304502-e1f3-3254-bc9b-e9ca1aad3e53 | -13.32496 | -48.0619 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f257a830-9c0e-35b0-838d-051b301f3999 | -13.33907 | -48.05325 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d1ec475-7360-352e-b1c5-246f31f6e1f8 | -14.66708 | -48.37879 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83ef209d-8800-32f3-b16c-28a379f3f29f | -14.90842 | -46.84866 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a0b14072-9672-38dd-9f61-897d5bacc8a4 | -14.6789 | -48.39127 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2d40b84a-95c5-3275-950d-db0040a650cc | -13.3646 | -47.24784 | 2025-10-06 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e21faabf-bea6-3857-bde8-c5fd5a20a9ad | -14.34674 | -47.71724 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fbebac1c-b4f9-37d1-b64d-f227abfda404 | -18.2708 | -53.31892 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f73e20f-4ef9-33bd-85a5-38d02233c1f1 | -16.00316 | -50.84542 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e273a41-0c47-3973-8357-7f53c73afd7b | -11.82978 | -60.48427 | 2025-10-06 05:18:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 089a9eb3-42e8-3697-a82c-1a3143dd69ae | -13.25948 | -47.81072 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f83c46c-6e8f-3e4c-84f9-86b1781b620d | -14.65562 | -48.35959 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6134a6aa-61b3-3240-bfde-abce1dcb9785 | -16.00144 | -55.99092 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9c161a0c-b73d-3f2f-b33c-43b581a35067 | -13.26271 | -47.84323 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ed06f040-c23d-3862-8e58-194c321ccccd | -13.26478 | -47.83685 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50d44ca7-3ea4-3619-b7ab-31a6e941877e | -12.3073 | -55.11427 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85295cce-8e34-3fec-bb25-907d914893a8 | -14.70637 | -48.37836 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b071bc36-77e1-3149-a024-40c9c4625d50 | -11.8258 | -62.87977 | 2025-10-06 05:18:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6ba1783-41db-3fad-95bb-eddea3e9109e | -18.12584 | -53.39173 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 69ded876-0343-34e3-880d-28b7b1a2b341 | -16.4377 | -52.17096 | 2025-10-06 05:18:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eb6f713-4e88-3a7f-b49d-60642ea113d6 | -15.22998 | -56.77535 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2467e633-542b-32fc-ba82-3d21fcca211d | -14.67151 | -48.39452 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a54e14a-c06f-375b-ac2e-a0522aa1eab4 | -14.63205 | -52.52716 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 16ee35c8-4b27-3e51-8ab5-9e8958342ef3 | -14.9458 | -46.8329 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1274206c-6444-3cbb-94c6-59dc248ae479 | -14.69532 | -48.29526 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7f7fc4c-9406-33de-8459-a80ea2fb1339 | -13.05155 | -47.91769 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 450eb48c-c77e-3f47-aab7-425cdc9ba77e | -14.63536 | -52.5518 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e037315c-d034-3460-adff-bb1587bfe453 | -12.89242 | -47.30137 | 2025-10-06 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21a04620-5d00-32ff-8156-b62c58788424 | -14.63835 | -48.33706 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99fdeefa-b100-37ef-a34d-57e31053c61a | -15.57345 | -52.4431 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7c89f507-8e91-3d70-b4ff-ba3f52d8db38 | -12.89939 | -54.75511 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b6f0d5f8-7804-39e2-b5c8-037eed9422da | -18.19516 | -53.36982 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85058b2b-0dae-3ea5-9505-fa6b48ee2fcb | -13.26275 | -47.85494 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d9ff6fc5-9b43-3f67-8aee-b01c4a61ff90 | -14.54244 | -46.96181 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6392ae51-a807-3bda-94f3-d88c981fb815 | -13.60788 | -48.70301 | 2025-10-06 05:18:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10726a2a-f133-3ca3-93c0-c22914e6f5ac | -18.17473 | -53.37463 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6d8fbb20-14b9-3b6b-baf9-acfc04267706 | -14.67296 | -48.38534 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3dc2816-594d-35ba-ac7a-4f7b5547330f | -14.35987 | -47.72132 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0cd54cc-9b2f-3917-aa2f-fa57538a2044 | -12.89575 | -54.75071 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a198821-5c63-3a84-bbc1-9246a6321b97 | -16.14523 | -57.57832 | 2025-10-06 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 24a8898a-ee33-30cc-81ac-6ff417c10bcc | -13.34563 | -48.05339 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c49e231c-6be4-3e2f-b411-a1669cd3b8a1 | -18.15466 | -53.31488 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d15b1c52-61c8-346b-b0a8-1da7d2729743 | -15.98992 | -55.9856 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c365ce50-1b18-37a8-b4ce-20fe6e49edcc | -16.02707 | -51.04365 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README68.md)
