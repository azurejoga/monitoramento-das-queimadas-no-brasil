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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a996b03-8b81-3f9b-a1d1-5431554be037 | -8.4483 | -54.725 | 2026-09-27 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e16752ad-5c08-3046-abc6-809e8bcaf168 | -7.2755 | -43.321 | 2026-09-27 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 147.2 |
| e12199f4-ad89-3ce5-abbc-56ac6ef655d4 | -12.7028 | -47.3189 | 2026-09-27 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 35600bfb-a17c-32b6-a881-71e5f63f0318 | -11.0044 | -54.0576 | 2026-09-27 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 20bbff02-150e-3deb-9695-8c82cbff7256 | -17.0533 | -56.5693 | 2026-09-27 14:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 1787734a-fe89-30b7-9119-f29bfca1d2ee | -10.2827 | -49.9606 | 2026-09-27 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 31b5ccd6-4571-38c6-9466-29aae19889a1 | -12.7225 | -47.2937 | 2026-09-27 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 281.7 |
| 4599d135-c5fe-3fc0-af4e-c32134eec9d3 | -12.6651 | -47.2795 | 2026-09-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| d678d991-9c58-3b75-b956-e420d8064765 | -10.2824 | -49.9821 | 2026-09-27 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 99c281da-7eab-3ea4-a3aa-868b6db0cf6b | -12.288 | -50.3789 | 2026-09-27 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3b5f3aa6-282e-335b-b2b4-221361b38a12 | -12.8059 | -54.0255 | 2026-09-27 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 158.9 |
| bd005648-855c-3a8e-8b0f-c3fe675c0b5e | -7.3653 | -42.1058 | 2026-09-27 14:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 147.8 |
| b500cbf4-a105-359d-ade1-4f8357f1f305 | -8.7955 | -49.996 | 2026-09-27 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a310145c-1a55-3aa8-8be4-2a3c05fe6cf5 | -12.4351 | -44.1497 | 2026-09-27 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 50c1f1f8-c6ed-3c51-b9d7-51f1e8f37714 | -11.5815 | -50.5261 | 2026-09-27 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d956f9e3-cfdc-31d0-86fd-725977b4b067 | -9.1525 | -49.9639 | 2026-09-27 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| dcf5c1d9-2470-3536-918a-3033722c01f2 | -10.02 | -50.14 | 2026-09-27 14:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 790810bd-1eff-31d6-bc6e-e204a6b3671d | -7.3653 | -42.1058 | 2026-09-27 14:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 148.0 |
| 89811a05-0bc6-3e98-a06b-5a852108c682 | -8.5982 | -54.6341 | 2026-09-27 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 0e6b53d2-35d5-321b-a20c-275780b4d0bd | -11.2113 | -54.1208 | 2026-09-27 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 7b9f2418-cc22-3f53-b9b4-a6ef3b1a2faf | 1.2978 | -50.8507 | 2026-09-27 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 9111647a-089d-3020-b147-1e58cc82fa6a | -15.9869 | -54.9419 | 2026-09-27 14:20:00 | GOES-19 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 62a0d9dc-19b3-3378-85a8-0edf7a1bf3c7 | -11.7887 | -50.6521 | 2026-09-27 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| d5e7c1f4-6e1b-3c84-8b9e-18ccd30cef7c | -6.8408 | -43.5021 | 2026-09-27 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| cb248b2d-e22e-375d-890d-cab68925e5b7 | -6.2026 | -47.5026 | 2026-09-27 14:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b506bb92-2c84-36b8-9e37-918ac9d1556c | -10.0164 | -50.116 | 2026-09-27 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| ef0f3cea-03b4-351c-81a4-a57076a151e1 | -9.0249 | -49.6334 | 2026-09-27 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 4dca3fa3-f7bb-371f-a5f6-9771ecc77a5d | -6.8596 | -43.5003 | 2026-09-27 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 9533d8c9-e299-3cd2-aec0-6156fe9222d9 | -9.9318 | -49.3733 | 2026-09-27 14:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| b2414523-0241-3b3d-901a-4c8e51b6e575 | -9.1525 | -49.9639 | 2026-09-27 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 4cc7089c-23b0-3b7c-af7b-36d2cc4e57a0 | -11.6374 | -50.6053 | 2026-09-27 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 8eafd3c9-ea3e-3b01-874a-563b127144d0 | -11.1901 | -51.3766 | 2026-09-27 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| f1ac8b88-197c-3f40-bf43-5c36a28ea213 | -6.8405 | -43.5254 | 2026-09-27 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| fed09e17-ded6-32fe-9bed-95e36ce7dea6 | -8.9637 | -44.1422 | 2026-09-27 14:20:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| f01e9bb5-56ae-3069-a16f-d6d98753e06b | -12.7038 | -50.6499 | 2026-09-27 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 5cdb2e11-6cd9-37ac-b2bc-14d096f32552 | -11.0238 | -54.0148 | 2026-09-27 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d9c86956-5d09-3271-8f21-a04bc723f99b | -12.4351 | -44.1497 | 2026-09-27 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 274.7 |
| e550df04-955e-368a-8564-1bd673460f7c | -8.6171 | -54.6126 | 2026-09-27 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5ae9cd8f-9fae-34ce-bbf1-14117dd4ce03 | -8.5984 | -54.6139 | 2026-09-27 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5912043d-5aee-3666-adc9-7b650aaa4029 | -10.0162 | -50.1374 | 2026-09-27 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 3f0ab9c3-c30c-3e31-8623-6ddec235b634 | 1.2978 | -50.8715 | 2026-09-27 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 03d8ddeb-d98f-3819-969f-7bd3590a87e4 | -11.6561 | -50.6245 | 2026-09-27 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b74c6b0e-24df-33ab-ae3b-6c19fa08b837 | -10.035 | -50.1355 | 2026-09-27 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| fc231540-4b7e-3837-98e5-a7a4c94d40ce | -9.2415 | -47.3487 | 2026-09-27 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 687da81c-3420-3fdf-9c8a-ae0c4abcb9dd | -11.9132 | -49.9721 | 2026-09-27 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a7141033-6626-3826-ae0a-98ed33b57b5f | -10.4046 | -53.803 | 2026-09-27 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 97117ef3-9aac-3033-b947-4bf548192eb6 | -6.84 | -43.572 | 2026-09-27 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c61b09c2-2fe6-38d5-9662-ab6c2d21c2cd | -9.2226 | -47.3507 | 2026-09-27 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0c5df418-6c4d-3031-9f16-694c488caee5 | -17.0529 | -56.59 | 2026-09-27 14:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| 5ae3704b-8f18-3ce8-a66b-eb549a0ac980 | -10.8238 | -60.744 | 2026-09-27 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 8cad00f1-6c88-323e-a628-5f58fca39cd2 | -6.8594 | -43.5237 | 2026-09-27 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 45adde90-d6eb-306e-bf84-2da5ccf82d2d | -12.8059 | -54.0255 | 2026-09-27 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| a98de4a6-54c2-3270-8b94-88ae0cab2a3d | -17.5697 | -46.9019 | 2026-09-27 14:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 152.7 |
| d2baef2a-417e-3765-bb8e-7841053a0b8a | -11.0991 | -54.0285 | 2026-09-27 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4a88ec71-f7ab-344d-8b3e-992d454f7047 | -17.0533 | -56.5693 | 2026-09-27 14:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 31b1aae7-226b-393f-987f-d57dc08f14b9 | -11.7135 | -50.5966 | 2026-09-27 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6ea8b1b3-ec17-35fc-accd-756ab131f96b | -7.365 | -42.1298 | 2026-09-27 14:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 136.4 |
| 8e7683ca-d4b1-34b3-845d-47aab393c4bc | -11.77 | -50.6329 | 2026-09-27 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| af407d48-da22-3051-8ec7-befe387b3dfe | -12.6651 | -47.2795 | 2026-09-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a67209ea-e65f-322d-9a81-14e62e65ebc4 | -6.8408 | -43.5021 | 2026-09-27 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| cbab8f70-475d-32bf-8f80-fc228d8304d9 | -5.8496 | -45.168 | 2026-09-27 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| d7ac5bc6-7656-35a4-9e59-ef7b74c4b249 | -11.9622 | -50.5036 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 67694f0e-90f6-3c9f-8684-166bf0bb6724 | 3.8592 | -60.5802 | 2026-09-27 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5fa510f4-7c2e-3561-8c9f-2714062da94c | -12.6463 | -47.2598 | 2026-09-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| b3297940-22ca-32b7-9c11-2beca1bf5db2 | -11.9593 | -50.6965 | 2026-09-27 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f3b04c43-6404-3982-8835-2c7c74af2bcf | -10.6094 | -53.9902 | 2026-09-27 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d928962d-2754-3c5b-bac2-de1b05483bf5 | -14.7289 | -45.576 | 2026-09-27 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| adc30b38-a58f-3664-97d1-cb3572ed77a2 | -6.84 | -43.572 | 2026-09-27 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 131bd510-b734-3875-885f-f78b08af5fe0 | -10.8238 | -60.744 | 2026-09-27 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4d605eb3-c82f-3568-8f5a-7c73ec5299a2 | -12.0365 | -50.6233 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e85cc226-7e6e-3ea0-8b49-f88a7c263971 | -12.4351 | -44.1497 | 2026-09-27 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 349.5 |
| 9ed1bc46-d806-3432-841c-a86cb3f055dc | -10.0164 | -50.116 | 2026-09-27 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 8038c707-2d7c-32cb-9ef6-569218850d07 | -17.5697 | -46.9019 | 2026-09-27 14:30:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 172.2 |
| cd5519a2-54c7-32bc-99f5-f1ac344d514d | -14.13 | -46.326 | 2026-09-27 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5e5984c0-f0ce-3a24-bd2c-14d0ea6ad672 | -11.2844 | -51.409 | 2026-09-27 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 5e6d69de-e2d5-3ebc-8fea-ddbe0ae47310 | -11.2856 | -51.3243 | 2026-09-27 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 744ecffd-3412-375f-bd9b-6cecff501a56 | -13.3824 | -51.3138 | 2026-09-27 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 3b2d5584-c483-3dfb-a776-8532f23845d4 | -7.055 | -42.849 | 2026-09-27 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |
| 76ab7d4b-f3d5-36d4-9646-927a81985169 | -12.0559 | -50.5996 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 310b49d9-3311-3fb6-aac4-7586f0f0f11e | -8.4483 | -54.725 | 2026-09-27 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| f09d7e69-d375-3927-a00d-14da3fdb8439 | 1.2794 | -50.851 | 2026-09-27 14:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 6ca650e4-6092-3392-b92d-c9bc7050e149 | -10.4046 | -53.803 | 2026-09-27 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 18cb0ec3-c41f-3056-a588-aca37363d60c | -8.5982 | -54.6341 | 2026-09-27 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 8f7fc1e3-006d-3e28-9a8d-a900897da0f7 | -11.8014 | -49.8129 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| f4442598-09e2-3bf9-b631-de0f2f8e71ab | -11.8097 | -50.5214 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 843630de-f973-332f-a776-6808b142e87e | -11.0991 | -54.0285 | 2026-09-27 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 409451bf-dff5-32b2-9b49-8cd90353f682 | -10.7157 | -48.7464 | 2026-09-27 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 3caebfb8-eeaa-3fa5-a237-f7b140ba4ba3 | -9.7874 | -44.8289 | 2026-09-27 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| defc8712-7b1a-3a56-9b50-fb293f83580d | -12.4355 | -44.1262 | 2026-09-27 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 4c0a9552-c6bb-3729-97f0-2d90fbd42361 | -11.7659 | -50.9107 | 2026-09-27 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 50ae8fb7-9066-3eef-abae-9650dddaa630 | -8.6171 | -54.6126 | 2026-09-27 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9d737ded-c14a-3566-b4e9-64dfb59ff883 | -11.8478 | -50.517 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c083cd9c-aefa-3efc-886d-0cefdaaf3181 | -8.5984 | -54.6139 | 2026-09-27 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| dd1c6626-6baa-3597-a944-93467aabaf6f | -11.4173 | -51.3948 | 2026-09-27 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 806d3e98-0549-3f16-a69f-b6d35662a6cb | -10.2446 | -49.986 | 2026-09-27 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 156d6d71-5624-3e2d-a17f-5e64fe6954d2 | -11.9418 | -50.5916 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d407094f-b165-3203-9448-b11fb7de113a | -10.8051 | -60.745 | 2026-09-27 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 91013bc8-b35b-3ff3-9c2b-ed30382bc68a | -12.7038 | -50.6499 | 2026-09-27 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 382973dc-3a12-383e-aa20-3412e215ed27 | -14.3693 | -52.1026 | 2026-09-27 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 288bdde9-6d68-3993-b62a-e783929b57c0 | -10.2257 | -49.9879 | 2026-09-27 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |


[Clique aqui para ver as próximas entradas](README60.md)
