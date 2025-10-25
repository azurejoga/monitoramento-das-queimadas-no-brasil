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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb4b221c-7475-3f2a-a589-5cfbb4f516b9 | -18.1714 | -51.7466 | 2025-10-25 03:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 6b13285b-3b86-3b3a-b6a4-8c828e288717 | -2.8149 | -49.1354 | 2025-10-25 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| caf508cb-30d7-3729-b24c-e43eba25ae69 | -14.8706 | -48.0822 | 2025-10-25 03:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| fec3981d-3ca9-3cc1-8095-29e34bb7668c | -2.7964 | -49.136 | 2025-10-25 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d2186967-70b3-3ba1-b530-600c07e1ae42 | -2.7964 | -49.1572 | 2025-10-25 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 791f685f-8227-38d6-9de5-1a3c3040f9bc | -14.8701 | -48.1047 | 2025-10-25 03:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e483c831-b4be-320c-9b38-1c02fc112bdf | -2.8149 | -49.1354 | 2025-10-25 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9f6a2df9-22bb-377e-89fe-090e70e4d584 | -14.8701 | -48.1047 | 2025-10-25 03:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 8eb4014a-f0b8-3427-9c11-648de17a945d | -2.7964 | -49.136 | 2025-10-25 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e4efb0af-c397-3e9b-b2cb-68c660162c0e | -14.8706 | -48.0822 | 2025-10-25 03:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ea92683b-b1bc-32a1-8fba-9a329c4e55d1 | -9.12176 | -45.85839 | 2025-10-25 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2975ecf6-09c2-38a4-9098-fb7560d98bc6 | -4.55324 | -46.68923 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ff562317-cf24-3b45-80cb-16f3554b6526 | -6.11049 | -41.74705 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 206b5d7a-acc5-39fc-b8d3-bfd67778754b | -4.22363 | -48.6152 | 2025-10-25 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c10259ee-74e5-3424-8acb-644ac1691149 | -2.72693 | -49.16409 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a74d9c81-c6ba-360f-a84a-0add78750aa6 | -5.93666 | -43.36563 | 2025-10-25 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| adb782e9-87a6-39f7-9904-2f021a295c7c | -5.8228 | -40.80672 | 2025-10-25 03:57:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c2eb41ea-5a0f-3061-8d49-23c237c9a494 | -6.13985 | -42.45863 | 2025-10-25 03:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5dd39ffa-d672-327c-9b2f-fa9993b4fe4b | -7.5868 | -43.57024 | 2025-10-25 03:57:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7772274-6c16-3aa6-9f34-bf1f9643c2f6 | -5.13588 | -41.19889 | 2025-10-25 03:57:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fed0b567-4410-3a59-b4d3-9be34a986984 | -9.62195 | -40.34501 | 2025-10-25 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5a78b169-ab37-3347-86e7-3ae4dfb95678 | -7.78594 | -45.39608 | 2025-10-25 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d08d2f67-05f2-381b-bebb-7760b043ad48 | -6.32 | -41.85872 | 2025-10-25 03:57:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 90fefae5-d464-33f3-8189-5428947f1261 | -6.59192 | -44.32352 | 2025-10-25 03:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64e3c4fc-2489-39e2-af6f-32ca5e3ebda7 | -5.45705 | -45.40641 | 2025-10-25 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac23e077-f9e3-3134-be3b-0f54971ee36a | -3.9046 | -38.52205 | 2025-10-25 03:57:00 | NPP-375D | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 809d8475-f245-35fa-83a2-8440f81bca79 | -6.83222 | -44.78049 | 2025-10-25 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcf72386-a024-3027-9032-dd8f7cb1cefc | -6.88397 | -43.61665 | 2025-10-25 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea1aa86f-c231-3dab-9660-c92629840007 | -5.03626 | -41.19559 | 2025-10-25 03:57:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b84d5a9a-28f2-3765-9c77-758ae5776d74 | -7.94291 | -47.20196 | 2025-10-25 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fef3998e-bf0f-34c5-b992-65197c72b5d5 | -5.72368 | -49.09944 | 2025-10-25 03:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 251e75d3-a79e-3e12-bfac-b1a2b628e8c4 | -6.9161 | -45.1587 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eef5f43d-e0b4-3a2b-8af9-5782ab53f978 | -7.62397 | -42.20986 | 2025-10-25 03:57:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bc910906-e2e8-32c3-80e7-4a229fa2047a | -2.8117 | -49.14052 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7b30eec8-e1c2-3af7-9178-51893eb71bb2 | -9.61917 | -40.34085 | 2025-10-25 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9cb4525e-dfca-35eb-b71c-eea280f16198 | -6.83766 | -41.5483 | 2025-10-25 03:57:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3edfe1dd-d882-35ad-a874-22af8dd3897e | -9.6728 | -35.82697 | 2025-10-25 03:57:00 | NPP-375D | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 525c3d28-ceb7-379c-af9b-ed7d4caaad41 | -8.50102 | -44.08532 | 2025-10-25 03:57:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8355fea1-e29c-32c1-ad25-f7487cc3c4a0 | -4.8331 | -50.92994 | 2025-10-25 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1c3c36f8-b3db-3275-9869-7686453f2f8a | -6.80383 | -45.4297 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3be7dcc4-a63d-33d4-9eec-d035b9f774fd | -8.1057 | -44.49799 | 2025-10-25 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f23c059-7632-305f-9cba-6d425d4c3877 | -4.9592 | -47.59835 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b7ad7b8-2060-3588-876d-df293a5c4bc0 | -4.00147 | -43.75321 | 2025-10-25 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bdeacd2-162c-340e-8801-ccb4574cfee4 | -6.1287 | -41.72777 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ac8b7a55-1850-3812-bfa1-f06a50af92c5 | -4.2261 | -48.61695 | 2025-10-25 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8163db78-ce1e-3e20-940a-f9e0359a65fc | -8.13061 | -47.04709 | 2025-10-25 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9715d4be-1858-3cc4-aaad-cbbac2f49b7a | -2.89193 | -48.06427 | 2025-10-25 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c78c520a-c521-3ee3-9fd8-5a4a43727072 | -9.62649 | -40.33836 | 2025-10-25 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba0d3a67-37d1-3067-91b0-cd1a2d53a6ab | -5.70497 | -49.31192 | 2025-10-25 03:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0fefadad-ff8b-35ae-9877-726f1c823991 | -3.9171 | -47.69159 | 2025-10-25 03:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 02516b28-9348-3cbb-9d70-e5ea5b5bfdfe | -4.2229 | -48.61954 | 2025-10-25 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8eb7acf-9169-3b79-acca-194d83f02392 | -6.245 | -46.39746 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5954affa-f78e-30f1-afb3-649a661d84ea | -6.23906 | -46.40219 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e33eebe-b185-337d-a912-390c167a002f | -6.54848 | -41.57796 | 2025-10-25 03:57:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 89d1bfe1-d4b6-3e0c-b15c-1bf5353d6850 | -5.45197 | -37.6358 | 2025-10-25 03:57:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 64508afd-7046-3cc6-a146-ce609883223e | -5.45151 | -45.41055 | 2025-10-25 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8ae69b2-bc7c-3626-91b1-a5e689e5bf4c | -7.0043 | -43.46989 | 2025-10-25 03:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e54cf893-bd1f-3215-8717-52eb9313e4f8 | -7.04797 | -37.96447 | 2025-10-25 03:57:00 | NPP-375D | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2dcb1669-7c33-35cf-a37a-15b42d33e487 | -7.55842 | -47.11951 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7ca9f0b0-1775-341f-b973-5c875f275e46 | -6.81603 | -45.44149 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3cd2febe-fecc-308b-a1e2-a2f662e45ccb | -6.06443 | -38.15186 | 2025-10-25 03:57:00 | NPP-375D | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0ad4dde7-b5a4-3b5c-841a-743e7826fe01 | -6.31702 | -41.85377 | 2025-10-25 03:57:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b4c21f0d-8b14-322b-869a-958f5606f431 | -8.5696 | -48.51353 | 2025-10-25 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78a540ae-aafe-35b5-842c-4009941c1eac | -7.55948 | -47.11351 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e970ee6-6e68-3873-b89b-d8b1d193a582 | -7.82595 | -40.25586 | 2025-10-25 03:57:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aaabe2f4-aa45-3bf6-a935-d5866798e6ec | -6.66627 | -47.50822 | 2025-10-25 03:57:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4b57a11-e987-3b4a-bc64-2cf018f5cd99 | -6.67158 | -47.50911 | 2025-10-25 03:57:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42d0a532-8774-35ff-84ea-e4d74f3bf45c | -6.71353 | -44.63351 | 2025-10-25 03:57:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4840d89d-bb9e-3472-823f-280bd7869d5b | -4.55894 | -46.6871 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfa0faa1-761d-381b-b872-e40d1df3a9e7 | -8.5641 | -48.51263 | 2025-10-25 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ced78df4-cb36-39ef-8230-aa64662a5430 | -3.10048 | -50.20342 | 2025-10-25 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a17fb6b9-7e01-3db2-8362-68b301741064 | -6.96355 | -42.53236 | 2025-10-25 03:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a7065ba0-dd54-37c2-9172-102431a8f43a | -3.82734 | -50.19785 | 2025-10-25 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 02dd2c74-65b7-3225-b79b-f3952f05e010 | -7.84706 | -40.90158 | 2025-10-25 03:57:00 | NPP-375D | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0747c719-1347-33ff-9305-079d461d8ba7 | -7.58441 | -43.58413 | 2025-10-25 03:57:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0069769-2b51-3c44-93e7-51674f49642a | -6.91815 | -45.17376 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abef7a43-0149-3544-aff1-cf0739b9148e | -6.9669 | -43.49551 | 2025-10-25 03:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9584ffd2-08b8-3583-9694-51f78aaa4820 | -5.89383 | -41.28846 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc566fdb-0128-3d20-ac0e-b6b1ebad6cf9 | -7.77759 | -42.91515 | 2025-10-25 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e9912c1-92b5-3006-94e5-6556f5e6e0ff | -6.23 | -41.84156 | 2025-10-25 03:57:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c82e6136-987b-3fdc-b7e9-0e714c90cc2c | -6.8912 | -46.37042 | 2025-10-25 03:57:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 263221f8-9875-3a38-b735-e4ef24946455 | -7.15547 | -40.44767 | 2025-10-25 03:57:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8d9b1fdb-54df-3f16-ba28-c8e6655fdecd | -6.8193 | -45.44552 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 16d28522-569a-3343-acfb-9fceb9911590 | -3.83392 | -50.19897 | 2025-10-25 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d49122c6-da97-390b-a9f2-44cafb02f08e | -3.98606 | -50.52627 | 2025-10-25 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c6728d7-444b-3a4c-a026-76192b8ece36 | -3.86486 | -51.89967 | 2025-10-25 03:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9c75b8c-6c58-3a7c-ba68-8511c4547e5a | -5.60865 | -41.12187 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0a37af83-7779-3558-b166-15f5388bbd83 | -5.80358 | -35.58263 | 2025-10-25 03:57:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c1fea1f4-2992-38c6-982c-0951a05188df | -6.16089 | -47.08693 | 2025-10-25 03:57:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 531690f5-3fc6-3540-9e2d-c1994e48e1f1 | -4.55379 | -46.68594 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eb608e14-8b03-38cd-893e-301f9af2af88 | -6.43346 | -42.02226 | 2025-10-25 03:57:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dca4e010-0d95-3f27-a15a-9a29905c8cf5 | -6.90998 | -45.16734 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 490df728-c130-3475-b410-4cf86c9945cb | -5.82218 | -40.81051 | 2025-10-25 03:57:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eeb71256-3fe3-3438-bd9d-f8b4b92432f5 | -2.86883 | -50.71808 | 2025-10-25 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4811027e-756c-3d2a-bcac-5320c3cef671 | -6.16035 | -47.09003 | 2025-10-25 03:57:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fc03b1f-e2f2-367b-915e-2bf66c243b7a | -4.27346 | -40.70066 | 2025-10-25 03:57:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fef1bfc2-b416-34fa-8a63-e9cfaffd9b90 | -5.83933 | -40.7938 | 2025-10-25 03:57:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d92c4ced-4e7d-381c-92c1-fab415b4c2ea | -6.6444 | -43.60613 | 2025-10-25 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89331ad7-0256-3240-8cb1-b7b4dc943def | -6.64847 | -43.60683 | 2025-10-25 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92c81f9b-7406-3db7-9acb-0543e6571107 | -6.13757 | -42.46094 | 2025-10-25 03:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README14.md)
