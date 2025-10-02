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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac31f96f-fd50-30be-90d7-9abd58df9a55 | -14.48274 | -48.41508 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f9189805-b91b-3643-b572-4c1505aaf19a | -14.69346 | -48.2562 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc92e8d9-bde7-3c6d-b035-3039edaa29a4 | -16.02456 | -50.91751 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 734ffd99-5400-3fce-a83d-bf2f902a26e5 | -14.40757 | -46.10264 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a20ca78-6ff0-3dc3-9c2c-a66d65167eb6 | -13.3235 | -47.22873 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98c7d25f-6255-3dea-a063-86e7217b2602 | -14.42068 | -46.1399 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 54ca569c-234a-34c2-9102-5e8caf25366e | -13.85982 | -51.24709 | 2025-10-02 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78ea9ae5-2ff0-3a80-ab02-226bb86c94f1 | -18.97029 | -47.87211 | 2025-10-02 04:04:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10e562e8-0ac5-32cc-906f-42f30f63ef4f | -15.18646 | -46.41237 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa2df36f-b857-3377-8513-6df496d25829 | -19.28937 | -43.74843 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e20cfdc6-2d77-387a-80db-76714724e787 | -14.41853 | -46.08464 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5cd79053-37a1-39f8-bbbc-a108f298fb68 | -13.95813 | -48.1073 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9380ac68-3db3-3fb7-af91-3591590eb521 | -13.31166 | -47.58537 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 248b0c46-74b9-3497-99ec-48aeef4ce4fc | -14.42701 | -46.12601 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06d9578f-8356-3116-bcb0-37e2cd4e7fae | -13.17671 | -47.80707 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5e385497-736a-3bcb-ae93-e49310d42e80 | -13.16815 | -47.83012 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d28bb650-d64f-31f2-b0d8-56a6fa2b9cf1 | -20.13415 | -46.35162 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87df6ac0-83b5-3105-a577-7ef3fa91f732 | -20.11946 | -44.3831 | 2025-10-02 04:04:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6ff1f6ad-fd34-3fa6-a3da-f1ed06e3a79b | -20.41381 | -43.3551 | 2025-10-02 04:04:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 69ffaf9b-4bd4-3394-a271-a5a62880d9aa | -15.40483 | -47.04121 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c554db6-86da-3810-8f13-b5d1a3d2d945 | -17.95573 | -45.03386 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f341a13b-1f37-3756-b799-faf9a024d0f5 | -14.3158 | -46.00402 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 743b2ae3-2ec4-3592-9266-874b67f55efa | -15.1883 | -46.40208 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4acedacb-d4fd-323b-b048-b8a1269942c0 | -19.89419 | -42.62725 | 2025-10-02 04:04:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 6a0c3ddb-ac3d-32dc-a4c9-f282090163e5 | -15.25053 | -47.90567 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85cdeec8-75a9-31e1-a17d-cf47ac403d70 | -13.28447 | -47.25516 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4496f15-96f1-324d-b512-57628b5b088f | -16.00044 | -50.90752 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a31a267b-ad19-3e84-9b40-fb47a2c729fe | -13.18011 | -47.78789 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87fc9337-305a-3cf5-9768-26af7c04cdd8 | -13.7745 | -48.04971 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d2ff59d-5b91-3937-9241-b57e4364212f | -15.94714 | -43.33385 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 631ed939-716e-3d42-accd-59a4ef2204b5 | -13.29357 | -47.25227 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a714bf10-991d-3286-8cae-8b6b5c9449f1 | -14.69324 | -49.61901 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5808c07-752e-3287-92cb-a90edf201b65 | -13.82765 | -43.06796 | 2025-10-02 04:04:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6df281f8-344c-3fea-82a6-ae2110f32a53 | -13.8118 | -47.54306 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8387163d-39d1-33cf-ae5a-aa89c51003e2 | -12.90625 | -47.17209 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13ac862c-020a-3527-8602-f4fd5328f5b6 | -16.02338 | -50.92347 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f84cfd6-d6ac-3b5a-8594-003ffb7da852 | -13.75879 | -47.95605 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32301111-884e-3af2-b019-712dd190ba89 | -15.14546 | -48.02475 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccf6ca4b-f508-3b02-83c4-39dec2bfb709 | -16.02901 | -50.92139 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e27ba4ba-8bae-3674-bb2f-afacb13e633d | -15.83956 | -46.245 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 788d5d9c-d410-317b-a607-b3c324246011 | -15.56173 | -48.18085 | 2025-10-02 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b79a242-77f8-3bc5-aee5-54df27079989 | -14.90221 | -48.33093 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cb41f55d-a855-3099-91cb-e3715793dc85 | -13.94215 | -48.09663 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f0fdd11-8daa-33c4-b0b3-0b1aa99dd6e6 | -13.40545 | -47.78448 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6795cbc7-af38-3c55-bdd8-288e675bb5fa | -17.5167 | -43.48407 | 2025-10-02 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b00e897-33a5-30b7-bcc7-86ad28e6f6c0 | -17.66593 | -48.15188 | 2025-10-02 04:04:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 929bf37f-58ee-3d58-a2c5-f23931789de5 | -14.47182 | -48.42555 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 80f19bd9-8020-337f-97a3-a3015685b269 | -15.25899 | -49.29352 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8ffe4d27-8113-36a8-bc23-1d1ba0b27db3 | -15.35325 | -47.08516 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| febd3541-449e-3d37-905f-7bb3748165c9 | -14.36508 | -45.96732 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f86afbb5-2ff6-3c62-ad4e-b90fb2a50334 | -14.22337 | -44.9295 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10a76943-99ca-3898-af85-c7e21f0f1286 | -13.78778 | -48.05067 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 409c845d-d10e-3129-845b-efb11c72f6c0 | -16.37573 | -47.01684 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50719113-3939-3a66-b948-392910e657ab | -20.12856 | -44.01423 | 2025-10-02 04:04:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e89154b3-2d05-3bfa-936c-8c5f481c434b | -13.80779 | -47.51748 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da48a869-c684-392d-8cfc-08f03a467223 | -12.76378 | -50.55164 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c4ce574f-3291-3651-85fa-781d56a63ac0 | -19.44433 | -44.15967 | 2025-10-02 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a6ed08b-d399-3b77-9b0c-781a020c0089 | -13.7603 | -47.94775 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1251f3ae-25ea-3114-a74e-c86e3b39e60a | -14.33125 | -45.98233 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00111a2c-da1c-3dd2-9295-8ceabe867001 | -14.64744 | -48.26316 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3818d0b1-fa7e-3b2c-876b-289d535fa437 | -14.79588 | -42.82882 | 2025-10-02 04:04:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74d80c98-f57b-3f96-a817-3bc572316142 | -13.16722 | -47.81035 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e795b1b2-cde4-384f-ac98-4f239076a7f0 | -14.42865 | -46.11651 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1458d6c2-c59a-3a1f-b8d5-c5b28d347e07 | -17.70244 | -46.88728 | 2025-10-02 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6936988-dd0b-36ac-9e3e-262435157d6f | -15.26314 | -46.40207 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2633a1a0-fd08-3b3a-9414-bf2e31ca0b5b | -14.36797 | -45.94967 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 26913558-e7a9-36d1-b0ab-a290ba8b2172 | -13.79724 | -48.04798 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9775c8ed-a50b-3330-91cc-168b82b9c02e | -14.28525 | -45.9782 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34016e7d-e7bd-3ec2-a321-d4f6d7488869 | -13.75211 | -47.99282 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0e009fe-a457-38f6-ac4b-478e17d7a033 | -15.83501 | -46.24891 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c61bfb3c-13e0-3c1a-87cb-19e92ddee376 | -16.36928 | -47.05224 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac739217-5cfd-3ab1-a781-314c0064c223 | -15.33861 | -46.25903 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3467f51c-1d00-39e6-97dc-94240852d371 | -14.64671 | -48.14745 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b0e0ee6-1a16-3197-abcc-f2e0e3f9270e | -15.7529 | -43.68706 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 329fa493-9e22-391c-a252-e00349e0ab73 | -13.47002 | -47.23396 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cee45d51-33df-389d-8c21-c7d24ca1d700 | -13.17236 | -47.80648 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3f2cc144-4e1c-3b56-8a7b-32c22aa470c9 | -17.70314 | -46.8849 | 2025-10-02 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ed5edc4-d254-3709-bce1-8d27c0a89f1b | -15.99921 | -50.9137 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d036b570-5b38-3348-bc86-3535f4547675 | -14.81826 | -51.40245 | 2025-10-02 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1e822931-506d-3677-b239-f7e5b18e072a | -14.40674 | -46.10741 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92b3d509-49aa-3257-a767-58cb8d26724d | -17.2615 | -40.30532 | 2025-10-02 04:04:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3b88eceb-313e-3921-9a51-4ec8a9ce986f | -13.24707 | -47.33527 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 918f1078-bc1c-35e1-831c-d0fc12707a58 | -14.86631 | -48.28318 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa8b87d1-8a2f-3d1e-b709-baf2a3443a98 | -13.77661 | -48.05524 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2110890b-6070-309b-a149-a7d8f8cf8332 | -14.89746 | -47.21965 | 2025-10-02 04:04:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af1f1f2e-960c-330e-83ce-50bc7c6e325a | -13.3156 | -47.85004 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b91a4bca-5161-35ee-b2ca-1ace0968e351 | -15.25398 | -47.91041 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3fcb9fa7-1939-3aed-b374-3452cc4549a5 | -16.76757 | -44.94089 | 2025-10-02 04:04:00 | NOAA-21 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fa4089f-d1c8-3550-bc56-a68fad30add1 | -13.94282 | -48.09298 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76b8a801-615d-3179-95e7-5f74856647cb | -14.41669 | -47.14296 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90cc5f8f-cca4-3bf2-89a3-3e98efaefc08 | -12.76626 | -50.59214 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7785faaa-2d06-36ed-b96e-fc1104557499 | -14.64246 | -48.13348 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f9f3da2-4ed6-3604-8242-2bd06f742c15 | -13.67865 | -48.05134 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| edff3ab2-744d-3b2d-9c0a-d4ed04009b76 | -12.49856 | -50.25624 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e5369ee3-dc40-3a29-b23f-e3a0180b673e | -13.06475 | -47.06153 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3bfc769-0a48-3955-924f-7a60df3e3424 | -15.30712 | -46.3924 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 884d6e50-a562-3791-9345-428d10629bff | -12.58697 | -49.89185 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72a4a0df-7ace-3b88-baee-e5f4e4e8fbdb | -12.9021 | -47.17128 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5eeff07-c200-37f5-8ab8-dc8723dd15ba | -13.96881 | -44.8702 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b37d182-8e42-36ed-9317-a3237b62a1df | -12.76564 | -50.59542 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
