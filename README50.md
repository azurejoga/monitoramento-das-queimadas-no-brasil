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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcbeb921-93d0-3562-ae8b-e80eaec0560a | -18.33991 | -45.13171 | 2025-09-12 04:06:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 346741a0-9daa-38b6-93e0-3793c6f738d7 | -14.18731 | -46.17229 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72f352a6-3147-3134-afb8-4394143d0bc1 | -12.93585 | -48.00629 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dd72b38a-7fda-334b-b7c2-89a2a8fc3a4d | -17.55266 | -44.55252 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1049791e-aabb-3e19-a69f-c83e6bb6868d | -14.16926 | -46.18377 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ff701ba-f380-3713-becf-bd0ccc601e2c | -12.50365 | -47.43964 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 213b41cd-76ac-39c8-8905-ec642e200b69 | -14.26788 | -54.78603 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc13b504-23e3-3890-9d9a-7543ddbbc41b | -12.85558 | -47.61155 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b477acb2-afe8-32a9-b65f-9f9a38b896da | -15.69033 | -47.02266 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63d02cfe-09f2-30e3-9607-5d01c8a842a5 | -15.6504 | -41.82691 | 2025-09-12 04:06:00 | NPP-375D | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 95621b84-eb60-36bf-ada7-c5d0cc621337 | -12.8244 | -47.96034 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e855bff4-c6ce-3c64-b54f-43f1aa9a169c | -17.55099 | -44.55098 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b65c1df-c7a8-3203-968c-1d38247946a7 | -14.17484 | -46.17489 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d09b633-45f1-3567-99d9-4eebc7f334c7 | -14.28201 | -45.04703 | 2025-09-12 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 982ab8ff-6cc0-3bf7-bcd6-4a56fc7e0c2d | -11.97095 | -51.18065 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b941b18c-59c2-35e8-b1c0-063af0d93024 | -15.86797 | -48.33282 | 2025-09-12 04:06:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1768c01b-0079-3d1c-a640-096258a23315 | -16.25109 | -52.65296 | 2025-09-12 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fa8b0a5-fcfd-388c-bc73-a84362b6a032 | -16.49289 | -51.97342 | 2025-09-12 04:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0711e808-2bc5-37cd-bc20-d593dbade0e2 | -11.18437 | -55.09709 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f525b23-b28a-31cc-adb1-8ca8aeca1e79 | -11.52715 | -50.59875 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 26723659-1868-360c-be4a-8b987696da1e | -12.84101 | -47.95771 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cf4ef071-3faf-3245-8097-663470435071 | -11.53142 | -50.40298 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 5973a4b1-6a39-34f8-a039-4ec90242f925 | -16.6022 | -49.81298 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5f5574b-e865-347d-b1dc-e4dd1b2d8645 | -12.00317 | -47.76745 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 667bcd02-801d-33b8-9965-e27df7ee5802 | -13.9028 | -48.2682 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| c52d08a3-f21d-3b44-95f4-ba5114c6c03c | -11.19036 | -55.08093 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fc17fa2-5661-31f9-aed4-9637c2b0ca58 | -15.11709 | -48.60298 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ea2e917-f7a3-3e9b-9737-6737d71c2513 | -14.2864 | -45.04333 | 2025-09-12 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fac4f41-fab7-39ea-9fa1-31ce492e1388 | -16.5965 | -49.81732 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 035f5931-4830-3bf1-9a62-5ee02c8549ce | -13.90462 | -48.23375 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 69801a9e-63ff-30fe-b460-795f103c95e5 | -12.0023 | -47.56789 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88beeef9-a235-3d35-a4b6-3dbcd52a4199 | -17.20129 | -50.15124 | 2025-09-12 04:06:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 27db62e4-dfc2-3be5-a2d9-11196ecde156 | -11.97824 | -46.65451 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddc1ecd0-17f3-33c5-9dff-afc49a8399bb | -11.98108 | -51.12834 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42982d86-8f7e-3cd3-9fc2-7118cd78996a | -12.08362 | -47.5895 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 28585796-fe51-3fa5-953e-ca4ab1c94fcc | -11.51608 | -50.3964 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 552b7070-a422-3c14-ae8b-917d36b5882b | -12.82103 | -47.9663 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7178df27-9771-376d-83ac-093f8295df50 | -15.78354 | -52.23907 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 317d4c81-1f68-3386-8d08-4b48228ab61d | -14.26332 | -54.7945 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3346a0c6-ee22-354a-915a-d6386de5a168 | -16.60807 | -49.78827 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e8175376-7226-32dd-8524-0a2511eaf6d9 | -15.10562 | -48.01982 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1a0d2dc-aba0-322d-9341-af7a1d1aa35e | -14.17397 | -46.17981 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f40c73b7-8e71-3a6e-87c9-129c74a86bc7 | -18.05816 | -45.44634 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b845dac5-e164-3eb9-9533-0023513f1fb9 | -12.5383 | -44.69149 | 2025-09-12 04:06:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cd0868c-7414-315b-be52-3d5bbcffb950 | -11.97891 | -46.6507 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d80eb778-b4c9-3123-a14f-b7f6ae094873 | -16.59284 | -49.81104 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef65f2da-e2e2-34ff-8d02-3f85b4524e5a | -12.58787 | -45.68171 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 560d163c-6cfa-3056-a0ff-d95fba798807 | -14.17571 | -46.16997 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c64d00b0-7dfd-318e-8631-bf847fc749ef | -16.43397 | -45.68277 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c339f08a-562d-35c0-a56e-cd06560408c5 | -11.18479 | -55.07231 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e8f733a-c4e4-3c29-a406-a914f528fff4 | -17.58847 | -42.16745 | 2025-09-12 04:06:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4bd5bbdf-04a7-3541-ab54-902322faeaa1 | -14.45552 | -47.3118 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08d163dc-afa9-3381-be57-2fcc3aaee4cf | -17.7227 | -46.13668 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 84d0b354-5cbd-32af-8b92-3f1f9fe5464b | -11.22169 | -54.90015 | 2025-09-12 04:06:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b70d0a3-65fb-35c5-94ce-170fe2730668 | -15.79508 | -52.23436 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f27a349e-8c4b-360e-aecd-ac3063aa0ba4 | -11.80373 | -50.57087 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f485a33-6aeb-3bb3-8219-a62e2b914e99 | -12.49934 | -47.43882 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c5befa0-04b0-36fe-bd3e-47714d72fdc9 | -14.56565 | -48.75276 | 2025-09-12 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 369faa65-7547-3fb4-bd60-aa0509ea4fbf | -11.53011 | -50.40976 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b82a0eda-0047-3fa4-b30c-843db1ee86fe | -12.08279 | -47.59408 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f0c2f33-0e1d-3bc5-9a2e-84636ac5a5e1 | -11.62899 | -50.57224 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53f0175b-b98f-3dc0-99cd-64875225ab1e | -14.37411 | -47.28877 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 544ac7dd-a3b7-3bbf-9e2d-ab1732cbb09a | -12.46075 | -47.49901 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e1c5852-d09e-373a-847e-7b21ff47a0c9 | -18.06318 | -45.43859 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8b17d29-8613-3789-a639-1b4043663ed6 | -12.89579 | -47.95919 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 494f41d7-dae5-3107-ac6b-086090b9dd24 | -14.41279 | -47.31139 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e331369f-fe78-35fb-b395-6c7015f0a73a | -15.48984 | -47.34967 | 2025-09-12 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da7fb195-e3f7-386c-8e07-857156f95368 | -14.4234 | -46.39979 | 2025-09-12 04:06:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b8dd463-62c4-3a57-8054-7f420c14b451 | -16.56879 | -44.57986 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e757be6-382b-3689-8d06-486727d4df03 | -13.9628 | -44.18163 | 2025-09-12 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7bf9057-742b-30ae-a21f-c08c12aafca4 | -11.52648 | -50.60225 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 17a73516-206a-39a8-a742-9d54578a7195 | -15.15129 | -52.46363 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aa9a9799-4fb5-3ee4-a889-349dc1ece65d | -15.08322 | -52.44223 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf05cf40-b1be-35c5-a168-53b5cd1789f2 | -11.80845 | -50.57542 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd3c1177-497a-35d2-b40e-9e451bf54c53 | -17.34677 | -46.70094 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7caac8ad-27d8-3c95-bcac-f0781f8af9c9 | -15.69337 | -47.02872 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf151112-a40a-39ac-a080-e3dee28cc850 | -13.9171 | -47.94817 | 2025-09-12 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83ded519-0cee-30a2-b254-87c9bf6d2b5f | -11.50339 | -50.37631 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5020de57-b840-38aa-81a1-e4c0c178d869 | -11.53208 | -50.39958 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 56446362-3136-31e7-9afe-10a7cdcc25ef | -16.4055 | -44.04594 | 2025-09-12 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de80c8f8-c72d-3981-97e2-3764d7d68d86 | -13.78361 | -46.27949 | 2025-09-12 04:06:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a0eec10-06ab-3eb1-bd84-817958c12d95 | -11.9748 | -46.64978 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0de77571-2692-3519-b85a-334929d65cc2 | -13.31701 | -44.08998 | 2025-09-12 04:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 195512ef-920e-3577-969c-68023fa487a9 | -15.60328 | -52.74029 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e705b7d-8a5d-3111-803e-8afcbf3fd585 | -17.56133 | -44.55281 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeeb634b-ef7d-3775-9f68-a644075e683d | -12.8506 | -47.95549 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 46e9d21c-6637-39a9-a59e-438c09238ed9 | -17.33304 | -46.66774 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f15e8ae-3c48-3841-85f1-19302f7c2e5d | -11.18587 | -55.08986 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 838b9d8a-1cd3-3e7e-a1fa-8fac8832fd94 | -18.0204 | -46.85558 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cc27dc2-f61a-32c0-910e-20930252ffb8 | -14.17355 | -46.20481 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 680e1c4b-00c7-3594-b5ca-3aa7380615e1 | -12.9303 | -47.99657 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e558429-520f-37ce-bb12-5f7546305059 | -15.66993 | -47.06746 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39426c5c-ffb7-3e83-b8fe-1426de7339da | -14.77805 | -43.93074 | 2025-09-12 04:06:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da48605a-7bf2-3045-b408-b5dd6bb2ebbc | -13.89986 | -48.25925 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 88c74b2c-5628-3bb4-b19f-406b9e89d042 | -12.93052 | -48.01019 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2eb40fd-4356-3f28-b1ed-94932dfaa790 | -16.44131 | -49.0284 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11da4f22-9d98-3529-b584-5b10c9892689 | -12.39531 | -46.50314 | 2025-09-12 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6aa879e4-1a91-34cf-b162-ebdb1b267a56 | -15.07847 | -48.01074 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e8a9006b-a256-324c-a274-1a68c41ca510 | -14.66512 | -44.06388 | 2025-09-12 04:06:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 179ef343-6e65-3b52-a7c0-7d4b6768ada7 | -11.86526 | -46.75962 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README51.md)
