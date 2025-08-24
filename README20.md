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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7775c587-a323-3fa6-9735-a25199cb0a49 | -9.1721 | -59.4823 | 2025-08-24 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 0bb7cf1e-8280-3237-97b2-4ce67fedb87b | -17.6183 | -44.2738 | 2025-08-24 03:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 52.0 |
| a7d77dd7-9aba-3989-8add-643a3e95bb67 | -16.7965 | -51.3637 | 2025-08-24 03:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 2a2afda8-54ee-3339-8c8d-91ea35f4b811 | -17.5975 | -44.3027 | 2025-08-24 03:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 749508c2-5756-3cab-a089-e8e9e7a82b21 | -17.6176 | -44.298 | 2025-08-24 03:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 1d7f8ccb-7785-323f-acd4-f212c0b352d6 | -20.3594 | -51.7023 | 2025-08-24 03:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 82218277-9e60-3e3a-a23c-701ff3949435 | -8.6131 | -62.5929 | 2025-08-24 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e9112d5f-6a65-3695-a922-1fc3da94450c | -9.1535 | -59.4834 | 2025-08-24 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 246882d2-2b0f-3f98-8d1f-49d26179a419 | -9.1722 | -59.4629 | 2025-08-24 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 09a6d9c0-ef54-3bc2-96e1-0bcfbb3653f3 | -20.339 | -51.7062 | 2025-08-24 03:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 64.6 |
| a1e6a89b-8878-3606-bf35-ffa4453a5595 | -9.0231 | -65.7169 | 2025-08-24 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| f88d5867-cba3-355a-8175-22b9641e50ea | -11.9867 | -61.0214 | 2025-08-24 03:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| f6569f93-c7f7-3171-9021-b17e0ae44e5d | -6.8927 | -45.6963 | 2025-08-24 03:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 56a61cbb-3e0a-3a21-8d4a-148f1f405850 | -9.0232 | -65.6982 | 2025-08-24 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| fbe3a03c-5b8c-3e8e-8fb6-c6e5cb4f94c2 | -20.3396 | -51.6839 | 2025-08-24 03:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 83.8 |
| cc8e627b-8d35-3daf-a184-4abd4b5c9fc3 | -9.1536 | -59.464 | 2025-08-24 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.9 |
| f4e52df0-28c1-3593-a7a0-98327405fbc1 | -4.9605 | -55.8226 | 2025-08-24 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a9f71e25-cde7-3a81-b3d9-6c8f45f631e8 | -20.3599 | -51.68 | 2025-08-24 03:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 976f0653-faac-3526-bcd1-441900da3e91 | -9.0046 | -65.6988 | 2025-08-24 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 80289eaf-4127-3807-a97b-e7f7959ec697 | -9.1998 | -60.793 | 2025-08-24 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 2ea69cb9-eb01-3e6f-bbd1-0c24937b7f90 | -5.4181 | -60.1784 | 2025-08-24 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 00aa1bd1-791f-399d-99d3-1639b9237519 | -14.8157 | -47.9118 | 2025-08-24 03:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5eae01ac-32f5-360a-b701-ec250f013a36 | -9.1721 | -59.4823 | 2025-08-24 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| e56688d2-202d-3ae3-9f55-856ab81a90e7 | -5.4364 | -60.1779 | 2025-08-24 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| df064b50-7265-3f24-8a12-b845a7c2f8bf | -16.797 | -51.3419 | 2025-08-24 03:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 6e8c4230-834e-373a-8805-6019fb4fe938 | -3.79891 | -41.00567 | 2025-08-24 03:17:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2cb4bf47-8156-3f9d-9e02-34e543450a9c | -5.53251 | -36.84311 | 2025-08-24 03:17:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1f5ae9ff-d8b1-35c1-afd3-869b74f39c73 | -2.87242 | -41.76402 | 2025-08-24 03:17:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 68068a1d-3e93-3cb3-b223-1d5a73138c89 | -5.6923 | -38.49121 | 2025-08-24 03:17:00 | NPP-375D | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 169e6428-a18c-3731-ab20-085e954a71f0 | -4.72116 | -38.3966 | 2025-08-24 03:17:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a7e4e209-c0ba-390a-a855-b32b72e85757 | -5.53147 | -36.84904 | 2025-08-24 03:17:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5aa980c4-16c6-3bd1-b6fe-7c1f6542eebe | -5.53199 | -36.84609 | 2025-08-24 03:17:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2d18ff3b-a667-3abc-8a1c-2613d5448990 | -4.72495 | -38.39817 | 2025-08-24 03:17:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6891168f-4b29-3e51-9807-9ac8b0659be9 | -5.52871 | -36.84808 | 2025-08-24 03:17:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| da35504f-22a0-3217-9b54-aa877c830254 | -5.69298 | -38.48741 | 2025-08-24 03:17:00 | NPP-375D | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 84fc028e-463e-36c8-bd1b-1a9c40c69625 | -3.79214 | -41.00442 | 2025-08-24 03:17:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 47f21495-29d4-34bf-8842-419978896857 | -5.53377 | -36.84898 | 2025-08-24 03:17:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bc6d88c5-a6a4-3c59-bc7c-da0258b18365 | -5.52921 | -36.84513 | 2025-08-24 03:17:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 54b28061-649d-3237-a653-ed43b950e32e | -5.53427 | -36.84602 | 2025-08-24 03:17:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28708bff-6329-33e4-af51-a7590cd94d5b | -8.53999 | -37.72346 | 2025-08-24 03:19:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5130be42-d649-3dfc-a168-b68ace604e97 | -13.33427 | -43.19329 | 2025-08-24 03:19:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9cc279de-988f-3dc0-9969-d6d1aa97bb36 | -7.70151 | -42.13246 | 2025-08-24 03:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 107fc90e-9c04-33cf-ad61-b5915fdd3d5e | -7.70279 | -42.1296 | 2025-08-24 03:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 62228fa2-fc47-331d-82b5-d9eb7eaaeef6 | -13.12528 | -41.05024 | 2025-08-24 03:19:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0dfd487a-9780-3988-b01d-8ade57f12f32 | -8.53945 | -37.72647 | 2025-08-24 03:19:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9cf427de-3008-326a-96fc-96d55162bda5 | -7.7027 | -42.12608 | 2025-08-24 03:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6834dd16-9058-3b17-a2a4-39bcc12a378c | -9.1536 | -59.464 | 2025-08-24 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 1e609841-981a-3775-bdd6-f184fdeb5438 | -16.7965 | -51.3637 | 2025-08-24 03:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| abf171a4-a008-3177-abaa-89c76d65729c | -4.9605 | -55.8226 | 2025-08-24 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 73dfba0a-34cf-36fc-a0b2-c82962647356 | -14.8157 | -47.9118 | 2025-08-24 03:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| da47873f-ac56-30e2-874f-056c2f106218 | -9.0232 | -65.6982 | 2025-08-24 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 3131465c-cf1c-3e0d-b50b-bdeb19689d55 | -8.6131 | -62.5929 | 2025-08-24 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b2b465f9-6d1f-3ba1-81a9-3478c8cdaeef | -20.339 | -51.7062 | 2025-08-24 03:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 945fd159-805d-3fb9-9dd8-1d218d6d61e4 | -17.6176 | -44.298 | 2025-08-24 03:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 099d2e1c-4b02-34e2-b491-f689542245f7 | -5.4364 | -60.1779 | 2025-08-24 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| a6e6c739-aa9e-3427-947a-896066c60653 | -20.3599 | -51.68 | 2025-08-24 03:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 4ee609cc-36ee-30aa-a691-b1b6ecf3b449 | -9.0046 | -65.6988 | 2025-08-24 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 0a31fe49-3f11-3088-aa1c-6be118104e49 | -9.1535 | -59.4834 | 2025-08-24 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 0b53c2b6-f9a3-338e-8e3a-d3a2d232810f | -9.1721 | -59.4823 | 2025-08-24 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 4e55a94a-9a6d-3161-a315-493978198249 | -20.3594 | -51.7023 | 2025-08-24 03:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 84.4 |
| dce0a614-82d6-35a1-80c6-b4acdc2af7b4 | -9.1998 | -60.793 | 2025-08-24 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 3a7fa4a7-f66f-37d4-bad4-58492f4aa20e | -16.797 | -51.3419 | 2025-08-24 03:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 1d80f254-614e-31c7-8502-ec994519e23a | -20.3396 | -51.6839 | 2025-08-24 03:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 275a8f61-c404-372b-8294-a7a8337afe62 | -9.0231 | -65.7169 | 2025-08-24 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 36be62be-5e92-3fe3-9d65-e33dccc31b1e | -17.5975 | -44.3027 | 2025-08-24 03:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 3533cef4-3d1d-3564-8af2-06952db86154 | -9.1722 | -59.4629 | 2025-08-24 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 50c2abc5-89b3-3b84-b1a8-84482e2f6ac5 | -5.4181 | -60.1784 | 2025-08-24 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| db3d83d3-bb73-395a-842f-bedd613cbbb3 | -17.81385 | -44.27357 | 2025-08-24 03:21:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c550506a-2f96-31be-aad7-c955ba28afbf | -17.81257 | -44.27903 | 2025-08-24 03:21:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0a9044b-0d8d-38b1-8c8b-1e71637bac18 | -17.40565 | -42.62047 | 2025-08-24 03:21:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5230c8f2-1124-3730-af6f-8059eda4e842 | -20.69356 | -42.3156 | 2025-08-24 03:21:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| db199b18-99dc-33e6-ba2b-3f15fc1b64ca | -20.36687 | -46.73138 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4788c15-77e2-3842-97b3-4c1788f7c647 | -17.6078 | -44.29715 | 2025-08-24 03:21:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 20be1f17-1a0c-33ad-bfba-b3c5489ef7e5 | -20.35655 | -46.7426 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 507639e9-3a3d-3dcb-8caf-6c23c953431b | -20.96464 | -42.86307 | 2025-08-24 03:21:00 | NPP-375D | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b2ea4032-34d2-380d-8c78-18d2593e9b32 | -20.90636 | -42.64191 | 2025-08-24 03:21:00 | NPP-375D | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1c48d795-cf09-3c0c-8292-939b91f43b0f | -20.69275 | -42.31923 | 2025-08-24 03:21:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| de35f6f9-ddb6-3de2-8016-6ab6ce57d4f5 | -17.5925 | -46.10608 | 2025-08-24 03:21:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea5093d0-8fe1-3687-914c-6eb5182d0f9a | -20.36759 | -46.7433 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 869b2661-5882-387e-a8cb-aec05e23ae3a | -20.35927 | -46.76137 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c0b6175e-9455-3965-8bc1-b975420cf6b1 | -21.78436 | -42.08355 | 2025-08-24 03:21:00 | NPP-375D | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8773bdd1-ea71-3a6e-aaa7-f17fe7d85d31 | -21.0339 | -42.53201 | 2025-08-24 03:21:00 | NPP-375D | ROSÁRIO DA LIMEIRA | MINAS GERAIS | Brasil | 3156452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8da55abf-fb25-3050-8cf5-d48cf13457fa | -17.61053 | -44.30676 | 2025-08-24 03:21:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f07bbf6d-2a61-3bdf-84d2-8ebd49ac3a5b | -20.36557 | -46.76607 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ce12c8d-17ce-3f57-9fcc-e710c8b8e778 | -17.60512 | -44.30906 | 2025-08-24 03:21:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 038c0a0b-5626-393f-9b92-71e9d889e4ae | -20.96234 | -42.86449 | 2025-08-24 03:21:00 | NPP-375D | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 775adbfe-bdcf-3619-9872-35d96cba2f5c | -17.39084 | -42.6314 | 2025-08-24 03:21:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4611748d-450c-3a69-bf0b-e5fc8515999f | -20.35843 | -46.73517 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e081e8ef-403e-3b74-86be-c11fe03e260a | -20.47581 | -42.62292 | 2025-08-24 03:21:00 | NPP-375D | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 923974b6-0d06-3c14-9120-3c8a67fe7838 | -20.97352 | -42.86736 | 2025-08-24 03:21:00 | NPP-375D | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e411294-e06d-3563-bc8c-2d51542cd892 | -20.08265 | -46.10965 | 2025-08-24 03:21:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 496f7334-cd2f-38e4-8053-fb125e5d5b69 | -18.7572 | -45.09233 | 2025-08-24 03:21:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d36b86b5-a657-3463-9628-1ca98f3b3f34 | -19.6298 | -43.1901 | 2025-08-24 03:21:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 4245b2f6-49d1-3278-b9a8-0aab0604371b | -17.83234 | -44.54987 | 2025-08-24 03:21:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b131b9c2-17f8-35dc-98a7-500686de7d80 | -20.3652 | -46.73796 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4edbf9ed-7b81-396a-8129-1e791b26060f | -21.04006 | -42.53035 | 2025-08-24 03:21:00 | NPP-375D | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 519700a0-9e93-3b16-8b63-63357c1e5d50 | -21.03573 | -42.53025 | 2025-08-24 03:21:00 | NPP-375D | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9a851b15-5b01-3e42-b3ba-fb6bb37232ca | -19.63175 | -43.18146 | 2025-08-24 03:21:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 03a89fa5-5a37-3473-a6cc-96d436ee9204 | -20.36356 | -46.75966 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d1ebbf3-8b23-3e16-ab46-1cd84dc36e9e | -17.60646 | -44.30311 | 2025-08-24 03:21:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 48.2 |


[Clique aqui para ver as próximas entradas](README21.md)
