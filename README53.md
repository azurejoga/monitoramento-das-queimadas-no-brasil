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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61d39352-4d09-35f5-a374-466f604fff0b | -2.12777 | -56.84667 | 2025-10-26 05:40:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db57c771-d62b-33c3-90ff-8f004bad4cb0 | -1.3784 | -55.35007 | 2025-10-26 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b545753-0ad7-3f5a-9ea6-9d989a281aef | -2.78354 | -54.4194 | 2025-10-26 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b239a02-93a6-350b-8138-f9686112a76f | -1.38362 | -55.35066 | 2025-10-26 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e6f2f2b-d858-3c9f-87de-10a2be6f2480 | -1.38011 | -55.3485 | 2025-10-26 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a73b3b00-d339-3e34-a33b-635f642f2b74 | -1.37965 | -55.35158 | 2025-10-26 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6a7ff15-fab4-3885-ace9-26f1b935d613 | -6.53892 | -54.97071 | 2025-10-26 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f7c949d-ca1c-30ee-80ef-2cf4537ab6eb | -3.86845 | -52.19401 | 2025-10-26 05:40:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 693faa27-0bd3-3dcb-8ce0-ce6c92496579 | -1.746 | -55.74759 | 2025-10-26 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d72b9908-9e77-3470-bce7-007680a797a9 | -1.75105 | -55.74849 | 2025-10-26 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31fae161-8a80-34cd-b0ea-46c0cdab902f | -2.92169 | -52.72194 | 2025-10-26 05:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1592f096-48ce-3509-ab1d-5c6a8ce18380 | -1.7506 | -55.75135 | 2025-10-26 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a15323f5-b35b-3dfa-9e99-b4b9955fa633 | -2.12694 | -56.8446 | 2025-10-26 05:40:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5891f57-c84e-38a9-8a74-ec8ff67677a8 | -6.53837 | -54.97471 | 2025-10-26 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5fb8c63-7173-3202-b77a-f66f2077bcf3 | -3.79708 | -51.35111 | 2025-10-26 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ba6d90b1-fbce-38bc-849d-faeb68b9f34f | -3.79654 | -51.35115 | 2025-10-26 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4af3961c-c567-36c3-bc41-99e08001dc74 | -2.69046 | -54.77143 | 2025-10-26 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b03ee01-0c5d-3b22-92da-c4bb6fa3c353 | -3.53999 | -53.3211 | 2025-10-26 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83221977-e6e2-314d-ac3e-f01ccb90ecea | -1.74904 | -55.75279 | 2025-10-26 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63d5bed6-277b-3cbc-b232-c7f3398a31de | -2.06245 | -56.88622 | 2025-10-26 05:40:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a64f8ea-2a89-3b7e-9a15-dc55f52e10cf | -3.87045 | -52.19314 | 2025-10-26 05:40:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd692e3e-64d2-3f0f-b1dd-9ebd6a8e6363 | -9.45319 | -56.65118 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b3086fa-f68c-39c2-a0aa-70550fab202d | -9.63045 | -57.01561 | 2025-10-26 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebd16492-fac4-3330-be26-a80ebbc1ca38 | -9.29058 | -57.55011 | 2025-10-26 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9be766c0-e1b8-3252-a194-3f92659c7bcf | -11.21418 | -54.84293 | 2025-10-26 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9183bef-dcb6-3ca3-823d-78838ad1c727 | -11.81382 | -57.93925 | 2025-10-26 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9213b1f-54c1-3658-b4fa-a60d0817f92c | -11.36383 | -54.31346 | 2025-10-26 05:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c1097d5-f6f6-3058-aad9-a39ad1829461 | -10.60757 | -63.46629 | 2025-10-26 05:42:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6f32298-d524-3fb6-95bf-86b0ad3b0899 | -9.44739 | -56.65397 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd7c8ae3-d2d7-36dc-9a20-7712cc0a03fc | -11.36319 | -54.31887 | 2025-10-26 05:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5537858-c1f4-3511-9187-01a9b0e1ed9e | -9.4456 | -56.64349 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a5d5413-98c5-325a-8928-15f64f2258fb | -9.44782 | -56.65061 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81c74d39-12ba-3c87-80f3-db67d8bde2ac | -9.45006 | -56.65081 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0516ea96-9245-3830-bbc1-3a1319dacaea | -9.18011 | -57.69194 | 2025-10-26 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7a64403-40e4-3f30-952b-a2fddb1aea73 | -9.5556 | -66.74447 | 2025-10-26 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b51fec0-0af4-3ef5-bf86-6bb2e54c087f | -9.29018 | -57.55306 | 2025-10-26 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdb8de44-fc8c-31a6-b62d-207440826d80 | -10.6074 | -57.76872 | 2025-10-26 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 202137f6-e6f4-36b0-a8e5-7cd828d77f26 | -9.43979 | -56.64616 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8f4fcbd-e01b-3314-9848-a4b6f85d9592 | -9.44423 | -56.65359 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35594481-cc8a-31a3-a276-b82c126df5e1 | -9.44246 | -56.64997 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c38dc158-3429-3e3e-bb55-f3656aa50896 | -9.44333 | -56.64317 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 11bfbeed-6e79-3c04-9bc7-43907d5bea8f | -10.59349 | -63.46412 | 2025-10-26 05:42:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5964566-1178-32ca-b962-5cb8ed9d1f4d | -9.44289 | -56.64659 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b7496ba-fce6-39b3-aeaf-87bfc4461aec | -9.3267 | -65.50836 | 2025-10-26 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b521ff8-c4cc-36a2-a329-f1c063f17a95 | -9.44025 | -56.64275 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12103e34-086f-3a62-b54f-db1fd6dce829 | -11.91051 | -55.37565 | 2025-10-26 05:42:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f506dbf-51cf-3aaf-9baf-50656877ea48 | -10.59291 | -63.46801 | 2025-10-26 05:42:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c31a0d2-6149-3f77-b04e-ba8da933cfa3 | -10.07744 | -64.9855 | 2025-10-26 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc05d4e5-c3c7-37ca-b43f-a520db2cd2b3 | -10.0341 | -59.59078 | 2025-10-26 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2c29150-3b01-36d2-8032-2d05bffcb9a9 | -11.81813 | -57.94579 | 2025-10-26 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cc51ea3-323e-31e1-850a-d8c38f377430 | -9.55616 | -66.74094 | 2025-10-26 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34559283-1730-3105-b166-8f72813bbc84 | -11.32805 | -53.93988 | 2025-10-26 05:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15cc9537-5f49-3321-b7f2-7eaf3d398daf | -11.81852 | -57.94282 | 2025-10-26 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0951c610-976b-3185-b465-150c6cca6e7b | -9.3134 | -65.46339 | 2025-10-26 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a939138-97ba-391a-a76b-b0d2491abb95 | -9.44514 | -56.64688 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4dd1d73e-a7ed-34b9-b526-ca8710a867b0 | -9.4496 | -56.65417 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06f6b38b-db5b-3e3b-860f-47beeaecc0a8 | -12.42003 | -57.80597 | 2025-10-26 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d92ac0c5-e339-310f-afd6-b207aa0ae38d | -11.20803 | -54.84207 | 2025-10-26 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fce79e4a-c37a-36a5-9361-7468180cbcd2 | -9.29098 | -57.54716 | 2025-10-26 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 027d995c-7f11-3e1e-bb07-a49f3df76c93 | -11.3287 | -53.93431 | 2025-10-26 05:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba2bf436-400a-3010-ae1a-66a0d5650d15 | -9.44469 | -56.65023 | 2025-10-26 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b29d9eb2-895c-38a0-8a49-4686e4db5bca | -15.83521 | -53.58598 | 2025-10-26 05:44:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0d57b6c8-3d2e-3e07-87e7-f448f174ba37 | -15.83356 | -53.59063 | 2025-10-26 05:44:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fb871092-eec5-31e4-9a30-7b70cf224dac | -16.09508 | -57.27826 | 2025-10-26 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60e618ab-059b-3125-91ae-c2da3cc9cd42 | -14.50022 | -57.34121 | 2025-10-26 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b7741ac-0ee3-3858-b83e-8dbc1677678a | -14.89577 | -57.5542 | 2025-10-26 05:44:00 | NOAA-20 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3df2fee4-9574-38ba-9c1c-ff06cd383468 | -14.50064 | -57.33755 | 2025-10-26 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06cef243-5b34-3503-8293-a32e7662c314 | -14.89536 | -57.55777 | 2025-10-26 05:44:00 | NOAA-20 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1fc80318-c794-33d1-bb4a-a9d5a8f69a15 | -15.83421 | -53.5836 | 2025-10-26 05:44:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1fa04194-b3b3-3934-a64a-2580cfa434fc | -1.18579 | -53.3859 | 2025-10-26 06:35:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c3634ed4-cf54-3f76-8983-e152aede454a | -3.09465 | -49.45846 | 2025-10-26 06:35:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| cfb44de4-101e-30e6-99ec-11494120ac19 | -3.0971 | -49.44192 | 2025-10-26 06:35:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| bc16057c-e03a-3a8f-935f-c1148bbe5d1b | -3.54332 | -53.31922 | 2025-10-26 06:35:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ebd5d692-df59-3f17-851a-8763302882b9 | -2.78767 | -54.41582 | 2025-10-26 06:35:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5f779b2c-2eb7-375d-9489-2cb317f8b194 | -2.31996 | -48.57032 | 2025-10-26 06:35:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 53aea138-0886-36db-af9f-ef3f6a2f03fe | -3.14111 | -50.15592 | 2025-10-26 06:35:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6119f5c7-eaf3-38bb-b7f0-3cab4f5fad39 | -2.32212 | -48.57602 | 2025-10-26 06:35:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 375b1090-c9b8-3816-8658-bbc1e52f4b1c | -2.68992 | -54.76743 | 2025-10-26 06:35:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e4b7d3b5-b8df-3dce-91d0-5131cb151c21 | -3.10432 | -49.44824 | 2025-10-26 06:35:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3fa06142-8d04-358a-9cf4-3cab8c564e96 | -3.2729 | -50.04448 | 2025-10-26 06:35:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c0e45377-eec8-39b9-87a4-9116b84977b8 | -3.09253 | -49.44645 | 2025-10-26 06:35:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 49a6bc26-9580-34c3-91b4-db4449e51599 | -3.29091 | -52.54066 | 2025-10-26 06:35:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 930c966c-bfb1-3ee6-ab96-aa946a2a3939 | -1.19604 | -53.37827 | 2025-10-26 06:35:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04a1b881-f231-374f-b0ea-9d2de55be15c | -3.09021 | -49.46302 | 2025-10-26 06:35:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 251a1a1e-ec2a-36e9-b882-ae2356ed34f3 | -2.31716 | -48.58897 | 2025-10-26 06:35:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f6a7f525-3ef8-36cb-89e5-9de7e1188334 | -4.96761 | -56.26262 | 2025-10-26 06:37:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0bca8574-2c3e-36ba-908b-9042d4809103 | -10.89118 | -48.0162 | 2025-10-26 06:37:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| f1c97c0e-f11e-321b-b3e3-8c91f2695f27 | -10.94723 | -48.05668 | 2025-10-26 06:37:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 9edc1a0d-1b72-3998-863d-abadb7fb1b27 | -10.89375 | -48.0094 | 2025-10-26 06:37:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1772d950-5e44-3cf2-b241-043add07b9ea | -10.94818 | -48.05193 | 2025-10-26 06:37:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 8dc82a1d-122b-36ad-adef-69683eb66ea2 | -6.39089 | -45.75885 | 2025-10-26 06:37:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 13d5ace1-17e6-33ce-80ba-5dbba1c025f3 | -15.83537 | -53.57559 | 2025-10-26 06:40:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 43.3 |
| f8c33177-cb9a-3191-ad55-aa4c4e18e241 | -15.8336 | -53.58892 | 2025-10-26 06:40:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fe870d37-a656-35ac-a3b6-eaea7f30e6ac | -14.83826 | -52.43515 | 2025-10-26 06:40:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dedc3401-4751-3c0c-8598-a42b13a93bd5 | -17.3165 | -43.643 | 2025-10-26 11:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 048afe17-257c-3503-9ca5-d570597a7806 | -11.738 | -50.2295 | 2025-10-26 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 806e4bb0-e2f0-3ab5-9155-03213eef6213 | -12.8712 | -48.6504 | 2025-10-26 11:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 9179da5e-5cf4-3d90-9b18-97c1a55de88b | -11.7377 | -50.2511 | 2025-10-26 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 67ab352e-5dce-39ca-b515-55ae8f75a0b4 | -3.84996 | -42.09242 | 2025-10-26 11:57:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 0a624c78-30c8-368d-9db5-450b70f21c8a | -5.61276 | -42.66885 | 2025-10-26 11:57:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |


[Clique aqui para ver as próximas entradas](README54.md)
