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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23f92832-c234-3cc9-aed6-282382561aea | -17.63523 | -57.58494 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| c0bf3d71-f589-3e07-ae18-e67bb8fb9414 | -20.90526 | -55.32755 | 2024-11-26 04:42:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26bd9e27-6d94-3d69-a482-0f681eb69531 | -20.47869 | -48.72157 | 2024-11-26 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7feaf8b-ffc4-371a-af79-9ccc1af0e9de | -21.56104 | -54.20341 | 2024-11-26 04:42:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 990fd071-0a77-3ac9-955b-f0188b987f88 | -21.32155 | -47.40489 | 2024-11-26 04:42:00 | NPP-375D | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ffb3f4c-f72c-3e56-b6f6-2b92879e9148 | -17.63308 | -57.58974 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2b13e375-3255-3194-8951-15408db77037 | -23.40616 | -46.55822 | 2024-11-26 04:42:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6523660e-b1d3-38e8-ab5e-73a6d9852761 | -20.80441 | -49.0355 | 2024-11-26 04:42:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| beb2b9da-770d-3ac3-9359-943e27670d65 | -21.56167 | -54.19958 | 2024-11-26 04:42:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61e2de8b-5111-3b32-b2e5-33d926c41030 | -19.67318 | -49.89536 | 2024-11-26 04:42:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2501eb26-f410-35e6-b91b-adc07c078200 | -20.76183 | -46.7692 | 2024-11-26 04:42:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 603aba54-df21-33c2-8fac-1fe68a2f4cc7 | -23.01702 | -50.4235 | 2024-11-26 04:42:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f2af36f5-5549-3a36-9d37-4c4c82e97bd4 | -17.64275 | -57.5905 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e1a87055-9c64-3cd3-9c50-615996c3be8a | -19.19078 | -52.31956 | 2024-11-26 04:42:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 761da76d-859e-33c2-b4b0-9bcbda0d04cf | -17.22708 | -54.4417 | 2024-11-26 04:42:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6801bec9-37bd-3b51-b9b4-358b8140606e | -17.70465 | -54.9437 | 2024-11-26 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64275f3b-e75a-34bd-a174-21a3946c3d82 | -21.37997 | -48.63264 | 2024-11-26 04:42:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eae504ad-2c8e-3b4a-b400-0061d60aaffa | -21.56441 | -54.20405 | 2024-11-26 04:42:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75fe0cd3-d928-38d8-813a-ccd26185e31f | -17.651 | -57.59217 | 2024-11-26 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e08db43a-d9e9-3d9f-b13a-4b77f983d37f | -20.64412 | -56.58458 | 2024-11-26 04:42:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 778925fd-f233-3912-8ee9-18e0467bb087 | -23.75 | -49.01128 | 2024-11-26 04:42:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2ad4e49-54ee-3d99-b06e-951a3a0af16a | -20.76396 | -54.30719 | 2024-11-26 04:42:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 366d06ed-8230-3ffe-ae0b-f12b659e0d06 | -24.73063 | -52.19655 | 2024-11-26 04:44:00 | NPP-375D | MATO RICO | PARANÁ | Brasil | 4115739 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6702d735-32b4-3972-a791-1be55f032f16 | -24.63744 | -51.00018 | 2024-11-26 04:44:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 3200c237-b45f-3931-8b0f-6359ec821f77 | -24.72724 | -52.19595 | 2024-11-26 04:44:00 | NPP-375D | MATO RICO | PARANÁ | Brasil | 4115739 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ad56875-d715-3c21-a1f3-ced0dbb40ea7 | -24.96227 | -49.22704 | 2024-11-26 04:44:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0c5a7190-efc3-3fae-8eca-714c70ac3f91 | -27.17471 | -50.83825 | 2024-11-26 04:44:00 | NPP-375D | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 27a7f42b-5df8-38ac-9d66-92b09f4a8f14 | -24.96609 | -49.22778 | 2024-11-26 04:44:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 78baeec4-bef7-37ab-a713-f6604d55b71a | -3.1691 | -48.4394 | 2024-11-26 04:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 74e78522-fa4f-3055-8fe7-e4c185ad3fc5 | -2.6943 | -51.9831 | 2024-11-26 04:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 16c61af8-44c2-30e7-956c-ed97b5794a8c | -3.1877 | -48.4172 | 2024-11-26 04:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 467e3123-332e-3110-a76e-7b2120130428 | -17.6453 | -57.5874 | 2024-11-26 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| d1c58222-0edc-3a01-ae7b-18f2224b3d27 | -3.1876 | -48.4387 | 2024-11-26 04:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 669dead6-0817-3f7f-bd09-d6d11cce461e | -1.63098 | -52.77146 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6086de8-c01f-3f69-988d-00b772155391 | -2.7108 | -46.25941 | 2024-11-26 04:59:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8983c7a1-f509-3aa7-bd7a-bcf109b26b22 | 0.69677 | -51.44151 | 2024-11-26 04:59:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63a90cbc-79ba-32c4-aba1-ce6442076d22 | -2.17553 | -45.60567 | 2024-11-26 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ccb3c5b-244d-3d77-a5a4-a578cbc28be6 | 0.67245 | -50.79751 | 2024-11-26 04:59:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77488898-ebc6-3809-8761-8ffea55715db | 0.67609 | -50.79694 | 2024-11-26 04:59:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02b15b5a-bf16-31d3-9013-877351f8a917 | -1.70109 | -47.72734 | 2024-11-26 04:59:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05a8beb1-5998-3dc2-a0ef-c99ce0379863 | -1.44073 | -52.44255 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb4e0f3b-c880-3230-8490-9523244518b4 | 0.73059 | -59.8158 | 2024-11-26 04:59:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd71cf03-5988-3eac-8f3f-35c808d802a0 | -2.17796 | -45.606 | 2024-11-26 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b9feaf1-6308-3498-bfdf-f3f7f9acb8fb | -1.79009 | -52.73884 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f7972ad4-d240-3e1a-93a6-177eeb770d47 | -1.11751 | -53.38922 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83c61a29-b0be-3332-b468-14354d9d646b | 4.24419 | -59.86063 | 2024-11-26 04:59:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 297bafbc-7598-34b1-a708-2a73c29abac0 | 0.48759 | -50.94957 | 2024-11-26 04:59:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ac52ba3-5043-3675-93b4-f56d251476c9 | -1.72059 | -53.24904 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4379891-f5de-35cd-bec4-e3173282ef2f | -1.21502 | -54.54223 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c35cef54-d73f-363f-913f-01d08764cb29 | -2.50065 | -48.35126 | 2024-11-26 04:59:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ca9d7c0-71a3-3ca2-9058-c669e818c5e5 | -1.71539 | -52.72399 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b03ab78-65e6-3c1f-a764-7a54c1d1e2ea | -1.12976 | -54.17715 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28cea72c-2c96-3970-8357-39ca951bb098 | 2.68321 | -60.42241 | 2024-11-26 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0f16a123-4680-33a7-b67f-53d65a067266 | 1.99732 | -50.80795 | 2024-11-26 04:59:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb229be1-4800-37f9-81b5-c1ca32b9f568 | 0.48397 | -50.95012 | 2024-11-26 04:59:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9af119d0-2e20-30b2-a9ab-0c006fb49bac | -1.27556 | -52.16866 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd3122a2-3479-3343-9966-670c8b7c8000 | -1.56379 | -45.68361 | 2024-11-26 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72e5616f-e684-3f27-b2be-262bb290977f | -1.77698 | -52.73304 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 061bb404-2730-38cb-a120-4ccd818ee682 | -1.78667 | -52.73831 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 72c28637-5b84-34aa-a280-91a521358deb | -1.35376 | -54.63395 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3267e9f7-ce57-3771-9ea0-bf9d3a85962a | -1.62157 | -52.44962 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 949c8943-101a-39bd-bb00-d2f5d57b1c96 | -2.57751 | -45.47455 | 2024-11-26 04:59:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd1c80be-dd0a-3bca-941d-0adce7579965 | -1.35322 | -54.63738 | 2024-11-26 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc424481-fe20-3f94-bd35-211b78692b56 | -2.54388 | -46.40747 | 2024-11-26 04:59:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7537b02-a874-3deb-9dd7-38921ca4cfb5 | -1.09904 | -53.6162 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efca81c1-f4bc-3274-9268-ab979a60fd65 | -2.71851 | -46.28972 | 2024-11-26 04:59:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d794803-539b-3634-96d8-a8c228ce5a82 | -1.30247 | -51.73577 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 452f78af-87b8-3236-8a75-205bc98c51df | -1.71598 | -52.72029 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d39c3230-25d4-3f98-8dcb-d64cde25f4b5 | -2.17602 | -45.60231 | 2024-11-26 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11442d54-b1db-339a-ab74-c4e6d170c0b7 | -2.17799 | -46.38644 | 2024-11-26 04:59:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bacf73e6-ca74-3547-b350-082e3d7a8f54 | 1.95194 | -60.8575 | 2024-11-26 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f219d3eb-f5b6-338e-b02b-5e734f0269b5 | 1.83107 | -55.97599 | 2024-11-26 04:59:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a2fa030-fe80-38cd-82a0-72c44be809f4 | -1.51637 | -52.63007 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dfeb7c7-4d88-394c-b734-f8497b50a052 | -1.61669 | -52.36743 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea295f80-f687-3d65-b622-d7a50c5963cf | -1.21556 | -54.5388 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9534185-939a-3b2e-ac3c-2bde6aa3cdef | -1.75308 | -52.66095 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04c23d91-ca52-394c-98ad-4ecdc8ca9796 | -2.71637 | -46.29179 | 2024-11-26 04:59:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4f2a5f3-dfbe-335c-977b-4a881c265470 | 1.93645 | -55.75063 | 2024-11-26 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44526a6a-993c-3490-bc72-d55e3ad1e398 | -2.31636 | -48.55444 | 2024-11-26 04:59:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ef45bc4-cc6e-33fe-b211-e25ac723bcf5 | -1.60047 | -47.46429 | 2024-11-26 04:59:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa6216c1-2995-357d-8c95-dffa4d3ec4ea | -1.23967 | -53.39007 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e800e06e-1b23-38cb-ae92-8f88677c1fe5 | -1.63804 | -53.3023 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3dab7e01-a178-3e8c-81ff-d27b2e56260b | -0.10661 | -51.7436 | 2024-11-26 04:59:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5317785-0e50-3707-aa41-54a6b83e176d | -1.44867 | -53.4217 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e8ca171-92cc-385f-9020-687dc183d86d | -1.77641 | -52.73673 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a08ec24-08cb-3156-bb4a-85b99bd450bc | -1.088 | -53.64312 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb5f2030-5c12-3e19-b4d7-1504d0baa8ba | -1.55706 | -53.79392 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1adadff-f11a-3331-9c46-cb5853bba5c0 | -1.78267 | -52.74149 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 815e4c1b-e31c-3952-b0f0-ac2156e46939 | -1.72424 | -52.48834 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7bf7a07-2088-3036-a434-e9896c04cd3c | -1.82558 | -46.28679 | 2024-11-26 04:59:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70930f95-5045-37d8-b8ac-98cc5af2885a | -1.62944 | -53.87287 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bee889ac-5acb-30c5-b5ef-0c5017c32ca7 | 0.67675 | -50.80117 | 2024-11-26 04:59:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c836cf12-bc17-3db0-a789-9322e7c7e56f | -1.48694 | -52.5263 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f73ef79-cb26-3e45-8739-f10753514053 | -1.78894 | -52.74624 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 707c4857-9d04-34dc-a7cd-16d62503d0ab | -2.58632 | -47.45236 | 2024-11-26 04:59:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d138399-27b4-3438-a46b-4b6a52236a22 | -1.48752 | -52.52256 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 492f27ff-5d99-329a-a0ad-a5c79162d352 | -1.21048 | -54.16203 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38976296-4281-371a-b0c9-62877bc7a7dc | -1.15914 | -53.66493 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2515aad-9329-3290-9058-77377bc0e019 | -1.39687 | -55.20077 | 2024-11-26 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f913709-15e5-3268-8a7f-fd7634445f23 | -0.87376 | -51.72289 | 2024-11-26 04:59:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README34.md)
