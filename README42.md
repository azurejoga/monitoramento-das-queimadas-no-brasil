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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19fde029-7774-3eea-ba06-3a771b2e5f42 | -18.44885 | -42.61655 | 2025-10-07 04:10:00 | NOAA-21 | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 72a8a70e-f188-3528-9f35-28024ad29442 | -13.94867 | -48.1749 | 2025-10-07 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45e6b8cc-ed59-38f1-9abc-98b8dcde42d0 | -13.54205 | -42.99654 | 2025-10-07 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0307a303-c2b6-3df2-ad41-2dc4f8e7ef05 | -13.38169 | -48.04464 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92b3fb00-7861-3aa1-849a-6decc5a81d05 | -14.62424 | -43.8861 | 2025-10-07 04:10:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b3f3273d-38f1-3c84-96ea-abdcd1580b0d | -12.34828 | -47.05912 | 2025-10-07 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bed4704-0084-3ce5-bb90-757a122de69d | -14.15667 | -44.75781 | 2025-10-07 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f123d43-d052-3e4d-9aaf-54865a6ef6af | -14.30956 | -45.84852 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d824f8f1-3a33-391e-acb1-57990b5bf641 | -13.23493 | -47.24598 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a53a5d7-6e21-33f9-b02a-467ea3d986ec | -18.96932 | -47.82713 | 2025-10-07 04:10:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ae1a4c7-5346-37f0-8c0a-4a9f4386a033 | -15.36121 | -47.30301 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1f373fa8-a6c6-303b-976c-9f59f17eaa3b | -13.09112 | -47.86212 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b219fc8f-dd3a-3e1b-91b5-f921660822c9 | -15.59135 | -42.3605 | 2025-10-07 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 26d33801-d66b-3f6c-94be-126270ccc182 | -13.25908 | -46.46925 | 2025-10-07 04:10:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4eb0508-7bc8-3980-8c05-93f5a4be9bf3 | -14.92293 | -46.81486 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37483f04-7cc1-375c-be80-2acb55135dd7 | -13.32859 | -47.56184 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb1f7d5e-276b-3230-9450-6ec682fbb05c | -20.25237 | -45.48132 | 2025-10-07 04:10:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e0a2ea9e-6810-33f3-a388-f0e8f89b77b6 | -13.33975 | -48.03403 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 63fb706a-e151-3c53-9cec-e9641e577383 | -13.09689 | -47.98986 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc211381-330f-3ab1-9073-a7d7e9a97506 | -13.34724 | -47.56828 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3e9d37d-5a14-32bf-a819-c70c3ce2c676 | -13.0761 | -47.83302 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 13f3c932-a791-3293-9e68-d91447d57384 | -15.27063 | -46.35514 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4241b24c-2b2c-34f0-b70a-25c19165f46a | -14.70164 | -48.39412 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c645af3-dcf8-3b2d-a41f-cc0de0945cfb | -14.77017 | -46.04484 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3775eb0a-a1e5-3d41-aa4e-af544d296f63 | -16.00157 | -50.95991 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cfb364b5-c900-39b0-ba3c-fc2ee325b926 | -15.60409 | -52.57278 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6204b5e9-1a62-3ee6-af52-e2ca0bfabbb6 | -14.74911 | -46.02071 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f3efed1-9e68-3470-a217-160583fa2d9e | -15.27554 | -46.34744 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b6ec0c94-3c22-3049-a6fd-ebe775c225d3 | -14.91745 | -46.86809 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8f4c955-c8eb-3711-9e2b-86c855307099 | -19.95472 | -44.63216 | 2025-10-07 04:10:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e1c46de9-45f0-363d-ad31-631e84260768 | -14.73732 | -46.02685 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6fdc648f-adb6-3f87-9abc-5da0070b51a1 | -19.70716 | -44.12145 | 2025-10-07 04:10:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cf8725a-cd8b-30e5-a0f7-9269ea23429e | -14.90976 | -46.82653 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cf1def2-4fc3-3d3b-953b-ed490c0a3736 | -14.5238 | -46.92453 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abbb568e-9d38-3d5d-b5e2-7c0b7126019a | -14.49757 | -46.92429 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3c0c701-3089-361d-89fa-4c331232d0e8 | -15.38762 | -47.98932 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5292d8fd-990d-3bcf-bfec-16b987a86b4d | -14.92506 | -51.44657 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a1c6728b-5711-3446-9b40-48177f4c140b | -20.11505 | -44.409 | 2025-10-07 04:10:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 805ef976-7bf3-37f2-a891-bbe1838e7a89 | -13.27986 | -47.56896 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 645ef687-0dcf-314f-bd0f-5350fc821e09 | -17.08832 | -43.37653 | 2025-10-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ab31439-4c2b-3007-82c5-1bee0ce69a57 | -12.40684 | -51.13891 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d7e79b4-050e-3039-b6ac-4426a5fd2fff | -12.4103 | -50.26788 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e9590ab-ed5a-3fe2-b94f-15f5a835734b | -18.44942 | -42.61274 | 2025-10-07 04:10:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fb17819c-d564-3837-8a8d-8695142c8026 | -15.36416 | -47.3078 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd77c5c4-62c0-389e-9f22-f185aa005392 | -20.09971 | -44.19928 | 2025-10-07 04:10:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e6d0f914-939f-3db7-96f2-6e3d762e0f1d | -15.61992 | -52.54659 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50b4b931-3d8d-3e87-96b5-5ef1481cd916 | -13.66862 | -44.30585 | 2025-10-07 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 92777036-ba84-36ac-b0e9-0f997b9d9462 | -16.1152 | -48.93776 | 2025-10-07 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1a2045a-9f05-3da3-ba0d-5d476eec789e | -12.18642 | -47.77401 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d226cfe1-ac4a-3983-b840-e847479d3440 | -14.70543 | -48.37261 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bfb7866-1e1a-3060-8cbb-7b5e4d430702 | -11.15278 | -54.87331 | 2025-10-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3410c56-2e3e-354b-aba8-530b974e9d7e | -13.23602 | -48.45781 | 2025-10-07 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 457c6458-db19-3e4a-837b-454920ab012c | -11.15706 | -54.88491 | 2025-10-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d95931b1-6e0e-3b19-b192-4663303e9006 | -15.60403 | -47.29227 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b7ec4573-b429-3e39-9f0c-ba0bdeb02389 | -15.58218 | -47.26719 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08e2bb38-e3e6-32a0-8837-1de8b081b1b2 | -14.9288 | -46.80236 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 851e5abe-aa88-3d50-9b8a-01dc379dd35c | -19.43401 | -44.17284 | 2025-10-07 04:10:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 242e736a-1cf2-346b-8603-ea0b8df247a6 | -14.90388 | -46.83899 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46bf5d51-f26b-3dbd-8543-9bbc85f2b77e | -14.90147 | -48.08985 | 2025-10-07 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d47b802-31a1-3564-8840-9c992931abab | -17.61094 | -46.68523 | 2025-10-07 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b27b073-99e9-3ed8-8669-d6200df1e152 | -11.86849 | -56.88806 | 2025-10-07 04:10:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 09a02f66-5b80-3724-8a8f-62c3e8d08ba0 | -13.04881 | -47.89685 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fec597e-081e-34be-9e7f-3101edad03d0 | -14.54193 | -42.42143 | 2025-10-07 04:10:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 77242a9e-b0b5-310b-8ccf-897614a571ba | -13.24925 | -48.06131 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c2d00b0-e448-3cca-9b3a-1c775920ade3 | -13.074 | -47.89174 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 53de9b68-cfb6-30cf-8789-2eb00f5b9b19 | -15.5905 | -44.50816 | 2025-10-07 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7f29a92-a99f-3087-8dec-4469badb151d | -13.24786 | -47.79723 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 834d6149-ff61-3c52-971d-adf2fe978781 | -13.03438 | -47.90995 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 117eac77-8f4e-3b2b-b367-68df5fe9ff37 | -14.61977 | -52.48841 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4e18751-da28-379c-9a8a-5645f4cf9ec8 | -12.38169 | -51.11066 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f683d4d9-1ee5-311d-b4fa-754da14897a9 | -13.52107 | -48.62167 | 2025-10-07 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c12725ef-69ee-374b-b912-ffd942535cf0 | -17.5706 | -42.93122 | 2025-10-07 04:10:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cb7fd9a-301b-3407-8b9f-6defde82fc67 | -13.29461 | -48.05884 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 755e6c8a-a841-34b1-828d-91c1b8dbe4fd | -15.2198 | -56.77296 | 2025-10-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46ba0960-9149-3886-bdcb-f18ea71879ea | -13.24672 | -48.05914 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a55e6ca7-909e-3192-b3ec-da71b67bc25a | -13.71947 | -48.19156 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f318bf6-3631-3680-b9b1-c0dbd8688129 | -17.55057 | -46.76585 | 2025-10-07 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fcb6383-1f26-3a00-97e7-d07ba30b2b4a | -17.92425 | -44.60316 | 2025-10-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e83efb6c-f466-3c3d-a384-ce856bb9e45a | -13.36617 | -47.56389 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9bf8b823-7241-3cfe-ba83-cd9d162252f7 | -13.26024 | -47.16675 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ffcc84d-7540-35b6-97e3-31593e9db3ba | -14.93408 | -51.42806 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad019ca2-81f9-3e7e-838e-36b76f6d8b1c | -13.28728 | -47.16686 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00a6b90a-1cef-3ab6-b3eb-320afe53b442 | -13.71676 | -48.06944 | 2025-10-07 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6041a533-a29f-3b55-83f3-7a50eeb9bafe | -19.80518 | -46.05635 | 2025-10-07 04:10:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51c953e3-239e-3f63-85e2-776b85c5c603 | -13.27638 | -48.46647 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 490a8c39-26b4-3009-be0e-395038ffdee5 | -18.77923 | -44.62037 | 2025-10-07 04:10:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e10db120-713b-3a3b-b6b9-c6b9f4d96cd2 | -13.69976 | -42.83788 | 2025-10-07 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e48e451b-f867-3b55-add6-d30fc04f15c7 | -18.37847 | -46.43148 | 2025-10-07 04:10:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fcc954c-4824-329a-bc69-af630354f28f | -14.9081 | -46.85756 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b67cbc5d-4984-3bac-ad57-e53453c98663 | -18.97107 | -47.82572 | 2025-10-07 04:10:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6d0a4969-943a-3ff1-b046-f9576326bb37 | -19.80579 | -46.0526 | 2025-10-07 04:10:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6c8e179-77f3-36fb-9527-1b7c75bce7a3 | -14.94466 | -46.81804 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9230f68-d84e-31e0-a937-0ec47860e6ca | -15.60363 | -42.37004 | 2025-10-07 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a6bf1304-43fb-35be-b02b-0398c6553d1d | -11.74161 | -54.7234 | 2025-10-07 04:10:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4a487a43-6da4-3f13-a056-0d29ccc54693 | -14.75273 | -46.04187 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9fb0d08-cfe1-3dae-8a1f-534dff9ea2bf | -16.28133 | -50.98573 | 2025-10-07 04:10:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55dcd02c-8efd-3014-a0d1-c1a6f9f9caed | -15.05419 | -42.33961 | 2025-10-07 04:10:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 04819210-a386-3d97-841f-d1f11d37bd47 | -13.25556 | -48.05526 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58c62baa-66f4-3dc7-a50c-9b9cca1f945a | -13.05506 | -47.9278 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a985902-560c-385b-97b5-9e5daa0e104e | -19.76385 | -43.95042 | 2025-10-07 04:10:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README43.md)
