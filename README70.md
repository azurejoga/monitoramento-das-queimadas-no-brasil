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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5f8c62a-d375-33c9-957b-717311e8726f | -16.95007 | -57.92847 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 83c5ba93-b4cc-36ce-aeae-be655174fb6b | -16.94993 | -57.94136 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 2f5ec8fe-8cd3-3a37-8e25-50d5a83a28f7 | -16.94967 | -57.93213 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d6752a89-48d3-31e3-81b8-3585471133dd | -16.94955 | -57.94503 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b35187d9-2807-3342-a232-4c9ca3d97c64 | -16.94926 | -57.93578 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d9c0ff49-a70f-354e-a5c3-f2849ad64aa4 | -16.94885 | -57.93943 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c20dbf0d-f395-3711-b11f-dc94a6592551 | -16.94844 | -57.94308 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1c322f30-c397-3803-97da-883fba5ffe2e | -16.94561 | -57.9297 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6aec2715-f331-394b-8adb-329abfeac21e | -16.94486 | -57.937 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 86ef2eda-4b31-38fc-9c8b-221ea2821208 | -16.94448 | -57.94064 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c6a50112-b102-3ca0-ac8f-f0f0382a0957 | -16.9441 | -57.94431 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c1138db3-d74f-3ebc-b839-00be11ada19d | -16.94381 | -57.93509 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 66aa18cc-eb20-3c7b-bf18-775ec020b1e7 | -16.94372 | -57.94794 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d211a2b4-8634-3301-9e3e-1c449f7fecda | -16.9434 | -57.93874 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5ba9dd15-e743-303d-8346-ee141e4ebe1d | -16.943 | -57.94239 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 28a95020-fbd9-3a2c-9b04-9282b271e01d | -16.94259 | -57.94603 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d7fc874d-768e-3b62-81e2-bcf1a8c5275b | -16.93835 | -57.93441 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b635eea5-4a0b-3b13-ab34-fd58d7de2449 | -16.93312 | -57.98159 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 2c6d3031-5959-3b31-9ef8-c80e166aaf1c | -16.9329 | -57.93373 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0d8a51dc-1b7f-3438-afbd-373c84fa97a9 | -16.93272 | -57.98521 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6574ab6e-16a1-3856-9938-c995f7487913 | -16.92785 | -57.92941 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d7d134a5-8564-368f-a161-a6e85c4a2fdf | -16.92769 | -57.98091 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e1a7fe06-88b3-3dd5-8619-a97383520f9b | -16.92265 | -57.97662 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6d0be799-d4cb-3210-885f-53348b64ff1e | -16.92239 | -57.92872 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8ecc935b-c13c-3978-8779-4847358abb20 | -16.92225 | -57.98024 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 979d41ac-e2c2-3e8a-9ab0-3207f8cae1c5 | -16.91761 | -57.97232 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 0f8a7ede-dfd8-3bfd-8719-5236e8dbdc1d | -16.91721 | -57.97594 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a6805150-fa33-3f89-a929-21b1ad0ad726 | -16.91681 | -57.97956 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| eef4914a-e542-357e-b1bd-254981338482 | -16.91376 | -57.95713 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 70c87a38-01fe-339f-bd7d-e279556f1a18 | -16.91336 | -57.96075 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| c4f16af4-8cdb-3427-91f2-8ae6ce9fc2fd | -16.91296 | -57.96437 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 56adff9c-afde-3040-8c30-3c6f33447d4b | -16.91257 | -57.96801 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9880dbee-b699-32ef-937e-3d9a32ef34d3 | -16.91217 | -57.97163 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 37e2fe27-f322-36c2-84f5-890f6453a9e5 | -16.9095 | -57.94555 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f98a4076-7987-323a-b51e-28f49eec8c51 | -16.9091 | -57.94918 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a132608a-0bf3-3e9e-827d-fd254773e263 | -16.86334 | -57.69958 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 764557e5-f572-36dc-acd8-fab60d8a88c4 | -16.86292 | -57.70336 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 46e04be7-c957-3d62-a359-c120c3cae6c5 | -16.86287 | -57.70291 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a7d64987-0bd5-3dfd-b79f-d3c98d86070f | -16.8578 | -57.69889 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 14f98b6e-2fb0-3a99-8f8a-d7120fb19903 | -15.93354 | -59.5582 | 2024-09-29 05:46:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77291ff1-445e-3789-a527-b7ea1b9314b7 | -15.92976 | -59.55706 | 2024-09-29 05:46:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9923aa47-f54e-370e-b0cc-8b5f62c4e60e | -15.92871 | -59.55755 | 2024-09-29 05:46:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36dcfa03-6511-3080-a33b-0c5e018f8743 | -4.8363 | -50.92591 | 2024-09-29 06:01:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2ffd94a7-f8a7-369c-b9d2-4cd8b02ce454 | -3.88548 | -52.36699 | 2024-09-29 06:01:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d5cef7fa-21c2-33bb-9ce4-d395ce21918e | -3.56562 | -50.3723 | 2024-09-29 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 1736e7e8-2899-39bc-b7ab-139e57d51cfd | -3.56465 | -50.5704 | 2024-09-29 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 08e05540-12d3-3a15-a7bb-9c2c39820bb0 | -3.56067 | -50.58156 | 2024-09-29 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2434109e-2d75-3921-a14c-7530b3f4f2af | -3.55299 | -50.37037 | 2024-09-29 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7f869683-060e-3bfb-bd15-0c6d3f222e35 | -3.50087 | -51.19851 | 2024-09-29 06:01:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9d4c8ead-1a79-3a15-afe7-1beb106e13d3 | -3.45484 | -53.79794 | 2024-09-29 06:01:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 63a434f1-d74e-3dc3-9e90-e76800ea801f | -3.4426 | -54.08666 | 2024-09-29 06:01:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a4a6cb88-2927-30e4-a716-d4ad7890c692 | -3.32697 | -50.30681 | 2024-09-29 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fd4cb312-8229-3112-ac11-158f1ab0be72 | -3.32594 | -50.30146 | 2024-09-29 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| fcefd048-ae4f-377f-8686-67385676ce58 | -3.13263 | -53.68315 | 2024-09-29 06:01:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 405cd35d-f339-33ac-8b69-5ad6c29f4007 | -3.12478 | -53.73712 | 2024-09-29 06:01:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 308a065b-489b-3d0d-9884-04a2e638c75f | -3.12322 | -53.74783 | 2024-09-29 06:01:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 86dabd1f-cbbe-3c50-810d-65c9399db396 | -3.09505 | -50.47286 | 2024-09-29 06:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 8c92c82f-722d-3dc9-9a5c-9ebc03c42b34 | -3.09247 | -50.46725 | 2024-09-29 06:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 44f9cd86-31ae-3325-937d-e9d6a525b70f | -3.08979 | -50.48565 | 2024-09-29 06:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| ad5a9560-f988-3854-97be-4bad34431cca | -3.08003 | -50.46546 | 2024-09-29 06:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 3e2391e6-221b-316d-86ea-6111d82f555e | -3.07736 | -50.48392 | 2024-09-29 06:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 4c1746a1-1455-30e0-a1b1-52ced969d3fd | -3.06493 | -50.48218 | 2024-09-29 06:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 56a39ee8-7f5a-356a-a5dc-bebab7625bfe | -2.95487 | -51.64658 | 2024-09-29 06:01:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0841fade-b77b-3b25-8602-2cc148f11443 | -2.87208 | -51.65969 | 2024-09-29 06:01:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1c58d944-a61a-332c-a482-e4847b8f5858 | -2.86997 | -51.67444 | 2024-09-29 06:01:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 8b04c9b4-c6e2-39ad-b9e0-24b2385b0106 | -2.84811 | -53.31394 | 2024-09-29 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b0e3da6d-7272-3be0-b473-74cdfa8582f0 | -2.67959 | -52.43804 | 2024-09-29 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8f7ed3c3-4106-3d30-9df0-3937dc1e57e6 | -2.66862 | -57.49966 | 2024-09-29 06:01:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 32d5d664-cd11-35ec-b83c-6f054bbcac72 | -2.64928 | -57.50613 | 2024-09-29 06:01:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 45969c8b-a817-3836-81b7-b8e19ac3c7da | -2.36528 | -47.59277 | 2024-09-29 06:01:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9b160013-e851-3b67-8c0e-72adbf6ddb5d | -2.35498 | -47.58362 | 2024-09-29 06:01:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 2664dfc7-00ff-3bd2-a685-af04372c1db9 | -2.35047 | -47.61393 | 2024-09-29 06:01:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 42a14048-3db7-3277-9946-d354db97e019 | -2.15072 | -53.66951 | 2024-09-29 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 483a0257-0139-3201-b666-0783f00dc07a | -2.14266 | -53.65755 | 2024-09-29 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 2222e4bc-fe7a-35cc-9eaa-6602f3c3fc3c | -2.14111 | -53.66805 | 2024-09-29 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| f3962671-c958-3d6e-94e5-42358b8cc062 | -10.7257 | -60.75706 | 2024-09-29 06:03:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ed98e2de-c3a2-304e-991d-4ded71151e33 | -10.69386 | -58.53066 | 2024-09-29 06:03:00 | AQUA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a41f06e4-53e5-304a-ad62-63b7d9d29d54 | -11.06279 | -52.477 | 2024-09-29 06:03:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1600.5 |
| 5f21f53d-072f-37f1-9532-13403dfd1128 | -11.0605 | -52.4943 | 2024-09-29 06:03:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 1887aaf8-03de-3690-aff4-a19fcd9828de | -9.8235 | -58.97205 | 2024-09-29 06:03:00 | AQUA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4f30a3a8-2347-3efb-885a-c2bcb56788a9 | -8.08431 | -55.39115 | 2024-09-29 06:03:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d5d9d6c1-78fa-3b2b-8d1b-b14316703e13 | -8.00911 | -55.71359 | 2024-09-29 06:03:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 609220b9-77e1-3cd0-a02f-ac9c15b2e1a5 | -11.0507 | -52.47536 | 2024-09-29 06:03:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| dc630663-a6f6-3add-82cb-2abeb12cf8d5 | -12.27759 | -50.47908 | 2024-09-29 06:03:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 71af46bd-de59-3aa6-9045-b3aa8ebd483e | -11.84259 | -59.05448 | 2024-09-29 06:03:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6bd1f17a-83a2-3a72-be6b-a4baf02de3de | -11.68387 | -59.30482 | 2024-09-29 06:03:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 10d1480e-e4c9-337f-86e3-716400621413 | -11.2102 | -53.86418 | 2024-09-29 06:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| c57c0b2a-81f1-3b96-af75-637a78c765b7 | -11.19933 | -53.86274 | 2024-09-29 06:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| b872af34-abfa-3ed3-898f-50a47e699123 | -11.17396 | -53.88753 | 2024-09-29 06:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| da8989f2-62cb-35f1-b349-837dda0e209d | -11.17216 | -53.90127 | 2024-09-29 06:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 3c07e583-b564-3040-a53b-d7d4710f102d | -11.17201 | -53.88055 | 2024-09-29 06:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 91d55b1e-7afb-3ff9-ae65-8424695f10b2 | -11.17012 | -53.89426 | 2024-09-29 06:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |
| b7e0f352-f950-3f51-917d-67afaaa0f0b5 | -11.16311 | -53.88615 | 2024-09-29 06:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| eebeaef5-656c-3337-9b12-75091e14e51e | -11.16132 | -53.89988 | 2024-09-29 06:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 55a1e415-b44e-3117-97aa-0d72cb229094 | -11.07491 | -52.47845 | 2024-09-29 06:03:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 62736d4d-6041-3c5a-8c78-4d98dc33d701 | -11.07015 | -52.46526 | 2024-09-29 06:03:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 310.1 |
| 7d1fbacb-57c4-32d2-99fc-e5c28989cd90 | -11.06795 | -52.48287 | 2024-09-29 06:03:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 325.6 |
| 1479f761-48e8-3ca8-95c5-18716dff3182 | -11.06512 | -52.45939 | 2024-09-29 06:03:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 234.1 |
| eda76abe-692e-37a1-bf8c-e613b19e8f12 | -10.9537 | -63.58296 | 2024-09-29 06:03:00 | AQUA_M-M | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ae75c29b-3311-3e26-bb15-59c3b144e555 | -10.9513 | -63.59732 | 2024-09-29 06:03:00 | AQUA_M-M | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 18.3 |


[Clique aqui para ver as próximas entradas](README71.md)
