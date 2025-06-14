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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcef6731-7469-38aa-b945-f3a4b80143b1 | -10.9355 | -56.8322 | 2025-06-14 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 15d441dc-2807-3f34-a60b-a96de7b16ad1 | -7.2214 | -43.1153 | 2025-06-14 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 9ab5da8e-db7a-32b0-871d-9b266725a561 | -6.9416 | -42.8834 | 2025-06-14 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| cdc09ea8-309c-3bf5-91a4-c6b91e7ee92f | -6.9605 | -42.8816 | 2025-06-14 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 03075ffc-3027-3caa-9255-02978402c2e6 | -21.4315 | -54.5711 | 2025-06-14 01:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 3b7bee52-0c9b-327e-b80a-7a00591c4051 | -11.8158 | -57.3413 | 2025-06-14 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 88184c92-af1c-3cfd-807e-f69b11d3c73b | -13.9062 | -54.6084 | 2025-06-14 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 411752a8-38f5-3158-a902-6596229fb248 | -14.2121 | -57.4098 | 2025-06-14 01:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7802d96f-0fbe-3983-8a60-01367d8cabb5 | -10.9205 | -54.7795 | 2025-06-14 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| b2fc75aa-0200-3e7c-bbda-e6b4603de893 | -21.452 | -54.5675 | 2025-06-14 01:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 18d2355b-91bc-3dbd-a9ae-a9d8e2933d58 | -6.9414 | -42.907 | 2025-06-14 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| dca0ca2f-6796-3b77-bb64-cab1fdd77a55 | -13.887 | -54.6106 | 2025-06-14 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 3c6d1830-91ea-3fe1-a4de-7479ada907f9 | -7.4575 | -45.5116 | 2025-06-14 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 015a4c93-2539-3590-82d7-318a12e429b6 | -6.9605 | -42.8816 | 2025-06-14 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| dc587d11-c9b4-3c2c-b86d-dab744dcba9b | -10.9353 | -56.8522 | 2025-06-14 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 0b89d758-e063-3a53-8d08-0ba1e2525e4c | -21.4315 | -54.5711 | 2025-06-14 01:30:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ab6b6b83-9680-360c-ab76-46efbb4689d7 | -11.7969 | -57.3428 | 2025-06-14 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 5421bc69-2c4c-3bb3-a624-0164c0cf03b0 | -10.9355 | -56.8322 | 2025-06-14 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 586ed93f-42d5-3eee-99ee-77da8c72aa59 | -13.9062 | -54.6084 | 2025-06-14 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f5e73d59-4d0b-3195-8de3-1de21a063980 | -10.9205 | -54.7795 | 2025-06-14 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a74629c6-222a-35c2-a1cf-711bc3836f25 | -11.011 | -55.0967 | 2025-06-14 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3237ead4-a834-38d9-b9e9-0f1f6446557a | -13.887 | -54.6106 | 2025-06-14 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| d28c0939-9f9b-39b3-8d7c-ecdacd71219c | -21.452 | -54.5675 | 2025-06-14 01:30:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 085a9c86-215e-3ca2-a7f4-426a2f199866 | -14.2121 | -57.4098 | 2025-06-14 01:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e2870aba-d347-30b0-a098-d5fff3175db4 | -7.2214 | -43.1153 | 2025-06-14 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 75fcf525-08a2-3926-b845-73a6c0f4956b | -6.9602 | -42.9052 | 2025-06-14 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 86289ebd-8816-3795-9455-ed5fef6fc9b9 | -11.0113 | -55.0764 | 2025-06-14 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0e85825e-c8e7-32c8-aa11-e1ad94b75262 | -21.44411 | -54.58527 | 2025-06-14 01:34:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 9ec33cc7-e81c-39a8-969d-45d91158adcb | -21.44106 | -54.56789 | 2025-06-14 01:34:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 055abcc7-aa77-3aa4-a7b3-3a99daeed522 | -14.21277 | -57.41439 | 2025-06-14 01:37:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 0bb08300-7e1c-357d-a007-06c2fca5085b | -13.88951 | -54.60974 | 2025-06-14 01:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b3ecd43b-faa5-3814-af21-2a55c7f77eba | -14.20364 | -57.40967 | 2025-06-14 01:37:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| ffc1cbf8-b0cb-3c28-8ccc-2d200ac021f2 | -14.21055 | -57.40008 | 2025-06-14 01:37:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 540031e9-7ad7-33d7-838e-b5dd6f182a65 | -16.14246 | -60.07547 | 2025-06-14 01:37:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3b775e1b-8e5b-3d28-91df-e38c7595e480 | -14.85184 | -59.82278 | 2025-06-14 01:37:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 54569b7c-9565-3f6d-978b-6c6b28712062 | -14.21452 | -57.40769 | 2025-06-14 01:37:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| c9c6d787-c512-3390-aa95-9893ebda56f1 | -14.2019 | -57.41643 | 2025-06-14 01:37:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c2597a94-08ea-3fa6-9ac9-b0d68742a647 | -14.22538 | -57.40554 | 2025-06-14 01:37:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b267bf73-6600-376d-a7e1-d22b5b52ae6b | -16.14387 | -60.08516 | 2025-06-14 01:37:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1d85ef9a-0003-369e-9ca6-a6fd55f76bb7 | -13.90314 | -54.60715 | 2025-06-14 01:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 41093d4b-535a-3f85-b25e-5ba13c8d4215 | -14.21683 | -57.4219 | 2025-06-14 01:37:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1446cb2a-a06f-3c05-9640-4ffce3c23a16 | -13.89361 | -54.63366 | 2025-06-14 01:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 56a94ce3-6bcd-3ab5-ac64-5f0877a869d5 | -13.90719 | -54.63092 | 2025-06-14 01:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 80448a56-7382-372b-b629-4f4e3023b4ca | -10.29906 | -60.55077 | 2025-06-14 01:39:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 97fb0ca5-dc01-3c02-b322-25b5da9be4bf | -10.28967 | -60.55225 | 2025-06-14 01:39:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| acd1ca80-f7ef-330a-b797-405ae3f63c48 | -10.09422 | -52.7417 | 2025-06-14 01:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 7e5b1abf-487c-3bd6-a6c2-2b26f74d9f27 | -12.61424 | -57.88109 | 2025-06-14 01:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 07f08ef0-9463-32fd-9423-c2a4cf2cfa98 | -10.91575 | -54.78418 | 2025-06-14 01:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e5d67ea1-3221-3f88-a9a7-343ec918fda5 | -10.94172 | -56.84027 | 2025-06-14 01:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1a9752a5-be60-32c7-ae68-9cb26cd3336b | -10.92323 | -54.762 | 2025-06-14 01:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 25ef3e41-7337-3caf-a781-cfc2b93db5bb | -12.62719 | -57.8932 | 2025-06-14 01:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| caf57697-18a3-3c91-bce4-b3b608cb03e8 | -12.27641 | -57.26669 | 2025-06-14 01:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9813bb93-ac00-30ab-8bc3-2e4413fe6e26 | -9.46484 | -57.84493 | 2025-06-14 01:39:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 33.7 |
| d0cd6be8-139b-3a81-85ca-faa8224962a8 | -12.27892 | -57.28232 | 2025-06-14 01:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| dc0a8ec0-7043-34f9-94d6-226aebc9f85b | -12.6211 | -57.90194 | 2025-06-14 01:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 26e7cb3d-2986-390f-8f19-d9f73612e513 | -12.61889 | -57.88817 | 2025-06-14 01:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| b31be78d-abf9-3676-bc95-790bf3a1d52f | -10.92963 | -56.84245 | 2025-06-14 01:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 34dc43e1-82ac-35c3-b45d-bf4350c76dcf | -9.46723 | -57.86064 | 2025-06-14 01:39:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 08a69948-4c00-3977-82a5-cb97c1c30786 | -11.79527 | -57.35135 | 2025-06-14 01:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| af772b6b-7aab-3a51-821f-6ce59ecca528 | -11.8155 | -57.34133 | 2025-06-14 01:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3e7d72e8-d892-3005-8645-070dadd5a0cc | -11.00922 | -55.07886 | 2025-06-14 01:39:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 00327f0b-0de1-36e8-aba7-d19f06bc73d1 | -11.80406 | -57.34328 | 2025-06-14 01:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 35dbe13d-a668-33ee-a021-eff194881666 | -10.30056 | -60.56106 | 2025-06-14 01:39:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6e741610-63b9-39ce-aa6e-e64adf49037e | -9.87847 | -61.40293 | 2025-06-14 01:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 49e9cd67-df23-3e0c-a2e3-009d3de94baf | -10.29119 | -60.56263 | 2025-06-14 01:39:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a9ba342c-0365-36cb-81f1-ccaf31297e2b | -9.87982 | -61.41239 | 2025-06-14 01:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e6cdde27-9172-385e-b906-684fb0b58431 | -10.92677 | -56.82463 | 2025-06-14 01:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f7b66a91-5940-3857-b4c1-01c8de479351 | -12.61638 | -57.89503 | 2025-06-14 01:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| cf404484-219d-3d69-b865-9b351d13f69c | -10.91316 | -54.79018 | 2025-06-14 01:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4a2e572e-870f-3a81-8723-0d2fdeb1ae6b | -11.0132 | -55.10272 | 2025-06-14 01:39:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ffbdc16f-3b4a-3258-8732-811e03343840 | -11.80673 | -57.34946 | 2025-06-14 01:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| ea465a0f-ab58-3cd5-9a8c-ed5a307166bb | -10.92745 | -54.78785 | 2025-06-14 01:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d37339b4-af12-34a7-a90c-8039f2301b31 | -9.39163 | -57.5245 | 2025-06-14 01:39:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f9c78fc1-1b3d-3f26-a173-e50f9fb9fdb4 | -10.93243 | -56.85996 | 2025-06-14 01:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2ab11f35-5a45-3b40-ae9f-fab128d382d5 | -11.91729 | -57.46837 | 2025-06-14 01:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6f1c1916-3df8-3832-afc0-cd93fda4a703 | -10.91749 | -56.84438 | 2025-06-14 01:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 75a2c33d-190b-35ed-9e21-54aab8a3fc06 | -11.80663 | -57.35918 | 2025-06-14 01:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d1cded5a-1dc0-37fa-9066-73c83dcaa75b | -11.7969 | -57.3428 | 2025-06-14 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 87aea5f7-95f6-3d8c-b48b-80858082c8de | -6.9602 | -42.9052 | 2025-06-14 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 35219d9d-c6ac-3496-aa13-846ed87dcebe | -14.2121 | -57.4098 | 2025-06-14 01:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e56c82bf-91a4-3943-81a4-ad76cbb42dab | -10.9353 | -56.8522 | 2025-06-14 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| aadea182-c7c0-3c1c-960c-d3fb9747372a | -7.4575 | -45.5116 | 2025-06-14 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| e4ac69cd-2efa-3f4f-a8c7-7430aa0b8c3c | -21.452 | -54.5675 | 2025-06-14 01:40:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c3b02088-1d14-3b74-bbe3-a3bc3b525136 | -16.1967 | -46.4589 | 2025-06-14 01:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| e551d358-7aa9-308d-a025-6cbce9c7f156 | -10.9167 | -56.8336 | 2025-06-14 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| be57606b-bbec-3f6c-a6be-e9dc3f6afcc7 | -11.0113 | -55.0764 | 2025-06-14 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b52fd6d2-67e6-3690-a7da-cae40d258273 | -10.9205 | -54.7795 | 2025-06-14 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 5203a2c3-cc50-385e-8c76-84fc1dff1753 | -13.9062 | -54.6084 | 2025-06-14 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| c8b5d4fe-296d-3173-b73a-3ee959a876b6 | -10.9355 | -56.8322 | 2025-06-14 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 10eacff1-54d4-3aed-9045-a864a7e26562 | -13.887 | -54.6106 | 2025-06-14 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 089d933e-87c1-3f1a-a1bf-a4ac482e70bc | -21.4315 | -54.5711 | 2025-06-14 01:40:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 65.5 |
| e0f99583-aa88-3df7-99f3-9bfd307cbae5 | -6.9605 | -42.8816 | 2025-06-14 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| a40927ba-ea23-3b36-b59d-061c7fca49f1 | -10.9322 | -54.7812 | 2025-06-14 01:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abd2e634-761f-3248-9da2-ccc86e6eaa51 | -11.823 | -57.357201 | 2025-06-14 01:42:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 077efc02-0dbd-344f-ae78-2ea9c173195a | -21.4575 | -54.573799 | 2025-06-14 01:42:00 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 85b61120-7064-3d29-ac61-0de05dc2d964 | -10.9441 | -56.859402 | 2025-06-14 01:42:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 297e83b0-c5d4-32fd-a5d5-ef8122d677b7 | -11.0214 | -55.0872 | 2025-06-14 01:42:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38d69465-a774-3d4a-a6e2-ac6f649c2159 | -10.9277 | -54.763599 | 2025-06-14 01:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3896fb5b-853d-3548-956b-b49cbac565e4 | -14.214 | -57.400799 | 2025-06-14 01:42:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4be42197-d908-3e7b-aec9-642255ffed54 | -9.3953 | -57.5275 | 2025-06-14 01:42:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
