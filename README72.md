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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 785327e6-321d-3988-acf2-4e158bfbd454 | -10.9685 | -48.3232 | 2026-09-16 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 16020fe7-5cb4-3f43-a181-19f4aed318e8 | -13.287 | -51.2832 | 2026-09-16 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 45365e55-f860-3bb5-befd-5a96ab9eac01 | -5.6311 | -51.6858 | 2026-09-16 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| eb044aa2-ebe4-3783-9a0e-93cbb4386827 | -10.876 | -50.8163 | 2026-09-16 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| bf042c42-e5d0-3ee8-b8ea-0321d669fe0a | -11.4167 | -51.4371 | 2026-09-16 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| bc838c27-4483-3914-ab83-7c44c84a6ad7 | -9.0264 | -45.0792 | 2026-09-16 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 150.4 |
| a223e6c8-34d0-3ae3-8fd8-6ec03015cde3 | -5.144 | -55.9345 | 2026-09-16 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 35a58051-1240-301a-965b-61e63bb1d878 | -5.1439 | -55.9543 | 2026-09-16 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 80521483-fa53-37ff-a234-6985b0b66750 | -9.2311 | -46.7055 | 2026-09-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| aeee3d18-dda0-3f35-bf46-8bff5a307768 | -6.8216 | -59.1686 | 2026-09-16 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 177.4 |
| aaa45f93-d761-3e80-a071-c2fc13ab036e | -14.6775 | -48.0241 | 2026-09-16 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 3dde2ef7-adaa-378c-89ee-b6880bbe6512 | -9.0866 | -61.0287 | 2026-09-16 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 110e9e73-6d1e-3962-9ddb-e60c6ac7a897 | -11.5436 | -46.852 | 2026-09-16 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 71f7ca3a-5e93-3888-bc3a-4a7ed2d349aa | -6.8567 | -47.4328 | 2026-09-16 13:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 8b556334-975e-31e8-8a51-0de0c254fef2 | -11.9033 | -43.8112 | 2026-09-16 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 200e168d-6a2b-3acf-8bdf-777208436aa5 | -10.3113 | -45.3366 | 2026-09-16 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 135.4 |
| cf677fae-6b12-3777-b1b3-87cbcb703090 | -14.6584 | -48.0048 | 2026-09-16 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 4aaf833a-969f-3254-9602-2c4420a46c00 | -11.417 | -51.416 | 2026-09-16 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 9dc5358e-ef86-35bc-8b16-7c1dc856c8a5 | -11.5432 | -46.8745 | 2026-09-16 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| c0e59458-6844-3b08-9489-1a44a23f3f24 | -2.6966 | -57.6084 | 2026-09-16 13:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 216.7 |
| a155083a-3c05-38b8-8be5-36401e8f02f8 | -14.658 | -48.0273 | 2026-09-16 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 10e03c5f-362b-3e4f-a371-993876131242 | -8.396 | -47.2121 | 2026-09-16 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 2d55d41b-237f-319a-87ee-d9ac1757d015 | -15.4626 | -53.7761 | 2026-09-16 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| dc2065fa-3e2c-301d-bd7d-61460cd1029a | -7.0454 | -42.0427 | 2026-09-16 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| 03884d7b-16b7-3167-9ccf-4740a7345372 | -14.658 | -48.0273 | 2026-09-16 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| e62c603e-7fd7-3d15-94f1-77e006755d6a | -12.1453 | -44.2195 | 2026-09-16 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 6f695c89-55e4-3f04-876f-c568ece2dff1 | -2.6966 | -57.5889 | 2026-09-16 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 7f682488-9ecc-3656-8b24-4e9632cc853e | -5.7614 | -57.6002 | 2026-09-16 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 2167e78f-9fd7-3ee0-8cdf-c053f037d3b2 | -15.539 | -53.8502 | 2026-09-16 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 79e4b13a-d2fb-3447-b610-b834a4f174f8 | -9.5912 | -46.6213 | 2026-09-16 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 180.5 |
| da59eb16-fe35-399a-8da5-28dbec3a57b2 | -12.3085 | -47.9539 | 2026-09-16 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| f04aa056-3359-3865-abc4-0799a55d5b88 | -15.5199 | -53.8317 | 2026-09-16 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| e5677fea-00c9-39ef-a25a-cef382b5b777 | -5.1255 | -55.955 | 2026-09-16 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 95c76fb4-dc9a-3f73-b842-8b9ab782616d | -15.4623 | -53.7972 | 2026-09-16 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 223.7 |
| dd3d8815-c5ba-3d15-a7bd-e5066976c781 | -12.3277 | -47.9513 | 2026-09-16 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 48baf75f-8bc7-3984-8f8a-1848bf332c62 | -9.376 | -50.1352 | 2026-09-16 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 16ce48e9-0178-38f7-a72e-4afb81a54ab6 | -6.0184 | -57.7657 | 2026-09-16 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 25124365-4a92-39f6-ab95-5406d3980aa1 | -12.4145 | -48.4701 | 2026-09-16 13:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| dad522ec-9d2e-3a04-a831-cca670fdcd96 | -10.3116 | -45.3136 | 2026-09-16 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| bca06038-7ea6-38d0-a63a-c0bec76733a0 | -8.5428 | -44.5132 | 2026-09-16 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 475.9 |
| 67d5c3f2-b453-379c-a18b-c13a80fc31cb | -13.2239 | -51.6318 | 2026-09-16 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d1d7d292-f776-3d40-b70e-9048fa042d61 | -5.1439 | -55.9543 | 2026-09-16 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 249da269-be29-343a-a30c-efb04307d8a5 | -6.7892 | -48.6563 | 2026-09-16 13:40:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 6347b350-3401-3522-b73c-a0f85811030f | -11.5624 | -46.872 | 2026-09-16 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 309b9309-22e2-3066-8fe8-2d842a64ece1 | -13.2874 | -51.2618 | 2026-09-16 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 89985d40-4226-337a-9a0c-840cee3cdafd | -5.144 | -55.9345 | 2026-09-16 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| e9f15ab2-3850-3c34-a7f3-de8023da7fa6 | -14.6779 | -48.0016 | 2026-09-16 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| fb92c5c1-53e8-3004-b631-d9668b86faca | -11.4167 | -51.4371 | 2026-09-16 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 7df793ff-166d-3b74-9ba3-5af05cf49cb8 | -15.4428 | -53.7997 | 2026-09-16 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| f84cc228-bba0-3179-902e-3f6ec61d477a | -10.8495 | -46.1771 | 2026-09-16 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.9 |
| cbde244b-7849-3a18-b296-21dbcc654ec7 | -10.8919 | -54.0062 | 2026-09-16 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 61cafabf-56b7-3f28-8fdd-758617a85fc7 | -9.3379 | -50.1814 | 2026-09-16 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 23059d6f-c054-3701-aecf-4903a2bcb3f9 | -6.8216 | -59.1686 | 2026-09-16 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 192.8 |
| a3c56e3f-750b-3396-804b-70084db8d743 | -9.1337 | -65.844 | 2026-09-16 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 9f1f93eb-8e1b-3fe9-ab69-c52dbdb2e524 | -11.5432 | -46.8745 | 2026-09-16 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 799f4241-280f-3c4c-8978-42b48fd418bc | -11.417 | -51.416 | 2026-09-16 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 7b02dfb6-69f4-39a6-8892-a9c78a7bc25c | -3.7128 | -60.6211 | 2026-09-16 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 6de3649d-8304-3ef3-96c9-98bc99b098d1 | -7.3561 | -44.4956 | 2026-09-16 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 156.5 |
| b0ac228e-795d-31a4-90f6-3e17885b9053 | -9.3765 | -50.0925 | 2026-09-16 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f3a0cf76-4392-379e-bbfb-8947028da4d6 | -10.8571 | -50.8183 | 2026-09-16 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 209.0 |
| c5a69611-4b96-307f-8996-2630cfbde209 | -10.8492 | -46.1998 | 2026-09-16 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 72e5e079-a269-3389-919c-7a226790a612 | -10.9685 | -48.3232 | 2026-09-16 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| da882975-b0b0-355d-b5e7-a0388cc362c2 | -15.5004 | -53.8342 | 2026-09-16 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 83ba484b-3369-30b2-972b-40e9f8f3bdbd | -8.8588 | -44.8919 | 2026-09-16 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 9f7e8862-d0b1-350a-85d9-1f7c82cb437b | -9.3763 | -50.1139 | 2026-09-16 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 1d86daca-2dd6-37f2-a745-d7e804571642 | -14.6775 | -48.0241 | 2026-09-16 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 823f1fe7-c078-3e2e-9f02-39bfafe9380a | -2.6783 | -57.6087 | 2026-09-16 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 706e65d5-b861-32db-8880-b35dcd441246 | -13.287 | -51.2832 | 2026-09-16 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| d7a556a6-4556-3529-9d0f-9a4bfaadec3d | -10.876 | -50.8163 | 2026-09-16 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 6fbe2865-814e-3353-9a46-23fdd5579326 | -2.6966 | -57.6084 | 2026-09-16 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 258.6 |
| 401c46ae-6791-3b23-bfdf-b9027df2d1f4 | -9.3758 | -50.1565 | 2026-09-16 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 3f50ac1e-4a83-319a-aaa0-76882d57440f | -5.6311 | -51.6858 | 2026-09-16 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a2950163-5ea0-30b5-9929-eb0d0728dd23 | -15.5386 | -53.8712 | 2026-09-16 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e50a1e2d-6ad2-382a-ae1d-04ebde6ab51e | -10.5975 | -47.7505 | 2026-09-16 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 63e24b6b-c2ad-3732-a907-8b9b1c21d998 | -6.1159 | -44.6932 | 2026-09-16 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b436007c-0fd7-370f-923d-500516bde6f0 | -6.8032 | -59.1693 | 2026-09-16 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 344.1 |
| cbaf843a-7d37-3255-83eb-b300170d2558 | -12.3273 | -47.9735 | 2026-09-16 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b2eab723-a10e-34f6-b2a3-4ebc1c4cb813 | -11.5436 | -46.852 | 2026-09-16 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 70019bad-b00d-3ff7-bd8e-e35fdba1eeab | -8.6566 | -44.4777 | 2026-09-16 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 230.6 |
| 8ba9f954-0636-3aee-87bf-a06ea4233252 | -13.2867 | -51.3046 | 2026-09-16 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 44e85008-72dd-3f09-9ef3-26c8dc334e7f | -9.3951 | -50.1121 | 2026-09-16 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| c2d666e7-556b-31ca-9983-8b5459bd9495 | -10.4772 | -50.9634 | 2026-09-16 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d70684a8-e893-3934-89d2-8ed7983ddf4d | -8.5617 | -44.5112 | 2026-09-16 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 36c5dcac-5309-307a-8b67-7608744fad78 | -7.3373 | -44.4973 | 2026-09-16 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 6e2f35f6-5e07-3e6d-816c-93277fe9d31d | -6.7705 | -48.6577 | 2026-09-16 13:40:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 93.9 |
| ed67b70f-7dd0-3185-a01a-6711fbf7cc53 | -8.5431 | -44.4902 | 2026-09-16 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 9d86a1cb-dc5b-3efc-80d4-17cdacf6146c | -10.8916 | -54.0267 | 2026-09-16 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 2a252984-937e-37c2-9902-1acfdea80817 | -6.8032 | -59.1693 | 2026-09-16 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 360.4 |
| 9de873f9-e303-3d87-be6d-85122cb23ff3 | -12.7709 | -51.2403 | 2026-09-16 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 3f365e3b-9d07-33d9-81f0-8a897ae7cb8f | -13.2239 | -51.6318 | 2026-09-16 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 2f893096-f7c7-3320-b428-3113943e9211 | -9.1337 | -65.844 | 2026-09-16 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a7375834-6565-3ae8-99ff-97e4134d3b39 | -10.876 | -50.8163 | 2026-09-16 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 1b102f18-4042-3425-9fca-9967430d522a | -12.3081 | -47.9761 | 2026-09-16 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| cac763ff-3e28-349d-a022-91652f9bc7ac | -8.396 | -47.2121 | 2026-09-16 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 2d08d253-60b8-3f0e-8893-817bedd959f1 | -6.8216 | -59.1686 | 2026-09-16 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 177.0 |
| 97980669-1333-36eb-8be8-9ec002044c31 | -13.2874 | -51.2618 | 2026-09-16 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6de57870-c3da-34c9-b9b9-66374382f1b1 | -10.8919 | -54.0062 | 2026-09-16 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 1040fbb5-2547-3c13-9cbe-283d55bd6e0d | -5.6311 | -51.6858 | 2026-09-16 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 4a906a24-ffc6-3cda-b0ff-913ba415c8c1 | -6.7892 | -48.6563 | 2026-09-16 13:50:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 331.2 |
| 588fa77a-38f2-36b1-a4e2-1641387829e9 | -2.6783 | -57.6087 | 2026-09-16 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 121.0 |


[Clique aqui para ver as próximas entradas](README73.md)
