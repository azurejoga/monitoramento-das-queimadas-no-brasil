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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe35eda7-bc48-379d-9e8c-ddc1993983be | -10.0964 | -45.728 | 2026-09-08 13:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| f679a069-395e-3366-86a5-ac5f62e6aeb9 | -9.7695 | -43.506 | 2026-09-08 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| dca53aa3-be56-3cec-8dbc-9c08cfbb3c50 | -8.691 | -44.727 | 2026-09-08 13:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 4be185c7-ecef-33c6-9a81-cf64fb8d7028 | -9.7705 | -43.4354 | 2026-09-08 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| bb01b783-2b55-3bea-afda-44dd14ce018d | -3.5407 | -48.1673 | 2026-09-08 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 156.6 |
| cb7b3fc0-b71a-3b9f-a3a4-e9d9bb7ef11b | -9.7698 | -43.4825 | 2026-09-08 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 287.3 |
| e7be6dbe-1f97-393a-8e8c-dbb751b59a9b | -7.6968 | -44.3247 | 2026-09-08 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 204.9 |
| f41474c3-a19e-3392-bdd6-33445f6e5413 | -9.7141 | -43.3956 | 2026-09-08 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 4507703f-0c63-36c0-a74c-a827edf033f4 | -9.7508 | -43.485 | 2026-09-08 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 2a879d1a-5f3b-3236-bead-3066b2bf5bdb | -10.8233 | -60.8019 | 2026-09-08 13:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| d9cb669d-aede-3ca1-8820-71754ab40cf2 | -11.3521 | -45.7465 | 2026-09-08 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 3d3c731f-15b3-34c6-9935-5df72fce6671 | -7.6779 | -44.3266 | 2026-09-08 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 6675f8df-eee6-39df-b5fa-e51a1be802bf | -7.6965 | -44.3478 | 2026-09-08 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 2f3706d9-ba15-3b6c-ad54-3145551390d4 | -3.5592 | -48.1666 | 2026-09-08 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| fa22ae86-5268-31b8-89d6-8d870d327791 | -3.5406 | -48.1889 | 2026-09-08 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 182.2 |
| 16e112c7-db66-3224-9f1f-af2e30b21761 | -9.7702 | -43.4589 | 2026-09-08 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| b2a830cc-2a59-3064-b87f-ad68cb3fd9f3 | -9.7131 | -43.4664 | 2026-09-08 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 334.4 |
| b2f0369c-d51f-36da-886d-5ded137edc93 | -9.694 | -43.4688 | 2026-09-08 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 125.4 |
| dae3a72d-e54f-311c-b6bd-62fb34cd99ee | -2.7582 | -49.4771 | 2026-09-08 13:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 3728ccc2-7bae-3696-b09f-e3bcdee2f651 | -7.697 | -44.3016 | 2026-09-08 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| f623266d-ee04-394d-9da7-7673e3dcbc68 | -9.7138 | -43.4192 | 2026-09-08 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 111.5 |
| ae9125d7-3b26-3fa2-a6dc-edddcac2b995 | -9.7705 | -43.4354 | 2026-09-08 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 748a77e4-c765-329c-b801-da86e75e1824 | -7.6779 | -44.3266 | 2026-09-08 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| f6b80f28-6c90-3fb5-a1ca-07baea7b679d | -9.7702 | -43.4589 | 2026-09-08 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| cbc703d2-37cb-3b10-8b88-4ad5df5fe6f8 | -9.7141 | -43.3956 | 2026-09-08 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 206fc70e-f4d9-3eb5-bae7-ac0343c981e7 | -10.8233 | -60.8019 | 2026-09-08 13:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 1435e8b8-995e-3c03-bb47-f84cfcd7fde7 | -7.7156 | -44.3228 | 2026-09-08 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 5f02ddc5-f8ba-36f3-90eb-1b26a3d33ea2 | -7.697 | -44.3016 | 2026-09-08 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 3d6aeb8b-f783-3efc-a4c6-31527cc55daf | -3.5407 | -48.1673 | 2026-09-08 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 186.0 |
| fbf69ca9-3b4d-3e16-99bd-4ab860fb8d2a | -3.5406 | -48.1889 | 2026-09-08 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 215.6 |
| bdd67802-e88e-32fe-b00c-db1b77230590 | -2.7582 | -49.4771 | 2026-09-08 13:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 565a2eb2-1730-3876-8f35-5e34b0dbdcf9 | -7.6968 | -44.3247 | 2026-09-08 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 174.0 |
| aaa7642a-35a4-381f-8dfc-b440ffe19b24 | -3.5592 | -48.1666 | 2026-09-08 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| fce0a4f8-96c1-3784-878f-9bf5976ab403 | -7.6965 | -44.3478 | 2026-09-08 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| a4ef9bd5-8694-3e51-9877-8ec30d0d8c87 | -2.7582 | -49.4983 | 2026-09-08 13:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d01114fd-f4b4-3542-a1da-2e540cdd3bd1 | -9.7138 | -43.4192 | 2026-09-08 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 138.4 |
| 9074dfb3-284b-340c-8267-b3808724b144 | -10.0964 | -45.728 | 2026-09-08 13:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 778af4a0-f655-3b90-813e-60f067140e4a | -10.0964 | -45.728 | 2026-09-08 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 251.5 |
| 2e4806dd-a2d5-3a41-b719-1dcef688c1c9 | -3.5406 | -48.1889 | 2026-09-08 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 275.1 |
| 0454837c-f186-39c9-9109-62ed9daef9c4 | -10.8233 | -60.8019 | 2026-09-08 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 147.8 |
| af288e23-140e-3572-9daa-ac404327b33d | -10.7862 | -60.7655 | 2026-09-08 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 95d721f4-5f85-3cf8-9720-7b6bb7e3050e | -5.1812 | -59.7648 | 2026-09-08 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 84ac7a7e-e2ce-34e1-a2c5-50b7d989043d | -3.5407 | -48.1673 | 2026-09-08 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 213.0 |
| c477dac7-f15a-3909-97af-7ccf1b6e1772 | -9.7141 | -43.3956 | 2026-09-08 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 126.2 |
| 251b4fff-8fe1-3413-9137-51af9c0c2c06 | -7.697 | -44.3016 | 2026-09-08 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 465caef6-2bf7-3be3-b328-c63a918aab37 | -3.5592 | -48.1666 | 2026-09-08 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| e2f9cc91-a420-3a8c-bd4f-76fea1e2ed33 | -10.1155 | -45.7257 | 2026-09-08 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| c0a2504c-f6c1-34b4-89a5-ba563d2fdd4c | -2.7582 | -49.4771 | 2026-09-08 13:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| c2d7f0df-39e6-3882-82c4-e420a9fbda3f | -10.7674 | -60.7666 | 2026-09-08 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5cd726b4-a2de-30b7-a89a-0d05de2aff8a | -10.0968 | -45.7053 | 2026-09-08 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ced06a87-ee77-31e0-97d6-162de423262f | -9.7705 | -43.4354 | 2026-09-08 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 61fb12c8-d514-39f7-ad25-60f1601b9ccb | -7.6968 | -44.3247 | 2026-09-08 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| c2214335-5b17-3708-928f-520b3205c1c4 | -3.8289 | -53.7634 | 2026-09-08 13:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 162.3 |
| e01eb56f-9196-3f8a-bc3b-499ddf224061 | -10.0964 | -45.728 | 2026-09-08 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 266.2 |
| 2b2c5b97-ea08-3a41-9a00-80d68ba3cc81 | -2.7398 | -49.4776 | 2026-09-08 13:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 37c30a5c-756d-3688-9fda-c222e7c2ca90 | -10.7674 | -60.7666 | 2026-09-08 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 47443b02-ab9c-3190-9129-1ac1560b6a8b | -9.7141 | -43.3956 | 2026-09-08 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 191.8 |
| 024e0f5c-3ad6-3525-bce6-79a05d386319 | -3.5592 | -48.1666 | 2026-09-08 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 83b69b6a-1ac7-3f16-b1d7-c3c3159a1b84 | -10.1155 | -45.7257 | 2026-09-08 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 8bc19ce1-0d10-3f2d-a221-5e7402a2f1ea | -7.6968 | -44.3247 | 2026-09-08 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 9fe19600-0553-3e5e-a688-a1d1cdd4477d | -3.5406 | -48.1889 | 2026-09-08 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 210.1 |
| 45e88385-e140-3d00-8a39-2d7478f3d215 | -3.5407 | -48.1673 | 2026-09-08 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 7443971e-ee3b-3f33-a6ac-9bf543b56372 | -10.7676 | -60.7472 | 2026-09-08 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 2e889914-26e7-316c-a42c-d5b2c6cc00b3 | -2.7582 | -49.4983 | 2026-09-08 13:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| da9b5b2e-bdbb-32a0-b368-1fc3c86eea0b | -10.7862 | -60.7655 | 2026-09-08 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 08a4d355-792d-3fbc-a790-b3bed2015cbe | -2.7582 | -49.4771 | 2026-09-08 13:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 2d1fe9c9-430d-336d-a668-4ae80ff56e6f | -10.8233 | -60.8019 | 2026-09-08 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a07a0025-2916-3b39-9311-b3e7e4e188e4 | -2.7398 | -49.4776 | 2026-09-08 14:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 43c0b2c8-29ea-3b00-8297-4750b5c2af0e | -10.7676 | -60.7472 | 2026-09-08 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 6a462162-a6d3-3026-be66-0994625ce036 | -10.8233 | -60.8019 | 2026-09-08 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 05c9acff-06be-3907-8627-941c183d6969 | -5.1812 | -59.7648 | 2026-09-08 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f7833271-e473-31ab-b660-3bf9ed2f9e22 | -10.0964 | -45.728 | 2026-09-08 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 3a2b95ee-60c7-3c6b-8a1d-bf034385629e | -1.1991 | -55.7501 | 2026-09-08 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| dbea405b-fbfd-3a4b-98b1-850eafccc7a8 | -3.5406 | -48.1889 | 2026-09-08 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 662bd200-6334-35ba-90e7-a71a431fce7c | -2.7582 | -49.4771 | 2026-09-08 14:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| bde499c0-16d1-34a3-a4d5-d3f94081fec4 | -8.691 | -44.727 | 2026-09-08 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d8fc2d7c-8525-3f21-9e27-ef841e594c47 | -3.5407 | -48.1673 | 2026-09-08 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 2a7d0039-12b8-3898-805b-0f85c7296678 | -9.7705 | -43.4354 | 2026-09-08 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 06ef31fa-23ca-31ac-9ad4-724689b1e198 | -10.7862 | -60.7655 | 2026-09-08 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 931c637f-149b-3370-a5e1-a924aa9b98fa | -10.7674 | -60.7666 | 2026-09-08 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 49ef9f3f-fd2f-3d25-a219-c46fbce253de | -2.7582 | -49.4983 | 2026-09-08 14:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| c131e32d-9173-324d-b913-f6fe5607f6dc | -3.5592 | -48.1666 | 2026-09-08 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 73eb0b6f-4a5e-3ddc-a974-9162c7591463 | -7.6968 | -44.3247 | 2026-09-08 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 3a3cce83-c02f-34f1-b98d-776da3f95dcb | -10.7676 | -60.7472 | 2026-09-08 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 162f5289-1d8a-3c60-8cb7-d92542279629 | -7.697 | -44.3016 | 2026-09-08 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d244523c-502a-35bb-aa13-b05f0ff9bf14 | -3.8289 | -53.7634 | 2026-09-08 14:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| f3a1dc59-36f6-341b-9b7a-e95b95d10058 | -3.5407 | -48.1673 | 2026-09-08 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 74671dee-cdf6-3943-ad01-41b58b1cb130 | -10.786 | -60.7848 | 2026-09-08 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5771ade1-c123-36fd-811d-560ae774bf44 | -10.8233 | -60.8019 | 2026-09-08 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 80d64bd0-5326-3bbb-b31c-56297c15bd6f | -10.0964 | -45.728 | 2026-09-08 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| f5eb4a1d-dcaf-37a4-83b9-833999939ec5 | -7.6968 | -44.3247 | 2026-09-08 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 593f0f82-c840-387b-9a63-b72ebaf38d9f | -3.5406 | -48.1889 | 2026-09-08 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| e976027d-b645-3ee0-aa8f-f7ef9c7c5fdc | -10.7674 | -60.7666 | 2026-09-08 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 5f7aa7c5-3f97-300a-accb-99875195820e | -10.7862 | -60.7655 | 2026-09-08 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 43167912-4c56-3e39-a4e4-4dae45fd4e98 | -9.72 | -43.46 | 2026-09-08 14:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 78024af5-08c8-3482-a246-d052759b2618 | -10.71 | -45.97 | 2026-09-08 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a70a58de-5edf-3d40-8c20-aca9fff24c1c | -10.71 | -45.92 | 2026-09-08 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c652c0f-720e-3183-b8a4-0443959dffe7 | -9.77 | -43.48 | 2026-09-08 14:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9443ae61-fb9a-366e-acaf-613589a81c19 | -10.786 | -60.7848 | 2026-09-08 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ade24a2f-e3d3-3e0c-8730-72524c02418c | -7.6968 | -44.3247 | 2026-09-08 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 207.2 |


[Clique aqui para ver as próximas entradas](README29.md)
