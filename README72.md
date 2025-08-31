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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f2dbbb3-6b68-34ae-b5f4-e133c1b2de4f | -21.43589 | -54.15749 | 2025-08-31 04:55:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4651b87c-8efe-3ac3-8b4b-fd37f7c9e885 | -28.70882 | -55.59743 | 2025-08-31 04:57:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| e9c01c21-0d44-3a26-ab63-9252e43a8888 | -28.71794 | -55.63451 | 2025-08-31 04:57:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| c495421d-0bc4-37c4-a0fa-be67dd1056ed | -28.71447 | -55.63388 | 2025-08-31 04:57:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| ba1825c7-3e53-3cb7-b3e7-9ce7ac1eba33 | -11.34053 | -43.61645 | 2025-08-31 04:57:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| d84b8834-ccd8-3380-a1bc-6a53c2cc0492 | -28.70982 | -55.64185 | 2025-08-31 04:57:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 1a45ed18-61a8-3f3a-82ce-f9de024770b3 | -11.34294 | -43.62176 | 2025-08-31 04:57:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 7fc276a1-4738-34bb-8b91-7bd46021738d | -30.20069 | -53.61579 | 2025-08-31 04:57:00 | NOAA-20 | SÃO SEPÉ | RIO GRANDE DO SUL | Brasil | 4319604 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 45d4e710-3326-3b2f-8be9-090db02a55cb | -28.71041 | -55.63755 | 2025-08-31 04:57:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 3b3814c5-6789-3016-9e00-dcb4ad1eaa73 | -28.7226 | -55.62651 | 2025-08-31 04:57:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 1c0aff51-adf1-3b08-8d79-c8b0e8ad20d6 | -28.70922 | -55.64616 | 2025-08-31 04:57:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 6067b7d0-63a9-3d2a-aa4c-6e8daf617166 | -28.71169 | -55.60241 | 2025-08-31 04:57:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| e3cdc94c-4bc0-3c36-8f32-e1f3edf5eebc | -29.47063 | -51.33879 | 2025-08-31 04:57:00 | NOAA-20 | FELIZ | RIO GRANDE DO SUL | Brasil | 4308102 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b791a62e-b039-313e-8940-d7768884b78e | -28.90515 | -51.79231 | 2025-08-31 04:57:00 | NOAA-20 | FAGUNDES VARELA | RIO GRANDE DO SUL | Brasil | 4307864 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 046da1b0-b351-31e2-b9d6-307d5feb5419 | -28.71388 | -55.63818 | 2025-08-31 04:57:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| a13a400f-7833-3fac-a6d4-ef9a579e7248 | -9.4684 | -62.3286 | 2025-08-31 05:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9c0c8dbc-b307-3db9-90ac-18eb49477b95 | -6.1665 | -43.3273 | 2025-08-31 05:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 505ed3f6-a17a-3f40-99df-f3e52f0ee088 | -9.4498 | -62.3294 | 2025-08-31 05:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 6d4ffb29-045d-394e-bf51-466e75a9acc3 | -16.2225 | -52.6565 | 2025-08-31 05:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 752db0eb-0431-330e-952a-396ac166c780 | -9.4497 | -62.3485 | 2025-08-31 05:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 901dfda6-5257-3419-9ae4-0239aa6e9000 | -7.0951 | -44.3128 | 2025-08-31 05:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 244f1208-0911-3f60-b064-429f06034a3d | -9.4432 | -60.5692 | 2025-08-31 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| bea003fc-a4e8-33e5-90ec-b49e66441535 | -9.4495 | -62.3675 | 2025-08-31 05:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b2d19992-ec72-3e97-aeee-4f566b47ea63 | -11.8181 | -46.4314 | 2025-08-31 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| bc1f1bc5-50e3-3c11-b2f9-b4242fc5e851 | -9.4683 | -62.3476 | 2025-08-31 05:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| b7d81e3f-3feb-3d6d-a13b-08ab06280e17 | -11.8373 | -46.4287 | 2025-08-31 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| c135173b-d7e3-3e28-b55e-48a359c23d3e | -9.4683 | -62.3476 | 2025-08-31 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 7ba2b25b-8b6c-3d24-9397-0458a130ebc6 | -9.4432 | -60.5692 | 2025-08-31 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 455ac1e5-44bf-383e-a47d-b6436dbc6d78 | -15.7102 | -48.9479 | 2025-08-31 05:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 18c667e7-ef70-380e-8460-7c3f0133f557 | -9.4498 | -62.3294 | 2025-08-31 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 15dfdfa6-b46a-3cf4-9b14-4799529be5cf | -11.8185 | -46.4087 | 2025-08-31 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| fb9f8255-291d-3cb2-8c8b-4e5d71626d50 | -6.1665 | -43.3273 | 2025-08-31 05:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 12d8cf8c-0c10-38b3-b568-a41080cc17a5 | -9.4497 | -62.3485 | 2025-08-31 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 8b608023-8399-3783-a6bd-4051aaecdf93 | -11.8181 | -46.4314 | 2025-08-31 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 8a0ba9bd-7ffc-3480-a1fc-ef36b7ab9cb2 | -9.4684 | -62.3286 | 2025-08-31 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ffd40f93-aa75-3dac-9eb3-16d8c11a1205 | -15.7294 | -48.9669 | 2025-08-31 05:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| f788e510-23d6-3812-92de-654ee3819a91 | -11.8177 | -46.4541 | 2025-08-31 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 9fa812d3-7e93-3979-95df-41fc9c0f3c08 | -15.7107 | -48.9255 | 2025-08-31 05:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| c8a4fbb7-ba20-3101-8208-6925e4f5d3de | -15.7098 | -48.9702 | 2025-08-31 05:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 42.3 |
| f0a268d0-c088-3534-abae-601be07c0489 | -15.7303 | -48.9223 | 2025-08-31 05:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 23ec58f4-6f4e-3536-9385-c6ab5a96b9d5 | -15.7298 | -48.9446 | 2025-08-31 05:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 6428ede8-9592-3a82-a7c0-00f9c4174fd3 | -11.3293 | -63.2681 | 2025-08-31 05:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 938bfef7-f5c5-3aef-8a86-85d17de14b3b | -9.0613 | -65.4542 | 2025-08-31 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 0220cd94-bbf3-3507-b93d-5d7ed5823dee | -15.7298 | -48.9446 | 2025-08-31 05:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 5fc2074b-b90a-3863-8c44-c752b161168a | -7.9265 | -63.0158 | 2025-08-31 05:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| bf58654b-1bc7-3bc6-8719-2bab1df4bf11 | -9.4495 | -62.3675 | 2025-08-31 05:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 70aae847-fc34-3d6c-903c-8b6432f2e19f | -11.8181 | -46.4314 | 2025-08-31 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| a1b13138-9696-3630-a6de-9a9311eff109 | -9.4432 | -60.5692 | 2025-08-31 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 306f60b1-3909-3d09-86d6-cac697461083 | -11.3293 | -63.2681 | 2025-08-31 05:20:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| fcf07308-d24e-3a53-9432-46405211243e | -11.8177 | -46.4541 | 2025-08-31 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| d72df893-94a0-3566-9b57-b89d19d1a33c | -15.7102 | -48.9479 | 2025-08-31 05:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 82d30c06-6c64-345b-9f42-b74ced6427e3 | -9.4683 | -62.3476 | 2025-08-31 05:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 537d2d2b-e39d-3439-a3e4-25b774418342 | -9.4497 | -62.3485 | 2025-08-31 05:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 2766c656-ec04-39a2-aecf-1726d0923535 | -9.0614 | -65.4355 | 2025-08-31 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| f671d238-c254-322e-8054-0888f3da802d | -6.1665 | -43.3273 | 2025-08-31 05:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| a942d985-8713-32f6-b620-91f935759009 | -9.4432 | -60.5692 | 2025-08-31 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 06884dc6-dade-3f10-8871-f5d0fc0a9e4e | -9.4497 | -62.3485 | 2025-08-31 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 8074d4ed-a3ca-3a23-bdc4-a9b3d2f88827 | -9.4495 | -62.3675 | 2025-08-31 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 2ead50fe-d46b-3f5d-bb9c-cc1e6ba31deb | -11.8177 | -46.4541 | 2025-08-31 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| b639c900-1efd-378f-9dee-7f891453ef99 | -9.4683 | -62.3476 | 2025-08-31 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| b55bb867-f53c-32a8-a00d-b556fd64abca | -11.8181 | -46.4314 | 2025-08-31 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f10d8000-a657-30a6-8b8e-e7190cdbca82 | -7.9265 | -63.0158 | 2025-08-31 05:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 20e17ddb-9dd0-3297-b664-687e4942b5e8 | -11.8373 | -46.4287 | 2025-08-31 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 93ce572c-ecca-3a51-baa0-79f8754a5b7e | -11.3293 | -63.2681 | 2025-08-31 05:30:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 042091a0-0ee4-3aa8-88ea-f84c9163e548 | -11.8177 | -46.4541 | 2025-08-31 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 34c0e063-9c96-383a-9e48-285a037b3fc9 | -9.4495 | -62.3675 | 2025-08-31 05:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5a3b0daf-4645-3fe7-b6b0-34f7e3cf227c | -11.3293 | -63.2681 | 2025-08-31 05:40:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f361b9dd-d301-3282-ab51-099750306eae | -9.4497 | -62.3485 | 2025-08-31 05:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 72f03918-c532-3e4d-abfe-408ea5d6b89b | -9.4683 | -62.3476 | 2025-08-31 05:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 82823831-ad2b-3ac5-90e9-7e37e5794975 | -9.4432 | -60.5692 | 2025-08-31 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c5419f24-6c59-3f00-a61b-20757e621d32 | -11.3504 | -43.637 | 2025-08-31 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 782ff87f-576c-3841-981b-0efbc8d670d3 | -11.8181 | -46.4314 | 2025-08-31 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 0ecd543c-498e-3c1d-9cb2-0122373ec1f5 | -7.9265 | -63.0158 | 2025-08-31 05:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 466d2f2c-a8f5-3889-a5d9-8ec7e17e01db | -15.7102 | -48.9479 | 2025-08-31 05:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 38.9 |
| b20033f1-8331-30cd-bc86-7ce9a892f2da | -6.90846 | -62.94265 | 2025-08-31 05:42:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f75f9125-1bb6-3a9f-9003-85c9668e2237 | -6.90906 | -62.93871 | 2025-08-31 05:42:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f3421e9-4fc1-358d-926a-3e561abf5920 | -6.8956 | -62.93262 | 2025-08-31 05:42:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de1a6fb9-e5dd-336a-99fd-87417e86fe89 | -3.38739 | -59.45766 | 2025-08-31 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d16fcb0c-30af-3590-9b71-4cff62a49ceb | -6.98895 | -63.01007 | 2025-08-31 05:42:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 416b2e9a-fd5b-3b2f-ab18-50b138cd284f | -8.23264 | -70.46895 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c659d97d-9535-3757-8663-4f5099dc19bd | -8.67415 | -62.42902 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b681a62-817e-30a4-86b4-0c0daaaefc42 | -9.45161 | -60.56496 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2175cb45-3009-36b3-a185-6668f008fe2e | -8.38618 | -70.83181 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd8e1fc2-1990-3869-be75-c90b0a591cd5 | -7.20723 | -69.89824 | 2025-08-31 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4be26413-cefd-3f76-b70e-8a7e07586190 | -8.69818 | -62.87904 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c79f340-2d9d-33a9-908e-a4bec5eb853b | -7.92665 | -63.00939 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 167e2eb5-90c9-3e0a-bf68-fa05b9a0f254 | -15.22071 | -56.05815 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 898f51cb-c39c-3fdf-ba53-6e65bc2c4af3 | -10.2457 | -54.97311 | 2025-08-31 05:44:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 269e3c47-837e-3fa0-a55c-2d4316a926b5 | -9.43159 | -62.33295 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35b92110-0b5e-3ec8-8999-9b3c2d1609c1 | -8.74087 | -62.38529 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84430534-e7e1-3560-9986-96c15dd6be60 | -7.92251 | -63.01287 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6452de8f-978b-3029-b2da-6cee4bef1c4b | -9.43532 | -62.33351 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f022fc83-b5e8-300f-98b3-723a603d707a | -8.43271 | -62.29532 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a49f23c-e69e-38da-b1f6-a60fd7072ce7 | -9.45266 | -60.55737 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bffbae93-88d0-34c9-aec8-9f7d2355d07c | -8.74588 | -62.37702 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afc007cc-b448-3016-a21e-791682f67c89 | -7.56585 | -63.41094 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 069dd870-bf94-326c-afda-f19e8a0998a7 | -9.06907 | -65.42487 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a06b319-ecde-34c1-ad9c-c569899b18b0 | -8.79531 | -71.02142 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40cd7553-0bdc-3489-9235-f4a5df30a228 | -13.00986 | -56.9041 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37e8275b-f553-3b40-af59-3dd778fcc2e8 | -9.17489 | -67.73032 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README73.md)
