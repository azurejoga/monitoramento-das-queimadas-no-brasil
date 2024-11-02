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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29d4a6b8-871e-3d7b-8293-7219ff0f38d7 | -1.4717 | -46.7214 | 2024-11-02 03:35:14 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e110dabd-198a-30f8-a974-3552c0d3a7b6 | -2.2663 | -53.7422 | 2024-11-02 03:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 000f325c-e6d1-3e55-abdb-1d27475189d4 | -2.8386 | -52.8794 | 2024-11-02 03:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c01255d3-ad9c-3fac-a4ef-fd74c5276a90 | -3.0734 | -54.167 | 2024-11-02 03:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c9c1fbfe-bacf-384b-b632-7ec3453570d9 | -3.2207 | -45.2925 | 2024-11-02 03:35:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e6f2fff3-0b76-3237-9e96-4c3b404451a3 | -3.1281 | -54.266 | 2024-11-02 03:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e51d65fd-c79a-3ac1-a942-df914a02331e | -3.1098 | -54.2665 | 2024-11-02 03:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f69724e4-91e9-3636-b767-e5d7c14c9f95 | -3.1097 | -54.2865 | 2024-11-02 03:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 04d0c281-5c8a-3f24-9b4a-e6508551e1e5 | -3.7888 | -43.5545 | 2024-11-02 03:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7e1b2a61-7c00-3f50-9e7d-0e23e278435c | -3.7701 | -43.5554 | 2024-11-02 03:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a1915bcf-c574-3209-8070-9d95557418d1 | -3.9474 | -48.3451 | 2024-11-02 03:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 914421de-cbe1-30f9-bafb-ee11447fa75b | -3.9473 | -48.3666 | 2024-11-02 03:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 588c3c73-d7be-386a-a68f-9729483d07a4 | -3.9289 | -48.3458 | 2024-11-02 03:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3540eba2-d2b3-3d60-8b3f-5ef5d619c053 | -4.3537 | -48.6068 | 2024-11-02 03:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 6090724a-a8e5-3d02-b185-92ec11410930 | -4.4054 | -43.4746 | 2024-11-02 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b3d2471c-9182-3a37-a310-5ab28a5f3f76 | -4.3869 | -43.4525 | 2024-11-02 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| f5526f91-46a2-3d35-8b41-40e78ab2e451 | -4.3867 | -43.4757 | 2024-11-02 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ca11f317-6156-3e74-a655-f6fd8c225c00 | -1.4717 | -46.7214 | 2024-11-02 03:45:14 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| c70e93a8-3293-3f96-9d78-08ccfc47c4cc | -2.2663 | -53.7422 | 2024-11-02 03:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 057c3a0f-0c45-39b5-89ec-9ae8abbcfddb | -2.8061 | -51.6095 | 2024-11-02 03:45:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 02d20676-113f-39aa-82bc-bf10b364e868 | -2.8386 | -52.8794 | 2024-11-02 03:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 4654683c-3800-3494-9d32-8a89ce80c306 | -3.0088 | -51.5834 | 2024-11-02 03:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 78d4fb0f-511f-39f7-b130-3f83891d870b | -3.0734 | -54.167 | 2024-11-02 03:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| a5028645-969d-39a3-82d3-b09ff6b4b4ed | -3.1097 | -54.2865 | 2024-11-02 03:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c5e7f778-a349-32df-8d37-2591e7409564 | -3.1098 | -54.2665 | 2024-11-02 03:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 43b37dff-df35-3aa7-84ee-a69ff525a96a | -3.1281 | -54.266 | 2024-11-02 03:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 58299421-1f40-34d7-a225-57d4b0f680e3 | -3.7701 | -43.5554 | 2024-11-02 03:45:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| af8287e8-7488-3f67-9eb0-a8aa63df6c09 | -3.7888 | -43.5545 | 2024-11-02 03:45:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 36ffeaeb-2fe2-31d6-9d2b-e7328cc9cd97 | -3.9473 | -48.3666 | 2024-11-02 03:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c90d26d8-12e8-35eb-830e-6166aa5c1383 | -3.9474 | -48.3451 | 2024-11-02 03:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| e357e9a5-6bc0-319e-be68-9fb6d397e730 | -4.3867 | -43.4757 | 2024-11-02 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 594778ae-d282-3a23-b493-dea557f61ab6 | -4.3869 | -43.4525 | 2024-11-02 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 69cf7e14-c8fc-3eb4-ac9f-e37936f056bc | -4.4054 | -43.4746 | 2024-11-02 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 322f42f2-7736-364c-9ddf-4583315416bd | -4.3537 | -48.6068 | 2024-11-02 03:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 4bbb7198-c49c-3c6d-b118-f75afdbf467a | -4.5575 | -43.1162 | 2024-11-02 03:45:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| dfcbc643-b234-3839-af80-732aae7d181a | -4.5577 | -43.0928 | 2024-11-02 03:45:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 5107a1db-29b5-387d-85b6-378df6486a1a | -4.5764 | -43.0916 | 2024-11-02 03:45:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| eac4f086-7ca7-3e86-b0d7-2002f40cf2de | -3.86514 | -41.03558 | 2024-11-02 03:47:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 35d2c65b-3703-306a-a5f5-50370b6754ae | -3.40129 | -41.64096 | 2024-11-02 03:47:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 50ee7617-3016-36f7-a832-faf64a66839e | -3.39643 | -41.64418 | 2024-11-02 03:47:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 39f1db2a-2704-3d25-bd62-a1d4abc21870 | -3.39157 | -41.64742 | 2024-11-02 03:47:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4736feec-3720-3fdb-a976-72f65a473279 | -4.58211 | -42.47157 | 2024-11-02 03:47:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 98ca0f8b-ef83-3095-a784-610c18096cf6 | -4.57704 | -42.47506 | 2024-11-02 03:47:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 810a8f57-ac7b-3bae-afb0-df18573604e0 | -4.7311 | -38.45768 | 2024-11-02 03:47:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73d53816-d179-3935-8493-8b3f45e0de35 | -11.211 | -39.90834 | 2024-11-02 03:47:00 | NPP-375D | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e681dc09-8d37-32ca-994f-0d2d06fa2e63 | -4.78769 | -40.06624 | 2024-11-02 03:47:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1562d1e8-23e3-397b-a85d-04dee548a06e | -11.5069 | -40.47496 | 2024-11-02 03:47:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 69c835ea-fde6-38f6-8f24-dc41a7a904bd | -11.11073 | -41.01358 | 2024-11-02 03:47:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| da3b2fcc-a445-3fff-a844-4b16422a286e | -4.56494 | -43.11883 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c8acb04-f0a0-3736-a5bb-dc4bd597c165 | -4.56113 | -43.1134 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdfccb9e-11be-3a13-8776-ca6ef0bccadb | -4.55811 | -43.10331 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa33f3f4-2850-3332-a9a3-2a2d783bcac1 | -4.55734 | -43.10797 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 321be65b-9587-3ce4-95c7-ca1afc2c3615 | -4.55656 | -43.11264 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f86da2d4-5529-39df-8331-065e150fdeda | -4.55578 | -43.11732 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a520405-6ede-33a1-b633-942e01506bc2 | -4.555 | -43.12199 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1675c3ba-6c7a-303d-845a-87e4134263fc | -4.55354 | -43.10252 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a95ed30a-3f1c-3495-90e3-40ababc397a0 | -4.55276 | -43.10719 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 720225b7-87a1-35c8-986b-4d3116dc5322 | -3.80548 | -42.5528 | 2024-11-02 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a4f2da-0077-3b45-a352-7df393092d0e | -3.54556 | -43.57209 | 2024-11-02 03:47:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b8f07ec5-4162-334d-b037-f7ee4a5ac24f | -3.53305 | -43.61844 | 2024-11-02 03:47:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11dca8a2-ee10-39bf-87a3-127e96003e7f | -3.52823 | -43.61763 | 2024-11-02 03:47:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a37e6e89-2f53-37c0-9fd1-37bb58f3c0fe | -4.6539 | -43.81763 | 2024-11-02 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af1aa738-6485-38e0-8c71-ea1bfa7364db | -4.60425 | -43.99393 | 2024-11-02 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5814715a-ff2c-3f39-80a8-ffe8b45cc94f | -4.59939 | -43.99313 | 2024-11-02 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a535372d-441b-3fd4-bbae-2086ccb2bc08 | -5.37037 | -36.81805 | 2024-11-02 03:47:00 | NPP-375D | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9e9c020-ae6f-3a8e-9480-33d093c56938 | -5.22989 | -35.68748 | 2024-11-02 03:47:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c6ee8928-10f2-35ff-840e-b6d2db45d6f0 | -10.73778 | -37.01982 | 2024-11-02 03:47:00 | NPP-375D | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8ea0b477-856f-3e19-b592-10bfdef3c482 | -8.021 | -38.44765 | 2024-11-02 03:47:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ecf9b4fe-ca5e-339d-b301-a4ae88e0c6a3 | -4.62677 | -39.67194 | 2024-11-02 03:47:00 | NPP-375D | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 761bec68-8f8b-3606-9bf6-f3508b1ea874 | -4.78804 | -40.06958 | 2024-11-02 03:47:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a176434d-624f-3412-864b-48fbfef3a2ef | -9.283 | -40.84453 | 2024-11-02 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 92005a73-7e3a-3bc4-9f67-371d66e69b73 | -8.85522 | -40.45125 | 2024-11-02 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8f54f841-495e-3cc7-bb4b-33a6e58c1e62 | -8.61077 | -40.50493 | 2024-11-02 03:47:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c3867412-d02b-32fe-a1ae-efd7d1dcad3f | -8.60716 | -40.50597 | 2024-11-02 03:47:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 77b89782-7bdd-364b-a93b-a4c6e77b861b | -8.61082 | -40.50656 | 2024-11-02 03:47:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c02aa1ec-1fbc-3ec2-abe9-3a32f24fe4e3 | -8.61004 | -40.50924 | 2024-11-02 03:47:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f1a3cc66-57a8-3949-9f5e-fe9226612d30 | -8.74267 | -40.58718 | 2024-11-02 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 78bb85b7-2db0-3046-a646-91d5ee447e26 | -8.73901 | -40.58658 | 2024-11-02 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 45a637e4-5327-3f54-9b94-e78dc27a5752 | -8.73531 | -40.56378 | 2024-11-02 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d75b4cf1-31cd-304b-8941-0f40fbab14d5 | -8.73459 | -40.56808 | 2024-11-02 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9133637c-12c9-3e87-80c2-98b432b70a13 | -8.20787 | -39.96043 | 2024-11-02 03:47:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 144911f2-1c41-36a1-b1c1-7093ec7b966b | -8.85885 | -40.45188 | 2024-11-02 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 06f8162e-c994-38a9-ab9f-a2463dd263f8 | -8.10557 | -39.77003 | 2024-11-02 03:47:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8aed45f3-aa9d-3dea-b62d-5adb377420af | -2.96954 | -40.32782 | 2024-11-02 03:47:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 084a4f31-148a-3d1c-845e-31447d250b3c | -2.96341 | -40.24209 | 2024-11-02 03:47:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 980673c9-18f3-3e03-956b-78bbcd85d4b8 | -2.89508 | -40.51406 | 2024-11-02 03:47:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 999d8553-3cd7-3283-98e0-13a8aa028db9 | -2.89113 | -40.51344 | 2024-11-02 03:47:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a556e59-d4ff-35bf-98e0-6ac0c3a3684e | -4.23456 | -40.40468 | 2024-11-02 03:47:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e9ba3d9b-c6af-33bd-80ef-9016b9f1d6e4 | -4.55198 | -43.11187 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54d36f33-1076-36d1-866c-8aed7fbbc2ad | -4.5512 | -43.11654 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e61ddc3a-b034-37cb-8fae-54f440f5e8a4 | -4.55042 | -43.12122 | 2024-11-02 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96ef5067-86f2-34a7-b706-1e84a40d1219 | -3.22702 | -44.41678 | 2024-11-02 03:47:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eee4edff-a9a0-3762-86f2-ffe3b4cecef8 | -3.22651 | -44.41984 | 2024-11-02 03:47:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60561495-81bd-31b3-9a98-42204feb48db | -3.22191 | -44.41588 | 2024-11-02 03:47:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2ff10e7-51f4-30ac-a0a5-9ad734bbcfef | -3.2214 | -44.41896 | 2024-11-02 03:47:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a600f2ea-1768-3f31-8946-71ae6a7426e0 | -3.52341 | -43.61684 | 2024-11-02 03:47:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28bed746-09ee-3f95-8fc6-c64916ce6fb4 | -4.45107 | -44.17142 | 2024-11-02 03:47:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3025d6a4-dd05-3196-a864-a3fd62f64bb2 | -4.44707 | -44.16518 | 2024-11-02 03:47:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3380f08-b658-33ea-80c9-dda204c7a4a3 | -4.44643 | -44.16416 | 2024-11-02 03:47:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bb4c60c-cf71-39a2-9d19-d182aab5923a | -4.44612 | -44.17067 | 2024-11-02 03:47:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README22.md)
