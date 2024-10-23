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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34901355-d181-37d4-8bb1-7d0fa97e1f14 | -1.388 | -51.9867 | 2024-10-23 04:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 70be1027-9035-3023-9759-028c3eb64b67 | -1.3879 | -52.0072 | 2024-10-23 04:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8fa0d9d8-d8eb-30e9-9b25-2d27c16c2043 | -3.1102 | -54.146 | 2024-10-23 04:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e41fe113-15e4-3130-8739-c0a0f15ed62a | -3.1101 | -54.1661 | 2024-10-23 04:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 9be14a98-6e57-31b6-843a-b96b9c8db3e3 | -3.0917 | -54.1666 | 2024-10-23 04:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e001da32-711f-35be-93ab-86d61ee0540a | -4.1306 | -45.5663 | 2024-10-23 04:05:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8ebae388-049e-39b6-9e3d-bcfd6493c637 | -4.1305 | -45.5888 | 2024-10-23 04:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 586.4 |
| 0d848cb0-e40d-37fd-96ca-7829b8cd4023 | -4.1304 | -45.6112 | 2024-10-23 04:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 314.7 |
| f98d9eb0-0dec-342a-9e03-29ab3e6e7d6f | -4.1119 | -45.5897 | 2024-10-23 04:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 8455e449-83df-325e-b0a0-60b5b9da5928 | -4.1491 | -45.5878 | 2024-10-23 04:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 851abdea-b0a2-3f21-b9e2-c9e477a10ce4 | -4.149 | -45.6103 | 2024-10-23 04:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| bc4f3116-2990-3cb9-b950-bc00d59aeed9 | -4.7751 | -46.6238 | 2024-10-23 04:05:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 7813063a-66fe-36eb-a7f9-65905c2980b4 | -4.7565 | -46.6249 | 2024-10-23 04:05:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f28249c3-b8eb-38aa-93a3-cb23cff397f3 | -5.5671 | -43.2576 | 2024-10-23 04:05:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 47b241dc-d8d7-3ec3-a054-a4b543595dc8 | -5.5858 | -43.2562 | 2024-10-23 04:05:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 44100527-434a-37ff-90a4-7d170ba5590b | -28.44754 | -50.07138 | 2024-10-23 04:06:00 | NOAA-20 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5c46205d-4598-341d-ba64-6bb1c3425eb2 | -29.12066 | -50.34894 | 2024-10-23 04:06:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 83c29950-622c-3805-b27c-19970629ae8c | -29.81529 | -51.17487 | 2024-10-23 04:06:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 286d98b6-bf55-3dc2-b048-8bb29dcfa7b1 | -29.81312 | -51.17529 | 2024-10-23 04:06:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| db78393a-44ec-3e74-ab5e-0573965a905f | -11.8261 | -47.0832 | 2024-10-23 04:06:13 | GOES-16 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| a95a9f99-4c9f-38dd-a0e3-8cd3a71f5bf5 | -17.0184 | -57.5178 | 2024-10-23 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 422eea59-8ad7-3161-a70f-6196a1aca383 | -18.3004 | -56.2222 | 2024-10-23 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 6695043d-892f-3504-bb73-8a4bbd52bda6 | -18.3203 | -56.2195 | 2024-10-23 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 174.1 |
| d4b5f6b1-3150-3768-a6e6-21d284344548 | -18.3207 | -56.1986 | 2024-10-23 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 82d05e26-1d33-3914-817c-ecbbe1e14e05 | -19.5268 | -56.6801 | 2024-10-23 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.9 |
| ec9f6d52-8b2d-37d1-aba0-b981a84593bb | -19.5272 | -56.6591 | 2024-10-23 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.4 |
| a22f0b94-b3b3-31b1-9391-50dbc208edec | -19.5465 | -56.6983 | 2024-10-23 04:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 387107c8-1b60-3c02-9344-5ffd22045e28 | -19.5469 | -56.6773 | 2024-10-23 04:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 198.6 |
| 4b03161c-10a0-3bc0-9ade-5dcf26d0bc6a | -19.5473 | -56.6563 | 2024-10-23 04:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 127.4 |
| 307e214d-1f2f-33b2-8a46-87d7f4c44d2a | -19.5669 | -56.6744 | 2024-10-23 04:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 53.4 |
| c055bd01-6c5a-3e1c-b903-46ad1b64347b | -19.6245 | -56.8129 | 2024-10-23 04:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 5bf36a04-1adc-3d27-a8b7-303b1a44f5a5 | -19.6249 | -56.7919 | 2024-10-23 04:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 106.0 |
| 75e311e4-ae8e-3bdb-96d8-8e3a4166f9e0 | -19.6253 | -56.7709 | 2024-10-23 04:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| ce1d58c3-44a7-39da-ab98-513bf5b5ecdc | -19.6446 | -56.8101 | 2024-10-23 04:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.3 |
| cf388c93-d634-3f57-81e6-45256c958733 | -19.645 | -56.7891 | 2024-10-23 04:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| d43b8db8-e21c-3eb5-96b3-93ea01f49d29 | -1.388 | -51.9867 | 2024-10-23 04:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b76e9136-8588-3b28-b4a6-dc71c38acc6a | -3.0917 | -54.1666 | 2024-10-23 04:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 431085a4-f023-3384-a3a9-eff31fa94297 | -3.1101 | -54.1661 | 2024-10-23 04:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 0f019083-0efa-35a0-9e73-ed16aaf18440 | -3.1102 | -54.146 | 2024-10-23 04:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e038fee5-c627-3049-95ff-e49829c229f9 | -4.1304 | -45.6112 | 2024-10-23 04:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 29d48c50-7fef-31d4-ad28-0c26bd5a9359 | -4.1305 | -45.5888 | 2024-10-23 04:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 262.9 |
| 46edb5e1-5f56-3ce1-ad89-214b5e0b14bb | -4.1306 | -45.5663 | 2024-10-23 04:15:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 05625c2d-0d4f-39d9-b102-a514fc57764c | -4.1491 | -45.5878 | 2024-10-23 04:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 245bee09-1ca9-3e14-8ba0-3e1b86d02175 | -5.5671 | -43.2576 | 2024-10-23 04:15:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 11cc5e6c-0057-3b0f-a0fb-23a4afc55244 | -5.5858 | -43.2562 | 2024-10-23 04:15:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 0ec08798-25de-3ef9-a43f-406a3fd37d34 | -17.0184 | -57.5178 | 2024-10-23 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| c4b838a3-2cd4-37e7-b85f-a6b9ff40ce27 | -18.3004 | -56.2222 | 2024-10-23 04:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.3 |
| ef6ba852-7cfa-3d2d-9745-3bd1e7464f43 | -18.3203 | -56.2195 | 2024-10-23 04:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.3 |
| 4b5ca24e-b241-3e7b-80a8-92adc178daf7 | -19.5473 | -56.6563 | 2024-10-23 04:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 306d9638-b3f7-382e-9b1c-e274e298df77 | -19.5272 | -56.6591 | 2024-10-23 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 40c34d2e-3a7f-353e-9a02-36d8c06bce0f | -19.6453 | -56.7681 | 2024-10-23 04:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 1a3f5abe-1914-31e8-bbc7-f6ec6be14fef | -19.6249 | -56.7919 | 2024-10-23 04:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 147.3 |
| b1a900c3-066b-3616-ab69-94fd51d820fb | -19.6245 | -56.8129 | 2024-10-23 04:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 128.5 |
| 1dd88191-93e7-32d9-b6d4-4413969b8467 | -19.645 | -56.7891 | 2024-10-23 04:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.0 |
| 6933cfa6-37f7-303a-9880-dacf0f6a70bc | -19.6446 | -56.8101 | 2024-10-23 04:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 959fbc5e-0dd2-346e-87c4-86b77bd6c608 | -19.6253 | -56.7709 | 2024-10-23 04:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 157d2ebf-6216-312d-9cbd-5df38d0cfd78 | -1.388 | -51.9867 | 2024-10-23 04:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f8c7cf18-0416-3a6d-b1f6-28f19928cf27 | -3.0917 | -54.1666 | 2024-10-23 04:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 4c338c74-093b-3c4b-b6ce-3fd9b27201f6 | -3.1101 | -54.1661 | 2024-10-23 04:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| b5ee1be9-cd13-3916-92eb-8a5c7e7935ff | -3.1102 | -54.146 | 2024-10-23 04:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 4a831bff-5fda-3d14-9ead-dace5189f342 | -4.1119 | -45.5897 | 2024-10-23 04:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d4339d5e-e411-3646-969c-5763eda40241 | -4.1305 | -45.5888 | 2024-10-23 04:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 225.6 |
| 0ba9ee01-f3d1-3f1d-8f9f-fb89bf1a9314 | -4.1306 | -45.5663 | 2024-10-23 04:25:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d4a2afa5-d45a-3807-a190-cb1288cd98dc | -4.1304 | -45.6112 | 2024-10-23 04:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 3b13a404-5ed6-34d0-b8a1-b5f634f03879 | -4.1491 | -45.5878 | 2024-10-23 04:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 17cfe7e6-34da-3a00-8306-a7cbe0d8abc8 | -4.7254 | -45.7363 | 2024-10-23 04:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 45ba62b5-8321-3f66-aaa8-227db9496a08 | -5.5671 | -43.2576 | 2024-10-23 04:25:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| d7ac677a-ddb7-35d8-aa88-87b21aad9fe3 | -18.3203 | -56.2195 | 2024-10-23 04:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 2b594662-5938-364a-9cc5-2ad5ce8ea9c9 | -18.3004 | -56.2222 | 2024-10-23 04:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.7 |
| 0db36d94-7e91-372e-a422-742ad8992180 | -19.5268 | -56.6801 | 2024-10-23 04:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 08379a20-da4d-3381-9770-800cd3be1ccb | -19.5465 | -56.6983 | 2024-10-23 04:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 141.5 |
| 7b52a03d-be73-3b10-bd08-68ca9caefd39 | -19.5469 | -56.6773 | 2024-10-23 04:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 252.6 |
| 71a0a221-fce0-3b85-9b26-c3e5ed059210 | -19.5473 | -56.6563 | 2024-10-23 04:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 0715bc35-f3e1-3009-b3a4-fd29045f71f5 | -19.5669 | -56.6744 | 2024-10-23 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 105.8 |
| 17f1092b-d9e3-3485-b436-5b3779e32695 | -19.6245 | -56.8129 | 2024-10-23 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 195.9 |
| 91444694-7801-3c3d-96d8-a75f88574bf0 | -19.6249 | -56.7919 | 2024-10-23 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 197.3 |
| 381b1ba2-30b5-382b-924d-86be8181c009 | -19.6253 | -56.7709 | 2024-10-23 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.1 |
| ace2ef2a-8d9a-35ee-ab52-ffa4163cccc0 | -19.6446 | -56.8101 | 2024-10-23 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 9b6a8629-219b-3afb-a5cf-a9fc2533bed4 | -19.645 | -56.7891 | 2024-10-23 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 65eb4e54-7480-34b1-bbda-8df4ed4482c1 | -3.0917 | -54.1666 | 2024-10-23 04:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| e7ab2354-2aa9-3c3f-a800-94cfae3ac390 | -3.1101 | -54.1661 | 2024-10-23 04:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 84897b46-48d7-30b8-bdf0-75317614a004 | -3.1102 | -54.146 | 2024-10-23 04:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 43fd36e9-5412-3ae4-9723-071653436ccc | -4.1119 | -45.5897 | 2024-10-23 04:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| bd3a6b95-19f3-3904-8715-a3b2944907b8 | -4.1304 | -45.6112 | 2024-10-23 04:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 43fb8841-f43e-31f9-86f8-d72239322b5f | -4.1305 | -45.5888 | 2024-10-23 04:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 169.0 |
| 335b06ca-067b-36db-bf7c-1efddef1409b | -4.1491 | -45.5878 | 2024-10-23 04:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a44ac055-4357-3552-9cea-05e98cd96990 | -4.1905 | -47.9885 | 2024-10-23 04:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 248cad21-c3da-3874-9dc2-9b431f60cf99 | -5.5858 | -43.2562 | 2024-10-23 04:35:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2c8727d9-c409-3ee8-801e-485619109c0a | -17.0184 | -57.5178 | 2024-10-23 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 7f59b3a2-2be4-378e-9292-f4dd7e214097 | -18.3004 | -56.2222 | 2024-10-23 04:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| f52f2415-8eae-3681-9b51-b9505acd139a | -18.3203 | -56.2195 | 2024-10-23 04:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 82da04f0-dc56-3521-82c0-225e04f87354 | -19.5268 | -56.6801 | 2024-10-23 04:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| e34ff42b-1ef6-35b0-95a1-5e94a4762a92 | -19.5465 | -56.6983 | 2024-10-23 04:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 5520ee61-72ff-3c11-a958-956e454d305e | -19.5469 | -56.6773 | 2024-10-23 04:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 119.8 |
| 88de7248-1c9a-35ce-9040-8a86a8891b0d | -19.5473 | -56.6563 | 2024-10-23 04:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 47b4b6ec-fd5c-35f7-8801-f627faa5421e | -19.5669 | -56.6744 | 2024-10-23 04:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| c1da07bb-c72d-351e-9c35-65a8e885586f | -19.6245 | -56.8129 | 2024-10-23 04:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.1 |
| 28b4f25c-0d5a-3317-8672-a91a8542dea7 | -19.6249 | -56.7919 | 2024-10-23 04:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 138.9 |
| 32b7386d-20a5-348b-81f5-c4d418e239c5 | -19.6253 | -56.7709 | 2024-10-23 04:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| c9af617e-6ada-3937-95db-0086a7614ecf | -19.6446 | -56.8101 | 2024-10-23 04:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |


[Clique aqui para ver as próximas entradas](README30.md)
