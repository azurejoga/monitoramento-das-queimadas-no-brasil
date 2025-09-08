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
| de824bc8-1c52-3a53-ae45-fab29d9ed821 | -12.82667 | -52.89036 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95776714-017d-3a7e-aa64-05043ef0569f | -10.88862 | -55.7177 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 592c8aee-de41-3c66-aa1d-e047d3801f38 | -11.59026 | -52.20064 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b1418a3-a8f5-31c4-8fd3-2f41ed99d49b | -12.94544 | -54.78307 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9089389-ba10-3223-aa0d-5a33d5c537a3 | -12.94539 | -54.80486 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 97463e04-3fe6-3975-b0c0-dc8bd42124af | -13.93484 | -53.98125 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc481cd7-4be4-3230-b4ec-06c34f60a0fd | -15.69004 | -53.56604 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66f5a095-c7ec-3e20-85bc-c5a1cb3ace95 | -15.38444 | -53.94722 | 2025-09-08 04:53:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2803870b-b815-3964-9df4-c951293a5b26 | -15.72921 | -53.53427 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04373510-2d96-3b07-b652-2cb2a017b9e6 | -12.9487 | -54.8054 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 33d3d22e-4b30-35d5-9872-ced8aa435060 | -12.93826 | -54.78552 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8679c2d5-7f5b-3727-9df9-436b972e28ce | -12.82356 | -47.99943 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e7ed363-add7-3835-a479-15df831bf3b0 | -14.51023 | -48.80311 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bca4f2e-d7c1-3390-8e59-619f9e58c3d7 | -12.89276 | -47.99032 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80261f5b-13e5-31a3-a7ae-bf3e7fe7b2fd | -9.3771 | -65.93851 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4703e106-1fc5-3866-939d-7fa9a19a3cd7 | -11.63776 | -52.2383 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f8b6b41-04a8-38bf-87d9-63c1ea7b4368 | -15.18232 | -47.95919 | 2025-09-08 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99511e70-ad76-3506-ab0a-8101b66d9325 | -15.26944 | -52.38527 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3152e068-e0bb-3a94-9158-fbbec1b5aca0 | -13.82028 | -46.25426 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef19546f-2c49-34c7-993d-d86a472428a8 | -12.63375 | -56.98327 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de4278b5-cd7c-3617-b221-29e4525c3e38 | -16.34188 | -52.92426 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aef9ea71-4ade-3cd8-83fb-1fe12370fc77 | -15.83287 | -52.29754 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9a19b18-cb49-3478-b498-bcb7756c0296 | -13.81587 | -46.25964 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7205458c-4147-3748-b16b-50708cf97f01 | -11.22451 | -55.01043 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cba7b59-deb9-36e2-a996-da5f7b07d972 | -11.22393 | -55.01401 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99288d67-d10c-3b4d-bdeb-b55db6f3dc1d | -16.54583 | -45.10746 | 2025-09-08 04:53:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3666a240-c95c-32f0-a1b8-e370c776f191 | -12.94595 | -54.80132 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fff7c07b-14ff-3b67-825e-69055b03f888 | -11.96946 | -55.53805 | 2025-09-08 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19664b82-2d5a-3b40-896c-e0566b8a67b9 | -11.41261 | -50.37038 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| d990a545-81f1-33eb-9360-54ff91f2fe07 | -12.94488 | -54.7866 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a50646cd-22c5-3344-8689-811935cb95a4 | -17.53682 | -43.7384 | 2025-09-08 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3429b696-c270-3048-96a3-93b01c09da55 | -12.9377 | -54.78906 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3de89f9-d0a3-37bf-afed-0a774ce552ec | -11.35446 | -50.38398 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2cbe62fd-ae63-3772-ac0f-708e5e4db573 | -13.03514 | -47.13712 | 2025-09-08 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 497e7615-1339-3a99-bed2-6e279749130f | -13.81522 | -46.26524 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 02985bc2-d53b-342b-b503-079539a3d35a | -12.95038 | -54.79477 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3fe69ee-2d09-3cb7-b038-5db76abdfef1 | -11.20112 | -55.0066 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f7cfb1e7-6966-3a47-8738-85ad0b30fd2e | -12.19146 | -53.90898 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61a3fe66-cefe-3764-8da1-7b522e09c6f3 | -11.87587 | -50.96374 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3ff19c8-700b-3da5-bcf4-84be1477afb3 | -13.71621 | -46.88622 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8423b463-ffca-3ab8-8e8e-1a94a79f9e8e | -11.40881 | -50.39662 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 93a06d69-8f48-32f3-9662-5b971c98716d | -11.64115 | -52.23883 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 846b5aeb-9ac1-37dc-a0b3-65134b125c2b | -11.40299 | -50.33305 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fbb0a8d-db44-3388-adc2-a0c6748b029a | -16.06679 | -50.48069 | 2025-09-08 04:53:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1922eeb4-210a-3a74-a4a3-ecfb0c3d364a | -9.13168 | -65.95558 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 136535c7-456f-3166-a3e0-a956a0ec6afd | -12.92889 | -54.78036 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6572ea8e-9c22-33f9-9d1b-9fb0ce085643 | -16.16335 | -47.91782 | 2025-09-08 04:53:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30040adb-cc9b-3201-af5f-7f54200ffc5f | -12.89563 | -48.00206 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 149f3d90-a124-3398-a2c4-81e4dd2fb076 | -15.7544 | -53.54977 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 927aa7c9-8de7-3a27-9a25-ec4591c5c5f0 | -15.19072 | -47.96508 | 2025-09-08 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ebb5157a-c9e8-39ac-bc48-13744ad8722c | -12.82413 | -47.99513 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e3a4ba2-29cb-3d0c-a157-4ed5d62f0c60 | -16.97944 | -45.82898 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b3e0d0c-c1bd-3e1c-a4c4-6d9aea4c9208 | -11.49641 | -55.54354 | 2025-09-08 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccdd2ff0-6ffa-3f38-aaa0-836e3ab11b8c | -11.10433 | -52.00916 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 590ed151-df37-391b-8749-a707fb3c5a57 | -17.15679 | -44.44066 | 2025-09-08 04:53:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a03b1c7a-0b7c-3abc-a69d-b1c5a836d93b | -11.38075 | -50.38347 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df6063bb-8b90-31e7-a9c3-6f1e570b5b45 | -12.63158 | -56.9746 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7fda920e-8b72-3801-b063-9e9f8ad8c1d6 | -11.83524 | -46.76277 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53c4dbc0-27a7-348d-ab6b-82b8f0037cf4 | -14.81482 | -48.10225 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| baf1ac43-cfb6-3523-8f98-d0822bf03960 | -10.5098 | -57.80101 | 2025-09-08 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11b128f4-3c6a-3bbd-8237-4ae5798c60b5 | -12.83298 | -52.93982 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 849e3c37-3df0-30e7-9255-c2703083d0de | -12.5236 | -53.85107 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41fac889-77ff-39f0-a0ba-44bea151fa88 | -11.21334 | -55.01593 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54bcd3f6-664c-3a15-9d69-767f913c6c72 | -11.41021 | -50.36106 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 03a7a1f4-adab-3b4d-9e96-d9a752d5ff42 | -17.5705 | -44.54057 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 552e0657-7151-3a67-ae76-8b60860af065 | -13.54466 | -48.11425 | 2025-09-08 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa4ea56b-176f-3d53-9210-1d7058434b59 | -15.96378 | -48.10691 | 2025-09-08 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 24bfbe8c-1cf3-37d4-8b98-0f19bfadd3b3 | -10.25402 | -59.38398 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dca7e4c8-eb83-370f-b329-e07002e7e8f1 | -15.50893 | -52.77915 | 2025-09-08 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73b28094-f8fc-33a9-aef9-d477846886bd | -12.81547 | -47.02802 | 2025-09-08 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb74b53e-88ca-31b0-8671-b80b49d40191 | -14.29331 | -44.86341 | 2025-09-08 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37541d6d-6228-3d13-831a-a6c3c205a790 | -11.65726 | -46.87906 | 2025-09-08 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11730f27-7bfd-3e43-bf8c-7ec61a83ad75 | -10.57916 | -61.25721 | 2025-09-08 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| afca2604-a989-3fc3-9541-3edf301eb391 | -17.25718 | -46.69197 | 2025-09-08 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f25531f3-a8e1-35c7-9320-5d8e6b792939 | -8.88984 | -64.2183 | 2025-09-08 04:53:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 727fb2d1-f5ee-3120-8370-ddbbe6431d8c | -15.85221 | -52.31281 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4f046cc-95b7-30f3-8ac6-5a5136d0c2e7 | -11.22842 | -55.0074 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cd38f45-114c-3e26-b148-3d0cc0b17f9a | -11.18633 | -55.05578 | 2025-09-08 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4bbc627-9f73-3891-bc12-8efc2ce3c415 | -11.41501 | -50.37968 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| fa97748b-dd95-3cbb-97f1-bdfb8e7c37e2 | -15.26307 | -52.38028 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2750cdf2-63c3-3432-9d69-aacc60bbb194 | -9.94242 | -60.14418 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d16906d3-a7f9-3164-af36-82c879c6d992 | -10.16857 | -61.12551 | 2025-09-08 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 75680c22-4d87-3674-aed3-62d4473de396 | -10.08492 | -59.1805 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd1d18bf-123c-3a78-b9f6-6b187047a2dd | -13.0113 | -54.81913 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41350a96-be96-33de-bb3c-888ac4a4ac54 | -10.02757 | -63.47832 | 2025-09-08 04:53:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebc69311-85c4-3589-bca1-910853401f8e | -11.41247 | -50.39717 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 27d2f1c1-af67-36a3-9be9-5cf780e210f9 | -11.098 | -52.00108 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d582814b-11f9-3bda-8fea-1f6d8e5bb8ac | -15.69227 | -53.55114 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e8fbeb7-619b-38d0-8d4b-92c94043cbba | -11.02947 | -52.03992 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cbcdc2f7-508d-31da-b202-4995424a092f | -15.74768 | -53.59415 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 843c9fc5-210c-3e08-b24d-d0241fa15126 | -14.09465 | -44.78754 | 2025-09-08 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff84fc85-6cdf-38a7-83fd-436eb1eeaec7 | -11.20665 | -55.01485 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1708c35b-6018-3f09-9b74-e4f1afe97150 | -12.92945 | -54.77682 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c17cd7c7-37fd-3862-b1fe-8f3726f4eab0 | -12.9267 | -54.77275 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25a9a193-1b14-3c3b-b982-e384b8932495 | -15.25612 | -52.37917 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a16e9893-e0a9-393f-8de2-2f865cddea82 | -16.33617 | -52.9393 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eae4c91d-4391-353b-a6e9-018b8f1d5047 | -10.50682 | -57.79572 | 2025-09-08 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a974a6e8-37ff-3048-a47f-f93f2f39e6df | -12.9543 | -54.77002 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b1f470a-32e3-3473-89d5-1cd9b885b56a | -12.94269 | -54.77898 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0757457-ebde-3467-9d98-3ee7bb24fc3a | -13.91983 | -48.02127 | 2025-09-08 04:53:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README74.md)
