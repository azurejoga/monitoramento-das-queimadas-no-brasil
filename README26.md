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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cd3236a-3a99-3974-802e-0501f18c0749 | -1.30775 | -55.43499 | 2025-11-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11ac4e5f-445d-3aed-b1d2-c005e82cc37c | -4.17112 | -43.73279 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bf154dca-be8a-36fe-b92b-c8246a743223 | -4.6752 | -49.38374 | 2025-11-26 05:10:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c59fe8ee-abc2-3de5-8ce3-3eddfbbf2ff2 | -5.21206 | -50.63226 | 2025-11-26 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e83b3881-fea9-3e9e-ab71-fdec4f03db9e | -4.17594 | -49.86422 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7d5530f-98d6-36ca-9873-60da059320b0 | -4.16699 | -43.71266 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bf10ae40-6bb5-3987-93c5-f152bfbddbdc | -4.01392 | -46.4994 | 2025-11-26 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e381fa6-725d-3aaf-8fa3-1ccae4453a42 | -7.74902 | -44.19489 | 2025-11-26 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58734cb4-6725-3735-b362-fdc2f9ab755e | -2.94435 | -51.97865 | 2025-11-26 05:10:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ff616cc-f854-36d7-8a9a-8b5e53790947 | -2.70218 | -49.51987 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30ec28e0-5b11-3575-8f13-6925a15a663c | -4.97405 | -50.87041 | 2025-11-26 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e708d32-beca-3bb4-b84d-3a886d025ecf | -3.44186 | -50.18669 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dda4a39b-cecc-3b09-82bc-770cdda04b4b | -2.63993 | -48.45543 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a357e577-1555-3de1-9149-9919144a4399 | -4.22614 | -48.37011 | 2025-11-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 06e07c6b-e800-363e-84ef-cb693d149a83 | -1.17936 | -55.69033 | 2025-11-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75119ea5-a8d8-3bf4-baf0-4cc46e8f9d8c | -3.16877 | -51.1622 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e7a1aea-e5d0-315d-830c-bea5a0cab6fa | -3.13335 | -49.40106 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 970688dc-fb8e-32f5-a423-22f56d1c9b3b | -6.04809 | -45.84064 | 2025-11-26 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52342aa9-1a41-3ae6-935c-4f7bf01e6977 | -3.16718 | -50.60109 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 199ea1ad-b409-31e1-a80f-2b97187e05d2 | -2.99069 | -49.59906 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ec348a1-1991-3e86-879f-7265612c56a5 | -4.96972 | -50.86972 | 2025-11-26 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8f099ee-9bf9-34e5-8b30-12bb368b9b58 | -1.3608 | -55.4218 | 2025-11-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3f36157-6723-332d-ab4d-f626e33af635 | -4.59791 | -44.41071 | 2025-11-26 05:10:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65570732-4b1b-355e-b283-12ad452bdc7e | -4.81412 | -43.8301 | 2025-11-26 05:10:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6495383f-6bab-3581-8052-6736b500d517 | -3.40197 | -50.5673 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a993912-8215-35f9-9793-ce41bb8e3d95 | -2.88221 | -51.80878 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb4c02e0-0f1e-3538-8193-5d47ac40f71a | -2.93275 | -48.21383 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d97d2b5-fbde-34af-a835-b9d39ba69e65 | -6.04874 | -45.83585 | 2025-11-26 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f91875c0-00da-37be-96f4-ed3dd2f51885 | -4.92508 | -49.01838 | 2025-11-26 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b6879217-1947-3e7a-a9e7-b9121c4a394f | -2.48432 | -47.82294 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 734c8479-8c4c-3c18-a076-b49f0de5c531 | -3.39322 | -47.18893 | 2025-11-26 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54c07582-e999-3e3a-b802-59962fa09ece | -2.03432 | -50.78855 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5967bfba-63ad-31bc-9505-ef4d56f34a10 | -6.57858 | -47.89821 | 2025-11-26 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99a734a0-153c-3565-89cd-72ffe1a54d3e | -4.16342 | -43.73774 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 6b5c8d95-35b9-34b0-9b43-97322f7068f6 | -2.94154 | -48.22433 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a835594a-c685-3fc0-9a36-6ffe2d57b6e7 | -1.36025 | -55.42527 | 2025-11-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1cbc516-8d14-3254-a026-553ecbdbc682 | -1.35639 | -55.42823 | 2025-11-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1605a2b-b675-3440-9e84-16f08f0935ab | -3.32468 | -49.71985 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 87198a8d-ced7-37ed-96d8-721225414d91 | -2.86952 | -51.78601 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b33e56a-d8cb-300b-a13f-9dcfe6f70a18 | -6.58354 | -47.90252 | 2025-11-26 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 814a9eba-d66f-376e-981c-90b30ff4daaa | -3.33052 | -50.26849 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a300660e-efd8-3e68-8e91-dd9a768b2427 | -5.71315 | -47.27054 | 2025-11-26 05:10:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a407c6e-1d7a-3510-a4d9-a7cf4a29f1af | -3.22038 | -50.58647 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0681542-5725-3bad-89b3-82c81f63be4a | -2.91965 | -48.23275 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9675122-a4c3-39a5-8290-ab75215a3b90 | -3.49362 | -51.21729 | 2025-11-26 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66aeadcd-ef79-342f-944a-9bce82903c9e | -6.76976 | -46.5169 | 2025-11-26 05:10:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d706e85d-a1cb-37fa-aa28-acef5c7333e9 | -4.17919 | -43.73211 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| df0ef11b-4dc1-39d8-bba2-9167a3d18a11 | -4.16808 | -43.71079 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 9205c726-61ac-38ce-a431-7abce3f798fe | -4.59709 | -44.41649 | 2025-11-26 05:10:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0a0e28a-7387-3240-84f6-1e2b229261d9 | -4.17037 | -49.86951 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f0011b9-a1ae-387d-a36c-6a346fedd6ec | -3.07943 | -50.26084 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89171517-9cb5-39d3-b89e-3e3b912abab5 | -4.53233 | -48.94591 | 2025-11-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af74a378-a49f-3c9d-943f-035220c946f9 | -1.36357 | -55.42578 | 2025-11-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f991a594-2c4e-39a3-9d48-3172f918ca36 | -4.17497 | -49.87018 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a97c242-9316-3839-b6e4-46a492337092 | -4.65227 | -43.97569 | 2025-11-26 05:10:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a234da9e-f16e-3377-8cef-3e1b81545977 | -4.01476 | -46.50067 | 2025-11-26 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 893c8f4f-e826-3a5a-87f9-6cffd77b8299 | -2.64114 | -48.45703 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8a2517c-c373-3c21-8356-823f899b6806 | -3.47405 | -43.42826 | 2025-11-26 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7220263-148a-3f43-acf5-069dbf2fe4a8 | -2.49369 | -47.83076 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c5f4ca6e-e0fc-3f87-a51c-8ebb48f3ead4 | -2.48292 | -47.83224 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 359e5172-9d4e-3ce7-98d1-7a6408ed9156 | -3.45116 | -50.54744 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ddbbcea7-ef43-3139-8836-2e2766546508 | -4.17834 | -43.73833 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 06d3208e-836b-3dbc-abab-bd55181ff799 | -4.18067 | -43.71501 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 94301035-e6a8-3177-9aab-86d3e0fb0cf3 | -3.20692 | -50.22104 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c97b0787-c096-3476-8afa-2edac0591c1c | -3.94936 | -49.45815 | 2025-11-26 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87eda426-0f6f-319a-97d7-fc6eb00c1f39 | -4.71987 | -46.46584 | 2025-11-26 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 973db9b0-bb51-3384-87ff-56227cfb6e5a | -2.93144 | -48.22273 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 16b2dc4d-319e-30e6-abd0-b736ffd7cd10 | -2.50539 | -47.82312 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a60b3d1d-29b4-3784-bdec-b50b2e1a7b95 | -2.49555 | -48.15592 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00c8928f-36f6-34f5-857c-87a2bc215a8c | -6.76916 | -46.52129 | 2025-11-26 05:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ca147ce-633b-350d-8fd6-0026d48e27f0 | -2.49884 | -47.83157 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8f84af4d-a256-3f87-bee5-1954e0c4bf75 | -2.49507 | -47.82159 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4872bdc6-953f-3a9c-b31d-ba6abc514c53 | -2.36756 | -52.70908 | 2025-11-26 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16df5905-d6ab-32d2-8c9d-e0f1fd66be16 | -2.50445 | -47.82932 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ba05e308-86c3-35e6-b2f3-5815fa5072c2 | -2.50071 | -47.81922 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78c1b622-3677-3465-830f-72faccb83f47 | -4.17492 | -43.71202 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 6a600d31-624d-3e46-8cb2-3e6bfcdfb34c | -3.32536 | -49.71513 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd13319f-4abe-33cc-ada1-355ce6d6fd9f | -2.42077 | -48.59562 | 2025-11-26 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 33fcc5a0-b146-3092-902b-ae3698c5ed2c | -3.4891 | -50.44206 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0984c413-769c-3150-a412-3b575199059a | -3.88112 | -54.20369 | 2025-11-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed742d12-afaa-3a8c-be7b-21019e78f657 | -3.96764 | -50.2232 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c1567bd-a62e-33bb-ae6d-cc00810f943e | -3.43875 | -50.17714 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c9bae7c-5ade-3c1a-8cc3-76b206dca18c | -3.42457 | -50.089 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c38f528f-b0b9-3e95-b769-d5cac187614b | -3.47584 | -50.79266 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51c0f299-0f77-383f-91e7-192513016c36 | -4.01331 | -46.50349 | 2025-11-26 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3c0b42a3-fed4-3470-a775-9308375a2177 | -4.18004 | -43.72586 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 93645937-1840-3225-b878-e5614e92d11f | -4.24861 | -48.5689 | 2025-11-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25bbb6f9-c0d3-3b4f-8bc8-9ed9873b18a9 | -2.94055 | -54.80004 | 2025-11-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbe04825-45e3-3f21-acd4-fe6a498f949e | -4.71164 | -43.99744 | 2025-11-26 05:10:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f457034-d2ad-3dc3-9f30-191e9ed236ed | -4.16897 | -43.70425 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2af8e2b-7e8e-3456-a9e0-0cadc055a172 | -2.9416 | -49.35497 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 87c43bcc-e09c-312a-bf11-a29b908e1eab | -2.48946 | -47.82381 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c53424fb-3c48-35ce-b56c-9086f8d15335 | -3.40686 | -54.57584 | 2025-11-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38ea81b8-3034-3127-8042-40a84689ab0f | -4.16968 | -49.87429 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8415d908-04bd-3ff4-b5cd-0b9f673fb370 | -4.66073 | -48.48106 | 2025-11-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8df13c73-f3bc-37c7-a8ad-afc87f71ee0f | -3.02854 | -51.09198 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cf587c0-2a76-39a6-bf6c-a68378f2fb22 | -2.44512 | -49.03005 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0af36e90-b32f-31d2-a54e-6b3df19421ca | -3.85528 | -49.36543 | 2025-11-26 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88677358-428f-3c57-b3c7-179829acdcd3 | -6.58519 | -47.90104 | 2025-11-26 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 595cdbf5-3aaa-3066-b27e-4a845039a1ba | -5.3287 | -43.56776 | 2025-11-26 05:10:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README27.md)
