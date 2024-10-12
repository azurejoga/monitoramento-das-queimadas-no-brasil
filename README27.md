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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5593351-fb7c-39b7-999b-d4342312fd5d | -4.285 | -50.9586 | 2024-10-12 01:45:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 739a7665-bbf7-3cd8-a29c-ba8012c430d0 | -4.7188 | -60.7882 | 2024-10-12 01:45:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0fb8c0e0-d326-3ace-90c8-9e3ab1f6af86 | -4.7371 | -60.7877 | 2024-10-12 01:45:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3c100504-0e04-37e5-9463-79e99e630e6f | -6.0603 | -44.629 | 2024-10-12 01:45:40 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| e86783c7-4215-3b9c-8c36-539dfbe4855a | -6.0791 | -44.6276 | 2024-10-12 01:45:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 2441fa70-90a2-368d-bd30-8f70dc84dae9 | -6.7285 | -59.3267 | 2024-10-12 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 32463e3c-2e22-3ce3-83af-1b0166c34c36 | -6.7469 | -59.3452 | 2024-10-12 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.8 |
| de0616d5-905d-37a5-aed6-a61f7a6a0583 | -6.747 | -59.3259 | 2024-10-12 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 237.3 |
| 60332d8a-8b95-3a6c-baec-279bebdbad9c | -7.8529 | -54.7027 | 2024-10-12 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c1c4c445-2167-3505-9c9c-c8c195e094c4 | -7.8713 | -54.7217 | 2024-10-12 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| be12b4b8-63bc-362a-b619-5a6e7aaf719b | -7.8715 | -54.7016 | 2024-10-12 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 176.7 |
| 0a9740e0-d88c-3e93-8e13-415438d7d708 | -7.8717 | -54.6814 | 2024-10-12 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| eec387e9-4e4c-3acf-837a-4ad1608223a3 | -7.89 | -54.7206 | 2024-10-12 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 24f8c315-5177-318a-9a34-c6dfde49cc2a | -7.8901 | -54.7004 | 2024-10-12 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a3d6d448-2359-36c1-994b-ffb8a769ab66 | -10.3708 | -61.232 | 2024-10-12 01:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 4903fff2-c3ca-372a-b50c-7e3c306545f1 | -10.3892 | -61.2695 | 2024-10-12 01:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 18d3b8af-7ac7-389a-8d99-371f3f805a6c | -10.3895 | -61.231 | 2024-10-12 01:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 5c7137cb-75e0-32fd-92d7-ac2f13c179b1 | -10.3897 | -61.2118 | 2024-10-12 01:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 7a9bd880-019b-3ef2-9cac-d638984074a0 | -10.4079 | -61.2685 | 2024-10-12 01:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| fc1a6790-e792-3d13-9314-14b23d5f0496 | -10.5328 | -51.0425 | 2024-10-12 01:46:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| eba530f6-db3a-3d74-9820-d8bc77848782 | -10.9506 | -44.653 | 2024-10-12 01:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 84afcd9f-140b-3111-bbe0-8bd9b4ec1545 | -10.8568 | -63.8988 | 2024-10-12 01:46:09 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 30.9 |
| cc756da7-c3d2-3d69-be9a-57a1acef93b2 | -11.8377 | -58.8445 | 2024-10-12 01:46:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 4d08b6af-ee1f-3bca-a1bb-3b31acc03c60 | -12.7866 | -44.8873 | 2024-10-12 01:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| cbb64235-507b-39bf-ba8c-da70a37f0cfa | -12.7871 | -44.8639 | 2024-10-12 01:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 382a0c33-7f59-39bc-a3e9-29ef7471f406 | -12.7875 | -44.8406 | 2024-10-12 01:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 1a3ebb0a-c563-32f0-97b6-d0892bfe4a99 | -12.8064 | -44.8608 | 2024-10-12 01:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 7bd70ed4-c9ad-3285-93d6-eba9f453e029 | -12.9464 | -53.5339 | 2024-10-12 01:46:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 752d8fd9-f32d-3df1-a70b-07dc205eb73a | -12.9467 | -53.5131 | 2024-10-12 01:46:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 8101dd32-609f-365d-bc07-ccd2df0a61f9 | -12.9655 | -53.5319 | 2024-10-12 01:46:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| b677af76-7f67-32b4-8955-9bed33f4642b | -12.9658 | -53.511 | 2024-10-12 01:46:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 6a647c3c-a994-33b1-9d69-b9ef0cd21694 | -13.9274 | -45.8091 | 2024-10-12 01:46:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 3a98948c-cec1-3c8d-a3bc-bd5803519f3c | -13.9278 | -45.786 | 2024-10-12 01:46:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 4b681cf1-0694-3271-b524-f84007f065fe | -13.9473 | -45.7827 | 2024-10-12 01:46:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| f69d581e-abc5-3c63-b9e7-f8a2d5de7811 | -14.3246 | -57.6002 | 2024-10-12 01:46:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| c9a64ed1-35f1-319f-945a-15da9f74771b | -14.3249 | -57.58 | 2024-10-12 01:46:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c543b11d-87cd-370b-9768-cbdb76119753 | -17.0426 | -56.0333 | 2024-10-12 01:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| d1bdba9c-ea31-3c81-937e-f5302212e1ed | -17.1761 | -57.4585 | 2024-10-12 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| 70950ac4-2849-305d-add7-687d6142d1d1 | -17.627 | -56.3318 | 2024-10-12 01:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.8 |
| a8e9a7b7-60e6-377d-96b7-58bfc7047866 | -17.6273 | -56.311 | 2024-10-12 01:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| a0174183-1f68-3783-ae4e-30c8e7404f6f | -17.6467 | -56.3292 | 2024-10-12 01:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 184.4 |
| 27460b8c-081d-3435-955a-b1fa5a65170f | -17.6471 | -56.3084 | 2024-10-12 01:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.4 |
| e96fca83-6f97-344e-99c0-849ac2e62a6c | -17.964 | -57.3843 | 2024-10-12 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| ae872ac7-d357-395c-957c-9d92cd2142a2 | -17.9643 | -57.3637 | 2024-10-12 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| e1e28390-a043-3b29-80b7-f5f5a8c8e9a5 | -17.9837 | -57.3819 | 2024-10-12 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 0dc8824b-a980-3302-9fba-73ea5ae8265b | -17.9841 | -57.3612 | 2024-10-12 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.1 |
| b31dea82-68f1-3ff3-9c4e-c65faca04190 | -1.6061 | -53.3492 | 2024-10-12 01:55:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 4aaea80f-8b5b-3169-8ab3-d56b10c34c22 | -1.8793 | -54.4312 | 2024-10-12 01:55:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 0d6c204e-163d-3d1c-b4c0-377fa41fd5b8 | -1.8977 | -54.4309 | 2024-10-12 01:55:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 81e02795-1382-3a06-a719-4bb597fc3ee4 | -2.77 | -51.3829 | 2024-10-12 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f09b4aeb-4cf3-3828-9258-95c856102e1e | -2.7701 | -51.3622 | 2024-10-12 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b9eb328d-45ad-3428-a67f-dac1e93fcbc9 | -2.7884 | -51.3825 | 2024-10-12 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| c693e398-2d71-3bc0-a510-3a3cf2cc19d8 | -2.7885 | -51.3618 | 2024-10-12 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 0936bef5-493f-39ca-8a75-b30a98d8acf7 | -2.7983 | -54.0129 | 2024-10-12 01:55:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7263e3f3-a1e4-3211-86fd-81cd10ebc37c | -2.8319 | -49.5385 | 2024-10-12 01:55:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 7fcad17a-68de-3431-8bd1-422609e3ef2e | -2.8611 | -51.6699 | 2024-10-12 01:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 538611cf-c743-3594-a6d2-b05c5288bbee | -3.0311 | -50.5642 | 2024-10-12 01:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 28230e70-2d50-3876-9073-1d20371afb7f | -3.2136 | -46.7843 | 2024-10-12 01:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7dffcadb-3f04-34e9-80f6-76a5e5b53ac3 | -3.2321 | -46.7836 | 2024-10-12 01:55:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 82cd99b1-548e-3b9c-820b-37cd511e6ad5 | -3.483 | -52.8211 | 2024-10-12 01:55:26 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 3be5fc27-55e7-3418-89f5-aaaf44185f25 | -3.7087 | -47.9227 | 2024-10-12 01:55:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 197.3 |
| 169cb30c-2af8-33fb-8fab-7d0979d6a4bf | -3.7088 | -47.901 | 2024-10-12 01:55:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2e83788a-796b-3485-90ca-ddec828a9f4f | -3.69 | -47.9451 | 2024-10-12 01:55:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b30c1960-3618-3644-bba4-529c60a6e216 | -3.6901 | -47.9234 | 2024-10-12 01:55:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| ebaffceb-81b3-3282-b345-af34123eb105 | -3.7086 | -47.9444 | 2024-10-12 01:55:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| d84135ab-9a1a-38b6-a193-37430206125d | -3.8167 | -52.3403 | 2024-10-12 01:55:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 48beaea8-f3ba-3774-a2ae-baa9b12e83c4 | -3.9394 | -46.445 | 2024-10-12 01:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 1d527b1f-3c35-3883-b5c6-643553da05b7 | -3.9396 | -46.4229 | 2024-10-12 01:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 111.8 |
| dd32ce59-6391-36bb-9b79-4fe6610346f3 | -4.1148 | -48.2515 | 2024-10-12 01:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| ecbce869-7334-359a-b624-a2d820e7a1b8 | -4.3782 | -50.8087 | 2024-10-12 01:55:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 22adb662-6044-3fa3-ae52-bcdba43bdc78 | -4.7188 | -60.7882 | 2024-10-12 01:55:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| be822bcb-77e7-3240-bcbf-2929f51df1df | -4.7371 | -60.7877 | 2024-10-12 01:55:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f33ed782-cbb4-31df-aacf-397f2f5cede6 | -4.8562 | -45.6838 | 2024-10-12 01:55:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 7856f6a1-4086-3f96-a741-749fd1a721e3 | -6.7285 | -59.3267 | 2024-10-12 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 3455c147-7fe3-3f40-a88d-bdb70228ef7e | -6.7469 | -59.3452 | 2024-10-12 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 6e08b2a4-be5a-3bea-a83c-50725829021d | -6.747 | -59.3259 | 2024-10-12 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 239.4 |
| 069c0dcf-84d9-3228-a55b-ad2d90807464 | -7.292 | -64.6676 | 2024-10-12 01:55:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 851d097d-161c-3816-b8f9-35a16cb4c975 | -7.8713 | -54.7217 | 2024-10-12 01:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 4fceeec8-16d3-37c0-89b2-cec6491a8fbb | -7.8715 | -54.7016 | 2024-10-12 01:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 609a3259-6283-388d-9597-a17b32cc3855 | -7.8901 | -54.7004 | 2024-10-12 01:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 49ce851a-38b3-337f-b933-53d0633a1349 | -8.4231 | -55.4704 | 2024-10-12 01:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 1c2e5a54-693a-3747-a550-8ac6b434357c | -9.5768 | -55.8133 | 2024-10-12 01:56:01 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| d6f48bfd-2793-3ad6-a8b4-066ff33374c2 | -9.577 | -55.7932 | 2024-10-12 01:56:01 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8ec4d982-bf46-3ad4-aaa4-6be241f95955 | -10.3708 | -61.232 | 2024-10-12 01:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| da287fa9-fb82-300a-936f-4a6fea1f9fbf | -10.3892 | -61.2695 | 2024-10-12 01:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 0fbf3f36-7f90-3525-950f-20e925a12455 | -10.3895 | -61.231 | 2024-10-12 01:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 99f62cc2-6f66-322c-8736-2038e8ac1499 | -10.3897 | -61.2118 | 2024-10-12 01:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 2eb131c3-3b87-3128-9314-abb8369c5472 | -10.4079 | -61.2685 | 2024-10-12 01:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 6132a4d7-3edc-3b7c-abfa-d0645bfd5219 | -10.9506 | -44.653 | 2024-10-12 01:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 18c3aa71-d5fe-3b32-856f-0aada53d473f | -11.8377 | -58.8445 | 2024-10-12 01:56:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8600535d-8b80-3fe4-a2cf-5e29657a9ade | -12.7871 | -44.8639 | 2024-10-12 01:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 3154f2ee-6ac0-3844-a648-2cedd32acd90 | -12.8064 | -44.8608 | 2024-10-12 01:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 4710f318-9dc5-36f7-85a0-ee2504d69cb6 | -12.8129 | -53.5277 | 2024-10-12 01:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 04d6a56f-3a8e-3400-a19a-d8e53d9f8fe9 | -12.8132 | -53.5069 | 2024-10-12 01:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| acc1aa05-e15f-34c3-b5ee-9be03afac872 | -14.3246 | -57.6002 | 2024-10-12 01:56:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 7052cea5-be32-38bf-ad22-fd9b7fed3557 | -14.3249 | -57.58 | 2024-10-12 01:56:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9c15995e-51a7-3c47-8742-b3d250000133 | -14.3438 | -57.5983 | 2024-10-12 01:56:28 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 92467ff3-891f-3363-9113-185b6b8ee0ac | -14.3441 | -57.5782 | 2024-10-12 01:56:28 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e4ac1b6b-4a2d-3f8e-b39f-d4e7c7c8080a | -17.0426 | -56.0333 | 2024-10-12 01:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.7 |
| c1fe79d2-3e80-3b16-82de-c8fd08cc6cf1 | -17.1761 | -57.4585 | 2024-10-12 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |


[Clique aqui para ver as próximas entradas](README28.md)
