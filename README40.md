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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afefff42-6265-3c96-acff-ecf7938dc148 | -3.1987 | -53.4078 | 2026-09-27 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 288ae6d9-a0b3-3cab-a933-b362052cc30b | -4.18341 | -49.4112 | 2026-09-27 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a07a0c1-7d48-36a2-8428-8a6fc6d934c5 | -3.82868 | -55.91202 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bd03f247-7b42-3ecf-af95-eff26483cdfc | -3.9659 | -50.71251 | 2026-09-27 05:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0968f5f6-3056-31ab-968b-d16829e50006 | -4.98091 | -56.15147 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44e880ea-27b0-3098-94a1-9b9dd2cf7df6 | -4.52033 | -54.97762 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8262dd5-6770-3fab-b208-f20972826b52 | -3.71228 | -54.65002 | 2026-09-27 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7a755be-076c-3501-b63a-3ff8007965af | -3.85232 | -52.00935 | 2026-09-27 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6081186b-473c-3185-8b2f-07a9ffdcaed6 | -3.76414 | -55.95744 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55814eb7-b2b7-3e1a-81b7-530bfc97dc6f | -6.05596 | -53.603 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52d051ae-b6ef-3ffd-96a4-2c957d437d57 | -4.44752 | -55.03265 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 879db810-a63a-3ba0-a796-a3b8f5c509cc | -1.11998 | -57.27294 | 2026-09-27 05:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 711c4435-91ea-3a37-9a43-010efd85a6b2 | -2.9307 | -45.50743 | 2026-09-27 05:27:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32ac4b5f-403d-325c-991d-a7f3766b310b | -4.50593 | -54.94855 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de87aeef-57d1-34ba-a7da-fcb5c7c255c3 | -2.914 | -59.13654 | 2026-09-27 05:27:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ba3328d-729b-3aa0-a670-95f4034070a6 | -4.49482 | -54.94678 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 9dfe27c7-1420-3f69-8359-59fe5f419e68 | -3.89126 | -51.96265 | 2026-09-27 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3c8e473-bfed-3a10-8a5d-a8aa767ac668 | -2.67124 | -56.45574 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f954494-fcb5-3d13-8d1d-68467a4ddaeb | -2.97986 | -54.14875 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed6b0eb9-ed67-3036-aabd-1124f480d68b | -4.51727 | -54.98379 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2848cc9a-6023-3b6d-9d5c-568c3eaf269e | -4.5829 | -54.92639 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c361bb66-425d-359f-b3c6-0867c4414fc7 | -5.68032 | -50.09389 | 2026-09-27 05:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88d519c9-b334-3b26-b236-f71df423f954 | -3.0054 | -54.20918 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa6040e0-9166-3862-9d62-3c894f3ffee1 | -2.05752 | -56.86759 | 2026-09-27 05:27:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bc54b3ed-57f2-3ec6-b849-fffce299fec5 | -2.93189 | -56.57356 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bef8f84f-9be6-3330-ba40-9d665148025c | -1.8364 | -54.72078 | 2026-09-27 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 96ca594e-3209-301a-98bf-9afb012a8e74 | -4.69573 | -55.94515 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 995286fb-19c8-3d37-a842-8670b6eb4d2c | -3.96993 | -50.7186 | 2026-09-27 05:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b48ddb1b-9216-39ff-9c03-b58feb0fb466 | -2.88677 | -49.47973 | 2026-09-27 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf8f0400-42db-3e71-a763-d25ce5bc0ee5 | -1.14175 | -54.09126 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 742369b8-3a78-38f7-9f27-3195aacc3a20 | -3.83282 | -55.91179 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8b74d2de-2c70-3fc9-8c0f-7c676f29ec23 | -1.34173 | -55.47742 | 2026-09-27 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84502365-832e-3236-a901-aff20b84f4dd | -4.54594 | -55.53428 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5e61ca5-2728-3e34-ac30-d62d655f005d | -3.94863 | -53.85243 | 2026-09-27 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e8a0733-8981-355b-8e55-af003ea02ab8 | -3.51139 | -50.31454 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b70a9ca7-e5d5-3413-b684-46a7a38ced23 | -6.12885 | -53.048 | 2026-09-27 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abd0fdad-2776-32bf-bed0-a5d2736332ff | -3.42473 | -50.41942 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e78393f-7052-3982-a61d-35efa845b843 | -6.0477 | -53.60202 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a65dacbb-dee3-3aef-ad2d-05d25ac14847 | -1.84433 | -54.71772 | 2026-09-27 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c9b421e-06e0-3fd8-add6-c4283794edaf | -1.74633 | -55.24257 | 2026-09-27 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23be9d87-916e-3c04-8019-8a02cc92c4fb | -6.05486 | -53.61041 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99c242d8-4762-3715-af15-170522a01f80 | -1.2257 | -54.12091 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 410b9848-fc64-3dee-b02f-1ca4faeba451 | -2.05821 | -56.87165 | 2026-09-27 05:27:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbf0a652-c4d7-37a0-8bb4-873a616eac08 | -3.84821 | -55.81125 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1ca5d4f-e246-36aa-88bf-4970180351fe | -4.50291 | -54.94356 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e8d65a3f-7916-3f0f-ba68-ec354303aefa | -4.14752 | -48.22137 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c210ea77-c50c-35c2-a010-028a3a4c3e2f | -5.73996 | -45.06099 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f12997b0-a917-3315-9ae0-17693cc13692 | -3.055 | -50.3379 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35c532a7-7a24-3969-8a52-44b00c1722a7 | -4.36115 | -55.27992 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdf5b8e1-a1a9-39d9-a83d-5bece3bc73c6 | -4.98152 | -56.14746 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2c8902c-67b5-3745-8925-3ff85534620b | -5.73652 | -45.03202 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2e7d75d9-a786-371d-858c-e8c97e88048f | -4.97385 | -56.15054 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d152f346-aa16-3bb2-b969-51339dacb32d | -4.47958 | -55.42861 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bdb18c4-08b2-34e3-b0eb-76c90d2add5a | -1.84367 | -54.72189 | 2026-09-27 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad42138b-6f1f-3bfe-bebb-3faf2696c6e1 | -3.96204 | -48.11439 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc04dda2-06b2-3b36-8057-043028e4a2e9 | -4.28528 | -48.56158 | 2026-09-27 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f60121a2-be5b-36f5-b821-a895803bbfea | -4.14646 | -48.22289 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a19f5dd9-d9ff-36da-9dff-8e17c3b9509b | -3.3606 | -50.46429 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa652423-14ff-38fe-b70f-e090657d9e66 | -2.94407 | -57.7151 | 2026-09-27 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9992348f-0e67-3581-b612-100898e743d6 | -6.07376 | -57.81223 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f247983a-d0c0-3c75-94a6-791dff33a110 | -2.37936 | -50.41018 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 442c2665-efa6-35ab-bd50-1f9a8044cd02 | -6.06091 | -57.82835 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c71c181-d5d4-3660-805a-6fd1f9960ae2 | -1.04447 | -53.56246 | 2026-09-27 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8df0c67a-b78c-3727-a52d-e48abf8043c5 | -6.07431 | -57.80869 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3287c584-8daf-3494-8595-29be8e81e081 | -5.47733 | -48.58254 | 2026-09-27 05:27:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19b75182-0c8f-3c0d-b645-1d6856d5ec6c | -3.51136 | -50.31703 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da63ece3-b085-36eb-8a41-841b572be22c | -6.05129 | -53.60617 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 548a6253-d663-390b-a60a-f68a4ae462fb | -5.73748 | -45.02481 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20ca18f1-0c21-34fa-92b8-a495ab1c1616 | -2.92455 | -57.66585 | 2026-09-27 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69e56f62-c102-3538-a3a0-a3c4f24efc75 | -3.95568 | -48.11742 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d44f3cf-040c-38c6-a35f-d78a6a162ee1 | -2.44344 | -49.22693 | 2026-09-27 05:27:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7de4544-e2af-3c10-bf50-e1789ff6a9ab | -3.06392 | -50.33701 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61be1f00-c661-35a7-937a-49df784cfa5a | -5.16505 | -56.00949 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c6bb124-977c-3cfd-8cc5-78e3142f5a82 | -3.86906 | -52.28211 | 2026-09-27 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 768cf12d-7def-3dc1-87ed-6e082b42a7dd | -4.28671 | -55.25303 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07f9b265-dc8e-37ce-b295-93acd4f73d6f | -2.54778 | -56.28727 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e67cd098-decb-3d5b-8faf-dd9acff5d17d | -4.56396 | -54.95081 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b65cd9c-f2e3-3965-aec4-41e39804991d | -4.25594 | -51.04862 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c28999e-24a0-3dbb-acad-69f2d90f8815 | -6.07095 | -57.80815 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15ce688c-be6a-3a6d-ae7c-b387bc628994 | -3.22501 | -54.33348 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed2242f7-d375-3d00-b3af-69c36e450d0f | -4.98083 | -56.15191 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed5369d5-2b05-3c7c-91d4-6e8ba6a9ab6c | -6.06984 | -57.81523 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b331d2d-ce47-3e26-a726-33b7b25730a1 | -6.06649 | -57.8147 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2e2840a-110d-39ee-87d6-f6d5b9a7c582 | -4.50353 | -54.98821 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b29b7899-d871-335f-b515-558b2bcfa4d1 | -1.72753 | -57.15057 | 2026-09-27 05:27:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bde8306-7208-3f77-b4fa-9fd52395ba8a | -3.69664 | -51.37124 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1d557067-6a61-36ea-8bbf-964e6722a867 | -3.8293 | -55.90813 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 73a5575d-6e44-31f8-bd19-8c81f51fafcb | -2.90843 | -54.116 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0386628-2592-3382-aa3d-9d25e122f0eb | -2.05627 | -54.48264 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd0852ca-5b9d-3ee9-bdf7-358a7c16aa56 | -4.28606 | -55.25725 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ed920b6-efd5-31a4-848c-5be8e3dd51cd | -3.83752 | -55.90458 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16a5b37c-2daf-36df-8521-65b4769f52b8 | -1.05856 | -53.58207 | 2026-09-27 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72d904e5-0294-3b03-ab07-8f02a35a99d5 | -4.2897 | -55.25779 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e09559a4-3769-3c35-b273-e454b0bf874c | -0.51595 | -49.13012 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c669dc55-5776-3824-8621-7262b6bdcd9c | -4.27087 | -55.25927 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc89217a-e4a3-3d21-83e4-8bdef82b0828 | -5.16624 | -56.00174 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c136e3c5-24b4-32b3-8a8a-107b1c12c111 | -3.0372 | -54.69408 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| da4b4797-2a31-33a9-aa84-08bc3af7e510 | -4.50661 | -54.94416 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecd233c5-724e-3760-a309-44380bc6aeb5 | -3.96408 | -50.71327 | 2026-09-27 05:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0134f818-4d2b-35cc-8971-8b983d0dd8bc | -4.26131 | -51.04811 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README41.md)
