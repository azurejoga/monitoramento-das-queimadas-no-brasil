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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 959c7120-7ef6-3688-9a8e-fe516044daa9 | -9.2023 | -60.787102 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e10d1a2-ad19-3214-b607-688b404497c0 | -9.5195 | -60.519001 | 2025-08-24 01:24:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 332bf01a-4088-3c0e-88e2-c787dd58cc1b | -6.919 | -62.9081 | 2025-08-24 01:24:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6652adfd-1222-347d-bbc9-02fb5c568f17 | -14.8032 | -59.603901 | 2025-08-24 01:24:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f86a1bfa-d32e-3751-8ce0-171458a16651 | -8.9166 | -62.410801 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ff86c096-51b0-373e-8210-9ca3d93823fb | -16.783701 | -51.358501 | 2025-08-24 01:24:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 868df30e-50d0-3170-8c40-c3944c5909a6 | -9.1686 | -60.8186 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1fc60dc8-12de-3356-b99f-2eddeb026f29 | -16.7742 | -51.3615 | 2025-08-24 01:24:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 68214a25-2f7e-3b21-9b8f-93b8a9b8794d | -9.1929 | -59.469002 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e69dced1-9b22-36dd-b0f6-dedccc443b13 | -9.0351 | -65.711601 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e53ceff0-5b03-37dd-84eb-93b5710fc378 | -8.9956 | -63.636501 | 2025-08-24 01:24:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d35ed08-1a2e-3ea3-8a62-6263ad551214 | -9.1441 | -59.437901 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b12aab4-1d10-38cd-af16-598c7baff4bf | -9.1288 | -60.781399 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 852cf3cf-a2ca-3fa0-befc-8dadfac97c0f | -9.0154 | -65.716103 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd4aeee-ca77-3105-866a-33cb4e54cb76 | -6.6879 | -58.861099 | 2025-08-24 01:24:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6b9436f-3ca0-3b3a-806c-c68aecc727e5 | -8.1359 | -62.865002 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 588750bf-e3b6-3154-8f9b-0a74989cba47 | -8.5871 | -68.147598 | 2025-08-24 01:24:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca3294ec-086b-380e-a262-b475151a0d49 | -9.4932 | -68.964798 | 2025-08-24 01:24:00 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e20c402f-2020-3192-a11f-80fe9ebbbe00 | -7.943 | -63.055401 | 2025-08-24 01:24:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ffd6e4a-ec00-39f3-adb7-9c0bfbc256fd | -8.1338 | -62.8563 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| edea894e-7e52-3fe8-9533-e3b33c659cf0 | -20.3349 | -51.677898 | 2025-08-24 01:24:00 | METOP-B | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 649d37f2-507e-31ef-9e55-67cbfb61287c | -9.0336 | -65.704597 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34904421-70a5-3d2c-a707-db861ea07d0e | -11.9959 | -61.030399 | 2025-08-24 01:24:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d2ef9ca5-9232-3076-8d85-e85fa2a0b7dc | -8.6842 | -62.8727 | 2025-08-24 01:24:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77d201bf-df35-369d-a4d6-e6b8fdfd3515 | -9.0139 | -65.709099 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 478e815a-5887-3964-ab8c-f6801bf42dab | -8.6373 | -62.627102 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2da72a44-e18a-3b90-b054-41496629d909 | -9.1898 | -59.625599 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5cb92d4-3d4b-3b4c-b845-9547576e5358 | -9.1873 | -60.7672 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b28305f-c975-3c44-b6ab-a0f101dd6a9c | -9.0661 | -65.711899 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 036d6a47-13f0-3a07-9fb0-2abc3d1276b3 | -7.5508 | -63.855301 | 2025-08-24 01:24:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b26ead6c-2d3f-369c-8508-4522bc7d9a8d | -9.0248 | -65.391701 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 436aeccc-a37c-3ec1-9929-753e43245485 | -6.3035 | -59.866901 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a5554ee-09da-39c9-80fe-074549e4b8c8 | -8.8992 | -62.4244 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de395c5c-9c00-3d2d-9839-893327e3a420 | -9.1757 | -60.805302 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 368f8fa5-321c-3b6d-ac79-9e8852d93b0d | -11.9936 | -61.020599 | 2025-08-24 01:24:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 287a82a2-3dc8-3da4-a5ed-bc86be5772c3 | -9.7245 | -65.708702 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aec11ed5-52d0-3cc8-80cc-1818416de37c | -9.1443 | -59.480999 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7101ba0-4adc-38d5-a51f-496f31b7a9aa | -7.567 | -63.4347 | 2025-08-24 01:24:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8842c056-fa9d-3f56-8ce8-fcc6a26eece7 | -8.6054 | -62.578602 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 62904dd4-0d59-3572-9ab1-60e84c9de0c7 | -9.8076 | -61.204498 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4be61e8-c006-35c1-a2b1-2cd1adaf2757 | -9.1573 | -59.4921 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b1b2f6f-1b6a-391b-a446-5c7127e63f53 | -9.6324 | -63.090599 | 2025-08-24 01:24:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6063a453-4371-353d-8c5f-89d82400592c | -9.0269 | -65.720802 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84c218e0-8294-32c9-9d5d-d92fef89c489 | -9.0135 | -65.386902 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fcd48df3-50aa-363a-9d6a-7d59942eafc0 | -9.0253 | -65.713898 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4fe37675-97ec-3899-8896-90317254602f | -9.1261 | -60.770302 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f773d83d-c8e1-367a-ab79-1864b0ef4506 | -10.423 | -64.420502 | 2025-08-24 01:24:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a814f524-3c43-353a-bd5d-c5a2a527f0ed | -9.1377 | -59.453899 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 483fae62-1e8a-34d3-a693-ad24a311c28f | -20.325399 | -51.681 | 2025-08-24 01:24:00 | METOP-B | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 171fd1eb-5a59-34c5-a1f8-973a6fffa8fa | -9.4741 | -63.119301 | 2025-08-24 01:24:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8dabcb9d-79c6-3814-b5d5-4a991e156c12 | -9.2049 | -60.798199 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abe0be32-4fc1-391f-95ad-c8f28a37e5d3 | -8.6862 | -62.881199 | 2025-08-24 01:24:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 64e7674b-92a6-35f9-a1ef-011d988d6017 | -9.1799 | -59.457802 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb72896f-9205-30bc-9195-d6a06e377718 | -9.0041 | -65.711304 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5d6d74c-eec6-3302-8d7c-7a1c7ab680fc | -8.9056 | -62.451302 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bdace101-04c5-39d7-932f-6408b249491f | -7.9666 | -63.067799 | 2025-08-24 01:24:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eea44948-f8cf-3c04-a836-445adc33cf71 | -8.5899 | -62.601002 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1f32a6d-4a02-36c6-8dd6-60bbe7d3b4e5 | -12.5896 | -60.363499 | 2025-08-24 01:24:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da3ad6a5-2345-390f-b97b-d06ff400a3b7 | -11.9838 | -61.022999 | 2025-08-24 01:24:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eee40406-628d-316e-8c2b-7e2b68629cce | -5.445 | -60.189701 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de586c99-2c46-36d8-8957-adcad1681c1d | -9.1734 | -59.473801 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f4b8097-98cc-38f3-a6cd-c77495d54406 | -8.9937 | -63.6287 | 2025-08-24 01:24:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 69000b5f-7527-3945-b8b4-a7d5afc19d2f | -9.1996 | -60.776001 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 338b5601-74f2-3afa-a104-7628bb45765a | -9.2414 | -60.477402 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d73b35d-a94c-30ec-b8e8-86742f3d22e6 | -6.6742 | -58.847099 | 2025-08-24 01:24:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31644e4d-aead-3840-ac8f-eb746fe7e875 | -9.1899 | -60.778301 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5116f074-150c-349a-8232-afdf83f5140d | -6.7438 | -62.8638 | 2025-08-24 01:24:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a28632f4-52fb-39bd-a650-e0e6d635cee0 | -14.7935 | -59.606499 | 2025-08-24 01:24:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e0464d7-c1a6-3c53-9eb1-5837147845da | -8.6352 | -62.618301 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 69ae9a97-9006-37af-8d42-4376b7e02a7e | -9.001 | -65.697403 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8df06f4e-3bbe-35e2-b4c2-254262c30708 | -8.696 | -62.878899 | 2025-08-24 01:24:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c762b45c-638f-38b9-b43d-4de7a4b915df | -9.1331 | -60.756699 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78520f0b-2fa3-328c-84b5-7a187867b429 | -8.909 | -62.4221 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 37682e49-a4ac-3b5d-bd1d-39b7e81b2e09 | -20.343201 | -51.706299 | 2025-08-24 01:24:00 | METOP-B | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 340ee4f7-f8af-3d30-bf34-e07d9ead24bc | -8.9994 | -65.690498 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e183e2cb-8a99-3c7a-9df3-650592337d34 | -14.7962 | -59.617401 | 2025-08-24 01:24:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af47721f-0ff4-3eb3-a0e5-fbfec69a0b7c | -9.0119 | -65.379898 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1251f4f5-1e45-3741-9423-e4f73c3f9107 | -5.4418 | -60.1759 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9f404d4-8963-3bba-9ea4-ee019537baf3 | -8.6275 | -62.629398 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 27453561-4003-3ac6-9df5-2a4e86a58a29 | -9.0289 | -65.6838 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de470bff-88df-3ce2-82da-16a53edac16b | -9.8211 | -64.267799 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4164719b-dad8-39f5-9156-1adcac2ede5e | -9.2364 | -60.929798 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cafd788c-34db-3572-988e-2e7db7be83dc | -9.2338 | -60.9189 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f2bf429-0f08-3af8-ab95-b8ecd2626325 | -11.9912 | -61.0107 | 2025-08-24 01:24:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1c695b1e-70af-3cfd-82a9-778330ee7cbc | -9.0092 | -65.688301 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d04ec0b-cfee-3e24-a155-3db5580de8ad | -8.895 | -62.406399 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ace5f1d6-d334-3267-8800-16d698489498 | -9.1659 | -60.807598 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6b688ad-e3dc-3f3b-8756-4a9e123278cf | -7.5453 | -63.831501 | 2025-08-24 01:24:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87c6bf19-33c8-3cf3-872d-3149aec3aee4 | -10.4213 | -64.4132 | 2025-08-24 01:24:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bf7af384-5060-306a-b40e-e346654a1b5c | -8.6121 | -62.6516 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 45044402-7f1f-34f9-8043-01f319809569 | -17.5982 | -44.2784 | 2025-08-24 01:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 531ae60a-ba00-3c96-a822-bb8efafcffbe | -9.1998 | -60.793 | 2025-08-24 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 20e26414-98d3-3902-b71d-976587cfbc9f | -14.8153 | -47.9343 | 2025-08-24 01:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ba2f4abf-e750-3396-a4be-43869c57129c | -20.3599 | -51.68 | 2025-08-24 01:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 38101dd8-ce67-3871-8d64-ee31359cb61f | -14.8157 | -47.9118 | 2025-08-24 01:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 06ac66c0-4bb6-3501-ba05-f1e7663c59c3 | -3.5995 | -47.5142 | 2025-08-24 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| dc7e161d-cd13-3983-971f-2b436587fac2 | -10.6128 | -44.3284 | 2025-08-24 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| c456fafd-95e5-357d-954a-f25cc16def5c | -9.0045 | -65.7174 | 2025-08-24 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| aad5b44f-3d8e-321b-8c3a-babf4d2d14d4 | -10.8078 | -46.4083 | 2025-08-24 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 903bc281-f17d-37ea-9596-4a67fbf914e1 | -11.5055 | -51.8705 | 2025-08-24 01:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |


[Clique aqui para ver as próximas entradas](README16.md)
