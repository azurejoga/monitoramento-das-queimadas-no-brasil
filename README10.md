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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2c79670-16b7-37a3-98d1-b22fd04ca1e3 | -8.8665 | -49.745899 | 2026-09-19 00:19:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6c6834e-aa2e-34a3-87d4-9b422f035e21 | -1.6376 | -55.1423 | 2026-09-19 00:19:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 833cec84-f0e9-3662-a5ba-774439923692 | -18.042299 | -49.289398 | 2026-09-19 00:19:00 | METOP-B | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9988ca3b-ded3-359d-b439-0099e0701ede | -4.2543 | -48.5298 | 2026-09-19 00:19:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aaa4670-6a41-35c3-96fd-47e415be25a6 | -6.6777 | -50.906601 | 2026-09-19 00:19:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe1ca646-c5c4-3a8b-be5d-9e09bcef2f04 | -5.8393 | -49.857399 | 2026-09-19 00:19:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f65e04bc-4950-3c2d-9792-dffa57909b7a | -5.8955 | -49.787899 | 2026-09-19 00:19:00 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 210f0108-cecd-33d4-bb07-95c9851ea35b | -7.0196 | -44.648602 | 2026-09-19 00:19:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ab82937-c81d-36f8-bb46-4a66d66dca8e | -10.9914 | -48.3158 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9d90080-84b7-3893-8151-3a65bd8bf68b | -8.7628 | -48.6731 | 2026-09-19 00:19:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8bb0ae75-ddd0-3fad-b29b-dc30120a2026 | -14.6791 | -46.648102 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 89c87947-66cb-34bd-b7b6-07cb004919c3 | -6.3484 | -51.726398 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b90e899-59b3-3445-a2af-150f8eebb5aa | -11.8304 | -46.838402 | 2026-09-19 00:19:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f19bc37-088a-3a51-8fc5-90d5c98eb208 | -12.3439 | -50.713799 | 2026-09-19 00:19:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b83e8f35-44d9-3b26-8c22-ec0c670ec7b0 | -6.0268 | -51.762501 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03a84af1-c04f-3c53-bc25-8b8e330d8a09 | -4.491 | -54.9701 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f61056a6-b974-3c05-80b7-d84b299e67a7 | -2.812 | -50.4557 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b35cc3f2-cd10-3311-83fc-82da2145c210 | -10.1717 | -48.519199 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ada3348-7486-3e39-8256-97683f8405c5 | -19.566099 | -47.665501 | 2026-09-19 00:19:00 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a62689e3-f9b5-36da-ab29-6266d52ef6d3 | -12.595 | -49.09 | 2026-09-19 00:19:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5df14a7b-01a6-3695-a435-d7b0bca95dba | -6.0005 | -51.782902 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6da7fde-bf43-3958-90df-e9094360941a | -10.8831 | -54.047298 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4a6f077-7c65-3a93-8590-05fd63e8fbce | -18.8724 | -49.507801 | 2026-09-19 00:19:00 | METOP-B | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9120fdfa-1787-3fab-957b-935712f08af9 | -7.6616 | -46.1115 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79971bee-0dd4-3c10-84c7-7f7665aaa27e | -15.0814 | -49.595001 | 2026-09-19 00:19:00 | METOP-B | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 48c49db7-6632-3310-ae4d-fe6568303d84 | -7.6546 | -46.1255 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cc132a5-abdb-3cee-8c6a-affca7c6c775 | -10.7197 | -60.715 | 2026-09-19 00:19:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d68348c-9b4b-3a00-8efb-e811ccf811a7 | -4.3577 | -47.779301 | 2026-09-19 00:19:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af8fb9a6-49d6-397f-a7ba-0cb7ef43ad0f | -15.5811 | -56.5229 | 2026-09-19 00:19:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77c72457-d2d1-3b81-9dc4-8401a9531f8e | -11.8566 | -47.601799 | 2026-09-19 00:19:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 762824d3-7976-3ab3-b618-4fef0bf89cae | -10.5746 | -46.597401 | 2026-09-19 00:19:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a50688e8-f910-3fa7-ae16-00ff3fed0133 | -8.4219 | -54.7178 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e6a89b-3814-30b4-999f-788a3290f088 | -12.5964 | -50.876202 | 2026-09-19 00:19:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0042354-0f50-3b48-b96a-6c50bca11ac0 | -9.8038 | -46.397499 | 2026-09-19 00:19:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a563501-d975-3bdb-b20d-c6c5dfecbf61 | -16.0788 | -52.2481 | 2026-09-19 00:19:00 | METOP-B | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93a3589e-1799-38de-9956-28fec1f90ef6 | -8.7688 | -48.654598 | 2026-09-19 00:19:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5bc7b83e-4221-350e-b333-27c4b5302378 | -11.3643 | -44.1241 | 2026-09-19 00:19:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 062ec1a5-8b33-3fe3-9f86-8e53ccb6f68b | -22.036301 | -49.548302 | 2026-09-19 00:19:00 | METOP-B | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2aef5780-6a81-3f9d-90ef-d43239dcad8e | -8.3707 | -47.224602 | 2026-09-19 00:19:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36202a7a-56ae-37cf-87b8-c3e4a5e0adfa | -9.691 | -54.323002 | 2026-09-19 00:19:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16b879bc-05e9-3e20-86c3-52b1d3fd90f6 | -5.8923 | -53.547199 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f128fe2e-3efb-3618-8e1b-d6c51b20ca5a | -12.2899 | -49.154499 | 2026-09-19 00:19:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90c00624-89b7-3a94-961a-42bc5d670494 | -7.1766 | -49.932598 | 2026-09-19 00:19:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84cf0220-8641-3756-9489-6ef006cb78e5 | -7.649 | -46.1022 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e41ae9db-31f4-3a50-9998-54e723e31833 | -16.3064 | -53.850201 | 2026-09-19 00:19:00 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dcb07cfb-6ed6-3480-b9f7-78f948d82c01 | -3.3658 | -50.443699 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aecf369b-9a97-36a8-acc4-e87fdecee165 | -5.8937 | -49.780102 | 2026-09-19 00:19:00 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f2e7c2a-c8db-320b-b2a0-f04b26fec012 | -10.1666 | -48.452599 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f821a78f-0bff-3de6-aabb-930809b02abb | -5.4989 | -43.762299 | 2026-09-19 00:19:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22ed8756-2162-30f0-aba5-7d867392fdcc | -14.6861 | -46.6657 | 2026-09-19 00:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 113.1 |
| c6f5e519-eaf2-39e6-81c3-a0f78b9fb234 | -5.5249 | -43.7953 | 2026-09-19 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 171ceb22-ff97-3e7f-a5f2-12b5d7257319 | -4.0576 | -56.2471 | 2026-09-19 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 440f41d1-9446-355c-ab0b-652586cef977 | -10.7115 | -60.7312 | 2026-09-19 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 46eccb35-3ad9-38c9-aec1-53b13369e0c6 | -2.8284 | -50.4863 | 2026-09-19 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| d7d96779-1ff4-3cd6-90b3-4a491febbf16 | -5.5064 | -43.7735 | 2026-09-19 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 01a90292-f5ab-3020-983e-2ae9ab13e505 | -14.6856 | -46.6886 | 2026-09-19 00:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 1743c0f0-89f9-30f3-bc8d-d02e308aa6ef | -7.6386 | -46.103 | 2026-09-19 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| d7ef0954-b8b0-3055-ae54-5d7cc669f57f | -5.5251 | -43.7721 | 2026-09-19 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 4be9697d-1a98-3d17-9dfc-2bc10f3734aa | 1.2608 | -50.976 | 2026-09-19 00:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 50.1 |
| df4edaf5-ddf8-31bb-9358-76d9e573eeca | -7.6574 | -46.1013 | 2026-09-19 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 818df2b5-8fad-3a88-beb2-84998c165140 | -3.3638 | -50.4492 | 2026-09-19 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 415d8bb8-c2ea-3381-971a-d8b76e916108 | -6.9871 | -42.1917 | 2026-09-19 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 900a49d8-7c0b-3c7f-94df-8f0ce34f6589 | -3.3311 | -59.8101 | 2026-09-19 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 707dd6fc-b6d1-380e-97f1-5f3ad5f56890 | -2.8285 | -50.4653 | 2026-09-19 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 247.5 |
| b0cfe8c8-eb32-3b87-8c82-217fb05ce8fe | -4.3587 | -47.7853 | 2026-09-19 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f60dcf77-2297-33d7-8914-1d3183206663 | -3.2313 | -46.9596 | 2026-09-19 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1aa9db0e-8cbc-35a1-aa12-68be2fbb547d | -8.4983 | -57.6271 | 2026-09-19 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1d78eba5-0daa-3aec-b1e0-27eaf083437d | -2.8101 | -50.4658 | 2026-09-19 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 3eee05bd-544f-3491-9415-8925eead3a63 | -7.6384 | -46.1254 | 2026-09-19 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 265248dd-0eb5-3e73-8a95-f84eec144057 | -5.5062 | -43.7966 | 2026-09-19 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 6247df82-8b67-35d9-9efd-06137d9fb040 | -12.5952 | -49.1046 | 2026-09-19 00:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 4bde0b50-c20e-3429-ba00-55b765c666ea | -10.9301 | -53.9618 | 2026-09-19 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 0110b292-5585-3055-b2c4-6a105ac0d24b | -10.867 | -56.1975 | 2026-09-19 00:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 72959a70-4ce2-338f-b4f2-03ae4e0a930f | -18.3903 | -49.1573 | 2026-09-19 00:30:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| 4e6945a0-a0b2-3b18-b618-b857c8724645 | -14.6861 | -46.6657 | 2026-09-19 00:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 113.7 |
| e48643f9-4ff4-3463-8a62-137bfa62254d | -6.001 | -51.7903 | 2026-09-19 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 965d7154-c618-3cd2-abf1-7e98ee1ceb25 | -10.7114 | -60.7505 | 2026-09-19 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 714b9cfd-d00c-3292-a2ba-9fd8667076d3 | -10.867 | -56.1975 | 2026-09-19 00:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 1ae0d77b-96e5-334b-a212-0c114424a7be | -6.1861 | -47.2625 | 2026-09-19 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f2d19e4a-c19f-354a-a740-8f569d8fd316 | -3.3311 | -59.8101 | 2026-09-19 00:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 6de36568-0a76-33ad-83a8-5b050a33582e | -18.4104 | -49.1534 | 2026-09-19 00:30:00 | GOES-19 | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.6 |
| 7c6b3e00-1e7b-317f-bb71-63eb45ae1740 | -18.3898 | -49.1799 | 2026-09-19 00:30:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| 94614133-37bc-3501-87ac-4be32ed26b73 | -3.3638 | -50.4492 | 2026-09-19 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 9bd2f85c-bd70-39ac-954e-6e7aef111647 | -10.9301 | -53.9618 | 2026-09-19 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9e598d8c-95f1-3346-934d-8c35ae5f3382 | -2.8101 | -50.4658 | 2026-09-19 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a4482977-a19f-35eb-83aa-81cffc7d4385 | -6.1859 | -47.2845 | 2026-09-19 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| e9e3a7d4-e4b3-3bfe-9706-1dc7f18e11f5 | -14.6856 | -46.6886 | 2026-09-19 00:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 47e2bb09-10bd-348b-9814-f6e1c0bc8848 | -2.8286 | -50.4444 | 2026-09-19 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 7d4cee10-1668-36bb-8349-85126dc3b35b | -2.8284 | -50.4863 | 2026-09-19 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 75d655fa-ec2e-3003-aa9c-867bb65bc2d4 | -8.4983 | -57.6271 | 2026-09-19 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 49894a87-d3d6-3599-94f9-5cc70e4afeea | -8.3581 | -47.2378 | 2026-09-19 00:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 011e9a29-739d-398c-bf30-64b6ddf3ca4b | -5.5251 | -43.7721 | 2026-09-19 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 53a291d4-951d-3a8a-9967-7caec7a19a0b | -18.4098 | -49.176 | 2026-09-19 00:30:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| a6697b33-696d-3c81-bc61-345f64e1cdbe | -5.5062 | -43.7966 | 2026-09-19 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| fb0ed142-4f28-396a-aef0-35fe2af615d6 | -12.5952 | -49.1046 | 2026-09-19 00:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| e80712c0-ac4d-3ec5-82fb-d8cd3cdd29bd | -2.8285 | -50.4653 | 2026-09-19 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 158.7 |
| aa25c541-f296-341b-923e-f7d663a47c79 | -10.7115 | -60.7312 | 2026-09-19 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 02e5585b-791b-374e-811f-364485f2c677 | -5.5249 | -43.7953 | 2026-09-19 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 5ca59e6b-8503-3b17-9015-2ff52f7f3b59 | -18.40056 | -49.19012 | 2026-09-19 00:37:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 957b57b3-5a37-33b2-b2e6-5cfba619edbe | -18.87386 | -49.52103 | 2026-09-19 00:37:00 | TERRA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |


[Clique aqui para ver as próximas entradas](README11.md)
