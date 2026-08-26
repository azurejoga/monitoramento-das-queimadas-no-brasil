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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bea8b1f-5ec0-35c5-8aa0-650b74c5be24 | -10.42532 | -61.21986 | 2026-08-26 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54cd6e47-8c0b-3e5a-ac9e-14db60858356 | -10.62018 | -67.92705 | 2026-08-26 05:50:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a7d439b-7c6c-3ccf-a24a-9fbe97454098 | -10.76282 | -54.04368 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 935133ae-3d3c-30af-ac14-feb907b1a339 | -11.15687 | -54.00753 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58f5a56e-83e9-33b4-b4fc-c9b1cbcc7010 | -11.74146 | -54.53189 | 2026-08-26 05:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e7c758f-ba59-3e28-8bda-24d9de6ff7d3 | -10.77154 | -54.03803 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 8d013bf3-9924-34c2-990e-1c61ae99001e | -12.0901 | -64.24238 | 2026-08-26 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6ed26ff-638e-37db-9b63-40059e3635f2 | -10.75978 | -54.02496 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a235bb07-b1ba-36f5-91df-91f063875d9f | -11.16349 | -54.0083 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8e26ab6-18d6-3783-98b4-ea4601b392ea | -11.74727 | -54.53809 | 2026-08-26 05:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5ea2e3eb-5b71-3a39-ac61-9bbb6d67dcd4 | -10.98517 | -60.79091 | 2026-08-26 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd383dc0-314e-375c-8d21-76532e77de8b | -11.16418 | -54.00245 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ba3e029-ec00-36d9-bb8b-2da0264833d6 | -10.42939 | -61.22045 | 2026-08-26 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd41c70c-662f-37dc-b994-d91adf344cd8 | -10.00489 | -67.56974 | 2026-08-26 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e31bb09-508f-3ed7-8c10-318188e993ee | -9.4817 | -63.27916 | 2026-08-26 05:50:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1e00e23-dc6f-3979-9c81-89d0acb3b3af | -10.64675 | -57.24722 | 2026-08-26 05:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7415b7f1-8ce5-3281-9cbb-0a78148e10be | -11.76126 | -54.53568 | 2026-08-26 05:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01545a9d-6c13-38b4-a193-a3ead1c277c4 | -10.98866 | -60.79628 | 2026-08-26 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 068e844d-7d85-33a0-810e-d6e026d13060 | -10.76413 | -54.03218 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6e8d605d-f8df-3cb4-974f-cfe1acb97b12 | -10.76389 | -53.9909 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95fa7af1-0aea-3b17-ae00-463ce2f938dd | -11.76834 | -54.53088 | 2026-08-26 05:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 335b0f07-f9b7-3608-b906-071db3b223a2 | -10.77223 | -54.03231 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 05a866b2-9170-3273-84ed-5f04b53c6781 | -10.76496 | -54.03728 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1303a8e0-dc11-37bf-bbc6-45973a43dfd6 | -13.85888 | -54.05146 | 2026-08-26 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c842d933-ae6e-3fab-b37b-24ca0969d1d9 | -13.87549 | -54.08998 | 2026-08-26 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c789e9aa-cc89-31a0-b9b4-d2d312f02f5a | -10.42991 | -61.21677 | 2026-08-26 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dbee8d8-5c68-30e5-bac9-3aacbb8f5933 | -10.06835 | -60.50357 | 2026-08-26 05:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef4eaaf4-2ca0-3fb9-9446-816a13cf7812 | -9.1901 | -66.995 | 2026-08-26 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bb76806-6df0-359e-b8bf-d3a76e05331c | -10.76635 | -54.02583 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 393ea84a-651f-38fe-a376-3fc0b88b4394 | -15.68042 | -56.29717 | 2026-08-26 05:50:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b00878c6-204b-340b-a8c8-0e10ff9be1e8 | -10.43346 | -61.221 | 2026-08-26 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4278c288-5463-3f88-9dec-a12487b02ef6 | -10.7707 | -54.03307 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bffe215c-0400-39a2-be4c-6e44de4f6036 | -10.7584 | -54.0364 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f6dcd54b-0a43-396b-987e-78dc929c5c75 | -15.67435 | -56.29653 | 2026-08-26 05:50:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 95a8f2f1-bc39-3729-9def-a147a2d19aaf | -9.91083 | -63.05763 | 2026-08-26 05:50:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae47700d-209c-302a-ba9c-4907e056ca90 | -10.98887 | -60.79531 | 2026-08-26 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bc0c169-2d4d-3e49-bf7a-ba0d3827f710 | -11.76792 | -54.52958 | 2026-08-26 05:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2236ea5f-834e-325a-b5ff-43c66eecd574 | -10.76542 | -54.02094 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eda3ef6e-a544-300a-a508-683180282bf6 | -12.08189 | -64.24926 | 2026-08-26 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6543f80-86bc-385b-a385-25f223ab9774 | -12.08719 | -64.23787 | 2026-08-26 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cd150f0-3690-36a6-8166-5acf1a3a1e5e | -12.07897 | -64.24477 | 2026-08-26 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 812bfc90-7db3-35dd-9865-0ecab34482c1 | -10.76458 | -53.98519 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdc3d6a7-e8af-3121-85ab-28b9fbb14684 | -10.76427 | -54.04296 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 6133c054-93e7-3bd2-b432-ff4e4202d105 | -11.76187 | -54.53019 | 2026-08-26 05:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70715da5-5f8e-3dd3-9f69-7324f0e5fa36 | -10.98921 | -60.79242 | 2026-08-26 05:50:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e49ddead-d575-37ff-940a-32f81cdb4117 | -11.76145 | -54.52892 | 2026-08-26 05:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 714e0157-8abd-3c62-8a6b-fd4a32003d7d | -11.15825 | -53.99576 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f0296ca-2d95-3399-a491-6a5b029d2603 | -13.86022 | -54.03849 | 2026-08-26 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59a5f1ad-6a4a-3fae-8c6b-614a38446bba | -11.74791 | -54.53269 | 2026-08-26 05:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c23791a6-8092-3bd2-a7c6-fd2027683869 | -11.7608 | -54.53439 | 2026-08-26 05:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0160a541-b4d0-3cef-bcc9-34061a54aa11 | -10.75321 | -54.02408 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e22a3477-68c4-3ce3-9067-912f811b9a63 | -10.9894 | -60.79145 | 2026-08-26 05:50:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 695500f2-5761-3f88-bca9-81f463dca6b0 | -10.64633 | -57.25053 | 2026-08-26 05:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9755e3c9-2e03-3b78-acb8-2d0f0ee7d950 | -10.76566 | -54.03149 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 4e9ce741-f414-3f71-93d2-5d688bcb9d10 | -6.6409 | -58.5181 | 2026-08-26 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| cf7eff1e-7ab5-38a1-9b4e-2c8bd2ee7735 | -13.2842 | -51.4541 | 2026-08-26 06:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 38254eb8-5986-3364-997c-db7dcbee4400 | -13.3034 | -51.4517 | 2026-08-26 06:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 216a9b99-fabe-35d7-a9cb-b4b16dfff153 | -7.5289 | -61.3825 | 2026-08-26 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 129.8 |
| e5bc7ddf-296c-39b0-91af-942e1af09619 | -13.3031 | -51.4731 | 2026-08-26 06:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 7aba245f-7ddd-3e5a-8995-655cd3ea9a96 | -9.6024 | -55.1078 | 2026-08-26 06:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 6f8771af-e470-3c48-a0c9-7c1e62c54640 | -10.7596 | -54.0384 | 2026-08-26 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b1dbc3f4-8a80-3e06-a155-52e576d7854c | -7.5104 | -61.3832 | 2026-08-26 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b90b61ef-7d4a-384e-878f-5c44bfeae4cf | -7.5288 | -61.4015 | 2026-08-26 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 12530976-2789-31de-9ee5-60549141c7b9 | -10.7784 | -54.0368 | 2026-08-26 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 29b9ccaa-7e8d-3e3c-85bb-5903cca4689a | -6.641 | -58.4987 | 2026-08-26 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ed475c69-eeb5-3710-b519-47148e6c1a36 | -6.2676 | -53.3768 | 2026-08-26 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d48da3b3-a99a-3a91-8a79-a222b5ac6c0f | -13.3034 | -51.4517 | 2026-08-26 06:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 252.4 |
| 5a1de38a-518f-366a-a81e-365bacc0f961 | -13.1711 | -51.3404 | 2026-08-26 06:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 7f5448af-a626-3682-a728-0a2c2a855225 | -6.641 | -58.4987 | 2026-08-26 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 06a747fa-f710-342e-8003-75d62a00fa03 | -6.2676 | -53.3768 | 2026-08-26 06:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 5570a12d-be49-37e7-ad50-ad11cc42b7f6 | -10.7596 | -54.0384 | 2026-08-26 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 029b5c68-b69d-3d03-851f-ed07d7e4645a | -13.2842 | -51.4541 | 2026-08-26 06:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 3692bd15-813b-3986-8bc1-f72caad07f91 | -13.1903 | -51.338 | 2026-08-26 06:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 200.4 |
| b807ab0c-3cdd-349a-a3b0-076c983373cc | -7.5104 | -61.3832 | 2026-08-26 06:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e2e389a1-ea7a-30b2-babf-e3beabb7e3e1 | -7.5289 | -61.3825 | 2026-08-26 06:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 4b9a09c3-2faa-343c-86af-694573b1605b | -13.3031 | -51.4731 | 2026-08-26 06:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 61d33bbb-e838-3493-8d97-6c123200cbf7 | -9.6024 | -55.1078 | 2026-08-26 06:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 081b04c9-de45-3793-aa96-bf6c848928df | -6.6409 | -58.5181 | 2026-08-26 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 35a74f86-b39e-3570-b32c-ceb1bf3915cd | -13.1906 | -51.3166 | 2026-08-26 06:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| dcc77b36-4e35-36b2-bdd0-5e70c40f3579 | -13.26 | -51.42 | 2026-08-26 06:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d74aa5c-8309-3cde-a36b-b88322f2e133 | -13.23 | -51.35 | 2026-08-26 06:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43ae1efe-5255-31c7-9f57-61194768bfc4 | -13.26 | -51.37 | 2026-08-26 06:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bbaae198-bf8d-3e33-b355-aa994690cc2d | -13.2472 | -51.3735 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 264.1 |
| 3f576a53-6031-34db-814d-36c1398e9c32 | -13.1903 | -51.338 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| bf30e7d1-e78e-3227-b52f-83b8cd6a4c5f | -7.5289 | -61.3825 | 2026-08-26 06:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 4e416f27-5748-3e3f-98fe-1321f8911b41 | -13.3034 | -51.4517 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 198.9 |
| c2d6e0c8-4bcc-3cc9-ba19-591e2090d936 | -6.641 | -58.4987 | 2026-08-26 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 681dab76-1872-33f9-8803-729375045d84 | -7.5104 | -61.3832 | 2026-08-26 06:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 5167de11-48f5-327c-8040-2c5125d9a4c1 | -13.228 | -51.3759 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| a91a4cfd-adf0-306d-a56b-72c6cbe999fd | -13.2664 | -51.3711 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 190.2 |
| f3e3da51-5cdc-3625-b1b0-c87c96efedd8 | -10.7596 | -54.0384 | 2026-08-26 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0f8f8c40-3a1c-3f2d-a956-ca44d33d4aae | -13.2668 | -51.3497 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.4 |
| b7fe4560-83b9-3013-b8ad-434b6ba7c273 | -9.6024 | -55.1078 | 2026-08-26 06:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| e22eaa80-3259-3f1f-ae37-da6d10fcfd26 | -12.6644 | -48.4142 | 2026-08-26 06:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6f8d9ba0-70fb-38a9-9cd2-7e7c4997d582 | -13.2842 | -51.4541 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 9acdfd6e-1ded-3228-9b16-de2ed49c2cab | -13.3038 | -51.4304 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 89c3f67a-756c-3451-8fc9-9a3999e9cc20 | -6.6409 | -58.5181 | 2026-08-26 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 71ec98a1-cbae-302b-890c-3a9ea45930be | -13.2284 | -51.3545 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 18414ccf-45b7-3983-8086-7dcc2072c846 | -10.7784 | -54.0368 | 2026-08-26 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 160e1ed6-6ba7-3fa7-874d-7e07e6380643 | -13.1906 | -51.3166 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |


[Clique aqui para ver as próximas entradas](README74.md)
