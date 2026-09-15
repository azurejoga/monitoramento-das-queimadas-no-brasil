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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3e70cef-c414-32f9-aa38-c83f3d669d69 | -3.0434 | -61.27093 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98a30c23-535f-368f-8bc8-96f6a4348eb4 | -8.85139 | -62.36317 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47c1ed04-d328-3b8f-b7b0-af08431a3c14 | -5.12786 | -55.94572 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcc2ac7c-ee75-3b30-aae8-e31123e30e7f | -3.69911 | -58.87833 | 2026-09-15 05:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00234bca-645e-314f-a004-fd5a6ebb7c19 | -3.41949 | -58.21817 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 224f1d58-4a0c-3893-bc21-af7592f12631 | -10.69057 | -54.17698 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c4e23e5-a03c-37a0-9697-570e7e121739 | -8.82076 | -62.49178 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dabae8cf-96f2-3934-a157-a94632539878 | -10.67309 | -54.15834 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b67c1601-303c-329e-8065-fc789853e3a0 | -3.18279 | -61.1152 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0dc3da2-3323-3381-90c7-5978dffbba84 | -10.68343 | -54.18164 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11e53a4b-1297-3db1-a6d1-828ac62ab34c | -3.08592 | -61.19037 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8d39d4b-46d6-329b-9d06-4c6ef2d616b5 | -3.17977 | -61.1103 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 518fdbf9-3718-3eb1-b423-d22c5c9d67ce | -3.17412 | -58.64861 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b9dd740-2e07-3e65-b61f-18ee82d57eb2 | -9.10509 | -65.56205 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb9285d1-5de5-3f6c-ac11-0886bf8102e5 | -8.78136 | -66.67783 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c248611-3999-3452-a09d-30e5daf3fec6 | -9.49526 | -56.75033 | 2026-09-15 05:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54015e32-a2d3-3ea7-a5ae-65c50825f33b | -9.69514 | -58.17545 | 2026-09-15 05:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 06e0f407-12b6-3498-b930-61cba50eab08 | -9.06881 | -61.00965 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb338a9c-b263-3a41-91b1-f1d6940fae01 | -5.07929 | -56.2467 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 282b4b42-bad8-3ebb-925a-6eda97fbad6a | -9.08077 | -61.01938 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4154154e-840f-314c-8931-039282ebad10 | -9.2646 | -59.6364 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbad11a0-063f-3e3c-9578-2055e705e10f | -9.67981 | -65.79714 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b992d4dc-cb06-3096-8e2a-e0dcead14500 | -13.39185 | -57.02534 | 2026-09-15 05:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfe7ecae-e41f-30d2-8f6d-3f49cd36cf15 | -3.42394 | -58.21885 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c8b4672-caf4-39fb-89a1-dddccd0b7b1c | -4.52206 | -54.96983 | 2026-09-15 05:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f950438-9b13-3cff-b620-50f2531e7e03 | -3.69848 | -58.88236 | 2026-09-15 05:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62690b44-e00f-32ba-95ed-b56d42795972 | -10.6666 | -54.15768 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f92e751-7051-3b4a-9a6d-bb811e0c87f3 | -10.23001 | -56.26044 | 2026-09-15 05:55:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12941dea-c2b7-3716-9c4e-895eecb5bc2f | -3.18346 | -61.11086 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 434a178e-552b-3373-afb2-01da396ec244 | -3.54741 | -58.67516 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77a8f8fc-f540-39c7-8ac0-264c29ef77e8 | -9.64269 | -63.50813 | 2026-09-15 05:55:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26cdf78a-7c58-3ecd-93f7-62d5efaba0ab | -3.74063 | -61.74696 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 557f917f-d159-30f7-8288-1a20ee842d8b | -9.6959 | -58.16994 | 2026-09-15 05:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fef6ee72-0c12-3e9b-860f-ec0b87cb9db1 | -4.52262 | -54.96595 | 2026-09-15 05:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91a3e122-1ed0-369c-9484-afaa32a16d77 | -3.12814 | -61.41997 | 2026-09-15 05:55:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40e2400f-2e6c-3abc-8b43-fdc7f729c452 | -10.66725 | -54.15224 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13a97031-4903-3df0-bd97-72fedcd430da | -3.10811 | -61.09673 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7629d0e-e05e-3707-bd07-a2e9d3e8f76b | -8.54093 | -64.0079 | 2026-09-15 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccb665b2-28fb-3ac5-a28e-f7f41d67fa69 | -9.25752 | -60.28109 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cc60e14-811b-35e2-bcfa-812a6b1ca5ce | -10.6977 | -54.17236 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed3f61ce-945c-307e-b6cf-79fa7ad75800 | -9.507 | -64.71152 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3087e33d-1da6-336c-9ae0-afdda7e323f6 | -9.26784 | -59.64045 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3747e80d-c25a-356f-9991-b5d75da84045 | -9.41183 | -62.71646 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 290d2107-d29a-3d3e-8a98-a009b308d497 | -10.60155 | -57.31703 | 2026-09-15 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ca9e773-952b-3fe9-8553-cb8a79ce9e33 | -3.1118 | -61.0973 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d0fb71a-eb38-3a4c-81fd-1475728d2c11 | -5.80985 | -53.80285 | 2026-09-15 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5c494be-413d-313f-86f9-22a13242a05c | -9.19876 | -60.39173 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c11db37-6b2c-334f-b2fb-36b828f806ae | -9.71625 | -64.91364 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8b0e733-695d-3286-9370-6ed1449b2b03 | -9.64622 | -63.50865 | 2026-09-15 05:55:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e13490ec-c1a1-3edd-b3d7-81bbd66d249b | -9.71177 | -64.9203 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac636c05-e125-333c-a64d-c8518cd612c6 | -5.12208 | -55.94792 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f88325e-f7e6-395e-9f19-8afd1ed484b4 | -4.39314 | -55.20684 | 2026-09-15 05:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6698f11d-eae9-389a-87a6-d57f753fc426 | -3.14563 | -60.63315 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25d2b94d-3c6d-3949-9ddd-2b9c2a33ff71 | -9.13966 | -65.83276 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e56733e0-5be5-3464-b301-fa3688039004 | -9.25808 | -60.2772 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08944a49-edfa-32c6-ae84-06b761f911ac | -3.60092 | -59.06448 | 2026-09-15 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 280c0ef7-a7f6-35c6-946a-8ce2ff8173da | -10.23564 | -56.26128 | 2026-09-15 05:55:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2bde947-d7a3-32bc-bfd2-436c34954546 | -3.35233 | -59.82698 | 2026-09-15 05:55:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f0a396c-96d7-3d17-a143-8dd321adbb77 | -3.44943 | -57.99033 | 2026-09-15 05:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88ad6648-d68a-3e0c-94a5-1652903f00cd | -4.51642 | -54.96884 | 2026-09-15 05:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6085a3b5-12fc-3204-a410-a85d813871e2 | -3.70073 | -58.88214 | 2026-09-15 05:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 179bb5ed-a5bd-30d8-9597-a8dfa372dfee | -4.38814 | -55.20217 | 2026-09-15 05:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 150a1b28-48d6-3379-ad99-79d1e7db616c | -3.08195 | -61.52748 | 2026-09-15 05:55:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9aa12cd-047c-34a7-adac-fc470d3d4a2e | -10.67375 | -54.1529 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ff27a8c-b062-3aba-9c13-bea93442ad86 | -9.20296 | -60.3923 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2dcabf0-ee02-3899-a11b-97dbf7734415 | -5.12737 | -55.94912 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32a3174d-ce67-30eb-9dc5-1eed66727477 | -9.53041 | -63.62885 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a99c8dd-cc2c-396c-9344-4547864950df | -9.4102 | -62.7113 | 2026-09-15 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 052ea0e3-c9f6-3b1f-89b1-2d0ae89cf325 | -18.1714 | -51.7466 | 2026-09-15 06:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 223f3f80-e769-3e1d-af61-1031a9ec5623 | 4.50044 | -61.17586 | 2026-09-15 06:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee412784-9b02-395b-a23c-73eca98e91c8 | 4.49495 | -61.17568 | 2026-09-15 06:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed8c25a2-1aef-3b91-9d67-47ef8c3f5f55 | 2.41236 | -59.95505 | 2026-09-15 06:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ded1db9c-5f1b-3482-bbce-04874f48aa6b | 2.70195 | -60.3018 | 2026-09-15 06:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30ceb62f-d190-39d1-b177-3fe60cb5c5f5 | 2.76732 | -60.21847 | 2026-09-15 06:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b909a830-5826-3adc-a4e7-de67b28e987d | 2.41173 | -59.95126 | 2026-09-15 06:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cad94035-75e9-38e9-b862-2416c9b2c1ee | 2.58375 | -60.306 | 2026-09-15 06:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 552eb761-890f-3efe-b9cc-36dac976d39a | 2.58316 | -60.30245 | 2026-09-15 06:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 477b742d-86dd-3557-b553-33e7f4700820 | 4.49995 | -61.17488 | 2026-09-15 06:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38f185fc-99dd-3688-aacd-79d095313c56 | 4.49544 | -61.17664 | 2026-09-15 06:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc601c8f-2f25-37a6-bd5f-5aeb79a96150 | 4.49494 | -61.17376 | 2026-09-15 06:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 031273b5-2e89-31c9-9674-0c9ac7cbeff4 | 4.49994 | -61.17298 | 2026-09-15 06:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d03bc3d-ee73-33da-a49f-b834b9159060 | -2.69311 | -57.52141 | 2026-09-15 06:12:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1b686e9b-d622-30e4-985c-42980ead7691 | -3.12561 | -61.24986 | 2026-09-15 06:12:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 330547da-328b-3bc6-be52-fca2405c8bb4 | 0.62133 | -60.15906 | 2026-09-15 06:12:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 504b0570-204e-34ca-b935-cea0a54556be | -3.5512 | -58.68102 | 2026-09-15 06:12:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 308d0e83-7911-3cc4-8c9a-db29ea7f31cc | -2.69105 | -57.52257 | 2026-09-15 06:12:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 72cc05dc-5697-329b-a9e6-5c54c690c03f | -2.69912 | -57.52915 | 2026-09-15 06:12:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 611be244-0605-3f67-9e78-c5fef447b8b5 | -3.35074 | -59.83026 | 2026-09-15 06:12:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4303e0a9-dda5-35c9-ad9a-151af2af9081 | -3.12616 | -61.24611 | 2026-09-15 06:12:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0b00a5a-a60a-3c60-83b3-ffdaff6e064e | -2.66602 | -57.55837 | 2026-09-15 06:12:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 42ea80eb-f413-3a30-83fd-6bd9d547ca40 | -2.66502 | -57.56501 | 2026-09-15 06:12:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4b5d6489-6ed3-36a4-b20e-a204d6f556c8 | -3.4202 | -58.2243 | 2026-09-15 06:12:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a97c1b8e-a063-3c19-9554-0162645c31f7 | -2.6971 | -57.53035 | 2026-09-15 06:12:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a02d9f6-1802-3cdf-b006-6faf2cc04074 | -3.54458 | -58.67994 | 2026-09-15 06:12:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e140090b-5a1f-321e-ba2b-be85cb3215fb | -3.42701 | -58.22533 | 2026-09-15 06:12:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcb1fdbe-e273-34c9-9b39-45458811405a | -6.01814 | -59.93184 | 2026-09-15 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| be4e1731-a70e-3116-aafc-a1a5029af6db | -9.71729 | -64.9169 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8320e0d-9d32-3bde-a3c6-6149795bab01 | -7.56162 | -62.33179 | 2026-09-15 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3e4f98e-9fbe-3693-b5db-47959b58d1e5 | -9.10199 | -65.55827 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 893c89c4-8880-3694-86af-6ca0631920cc | -9.13901 | -65.83302 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README69.md)
