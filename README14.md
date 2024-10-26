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
| 546c62d4-7062-3fc6-8d00-deddbdaccf9f | -3.41447 | -53.86816 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9f03c27b-70e7-3712-a3bf-46eebfb85a0d | -3.38585 | -49.71479 | 2024-10-26 01:09:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e3146bfe-edd7-3057-bec7-d3c8d6a0102b | -3.38438 | -49.70457 | 2024-10-26 01:09:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 81dbad66-4eb6-3926-b1e7-2d945d08c990 | -3.37702 | -50.23006 | 2024-10-26 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8e1c332d-9c6b-3a3e-bbe1-989095e781b8 | -3.37564 | -50.22034 | 2024-10-26 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| aa19cee5-302c-3c11-9baa-884491f00ddb | -3.37372 | -50.39333 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 48946ac5-dd96-3f34-a7e6-da178e761c05 | -3.35893 | -50.10336 | 2024-10-26 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d821adaa-22ec-3423-a435-85500cacef5d | -3.34157 | -50.82447 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7b89fbd4-cba7-3fec-90bc-bc49e67d3db3 | -3.33255 | -50.82576 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b00e5dbc-a3a7-33f2-a226-b79041fa0c34 | -3.33126 | -50.81655 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3f55959b-4b41-3da4-9b2b-6cb827f98be7 | -3.28728 | -53.67934 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 889d814e-6be0-3eb6-8db2-98e4cc632192 | -3.28054 | -49.55659 | 2024-10-26 01:09:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4c776578-9afc-309e-9955-e4ead6f0ed0b | -3.27903 | -49.5461 | 2024-10-26 01:09:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 41b92d5d-0a55-3c60-8744-9821521597c3 | -3.2486 | -50.35911 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 92212477-a7ff-31fb-be8f-3060f641403b | -3.24457 | -45.29812 | 2024-10-26 01:09:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| c20e7628-c23f-3359-8ea0-f90440dcc9b1 | -3.24382 | -45.82565 | 2024-10-26 01:09:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 9c091bb6-72e3-39c2-8a3e-07a8e8e407f0 | -3.24099 | -45.80625 | 2024-10-26 01:09:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 03436306-1fda-3b83-9254-8eec5fb2fb9b | -3.23473 | -50.1934 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 7bb264ec-74db-35be-9760-a12cb072a545 | -3.23337 | -50.18364 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 686137a5-ec5f-3b6a-ac5b-b0047079d98c | -3.21644 | -53.36438 | 2024-10-26 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 813efc8d-3493-354a-a226-beae2783f4f9 | -3.15288 | -50.46626 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3a66a94-907d-312f-87d1-409f85e9af55 | -3.15153 | -50.45675 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7e5f306b-b224-3dd7-911c-dcf34b9161e9 | -3.14984 | -54.34841 | 2024-10-26 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1dcbb5d0-78ba-31c1-a372-58f2d3fded7c | -3.14156 | -54.28842 | 2024-10-26 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 881d9382-53a8-3661-b748-5dc49d3f86f7 | -3.13083 | -54.27971 | 2024-10-26 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b31b8a55-4eb7-31f0-a47d-00ac4fe84aa6 | -3.12947 | -54.26983 | 2024-10-26 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 771053d5-f44d-3a69-adfe-2c24110ec676 | -2.1929 | -53.7234 | 2024-10-26 01:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0c5b8cf9-0304-37a2-9fb9-ff4a8cf15b36 | -2.694 | -52.0653 | 2024-10-26 01:15:21 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| ec910853-4fa4-3595-b154-2a54e5e50346 | -2.6949 | -51.7979 | 2024-10-26 01:15:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 4c822cc2-2724-3536-82e0-3f2ef68b7b3f | -2.8739 | -53.3252 | 2024-10-26 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 8ca561cf-2b95-3d8f-aa20-cbd8e49272d4 | -2.874 | -53.3049 | 2024-10-26 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 51ed420a-c078-322a-b51f-04a35f535f7c | -2.8923 | -53.3247 | 2024-10-26 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 7be5bf08-8674-3e25-9a27-308380eccc12 | -2.8924 | -53.3045 | 2024-10-26 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 515776af-2a89-326a-8841-310cb65bb5f9 | -2.9501 | -52.5708 | 2024-10-26 01:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| cdb29748-690a-3301-a7cd-bad216e640b9 | -2.9501 | -52.5504 | 2024-10-26 01:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2f94afe9-5ee5-33a2-9c0d-6fffc2b2d6e2 | -2.9578 | -50.4198 | 2024-10-26 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 941e7091-86af-39d4-aa8e-2665b8a32e66 | -2.9945 | -50.4816 | 2024-10-26 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| df996e40-49f9-3420-bcd8-51fcb740a1b8 | -3.0129 | -50.502 | 2024-10-26 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| f0acf2cb-b0d2-3853-a8ad-22b654abf8c0 | -3.013 | -50.481 | 2024-10-26 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 6fbcd664-fb3c-32fb-92c5-3b99bab88d8b | -3.013 | -50.4601 | 2024-10-26 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 09563a39-25f3-352a-82be-fb9b471b1c24 | -3.0314 | -50.4805 | 2024-10-26 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| d5260f4b-fcf9-3e80-8097-6f52449b0da0 | -3.0932 | -53.7239 | 2024-10-26 01:15:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 3a8426f4-7920-3240-89df-1112f0f700fa | -3.1116 | -53.7234 | 2024-10-26 01:15:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 4c202d70-feb9-3cdd-89b8-6783c871da51 | -3.2368 | -45.8077 | 2024-10-26 01:15:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 033bd636-940f-38f2-ae77-80f7df128e89 | -3.4729 | -43.3377 | 2024-10-26 01:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 2a68b912-85d9-3998-b616-104758dfd3af | -3.473 | -43.3144 | 2024-10-26 01:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7cff3b4f-1406-32e5-8778-e64a061d61a2 | -3.4915 | -43.3368 | 2024-10-26 01:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| a539ae0c-b0e5-39a3-9763-0fba11b112cb | -3.4917 | -43.3136 | 2024-10-26 01:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 63cd8736-8c02-3298-9955-09ccbdfd9638 | -4.5613 | -48.0358 | 2024-10-26 01:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| bb303a76-65e0-37c2-9fa3-09fa0c965c06 | -4.5614 | -48.0141 | 2024-10-26 01:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 9fbb3537-358f-39b9-b1a4-4d98fee375f1 | -4.5799 | -48.0349 | 2024-10-26 01:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 0bdd59bd-1a16-3865-b7f4-507daeb7cba2 | -4.58 | -48.0132 | 2024-10-26 01:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 189.2 |
| ee132c1f-4804-35f4-ace0-0ff11dd0a6c3 | -5.5542 | -47.0188 | 2024-10-26 01:15:37 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 312b3b98-9f77-3d11-985c-16b68e9af12d | -7.0548 | -35.2365 | 2024-10-26 01:15:44 | GOES-16 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 88.2 |
| 3fec6248-6c60-3f8b-ace7-354219b1775f | -7.6474 | -63.4584 | 2024-10-26 01:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 09e6babc-4aeb-360b-8c2a-c5459c4141b0 | -9.4996 | -47.8068 | 2024-10-26 01:15:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 82d9b201-fd97-306b-962b-3a1cee5d6c8d | -16.94 | -57.5268 | 2024-10-26 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 0006fc0c-961e-381c-acbf-3fd3ac3647d5 | -16.9792 | -57.5223 | 2024-10-26 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.7 |
| ba3b3591-3a4d-37fd-adc8-f5d6e6fce8eb | -17.0499 | -53.452 | 2024-10-26 01:16:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| be8a0e38-7bc9-34b4-bcc1-3488324867ed | -17.219 | -57.228 | 2024-10-26 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 66971838-563b-37ba-8cd6-a6bb3e77493c | -17.2344 | -57.4926 | 2024-10-26 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| 4b74c40e-c568-30de-b449-a5c6955587d6 | -17.2537 | -57.5108 | 2024-10-26 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| c59cca3e-e406-30cf-8939-87d0633d07fb | -17.254 | -57.4903 | 2024-10-26 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| fd4ce884-b5f6-3bdb-8538-e2c81862508c | -17.2733 | -57.5085 | 2024-10-26 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| 7d79702d-2c4a-3abb-a0f5-29f3f12a1efd | -17.6667 | -57.4822 | 2024-10-26 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 53aacbd1-0466-3600-8af4-bb92c6f77774 | -17.6865 | -57.4798 | 2024-10-26 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 891deea9-30d7-3673-8af5-21345e6c4518 | -17.7868 | -57.3649 | 2024-10-26 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| ba04b656-0b11-39c3-b9de-646f5a341d88 | -17.7872 | -57.3443 | 2024-10-26 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.4 |
| 4dcabeac-c946-343c-85de-9d43d8fe9262 | -18.065 | -57.2481 | 2024-10-26 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| f1d23b62-436c-326f-9a9e-793ca9e65d59 | -18.0653 | -57.2274 | 2024-10-26 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 1d302e18-5c92-3258-a042-3d849a12748b | -18.0847 | -57.2456 | 2024-10-26 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| a7a5face-7535-3990-bd05-3719092302c4 | -18.0851 | -57.2249 | 2024-10-26 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 8d6a702f-bce4-32c9-a26b-d26bc29448d3 | -18.2645 | -56.0184 | 2024-10-26 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.1 |
| 39b3ba4a-3fca-3672-8737-8893f7896ad3 | -18.2649 | -55.9975 | 2024-10-26 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 520404b4-1e48-3b16-aae1-910fba71c35b | -19.5264 | -56.7011 | 2024-10-26 01:16:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 1c96f1d5-b2b1-3af7-93ed-914d7eb3d5ec | -19.5465 | -56.6983 | 2024-10-26 01:16:54 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| b265d1c3-ce73-3f9e-8e9f-6bc190573937 | -19.6256 | -56.7499 | 2024-10-26 01:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 471347c5-f862-39c5-9160-12a7e9eb3556 | -2.1929 | -53.7234 | 2024-10-26 01:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| f260b0a2-8892-3d67-a5e2-e06cc62f74c9 | -2.694 | -52.0653 | 2024-10-26 01:25:21 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 00d0ac46-ee36-39cf-ad95-dfc716254a9f | -2.8739 | -53.3252 | 2024-10-26 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 81b6bb49-d021-3007-ba79-ed94d8328abc | -2.874 | -53.3049 | 2024-10-26 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 90de1160-b647-30f0-a5f2-09c657b54c5c | -2.8923 | -53.3247 | 2024-10-26 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 51d8edb3-e201-38ce-8994-e10a132c7e74 | -2.8924 | -53.3045 | 2024-10-26 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| e8c1f984-dfff-3664-9ca9-d93eb4f1909c | -2.9317 | -52.5713 | 2024-10-26 01:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| ac5c1ecc-2879-3c79-b1c2-871cd0cbed09 | -2.9501 | -52.5708 | 2024-10-26 01:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 858f8d29-086c-3730-9676-06f8db534ad3 | -2.9501 | -52.5504 | 2024-10-26 01:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| a70cffea-0cbb-3409-b075-d9f4ad02ce3f | -2.9944 | -50.5025 | 2024-10-26 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| c71c7633-6020-3590-ac0e-5f5ed0f1477a | -2.9945 | -50.4816 | 2024-10-26 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 1dba107f-ebcf-38e8-ac86-377510aa420d | -3.013 | -50.481 | 2024-10-26 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| d21446fe-52c1-3a6e-9861-fa506603bb30 | -3.013 | -50.4601 | 2024-10-26 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| eb66d56c-02d1-3e8b-9aee-0b71227a01d0 | -3.0314 | -50.4805 | 2024-10-26 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 833a71f2-7a3c-3e28-b77a-6d17c643832f | -3.1116 | -53.7234 | 2024-10-26 01:25:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 4d816b90-522b-3b51-86ad-11468f476a75 | -3.2393 | -45.2918 | 2024-10-26 01:25:23 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d7ef97a2-28bc-3b8f-9469-5d8d16bdca0d | -3.2553 | -45.807 | 2024-10-26 01:25:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 769284ba-db9c-3882-96a7-7529f84871cd | -3.4729 | -43.3377 | 2024-10-26 01:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 4c88cf1f-58ef-3f39-9536-a7294914c2eb | -3.473 | -43.3144 | 2024-10-26 01:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ee69ac10-82fa-3a53-9de9-b5f73209ec1e | -3.4915 | -43.3368 | 2024-10-26 01:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 55f17ce5-5fd0-3e4f-b4cb-5be0ccf2dc8d | -4.5613 | -48.0358 | 2024-10-26 01:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| fc546b32-ea86-32d2-9598-b5e9ab7969cb | -4.5614 | -48.0141 | 2024-10-26 01:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f9eb2590-098d-313e-ac49-bf49023e77e7 | -4.5799 | -48.0349 | 2024-10-26 01:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 241.3 |


[Clique aqui para ver as próximas entradas](README15.md)
