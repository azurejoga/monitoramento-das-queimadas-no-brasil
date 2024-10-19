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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48dee762-5d6d-3be8-9407-453f94731089 | -9.0344 | -67.4641 | 2024-10-19 06:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| e89a09c0-6fd1-32e3-8cf8-364341c068c3 | -9.0345 | -67.4455 | 2024-10-19 06:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6b1ef01c-c4ed-3f29-8a81-b7e8f9da13e5 | -9.053 | -67.4636 | 2024-10-19 06:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 1fbdc894-74fa-349b-ac35-70ca073be2b0 | -9.053 | -67.4451 | 2024-10-19 06:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 0e73b1ec-6c0a-33b3-8be7-7447217b1a94 | -12.023 | -63.4998 | 2024-10-19 06:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 21f53f01-6045-3707-b625-408479754f4d | -12.0228 | -63.5189 | 2024-10-19 06:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 814f54d0-8e3f-339c-a002-8546e7ef4806 | -12.004 | -63.5199 | 2024-10-19 06:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| da4dc266-f66c-3a86-b9a4-38d53448ef8a | -12.0041 | -63.5008 | 2024-10-19 06:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 714f3132-7aad-3784-99a6-c2fb5dd64e44 | -7.65361 | -73.24963 | 2024-10-19 06:57:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e187570-a032-392c-94bf-4dfe3caa0579 | -7.65422 | -73.24486 | 2024-10-19 06:57:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fd6b258-e634-3cd6-9a6f-898e65d8e5c1 | -7.35368 | -72.88059 | 2024-10-19 06:57:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34161ca1-d224-3510-96f4-50ae1c4a8d5e | -7.35435 | -72.8756 | 2024-10-19 06:57:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0599cca2-0c5a-3c6d-ac2b-cf91ee0af0ee | -7.62777 | -73.11578 | 2024-10-19 06:57:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a582eaa-35fe-3bb2-b03d-6a19c7aa11be | -7.63401 | -73.11649 | 2024-10-19 06:57:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb6a615b-f405-31f7-abd2-583aa80b2429 | -7.63464 | -73.11167 | 2024-10-19 06:57:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22557cd2-639f-3bd4-9d5a-91214f7aa8cb | -7.69845 | -73.04802 | 2024-10-19 06:57:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c5ae410-a2b1-33fa-b5b8-1dc862356987 | -7.70001 | -73.05012 | 2024-10-19 06:57:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0e4e7f93-5b99-3e6c-afd6-75fb46f8a10a | -7.70069 | -73.04516 | 2024-10-19 06:57:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aae32a60-5251-34d7-b8ca-c89d463ae20d | -7.78129 | -73.09441 | 2024-10-19 06:57:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 486cf535-10fc-318e-a270-d8daa663e677 | -7.70471 | -73.04881 | 2024-10-19 06:57:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa624f6f-26ee-32c0-9f45-1a4eaff67234 | -7.78063 | -73.09931 | 2024-10-19 06:57:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 755e7858-d4d3-30d3-a026-6263620859d9 | -7.3271 | -72.7538 | 2024-10-19 07:05:48 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 24920182-9ce7-39eb-bf1d-8edaa57a35cf | -12.004 | -63.5199 | 2024-10-19 07:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| bf0bb7dc-733f-310b-8268-a81a5acba9be | -12.0041 | -63.5008 | 2024-10-19 07:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 8b7bab89-5d83-3245-bc80-2c92c535a83a | -12.0228 | -63.5189 | 2024-10-19 07:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 1bf690ab-5d1b-3695-bcef-7962bb4c296b | -12.023 | -63.4998 | 2024-10-19 07:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6fe93dda-235f-33fb-aa50-a34ad2b8b000 | -12.0041 | -63.5008 | 2024-10-19 07:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b2d87706-e94e-3dc7-99db-04369b31aee7 | -12.0228 | -63.5189 | 2024-10-19 07:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| da9a79e9-5d09-3234-9ed5-039d8b58fe76 | -12.004 | -63.5199 | 2024-10-19 07:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.8 |
| dbeace66-63fc-375a-8382-8e4be509c0eb | -12.023 | -63.4998 | 2024-10-19 07:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e70c6f6c-3467-3a5a-a35d-afecb8dfd30d | -7.3271 | -72.7538 | 2024-10-19 07:25:48 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| f455e44a-7fff-348c-92af-5cc48ff58c6c | -12.004 | -63.5199 | 2024-10-19 07:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 7497a01c-d542-373e-a971-2c3180c35df3 | -12.0041 | -63.5008 | 2024-10-19 07:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 14446866-d4bd-3905-af80-ec8dd8af65f2 | -12.0228 | -63.5189 | 2024-10-19 07:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| cbd4b8f0-65c8-3932-82c1-ff429c9849eb | -12.023 | -63.4998 | 2024-10-19 07:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a1d8ab05-132a-3bd5-b2b7-bbd557c7595f | -7.3271 | -72.7538 | 2024-10-19 07:35:48 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 078b8ce6-cf26-30ed-b452-2a2113dd6948 | -9.0344 | -67.4641 | 2024-10-19 07:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 62a847f2-032e-3d4a-8e06-439f44d7ae99 | -9.0345 | -67.4455 | 2024-10-19 07:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 63f16d05-0093-3fc1-8bea-542b89461ab5 | -9.053 | -67.4451 | 2024-10-19 07:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ab3808bf-7802-3170-8632-8112f8134af1 | -12.004 | -63.5199 | 2024-10-19 07:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 561ac17a-5ae1-38a5-a34f-e67d50637a3e | -12.023 | -63.4998 | 2024-10-19 07:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a96c5987-7269-326d-9b8a-492846051b34 | -12.0041 | -63.5008 | 2024-10-19 07:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a9bb5c98-226d-3c8d-b602-77804adfef84 | -12.0228 | -63.5189 | 2024-10-19 07:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| b122aef6-de33-304b-939c-922b5702326f | -7.3271 | -72.7538 | 2024-10-19 07:45:48 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 9cb1879e-fe1e-3975-939b-5850fdb1750b | -12.004 | -63.5199 | 2024-10-19 07:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ef0f0815-36a3-3aa9-b4b8-f7ecb2c1f501 | -12.0041 | -63.5008 | 2024-10-19 07:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 6b89fe3e-8e6f-3119-b6d1-60b9be44e172 | -12.0228 | -63.5189 | 2024-10-19 07:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| b94f5057-67b7-37a3-8abd-9a382d83479a | -12.023 | -63.4998 | 2024-10-19 07:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 7741f7a0-9b2f-3557-a6eb-688bc77a2478 | -12.0041 | -63.5008 | 2024-10-19 07:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 5f99276d-be73-38c1-b7be-164c1061a395 | -12.023 | -63.4998 | 2024-10-19 07:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| aaae3fbf-7717-3604-81b6-caeb24c6f664 | -12.004 | -63.5199 | 2024-10-19 07:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| b0914822-fe15-3d94-bf80-c6a4d705fb80 | -12.0228 | -63.5189 | 2024-10-19 07:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 82758cc5-3c3b-3a0b-9ce7-eb2fb2aa8fef | -12.5147 | -63.3014 | 2024-10-19 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 0517c024-be67-36c8-b94d-829ba054ad18 | -12.5147 | -63.3014 | 2024-10-19 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| baf15647-d12b-30c3-bac5-b87a5cd665af | -9.0345 | -67.4455 | 2024-10-19 08:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 9fcd79d9-7d07-3cc9-839f-a31ad2177bd6 | -12.5147 | -63.3014 | 2024-10-19 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 4a950d4c-7ba5-357f-bc5f-f09d2ff42741 | -12.5336 | -63.3003 | 2024-10-19 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 125b816c-94db-317d-9406-cae6c1859bbe | -12.5338 | -63.2812 | 2024-10-19 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a75d117a-67ee-3b93-98f4-4e86ff1e1127 | -7.3271 | -72.7538 | 2024-10-19 08:35:48 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| d4b8b5be-ad47-3035-a291-b7a5bdecb894 | -9.0345 | -67.4455 | 2024-10-19 08:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f79c9689-d48a-3458-aae1-7bee3926b695 | -12.5338 | -63.2812 | 2024-10-19 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 0634157c-6023-3f73-a144-daf42eb16d0f | -12.5336 | -63.3003 | 2024-10-19 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 4dd4a73d-0601-30e5-8fd9-c1604445424e | -12.5149 | -63.2822 | 2024-10-19 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 80ae27e4-fd96-35e8-b10b-68c175ee56bf | -12.5147 | -63.3014 | 2024-10-19 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1c9ac1c9-1d19-364f-81cf-184d90cc5742 | -12.5147 | -63.3014 | 2024-10-19 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 1cc76de0-1f38-3ea4-84b9-982779b708c3 | -9.0345 | -67.4455 | 2024-10-19 08:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| debea213-8d5c-36af-b09e-d50a3a9b7fd8 | -12.5147 | -63.3014 | 2024-10-19 08:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 31f909a0-4974-3c8c-a464-8148dab45ce0 | -9.0345 | -67.4455 | 2024-10-19 09:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| b26b5046-ceca-3c73-bf12-ea6dbbc9e0e0 | -12.5147 | -63.3014 | 2024-10-19 09:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 33b16ad3-626d-3634-afcf-b974c9b10003 | -12.004 | -63.5199 | 2024-10-19 10:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 93ca0a70-57ef-3367-8bd7-bec8487cf73f | -12.5147 | -63.3014 | 2024-10-19 11:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 109.2 |
| ee618345-8468-3c89-b66e-8c70ae7a76f1 | -6.58095 | -38.18346 | 2024-10-19 12:06:00 | TERRA_M-T | LASTRO | PARAÍBA | Brasil | 2508406 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 81c18534-3931-35c9-b4fc-f3d07b717d8e | -7.98696 | -37.63299 | 2024-10-19 12:06:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| b0def6ae-f2a4-3ad5-b62a-726a233c5b37 | -3.33022 | -42.52257 | 2024-10-19 12:06:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4715a2d2-e878-3890-a43a-11ca33057775 | -3.52211 | -43.23257 | 2024-10-19 12:06:00 | TERRA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 30c33350-9295-38f3-a902-5c44a4507884 | -3.65098 | -42.38383 | 2024-10-19 12:06:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 9553d74e-d32e-3dda-9f79-a7b4051f99f5 | -5.26729 | -42.95665 | 2024-10-19 12:06:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 28491319-9d5b-3871-bb70-268c433aeac8 | -5.47507 | -38.24163 | 2024-10-19 12:06:00 | TERRA_M-T | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 2b21bf8d-389b-3718-b885-8f575e99deab | -6.17554 | -45.42581 | 2024-10-19 12:06:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 6824cfc2-6434-3722-86f7-c03f12fb9f2f | -6.18038 | -45.43335 | 2024-10-19 12:06:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| ee2f372b-2a0e-312e-bbe8-f191e3666246 | -6.29837 | -43.43539 | 2024-10-19 12:06:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f49847dd-5852-3b68-a8f3-0eabde970a15 | -5.73072 | -43.81251 | 2024-10-19 12:06:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7429fab5-9883-3caf-80bc-7a887958bf3c | -9.49357 | -37.14073 | 2024-10-19 12:08:00 | TERRA_M-T | OLIVENÇA | ALAGOAS | Brasil | 2706000 | 27 | 33 | nan | nan | nan | Caatinga | 13.0 |
| bf9f6340-6681-3cfe-b573-bcd660ab10eb | -9.20619 | -36.83123 | 2024-10-19 12:08:00 | TERRA_M-T | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 6bb5fd51-a9ca-3b07-b4c2-87a0b916c0ca | -9.19693 | -36.83005 | 2024-10-19 12:08:00 | TERRA_M-T | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 2919439e-d31d-3429-a026-f06685596eac | -8.73101 | -36.73607 | 2024-10-19 12:08:00 | TERRA_M-T | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 24c60b01-13e5-3b24-9c82-3b2e78f7dfe9 | -8.17446 | -38.57648 | 2024-10-19 12:08:00 | TERRA_M-T | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 0082ddee-2c1e-3e7c-afcd-f6f1ed9bd26f | -8.17316 | -38.58538 | 2024-10-19 12:08:00 | TERRA_M-T | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 18.6 |
| dc6dabbe-0d81-39d4-bc44-1954c09e8ba6 | -10.79211 | -39.33573 | 2024-10-19 12:08:00 | TERRA_M-T | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 9092ffd2-6b93-38ba-a7ac-072bcd4b8c38 | -10.7908 | -39.34472 | 2024-10-19 12:08:00 | TERRA_M-T | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 98.1 |
| bc0ba719-d96b-32ef-94d4-01e9cab23448 | -10.78192 | -39.34342 | 2024-10-19 12:08:00 | TERRA_M-T | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 59.1 |
| 69f5ad86-8ef4-3a94-a5be-67a8d6999f7c | -10.55151 | -42.38452 | 2024-10-19 12:08:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| e065c72d-6123-3c46-a3e3-72cd71c6e6e8 | -8.01388 | -37.5723 | 2024-10-19 12:08:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a93ee07b-218f-3ff9-bb10-e9d79a079862 | -8.06977 | -38.60057 | 2024-10-19 12:08:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 1b33bdf4-aaba-3b22-a193-ad77f49ea77b | -8.11606 | -39.97962 | 2024-10-19 12:08:00 | TERRA_M-T | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 0d15082d-8d59-3a02-875c-8d68e2e9fbe7 | -8.14164 | -38.16617 | 2024-10-19 12:08:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 337ec2d2-3568-3ccf-88c2-17980f2fc4fc | -18.08606 | -40.20073 | 2024-10-19 12:10:00 | TERRA_M-T | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 4f24220a-4c23-35ab-b89a-63169eea40ea | -18.05938 | -41.70206 | 2024-10-19 12:10:00 | TERRA_M-T | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 6e8258d9-fe1a-310d-825c-bfeb56e3a3a6 | -18.53093 | -40.69014 | 2024-10-19 12:12:00 | TERRA_M-T | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 2c205e25-73e9-32dc-a813-606750976f3b | -18.31347 | -42.16021 | 2024-10-19 12:12:00 | TERRA_M-T | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.1 |


[Clique aqui para ver as próximas entradas](README51.md)
