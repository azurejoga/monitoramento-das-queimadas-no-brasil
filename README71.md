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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 689977aa-d5c0-3318-8323-2acc4ffcaeda | -11.06 | -52.5 | 2024-09-29 06:04:23 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76abdde3-d776-38e9-b303-b430a469dfd1 | -16.12943 | -55.43358 | 2024-09-29 06:05:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c5326783-87cf-300b-b1d2-d8355b21138b | -16.10614 | -57.51934 | 2024-09-29 06:05:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cbf4b9e9-7472-333a-a3b6-2f15e8e76b29 | -16.10477 | -57.5291 | 2024-09-29 06:05:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a23497a7-95cf-3347-9c9f-95dc05128b7a | -15.9502 | -57.19907 | 2024-09-29 06:05:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 67f00581-9307-3819-9fbe-bf9459e28431 | -15.94082 | -57.1979 | 2024-09-29 06:05:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a4e01fe0-8f9b-3ce6-bc17-0984456dd2e9 | -15.90332 | -57.19309 | 2024-09-29 06:05:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8171fc17-15c4-3d19-bcfe-00a5f1b61843 | -15.8219 | -57.39136 | 2024-09-29 06:05:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 78d96fe6-fe8d-32f1-9cc2-7fb247591f6a | -15.81839 | -57.34939 | 2024-09-29 06:05:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9dff97ac-e928-354a-8ff7-ce918a1dfea5 | -15.81689 | -57.35997 | 2024-09-29 06:05:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 30c805ea-6674-3f89-a8be-2f744a486072 | -15.80907 | -57.34832 | 2024-09-29 06:05:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d6640a4c-69ba-3e6b-a141-c01c96809432 | -15.78458 | -54.18237 | 2024-09-29 06:05:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9d772754-f277-3cb0-bdeb-3edeed9c4a36 | -15.77316 | -54.18093 | 2024-09-29 06:05:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 36.3 |
| dec2c0c0-b0f1-3940-b408-b229288e4328 | -15.61855 | -57.46021 | 2024-09-29 06:05:00 | AQUA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 613c0c8b-db8f-3c00-9f65-9e8f9aba36d4 | -15.61714 | -57.47012 | 2024-09-29 06:05:00 | AQUA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b7096723-42ba-32e5-adcb-b6ef4f022e19 | -15.60934 | -57.45884 | 2024-09-29 06:05:00 | AQUA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 31659bcb-c1dc-3da4-8780-ed25fb2733b0 | -15.60012 | -57.45749 | 2024-09-29 06:05:00 | AQUA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3b2cf795-af6e-3acc-b995-2acf1c545eca | -15.57891 | -57.47459 | 2024-09-29 06:05:00 | AQUA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a96ede1d-ae15-3d6b-8a45-0a1c9f1d601b | -14.88806 | -57.9877 | 2024-09-29 06:05:00 | AQUA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 26786ec3-71f1-3d53-ad69-8de03a108ac3 | -14.88667 | -57.99726 | 2024-09-29 06:05:00 | AQUA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dc8c1aa7-1e82-3a43-99fd-95dcf8e55605 | -12.9842 | -62.70207 | 2024-09-29 06:05:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 2a0187c0-8c23-3d1b-977f-0a289ec409e1 | -12.97835 | -62.70773 | 2024-09-29 06:05:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e672fe9c-d3f0-32d2-a163-83b4d95e06b4 | -12.85886 | -62.73592 | 2024-09-29 06:05:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 1c027428-15b5-345e-b77c-71f747a76b91 | -12.85668 | -62.74917 | 2024-09-29 06:05:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 9202cbc9-2198-3ba6-8d05-017d1540e9a0 | -12.8545 | -62.76245 | 2024-09-29 06:05:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2fe54243-d54b-3c48-8937-66dd056acc99 | -12.77758 | -62.60725 | 2024-09-29 06:05:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 245c41b0-2b31-35cb-a741-409a84f68397 | -12.76709 | -62.60541 | 2024-09-29 06:05:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 0ba927a1-1a4d-36ee-8f55-2a90858e644d | -11.65126 | -64.00416 | 2024-09-29 06:05:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6596240d-c302-39ca-a94d-f8804299069d | -11.60498 | -63.88455 | 2024-09-29 06:05:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1abcf940-af80-3b85-84d5-00143c22ad5c | -11.60208 | -63.90144 | 2024-09-29 06:05:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 5d1118d8-5cde-357e-b0c6-c6288593bbb9 | -11.59804 | -63.87782 | 2024-09-29 06:05:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c1df9b60-b4c4-3a08-a00d-27f975a52d7a | -11.59526 | -63.89475 | 2024-09-29 06:05:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 15431520-e485-3b23-ab42-561e88eacc4d | -11.59316 | -63.88246 | 2024-09-29 06:05:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 86163943-ccf3-397e-98c0-c7aade6f956b | -11.59052 | -63.70442 | 2024-09-29 06:05:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 23142146-3d14-3629-8222-96c7bda3dd23 | -11.58621 | -63.87586 | 2024-09-29 06:05:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 48f7a6f0-9eb3-3808-84fe-c8030996acca | -22.16628 | -56.02913 | 2024-09-29 06:08:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 20.6 |
| d548ebd8-c2c9-3096-a769-66b8509c2b7f | -22.16457 | -56.04369 | 2024-09-29 06:08:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 8f83ea10-581b-33c4-a0ae-e6088c0d05b4 | -22.16417 | -56.02362 | 2024-09-29 06:08:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d517c45f-da69-3a83-bd46-06e156795ecf | -22.16238 | -56.03814 | 2024-09-29 06:08:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 1e242f49-875e-38ad-8e1b-af7f2f486ad1 | -22.15526 | -56.02804 | 2024-09-29 06:08:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bb669128-2244-358e-8d2a-f519745599ba | -19.97854 | -55.49261 | 2024-09-29 06:08:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 752dc8e3-d460-3439-ab5a-62c646f93b30 | -19.97688 | -55.50627 | 2024-09-29 06:08:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1a3b4011-56e5-32db-99f5-17605cf01723 | -17.11982 | -56.20241 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 70022ca0-bf08-37ae-af98-e8b06630cf2b | -17.11825 | -56.21442 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 1bde41de-b84c-3982-be8b-335c36e9cf18 | -17.11444 | -56.16485 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 901e1bae-8cd2-3cbf-b351-24fbfce97621 | -17.11288 | -56.17694 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.7 |
| 5e329f8d-84fb-351b-86a4-206b8a1d5ad1 | -17.11132 | -56.18898 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| dfcfe34a-3b07-3464-902e-31dad4e2a3e6 | -17.10976 | -56.201 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| bd2eed04-cc66-3952-84ef-318aa5f24292 | -17.1082 | -56.21301 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 4250b318-43d7-3ecd-b0d2-6eb53eeef794 | -17.04956 | -56.73481 | 2024-09-29 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| b9b1d8ff-6995-386f-b010-e13f328f14fa | -17.02191 | -56.09594 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| e80a1515-d27e-3cec-8f7c-1eba9cd344eb | -17.01256 | -56.16852 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f4a30ba1-8cce-30aa-b758-52cbfe12d9d7 | -16.98627 | -56.13456 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 9797475c-7e47-39ce-b524-5a07a95694a7 | -16.98466 | -56.14661 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| e82fe803-d03d-3ddc-8952-b533c8cb2ff7 | -16.98306 | -56.15866 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 674d363e-19e1-3f43-8442-f8701b4564c7 | -16.98146 | -56.17065 | 2024-09-29 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 5a734b21-7ac6-3099-b2fa-431ac7c083d7 | -16.9508 | -57.93275 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| be6434be-eb1c-336f-9e6c-5ad3fc71792c | -16.94939 | -57.94258 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| d8a49065-eb07-3767-b321-ac7047281b28 | -16.94165 | -57.93139 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| a3f795fd-22c0-33bc-95a6-3b7398a42432 | -16.94024 | -57.94122 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 8de87ffe-0f07-318a-9ce8-f789662d4482 | -16.93464 | -57.98044 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 67a35c2b-78a8-33d4-9b76-783ecbafc66e | -16.92551 | -57.97907 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 69d43d56-640c-3409-9153-19bb935789c9 | -16.91777 | -57.96791 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5e002cab-5b1b-3c4f-8d4c-fb4815d9187f | -16.91638 | -57.9777 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| d462778e-8326-3ea7-823e-9a228a12bdc6 | -16.91002 | -57.95674 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.4 |
| f784dab2-8634-3108-abdd-c1145f7de2ca | -16.90863 | -57.96654 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.8 |
| 35ceda8b-656b-3120-a9d6-bc7ee6839552 | -16.90227 | -57.94556 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| a95a5157-c336-3ca2-9a14-751ca9e64267 | -16.8549 | -57.69912 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b49265fe-9c2b-37af-b6e8-16c9aaa436bb | -16.7039 | -57.53078 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| c0983952-d50e-32a4-83cf-8b86deb4dbe5 | -16.67802 | -57.444 | 2024-09-29 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 4258be30-00e9-3e47-8f87-81d2399a58e7 | -6.66979 | -69.9585 | 2024-09-29 06:29:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78f1d146-b789-3932-b4c0-3c16095eb3c9 | -6.66703 | -69.95378 | 2024-09-29 06:29:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| db9fed43-dec2-36b9-addb-661d356cc9db | -6.66646 | -69.94672 | 2024-09-29 06:29:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1849be7d-788a-309f-b86b-91161a11ef0e | -6.66627 | -69.95934 | 2024-09-29 06:29:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b392b6e3-d2b5-3912-96ac-bb9f6c57e482 | -6.66566 | -69.95227 | 2024-09-29 06:29:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7197d40-5801-3e83-a65f-7e6751569679 | -6.66486 | -69.95783 | 2024-09-29 06:29:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2866ffae-2146-3bb8-9c76-f91e6f53a4f8 | -6.66406 | -69.96338 | 2024-09-29 06:29:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a44419db-1014-3ef5-9d73-4718c00367c5 | -6.66361 | -69.94193 | 2024-09-29 06:29:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02063cdf-8c5b-30b2-8ed2-5a93356d0db0 | -6.66285 | -69.94752 | 2024-09-29 06:29:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62ce34be-f070-3f98-bbbd-bfc2bef15686 | -6.66152 | -69.94603 | 2024-09-29 06:29:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8467c809-b235-3e90-8698-647b8b5c7724 | -9.65993 | -68.5619 | 2024-09-29 06:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61b69681-42f6-316b-a783-a8b807f06df7 | -9.65944 | -68.56579 | 2024-09-29 06:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bd179e0-b17d-3aec-acf8-1e6eb4223ce8 | -9.44893 | -70.43877 | 2024-09-29 06:31:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92ce0631-5786-369d-8e46-b30996632af8 | -9.29755 | -65.34846 | 2024-09-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e76fc01d-af7d-3b86-b60a-7c6acfe637ad | -9.29683 | -65.35458 | 2024-09-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 09119098-59ef-36d6-91a6-a83cc40b969e | -9.15125 | -68.3771 | 2024-09-29 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a11bd12a-4669-39be-87ba-6d6e7a37b4be | -9.14867 | -68.37675 | 2024-09-29 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 670c9893-925e-38a9-a41f-fe473ddfd698 | -9.14815 | -68.38065 | 2024-09-29 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 203596ac-9e94-3640-9475-b9e4926bcced | -9.14508 | -68.3802 | 2024-09-29 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c04cec9-76d2-3d26-8f20-97cb30f20ae1 | -9.1118 | -67.89369 | 2024-09-29 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39d88654-21a2-3a82-bc5e-c33490940e20 | -9.10541 | -67.89711 | 2024-09-29 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8e67ea3-f5ed-3033-8aa4-3f0a4e5c824d | -9.06342 | -67.81579 | 2024-09-29 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb1cf00f-0dcd-35bb-bc29-a152134fdb6c | -9.06288 | -67.82001 | 2024-09-29 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59ad22de-bbe1-329b-b01e-51a4bd285603 | -9.05699 | -67.81927 | 2024-09-29 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1cfd93c-3075-3f5b-95a3-fd5f14e450ef | -8.1004 | -70.6396 | 2024-09-29 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2bde807-33c1-326d-af9d-77d387d605b1 | -8.08739 | -70.62716 | 2024-09-29 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2080574-d23d-3d1b-b776-768697cfe9d0 | -8.05079 | -70.57735 | 2024-09-29 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26bd3160-356b-3c0f-998a-75a48c9cfd87 | -8.01631 | -70.89309 | 2024-09-29 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0026e35-9f0e-37d8-88bf-25e05ae802de | -11.28794 | -65.28032 | 2024-09-29 06:31:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34392f45-3ec0-381f-b9bf-d895e7a486c0 | -10.11059 | -67.88928 | 2024-09-29 06:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README72.md)
