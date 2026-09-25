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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb2e11b3-034c-3850-84a7-2dd0ba1e22eb | -9.11603 | -59.5033 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ef1aade-869d-3556-9dab-5590287d46ed | -12.21138 | -50.70978 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 150c772e-e69a-3554-9a83-40d3604c6436 | -9.3277 | -56.81565 | 2026-09-25 05:31:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56bb474f-2087-3a67-b5c0-46f77b299fe9 | -12.21745 | -50.7167 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cd0c93ce-3355-372c-a1ee-9f627876cb02 | -12.21614 | -50.72881 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| dd668b86-4cbe-3abf-b546-fa0a42e70ed6 | -12.24233 | -50.73829 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 9954d649-c6c4-386d-b43f-b6f3a3f7c04c | -8.02796 | -71.36097 | 2026-09-25 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db45c1a3-8455-3393-a8ab-805a3268fac7 | -8.46392 | -64.15597 | 2026-09-25 05:31:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd5603e0-155d-3315-bfd0-9f93495b029f | -11.56355 | -61.24324 | 2026-09-25 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75183c44-f445-313a-aeb6-3bfc25b2bce8 | -12.18763 | -50.80437 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 099dc1a8-8e1d-32ca-9ffd-d02fedb619af | -9.36076 | -60.36205 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60269589-8fed-3c31-93ae-02b51aabc48d | -8.38819 | -71.07401 | 2026-09-25 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfdf0d56-a9ec-30be-91cc-c8833ae5dcf6 | -9.02509 | -60.52596 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b9c1a45-0ea6-3843-b696-4c8456e7537a | -12.23364 | -50.75555 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1394ec37-7a93-30d3-abfe-6a3cf0d30b68 | -8.51157 | -71.3899 | 2026-09-25 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef4fe07c-652a-3645-ac7a-3ec41cdde350 | -6.9988 | -71.586 | 2026-09-25 05:31:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70b949f2-ee96-3865-a40b-d75a201d550b | -10.03366 | -62.14502 | 2026-09-25 05:31:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81f56ea5-d5fe-3cb4-8660-b7a6cd5ffb91 | -12.24499 | -50.71407 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f23e15f1-c1e5-3163-9ce3-552d2b74de8e | -9.824 | -64.14434 | 2026-09-25 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4621263-b309-33e0-89e6-07a74209716c | -9.17238 | -60.80536 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3cdc38fc-399f-3822-b27f-4a494a63dead | -12.25104 | -50.72099 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 5d559637-91a8-3e65-9c16-14cda2720060 | -11.8075 | -58.16546 | 2026-09-25 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5f5f157-6c7b-30bb-aa73-8e56ef7c7908 | -10.56521 | -59.48176 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e41bb98c-e6cf-34e4-adb3-44a452c36481 | -8.26512 | -70.80317 | 2026-09-25 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5431d445-f996-3441-a392-2a4958a824f8 | -9.93134 | -60.71622 | 2026-09-25 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 070c0800-bf8a-3c6d-be60-e1e9abc8091c | -9.17233 | -60.78197 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65298d52-f1a9-39d8-8efb-9a6dd60ad0c9 | -7.60558 | -69.89297 | 2026-09-25 05:31:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7001718-cd5f-3b22-bc27-b1f70765ecc3 | -9.19885 | -60.86367 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41686aab-403f-34f8-ba71-34c32ae801d8 | -9.11667 | -59.49901 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6356e44c-5620-332a-a55a-7cf4031fcd1a | -10.89889 | -53.94471 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a253ca12-4a00-3da0-b0b5-12eb3966dc1b | -12.20208 | -50.76252 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 425504b8-e075-3137-8439-cd20c6afe13f | -9.18246 | -58.06578 | 2026-09-25 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a3dbd55-3e63-347b-beba-46acfd78f721 | -12.17104 | -50.70462 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c7a1bfd2-efc9-30f8-81cf-8c2fc513c497 | -9.08695 | -61.44448 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5da1c55-ccfa-3cb1-b28d-a68f3ebea574 | -12.24705 | -50.75724 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f47ce554-9be0-3258-89d8-7b6102a26bdb | -12.17657 | -50.80783 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6f575280-5d57-373f-8787-1875edd1fcba | -11.8047 | -58.16224 | 2026-09-25 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b33bc99-811a-3794-89af-7f7edd3cccba | -9.21678 | -60.45721 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd4ab930-239b-3138-8aa4-7ec49dfb2de7 | -12.20621 | -50.72636 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 08a07d80-8c93-370e-854d-6d8b0a8fcf72 | -10.61771 | -54.0056 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d7ad90e-5a4d-3857-b94d-403e45cb9c08 | -12.22219 | -50.73574 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e38fd702-907b-3ad7-9e03-22b71b35480f | -10.61936 | -53.99197 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0361d8c8-adf1-3d99-9073-0ca4c1b6396f | -8.27038 | -70.81296 | 2026-09-25 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0f2e8dc-9f56-3a8b-9846-497f875bc7db | -9.15736 | -59.47726 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8d9cac52-18a5-3e23-bf8b-16eb9c9f718e | -9.17578 | -60.78252 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6ccf063-00eb-3953-a914-222c753cb30b | -10.89846 | -53.94817 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7000fbf5-4109-336a-beb3-3d2e3e74013e | -9.21175 | -64.50625 | 2026-09-25 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43d2e240-487c-330d-b1cf-dc85b5173c2a | -10.61812 | -54.00221 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 406588ba-8979-3b8a-8769-86311838b3fe | -8.96258 | -63.37061 | 2026-09-25 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 510c2c3d-2241-373d-a5b9-414c8d3e1f23 | -7.51799 | -70.39309 | 2026-09-25 05:31:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79d52eed-8cde-359b-9f3d-c6e35438510b | -12.22088 | -50.74784 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| e9785352-e3ef-33b8-8363-0684ca8a1ca1 | -12.19278 | -50.7247 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73e72bcf-03b1-302e-bda9-2bbcdc7a6bc0 | -10.89932 | -53.94121 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50776898-656b-3fc3-bdae-77fa85c783fb | -9.69369 | -58.12976 | 2026-09-25 05:31:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c0270a9-773b-31a9-bb5d-8bb0dda23cd0 | -12.16432 | -50.70375 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a378261c-6336-38f8-ac99-ed9ee4f71066 | -9.02972 | -60.51873 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61f214bb-b47c-3fe3-835b-51fa48f8dfd5 | -10.56021 | -59.49021 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55d84e9e-edcb-302c-8341-ee7ae23562ef | -9.15004 | -59.47615 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c958a3f3-3901-3cb1-80b6-67c1322ced0c | -9.38413 | -66.5075 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa8f272f-d35b-3371-a60c-9cc028b14609 | -12.18992 | -50.71935 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f1ec6faf-7041-3f6f-8c22-580f5ccac48b | -9.40017 | -65.90675 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93b79e12-6789-3a77-b207-3c62c235e8bb | -12.22628 | -50.7607 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3af643a2-0075-3d47-8a29-9b53aa882741 | -12.24299 | -50.73224 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 211c35c5-7372-3654-acc3-3b5836de1e4a | -9.69018 | -58.12571 | 2026-09-25 05:31:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1870d66-9134-3e2d-a3e1-4ebc15cfe24f | -12.23166 | -50.77359 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a9a96cb6-65d8-3a06-877c-3d5182ade2e9 | -12.21892 | -50.76588 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7c04fc0b-7e03-39b3-b834-92997c5cf5fc | -9.02103 | -60.52932 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29268031-6199-3587-a9b9-0947c4ef2bc6 | -10.41551 | -53.80449 | 2026-09-25 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f816e71e-d232-362a-af99-4a55e4c6f9e3 | -10.43157 | -54.46689 | 2026-09-25 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0979698f-d99d-3724-9b7f-e75353d94b41 | -8.26907 | -70.8096 | 2026-09-25 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a0082eb-6557-39ac-876c-da5182865fe5 | -9.08413 | -61.44033 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 417b7ca1-33a1-3b03-8ff9-66554d8138c2 | -11.28802 | -51.29609 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5709a3e6-97df-3020-ba5f-7c3957538beb | -12.21027 | -50.78303 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5f8ebda8-80ba-3ed6-aeea-e8ab7314da2c | -9.11238 | -59.50276 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0b2b94e3-dda3-3033-ace8-2c43acf55076 | -10.62145 | -53.99309 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f02e47b4-9314-38d1-a098-ab1907f1f409 | -8.3148 | -70.53972 | 2026-09-25 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18505f4a-364f-3286-81c4-e82c2361cfb2 | -9.57168 | -66.4868 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a281b03a-d793-3408-b3ea-acb5546dbcfd | -16.00884 | -56.32091 | 2026-09-25 05:31:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 65c60da5-bbd1-30b8-8e22-bdbc55594d1c | -9.15882 | -59.41526 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d802ad82-d842-34e5-aad9-e81545d59574 | -12.19881 | -50.73156 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 373c6844-199e-34e4-8f76-b65d0cb2b0e7 | -12.21287 | -50.75902 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| de74f5f7-9ac2-3aac-af85-ef19d76079b2 | -12.22759 | -50.74867 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 3c985ebb-4dd9-3f72-9184-8b3ad82d5a17 | -9.04014 | -65.42068 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a85cc979-9bfe-3b99-bff8-282bcf1b7cbe | -9.2162 | -60.46115 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f3a80c3-0528-39d5-b672-7f59d9b68e04 | -12.24432 | -50.72013 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 088dfd3a-f16c-319b-bb97-3b05f7655d21 | -10.56085 | -59.48569 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aeb72a8-9fac-3098-a7b3-b7c62e0f8235 | -12.17399 | -50.71013 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 54457528-8f52-3697-bf79-d837c44cb8fd | -13.77768 | -54.04118 | 2026-09-25 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 740aa5dc-9871-3d47-9088-a68517e43d18 | -12.23902 | -50.76841 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3cd10333-8a54-3afc-a9a0-97daa74220af | -9.27828 | -61.38804 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1e72f78-8f33-348b-8fc5-8337a765a269 | -10.56893 | -59.48233 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f4e1a12-5dbd-3cc9-85fe-9904258fb57d | -15.18434 | -56.05259 | 2026-09-25 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2432232-bec4-3e23-947a-52b76c415854 | -9.31984 | -59.67331 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af110c7e-7bd2-3319-b0a1-362cfbb8c49d | -9.2989 | -62.30432 | 2026-09-25 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd3981ec-7db3-3ffc-a7f5-43010c0812f8 | -9.03262 | -60.52312 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbf27dd7-1773-32b1-90b5-38a1adca23fb | -9.02624 | -60.51821 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8033731-a34d-354f-8aa0-dc032e35f15b | -9.31921 | -59.67088 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4025f7c6-a9ef-3eb3-9c57-a8b88f556d2a | -9.1946 | -65.78755 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4c16c10-fd81-3bd6-b815-693bee46c860 | -12.21762 | -50.77789 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ce3a80a4-7b77-357c-be73-99c054d425f7 | -9.41879 | -60.46236 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README33.md)
