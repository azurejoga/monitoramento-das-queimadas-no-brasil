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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04e1f833-0cea-3104-9f43-c2cbc01bfeca | -1.8059 | -54.4723 | 2026-01-31 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 21140f76-3509-36f1-833d-73e860199758 | -9.9106 | -36.3175 | 2026-01-31 00:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.5 |
| f3fdcd53-c758-372f-a6b5-0e3d82ae4b69 | -20.298 | -57.3463 | 2026-01-31 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 1e576e17-0a39-34e2-81c8-6d67509f0391 | -20.3178 | -57.3644 | 2026-01-31 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| a33bc0cc-664c-343f-b099-d7ad6fd0cfa2 | -9.9299 | -36.3141 | 2026-01-31 00:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 116.5 |
| 96ff5fe2-828e-37fc-b2c5-01621ece42fe | -1.8058 | -54.4923 | 2026-01-31 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 175.5 |
| 3bb55c70-442e-3d57-b678-b4cbd22b40e5 | -20.2976 | -57.3672 | 2026-01-31 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 3dc0ac05-c7d8-33b7-abad-53e163165fcd | -20.2976 | -57.3672 | 2026-01-31 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 3ffea055-6df2-3a5c-b90c-d7bc9c0d9147 | -20.3178 | -57.3644 | 2026-01-31 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| f46dcf77-3820-350c-bb43-1e9e1b6e5ed6 | -1.8058 | -54.4923 | 2026-01-31 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 166.9 |
| 6d97f18a-5758-3ec7-bea0-af1dceca0419 | -20.298 | -57.3463 | 2026-01-31 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 56.4 |
| eb3104e6-9ddc-3981-8957-31dec998decd | -1.8059 | -54.4723 | 2026-01-31 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e6bdafca-39f5-37ef-9a16-85696542b2fe | -1.8058 | -54.5122 | 2026-01-31 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0b48bd6c-b791-3200-94e2-27972c359284 | -20.2976 | -57.3672 | 2026-01-31 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 040a7850-6a34-3d71-ae62-38e9cb697f74 | -1.8058 | -54.4923 | 2026-01-31 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 6218fb76-fa46-31ca-8185-af189584f847 | -20.298 | -57.3463 | 2026-01-31 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 6349606e-ecc9-388a-83b5-125ea90b69ee | -20.3178 | -57.3644 | 2026-01-31 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 804e47ff-a342-3d37-89bd-2ecface2ca8f | -1.8059 | -54.4723 | 2026-01-31 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 6ad948aa-4f5a-3d5f-8e0c-5ea0e640a921 | -1.7875 | -54.4925 | 2026-01-31 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 9e44372c-223d-3a69-8761-64f7829dd7c4 | -1.8058 | -54.4923 | 2026-01-31 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 153.8 |
| cfc876ee-377f-36dd-a4fd-9dc509dfb5f7 | -20.3182 | -57.3434 | 2026-01-31 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.1 |
| e327c3ca-9eb0-30bf-99f2-062d04b6962e | -1.8059 | -54.4723 | 2026-01-31 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5745fa2c-a644-3584-b04a-7d706251f377 | -20.298 | -57.3463 | 2026-01-31 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 1a1fb66e-821b-3645-a403-edc7ca41ac8e | -20.2976 | -57.3672 | 2026-01-31 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| d30a30f9-29f2-3d7a-9fe2-0f77fd906e04 | -20.3178 | -57.3644 | 2026-01-31 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.4 |
| ce271bd1-48bf-36a0-bedd-3db7d75a0a8b | -10.1435 | -36.222 | 2026-01-31 00:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 155.8 |
| d09053e8-5f8a-3aea-a2d1-c8c6e2125402 | -20.3182 | -57.3434 | 2026-01-31 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.6 |
| f1af7e32-62b6-34c4-bd29-ed8c8e5a77ab | -1.8059 | -54.4723 | 2026-01-31 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 224f7b27-0871-336b-9a4b-c9b49646cd7e | -1.8058 | -54.4923 | 2026-01-31 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 163.5 |
| dff69c86-9f46-3cab-9abf-cceef2cd5b7d | -20.3178 | -57.3644 | 2026-01-31 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 80b07896-88b8-30d2-8e28-a6fbd61bef7a | -10.144 | -36.1949 | 2026-01-31 00:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 139.8 |
| 66ac4869-4ebb-3309-bf8a-40f1107bbeef | -20.2976 | -57.3672 | 2026-01-31 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| b4a3ea05-4258-38d3-8d94-775b0e672d3f | -22.02513 | -49.49833 | 2026-01-31 00:43:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| a8c58048-f038-3f4b-9a46-fdfb2802fa3f | -22.0269 | -49.50964 | 2026-01-31 00:43:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 66fe39a6-fc85-35c4-9eca-bf107b0b054c | -20.2993 | -57.3692 | 2026-01-31 00:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.7 |
| f1727fc5-d25f-32f7-8ba3-6d7e4cf86cfc | -19.47271 | -55.47439 | 2026-01-31 00:45:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 771245e3-cab4-383d-9432-9cd961d74d7a | -20.31015 | -57.36781 | 2026-01-31 00:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 7a034a07-7482-3bc2-b76d-068cdbc35aa6 | -21.96284 | -53.6918 | 2026-01-31 00:45:00 | TERRA_M-M | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b49dd470-7818-3a99-a94b-5c729541bf98 | -20.29767 | -57.35472 | 2026-01-31 00:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b29a2d45-3b13-3f7e-aaeb-7bf88730c8b5 | -20.2728 | -57.32864 | 2026-01-31 00:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2e2e381b-6507-3276-a8b6-47433af129f7 | -19.47135 | -55.46359 | 2026-01-31 00:45:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.4 |
| eb303947-99ba-344e-8421-ee56daf857da | -20.26831 | -57.32091 | 2026-01-31 00:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c9f6a50f-db54-347e-9755-661eac9a1011 | -19.43731 | -54.77176 | 2026-01-31 00:45:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d411b3c8-f803-3b41-bd71-cdc136f67cac | -20.26198 | -57.33004 | 2026-01-31 00:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 45ce0477-d9ed-3246-a1c9-72675ceeaa2f | -20.32101 | -57.36642 | 2026-01-31 00:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| f311b8c5-c434-3aa2-b788-a1e00cbf622c | -20.26999 | -57.33528 | 2026-01-31 00:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 1a930e62-d0d0-347e-9e7d-ddba06c8daa8 | -11.1806 | -55.91731 | 2026-01-31 00:47:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 476545d7-e206-3cc6-9d10-3b1585d23d83 | -12.29966 | -57.40532 | 2026-01-31 00:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 394993d8-e5a2-32cb-a3e7-b06d1a3eaa76 | -17.98044 | -53.69759 | 2026-01-31 00:47:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7ef6ace4-572f-3f6b-8e5a-28164d4fda17 | -1.81105 | -54.48238 | 2026-01-31 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 1d5220e8-663a-3b77-bd2a-9f1ffc30a672 | -1.61423 | -54.7117 | 2026-01-31 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 895c405c-69d4-3b21-bbfe-922ae1514aff | -2.58269 | -54.7269 | 2026-01-31 00:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7aa87992-e44e-31ba-8a3a-66f044e0d159 | -1.80164 | -54.48374 | 2026-01-31 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2ea8d776-269d-3e19-9d84-da7fea07604b | -2.81466 | -52.95864 | 2026-01-31 00:49:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 242af31e-9c8a-329a-9155-03ee4d67fab2 | -1.80447 | -54.50384 | 2026-01-31 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d0881d18-6b02-343e-a925-4445df48f61e | -1.81246 | -54.49247 | 2026-01-31 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| a558caa2-2bb6-3db8-8c29-e49b2ad6534d | -1.87754 | -54.68637 | 2026-01-31 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 98939683-b5fc-379d-839a-e59bf36f7a99 | -1.80305 | -54.49378 | 2026-01-31 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| f93e46cd-2095-3949-8901-57fff8052516 | -1.6867 | -54.77581 | 2026-01-31 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ce535495-8cb3-3fba-a265-053c067bdc7d | -1.8058 | -54.4923 | 2026-01-31 00:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 0ba9cca7-2d41-36f5-8520-34584466f970 | -20.2976 | -57.3672 | 2026-01-31 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.2 |
| b34fae3f-c716-3a17-9d61-f34311f01d84 | -20.3178 | -57.3644 | 2026-01-31 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.7 |
| bb17ce8e-1691-3f41-b4b2-f8475720c018 | -1.7875 | -54.4925 | 2026-01-31 00:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 1c2e446b-731b-3b1c-98b6-93b02ca94faa | 2.3208 | -60.93865 | 2026-01-31 00:52:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 40ef842c-fc12-3f73-a8b7-d5e82836dbbc | 1.83411 | -60.83292 | 2026-01-31 00:52:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| dbb2c28b-ad98-36d1-b835-1041a9ced266 | 1.8325 | -60.84448 | 2026-01-31 00:52:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 40eac2c2-194f-31a8-9f00-e0816f639904 | -1.8059 | -54.4723 | 2026-01-31 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 1493296c-bc4d-36b9-b7fd-db871f5993bd | -1.8058 | -54.4923 | 2026-01-31 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 157.1 |
| e0487d69-51f7-3f4d-89e8-0cefd18b662c | -1.7875 | -54.4925 | 2026-01-31 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 541ef680-1b85-3cd4-a0b3-1040dc416a02 | -20.3178 | -57.3644 | 2026-01-31 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.3 |
| b7eb1e2d-a881-31c8-b9b5-b9b7bb1966e2 | -1.8059 | -54.4723 | 2026-01-31 01:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| eb75387a-cf6a-3105-b8fd-ce8b94775457 | -1.8058 | -54.4923 | 2026-01-31 01:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 146.5 |
| cf4f7e99-fa4c-3b6a-933c-b1daefdb82ef | -20.3178 | -57.3644 | 2026-01-31 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 2177b152-3d70-3805-85cd-cb5b285768a9 | -1.8059 | -54.4723 | 2026-01-31 01:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0d596b0a-7b95-3931-85de-b63371e26660 | -1.8058 | -54.4923 | 2026-01-31 01:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 159.3 |
| d1464b6e-907a-390e-adf9-0675cb7a5be1 | -1.8058 | -54.4923 | 2026-01-31 01:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 6b37fb5b-9a31-325d-b693-0e2d0bd6f744 | -11.9961 | -50.7777 | 2026-01-31 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 24d529eb-dc54-311b-bac8-f64bbbbb9495 | -1.8059 | -54.4723 | 2026-01-31 01:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| bc36f615-7078-37df-91ee-29ad311c3722 | -20.3178 | -57.3644 | 2026-01-31 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.1 |
| a7317589-22f6-3ce5-b71c-01990ef969b5 | -1.8058 | -54.4923 | 2026-01-31 01:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 3bf62c17-4df1-3557-a926-1d2196f8d809 | -11.9961 | -50.7777 | 2026-01-31 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 118c6306-7687-3637-9910-de3793592120 | -1.8242 | -54.492 | 2026-01-31 01:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1940f83f-ad2b-3d3f-8f37-d0cb528a42d7 | -1.7875 | -54.4925 | 2026-01-31 01:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 09588570-116f-3f95-98d2-7a64bd498af6 | -1.7875 | -54.4925 | 2026-01-31 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 06d0e070-cba4-3914-964b-5b23bfa2fe40 | -1.8058 | -54.4923 | 2026-01-31 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 52000aa1-4e6c-39be-9a3d-0652ea97dcb0 | -1.8059 | -54.4723 | 2026-01-31 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 7605a8c4-60da-3ae2-914b-d9b6a618581c | -11.9961 | -50.7777 | 2026-01-31 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4e6511d3-bd4d-3432-a5c3-a5ab230dbebf | -1.8058 | -54.4923 | 2026-01-31 02:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 7212d381-ed83-36fc-9e2a-3e0184058275 | -1.8059 | -54.4723 | 2026-01-31 02:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 610510e5-204a-31f7-b6fa-de3c472038df | -1.8058 | -54.4923 | 2026-01-31 02:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 8d298984-86dd-3494-b2a6-501321d83bcc | -20.3178 | -57.3644 | 2026-01-31 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.7 |
| 44d28522-af9c-3264-8b3e-c995f51982b9 | -1.8059 | -54.4723 | 2026-01-31 02:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| c13cc47c-6edc-36ee-ab1b-90a1abb7db41 | -1.8058 | -54.4923 | 2026-01-31 02:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 068c78f8-7ac4-3f7e-a938-38edb37f6f6d | -11.9774 | -50.7585 | 2026-01-31 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| d35d0321-16a4-3ef4-bb99-5ec0b1851826 | -1.8058 | -54.4923 | 2026-01-31 02:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a65b88b4-930d-3bf7-a0df-3464d9941634 | -1.8058 | -54.4923 | 2026-01-31 02:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| dd79b6bf-0300-3631-b608-c52eb0352525 | -1.8058 | -54.4923 | 2026-01-31 02:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| e61e08ee-021b-3fbc-9b52-398f877974c9 | -7.38342 | -35.68735 | 2026-01-31 02:53:00 | NOAA-21 | ITATUBA | PARAÍBA | Brasil | 2507200 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 36ac97c8-626e-329b-b2d0-988e291f7b33 | -7.38231 | -35.69325 | 2026-01-31 02:53:00 | NOAA-21 | ITATUBA | PARAÍBA | Brasil | 2507200 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6ba33615-b262-353a-a1a3-8078edde0921 | -8.46714 | -35.31714 | 2026-01-31 02:53:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |


[Clique aqui para ver as próximas entradas](README2.md)
