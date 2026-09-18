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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f192378-3f08-3bcf-a9b7-34fa3eb56eda | -11.2787 | -43.3643 | 2026-09-18 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 467.5 |
| a3eb1d65-3fcf-3ea7-a4ea-88f61db52676 | -7.0086 | -43.6264 | 2026-09-18 01:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| ee815d6f-6377-38d7-a581-72c77a269ac3 | -2.8284 | -50.4863 | 2026-09-18 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 2a941134-40f0-37d4-a705-b92916465375 | -4.5961 | -42.95 | 2026-09-18 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| cdf4862d-c91a-3c66-9c6a-e46db4a05fe4 | -4.596 | -42.9734 | 2026-09-18 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 9272efce-4885-394f-a9e8-f2ee4e95838e | -11.2975 | -43.3851 | 2026-09-18 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| ae14f46a-8d46-3954-afc2-3747c4f02910 | -11.2783 | -43.388 | 2026-09-18 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 9e9c1e7b-ea8d-3d1c-ad91-9631dcf50332 | -11.2979 | -43.3614 | 2026-09-18 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 263.2 |
| ec3aaff6-9f10-3d4d-9967-aa907e3130dc | -9.7177 | -54.8162 | 2026-09-18 01:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 75f64bb8-b8c8-319a-af64-37a359f0b0c8 | -2.8101 | -50.4658 | 2026-09-18 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| d585c51b-be48-32e5-9600-aa0b1a944dd9 | -2.81 | -50.4868 | 2026-09-18 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7eaba132-8114-332b-832c-4e13895156e0 | -2.8285 | -50.4653 | 2026-09-18 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| f5f6f8fd-ddd4-3650-b1af-4c9c0bda6f33 | -5.7429 | -57.6009 | 2026-09-18 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 2c9764c1-8be9-3346-bc41-61b43810e4f6 | -4.5585 | -42.9758 | 2026-09-18 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| fb744a77-090c-3af8-95f1-32ec5d8416df | -9.7179 | -54.796 | 2026-09-18 01:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8c43991e-18e1-3e0b-83a7-2e81b8ddbfd6 | -4.5772 | -42.9746 | 2026-09-18 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 163.0 |
| e9a482ce-5dce-390c-bd87-6673d85581bb | -19.1812 | -48.7717 | 2026-09-18 01:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 98.8 |
| f44758a0-bd4a-3a73-994f-a49597ebff63 | -4.5587 | -42.9523 | 2026-09-18 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 1369d4c9-cf00-393d-b0b7-f59446bb86aa | -4.5776 | -42.9277 | 2026-09-18 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ba730eb6-6a3a-3ad4-bc9e-3c0018eee137 | -3.3823 | -50.4486 | 2026-09-18 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 12eb2096-1c01-31ef-a8e0-86661aea01ab | -5.7615 | -57.5807 | 2026-09-18 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 4a106bd8-2fcb-3a6b-a5c2-8c6bed69460b | -3.3638 | -50.4492 | 2026-09-18 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| ad5847c8-d2bc-37a2-9220-6e541e316f10 | -3.4455 | -58.2134 | 2026-09-18 01:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| ae77df65-16d1-3090-8c97-25c5b744da30 | -5.7431 | -57.5814 | 2026-09-18 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| a2d3747d-028a-39ad-90b2-5ecb2e7009f4 | -9.7177 | -54.8162 | 2026-09-18 01:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 87053b1a-804f-3261-91e8-95a4fe055f51 | -2.8284 | -50.4863 | 2026-09-18 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| fbec758d-8963-312f-ad59-3e0760a441cf | -5.7615 | -57.5807 | 2026-09-18 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 82376847-01d7-3404-81e2-c41f612e9d9f | -3.3638 | -50.4492 | 2026-09-18 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 3647df9c-69fa-357c-91ab-edba672f0f14 | -11.2979 | -43.3614 | 2026-09-18 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| fcc2608b-1668-3c4f-83c7-a228662cc326 | -4.5587 | -42.9523 | 2026-09-18 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 53cbc4db-0606-397c-ae09-f795cbb1845c | -5.7569 | -45.084 | 2026-09-18 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| d7d67eb5-2f2c-3d41-ae33-80f38a17af19 | -7.0086 | -43.6264 | 2026-09-18 01:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b457eb52-0ede-36da-9485-f87ab645c848 | -9.7179 | -54.796 | 2026-09-18 01:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ee5442ad-1b23-3cef-bd80-5244b113c608 | -4.5772 | -42.9746 | 2026-09-18 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 677f8860-dd88-372f-a18d-6cb5c3458cfc | -5.7429 | -57.6009 | 2026-09-18 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 4efd3d65-f8dd-34ef-a59b-1f4022bb655f | -12.4359 | -50.6827 | 2026-09-18 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 82b47968-2de5-36ff-b1b0-acd7c61663ea | -6.1359 | -59.9446 | 2026-09-18 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d4a3a1f5-ee69-3709-8ccd-53d9466c017b | -9.699 | -54.8176 | 2026-09-18 01:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 6e1934b7-a2e4-3116-b743-f23ff2bf2903 | -11.2787 | -43.3643 | 2026-09-18 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.1 |
| bb75cd0e-6acc-3f2d-b3bd-1161876890a3 | -4.5961 | -42.95 | 2026-09-18 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b2904fc1-a348-3b7f-bd1c-e7d9487d6e09 | -2.8101 | -50.4658 | 2026-09-18 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| a3fb6398-4b19-3ba1-8dc9-174f3cc6d5aa | -12.4547 | -50.7019 | 2026-09-18 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| edb4f273-96e4-3021-bed2-d8c9792565d2 | -12.4742 | -50.6781 | 2026-09-18 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d7ac98d6-b9fe-3f55-8e83-76b835f7bd56 | -4.5589 | -42.9289 | 2026-09-18 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 7c0a82a6-5ade-3985-9c0d-2f74d5b7c088 | -19.1812 | -48.7717 | 2026-09-18 01:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 80bd93a3-9ecc-3ed5-80e3-ee890ec2b991 | -12.4551 | -50.6804 | 2026-09-18 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 132f1db2-f467-39ed-b6e7-48348fc46855 | -4.5776 | -42.9277 | 2026-09-18 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f84e4e57-6f5d-3795-a05b-dcbeac67747c | -3.3823 | -50.4486 | 2026-09-18 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 77a8a7a5-c3f9-3e0e-8bf7-d9fba3eeaa8c | -19.1806 | -48.7946 | 2026-09-18 01:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 81.2 |
| faf15e38-a5d5-33c7-87d0-bdf7ac397da5 | -4.596 | -42.9734 | 2026-09-18 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f31b2e90-a7d4-3c2c-8687-951465c5c123 | -7.0275 | -43.6247 | 2026-09-18 01:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 6e482025-1804-366a-9676-969dc3db426e | -4.5774 | -42.9512 | 2026-09-18 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 278.7 |
| 3d864677-4ceb-3296-88ea-421c45f7f684 | -6.3656 | -58.2966 | 2026-09-18 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 51638150-f90c-3852-a4a6-233eadb381cc | -5.7431 | -57.5814 | 2026-09-18 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 68fc3638-a0e0-3136-971e-b95999bf5882 | -11.2783 | -43.388 | 2026-09-18 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8c668d17-7f2e-3b35-a6d3-f42125e06df5 | -3.028 | -51.376 | 2026-09-18 01:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 28244aa9-eaf0-3ab9-a699-3cf437e33b43 | -2.81 | -50.4868 | 2026-09-18 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| d514cfc1-a1c8-3789-a49c-6eb1a3db234e | -2.6125 | -54.7577 | 2026-09-18 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 52fa560c-f455-3e17-9332-96b25010809d | -3.0465 | -51.3755 | 2026-09-18 01:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 53f765fb-45a0-363b-b6aa-94efd4b980c3 | -11.064 | -48.2898 | 2026-09-18 01:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 9c212eb9-fbb9-3217-8a34-247f2c52a75d | -5.7567 | -45.1067 | 2026-09-18 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 4cd0abff-2b50-3100-9a41-37c8f7e759c3 | -2.8285 | -50.4653 | 2026-09-18 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| a4d9a938-364f-3028-bcf2-30949d02ea56 | -7.0084 | -43.6497 | 2026-09-18 01:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 4fbf8673-db6d-350f-bde7-0a9617cbfb26 | -11.2787 | -43.3643 | 2026-09-18 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| ea2d3499-0cdd-3451-854e-a7c81dcc2338 | -19.1806 | -48.7946 | 2026-09-18 01:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 64aa6f6f-bace-36cb-941f-9f6e214c1b4c | -19.2015 | -48.7675 | 2026-09-18 01:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8b5d3e9f-d7fd-3b9f-96c5-8703085fb8d1 | -12.4547 | -50.7019 | 2026-09-18 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c83f887f-8e68-3de7-aea7-b819c68fcb83 | -3.3638 | -50.4492 | 2026-09-18 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 2a45d58e-1521-3486-9bbb-ea18e50590ec | -12.3397 | -50.7371 | 2026-09-18 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 97de7972-4c92-31ec-8816-b94a2d1d100b | -12.3585 | -50.7563 | 2026-09-18 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 455a4c26-f710-385a-a6d4-350dbb031e8e | -9.7365 | -54.8148 | 2026-09-18 01:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 950a9386-c342-3053-b845-8012efcfa0a2 | -12.3394 | -50.7586 | 2026-09-18 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 8aaf7079-11d6-3a0a-b43a-44fb493ab702 | -5.7431 | -57.5814 | 2026-09-18 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 056fd1e2-ed53-31d3-aaec-d74e1fc51b1a | -12.3588 | -50.7348 | 2026-09-18 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 164fb28a-05cf-3a29-a1d9-c071cf23fbfc | -12.3206 | -50.7394 | 2026-09-18 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| ddd28b09-a80e-30d7-9f34-d396d9caae84 | -2.8101 | -50.4658 | 2026-09-18 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| fd4dc355-18e7-3ea8-8705-e70b253cf276 | -2.6125 | -54.7577 | 2026-09-18 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 486d28d6-d9e6-356d-ab57-b2392fe96ae3 | -2.81 | -50.4868 | 2026-09-18 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| db22184a-74b4-327e-9f17-8619bff3ec9f | -21.6079 | -50.0054 | 2026-09-18 01:50:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| 4b0e5343-ab26-30c8-bf5a-12fb69cadfe4 | -9.7177 | -54.8162 | 2026-09-18 01:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| a2ac63ab-a57c-359a-8724-334e3f31a75d | -9.699 | -54.8176 | 2026-09-18 01:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 0412844a-a2ab-3f00-ac22-8d7b369e8caf | -21.6286 | -50.0008 | 2026-09-18 01:50:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| ba87325d-f6e8-365b-bb60-2aca96518a80 | -2.8284 | -50.4863 | 2026-09-18 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| ba2f3526-113d-36b8-b9f8-8c1fe48ee135 | -3.028 | -51.376 | 2026-09-18 01:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 82c7847f-2ce9-3108-b8f5-2dc4d67747d1 | -2.8285 | -50.4653 | 2026-09-18 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 0dfba991-a42f-33cd-b9d1-fa3d2c453111 | -19.1812 | -48.7717 | 2026-09-18 01:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 3555bf60-4803-37c8-9f31-db579974c4a2 | -11.064 | -48.2898 | 2026-09-18 01:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 034761cb-a12c-3390-bf7f-95eb20046997 | -12.3203 | -50.7608 | 2026-09-18 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 6aafb282-0178-362b-949e-aed688078c4b | -4.5587 | -42.9523 | 2026-09-18 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 10eb7306-5b7f-3186-936a-898b6f84ac20 | -4.5774 | -42.9512 | 2026-09-18 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 245.3 |
| 028ade36-2ff9-35e9-a9c1-4a6c93f71fdf | -12.3977 | -50.6873 | 2026-09-18 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f6332d4f-d5ac-349e-84d2-36f50d559f96 | -12.3782 | -50.7111 | 2026-09-18 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c985b4da-bb73-307b-a8bb-a2561ca214b3 | -3.0465 | -51.3755 | 2026-09-18 01:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 6225c470-27dd-3123-8128-22747a4df84e | -5.7569 | -45.084 | 2026-09-18 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| b0ab9ec8-d35f-3f1f-ae01-850c0db02206 | -5.7567 | -45.1067 | 2026-09-18 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 3c518727-63c8-3b9b-a942-8639681a68a3 | -4.5772 | -42.9746 | 2026-09-18 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 842b667b-39db-398d-b0b1-1776ed1a495d | -3.3823 | -50.4486 | 2026-09-18 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 03cc78fd-9eaf-3680-b96b-8a050318472b | -4.5961 | -42.95 | 2026-09-18 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f2eb7792-ec27-36fb-9613-4e3906477f41 | -5.7429 | -57.6009 | 2026-09-18 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 62855804-cc8e-382e-8d9d-38cab45bff5d | -7.0086 | -43.6264 | 2026-09-18 01:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |


[Clique aqui para ver as próximas entradas](README20.md)
