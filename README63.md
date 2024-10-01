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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40bb5c22-1c00-3a11-890a-04cc535800a6 | -2.89356 | -50.70724 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f4d79409-c4ba-381f-8b0d-a487a4545d0d | -2.89305 | -50.71027 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7b0fdfe-2485-3a56-9b26-b6c2400bf755 | -2.89254 | -50.71328 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4f4965f-1f3c-3c3d-aabe-9625ccf44b2d | -2.89204 | -50.71631 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 6ba089de-c514-3abd-9b9f-11984de8931b | -2.89051 | -50.72539 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| e7834e74-3a95-3935-adbe-f3d344618d13 | -2.89001 | -50.72842 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 784e3c52-86a1-34f3-b2f9-d09ab103e010 | -2.8895 | -50.73143 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 7ae2c6b7-d30b-37f5-9457-7fd04146d972 | -2.88899 | -50.73445 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| f85aaf3e-ba61-368d-b8a2-34a6fc1645a7 | -2.88743 | -50.71242 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f1bb1890-1eb4-3435-a896-bcd297c2b176 | -2.88567 | -50.70598 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78874594-d560-3d42-931c-bc921651e245 | -2.8854 | -50.72455 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 56aabe7a-9a81-369d-aee6-b200d8316fec | -2.88518 | -50.70899 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9845642b-1bee-3c99-8909-cda86389a97c | -2.88489 | -50.72757 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 60395b95-3f6c-3c0c-88c6-bcbcbb6df5ca | -2.8847 | -50.71201 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a484f028-54ab-3c39-a8f6-79208a016095 | -2.88438 | -50.73059 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 149dd790-6a2b-3b80-92ed-63168c9ea0c8 | -2.88421 | -50.71505 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f8ef5903-7965-3a5f-ba9a-945342edccb8 | -2.88387 | -50.73361 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41318c1e-fe71-3c2c-8ef9-86ac714f9c5d | -2.88372 | -50.71809 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b2addc6e-c2ca-3630-a6df-83145fc5394a | -2.88283 | -50.70856 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7bb39cbf-fa0e-3a2f-9afc-9caf6f43999d | -2.88275 | -50.72417 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 53fca597-dbed-311f-a7f2-89a96811ef01 | -2.88226 | -50.72721 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1c7428b0-e6ca-3e5b-965e-a0434456150e | -2.88178 | -50.73024 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9aea837b-cd45-3cb6-bc28-32cf1a20bbcd | -2.88129 | -50.73327 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8734ee24-d37a-3459-9ea8-3d62ccb10b05 | -2.88028 | -50.7237 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 57e0fc4d-9512-34a9-8af0-f0868135fe42 | -2.87977 | -50.72673 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a82a4964-974e-3522-848e-dee05e7b1d70 | -2.87926 | -50.72977 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 57b036fc-af5e-372d-8a26-da966cd7c81d | -2.87875 | -50.73278 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4027f079-1451-3773-92ef-840c819f9612 | -2.87861 | -50.71721 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 81a169ed-f8a7-31db-961c-5dd04a3ae628 | -2.87812 | -50.72026 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 300045c0-d46d-3e35-ac6c-e264dd25e076 | -2.87763 | -50.7233 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4be122df-4c82-3234-ba51-f1b64e98b70c | -2.87721 | -50.71072 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afd9384c-f8ae-344f-93e2-03021fb57e74 | -2.87714 | -50.72635 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 46a359b6-1968-3956-877d-5f2bde9384d7 | -2.87665 | -50.72939 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3f82f375-42ee-3f2b-9731-bf6a9bd4a9a0 | -2.87619 | -50.71677 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b300efca-5ac3-3453-903b-703ae902b4eb | -2.87617 | -50.73241 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db377c36-a532-32bc-b093-170d81826049 | -2.87568 | -50.73542 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| feee3dfc-5192-3b68-8afd-6a7ea63dca5d | -2.87517 | -50.72284 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65fa795e-9e14-3623-9b7a-20a029240d41 | -3.29204 | -51.06056 | 2024-10-01 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c2a6dcf-5df4-3a75-a48f-a2e78711437c | -3.29151 | -51.0637 | 2024-10-01 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7c60a3a-66fd-3c9a-8918-e055441a911a | -3.0719 | -51.21881 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c353d631-70b7-3171-9552-a4ac23f3af8e | -3.06663 | -51.2179 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f795ccd-2ba5-3dba-87fa-c0c3c005dbb8 | -3.04168 | -51.33551 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 112780c8-1dc6-34c1-8dfa-ccf85ace7a41 | -3.0364 | -51.33438 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 987e8952-2a44-32f7-82f3-20bb1559d328 | -3.03164 | -51.33014 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6aac2f0f-18a9-36c2-a28c-94161382c215 | -3.03108 | -51.33348 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 35d266c9-bd59-38b2-9f4c-ab7794c1f188 | -3.03052 | -51.33682 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cdfd9fac-e57d-3c1a-8af3-405b949e93c2 | -3.02519 | -51.33598 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5edaa6e2-fda7-3313-bee8-d8252fecb49d | -3.02462 | -51.33944 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 666451bb-29d9-34f0-95b2-01807ae0c5eb | -3.02403 | -51.34292 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 929c256a-5923-3ea1-92e6-fd23f9ef2abf | -3.01871 | -51.34203 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b88f89f-3ff4-34b2-98a1-368522629635 | -3.01814 | -51.34546 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af7d3e8e-4c1f-3527-9b87-98ef3394090d | -3.01758 | -51.34878 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff560183-8242-33a5-afeb-55cd882aa63b | -2.91062 | -50.79448 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba14949d-f78b-373e-a0b8-74b8cc714d30 | -2.90954 | -50.76913 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4eaf63ae-d695-36e3-8083-dad8f2a6178d | -2.90599 | -50.79055 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c97f998-c5ae-355e-b4fc-0e60ee7d5b0b | -2.90548 | -50.79364 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9c50251-5a77-32b4-aa2d-56077f187f95 | -2.90441 | -50.7683 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f08cd38-17f9-3f56-b99b-4f234fc19729 | -2.90288 | -50.77749 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71cb5f8f-1a58-3781-908c-2edde5f4f06b | -2.90085 | -50.78973 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce1113cf-55d6-3471-b6d7-995b06c1cc7c | -2.90034 | -50.7928 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6fec406-ee5e-32f8-bb3a-a9ebf3745720 | -2.89983 | -50.79585 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90d81c06-04d8-3469-bc90-05c98b302635 | -2.89882 | -50.80194 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dbe124d-8706-3bb8-be4e-f43893dea558 | -2.89831 | -50.80498 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39f1688a-d133-37b6-9daa-fd3427a48278 | -2.89673 | -50.78274 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93152945-d3fd-3ae5-9cf1-b84ffbe97a62 | -2.89571 | -50.78889 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 108ed68f-9cf5-36b4-9e4e-0a3b8cc711a2 | -2.8952 | -50.79196 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d2266f1-758d-39eb-96eb-69eab5235b3f | -2.89469 | -50.79502 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 119cd404-378a-3065-9439-452bc887d68d | -2.89367 | -50.8011 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 06ee9be2-86bc-396f-8121-47556b6d6581 | -2.89266 | -50.80717 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 59330c41-16b9-3290-86ca-7d316db1a9ee | -2.89263 | -50.77571 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6c48d94-bfd7-394f-89e9-474925a3de9a | -2.89165 | -50.81325 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 203ada84-290c-3683-8fc7-139e3188db51 | -2.89109 | -50.78491 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af09d988-1618-3e38-b175-73ed13e50a3b | -2.89006 | -50.79107 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2744411f-3432-3aed-8041-080e763c96cc | -2.88955 | -50.79416 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5a78741-5922-34d7-854c-d7deeb3b96a4 | -2.88853 | -50.80024 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3766f02c-402c-32c1-bc29-61df6122e038 | -2.88803 | -50.80326 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 444c7dd8-7c02-351d-bbfb-0c4d91925158 | -2.88752 | -50.80631 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 1babf621-00d1-319b-8f14-a3b144c715bb | -2.88701 | -50.80936 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2baa1551-1243-3f58-a3a5-83c061f04876 | -2.8865 | -50.81242 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d3af5836-ad6c-3566-806d-2d902383d8e8 | -2.88647 | -50.78096 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ac235c1-4b52-3e5b-8b8c-cbde110be169 | -2.88493 | -50.79017 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d54cd786-a93e-3496-97be-b0edd5593475 | -2.88289 | -50.80239 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b50d1259-713a-3a38-bcf0-8ca0c3dea569 | -2.88238 | -50.80542 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b832c2a8-df75-3f98-8d86-b102f472e883 | -2.88187 | -50.80848 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87382b3b-c633-3969-abe0-186762f493b3 | -2.88135 | -50.81157 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11c55ab0-b15f-307c-bd97-1fa4521f3c4f | -2.88084 | -50.81462 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4530e6bf-3052-380e-be11-691d70d1d8c6 | -2.87921 | -51.66532 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1210a821-b158-329e-9c66-562756a878ea | -2.87876 | -50.79546 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2265e99a-c09b-351c-8dbd-76c64475ae58 | -2.87775 | -50.8015 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67052828-c3ee-37b8-91aa-48a5a0b104b8 | -2.87672 | -50.80762 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8858be17-b3b4-3c71-a50a-f2cbb9c0442a | -2.8762 | -50.81072 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| edea8d46-bed3-3a15-9cf5-dfda6cb8ecff | -2.88849 | -50.73747 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 5135ca4c-725f-3157-a498-e1b734dba9c7 | -2.88798 | -50.7405 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 96c8a2b2-1a3d-3584-a096-d2c8aa90be88 | -2.88747 | -50.74353 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5bd86734-6f92-3840-a063-9a2838962e77 | -2.88696 | -50.74657 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da06e173-64ee-34d2-a97b-4378aa4a30fa | -2.88645 | -50.74961 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc227030-eda5-38d1-ac36-ed105cd6a5ea | -2.88594 | -50.75265 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21b17444-94c9-3745-83e5-f95eeebee75b | -2.88543 | -50.7557 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc38410f-cbad-3c95-8563-bb382959a429 | -2.88337 | -50.73663 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afe6d4e3-6f5b-3f76-ba87-ab605aa831f7 | -2.88286 | -50.73965 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README64.md)
