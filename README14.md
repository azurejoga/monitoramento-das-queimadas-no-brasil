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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be2c5faf-5698-3d6e-85c6-22234e3535ad | -6.12157 | -41.7123 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b163bf29-e06d-3390-99cc-3f89904b1528 | -6.03252 | -40.45538 | 2025-10-28 04:12:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 29eee874-66d4-3e9b-a706-25f7292379b5 | -6.16158 | -41.6747 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17f057d2-d49e-3bfd-9dfd-1fdd935e580f | -4.47877 | -43.43073 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2434fe70-02ca-3fe7-b057-ac979a6147cf | -4.8554 | -46.73907 | 2025-10-28 04:12:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3f28f0a-cccb-3cc6-93ea-5828aa9f58e2 | -1.67163 | -51.99905 | 2025-10-28 04:12:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd5a7fe8-6ec2-38a8-b0af-7b9d9f339a30 | -5.14257 | -44.95998 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45e86c8c-c436-3428-8b28-7d05126b08a6 | 1.04271 | -51.3098 | 2025-10-28 04:12:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17d6c75b-fc80-38c4-ab33-520a19ccc746 | -1.49896 | -53.12786 | 2025-10-28 04:12:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dcd10d8b-012a-3e4d-bd10-1cc8698c018f | -6.06557 | -42.14204 | 2025-10-28 04:12:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f8023ee0-c4bb-3d54-8281-d6ea2552416b | -2.58226 | -48.4038 | 2025-10-28 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c3159aa-dec3-3f23-bea6-46a2639c8ca5 | -3.76812 | -42.80077 | 2025-10-28 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e157ccaa-60f4-3343-a9c2-339be0468130 | -6.10072 | -41.78129 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cfd50a12-c1c7-3f36-b8c6-73cb96a018fb | -4.48209 | -43.43124 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67a47e27-e354-3625-b1d6-84bf3b1b9d47 | -6.17558 | -41.69497 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dea0c50d-b9c6-3b5d-889b-620011a0565e | -3.44761 | -41.84571 | 2025-10-28 04:12:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 56a2175f-d79c-3b2d-aeb9-5f539e37c4e4 | -4.85933 | -45.77916 | 2025-10-28 04:12:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dadf65c9-69a1-39c3-8208-4b400f26ef1b | -6.10947 | -41.74659 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6bf2eb78-3294-3029-97a6-922e4bc0f749 | -6.19638 | -41.51561 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aa61e966-acee-35b6-a40d-63a3c2bb05c9 | -3.56957 | -49.0236 | 2025-10-28 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6e6ef89-00a3-394b-be76-4fc821239825 | -4.63487 | -48.69804 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d43d9a2e-bc64-3f87-b3c4-64b898ed5651 | -4.99416 | -42.55757 | 2025-10-28 04:12:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 648042b0-09d6-375d-b345-477babad1585 | -2.75392 | -47.74972 | 2025-10-28 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5853d274-ccf2-32e5-92d1-18226d2ee689 | -5.71613 | -44.53437 | 2025-10-28 04:12:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae68fd5a-9bbf-344e-a179-fcab535d3e0c | -1.4881 | -49.08206 | 2025-10-28 04:12:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04c86724-93f9-3bc1-81e6-956f2ae7cf99 | -4.97529 | -47.81277 | 2025-10-28 04:12:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da3beb7f-3f8e-3b4c-a772-b2d35657315c | -4.01996 | -42.90716 | 2025-10-28 04:12:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 936aaa71-5b38-3be7-aad2-fd8cdf880a14 | -4.37194 | -49.67249 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c1194c9-856b-302c-a889-69f3fcc9b3fb | -3.05251 | -53.01785 | 2025-10-28 04:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73c25787-ce38-30e4-b470-6da63cac88a3 | -1.70087 | -53.69505 | 2025-10-28 04:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd6ff5d8-fbf0-34bf-bb60-3b6d33fd4228 | -3.60441 | -43.55865 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43b516c6-f67c-3645-adc0-83a51f957c93 | -5.41969 | -46.00105 | 2025-10-28 04:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77956977-d944-30f0-843e-c8c72edf5858 | -4.46774 | -43.50061 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f43c14d0-45af-397f-bab8-34f1ccd3fef1 | -1.84107 | -45.29704 | 2025-10-28 04:12:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b431c2b-5309-38a9-9e7c-12f160399788 | -3.44903 | -42.51037 | 2025-10-28 04:12:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 092baea4-c7e3-3ec5-a654-e5e041fd4686 | -4.51005 | -42.84031 | 2025-10-28 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36c721ae-bc44-3c1c-b745-87105c3639b2 | -5.66239 | -41.1135 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a7adee33-38f2-3d9d-b717-1c1f4c0b1318 | -6.16104 | -41.67822 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c7b5fc5-fcc6-311c-b3e6-cb0e33276c6c | -4.22703 | -43.19131 | 2025-10-28 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4205636-6a91-3f8d-985c-37c904690ae5 | -4.55566 | -43.41776 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c017e548-3e70-32dd-a5c4-547845fa730e | 0.98211 | -51.12537 | 2025-10-28 04:12:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e524981d-0bb5-3cfc-8dfb-1708988994f8 | -3.97088 | -44.31026 | 2025-10-28 04:12:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4b7b3ce-8a4d-3a3a-be36-9ee8c40fbf70 | -4.97936 | -47.8133 | 2025-10-28 04:12:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa8503b4-406b-32f2-b18f-348067126694 | -5.79486 | -35.60459 | 2025-10-28 04:12:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 17044827-7911-3a86-b879-b0deaa0de622 | -5.20122 | -46.1486 | 2025-10-28 04:12:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97d5df26-1d5d-3830-9978-10ec4fa9060c | -2.99361 | -51.03865 | 2025-10-28 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db1abb7d-fc40-3f18-b3f1-1f35c9ecfebf | -3.95342 | -43.2869 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 251adb74-b101-3c68-8551-bffd6322f57d | -5.04726 | -45.13327 | 2025-10-28 04:12:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a661625-3d2e-3941-a709-e5e2dd329525 | -6.16461 | -41.5658 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 30b01f2b-8a2c-32c1-9911-999ab063947e | -5.79558 | -35.5997 | 2025-10-28 04:12:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 07b1e4dd-8180-3fcd-93f4-328adf94cecd | -5.27163 | -44.61155 | 2025-10-28 04:12:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a43060e-f86b-3f67-bd9e-03429a5938a3 | -6.12935 | -41.7062 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 436cbfde-9aea-3066-b57d-393dcdee78da | -6.14546 | -41.69047 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c48955be-9aef-3681-8af7-58ce5ecb0f80 | -6.02963 | -40.45098 | 2025-10-28 04:12:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9d1a6127-ace3-35a9-8023-3a032ecb3db1 | -3.47179 | -49.97286 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c81d427-e667-36e5-bdce-169f1be7e5ec | -3.58657 | -43.62838 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b2d50d5c-393b-301f-8193-1728c629e723 | -2.76676 | -48.57508 | 2025-10-28 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1d6af1c-6c8e-35ac-99c0-a602629a522c | -2.75524 | -45.39637 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b8d7e9be-bbc8-3634-9c94-09767a7fbc50 | -5.65741 | -41.1462 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 99fa0a45-6684-32ab-94ba-cd987bb3661f | -6.11497 | -41.73302 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7db44e27-1129-333b-9d0e-88e088e08549 | -4.62948 | -47.41863 | 2025-10-28 04:12:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5233a7bf-a224-3ad4-a613-0dba394a2481 | -4.43227 | -43.44495 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 643a65b5-704b-3231-b288-8901a19cff25 | -3.05178 | -53.02208 | 2025-10-28 04:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79d2ead8-b9b9-32f9-ac1f-c1c94b982bf0 | -3.70819 | -47.64134 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d055a938-ae4d-3fc0-8cc0-4eca3e2054e0 | -4.01185 | -43.19626 | 2025-10-28 04:12:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f7e4767-dc11-3a39-9db1-3e9968963d5a | -5.66128 | -41.12078 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 54d05b1a-894f-3f42-8571-bcadd5ff5895 | -5.59542 | -45.04541 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6435dcb7-1eef-3b2e-a795-e838f7142063 | -6.16882 | -41.67217 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1db3d35b-0881-3ed3-ba7c-f3a96666dc39 | -3.20135 | -41.43906 | 2025-10-28 04:12:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0592738e-2ae7-332a-bb2b-1073dab6d006 | -4.85615 | -46.73439 | 2025-10-28 04:12:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 045c0cc7-f9a4-3aa2-a750-f4164f8664c3 | -4.20127 | -43.01021 | 2025-10-28 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0d685ac-72f0-33b2-ac26-1c743527c0e8 | -4.21768 | -48.35402 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f16758b-edf9-3f4a-a839-9a08ecf05098 | -4.8111 | -43.30884 | 2025-10-28 04:12:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14c0ba2c-0e78-329d-baf4-1088736c7ae0 | -3.57631 | -49.4383 | 2025-10-28 04:12:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 900965f4-89a6-3ca2-b931-c35bc8d69d2b | -3.5821 | -43.63499 | 2025-10-28 04:12:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f6d6a48d-e1de-3b5a-9a05-cdaea4981af1 | -3.53264 | -50.31255 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a6a8d122-e080-3a3a-95d3-7c8a30fc42b7 | -6.29337 | -40.86031 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 322c5a8d-3a22-367a-b8b3-48cc57331e82 | -4.96398 | -48.25665 | 2025-10-28 04:12:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e15c920e-e496-3afe-9148-660208fe4fa2 | -3.44046 | -41.84813 | 2025-10-28 04:12:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8b82bcc9-6eef-3c49-a6f9-86f64ea175e0 | -4.45169 | -43.64548 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0bc247c-a02a-3c13-8390-125f5d128e3b | -6.1714 | -41.58864 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6d8f5fee-a217-383a-8141-68d8dab7fe48 | -6.15853 | -41.58305 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d96c8e92-060f-327e-8e85-9f74380ff997 | -5.9736 | -42.73342 | 2025-10-28 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a8171fb-5270-338e-888a-c780d97e7f1f | -3.43984 | -50.22086 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b27141f-9377-3725-822f-a1357078efd7 | -5.42326 | -44.80598 | 2025-10-28 04:12:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0deb7f4-7c19-39e1-b1ce-580a66c7aaa7 | -5.9693 | -42.76096 | 2025-10-28 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 921de8ca-e3e0-3735-b0b7-cbed11125761 | -3.00552 | -41.69213 | 2025-10-28 04:12:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5642e97b-230b-3ab5-a42d-ee53c8914fb5 | -3.57764 | -43.61976 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8a9382f-de7b-3ad9-9326-c3cafe979a42 | -5.26638 | -44.3186 | 2025-10-28 04:12:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a884e07b-780f-365b-a5ca-883b6f8f6f29 | -4.74241 | -48.30759 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89f8aef6-ca3d-3a0d-8c0f-ec1de0be6411 | -5.20487 | -46.14917 | 2025-10-28 04:12:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68a45131-5e3f-3da8-8d3e-76b7d7f3a590 | -3.0223 | -45.37551 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 83a7a0c0-0c47-3446-b64f-da0076d1ac5c | -4.72956 | -43.20014 | 2025-10-28 04:12:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 256b248a-cec9-3258-9dc5-3ea96954e67f | -4.92817 | -48.54761 | 2025-10-28 04:12:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c28ea0b5-c1a1-3e0d-89c2-94c130c9f11b | -3.57987 | -43.62737 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc3e90a8-cb20-3cda-8622-9245ec30aae9 | -5.78613 | -42.97138 | 2025-10-28 04:12:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d19fe9e-b32d-3e1e-b9a6-aa083bd1110c | -4.17812 | -48.19781 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 997afeb7-e48e-388b-a277-e609d6c57be3 | -3.58378 | -43.62434 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 460349a2-b499-3bc1-9aa8-a4c011117f2e | -2.75746 | -47.75426 | 2025-10-28 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1448b215-a0be-36d3-aa98-50e8395b8be7 | -4.57246 | -46.49255 | 2025-10-28 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
