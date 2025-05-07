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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fa60ac1-88d9-3723-b316-d48f6ff0cf1a | -18.26724 | -52.9965 | 2025-05-07 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3068802-1741-367c-a1e9-46a4f39aa88c | -18.42228 | -54.71051 | 2025-05-07 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f4bc8b6-79c2-390a-9a01-21bd19867fef | -21.04953 | -55.99672 | 2025-05-07 05:21:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25c08fc3-e093-3650-bab3-7be1afa4f37d | -21.05383 | -55.99735 | 2025-05-07 05:21:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84aadf4c-4efd-34bc-ba28-408c85cef9b2 | -23.60481 | -49.00187 | 2025-05-07 05:23:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dca7920-51d8-36f1-9198-9f907a7a319b | -23.60921 | -49.0181 | 2025-05-07 05:23:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44c19891-7d42-371e-9471-2b953bb8ed97 | -23.61007 | -49.00541 | 2025-05-07 05:23:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17fbd914-dcfd-3886-a3f7-faf2e03da1e9 | -30.27877 | -53.34155 | 2025-05-07 05:23:00 | NOAA-21 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| b5cf376a-4903-3952-b112-38232bdcc4c6 | -30.27905 | -53.33743 | 2025-05-07 05:23:00 | NOAA-21 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 63cc1741-8f84-3895-afa1-422df45a3321 | -23.61084 | -49.01545 | 2025-05-07 05:23:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c89f539-af46-30c7-b971-5580d04aa12c | -23.61163 | -49.00274 | 2025-05-07 05:23:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c647e375-fd42-3432-8373-14f60603d0f6 | -11.3963 | -52.9477 | 2025-05-07 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 1db10479-64ff-3b34-a062-7e6dde82bcd9 | -13.04529 | -53.72303 | 2025-05-07 05:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcca71e7-686b-32ed-923f-e84dd8ffe884 | -11.38978 | -52.93723 | 2025-05-07 05:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 92648706-b62f-3f68-9a74-a103981cf2e6 | -13.05311 | -53.71902 | 2025-05-07 05:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b772f0c-b799-3bfe-948c-322dc55e4017 | -11.39529 | -52.95153 | 2025-05-07 05:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e37747ba-e04b-3339-8d86-f5aa6a0cbee8 | -11.39681 | -52.938 | 2025-05-07 05:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c4a3e509-d727-3b2c-b2a4-98b5c475e8b6 | -13.04463 | -53.72935 | 2025-05-07 05:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ed69e6f-b5b1-3883-ac8b-ded46a135655 | -11.39604 | -52.94486 | 2025-05-07 05:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d00f9e6-116e-3a6b-b03a-f7022d2a7bc2 | -9.15853 | -61.95728 | 2025-05-07 05:44:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 558aad73-6505-3f9e-8688-a3d53dfd5e1d | -12.1739 | -54.23731 | 2025-05-07 05:44:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a9b41b5-03e3-35c5-a7da-43f2578a7654 | -12.17321 | -54.24314 | 2025-05-07 05:44:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 68ac06c1-3514-39a7-9c35-3afc685d1444 | -9.92965 | -65.01934 | 2025-05-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03e13e74-dc3d-3f36-bc1b-f974228d71a7 | -13.05382 | -53.71272 | 2025-05-07 05:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 624b1970-ea3a-36d1-b586-be3d3554a191 | -11.80253 | -57.37011 | 2025-05-07 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74daa421-194d-3d43-ac82-0b2a57cae7c7 | -10.23268 | -59.24115 | 2025-05-07 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa5f767b-3b61-36ea-b3ca-1b64781b928d | -11.38902 | -52.94404 | 2025-05-07 05:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a6a1ed30-2298-3330-a337-dfe5d484b747 | -9.15921 | -61.95266 | 2025-05-07 05:44:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35fe678d-ab6d-3b7a-b011-4cd018f6e68e | -12.55423 | -57.75814 | 2025-05-07 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5daf24fb-fc1d-34aa-b761-4b9aa8bd88ae | -9.08295 | -63.70011 | 2025-05-07 05:44:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f8b0b03-88b3-30a9-a528-1470415b34e2 | -12.55465 | -57.75482 | 2025-05-07 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5ef2d31-b8b4-3a22-8ecd-022145321e35 | -13.04554 | -53.72485 | 2025-05-07 05:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 447c2ca4-096f-3ba6-b7ce-d56c429a50fe | -12.17032 | -54.24292 | 2025-05-07 05:44:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84297f3f-75a2-3c6b-a488-07c759e93fa5 | -12.16967 | -54.24869 | 2025-05-07 05:44:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32922609-5306-3271-9f4e-88ce6e47ad69 | -13.05282 | -53.71725 | 2025-05-07 05:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcf2a2a3-3351-34f0-b55e-73af4e2529dc | -9.93583 | -65.02398 | 2025-05-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d733dd08-171c-3fd2-b11e-de8aa9ff51db | -13.04624 | -53.71852 | 2025-05-07 05:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17137ef5-4043-3d4e-8db8-40cc6ccd8714 | -13.05215 | -53.72356 | 2025-05-07 05:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cfa8d41-fce2-35ec-b2df-0c0d3a053e2d | -13.50211 | -52.95768 | 2025-05-07 05:44:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b86c8747-ec13-3c56-8ebd-63eb50a3c7d2 | -18.4236 | -54.7069 | 2025-05-07 05:46:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5f46442-2a12-3220-8ac6-ea1b7cec8501 | -18.41624 | -54.71226 | 2025-05-07 05:46:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a608840c-cf19-3f21-bd3c-2c4a346be4ab | -14.68508 | -53.39609 | 2025-05-07 05:46:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39e4c841-56cf-3a3f-8b60-411061bed112 | -11.3963 | -52.9477 | 2025-05-07 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 17ceefe7-b057-3a70-8a18-2d625fcff99e | -5.13206 | -37.96304 | 2025-05-07 11:57:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 78c8e4a7-e3ce-3c82-b79a-7ef152aedf23 | -4.89849 | -37.52906 | 2025-05-07 11:57:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| cddae0bd-3dcd-3df4-891e-885dc656c638 | -6.9801 | -42.809 | 2025-05-07 12:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| dca89219-1c0c-30a4-a6f7-fc996e0b0e1e | -14.7084 | -42.512 | 2025-05-07 12:00:00 | TERRA_M-T | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 86378bc7-d222-3192-a8d2-012b971ec8ee | -8.56322 | -36.75075 | 2025-05-07 12:00:00 | TERRA_M-T | ALAGOINHA | PERNAMBUCO | Brasil | 2600609 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f7910847-6721-3d9d-9931-4e22f8ffb6d9 | -11.80478 | -43.78294 | 2025-05-07 12:00:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ebedf543-87a2-33a3-b30b-7592325e11cd | -10.72277 | -42.32894 | 2025-05-07 12:00:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| abd80d97-8b07-364b-bc30-5cf57ef85a5b | -10.96758 | -44.43208 | 2025-05-07 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 5f273689-d26f-3685-975e-e0e15e228d56 | -5.90477 | -40.65858 | 2025-05-07 12:00:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 50ec9d1b-7878-3caf-82bc-571706fd27af | -13.33015 | -43.54229 | 2025-05-07 12:00:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2b5b4f5b-bd2e-3c6c-b5d6-63df52f9c024 | -14.69785 | -42.52027 | 2025-05-07 12:00:00 | TERRA_M-T | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| aed7a305-22be-3452-95ef-58e518efb7c0 | -11.7955 | -43.77523 | 2025-05-07 12:00:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bd4b7b1e-ff54-3005-b799-6496914978cb | -14.69932 | -42.51063 | 2025-05-07 12:00:00 | TERRA_M-T | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 2dd88274-7027-3ea4-8b1e-ace7ed79ee4b | -7.40399 | -37.32632 | 2025-05-07 12:00:00 | TERRA_M-T | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 03c956d7-bdf0-32cc-a9f0-b0f0837f5463 | -13.7774 | -42.94072 | 2025-05-07 12:00:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 3034a5b6-67f2-3ca2-ad3c-c4cb5af7acb6 | -8.07227 | -43.12354 | 2025-05-07 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 4b7c0173-dc8e-3161-9d04-2e9e7246e639 | -8.32364 | -36.18489 | 2025-05-07 12:00:00 | TERRA_M-T | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 30783bdc-923b-30a4-9911-fd95962ebc12 | -8.72703 | -36.75167 | 2025-05-07 12:00:00 | TERRA_M-T | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 23fd4b89-77fc-317d-b62a-22df3ad557af | -14.07756 | -41.41477 | 2025-05-07 12:00:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ce97f971-03d5-3ade-b250-47d666b96501 | -10.96551 | -44.44551 | 2025-05-07 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0872b91e-dea4-3b2f-a970-21afa8afc2e0 | -7.41801 | -36.08641 | 2025-05-07 12:00:00 | TERRA_M-T | CATURITÉ | PARAÍBA | Brasil | 2504355 | 25 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 78741c40-d8d6-3aa8-bd37-76bb23d00b7d | -8.0741 | -43.11155 | 2025-05-07 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| c7ff7046-6fad-3e47-aa3c-773986ab0871 | -10.96054 | -44.43698 | 2025-05-07 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9cdef171-d7d4-308d-b129-174cd0d2cf21 | -13.77894 | -42.93047 | 2025-05-07 12:00:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 29.4 |
| 149b910b-a9c5-3073-8bbf-05819d39a692 | -17.99833 | -44.39813 | 2025-05-07 12:02:00 | TERRA_M-T | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 31ad3481-3c41-3520-a4b7-db82bb3db033 | -17.49221 | -45.3026 | 2025-05-07 12:02:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cb15f670-1e55-30fd-89a7-568c7591af49 | -17.49426 | -45.29014 | 2025-05-07 12:02:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 83eb5cce-e6e5-3f33-8c6e-60fe49ef0a9e | -18.12048 | -44.27205 | 2025-05-07 12:02:00 | TERRA_M-T | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c15ba773-e933-3eba-adb8-be3ffdf04b8f | -6.9801 | -42.809 | 2025-05-07 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 3edafc3f-366b-3c88-9250-1e13b1f99574 | -6.9801 | -42.809 | 2025-05-07 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 1e0aa3d1-c559-3cd5-9797-24b676a628e1 | -6.9801 | -42.809 | 2025-05-07 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.8 |
| 9149a985-e1cc-31a5-9aa6-c464655422ec | -10.9733 | -44.441 | 2025-05-07 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f953ac9f-e727-3c5f-99df-28e3daf3ab2c | -6.9801 | -42.809 | 2025-05-07 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 113.8 |
| 83dd2688-723d-3504-91fd-127892e23e6f | -6.9801 | -42.809 | 2025-05-07 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 136.1 |
| aaf97b96-bf61-397c-8372-2ddd1d5c052d | -10.9733 | -44.441 | 2025-05-07 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 3830623b-4ed9-3012-9f9d-375e9631c238 | -6.9801 | -42.809 | 2025-05-07 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 166.4 |
| 0d077302-147e-3add-9055-acae5eb963e8 | -10.9733 | -44.441 | 2025-05-07 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 08edc194-4f79-3efe-8098-8cf7eaad328e | -10.8153 | -49.732 | 2025-05-07 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| dfeb4272-fe7b-3b01-94cb-6bb3a200f73e | -10.9733 | -44.441 | 2025-05-07 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 022869fe-ac96-3a0e-b637-c35de9620fda | -10.9733 | -44.441 | 2025-05-07 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 64b0f821-43c7-376a-b253-c2320a90415b | -10.9733 | -44.441 | 2025-05-07 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 67cb3503-c5c1-332a-a8b5-f50113497628 | -18.408 | -54.7158 | 2025-05-07 13:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 98.0 |
| be7efe8b-d04e-3987-9398-f397158d8f0b | -9.6634 | -49.7228 | 2025-05-07 13:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| be194e25-012a-3ed9-b75b-bb9c0affe960 | -10.9733 | -44.441 | 2025-05-07 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 8753f15c-968f-3aee-99f0-1620c8144133 | -18.4279 | -54.7129 | 2025-05-07 13:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 86.3 |
| f3b79b20-1939-30b9-9441-296c286717a0 | -10.9649 | -49.8661 | 2025-05-07 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| daf4242a-6bfd-392d-9490-0fe2dc4fa227 | -18.4279 | -54.7129 | 2025-05-07 13:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 1541bd02-7a29-32f5-9520-8b49f2c196a5 | -10.9733 | -44.441 | 2025-05-07 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 47d07e8a-ccec-3dee-91bd-d53588908a6b | -18.408 | -54.7158 | 2025-05-07 13:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 868ad765-d43c-3e8d-bc23-03c23ddfca51 | -10.9733 | -44.441 | 2025-05-07 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 971e9285-524a-3b19-b280-03b08aab06d0 | -9.6634 | -49.7228 | 2025-05-07 14:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| e161e012-b65b-3770-8a4a-dbd911ed1e37 | -18.4279 | -54.7129 | 2025-05-07 14:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 111.7 |
| d4769f47-40f5-37a3-9815-e8717ba6da68 | -10.6479 | -46.9221 | 2025-05-07 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1b437a18-8a92-3e9c-a7d6-c17f1ad3d08b | -18.4283 | -54.6916 | 2025-05-07 14:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 82.6 |
| d017b7cb-888c-3ba5-8b0a-78a7ccdb6d40 | -18.408 | -54.7158 | 2025-05-07 14:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 976fc35a-4cfd-333d-8f61-6cf2b41cec1b | -9.6634 | -49.7228 | 2025-05-07 14:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 348c4acb-0dd5-3ccd-b6c0-dbe135cdefd6 | -18.408 | -54.7158 | 2025-05-07 14:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 130.2 |


[Clique aqui para ver as próximas entradas](README8.md)
