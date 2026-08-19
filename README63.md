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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 925df847-5401-3bd9-b834-f77d13eecfc1 | -19.75109 | -57.94311 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0363dda8-5644-3852-ae26-cc067eaf6f91 | -19.75743 | -57.9603 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a426222f-3f7f-35f5-ab6b-b70d7c225f36 | -19.75576 | -57.93969 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.2 |
| a231737c-2515-3a77-8351-fe29248d7bfc | -19.08033 | -57.35364 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8c1d1a5c-cc9d-3b92-a40f-5aa3c59bb3bd | -19.73538 | -57.93274 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2dfb9c99-4e49-3c3c-91d2-08d217b67b6f | -19.76728 | -57.94947 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| cfce4bde-f9bf-3895-9f00-75b87e31be11 | -19.74055 | -57.9253 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 332daea9-bfd0-3de8-b045-71c098a8785d | -19.73857 | -57.94134 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 49a932ec-d978-3128-a015-06ad48037bbf | -19.77203 | -57.9575 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 75ef39b7-90de-3adb-b144-3765942457fa | -19.05352 | -57.35856 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| c41404b7-7263-3522-97f1-f4b22a6a848c | -6.0912 | -57.9187 | 2026-08-19 05:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| ea517552-5b09-3711-aa4a-87566a6b0506 | -9.4256 | -60.4353 | 2026-08-19 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 061baa03-e03c-3105-a5a2-20861d76b49c | -9.08 | -65.4163 | 2026-08-19 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 01802fab-fad9-3c4d-bef8-63648a1acda5 | -8.5598 | -54.7579 | 2026-08-19 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| cb56d66a-fe07-358a-bb7e-15cc6454cd4b | -8.5785 | -54.7566 | 2026-08-19 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| f613430d-9b42-3947-8d97-e70cb82990cb | -5.9994 | -57.8639 | 2026-08-19 05:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| b541b05e-f426-3d2b-b062-50345fa470e4 | -5.9198 | -43.6264 | 2026-08-19 05:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 274f9d86-2711-3aee-beea-29c1c37363c0 | -14.8028 | -46.6683 | 2026-08-19 05:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 47.7 |
| c1146fe8-dcd5-3756-8a11-a0bea71c3e3d | -5.9011 | -43.6279 | 2026-08-19 05:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 92e547ab-8a36-39a9-9d4f-0ab3c3d69c81 | -8.56 | -54.7377 | 2026-08-19 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| beea0666-6535-31f2-b3f5-ec3f5cf614cc | -9.4254 | -60.4545 | 2026-08-19 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 81905c58-7dd5-37b1-8bb2-e96dc85b808b | -5.4317 | -48.4212 | 2026-08-19 05:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| b046ec49-8d73-38c6-82b6-3233f3972ec3 | -14.8033 | -46.6453 | 2026-08-19 05:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| f538256e-b6c5-3b9c-b9d5-fa108343f715 | -5.9198 | -43.6264 | 2026-08-19 05:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| d9e002bd-1e0f-34df-8c84-2e33cde24297 | -6.0912 | -57.9187 | 2026-08-19 05:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| dd115a5c-e22f-3d5f-ab81-02996c8b58e2 | -8.56 | -54.7377 | 2026-08-19 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ebe0fec7-1a42-322d-9298-1fc7577af52e | -19.784 | -57.958 | 2026-08-19 05:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 04dfc51d-e794-31e0-951f-b5d91ae881ff | -19.7639 | -57.9607 | 2026-08-19 05:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.6 |
| 5b4de598-6328-35e3-ba8b-49afcd1cd6fa | -8.5598 | -54.7579 | 2026-08-19 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 175698f4-fc62-3b37-af24-ac7b706448bd | -8.5787 | -54.7364 | 2026-08-19 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 78e9c93d-c3db-317c-a9e7-b030ff7d4da4 | -14.8033 | -46.6453 | 2026-08-19 05:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 192b79f2-bb78-3081-b200-1fe36f8155a8 | -8.5785 | -54.7566 | 2026-08-19 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 5e92dd3a-8a73-3c76-a179-1526e25ff259 | -19.7442 | -57.9425 | 2026-08-19 05:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.9 |
| 7eb82819-bea7-39b7-aadb-fb3021c426ca | -9.4256 | -60.4353 | 2026-08-19 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 5898712e-0d60-3ecf-a8d9-66ab4036ad23 | -19.7647 | -57.9191 | 2026-08-19 05:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.2 |
| aa07871d-3d38-3e47-8f02-1a4babe65a52 | -19.7643 | -57.9399 | 2026-08-19 05:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 282.6 |
| a590ff23-0a3e-34b0-a89e-18af1e75292f | -5.9994 | -57.8639 | 2026-08-19 05:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 5d3b2ccf-f61c-3f20-a77a-0eea5d9fc3ba | -5.4317 | -48.4212 | 2026-08-19 05:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 7d211137-8ca7-3ddf-ba9b-f9a930f0e31e | -19.7844 | -57.9372 | 2026-08-19 05:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.4 |
| 23dd0e6d-00da-3898-a409-30deda3d837a | -5.90065 | -43.64511 | 2026-08-19 05:46:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| ba321126-05f3-3689-bdb8-f8fe5e2f566f | -5.90733 | -43.60527 | 2026-08-19 05:46:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 157ba9e1-a606-3e53-aeca-7c7284f09f38 | -5.908 | -43.61345 | 2026-08-19 05:46:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 46d6c20f-9ec5-3b9b-b0db-1612907edff1 | -19.7643 | -57.9399 | 2026-08-19 05:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 205.7 |
| 958f7abf-c7f2-375c-9509-608e30339a06 | -19.7647 | -57.9191 | 2026-08-19 05:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| c3f65108-8789-366e-a2f9-e4adaa839fe8 | -14.8033 | -46.6453 | 2026-08-19 05:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 3d0ab9a8-05c3-303e-a10d-f973551f2c7d | -5.9994 | -57.8639 | 2026-08-19 05:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 40b88868-b3c4-3049-b817-de9d3cffccc5 | -14.8028 | -46.6683 | 2026-08-19 05:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 9ce54c24-8699-3ed4-9bfc-6e2c4649588b | -5.9011 | -43.6279 | 2026-08-19 05:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e963a100-a2f9-3176-adab-c65bf6c749af | -8.56 | -54.7377 | 2026-08-19 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 30ae4993-f8ff-3b73-a161-e1d991d7dc1d | -5.4317 | -48.4212 | 2026-08-19 05:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c6fcb97e-f192-345d-843d-b0b6ffc5b689 | -19.7442 | -57.9425 | 2026-08-19 05:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 29c10730-30be-3976-928e-8e940c935b28 | -19.7639 | -57.9607 | 2026-08-19 05:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 4549e235-4225-3410-a6ca-f74034a50772 | -8.5598 | -54.7579 | 2026-08-19 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 446eae5e-e59b-3895-8cab-b9682ace36c1 | -19.7844 | -57.9372 | 2026-08-19 05:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.8 |
| de6f6a2a-0809-3099-8500-f12627367848 | -8.5785 | -54.7566 | 2026-08-19 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 98f5ac54-a903-3c94-a235-28b215fd853e | -6.0912 | -57.9187 | 2026-08-19 05:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 4b8d6634-0f78-31a8-a83f-c8356ed9f077 | -5.9198 | -43.6264 | 2026-08-19 05:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 47914991-aa98-3d5d-8920-6920e4c1a6dc | -3.21992 | -61.25893 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 321fc94a-f19b-3a65-98c8-988e34327b86 | -3.0967 | -61.22232 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2aa3a0d-723b-3e4b-a415-682449390a94 | -3.1013 | -61.21938 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83e1356a-2694-302d-86a3-e734e3f04560 | -3.09832 | -61.21166 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e03d5de8-3a48-36fc-a920-648b79c26c3f | -3.10048 | -61.19741 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59e195ad-6bd1-32ae-8139-244f34c788cf | -3.09994 | -61.20097 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c26774d-1d2c-37bc-b899-7a3fc61839a9 | -2.08356 | -56.58816 | 2026-08-19 05:57:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5066664c-78f3-3fb3-9fdb-5f3573d66674 | -2.32592 | -60.06336 | 2026-08-19 05:57:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6de017e5-aa64-328b-93e5-3a5c69630b6d | -3.10346 | -61.20514 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f96368f9-e2df-35e2-b16c-e636137e4c68 | -3.22397 | -61.25956 | 2026-08-19 05:57:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47e94b98-f0d2-3591-89cb-cce7d09f99bf | 0.30867 | -60.44745 | 2026-08-19 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f31a824a-dfd5-3f03-99f2-7590776f76b5 | -3.0994 | -61.20455 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd29c5ba-8faa-3ca3-af28-06c4659c9601 | -3.10238 | -61.21227 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96bab9cf-313c-3911-90e2-88c390ecee31 | -2.07808 | -56.58729 | 2026-08-19 05:57:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 75c2dd1c-8c2a-3e19-97f0-b47181d18dd1 | -3.09696 | -61.19324 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e7aa8f1-f361-30ba-880c-c5641c90eb3e | 0.30462 | -60.44808 | 2026-08-19 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96f5ef62-5992-3b52-81bf-0b2d33a22f2d | -3.10535 | -61.22 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8326f7ac-5cf5-31f6-94b8-886c1b9de8df | -3.09724 | -61.21877 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0144112-1523-335d-ba7e-615a9349d8c9 | -3.1515 | -60.26614 | 2026-08-19 05:57:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ddedf94-37c2-36f0-8ecd-ab23f429268c | -3.15583 | -60.26678 | 2026-08-19 05:57:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07026f12-f6f2-35e9-b312-5721ef605f30 | -3.10076 | -61.22294 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d03ae04-dc72-3c7b-bdf4-88a7f952e6d4 | -3.09778 | -61.21521 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3681dd0c-dddd-3f8b-b4ab-cb803a3e79af | -3.10102 | -61.19384 | 2026-08-19 05:57:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c0a7371-b4ad-328c-8cc1-f09453c193a5 | -6.86185 | -59.0294 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e23bde9a-f87c-315d-a75b-5a95ce7b2998 | -9.4208 | -60.42504 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca76cb40-5904-3762-96e3-792c79c474e9 | -6.75594 | -59.16868 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b30a0250-1f2b-3741-a694-b210f9cc9574 | -5.49948 | -60.12797 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18ba3c82-3f93-3468-a936-6dc967bd6011 | -8.57891 | -54.721 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b454295a-2c42-3419-a93a-fd55d7202e36 | -6.13812 | -57.86517 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dcc6093-a0a3-3b97-a9c7-36d9be38b88b | -6.84236 | -58.99108 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f44f0dfd-060a-3531-a3f8-50e978965c5d | -9.39091 | -60.5607 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45755737-6199-3e47-a125-632f89692821 | -8.53836 | -54.74927 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 07f7985d-0882-30d5-a246-e42fdddeff23 | -8.5503 | -54.76294 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23d72e13-7572-38ea-bfc6-b9b8a82170cd | -6.0981 | -57.85992 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8b112ab-c5c0-33ed-a1b3-f359e6677be2 | -8.53758 | -54.75537 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d4b8a853-dc0c-3eeb-b2be-7843432eef57 | -8.57835 | -54.7052 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 162cdcc3-7781-3535-af96-a8eca8ea62a9 | -6.68278 | -59.07088 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8ebcd7c-8437-3e6b-9b4d-0de533d18913 | -8.57669 | -54.68323 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 481b3f99-767e-36e8-b49f-046323a4113e | -8.56914 | -54.68867 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 415ebc5e-43f4-3271-aad6-ef659ffea2e3 | -9.42618 | -60.42072 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83cd4d55-4578-3a9f-a9e4-79e507c48044 | -8.56464 | -54.72541 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08c09418-5bac-3dac-b2a8-1875029343f5 | -8.57395 | -54.68614 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b027ea74-5a9d-3b85-883f-928bf752e7bb | -9.42313 | -60.43439 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README64.md)
