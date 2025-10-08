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
| 35d701dd-5188-3f2b-95d1-3537f36b87ee | -7.91507 | -47.14061 | 2025-10-08 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41b451f4-6c5c-3c43-ab8d-91844a5db3ed | -16.18717 | -43.66611 | 2025-10-08 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80bceda2-531d-3f80-8d04-04b61a4226fa | -18.05862 | -44.47355 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75aecb94-7351-3406-964a-a8583ee73735 | -18.50897 | -43.89911 | 2025-10-08 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c830a77-d695-3ac6-9df7-f9d7de2f0ad1 | -8.26952 | -47.00569 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f63849e-c42b-3e81-922b-fcc220434f60 | -13.80457 | -45.79337 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef523d7b-dbc6-3222-a07b-1e644b0feb88 | -16.0099 | -51.05592 | 2025-10-08 04:19:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41fd733a-565a-32de-a30c-d1cfb9afd8c6 | -15.79198 | -43.65549 | 2025-10-08 04:19:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1377537e-d8fd-38c0-9175-ce28c2c9c137 | -14.70685 | -46.08992 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e25586c5-a91c-36d0-a988-bf96e6ae4aee | -20.26954 | -43.26236 | 2025-10-08 04:19:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0bd78e8a-9045-30e7-9b49-8082f1a9f713 | -16.6663 | -43.93478 | 2025-10-08 04:19:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fc299b4-b1e1-310e-878c-24165056d2b5 | -7.82342 | -44.14525 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 581cae28-4870-349c-9e33-88e64a45b349 | -17.96806 | -44.97747 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7c99462-b8f9-3e99-aa4a-fb5edb02da45 | -15.26468 | -46.33089 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e77977f-c348-342e-8153-83c9e8a4241f | -15.76719 | -46.25075 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4bd131d-caf6-33da-812a-492f19839f71 | -14.89536 | -48.09037 | 2025-10-08 04:19:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a97648c-cd41-39c0-84db-bfe270efc78c | -8.19736 | -44.11495 | 2025-10-08 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c213380-ed04-32d2-a1ec-ce19c3e5a4de | -20.38083 | -44.44767 | 2025-10-08 04:19:00 | NPP-375D | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| efc030dc-f4e0-3a8a-9cd0-85cc293d6ca9 | -8.22593 | -44.16618 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 80128c39-31bf-3e22-be5e-2910356873b1 | -15.38556 | -48.02834 | 2025-10-08 04:19:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1a598a9-d5f3-321c-9d43-fd3ec9c5b2bd | -17.26988 | -42.65258 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 150bfd4a-6cf6-35b4-b1eb-1ba56a3443f1 | -17.97628 | -57.51141 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3698c5a9-afb0-30a6-8158-e046f6ebd7b4 | -8.33442 | -46.22882 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee090bc5-4f4c-3329-888b-73765cab9075 | -19.42794 | -49.58281 | 2025-10-08 04:19:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44f90941-f8bf-3f33-a814-2b5e9a80a021 | -8.26838 | -47.00344 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebbf08fd-0290-3d6c-8f80-756877e8c358 | -16.00524 | -50.82055 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18b4acf1-1fbf-35e3-b669-ca29591b82ce | -8.54312 | -46.23229 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1733325f-4920-3e47-92a3-301254457a3b | -17.15147 | -43.43706 | 2025-10-08 04:19:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5fc30a52-f111-3612-8d6c-8121273c45c5 | -9.09303 | -47.96181 | 2025-10-08 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 083fc990-d674-31fb-8a72-0f937e9b921b | -8.67628 | -43.9083 | 2025-10-08 04:19:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26f9c106-93d7-35bc-86e1-9b304a578a0b | -13.7894 | -45.80192 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 660ca95d-4c2d-35ae-96a9-03b580d0f329 | -9.17882 | -46.92146 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 154f0d50-c443-32d4-9943-e40c73e9b0d0 | -8.37655 | -47.05735 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 63bbe18a-3b2c-3e95-bd8f-55a23d57fdfd | -18.00101 | -44.98674 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb1c2d27-cfcf-3334-a3a2-80e0d6534c02 | -13.84381 | -51.85753 | 2025-10-08 04:19:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e5c1de7f-bda7-3e66-a893-347e289af0a3 | -9.19118 | -47.8114 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fa75fda-c989-3be4-bb54-261843f9eef4 | -15.49631 | -47.92879 | 2025-10-08 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| feb99377-9e79-3195-bde6-3cc2192fe152 | -15.38567 | -47.30605 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef4fe9d5-927d-3500-8821-25d353deef8e | -18.05846 | -57.53975 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 13e8bd7b-261d-30c3-8adf-4332d11da3e9 | -20.1882 | -43.93646 | 2025-10-08 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 60902daf-262f-3914-b6a8-aeb867fc54df | -18.29462 | -45.46352 | 2025-10-08 04:19:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8821cef8-ff6c-3d42-b554-cc44d26dd2e5 | -7.78934 | -44.22982 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddf0184c-605f-3b0c-8d32-ad349a2ba4f5 | -14.7927 | -46.07095 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7360c5e-8bed-325f-92e0-6b0e435e3d1f | -18.07386 | -44.46455 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 967c5d64-148a-36bc-81d1-a72dd6fa4db1 | -20.00413 | -45.29282 | 2025-10-08 04:19:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dea779d7-fbc0-308b-9813-67d39f4bae62 | -17.98147 | -44.97966 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 62778b64-1a53-3851-8253-42071c369047 | -14.38829 | -46.02143 | 2025-10-08 04:19:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed5aeb88-2fa2-348e-9845-cc404111a062 | -14.45008 | -48.79507 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c2b72aa-63e7-31fa-b812-f75510bf7ab8 | -14.71912 | -46.03591 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2cb4814-296b-3cc5-8dcb-50585297bcee | -17.93002 | -57.51892 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| de86b0bb-0fb6-315c-8b66-4fcf4b6a6000 | -9.18813 | -46.91028 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbfbf1b0-c756-365a-bd11-5b61ff1f8ad3 | -8.67548 | -47.07659 | 2025-10-08 04:19:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 120e0e13-0691-3c1b-add3-9da8a973b963 | -13.31416 | -48.02596 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4ba8840-4c3c-3d77-b3c8-27330ef6c2e9 | -14.10232 | -44.30658 | 2025-10-08 04:19:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0eb79ef-266b-389e-879c-8886162c7aa8 | -18.04267 | -57.5254 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 78b75ac4-f1d4-39e3-8c5b-b3ba8feab9ae | -7.76376 | -44.19693 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6c797aa-0978-36f3-843d-60fdae93d953 | -14.71199 | -46.07957 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2fbf0a2-dd09-3606-99eb-db2002611ec0 | -19.7187 | -43.90568 | 2025-10-08 04:19:00 | NPP-375D | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91753722-7bb8-388f-9ff6-c34d59d54cd8 | -20.09892 | -44.20952 | 2025-10-08 04:19:00 | NPP-375D | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 220aa08d-448f-3795-b4eb-bb57f2dc7f73 | -17.93078 | -57.51545 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 992a2fc3-fe38-3ad7-a7f1-950b0481c695 | -15.2492 | -46.36211 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7201f0ee-094e-343e-a42d-08e20bebc817 | -13.4691 | -47.71536 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12fc2fe7-6f45-365b-bed7-810b910e7b3e | -14.9333 | -46.7938 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9d8f6b6-a7b6-36b3-943a-da1f6360113d | -17.65491 | -42.34609 | 2025-10-08 04:19:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9da22a2-1e67-3364-9d8b-2e88b45f7785 | -19.98341 | -44.23667 | 2025-10-08 04:19:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fcb55a9d-d951-37d0-91fb-d6d9c50e94b6 | -8.4715 | -46.29537 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7d5349ab-a8d3-393b-8035-2364c08820ca | -13.73888 | -45.71947 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb5dd495-5e82-3e4c-a0aa-d7723be1c803 | -18.29802 | -45.44163 | 2025-10-08 04:19:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b7f090d3-d8b0-38e8-9b71-6a3cc5968b8c | -14.52474 | -46.64385 | 2025-10-08 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2d5def3-4923-3c70-8e72-024a6bc7554a | -19.30776 | -43.76572 | 2025-10-08 04:19:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 04fc308c-8061-3373-b822-a0dd58e3f0a8 | -7.7816 | -44.19257 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8173aa47-6b30-3a3a-b6bd-6922fbfa8d3e | -7.78716 | -44.20062 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c3478ab-3df4-32f7-a8ac-b07e8d64e765 | -18.51004 | -42.09937 | 2025-10-08 04:19:00 | NPP-375D | MARILAC | MINAS GERAIS | Brasil | 3140100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5f03e350-e7d2-3382-ac16-a4baa7250ee5 | -17.95143 | -57.5078 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7a8f4e5c-76d9-32f8-bbb4-fbcda6d0346f | -8.92513 | -46.58523 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 12a10982-6099-37a5-9494-00c588c82d95 | -15.76101 | -48.71188 | 2025-10-08 04:19:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f63b4e14-a9a5-3000-93c5-04c311c74a51 | -17.95831 | -57.50522 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6ee5c084-ebb9-32a6-8968-388d1b596c5e | -18.05352 | -57.53775 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 5b727306-3f16-328b-8c9c-c5fe8cb64454 | -16.32747 | -47.07116 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc6d2fc5-293d-3718-8bc4-c330683e95c5 | -8.89333 | -46.03508 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 586ed2cb-bd92-3237-b904-d9f2e92e45a8 | -16.6209 | -45.42665 | 2025-10-08 04:19:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcfdd905-ab37-3ee4-88e9-c91fe091add4 | -8.23092 | -44.17778 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91488705-deee-38b0-a729-5d061944f2c2 | -19.44779 | -44.19033 | 2025-10-08 04:19:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f537b5e7-4be4-3ac5-81d8-1672f57963f6 | -18.01624 | -44.29379 | 2025-10-08 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88406c91-2133-3282-8f99-2e4684d88b05 | -21.07029 | -46.88734 | 2025-10-08 04:19:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9d413e1-203b-3f81-b426-595931d835a8 | -15.7952 | -46.24802 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22305945-6a46-36a9-825f-517c647b91bb | -15.38271 | -48.00241 | 2025-10-08 04:19:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f06eaafc-4777-374b-9a12-8b52c67c108e | -17.2981 | -58.06544 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ce1f1a10-b7db-37cf-9dfe-2bd8316f61de | -8.86339 | -46.77791 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 849bfc23-a587-3012-b02b-63f15bbeb675 | -18.41804 | -45.21008 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99597d3b-8ccd-364f-9872-496a0428cfd6 | -17.28719 | -42.65975 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9bf8d313-c401-3986-8f92-d4c5ee5c4b1a | -18.40954 | -45.20847 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3eb2b3dd-3395-3eef-8f54-d6f3e3e8140c | -14.90732 | -46.82507 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed789e82-a2cc-3912-8257-2a13f9997ee9 | -15.79578 | -46.24445 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f587fadb-c29b-383f-9a8a-baced98385ff | -14.74485 | -47.86428 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9f3e69a-5ea4-3466-8a1c-7e2305792251 | -8.1544 | -54.84518 | 2025-10-08 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a3cf362-ab60-3c6c-8905-b87cb381ebbf | -16.33742 | -47.05342 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa901520-1cb3-3fef-91d7-83b24d4e903d | -15.19213 | -43.73159 | 2025-10-08 04:19:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| caf396d1-6f31-3372-b55b-dcfcec929c57 | -18.30357 | -42.2289 | 2025-10-08 04:19:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f9b4b39e-7370-3744-acba-45878a66c9e8 | -20.4971 | -45.94804 | 2025-10-08 04:19:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README51.md)
