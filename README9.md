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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a84e4cd7-698f-38ca-a9ae-3c55c320f659 | -12.42277 | -58.47913 | 2026-06-12 05:33:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0e6be31-f39e-3194-94ae-8079ffb8afd7 | -12.54796 | -57.19342 | 2026-06-12 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1be9ea35-abef-36d8-9953-76fab3803a42 | -9.2095 | -47.92218 | 2026-06-12 05:33:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdc4f5c1-2e74-3d0f-b20c-8701c14ba7ec | -12.42955 | -58.48481 | 2026-06-12 05:33:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59d37d42-0e39-33dd-a08b-be9dd668e7c5 | -9.2205 | -48.58341 | 2026-06-12 05:33:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7ff0055-fcf1-37a3-8e1e-88aa6e657ae8 | -11.62261 | -55.17819 | 2026-06-12 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a6b4428-2e47-32b0-8aad-0b5215663a78 | -9.21031 | -47.91549 | 2026-06-12 05:33:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdfc2d91-357f-39f7-b16f-e1195c379582 | -12.30252 | -57.3989 | 2026-06-12 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7e942cc-da24-3a28-bdff-05a007906e06 | -11.04995 | -56.93654 | 2026-06-12 05:33:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a916702-b764-3174-bdb4-70f8048971ba | -9.31135 | -48.97041 | 2026-06-12 05:33:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c74d46d-17c3-3b10-866d-4c73d0f20d66 | -12.29707 | -57.39956 | 2026-06-12 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d222a28-d43d-3e0c-b847-5243de054532 | -12.55107 | -57.19439 | 2026-06-12 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5df71ce9-8ad7-3511-8992-395024596431 | -9.21376 | -48.58229 | 2026-06-12 05:33:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 70b99303-ed3c-39ae-8026-0aa04845c43c | -11.45243 | -55.90081 | 2026-06-12 05:33:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4f5ec29-11ea-34a5-8e52-ade6de89ed9a | -12.54705 | -57.19382 | 2026-06-12 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bff179d5-1f97-3ac0-927d-0a4a5d880584 | -12.29855 | -57.39838 | 2026-06-12 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7943f106-8b25-3545-8854-bdc84957dc10 | -16.12436 | -58.49819 | 2026-06-12 05:36:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 21a467fa-abc2-3a25-9242-5683b2a65d29 | -17.46293 | -55.20559 | 2026-06-12 05:53:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dcfe4c89-4ea7-3a24-90c0-ee092a136802 | -12.42887 | -58.483 | 2026-06-12 05:55:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc9d968a-ed15-322a-841a-ac1242c4abd3 | -12.4238 | -58.47839 | 2026-06-12 05:55:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 240fc248-6622-3a3d-9a89-f295557a8aec | -12.4178 | -58.48145 | 2026-06-12 05:55:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36f6e442-0835-3ff4-ab85-a2b524ce37ea | -12.42427 | -58.47454 | 2026-06-12 05:55:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9c5f607-c78b-3d9e-9287-30b276d3a0c9 | -12.54773 | -57.19302 | 2026-06-12 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2068ede7-79a7-3d93-8d2b-96567e6a5464 | -12.42333 | -58.48225 | 2026-06-12 05:55:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4193f2cf-79a1-312c-ba90-65e4c2a29c90 | -12.42933 | -58.47919 | 2026-06-12 05:55:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c141e379-e06b-3373-99ba-dc79dabe925f | -8.1667 | -47.5421 | 2026-06-12 06:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4a2b7b3f-d365-3117-a630-dddfa8cdb22c | -3.49753 | -48.03049 | 2026-06-12 06:54:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d06a487c-fda7-335b-995e-62b0c5f11bbd | -8.15952 | -47.52882 | 2026-06-12 06:54:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 5076e22f-8f1b-3e0e-9d69-dabab220ec92 | -10.90137 | -54.13313 | 2026-06-12 06:54:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c0752c7d-7561-3359-bd51-6d21c8e0735c | -9.20939 | -48.57735 | 2026-06-12 06:54:00 | AQUA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 567ade1a-8560-37d4-a1d8-a2f6bcb9cd3d | -12.72027 | -54.99981 | 2026-06-12 06:54:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5057e597-33ee-35d8-9bfe-d44a519ee0d3 | -11.61869 | -55.18357 | 2026-06-12 06:54:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cba36062-fb31-3376-a50a-7430860de0fa | -8.15718 | -47.54575 | 2026-06-12 06:54:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ef1985b1-8987-368e-bc20-e482f20181b8 | -11.62016 | -55.17422 | 2026-06-12 06:54:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a6cd111a-b51e-328c-9832-3f05a2da62cf | -18.5164 | -53.53669 | 2026-06-12 06:57:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 20657930-a544-3cf0-8db1-a2b5c24b0fb6 | -12.4274 | -58.484 | 2026-06-12 12:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 804450aa-7a3e-3865-9909-c457792b89f8 | -12.4277 | -58.4642 | 2026-06-12 12:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| a96c982c-ec36-397a-9f1f-5c9ab665e6cd | -7.6479 | -45.29 | 2026-06-12 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| fde39d70-a31b-38b2-8818-c9be0c2aa26f | -7.6479 | -45.29 | 2026-06-12 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 00be37d5-165c-368a-be88-e7ac1fdecfa8 | -12.4274 | -58.484 | 2026-06-12 12:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 29e21a23-24b2-3a1a-9981-7a8f4114ba0b | -12.4277 | -58.4642 | 2026-06-12 12:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 8a25379f-9d9d-3fd6-9565-fd2b432cf3d6 | -7.91144 | -47.05133 | 2026-06-12 12:29:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 627fe0d4-4bc7-3ebc-a31d-b8ffd307b7e3 | -7.90742 | -47.08655 | 2026-06-12 12:29:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 3d48e5e6-2816-37b0-a7de-fc0617d6a430 | -7.92774 | -47.05385 | 2026-06-12 12:29:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| c6c6c0d5-da7d-3959-8891-ccd9610c1779 | -7.91677 | -47.08149 | 2026-06-12 12:29:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 863f3507-bb96-34bd-b4e6-5e7d8c43fdf2 | -7.92108 | -47.04618 | 2026-06-12 12:29:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 9052fc56-9510-3d67-81bf-100ac0046656 | -12.4274 | -58.484 | 2026-06-12 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 290.7 |
| 33342e45-26da-321b-b143-a9716637b2d8 | -7.6476 | -45.3128 | 2026-06-12 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| f1db49c9-320a-302c-bd2c-7332794e9b8c | -7.6479 | -45.29 | 2026-06-12 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 3a0c2ad4-5d77-3405-8291-ceb02eb1ee4b | -12.4277 | -58.4642 | 2026-06-12 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 05de22d7-57c6-3dc4-8ab1-64c3d5c3cb31 | -12.43858 | -58.48173 | 2026-06-12 12:32:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16c4214d-1964-3d5e-b9b0-400f74d6fdbb | -9.41278 | -50.67106 | 2026-06-12 12:32:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| dc357491-2dc3-33ff-ae4c-f2e5276eb93b | -12.42211 | -58.46994 | 2026-06-12 12:32:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 9b20fcdd-5529-3975-bbce-9e43603272ce | -8.17515 | -47.54483 | 2026-06-12 12:32:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 84c2aa1f-fba8-3a6d-a9da-e5321c3bb241 | -12.54883 | -57.20334 | 2026-06-12 12:32:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 654a63e5-b94a-3abd-85bf-074ddc510879 | -9.40893 | -50.68431 | 2026-06-12 12:32:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6fb06ada-3d3d-368d-9d59-5b28f92865ce | -10.85123 | -46.7754 | 2026-06-12 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 1c8698cc-dd5f-3bff-9a06-badecf7e0bad | -10.09686 | -52.17973 | 2026-06-12 12:32:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 25741b1d-e745-3bf1-afc7-f7c195cb79f5 | -9.42301 | -50.69172 | 2026-06-12 12:32:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 01581ca4-1620-3f77-adad-e23beb4e21de | -11.45013 | -55.8984 | 2026-06-12 12:32:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 750c947b-8cc9-3c68-8a7b-0dc21fb59bf4 | -12.55011 | -57.19436 | 2026-06-12 12:32:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| d6047a7f-e065-3bd2-a164-335502fd0002 | -12.42967 | -58.4804 | 2026-06-12 12:32:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 7a55d8e5-ce1d-31cd-977d-d8647dd43909 | -11.60092 | -55.33538 | 2026-06-12 12:32:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 9a8f4888-cca4-30ef-bef0-44ff984c2f44 | -9.41047 | -50.69014 | 2026-06-12 12:32:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 329ae82e-8b10-34b7-b520-767269e359a2 | -9.42147 | -50.68587 | 2026-06-12 12:32:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ce0fa6a7-f508-3755-aec0-0fc2f6df1d7f | -10.8498 | -46.76841 | 2026-06-12 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| a11e6047-df3e-3535-aaf9-9c1f2db14ae5 | -8.49391 | -51.53838 | 2026-06-12 12:32:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 84b4955e-0fc3-34ea-a914-b12b0f1589e6 | -8.48538 | -51.53078 | 2026-06-12 12:32:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2ad2412f-5865-3a3e-b51e-4503b759e92e | -10.60351 | -53.46805 | 2026-06-12 12:32:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 994d0d2b-15f1-345d-b57b-53ca26e78288 | -9.47355 | -57.16668 | 2026-06-12 12:32:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b93a78b-cf73-3721-af69-9dd2da13138e | -10.57591 | -57.32656 | 2026-06-12 12:32:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7de044ec-c846-39c8-91f0-93de745f4913 | -12.30014 | -57.402 | 2026-06-12 12:32:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 62913a09-b208-30bb-8c41-0867992aa69a | -12.42076 | -58.47909 | 2026-06-12 12:32:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 7bb49a9b-d43e-3bd3-a2fc-488f531b7558 | -12.43102 | -58.47126 | 2026-06-12 12:32:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 78bfa58f-fdb7-3c2d-8690-4f322f750546 | -12.4277 | -58.4642 | 2026-06-12 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 317.1 |
| 4624b852-9fc3-369c-b5ec-5a723d1420ba | -12.4274 | -58.484 | 2026-06-12 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 306.3 |
| 57eed88f-e898-323b-839c-d4b439216b28 | -7.6479 | -45.29 | 2026-06-12 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 75cd29cc-7fda-3be5-a0d8-a9921149b32c | -8.1667 | -47.5421 | 2026-06-12 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| db3e65c8-aaca-3f65-b8c6-43389552103b | -12.4274 | -58.484 | 2026-06-12 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 345.9 |
| 139cb308-672c-3396-8ace-0c0c53b35f8c | -7.6479 | -45.29 | 2026-06-12 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 8c992e1d-7d46-3dc6-b3a2-9ca389594a5a | -7.629 | -45.2918 | 2026-06-12 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6595cd6d-a50a-321d-8d89-660e9f7ae8d8 | -12.4085 | -58.4855 | 2026-06-12 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 8fb39581-4c82-3bca-81d4-a6de1918e68b | -12.4277 | -58.4642 | 2026-06-12 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 290.5 |
| baebd5f7-1c07-3695-9de5-42800e889e49 | -8.1667 | -47.5421 | 2026-06-12 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 7908b4d8-fe86-3dcd-ba6a-6e1084bfad86 | -7.6479 | -45.29 | 2026-06-12 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 2c09d176-a538-3fa4-9c59-594bb4713fed | -12.4277 | -58.4642 | 2026-06-12 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 361.8 |
| 333d484e-339d-3a16-8558-451f17fdd35f | -12.4274 | -58.484 | 2026-06-12 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 376.5 |
| 0ba7deff-b3fa-3131-951d-cb2948da5800 | -7.629 | -45.2918 | 2026-06-12 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 18eeafe1-36ca-3541-9525-eab2694b1c6f | -7.6476 | -45.3128 | 2026-06-12 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 8d2b81f0-c0bf-393c-b64d-1b8ed2c2d917 | -12.4085 | -58.4855 | 2026-06-12 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 42db8022-f400-3675-b123-b320977d73d2 | -12.4274 | -58.484 | 2026-06-12 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 357.9 |
| ae2d9362-4a0b-35ea-9705-3d5d73586b2a | -12.4085 | -58.4855 | 2026-06-12 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 89d1751e-7713-37a1-a4e2-32ff21fd15ab | -12.4277 | -58.4642 | 2026-06-12 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 387.2 |
| 6d80fa5a-4c9e-3f77-b122-7b6381109dad | -7.6479 | -45.29 | 2026-06-12 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 3e8df076-dd0e-3a7c-849c-961c5b4664cb | -7.629 | -45.2918 | 2026-06-12 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| bf43d43f-337f-38d3-8999-039ea84fab88 | -12.4277 | -58.4642 | 2026-06-12 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 430.5 |
| 8eec4d40-aea7-34ad-9fc9-75c55ddc73b2 | -12.4274 | -58.484 | 2026-06-12 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 313.7 |
| 57cb1005-5a59-3170-9393-6bb508acb74d | -12.4085 | -58.4855 | 2026-06-12 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 35479348-905b-3192-ad2b-9f6663215457 | -12.4274 | -58.484 | 2026-06-12 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 343.3 |
| 54283884-97d9-37f9-b457-b543e5e6098d | -12.4085 | -58.4855 | 2026-06-12 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |


[Clique aqui para ver as próximas entradas](README10.md)
