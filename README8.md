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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cc6328b-628a-3ef8-926a-29b41ba89d05 | -19.5087 | -56.5779 | 2024-11-01 01:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| ca268827-85b6-3c65-9490-0fd222c6544c | -23.9254 | -51.9222 | 2024-11-01 01:57:17 | GOES-16 | SÃO JOÃO DO IVAÍ | PARANÁ | Brasil | 4125001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.8 |
| bf2d18cd-a0e0-392a-8141-e67ed0ab636e | -4.39 | -43.44 | 2024-11-01 02:05:01 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8665362-b679-31cb-964a-8be4f42ee7eb | -4.39 | -43.49 | 2024-11-01 02:05:01 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a33ada02-309e-33e5-a6da-019f67d743d8 | -2.1695 | -48.7252 | 2024-11-01 02:05:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cade4ac6-7ea9-3ad8-9600-2b784302b556 | -3.0353 | -49.4901 | 2024-11-01 02:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 22fd618d-0d98-37bd-8e8e-0f94c18e9552 | -3.0354 | -49.4688 | 2024-11-01 02:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| fc506caf-7a51-3e01-8138-56b80fb295bd | -3.0538 | -49.4895 | 2024-11-01 02:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| bc74b55e-ef96-39d5-bfeb-f35295713ba5 | -3.0539 | -49.4683 | 2024-11-01 02:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| ced43a73-0cfc-3b55-b08a-7fd54cc779d8 | -3.5446 | -47.3855 | 2024-11-01 02:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 54ab1979-60f8-3592-8271-43a9e0a41c9b | -3.5631 | -47.3847 | 2024-11-01 02:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 269.3 |
| 538d4acb-b891-30e9-b325-1082aba36eed | -3.5632 | -47.3629 | 2024-11-01 02:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 6b4e6aa1-a43b-364a-bb37-c3b4146a064f | -4.4056 | -43.4514 | 2024-11-01 02:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| c53897c9-2005-3fae-9b11-783d854aeb3a | -4.3867 | -43.4757 | 2024-11-01 02:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 173.8 |
| eb47885b-10a4-3988-9258-4f78fa075f5e | -4.3869 | -43.4525 | 2024-11-01 02:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 8db5b942-de18-34c9-b85e-679510634519 | -4.4054 | -43.4746 | 2024-11-01 02:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 235.1 |
| 2a8a7f4c-de7e-32ae-b8a9-e6ae1814b5d6 | -4.4555 | -44.3248 | 2024-11-01 02:05:31 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| cd1f0399-60bc-336f-9c0d-a3fb7965b8e4 | -6.1039 | -43.9824 | 2024-11-01 02:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 03119fcf-4558-3445-a952-d50e11f92ab7 | -6.1041 | -43.9593 | 2024-11-01 02:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 152.0 |
| e7438869-e946-369a-8868-c2c7473c059d | -6.1043 | -43.9362 | 2024-11-01 02:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0d7b6bbc-b2c2-332d-be23-267f4a7ce911 | -6.1226 | -43.9809 | 2024-11-01 02:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 12721901-a6f5-34b7-a118-db2f30c05dfc | -6.1229 | -43.9578 | 2024-11-01 02:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| e79bebdc-45a4-3125-ab76-f0aad0687f8c | -6.1231 | -43.9347 | 2024-11-01 02:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| e049000c-cbe9-36b2-950a-6156f00fc035 | -16.9012 | -57.5108 | 2024-11-01 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| ec56a8ca-1417-336d-b048-4f93fe53ce65 | -19.4878 | -56.6227 | 2024-11-01 02:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| b7d29b58-8c03-3c6b-9d4d-aae71d63ef22 | -19.4882 | -56.6017 | 2024-11-01 02:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 6debebc2-c992-3c8d-9c2f-5faabb1173c8 | -19.5079 | -56.6199 | 2024-11-01 02:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 2aeb84d6-aeb4-3e13-bc26-147fcc80c38c | -19.5083 | -56.5989 | 2024-11-01 02:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 1e324186-d9b2-3110-911c-9928305dea96 | -19.5087 | -56.5779 | 2024-11-01 02:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.6 |
| e10257e1-33df-364a-9527-32e63ad8e52b | -2.1695 | -48.7252 | 2024-11-01 02:15:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 0265acfc-e57b-38c3-8af4-016584f59577 | -3.0353 | -49.4901 | 2024-11-01 02:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 109f2c5d-c165-3271-bc68-1580fe54c245 | -3.0354 | -49.4688 | 2024-11-01 02:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| b63493cd-1807-3095-bb50-871f25eeed55 | -3.0538 | -49.4895 | 2024-11-01 02:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 2c2d4973-4b0d-3036-98d2-0b28fc926794 | -3.0539 | -49.4683 | 2024-11-01 02:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 0333f3a5-e194-31a8-b261-beb1498afdbb | -3.563 | -47.4066 | 2024-11-01 02:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| de4a491c-f845-321a-8c79-02243bb6541a | -3.5631 | -47.3847 | 2024-11-01 02:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 234.3 |
| 99695b03-cf65-373b-a5f0-1c3a258d9ddf | -3.5632 | -47.3629 | 2024-11-01 02:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 4149cdd5-9a87-384d-bb89-d716a247793d | -4.3867 | -43.4757 | 2024-11-01 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| bdb16618-fcd3-3e35-ba95-bca2a30fac18 | -4.3869 | -43.4525 | 2024-11-01 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 3eb2648b-7c76-3e92-ae13-88d61666bee9 | -4.4054 | -43.4746 | 2024-11-01 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 3e88a844-c41f-37e6-9d29-c3dce1cc00e7 | -4.4056 | -43.4514 | 2024-11-01 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| ee2a8b7c-60fe-339e-9bcd-e63da979c8d7 | -4.9024 | -47.0357 | 2024-11-01 02:15:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 3696d2db-9b20-33c7-a5e0-beaf31bf3e2c | -6.1041 | -43.9593 | 2024-11-01 02:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 7c70a813-2928-35a5-bdd8-ed313b7e172d | -6.1226 | -43.9809 | 2024-11-01 02:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c0a30b7b-caac-37f8-aa36-cc68f82be173 | -6.1229 | -43.9578 | 2024-11-01 02:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| ead87dfa-c688-32bc-9303-e281259f7054 | -6.1231 | -43.9347 | 2024-11-01 02:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 3b556a4d-58f7-3360-bf2d-aa7d46655b91 | -16.9008 | -57.5313 | 2024-11-01 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 12269824-a9b3-3421-9314-9a10b6e7b75e | -16.9012 | -57.5108 | 2024-11-01 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 17048dfa-44e8-34e7-9ec7-843471967723 | -17.6664 | -57.5028 | 2024-11-01 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 9b878c5a-fb7d-3012-87a9-c32dba48bb40 | -19.4878 | -56.6227 | 2024-11-01 02:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| d70ed5d9-3302-3d5f-8946-cee3d8ba2c31 | -19.4882 | -56.6017 | 2024-11-01 02:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 92e03a14-9ba5-32d2-989f-82820f4e24c9 | -19.5059 | -56.7249 | 2024-11-01 02:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 36d10e1c-be58-3242-a867-3fb0a0705722 | -19.5063 | -56.7039 | 2024-11-01 02:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 42288e56-510b-3b13-8e67-102714cdb416 | -19.5067 | -56.6829 | 2024-11-01 02:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.8 |
| a2d0f7c1-b11d-33f8-9850-3b974f3668fd | -19.5083 | -56.5989 | 2024-11-01 02:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| bb576cf6-7eda-30a3-bb3f-b67629830c86 | -19.5079 | -56.6199 | 2024-11-01 02:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 35a4f201-d875-35af-acfc-1e0edcb27607 | -19.526 | -56.7221 | 2024-11-01 02:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| c5da5d46-75b1-30be-8f85-7fada3ddc0e7 | -19.5264 | -56.7011 | 2024-11-01 02:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 1a8dd056-78cc-3731-867c-8445256d9866 | -19.5461 | -56.7192 | 2024-11-01 02:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 38842d6b-e552-380b-83aa-17452f3704e0 | -2.1695 | -48.7252 | 2024-11-01 02:25:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ae7edfe4-7afe-37f1-b2e3-c082dcf6147e | -3.0538 | -49.4895 | 2024-11-01 02:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 08db04af-3ca0-337e-b336-1bf051037089 | -3.0539 | -49.4683 | 2024-11-01 02:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 8deb8937-2625-36c5-bf9c-719fe754e0af | -3.0353 | -49.4901 | 2024-11-01 02:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 4d88ed21-1a0f-3544-a27b-4fdc1c2de64b | -3.0354 | -49.4688 | 2024-11-01 02:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 56a3b30c-588d-3844-9c85-b6141870c57a | -3.5632 | -47.3629 | 2024-11-01 02:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| d5ca5b6c-529e-3404-a736-31b293f3504d | -3.5446 | -47.3855 | 2024-11-01 02:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e25ff6e8-cab5-36a3-af2b-c4545794e13a | -3.5631 | -47.3847 | 2024-11-01 02:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 209.5 |
| c347e65d-e9f7-3ef2-8bf7-711884c3020b | -4.3867 | -43.4757 | 2024-11-01 02:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| ee0665f2-e727-3c68-bbee-ca2223212e11 | -4.3869 | -43.4525 | 2024-11-01 02:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 996ddcd6-477b-369f-b6e7-c564b38ca5ac | -4.4054 | -43.4746 | 2024-11-01 02:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 901f3f37-0b56-3b7a-afc5-3e22a3d68146 | -4.4056 | -43.4514 | 2024-11-01 02:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 6eea8aa5-fae7-38d0-9350-b2fa68769a79 | -4.9023 | -47.0577 | 2024-11-01 02:25:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 2a2c1a60-eb9b-36d5-b205-8ac4f719bef9 | -4.9024 | -47.0357 | 2024-11-01 02:25:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 4af7a1ba-f2b8-355d-b483-18501ccc927c | -6.1041 | -43.9593 | 2024-11-01 02:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 21acb500-134f-39f8-979f-fa34dd99fbfb | -6.1229 | -43.9578 | 2024-11-01 02:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 47fdf6a9-ea21-3cac-8826-bc47c8444bf0 | -16.9012 | -57.5108 | 2024-11-01 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 445b14ac-9103-3ee3-9885-0d8d722ee507 | -19.4882 | -56.6017 | 2024-11-01 02:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 829761ed-5b86-3e3a-9833-a61beaa41633 | -19.5079 | -56.6199 | 2024-11-01 02:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 2b2ca01a-22d7-31bd-b91c-3d1c8a20fa6a | -19.5083 | -56.5989 | 2024-11-01 02:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| aaff2647-44b2-3b83-a3ca-3b23923b9b60 | -19.4878 | -56.6227 | 2024-11-01 02:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 0567ee57-7c95-398e-91f5-7a27131e7654 | -2.1695 | -48.7252 | 2024-11-01 02:35:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 14f0d956-a8c2-3ef0-a5b0-d30d41ef6ba6 | -3.0539 | -49.4683 | 2024-11-01 02:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| f8922a34-c7bd-3acb-9422-53575521fb1d | -3.0538 | -49.4895 | 2024-11-01 02:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 96c47cd9-29da-3568-bac9-8a497735b241 | -3.0354 | -49.4688 | 2024-11-01 02:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 518fd949-55fc-3727-802e-3c623cecdd00 | -3.0353 | -49.4901 | 2024-11-01 02:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| ec1d7e31-fd2e-32fc-86df-b694837fb443 | -3.5632 | -47.3629 | 2024-11-01 02:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f479d395-9580-3814-8f3f-8550dadba818 | -3.5631 | -47.3847 | 2024-11-01 02:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 195.7 |
| ddf28649-970e-3a67-a15b-34bbf0a41511 | -3.5446 | -47.3855 | 2024-11-01 02:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| b6cbf383-0c27-3560-8f8b-f99a51b8f9be | -4.4056 | -43.4514 | 2024-11-01 02:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 48973a13-700a-3c49-a36e-c5639fd2b092 | -4.4054 | -43.4746 | 2024-11-01 02:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 198.6 |
| b16b3bb0-72d1-3058-bf30-c21c9a36cca8 | -4.3867 | -43.4757 | 2024-11-01 02:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 4f76c3d4-8531-3dca-b9df-f9bce41d15b5 | -4.9023 | -47.0577 | 2024-11-01 02:35:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c80260df-0a84-345e-83fe-a11257ff8661 | -4.9024 | -47.0357 | 2024-11-01 02:35:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 4033b1f4-e2a7-3344-8436-1be58921a10a | -4.9209 | -47.0566 | 2024-11-01 02:35:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| eded888e-744a-395d-8711-a720e8b17a28 | -4.9211 | -47.0346 | 2024-11-01 02:35:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 145a9ddc-1023-31b5-b4b8-f79c4669a0f3 | -6.1229 | -43.9578 | 2024-11-01 02:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 9a2efce6-fa24-3c3e-b6ec-cab03527374e | -6.1226 | -43.9809 | 2024-11-01 02:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| e31faf9b-3d16-3030-a443-afe66231a573 | -6.1041 | -43.9593 | 2024-11-01 02:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 1208b711-65a2-3e72-b154-6f0d78e8cb42 | -6.1039 | -43.9824 | 2024-11-01 02:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| dc0b6ae0-eaff-389e-ba96-3acf45b56877 | -19.5079 | -56.6199 | 2024-11-01 02:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |


[Clique aqui para ver as próximas entradas](README9.md)
