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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 598aaed9-d75f-3be1-ab94-e8f9dcb5a35b | -12.3277 | -47.9513 | 2026-09-16 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 163.7 |
| ac867d43-802d-3c5e-a3f0-33481f252871 | -11.4167 | -51.4371 | 2026-09-16 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 196.1 |
| 09d92533-99ff-347f-9554-c2865ddb7d89 | -11.5432 | -46.8745 | 2026-09-16 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 10762143-9b3d-3cfb-b3cc-f87cd35b0103 | -7.3561 | -44.4956 | 2026-09-16 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| d1f2fffa-1002-3292-9fe0-21698d9dc17e | -10.8305 | -46.1796 | 2026-09-16 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| e99fd352-3a39-3529-adc8-7720f2f2d303 | -10.8571 | -50.8183 | 2026-09-16 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 219.2 |
| 5876bcad-1ddf-3b1c-bd9a-4df04bcd98bc | -5.144 | -55.9345 | 2026-09-16 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 125d151d-0390-3f92-866d-67bc13a37348 | -6.7892 | -48.6563 | 2026-09-16 13:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 119.3 |
| dfbe336d-4331-3405-b33f-ed40bdfd0c48 | -11.5624 | -46.872 | 2026-09-16 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 0bebdc99-3931-3cbc-83ef-bf0ff6be8271 | -11.417 | -51.416 | 2026-09-16 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 65fccff9-119f-3cc2-bd00-199de67c4364 | -10.8492 | -46.1998 | 2026-09-16 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 351.8 |
| af246d8c-05f0-30cc-828b-4680098e7749 | -9.3564 | -50.201 | 2026-09-16 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 154.6 |
| 05e935e5-d625-3f67-adf6-16abfe9c65d5 | -8.5428 | -44.5132 | 2026-09-16 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 152.5 |
| e2461422-071c-3236-9968-760354e376ab | -9.711 | -52.0025 | 2026-09-16 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 438ada38-b784-3ed5-9899-26dad8545484 | -9.3569 | -50.1583 | 2026-09-16 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 16d72959-7615-3a59-a5dd-0bb70625048c | -10.8495 | -46.1771 | 2026-09-16 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 239.6 |
| d73a7ae3-19ba-312c-853b-72bb611f5a19 | -9.4137 | -50.1317 | 2026-09-16 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0441bf34-b081-38fc-a8b0-ec8c939b09c5 | -12.57 | -50.77 | 2026-09-16 13:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c4992ce-ddde-34e5-91c8-aa927c4894d7 | -12.58 | -50.83 | 2026-09-16 13:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a14e6ba-ddb7-37e4-8ed6-5c17907749d0 | -9.3379 | -50.1814 | 2026-09-16 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| a5839fef-a35f-378d-b43d-8a0be62cd1cc | -10.8492 | -46.1998 | 2026-09-16 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 5d2258ca-6dff-38b5-a105-f41d8d10a066 | -10.9685 | -48.3232 | 2026-09-16 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| a62a02e8-1de4-3e06-ba16-0759c9abd1f4 | -15.5199 | -53.8317 | 2026-09-16 13:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 6cfe6cdf-d2c3-3bab-9373-faa4df6c23ee | -15.4626 | -53.7761 | 2026-09-16 13:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5dc4d507-628d-3635-b0ca-8ab8dc04d633 | -8.5617 | -44.5112 | 2026-09-16 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 154.6 |
| b961b24d-495d-330b-9620-f8cd471c1f5c | -7.58 | -46.3097 | 2026-09-16 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| f796ac35-b25c-308e-b581-764e75d35909 | -13.2047 | -51.6342 | 2026-09-16 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| c108f6be-da76-355b-b696-f0e2dcab8aac | -6.8216 | -59.1686 | 2026-09-16 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 384.9 |
| 712accc1-45eb-3ab5-bbcc-902331d68c17 | -11.417 | -51.416 | 2026-09-16 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| ecfa7f97-1d8e-3456-98e7-428060eb844d | -11.5432 | -46.8745 | 2026-09-16 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 906755ee-acf3-3867-95c9-4e49b49e78c9 | -9.3567 | -50.1796 | 2026-09-16 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| fad3fc46-f9ef-3a6c-8261-7151f2729b46 | -6.7892 | -48.6563 | 2026-09-16 13:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 5145858a-844f-32c1-b2fb-60d91eb122f7 | -2.6966 | -57.6084 | 2026-09-16 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 2d3566e8-bf0d-357c-8b26-03d572cb98c7 | -15.5004 | -53.8342 | 2026-09-16 13:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 4ec98131-b238-30f6-8267-7d6df5e4f064 | -9.5725 | -46.601 | 2026-09-16 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 63b06956-8a45-3c46-8b85-a0d7e4bafa8e | -6.8032 | -59.1693 | 2026-09-16 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 576.8 |
| efb21674-be8d-38e9-a027-400ecf3ec231 | -15.4623 | -53.7972 | 2026-09-16 13:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 41fba097-5e1e-36d0-9f24-608fb0ee1043 | -12.0488 | -47.4777 | 2026-09-16 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 7e47a8ad-bc0f-3bdd-8d21-da84612ca4ab | -9.3569 | -50.1583 | 2026-09-16 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 085d03a4-6568-35d3-b354-790595dbe281 | -10.0982 | -45.6141 | 2026-09-16 13:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 9c7871b4-0f96-3d98-ab16-88ca582fbc96 | -11.5624 | -46.872 | 2026-09-16 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a181fb50-ea7d-36c5-9d4c-3fd94435f57f | -15.5001 | -53.8552 | 2026-09-16 13:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 0546a577-4a70-388a-8ef6-23c26c256923 | -9.2311 | -46.7055 | 2026-09-16 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 241.0 |
| aacfc28e-b721-3044-a2b1-3546765c2e30 | -9.3763 | -50.1139 | 2026-09-16 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 6f305242-b548-3b65-8863-b4b7b039b84b | -10.296 | -51.8655 | 2026-09-16 13:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7ccbb5ea-5c68-365e-b0c2-fa78c1709346 | -3.7128 | -60.6211 | 2026-09-16 13:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 03a9c089-c2d1-384f-bace-a67664c4ec75 | -11.4167 | -51.4371 | 2026-09-16 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 585abb20-e44a-3f1c-96f0-486e87f2e890 | -15.5195 | -53.8527 | 2026-09-16 13:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 2eba67a1-9460-305e-a7e0-cb0885884073 | -13.287 | -51.2832 | 2026-09-16 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| d26b84d3-e10d-353a-b535-1ebdd09173d4 | -5.144 | -55.9345 | 2026-09-16 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c7200524-4dac-3eab-a3d9-186cbaf2cbfb | -12.3085 | -47.9539 | 2026-09-16 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 629d64f3-9401-3079-b468-76f4b6e9864c | -10.5975 | -47.7505 | 2026-09-16 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| fff35ceb-a776-31f5-a0cf-13080aaab76b | -11.5436 | -46.852 | 2026-09-16 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| f361095c-93ff-3190-9bc5-c38f46f96b09 | -9.4137 | -50.1317 | 2026-09-16 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ca970b69-11ce-334c-bebc-1edeba5e1711 | -8.5428 | -44.5132 | 2026-09-16 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 38f22e37-3766-3a90-866d-6bd7ceb596a2 | -10.3116 | -45.3136 | 2026-09-16 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 546a3a80-a83d-371b-a9d9-763a0518a381 | -7.0454 | -42.0427 | 2026-09-16 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 124.7 |
| 039c5078-f124-3700-9203-c8eef796d065 | -12.5341 | -47.0964 | 2026-09-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| b7663ffe-b168-32fe-93f5-a0b4db1863e4 | -5.6611 | -43.2272 | 2026-09-16 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 3276a7d9-ab37-329a-a438-2e2cad1204ac | -10.876 | -50.8163 | 2026-09-16 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ac920ea5-88a0-3072-b1da-a8059d7b66f0 | -9.376 | -50.1352 | 2026-09-16 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 61cefbb4-8b82-36c4-82b7-de51db39af8d | -12.3277 | -47.9513 | 2026-09-16 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 199.2 |
| c9b88a5e-7e51-385e-9860-cee053104c88 | -7.2691 | -45.5737 | 2026-09-16 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6e7442bf-0c2a-331f-ae4d-26945812233e | -13.2874 | -51.2618 | 2026-09-16 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 4eac9f01-da9c-364d-8c32-ddd44fe646ac | -7.3561 | -44.4956 | 2026-09-16 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 4139f1ff-7991-3e7c-af91-94d99888c304 | -12.3273 | -47.9735 | 2026-09-16 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| ad22a0a6-c329-3316-961c-82d20339dae1 | -10.8571 | -50.8183 | 2026-09-16 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b8f5e75d-1907-360d-a2b0-432be14245a9 | -9.3755 | -50.1779 | 2026-09-16 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| eed2d7e9-f7f9-371f-bdae-09a7c16b17c4 | -10.8495 | -46.1771 | 2026-09-16 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 68bffe29-5d4b-362b-98fb-7cc16190f9f6 | -8.5431 | -44.4902 | 2026-09-16 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 08e64911-2a7e-3d2a-8138-f2310a79b103 | -15.4623 | -53.7972 | 2026-09-16 13:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 81ed0a29-7436-3722-bc3d-95b3febd7299 | -2.6783 | -57.6087 | 2026-09-16 13:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 49051f9f-9b2f-3995-a305-eec6c628f229 | -10.296 | -51.8655 | 2026-09-16 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 1e5da0df-2f22-3982-b7dd-015302441034 | -12.3273 | -47.9735 | 2026-09-16 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 3c16d77c-7afc-3033-8177-6c42245a105b | -12.3277 | -47.9513 | 2026-09-16 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 63779cf2-7557-3168-b4a4-a15c37157fd5 | -13.2874 | -51.2618 | 2026-09-16 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| bfbd69fd-7f14-3d07-9212-d8a2386ebf9c | -7.3561 | -44.4956 | 2026-09-16 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 28e167e3-77ea-3f3c-ac29-35836e3956a1 | -3.7128 | -60.6211 | 2026-09-16 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 0bdcac45-d475-3328-bc45-6551765391f2 | -6.7892 | -48.6563 | 2026-09-16 13:30:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 146.1 |
| b015a0d9-6836-34a8-87b5-6eed6d792e5b | -6.8032 | -59.1693 | 2026-09-16 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 374.4 |
| d9ab9f73-3380-3e30-b0cd-9a9d6c90e71a | -9.3379 | -50.1814 | 2026-09-16 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 78ece0f1-8899-3f1f-b9b1-c7bc406b98fb | -10.8919 | -54.0062 | 2026-09-16 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c12eb626-9af2-313e-8fb3-5b0836dd8b12 | -8.6566 | -44.4777 | 2026-09-16 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 25c05c70-00a9-3597-b508-f4a7fb5de724 | -12.4145 | -48.4701 | 2026-09-16 13:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 7586f3f1-faef-3f5a-bd51-860e8ce9dfdd | -10.8916 | -54.0267 | 2026-09-16 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| dcbd7a31-0d3e-3c3e-a8c9-66d20478e442 | -10.4772 | -50.9634 | 2026-09-16 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 7cedc4a7-15d1-3b44-9525-ee7d57b81f84 | -10.8571 | -50.8183 | 2026-09-16 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 93084a55-8a72-3ed0-af35-e73f9b0fd1ce | -10.5975 | -47.7505 | 2026-09-16 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 118911d6-d1bb-32f5-bd1f-37c1eabdcc1d | -12.3085 | -47.9539 | 2026-09-16 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3afa2d3c-30b3-3bed-ad6d-a09920325dd0 | -15.4817 | -53.7947 | 2026-09-16 13:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0247ff79-b15f-3ccd-90a8-59a56bdbd959 | -9.5912 | -46.6213 | 2026-09-16 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 269.9 |
| 95a5803e-82bf-3a53-8012-9d91585feb67 | -10.8492 | -46.1998 | 2026-09-16 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| ab2fa4eb-0dfe-36a3-9b06-669b7863ab36 | -10.3116 | -45.3136 | 2026-09-16 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 6820023b-5b4e-3d89-9987-ba7af293b286 | -13.2239 | -51.6318 | 2026-09-16 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 2a211575-1641-322b-a64b-fc8d44ad20af | -9.5915 | -46.5989 | 2026-09-16 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 4efe6ebd-6f5c-3bec-aac2-1c7654178bc3 | -15.4626 | -53.7761 | 2026-09-16 13:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 155dad89-0bfa-3ded-acde-d66841634d34 | -9.5725 | -46.601 | 2026-09-16 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 177.4 |
| fbb009c0-7a88-3b92-bca7-21b02de1cbf7 | -10.9107 | -54.0045 | 2026-09-16 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 94736fff-1664-3228-a481-8a14c192aea9 | -8.5428 | -44.5132 | 2026-09-16 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 254.8 |
| 58b1838c-48fb-34d8-8007-30ea3a56f7bf | -8.5617 | -44.5112 | 2026-09-16 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 242.4 |


[Clique aqui para ver as próximas entradas](README72.md)
