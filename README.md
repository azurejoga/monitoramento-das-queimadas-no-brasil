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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2e62ca0-997d-34c3-8c61-544c2cf66a3a | -12.7603 | -44.2608 | 2026-08-26 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| d5708809-5bf4-3937-92de-566731426db6 | -12.7802 | -44.2341 | 2026-08-26 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| e495df74-4294-383b-a05b-cbb179cca826 | -7.4036 | -55.1513 | 2026-08-26 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1b3ede5f-e3a2-3666-bce8-f3397aff1605 | -7.0796 | -59.2351 | 2026-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 302.2 |
| c8756094-73b3-3016-875a-ddd08d30fd37 | -2.5042 | -48.1366 | 2026-08-26 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c7335ef7-fed2-3739-bba7-96f418fdfc99 | -7.0799 | -59.1964 | 2026-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| a1859451-7278-3fa2-a842-a15511c7364a | -9.6212 | -55.1064 | 2026-08-26 00:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 3a4edf07-5542-3ed8-ad72-cd430993bb57 | -2.7948 | -49.582 | 2026-08-26 00:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d2d3dc65-fccd-326d-b76f-8dfb6bd96258 | -13.2259 | -51.504 | 2026-08-26 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 169831e3-454b-3446-977f-56c6e2c52826 | -13.2451 | -51.5016 | 2026-08-26 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c13479bd-52cc-3970-8210-5d64dbfec2f9 | -10.3723 | -45.0767 | 2026-08-26 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 6104b4d9-3482-3763-a6e0-a7f6ed84b9db | -7.0797 | -59.2157 | 2026-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 422.8 |
| 0acea348-221b-3977-a602-b835fdda03ed | -7.2856 | -44.0875 | 2026-08-26 00:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| ecc286f4-0c7d-370b-9e91-9223b69c4005 | -8.8185 | -62.3189 | 2026-08-26 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| aaa79d9d-8211-3add-8198-7cbd4c718b44 | -10.3727 | -45.0537 | 2026-08-26 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 270.2 |
| f874694f-873d-3327-af1b-a8c6dab4a25f | -7.0242 | -59.2374 | 2026-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ef866db1-0b06-3c9d-8fcc-782064db7219 | -13.2277 | -51.3973 | 2026-08-26 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 09ff0c77-b854-3bf9-b732-9066c25de9b5 | -10.9848 | -51.1655 | 2026-08-26 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 255cf297-f171-36bb-9d83-7df77e0506b2 | -6.1286 | -57.8198 | 2026-08-26 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 1963e367-57fb-3184-965f-13161f9ad67c | -13.2448 | -51.5229 | 2026-08-26 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 1ce5af7e-7f39-3d2c-bad6-993beae8ebf9 | -11.2541 | -47.0694 | 2026-08-26 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 836e5cd9-7532-3340-906f-387aad9c624d | -6.2676 | -53.3768 | 2026-08-26 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| acb05b8f-6a9b-386d-a9e3-c51972c08c6c | -13.2835 | -51.4968 | 2026-08-26 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 05cd8d62-0b72-3ab0-8992-1a8dbd705173 | -13.2273 | -51.4186 | 2026-08-26 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 3812b6da-c025-3841-80d2-2e1fc0d3f4bd | -7.0613 | -59.2165 | 2026-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 587.6 |
| ca21b6ed-515a-3a27-8a12-cffdd198d3de | -7.0614 | -59.1972 | 2026-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 070fa27c-354c-300e-addc-f965dcaab7b6 | -12.7797 | -44.2576 | 2026-08-26 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 345cc513-393f-3277-be85-092334c2350b | -7.0243 | -59.2181 | 2026-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ab18b444-c355-3391-a36f-14d9a6d3f06a | -13.2253 | -51.5466 | 2026-08-26 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 28c53b42-9468-39d8-9511-e244f5594d11 | -7.5104 | -61.3832 | 2026-08-26 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ae088049-7d06-3c8f-ae08-26d997aa7f1c | -6.2492 | -53.3574 | 2026-08-26 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 72c7969e-4f4b-34e6-873d-85dbfc932b47 | -11.411 | -44.541 | 2026-08-26 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 374ea42f-d65f-3f3d-af88-3b73e495ebee | -8.8184 | -62.3379 | 2026-08-26 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6092d07b-b041-3fc9-a2e7-e726c3170dcf | -13.2085 | -51.3997 | 2026-08-26 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 9c810240-a73f-395b-8a5c-b160e82763d2 | -6.2677 | -53.3565 | 2026-08-26 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| df52a1d2-e772-34aa-a43f-87412fb5a9d0 | -13.2256 | -51.5253 | 2026-08-26 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 08341721-b046-34b7-abcd-e9febc078738 | -11.4302 | -44.5382 | 2026-08-26 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 41873a46-3142-32a0-9b39-2b895f23f51f | -6.2491 | -53.3778 | 2026-08-26 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| af9269cb-1c6b-3401-bd0d-ebd0ac0ed4e5 | -6.1102 | -57.8205 | 2026-08-26 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d733c27e-3887-3349-9e8a-e88030acc801 | -6.1285 | -57.8393 | 2026-08-26 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 12ef3b26-2b40-3142-90a3-851799fa95d3 | -11.2732 | -47.0669 | 2026-08-26 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 62daa4c4-74c6-3dcd-a80b-9e6676154160 | -7.767 | -44.7543 | 2026-08-26 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e51678cd-2230-3e55-a13d-0ac2926ba537 | -9.6024 | -55.1078 | 2026-08-26 00:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| f1cd8989-8042-36b6-8e42-1354ab2d3c45 | -12.7608 | -44.2373 | 2026-08-26 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f6d0afde-d139-3217-a46d-c4707625b21f | -10.3918 | -45.0512 | 2026-08-26 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 323a784a-54fe-3101-8190-66bd319fbd6d | -13.2445 | -51.5442 | 2026-08-26 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| c9602074-71ed-3df8-a57c-cb1cfb43386d | -7.5289 | -61.3825 | 2026-08-26 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 127e742b-e847-3a04-a753-9c7924ff0a7b | -5.6666 | -46.9455 | 2026-08-26 00:00:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 1c271b80-2d90-389a-9dff-16b5d22da479 | -10.3914 | -45.0742 | 2026-08-26 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 2dc4f80c-63e9-3379-abcc-d656a3dbfa0b | -7.0612 | -59.2358 | 2026-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 425.1 |
| 7a725fd9-518c-3195-9a26-92777808a09b | -13.2273 | -51.4186 | 2026-08-26 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| aab392bb-6323-3250-97f3-a847fc8ab2b5 | -6.6595 | -58.498 | 2026-08-26 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 639e4c42-b407-3b9b-bb4c-ad656ad59cf7 | -9.4773 | -40.3116 | 2026-08-26 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 161.1 |
| 84b89f8c-05bb-3faf-abb6-814008f101f4 | -13.2835 | -51.4968 | 2026-08-26 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| e3012df6-003a-3d38-815f-36ce083e1c07 | -6.641 | -58.4987 | 2026-08-26 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 179.0 |
| a7c595a8-7036-38ba-bdd6-493864eb5855 | -7.4036 | -55.1513 | 2026-08-26 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 62e0db6e-c98f-372e-ac02-2b19449297ca | -2.5042 | -48.1366 | 2026-08-26 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 75e4dc44-ad63-3d6f-a0ab-a9170b6786f5 | -6.6409 | -58.5181 | 2026-08-26 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 32f8e141-4bc8-3596-9392-4fcd2decca2e | -9.4578 | -40.3392 | 2026-08-26 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 156.4 |
| 9e3085a6-da0e-3f32-9f31-9d5009f81d0b | -10.9848 | -51.1655 | 2026-08-26 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 053667b1-6063-3297-ad99-3eeac9dbb0b6 | -6.1285 | -57.8393 | 2026-08-26 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 4efc51b0-b225-386e-a5e2-e2534e0c2771 | -10.3727 | -45.0537 | 2026-08-26 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 206.7 |
| d7f6f743-656d-3a33-893c-7e1a1b7ca6f0 | -9.6022 | -55.128 | 2026-08-26 00:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e0e2c0b3-6b05-3981-8404-7c0d3661d477 | -12.7603 | -44.2608 | 2026-08-26 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| c5c55380-8e14-3bcc-ad2e-80a9e410ebd0 | -10.3918 | -45.0512 | 2026-08-26 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| ce25b4a2-8f5c-3ce9-a6a8-f8d5a0ec6824 | -6.2677 | -53.3565 | 2026-08-26 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 0e87202d-6910-3bdf-89b9-b16d1810399b | -6.6227 | -58.4801 | 2026-08-26 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c4a6119f-c2c6-3081-935c-2207e82d69d1 | -6.6226 | -58.4995 | 2026-08-26 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 125.3 |
| cb2ca136-62b4-352f-846c-6a8383c636e3 | -12.7608 | -44.2373 | 2026-08-26 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 7b2bceeb-6c49-3d9a-a5f9-aab60977809f | -10.3914 | -45.0742 | 2026-08-26 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a93225c9-2345-38bd-a663-cc7ea06612ab | -7.767 | -44.7543 | 2026-08-26 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| d03af3b9-dd1c-3f83-ab96-402413c9544a | -9.4582 | -40.3143 | 2026-08-26 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 237.1 |
| ecdf1d43-6a38-3053-8d53-ef0685f8b23f | -7.2856 | -44.0875 | 2026-08-26 00:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 0b7ba0c6-6154-31f6-95f8-54800688421f | -6.2863 | -53.3555 | 2026-08-26 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f0fa7d85-4f35-3a46-bc32-59931fc4188f | -7.5104 | -61.3832 | 2026-08-26 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| abfc917a-7e8d-3064-96ab-2ae743244b2f | -13.2259 | -51.504 | 2026-08-26 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| de6fe88d-6041-3f95-ad89-62409682848f | -11.2732 | -47.0669 | 2026-08-26 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 2f8a147c-d811-3965-8a4f-1ef2ba87ad93 | -6.1286 | -57.8198 | 2026-08-26 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 10b2a5c9-78e1-3f7a-8ca0-0a2d76fc0611 | -8.8184 | -62.3379 | 2026-08-26 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 1d9d04d1-4ef4-3136-aefb-6b4425826141 | -6.1544 | -59.9248 | 2026-08-26 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| d35dc3b3-e65c-32c6-9e48-1043a50bb979 | -6.2491 | -53.3778 | 2026-08-26 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| b285ca66-a9a2-3b61-bd3f-57aa9de34805 | -6.6225 | -58.5189 | 2026-08-26 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| de953260-ec32-3c50-b66d-72e6468d92d0 | -6.2861 | -53.3758 | 2026-08-26 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| ff6a6970-9816-3d6d-bc53-1ad1bf4f3356 | -9.6024 | -55.1078 | 2026-08-26 00:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 94e68a8e-e742-33f2-b8a6-b21db1c7499d | -9.4769 | -40.3365 | 2026-08-26 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 3cc0a256-526f-3c0c-bd60-35727598239d | 2.5983 | -60.697 | 2026-08-26 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e9568c0a-2a16-38a9-92db-818e74f0a8ef | -11.4302 | -44.5382 | 2026-08-26 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 551ea929-d53f-392b-9c98-c975b8fec7ab | -6.1102 | -57.8205 | 2026-08-26 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 7feafa78-1a44-3eea-af3e-598419e8934a | -13.2448 | -51.5229 | 2026-08-26 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 248a6103-7c14-31c5-b096-a133f0dc4b5c | -12.7797 | -44.2576 | 2026-08-26 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5e20e1fa-5291-31de-9245-e2c80404943c | -13.2451 | -51.5016 | 2026-08-26 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 82fb032d-8ffc-3c4c-8efa-aeb24e9ce996 | -10.3723 | -45.0767 | 2026-08-26 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 43d31be0-582a-3e42-97a1-8da527d2fbd7 | -6.2676 | -53.3768 | 2026-08-26 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| d6dc3bce-54e6-350a-ba91-ce91f8539bfa | -13.2839 | -51.4755 | 2026-08-26 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| eff58530-8335-3a81-a655-5a28e82ce888 | -13.2256 | -51.5253 | 2026-08-26 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 43090b4b-6a0d-3f16-90d3-5727d699a2ea | -13.2277 | -51.3973 | 2026-08-26 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 1b22dd8a-dff6-3ebc-9ffb-b19ecc0a0057 | -7.7481 | -44.7561 | 2026-08-26 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 7eb40435-d514-3f6c-a4c3-d444e897031a | -13.2647 | -51.4779 | 2026-08-26 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7f322de8-1c8a-36b0-b406-be91fa75ddad | -10.74 | -54.03 | 2026-08-26 00:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6abe4b10-bf9b-3ab5-b202-032365a9e313 | -10.37 | -45.08 | 2026-08-26 00:15:00 | MSG-03 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
