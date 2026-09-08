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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c165efa5-c597-353e-a4cf-6f4423842839 | -2.72836 | -51.82931 | 2026-09-08 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26fe9afe-4df8-3e1e-8b9e-ab139c99e1e5 | 0.30505 | -60.44875 | 2026-09-08 05:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 893ed3b6-7290-3a93-8691-2712a356bde4 | 3.60528 | -51.79514 | 2026-09-08 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1fa672e-8a31-3518-bab8-5c455df9aa8f | -1.09788 | -48.05838 | 2026-09-08 05:01:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acdbd787-f97b-38d4-ab79-e1cc71307042 | -2.8686 | -50.44887 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72635874-3f7f-3572-9a28-c60942d40373 | -2.62985 | -46.77042 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e090125-bcc8-376b-a580-f9d746c4870c | 3.31748 | -61.30716 | 2026-09-08 05:01:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02014c46-2cbd-32e6-bac8-28f0c69da795 | -2.03383 | -48.57534 | 2026-09-08 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14c57df3-be16-3033-9488-446c5c2abf43 | -2.73234 | -51.82619 | 2026-09-08 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e231e155-5a78-31d0-9667-916a4b0c911f | -2.74049 | -51.37535 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7c1e1b9-2692-3902-a0fd-4b7fdd2e04b4 | -3.44898 | -47.27108 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab516435-68dc-33a7-b4a8-ac753cd7bd7c | -2.62916 | -46.77494 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09bd34c7-696c-3ea6-90fd-921782a8111f | -1.19338 | -55.71493 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 62396ffb-7e16-377e-b7db-2a3b09bd2f35 | -1.47624 | -54.80545 | 2026-09-08 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6d12b72-7d56-3b6e-85a7-1d8f139f1f46 | -2.73179 | -51.38561 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b5bac8a-30d2-3804-9fe3-a7a0546c2ba9 | -2.60722 | -51.21554 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95be8ffb-d46d-33d4-9cf8-759fef7aff2b | -2.75693 | -49.4798 | 2026-09-08 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfb86bef-4b2f-333f-8d0d-8a34c3315749 | -2.73584 | -51.38237 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17ff7de4-f532-3e5c-a167-91c7a48b3bdc | -1.984 | -48.38339 | 2026-09-08 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e27bf76-9f47-38b4-8846-cfed366df8fe | -1.48343 | -54.8473 | 2026-09-08 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 956561ee-6d55-3d77-b947-0195c22a9d19 | -1.19722 | -55.73561 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12808904-238b-3cb8-b46d-5ba3a2327d6f | -2.88009 | -50.44637 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4b21962-546a-38f8-a564-a509bdef8359 | -3.32863 | -44.59086 | 2026-09-08 05:01:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19f870c5-cb4c-3986-b3a2-12aadb74c41d | -1.56326 | -55.24828 | 2026-09-08 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8ce632d-e073-3b63-a3c6-f94450e97fbe | -3.33447 | -44.58835 | 2026-09-08 05:01:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2b52dbb-dffd-3fc8-854b-e96124bfb144 | -3.0679 | -49.51972 | 2026-09-08 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 11a7f692-17a9-37da-9651-15da39978ade | -1.47386 | -54.84206 | 2026-09-08 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a92fd3dd-6593-3504-a1c1-6601091e2b38 | -1.19946 | -55.74395 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3533b47b-e885-3201-9a1c-329cb053ed7c | -3.32329 | -44.59009 | 2026-09-08 05:01:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce781134-1c39-31b7-8254-32c376dd924a | -1.62477 | -55.17091 | 2026-09-08 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a2dcd46-3e1e-3a07-b293-ce3516eaf2a6 | -3.32913 | -44.58755 | 2026-09-08 05:01:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47a7263b-9036-3d2b-8942-f01817200a77 | 3.284 | -61.30197 | 2026-09-08 05:01:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32ac2def-0992-32ac-a581-68c97998e99d | -1.19021 | -55.7345 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85e3b7e4-9c63-3f29-ae6d-e851e74d49d3 | -3.44387 | -47.2748 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fda30b3-ef9c-3eea-97fa-80284af88578 | -1.19973 | -55.72002 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4e8cc3f-4b1d-3987-b910-48c7cfc7a013 | -2.88074 | -50.44222 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd243e91-9439-3a36-ba2a-cdae4a4d202f | -1.62195 | -55.16671 | 2026-09-08 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa2ab0a6-eef8-323f-8b99-af86240f07e6 | -2.87352 | -50.44113 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbb5336d-9bda-31e8-9c4f-d4787206dca4 | -1.61028 | -54.90714 | 2026-09-08 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 51ee854b-4bf4-3614-9094-44c38c5ca8e8 | -2.83294 | -48.65232 | 2026-09-08 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb8dda29-0d62-32bd-b1eb-21e698f1b191 | -1.09794 | -48.05868 | 2026-09-08 05:01:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd4bd696-b438-3626-bc91-603233778011 | -2.8324 | -48.65579 | 2026-09-08 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eebb09ba-c8de-3e52-b5be-0c6ce0580fcc | -2.63756 | -46.78085 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86a948b4-8fe5-3927-b1d3-6e7dc0cfa740 | -2.30309 | -48.57843 | 2026-09-08 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 298feb01-92ca-3f0d-a6ee-9a2da3350c4f | -2.73291 | -51.82255 | 2026-09-08 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9681266-e95e-3560-bd34-fc14cdcb8195 | -2.86925 | -50.44473 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03426096-c3ee-310d-86d0-4e5fd9fd1f68 | -2.74335 | -51.37966 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d9bdd80-14ea-3ad3-b843-84981f02c27f | -1.23785 | -54.10397 | 2026-09-08 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5c877f3-f8ec-38bb-a632-3a248049af25 | -2.30255 | -48.58186 | 2026-09-08 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab8586b4-577f-303b-a848-a211f78bc81c | -1.48738 | -54.84424 | 2026-09-08 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4832d5f1-ee5c-3b81-91a4-93052a4b85fb | -2.8699 | -50.44057 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5caba0e0-b3e1-3528-8c89-208e914b52b3 | -2.87286 | -50.44527 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e085493-ee74-3b7d-8827-81b611ddaf41 | -2.73574 | -51.82672 | 2026-09-08 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94738a48-707c-3e1b-a88b-96c671f2ca41 | -3.32278 | -44.5934 | 2026-09-08 05:01:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b79e6338-0cc3-32af-bc77-62d991690b7e | -1.225 | -54.22734 | 2026-09-08 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 663ddbad-00a3-3005-9ccd-e0766aad09e3 | -2.62847 | -46.77947 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 341f6d05-0a82-38e8-8063-cfd63caccdd0 | 0.3044 | -60.44651 | 2026-09-08 05:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4a0e9ef-1c48-3c18-b9b1-929fa718f419 | -2.87778 | -50.43752 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 403f7269-adc6-3eab-8a6f-1e61a1b1c93f | -1.1923 | -55.7156 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 747d4fbe-6451-360c-9ad2-626df86df45d | -1.19659 | -55.7395 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d6cb96e-c47f-336f-9b1f-609c2fd69ca0 | -2.0333 | -48.57874 | 2026-09-08 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1c68b68-da11-3939-8be4-8757fdd3533d | -1.86795 | -47.9847 | 2026-09-08 05:01:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e0856a5-cbde-3313-8e13-b543b1833a00 | 0.30984 | -60.44799 | 2026-09-08 05:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ded7e68-a6d5-3703-b3b1-61f4d78c2e3f | -3.24095 | -47.24961 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c2ef40af-17b5-39a0-8258-3034f861ca4e | -2.63895 | -46.77172 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7fa229d-7069-37f8-b829-ede97aabadee | -1.19274 | -55.71885 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66ee7ac2-5cd6-3cd8-a9d6-a802451f881f | -2.63371 | -46.77561 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df1e72b6-4144-35d8-8b99-1cb4fa287929 | -1.61367 | -54.90767 | 2026-09-08 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45fb33b9-7af7-3b4d-b50c-470fdedbd879 | -3.24162 | -47.24527 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1554b673-f3cd-30ad-86b7-70dcf8bcd4b5 | -1.19372 | -55.73505 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c58332ad-f6b3-30c4-901d-f01e656c02b9 | -1.86628 | -47.98443 | 2026-09-08 05:01:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6de8bb8-5721-3d9a-b0f4-7e63028d1714 | 0.3092 | -60.44573 | 2026-09-08 05:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5076c632-3efe-39b9-8a01-f14b94035f47 | -2.02568 | -52.10857 | 2026-09-08 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b886aac-390b-3b53-b852-c76939c955b8 | -2.9787 | -49.26596 | 2026-09-08 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81dcc36b-10e1-3028-95d9-9724f9e96cf4 | -1.70443 | -55.17598 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef467b3d-fa5c-36f3-b438-d86f745ada7e | -2.88174 | -50.45936 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 496cd99f-9b11-3632-8bfb-961ce5d69847 | -2.75312 | -49.47922 | 2026-09-08 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9990619c-c9e7-3788-9b7e-d56a1ad12e1c | -2.82838 | -48.65519 | 2026-09-08 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32367d46-e072-3224-8282-8f569469207c | -1.20009 | -55.74006 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e52360ac-7d64-3872-a96e-36ec325758d3 | 3.31798 | -61.3105 | 2026-09-08 05:01:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05fe4845-34f2-3f3a-ae20-678318e0aaee | -2.82893 | -48.65171 | 2026-09-08 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cd87814-9b6f-3f9b-97a3-e2e533976e06 | -2.96916 | -49.5595 | 2026-09-08 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd64e813-a90f-3f69-9c37-f10a45553b56 | -1.20584 | -55.74895 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 505913f2-889d-3b1d-8f6a-cd9045bcab33 | -2.63439 | -46.77109 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78f7fa8a-2269-32b6-b0f7-95f0fcb5e1af | -1.20671 | -55.72119 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f2bf656-e19c-3134-b056-487a9a765ede | 3.60968 | -60.46288 | 2026-09-08 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e54c1c7f-b5df-3a79-9023-b53637d2f6a1 | -2.97797 | -49.27079 | 2026-09-08 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2711e421-18b6-3908-8dce-28b87639de5d | -1.60886 | -55.4464 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f55c488d-b2fe-3b8c-af0f-a0d0e9364a83 | -3.44832 | -47.27544 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87411f6a-960d-3f13-8152-3a7fe3d85cdc | -2.95887 | -48.70745 | 2026-09-08 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab56de49-e62d-3f15-a30f-9848b2ac18a7 | -1.23451 | -54.10347 | 2026-09-08 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b8dfd6e5-8cf5-36ae-966b-f58bd7887b0c | -1.20609 | -55.72509 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f55fe44a-d5dc-3f2f-8cea-9b05cff1dc54 | -1.20322 | -55.7206 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b3c5122-f5dc-3bb5-aead-6aebb7098646 | -1.63183 | -55.12686 | 2026-09-08 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56408c7b-849b-39b6-a3c4-5b444145eb1d | -1.19084 | -55.73061 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e554c3e-10fc-39b3-a2f6-d2d5d159f81a | 1.13255 | -59.45142 | 2026-09-08 05:01:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfb97780-7005-3bef-be18-f31bbe2f1d2d | -1.19434 | -55.73116 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7387fd0-8e83-3c29-a0b6-ca70fa32b2de | -2.63825 | -46.77627 | 2026-09-08 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fe59be1-ed5a-3855-b903-f716740e1b97 | 3.61517 | -60.46505 | 2026-09-08 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2de0940c-d8b5-31c8-b958-b9f0f5533d99 | -2.87713 | -50.44167 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README19.md)
