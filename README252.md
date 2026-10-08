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

## Dados Diários - Página 252

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44756f56-089b-3e44-ab5b-837001ece56f | -3.36732 | -42.91315 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0930ab38-a319-3efa-8840-2600a93063bd | -2.87398 | -45.75747 | 2026-10-08 15:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| f23ad825-1d66-374a-b5e3-e06ea37438bd | -4.35932 | -43.80189 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a9cfc460-662f-302d-927c-c42b1b720cda | -3.80872 | -40.20134 | 2026-10-08 15:44:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| d4f7aad7-353e-3d61-a185-94fb796f4b4d | -4.43169 | -43.90006 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fba95e11-063c-39cf-a8e0-eb24960110e8 | -4.08261 | -44.10822 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 198.7 |
| da7ebbe7-24d0-3f99-80d7-af1ac9d7ed50 | -3.42735 | -45.04525 | 2026-10-08 15:44:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 465042ad-1050-3b19-8381-8395051a07d4 | -4.52867 | -42.62975 | 2026-10-08 15:44:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be54b6a4-c17c-324c-89e1-8fb44d17d72a | -3.85898 | -44.12154 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b5676bf8-6b57-38a2-ae43-febbfc824a62 | -4.59242 | -43.58674 | 2026-10-08 15:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8daba228-4eab-3b3b-8ce8-5e616a0b1db2 | -3.85956 | -44.12559 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 9fb716c9-1be6-35fb-ad17-ee561b0d6b7d | -3.49281 | -43.34023 | 2026-10-08 15:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d5cbe680-de2d-39d6-b554-66ef7877c6c2 | -3.21299 | -42.95938 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 1c67023a-df2c-3379-b102-6d92a5e6b0b7 | -3.91509 | -40.74152 | 2026-10-08 15:44:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 5de09de1-c216-3bf1-ae23-b3390d059122 | -4.84003 | -43.34116 | 2026-10-08 15:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e6256f8e-61ef-3198-8ee0-6a8ca4e7d412 | -4.84648 | -44.09454 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f9580d6e-7c3f-3cb9-acd5-5825ed018208 | -3.76823 | -44.35865 | 2026-10-08 15:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 33e2807e-f5e1-3f90-b4fa-484f8ffdbd25 | -5.10321 | -46.19859 | 2026-10-08 15:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| c08c0877-ad31-3810-8f94-41de1cf33540 | -3.44065 | -45.09484 | 2026-10-08 15:44:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1d015db0-5f55-3df5-b2ee-86d08a4dcb0d | -3.85262 | -44.11811 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e0028d84-f4f9-39a0-8966-a982ca7b617a | -3.2772 | -44.20202 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6adabc14-bd77-3045-b436-53d5e4760e13 | -4.05247 | -38.93458 | 2026-10-08 15:44:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| dddef0e8-3a16-326b-83eb-c3021ae13cb6 | -3.78629 | -41.66109 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 457c9c71-85d8-3ce7-8555-cb5d30bd4813 | -4.09653 | -44.12306 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 30eddb22-4a41-34ee-93bb-04f9296af903 | -3.91542 | -44.38914 | 2026-10-08 15:44:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| f494c0e4-83b9-3518-9f85-749aefee1292 | -3.25991 | -42.53814 | 2026-10-08 15:44:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff129a7e-24e4-37fc-b45d-f49e7f49ac3f | -3.25891 | -41.85073 | 2026-10-08 15:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| d925f950-c09d-3241-96ad-c2f9bca01f8a | -1.70724 | -47.77527 | 2026-10-08 15:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 636494c3-729e-39f3-a7f1-28d0ba9bdeb6 | -3.52961 | -44.31076 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a75a548-cba4-3e0a-81fb-d08dd1c43eec | -4.37171 | -41.82938 | 2026-10-08 15:44:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 4803d6f4-8ed6-381e-bef2-a9e9787a6f4b | -4.49478 | -42.54313 | 2026-10-08 15:44:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| db9865de-a016-3682-b3ad-b0dba3b1c3b5 | -1.67402 | -47.84079 | 2026-10-08 15:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| a064c6bc-0223-3713-bd27-f1e3023ac42c | -3.26625 | -42.95531 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 1ef9ccaf-a4e1-3e40-8ea1-dbf135493ebe | -3.40605 | -42.8087 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0617d6ea-5cb9-3590-b769-441450d68f21 | -3.45345 | -43.76596 | 2026-10-08 15:44:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ead8ae7-d08d-3c58-8b6b-38b91e7d2791 | -3.79279 | -41.67116 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 5650116e-f60e-32cb-b50f-c55d0c8ec574 | -4.08203 | -44.10422 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 181.1 |
| bc746b2b-25bd-38a9-981b-f344acd4938b | -3.13399 | -42.93298 | 2026-10-08 15:44:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d17b0c9b-f004-3f3c-b771-08beb6d8f8b2 | -4.08725 | -44.09961 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 12b168b8-56d5-3aa5-84fd-de5c8a6425c3 | -3.29288 | -44.68219 | 2026-10-08 15:44:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 567088d3-3fbc-3bc2-aa76-a7b10e3da12e | -4.31186 | -43.81267 | 2026-10-08 15:44:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 040dd47f-e463-333f-b6ba-5ca8066a1c34 | -4.36612 | -40.41885 | 2026-10-08 15:44:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 2e65b0de-0302-3b0e-9472-b306c538d8a6 | -3.20294 | -42.96293 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| a6e8ddd1-11dc-3465-b3cf-e1100409c301 | -3.45755 | -43.7642 | 2026-10-08 15:44:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99a6413d-1b05-3fd1-bf53-e4b73f61368b | -4.36097 | -40.41496 | 2026-10-08 15:44:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 779a6a03-00c9-3479-a2a1-2c0c6b078488 | -3.01191 | -43.34143 | 2026-10-08 15:44:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 31e8a375-e70a-3237-8bfd-33833e74d9d1 | -4.3725 | -41.83493 | 2026-10-08 15:44:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 21760db7-3e72-379c-b8cd-1658e7828434 | -3.17404 | -43.98462 | 2026-10-08 15:44:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f5c83d42-becf-34d0-9eba-9a1af8b0e3e1 | -2.47636 | -46.01728 | 2026-10-08 15:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| c623f686-885d-332e-a863-3d291143f5b6 | -2.99639 | -41.43172 | 2026-10-08 15:44:00 | NOAA-21 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3ee3dff9-c537-3beb-9974-31426c6a655d | -4.33786 | -42.79433 | 2026-10-08 15:44:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1545bf77-5c54-39e6-83de-6614a4f4d7ae | -3.78989 | -41.66315 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| df04d355-bde2-34dd-ad58-2084ddb3a223 | -2.99798 | -43.28445 | 2026-10-08 15:44:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e5a86d31-fe95-3be7-a0fa-da2a7b9d085e | -4.35914 | -40.41815 | 2026-10-08 15:44:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e7e14f3a-49fb-3796-bea3-1044483f06c8 | -4.09304 | -44.09899 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3efe14f8-5b99-3202-a2fe-95c4752c1fcf | -4.20681 | -41.75881 | 2026-10-08 15:44:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 71864f88-3166-374a-aea4-bfb25fc1a04d | -5.1337 | -46.02933 | 2026-10-08 15:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 96ca94fa-5482-3ef1-8dad-13d7d6c187cb | -2.87838 | -45.76345 | 2026-10-08 15:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| cd1b3eef-4810-3ba1-8257-8d572824c7dc | -4.09073 | -44.12367 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 99ee2e24-ca25-30f2-acac-1c935b1b74c2 | -3.11073 | -41.17163 | 2026-10-08 15:44:00 | NOAA-21 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e8133946-7f78-34ae-b93e-f1d8ea449ec9 | -4.19309 | -44.46981 | 2026-10-08 15:44:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3ee9c001-a57b-3913-af6c-001e66d96a55 | -3.44003 | -45.09699 | 2026-10-08 15:44:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c1e08c24-855e-390e-bbd0-e481c3eea0c2 | -3.73925 | -45.0769 | 2026-10-08 15:44:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3d8fb343-6c1d-30d8-833f-1b6c529af10d | -3.37295 | -43.02557 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3ff90fbf-9d8c-30a0-a199-06dbffa6aa21 | -3.1492 | -43.03741 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 25ad8584-4066-37a8-8457-e7bc6dc1e8c2 | -2.87692 | -45.75329 | 2026-10-08 15:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| d5499a83-2045-3737-8a95-3802ef3b2e05 | -1.70801 | -47.77122 | 2026-10-08 15:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 01d7718a-a99e-3c20-868b-16043af75900 | -3.89314 | -41.59751 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 141fa27c-0fe7-3ff3-ab90-ff8163473d40 | -4.0884 | -44.1076 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 0328c267-fff5-3835-a782-b39c3f052546 | -2.9926 | -43.2852 | 2026-10-08 15:44:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 49f3c586-dae7-3b16-b041-e10171724f4f | -3.52442 | -44.31563 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0b06479f-c696-300a-8ec9-e39c64fe1c35 | -3.51923 | -44.32049 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3dffe7e6-bd04-305b-8c70-5c88096a7b6a | -3.42637 | -45.04743 | 2026-10-08 15:44:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3de2e0b5-a6f8-3a90-8c47-189f830dcdc5 | -4.05297 | -38.93805 | 2026-10-08 15:44:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| d48541fa-a7e4-3f3b-8ad7-8718e2d1df87 | -3.81829 | -44.62436 | 2026-10-08 15:44:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| e0459642-67be-3a26-bf91-c9c1551a93e9 | -4.49524 | -42.5463 | 2026-10-08 15:44:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 88123362-4f4d-3763-9dd2-7eac8fdbdd8a | -4.43768 | -43.88622 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 238b5463-819a-330a-b19f-9f4179990a7b | -4.09714 | -44.12727 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 68070806-5e91-3a6a-8c20-9dcbfd04c393 | -3.41546 | -42.91244 | 2026-10-08 15:44:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2357327c-616f-3d50-a2d3-508373924eb5 | -2.83156 | -40.2273 | 2026-10-08 15:44:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d87f6639-8dd5-35f5-85ba-3ca345d80dc7 | -3.59607 | -39.14267 | 2026-10-08 15:44:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2f150bc2-dd60-3e66-8583-d22182842abc | -3.78711 | -41.66647 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 15133822-8c04-3bc2-a9b9-3771acdb77cd | -4.33603 | -43.8009 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 28b8ba7b-7366-3cf9-8da7-2696b57319ed | -3.01242 | -43.34484 | 2026-10-08 15:44:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b43bb61d-7abe-3fa7-be0f-2556d36e5815 | -4.15979 | -43.19757 | 2026-10-08 15:44:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f5d46acc-f276-3845-a1a2-4fd7879653f3 | -3.41577 | -42.91326 | 2026-10-08 15:44:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 342d4dde-7b5a-3cc3-aeab-e1e2772dc36c | -4.16906 | -43.33967 | 2026-10-08 15:44:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ebbbd24a-9097-34cf-826f-d7a6f851fda0 | -4.089 | -44.11171 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 654c75bf-0367-34a7-b9d6-be99c1252af9 | -3.00518 | -43.11322 | 2026-10-08 15:44:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c56423b4-a68d-3cff-be6d-1eb41cf57374 | -4.35252 | -43.79485 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ddd24be7-45c6-311b-b712-72cc53214dcb | -3.74998 | -40.04165 | 2026-10-08 15:44:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 29e2c7ae-42eb-32d0-99b1-056e0df42579 | -4.52009 | -44.0128 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| abac7406-493f-3811-8d61-4133316f43ce | -3.29022 | -42.68659 | 2026-10-08 15:44:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c6ca4542-e361-3828-a284-40172b2a6359 | -3.40559 | -42.80554 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9ca886ff-4e96-368e-a9dc-4e78ef4cb87c | -9.4819 | -66.765 | 2026-10-08 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 80d21c68-6f33-31e0-8c66-28f61f2b8604 | -12.4272 | -62.4425 | 2026-10-08 15:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 325145ec-f978-3dca-8c2c-92c3fce97f8d | -9.4818 | -66.8022 | 2026-10-08 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| cf9f46fd-2094-3e9b-80ea-3c1954ca947e | -3.4784 | -59.4631 | 2026-10-08 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 828bd40e-a37c-397d-8e36-a10142d575dc | -1.383 | -55.1944 | 2026-10-08 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| bd9140e8-8f0e-3631-86c9-d4d7d1e96b06 | -2.4805 | -56.1072 | 2026-10-08 15:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |


[Clique aqui para ver as próximas entradas](README253.md)
