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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22a1af53-978a-3695-8227-953131361d04 | -6.9161 | -43.4952 | 2024-12-11 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 199.3 |
| d16c8751-0fc2-3d35-8a50-57654d99696a | -6.1178 | -42.5559 | 2024-12-11 07:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| a5574bb0-818e-3043-a5dd-593de66193c2 | -6.1366 | -42.5544 | 2024-12-11 07:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 73e6bb27-2cb2-3e64-9b31-5307056c9761 | -6.9592 | -42.9994 | 2024-12-11 07:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| 7a5910be-b364-3c88-9b9f-ee385c17421d | -6.9158 | -43.5185 | 2024-12-11 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 178.4 |
| aa481182-81c6-3603-8e27-d87097af0ad7 | -6.978 | -42.9977 | 2024-12-11 07:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.1 |
| 5a994ffe-4be6-3a23-b2ee-56d0eac60319 | -6.118 | -42.5323 | 2024-12-11 07:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 116.9 |
| 1d3d5af2-5462-369d-ac8d-b52f50d86248 | -6.9 | -43.51 | 2024-12-11 07:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 47f85f1c-8de0-305c-b5e8-758861de599c | 2.75211 | -60.61624 | 2024-12-11 07:05:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 23.3 |
| c7acb59c-324e-3810-81ec-032c68f14ea4 | 2.75878 | -60.62 | 2024-12-11 07:05:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 2d048ce5-b2c4-34c7-84e9-54f12188d0f2 | -6.1368 | -42.5307 | 2024-12-11 07:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 5fc5c842-b78b-388c-a854-8ef6356742dd | -6.9161 | -43.4952 | 2024-12-11 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 207.9 |
| 243a0ef6-dcef-3a4a-be80-219723548fbb | -6.978 | -42.9977 | 2024-12-11 07:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 147.1 |
| 9de10c48-8be5-398f-9b53-31b1cfad1b52 | -6.118 | -42.5323 | 2024-12-11 07:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| 9103432c-5104-341f-a2fc-d14f5f37af72 | -6.9592 | -42.9994 | 2024-12-11 07:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.6 |
| 7af498ba-6485-3cd7-9199-96d25f3cccb1 | -6.1178 | -42.5559 | 2024-12-11 07:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 15c53f90-786c-3226-a471-a5ccc63d0504 | -6.9158 | -43.5185 | 2024-12-11 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 162.3 |
| be51f285-7114-3883-8b75-4c8e03d0c747 | -6.9594 | -42.9759 | 2024-12-11 07:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| d2532d8a-d473-3ae9-a8da-8a9ab4976acf | -6.9349 | -43.4934 | 2024-12-11 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 81998335-8fb3-31c2-8596-f91fe0441e00 | -6.9158 | -43.5185 | 2024-12-11 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 845b5138-5388-3bd7-9c27-86d13b5aa1f9 | -6.118 | -42.5323 | 2024-12-11 07:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 9937e549-f0ae-3069-ad47-3c611bf4eefe | -6.9161 | -43.4952 | 2024-12-11 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 67711de9-dcf3-3d4b-a331-4a6b643eea44 | -6.1368 | -42.5307 | 2024-12-11 07:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 5916c4b2-9672-34fb-9775-a8017309bad3 | -6.978 | -42.9977 | 2024-12-11 07:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 09339745-fb1a-3f1a-937a-c28b1d623899 | -6.9592 | -42.9994 | 2024-12-11 07:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.3 |
| eb9d44d1-9b7a-3e61-ab45-302c692e65e9 | -6.1366 | -42.5544 | 2024-12-11 07:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 7e8b35c8-8fea-343d-a3dd-8cc795bf9675 | -6.8972 | -43.4969 | 2024-12-11 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 84cd4b9e-47a3-3932-aa56-3c3599ae8c6f | -6.8972 | -43.4969 | 2024-12-11 07:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| efa4e89b-0dea-3674-a3c4-74606b0a675b | -6.978 | -42.9977 | 2024-12-11 07:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 120.5 |
| 0d7016ca-cd54-3c6a-b2d9-77e0c0e4cc1c | -6.9158 | -43.5185 | 2024-12-11 07:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 3cce4bbc-a914-311c-b0fc-3b18403c4eb9 | -6.9349 | -43.4934 | 2024-12-11 07:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 6e3f1336-ea89-379e-837d-a5364aba8e1d | -6.1368 | -42.5307 | 2024-12-11 07:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| c143a2bb-9125-3480-922a-252b4abe1cd7 | -6.118 | -42.5323 | 2024-12-11 07:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 7aa9cd87-9f08-33c2-acda-40ea147f38d3 | -6.9161 | -43.4952 | 2024-12-11 07:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 149.2 |
| ac750b87-bc77-3938-b024-6fc540f89eee | -6.1366 | -42.5544 | 2024-12-11 07:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 2b0decd2-a5bf-3625-b9fd-aed849bb42f3 | -6.9592 | -42.9994 | 2024-12-11 07:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.3 |
| 528249c0-3b1e-39b7-aa4a-9f88286e144f | -6.897 | -43.5202 | 2024-12-11 07:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 4ec1e9ed-87d7-3f72-a51f-6acd2452422c | -6.9592 | -42.9994 | 2024-12-11 07:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| a3df7d82-adc5-3c9d-b24a-9359a43ab276 | -6.1178 | -42.5559 | 2024-12-11 07:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 80bd10cb-a89c-335f-9c58-e4381a865529 | -6.978 | -42.9977 | 2024-12-11 07:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.6 |
| 5ac474ba-dd6b-342d-b0e1-0c5f22105108 | -6.9161 | -43.4952 | 2024-12-11 07:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 99ffb90d-5bd4-34b3-b9b2-6e23c880bbc0 | -6.1368 | -42.5307 | 2024-12-11 07:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 0940676f-4c12-3e86-bd56-00130d09bd15 | -6.9158 | -43.5185 | 2024-12-11 07:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 6a3a24e5-767f-38ec-abab-a2b1d60ca93e | -6.9783 | -42.9741 | 2024-12-11 07:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 81da7120-ea3e-3cb5-8a77-51335263d07e | -6.118 | -42.5323 | 2024-12-11 07:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| d8a91cc9-16b4-3405-ba3e-0dfc12f1c80b | -6.1366 | -42.5544 | 2024-12-11 07:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| e1f52f14-c5ee-3114-a6e4-b1f9b5d9bc7e | -6.9158 | -43.5185 | 2024-12-11 07:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 166512b9-6f52-326b-a4dc-d78c0c9d51ed | -6.1368 | -42.5307 | 2024-12-11 07:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| c2436f76-40e0-3df5-a08b-89c7e620f2a9 | -6.118 | -42.5323 | 2024-12-11 11:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 3cdc1c1f-d3f0-3add-9496-ea3ea8481fd2 | -6.118 | -42.5323 | 2024-12-11 12:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| a789cec3-0a99-3131-90ec-c2843d4ca04a | -6.118 | -42.5323 | 2024-12-11 12:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 7154bbc0-66b4-3910-b99f-c5a714f22d60 | -6.118 | -42.5323 | 2024-12-11 12:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 6e871eff-42b3-3548-bb5b-fbb11b526876 | -6.978 | -42.9977 | 2024-12-11 12:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 1f9215b6-0ff9-3fd0-8fca-1136265b18b2 | -3.14307 | -48.59623 | 2024-12-11 12:59:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2df1d2ca-41c7-3c77-b389-734fc52c162c | -3.0058 | -48.04155 | 2024-12-11 12:59:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 14ff5ec1-50b2-3570-8976-b747a277ccf9 | -3.42541 | -49.1356 | 2024-12-11 12:59:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 28cff91d-d3ff-3517-ba77-9ed46bf5c740 | -10.02509 | -53.74836 | 2024-12-11 13:01:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f40568db-4176-39b2-932c-a4b8cbf40ca8 | -8.68304 | -50.08941 | 2024-12-11 13:01:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7494dedd-fd5a-38ed-ab26-0117bc2162e1 | -13.24222 | -44.98778 | 2024-12-11 13:01:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| eec8e302-8508-39d3-9e68-da73219a1314 | -8.7391 | -50.37999 | 2024-12-11 13:01:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7f202364-549b-384a-980d-c54a2a86a2a6 | -10.50858 | -44.94413 | 2024-12-11 13:01:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 70669f46-9f36-30fa-a831-4b0176f6bb82 | -7.12097 | -50.23788 | 2024-12-11 13:01:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 168c1095-1023-312d-a78b-6301a2a66a09 | -10.59403 | -44.98947 | 2024-12-11 13:01:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 88ea160d-97dd-3b92-9522-1593f460e40f | -11.06651 | -45.35218 | 2024-12-11 13:01:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 441307f2-6782-3581-b711-19ab74725eb6 | -11.20434 | -53.82738 | 2024-12-11 13:01:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 16f9dd51-900a-38a8-bc8f-29196b8e473a | -12.59417 | -43.79337 | 2024-12-11 13:01:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 610dc3c9-f580-3dc8-9d05-70cc81287c4b | -11.15259 | -55.65451 | 2024-12-11 13:01:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1a44382b-a187-3e0e-bece-13271e6905d3 | -6.13436 | -42.53323 | 2024-12-11 13:01:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 129.6 |
| 0d279d28-620b-3a8c-bdc3-b99434d688db | -11.21187 | -53.83765 | 2024-12-11 13:01:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 8a1cdaa3-54d1-369b-bcbf-e8b3faa88b98 | -10.51213 | -44.91007 | 2024-12-11 13:01:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| f4df71cc-209e-3cf4-83bc-8384c9e43b7c | -10.50869 | -44.9388 | 2024-12-11 13:01:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 578ec4f3-5d01-38ff-9d4d-228d6b1708e1 | -5.29165 | -47.11776 | 2024-12-11 13:01:00 | TERRA_M-T | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 87fcd493-5c77-3947-8d2f-bbeedd8d44d5 | -6.98252 | -42.99002 | 2024-12-11 13:01:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| f3bbc1b7-29c5-3fc7-b035-c3ae26aa5746 | -11.00978 | -55.07644 | 2024-12-11 13:01:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| da1fde3c-e917-3606-8754-81f0b73be787 | -11.20565 | -53.81842 | 2024-12-11 13:01:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 919496f2-cd22-3dbb-9d91-180ef0c79cad | -11.04884 | -45.37752 | 2024-12-11 13:01:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| df98fc5a-9b54-339b-8b6f-9b2545f5819e | -11.21318 | -53.82867 | 2024-12-11 13:01:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a9c8ff4a-082b-321e-834e-d8e13d0e365e | -10.51179 | -44.9155 | 2024-12-11 13:01:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 210f8fbd-f464-37fb-8688-1822566d2bf6 | -11.6833 | -46.41699 | 2024-12-11 13:01:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| c790d9a1-3ebf-3a10-a012-bc2b7607234d | -12.54864 | -44.27234 | 2024-12-11 13:01:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ec640ec0-99cf-35aa-8492-e7f0874df159 | -11.01245 | -55.11271 | 2024-12-11 13:01:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d9ca4e1d-075e-3513-8455-d63295ec36a9 | -12.06181 | -45.25346 | 2024-12-11 13:01:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| cb350c88-f3b8-3954-b68f-bb143bfef006 | -12.58251 | -43.79928 | 2024-12-11 13:01:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| bf236cfe-670b-397b-a5e8-d40fed325074 | -8.05736 | -48.47093 | 2024-12-11 13:01:00 | TERRA_M-T | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3b91fe71-f48a-3c66-8d56-89d3f968cfaa | -8.37106 | -43.36327 | 2024-12-11 13:01:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.1 |
| c1d89240-28b6-31d6-b73e-f1788a800ef9 | -6.95125 | -42.84174 | 2024-12-11 13:01:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 8dafa47b-7ed0-3586-8a10-b26a2a605921 | -10.89098 | -52.86535 | 2024-12-11 13:01:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d8e1d42b-5e09-3de9-843c-83eb6961be90 | -11.77979 | -54.23532 | 2024-12-11 13:01:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 51a911a9-b5b5-34ec-a774-17f1a1a1206a | -6.97296 | -42.994 | 2024-12-11 13:01:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 153.5 |
| 525b8004-682b-383a-b8d8-b4581d8d7ed6 | -11.67607 | -54.25102 | 2024-12-11 13:01:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 252b61e7-59d7-35e7-a466-0be5acc66cf3 | -8.54376 | -50.35656 | 2024-12-11 13:01:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 46d79260-aabe-3a92-b2e3-4190b961d9de | -8.36211 | -43.36762 | 2024-12-11 13:01:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 8096f073-1813-395a-be58-cc8d811d833e | -10.09171 | -47.37256 | 2024-12-11 13:01:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 2717fc60-1f92-30b9-90bd-096d988e3511 | -10.59459 | -44.98278 | 2024-12-11 13:01:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 9242463a-294d-3733-adc9-6494ab43533d | -6.95659 | -42.99169 | 2024-12-11 13:01:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.8 |
| 5c3c8943-5620-3169-ab55-500babde2dae | -12.54054 | -44.26438 | 2024-12-11 13:01:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 12dfc708-7194-346f-a02e-5c7847644335 | -11.95399 | -47.84159 | 2024-12-11 13:01:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 21b2efdb-6acf-3e08-b242-3100cfb7509c | -10.34871 | -52.85112 | 2024-12-11 13:01:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 689ca89f-5ebd-3890-b6c0-a347e2c5cb4e | -6.96614 | -42.98787 | 2024-12-11 13:01:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| 95a0d2a2-e713-3de6-92ca-4c3b7a078dc7 | -10.88255 | -54.31635 | 2024-12-11 13:01:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |


[Clique aqui para ver as próximas entradas](README31.md)
