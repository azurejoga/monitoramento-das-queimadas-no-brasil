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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6657cb95-ebb4-3940-b714-a090046bbd07 | -7.5292 | -61.3254 | 2025-08-15 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 095906b0-6c86-3e4a-9705-7e409fda64c5 | -7.5291 | -61.3444 | 2025-08-15 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 89de5450-2324-3740-91eb-c7cab530d260 | -13.1267 | -57.1293 | 2025-08-15 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 85ff2d37-b9af-36fc-952c-b2268f669174 | -7.4085 | -44.8571 | 2025-08-15 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 450.5 |
| f7c7809b-9e18-3697-82c8-b813c38b642e | -9.4994 | -60.5278 | 2025-08-15 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 4388e22e-ac43-39ad-a7df-fa5b764bf384 | -16.3741 | -50.9089 | 2025-08-15 14:30:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 242.3 |
| 31eb2e47-d9a1-321d-92af-308c73f0074e | -9.518 | -60.5268 | 2025-08-15 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 22ca9122-377c-388c-87f9-4932fd479dc7 | -7.2931 | -60.6287 | 2025-08-15 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| cc5808b9-4471-3ec8-beea-5902b96106e5 | -8.6695 | -62.4389 | 2025-08-15 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| b212e021-6c09-3b01-ac15-750acff65942 | -13.1262 | -57.1695 | 2025-08-15 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 27332d77-f172-313f-8a7b-9f59480b5d1e | -12.575 | -46.9555 | 2025-08-15 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 80d2f280-fd28-3e21-97e8-3f27b01b5e6f | -13.3392 | -45.2377 | 2025-08-15 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 273.1 |
| 53bcfb44-4baa-3698-abea-cb03b4776eb1 | -12.5938 | -46.9753 | 2025-08-15 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 339.1 |
| ae26c181-e648-3a24-ba10-195448a222c9 | -13.3198 | -45.2409 | 2025-08-15 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 220.1 |
| f08663ff-68b3-3d4e-a080-15475b4fae8e | -7.3896 | -44.8589 | 2025-08-15 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 20da28fc-eccf-3064-be5b-5ab49e891e48 | -12.4973 | -47.0118 | 2025-08-15 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| d4ddac63-0157-32fa-ba3d-3398fda6abad | -8.5504 | -63.9162 | 2025-08-15 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 14f8587c-e921-39bc-90e7-d3218873b941 | -8.6694 | -62.4579 | 2025-08-15 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.6 |
| fd80e1ba-7178-34d8-b080-a1758643a305 | -14.5631 | -52.0557 | 2025-08-15 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 9fb098e6-9abd-3b6d-974d-7bfc54222b02 | -9.8915 | -60.4297 | 2025-08-15 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 5a1594a5-7d47-397b-ad73-6667222c89e8 | -13.1077 | -57.131 | 2025-08-15 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 1ec7ad42-3dda-3d03-b74d-031ce1dbad66 | -10.0514 | -59.1208 | 2025-08-15 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 218d2dec-1020-3389-8bfe-552fa6c58a06 | -13.1074 | -57.1511 | 2025-08-15 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 3e358f7e-420c-317d-ad79-fcf1196c392b | -6.0463 | -44.1253 | 2025-08-15 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 48b0473b-64f7-3e9b-bea3-8210543a8fbe | -13.4757 | -56.6739 | 2025-08-15 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 08a7116e-0dc4-32f6-9412-4afc48cace3b | -13.3397 | -45.2145 | 2025-08-15 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 529.3 |
| d9d8115c-ddc6-33b1-965c-abc5c35fd122 | -13.4759 | -56.6537 | 2025-08-15 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| ad990c50-d81f-37b6-bb60-e25b527cabe6 | -13.1453 | -57.1678 | 2025-08-15 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| aa91cef9-8023-30af-908f-a9489e6c80ec | -12.6461 | -45.1879 | 2025-08-15 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 311.8 |
| c887c61b-5f34-3a9c-bad1-fd80b05912e4 | -14.5634 | -52.0344 | 2025-08-15 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| f8367d1e-261a-3f15-851f-a58281b9c622 | -12.5947 | -46.9301 | 2025-08-15 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 27412977-9572-32ec-a8bf-66ced9c57b78 | -7.9148 | -61.7478 | 2025-08-15 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 277.3 |
| 0dc9699e-4213-3882-bbc9-c7c5c64292b4 | -8.6695 | -62.4389 | 2025-08-15 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 1ed43132-331e-3ea9-bd31-08e713cd4088 | -12.575 | -46.9555 | 2025-08-15 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7cdb829c-d8b8-3e72-a66d-9d8926f2024a | -7.4085 | -44.8571 | 2025-08-15 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 447.1 |
| 0f95cb4d-7d09-3a6e-9717-9b39459ec939 | -13.4757 | -56.6739 | 2025-08-15 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 143.6 |
| b4ca8efa-43a6-348f-8980-cd2efdca7ede | -7.4258 | -60.0292 | 2025-08-15 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 0b480b66-956c-3a92-85d5-d1b10d1f3d00 | -14.5631 | -52.0557 | 2025-08-15 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| d878d0be-b76c-3179-8de6-e41a391557d5 | -12.5938 | -46.9753 | 2025-08-15 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 301.7 |
| 5d63d11a-1a02-360f-8764-f2a28ca14128 | -6.8673 | -42.7961 | 2025-08-15 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 243.8 |
| 689eba82-578b-3e48-a0d0-598cabdd999c | -12.4973 | -47.0118 | 2025-08-15 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 82bef97c-c071-37d4-996b-5485331df722 | -13.3392 | -45.2377 | 2025-08-15 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 8f8bed6c-f568-324e-b010-b04e24a6004d | -8.6694 | -62.4579 | 2025-08-15 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 121.7 |
| ef6bec26-8289-3e55-99cf-ac3d25f828ed | -12.5947 | -46.9301 | 2025-08-15 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 128c47bd-736a-3d19-b9d9-3aa658236d5f | -6.0463 | -44.1253 | 2025-08-15 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 3d719210-c8b2-32dc-9594-41947139ff88 | -7.9333 | -61.7471 | 2025-08-15 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 129.4 |
| d66f74dd-0841-3de8-bc1b-bfd7e8208fe1 | -8.5689 | -63.9155 | 2025-08-15 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b77e2d29-93cc-3a54-9462-4f7d570e577a | -7.3896 | -44.8589 | 2025-08-15 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 145.0 |
| e2cd788f-189f-3aaa-8c05-091fba529cbf | -13.1267 | -57.1293 | 2025-08-15 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| bee57b82-a5e6-3b89-8b02-5c448ad83ce9 | -7.3116 | -60.628 | 2025-08-15 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b22f6023-e90b-36d8-9efa-e010b8aaeb4e | -6.8671 | -42.8197 | 2025-08-15 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 00ec6751-feff-333d-9609-b89ac6e6242d | -13.1077 | -57.131 | 2025-08-15 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3ca9806d-6584-32d4-98f5-956a4a6be9fd | -13.4566 | -56.6757 | 2025-08-15 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| a817e5cb-f8ca-3cff-9782-269a01ae9e24 | -7.6104 | -63.4972 | 2025-08-15 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f4ebb95f-1d71-3c97-90e7-878eefdfb274 | -7.9516 | -61.7654 | 2025-08-15 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 09b0cc14-e625-3618-b58f-c37d51a797f2 | -9.1069 | -44.7261 | 2025-08-15 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 928f13f7-6b54-3c8c-acde-4b7d4ef1ace4 | -9.518 | -60.5268 | 2025-08-15 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| bc8b4778-7ddb-39b6-8c9a-24e21fcf5b97 | -9.4994 | -60.5278 | 2025-08-15 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| d98f11f0-989a-3226-b43b-ca65c63fcfae | -13.3397 | -45.2145 | 2025-08-15 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 354.4 |
| 76ad3d9c-9167-3178-91c1-4bfe2530d2ec | -9.4992 | -60.547 | 2025-08-15 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 16513b9c-5a63-3168-8d72-8e195c30d81b | -13.1262 | -57.1695 | 2025-08-15 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 0d0a6aa8-5397-3341-8a14-301243871510 | -9.8915 | -60.4297 | 2025-08-15 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| cb5efa8d-f731-3b0a-97dd-373b59f7d38b | -7.5919 | -63.4978 | 2025-08-15 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 17d00af9-88d5-3465-aa99-18bcd4294b2c | -16.3741 | -50.9089 | 2025-08-15 14:40:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 941b0599-b056-37cc-9c92-88a8728d88f2 | -10.0514 | -59.1208 | 2025-08-15 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 243a7fbf-d40d-3508-9b52-2c8cdcabc394 | -13.1453 | -57.1678 | 2025-08-15 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 668437ba-72b7-3799-b077-03d276e2026d | -13.1074 | -57.1511 | 2025-08-15 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 136.8 |
| d12e0b50-3075-3bf8-b7c0-5af242c3d922 | -7.2931 | -60.6287 | 2025-08-15 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 341d5c4a-d941-3eae-bc42-3f5070f823c7 | -14.5634 | -52.0344 | 2025-08-15 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| fea42d41-5e0c-3f6d-9c20-cbfca989b204 | -7.3894 | -44.8817 | 2025-08-15 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 265.4 |
| baa5d12b-7488-337c-84ca-675a5c81d1c5 | -13.1265 | -57.1494 | 2025-08-15 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |


