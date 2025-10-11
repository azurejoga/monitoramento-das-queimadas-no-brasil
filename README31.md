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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5eb7d95-97b1-35a8-a90e-52d1f8edd34f | -18.00051 | -42.33376 | 2025-10-11 04:36:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| af16c9fb-e725-3019-8fa4-f004cba57450 | -18.07398 | -57.53575 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 42fbc7f5-7b99-3bcc-b6ac-152dcbd7cc47 | -18.07565 | -57.55124 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4937f2dc-5798-3b41-bf1e-0a5d9552bb8d | -19.73439 | -43.92666 | 2025-10-11 04:36:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb74872d-0cdd-3d6e-b40b-df4b88f2cc14 | -17.81927 | -57.62901 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1a6987cf-dc2f-35e7-9a3c-69ba364f837e | -18.38844 | -42.98392 | 2025-10-11 04:36:00 | NOAA-21 | MATERLÂNDIA | MINAS GERAIS | Brasil | 3140605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e1b4e270-257a-38fe-9453-00a927e4ef69 | -17.2641 | -46.89936 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 6f754e13-77db-3850-a154-a9640c00ded5 | -16.97711 | -44.43238 | 2025-10-11 04:36:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d337536-074a-35b6-a6d0-e21cf3bcb4bc | -15.21052 | -56.8629 | 2025-10-11 04:36:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd2de049-e1e5-3eed-9092-8799fae01e8f | -16.31141 | -47.16135 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39cd0a20-ad21-383c-85de-765eacc644bc | -17.82749 | -57.65923 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1a6d9c0d-78bb-362a-9898-121cdc4bd831 | -16.82115 | -46.72802 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05b58086-3d9f-3e36-9ad5-961f595baaef | -18.21956 | -42.37598 | 2025-10-11 04:36:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a5cbc87c-a373-328a-8e23-747ce0aaf4ec | -15.27638 | -56.90934 | 2025-10-11 04:36:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dfb75c5-87b8-34a0-84a3-3b186e9caf0a | -16.74281 | -43.97494 | 2025-10-11 04:36:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e90972e7-1611-34a0-aab6-a37513b18dd6 | -15.19689 | -56.86108 | 2025-10-11 04:36:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 104872df-adcc-304f-8c41-2d77f076fc86 | -16.87881 | -49.67297 | 2025-10-11 04:36:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 90b981ab-0f22-3fb8-9da9-7adfa839ac94 | -19.50524 | -57.47272 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5b2b9c01-33a0-36a4-b1a4-c9b5229539a7 | -17.37296 | -46.65358 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c24814a-cdb4-3e29-b822-714290df8f5e | -16.30671 | -47.14339 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4333f31-00ce-3458-8605-e5559eeb1066 | -17.21672 | -47.65281 | 2025-10-11 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f782a66c-1770-3b40-b5d8-c78e47313c91 | -15.18221 | -56.75442 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac62667e-3985-3407-8ca4-f8a92dafb9b3 | -17.59472 | -46.07643 | 2025-10-11 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc8a044b-44fb-3dc7-9f61-0de9fe3860f7 | -17.26046 | -46.89877 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 5706f956-6719-3658-a65d-5154d8e2c882 | -19.92085 | -54.35919 | 2025-10-11 04:36:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 302e22a7-7ad2-3660-8856-1ac5e475488b | -16.30667 | -47.16904 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 968ccfd4-7406-3dfd-819e-b044edd9a311 | -16.30252 | -47.17266 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 90bf8997-e504-3241-b3a9-41eaf8ae58a1 | -17.83731 | -57.65693 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2cd8974d-4f9d-3b51-9bb0-7deb3fa1039b | -17.5166 | -44.28405 | 2025-10-11 04:36:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d4c881f-c2ec-32be-ab76-4a001a4af6f3 | -16.53794 | -46.72501 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50f3986d-c594-3f64-a6a3-a9138f18f210 | -17.8919 | -57.67188 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e4bfd5c4-5d7a-32ac-9901-78e4d9f101ff | -22.86226 | -51.61619 | 2025-10-11 04:38:00 | NOAA-21 | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b7fda384-930a-32ed-a27f-3bfb88c7d8ba | -27.72628 | -51.2216 | 2025-10-11 04:38:00 | NOAA-21 | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 91df97d3-6e80-3903-bd77-d644e4637695 | -22.54899 | -52.05012 | 2025-10-11 04:38:00 | NOAA-21 | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| e8d9517c-14df-3b46-8719-d085303033e5 | -28.68628 | -50.91252 | 2025-10-11 04:38:00 | NOAA-21 | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ef2a8b1e-d3a1-30b4-b5be-8e98f5591586 | -22.85838 | -51.61932 | 2025-10-11 04:38:00 | NOAA-21 | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 33772c2b-2893-3749-aba4-a7c8a33ed852 | -22.54569 | -52.04951 | 2025-10-11 04:38:00 | NOAA-21 | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| e4ae55ff-7e9f-3ca1-a017-9a456c3dd6e0 | -22.5451 | -52.05324 | 2025-10-11 04:38:00 | NOAA-21 | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| c0ef16f9-2d6e-3ae8-bced-c17ebc8d9a69 | -22.85507 | -51.61872 | 2025-10-11 04:38:00 | NOAA-21 | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3da51c08-ac68-3a63-8638-5260b365ae90 | -23.09528 | -52.44564 | 2025-10-11 04:38:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 48e64908-7949-3b48-8ffc-5088ce38126a | -6.4421 | -45.8225 | 2025-10-11 04:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| a37cc413-38e9-3959-8a3a-a9a1dd4478ef | -10.0731 | -67.5478 | 2025-10-11 04:40:00 | GOES-19 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 38.6 |
| a3ca31d3-5d2e-31df-bb32-edee9ef541e9 | 1.20652 | -50.87136 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93146730-5ee6-3884-b988-12b56bf060cc | 1.20538 | -50.86407 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9c68b32-3108-3da2-835f-c40da6ea70b2 | 1.20778 | -50.87837 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1808fd62-a123-328b-8622-95d8661485f9 | 1.20944 | -50.86691 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f6c34ec-659f-375b-8e63-a378fa3356f8 | 1.20661 | -50.87109 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe8a4a16-b0af-3bbe-874e-dd1ff3beab06 | 1.19005 | -50.87771 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38d54f99-eb8f-3210-a6b6-e59969ecdc48 | 1.20486 | -50.86016 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08175b2d-4499-3f59-89e3-032a50188223 | 1.2072 | -50.87473 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c21f3925-aa50-3226-9557-a66786a95f5e | 1.20483 | -50.88284 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a020fdd4-ad34-3c26-ba07-5226144fd6b6 | 1.20709 | -50.87501 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee76d62e-094b-3eb7-902b-0daa0ac1c8a0 | 1.19856 | -50.86514 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd9fe8f9-5ba7-3882-83f7-641b17a61a76 | 1.19515 | -50.86568 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a1a1d66-9a3a-3458-a7a9-178c60b94fc8 | 1.19063 | -50.88135 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a4a70e9-11ae-34d5-94d9-596eb344dfc8 | 1.19346 | -50.87717 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 758a59af-9028-3389-b1be-44a275f8b85a | 1.19798 | -50.86149 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b56d2a2f-541b-3580-beb9-d79ba0364646 | 1.21343 | -50.87001 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26479faa-a194-300e-a541-7e45b705656a | 1.20885 | -50.86327 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb1c4be4-7c12-3560-a14f-67399fe2e866 | 1.21168 | -50.85909 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74c6bfaa-c343-33cd-803f-6e2be7111a6b | 1.21284 | -50.86637 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28111dd1-2f43-3a82-a365-2a2b49ddf5ca | 1.20544 | -50.86381 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2220c389-40a6-3b7c-b7b3-50b8df4460d6 | 1.21002 | -50.87056 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a215a2b8-5820-33ad-a913-ed854fbde8fa | 1.2048 | -50.86042 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92f34611-f281-316c-a8f1-4ae6fc476f85 | 1.20603 | -50.86745 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39f624af-0372-3f27-8b2d-6c49a54373b7 | 1.18722 | -50.88188 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca459cd2-1fae-3ba1-851b-e2d79eba8278 | 1.19687 | -50.87663 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e8eeb8f-cc60-3de1-bf08-4ecc2cacf294 | 1.20426 | -50.87919 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b492abdf-a8e3-3d56-bc8a-d0a2d66de281 | 1.20139 | -50.86095 | 2025-10-11 04:57:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5373d0c-f1e3-305b-bf1d-8ccb983caf04 | -6.73401 | -42.86585 | 2025-10-11 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3a18f2e1-847e-3432-9432-3af162a0cd45 | -4.14387 | -47.66121 | 2025-10-11 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c81e6283-4ca3-3454-ba49-1d1fd9e8ab32 | -5.8811 | -45.29662 | 2025-10-11 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0237f32b-9bfb-37fc-b160-5cea59608cb4 | -5.85807 | -42.84939 | 2025-10-11 04:59:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 44e6ffa4-7449-34fd-8ab4-ec13befc3f0d | -4.41976 | -43.47579 | 2025-10-11 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75d278a4-323d-3cb9-a90a-714cfd8f3516 | -5.12236 | -50.61714 | 2025-10-11 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a691d479-4e1a-3747-bf4b-ebefc94661bc | -6.00818 | -42.89024 | 2025-10-11 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| c533fcb5-52d2-301d-a3d7-969310beab0f | -4.7529 | -40.57912 | 2025-10-11 04:59:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d79e52c8-e835-3462-b7ea-c65eae43cff7 | -3.39075 | -50.13477 | 2025-10-11 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12e10b7a-aa8c-3e28-84c3-54be73f5d046 | -2.59667 | -48.11644 | 2025-10-11 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56e688c7-62cb-3b08-a45a-6de22088f186 | -3.98446 | -47.87976 | 2025-10-11 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b85faad-e1b6-3edf-8993-c65bfa0773a0 | -4.05247 | -48.89525 | 2025-10-11 04:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2b95373-1683-36fc-94d4-793d513d0d38 | -5.60935 | -45.82594 | 2025-10-11 04:59:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21f3c1df-9b52-30ce-86e2-5de09b778483 | -5.47453 | -43.4037 | 2025-10-11 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4752d3a4-032b-372c-b830-bb2116d29449 | -4.47774 | -42.86797 | 2025-10-11 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 061add66-1826-3ef7-b44c-648af14de457 | -5.84036 | -43.41299 | 2025-10-11 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3121e844-2d5f-32f0-9513-8f55f9bb9f52 | -3.50431 | -49.72258 | 2025-10-11 04:59:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa1e670e-df8d-3579-bfef-df490ea9d5b5 | -6.0072 | -42.89183 | 2025-10-11 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3a6b16ad-c51b-338c-8211-731b7538cc30 | -4.4087 | -43.47023 | 2025-10-11 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5ed8dd72-cfa2-3a53-b525-843ad68d3d71 | -4.75478 | -40.58074 | 2025-10-11 04:59:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c06b0c2b-2816-33d9-b8e7-3d07b4eb05b7 | -4.13953 | -47.65798 | 2025-10-11 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2263717a-6c1b-3ba5-8a8a-c7f1d22d1f88 | -5.59046 | -41.11614 | 2025-10-11 04:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c9be1734-d7bc-3c9c-a2ea-07bcbc2689be | -5.70541 | -49.30873 | 2025-10-11 04:59:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56909503-cb6d-38ac-b644-50e0d4ec6f56 | -4.42618 | -43.47256 | 2025-10-11 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48d10846-567a-3ace-9f58-a6ace08b973f | -6.16203 | -43.75767 | 2025-10-11 04:59:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2fb528c6-f303-3723-aac6-e2865086d0da | -4.66353 | -49.67801 | 2025-10-11 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15ca330e-77aa-31e3-a570-b3b0924c6410 | -4.24752 | -48.56542 | 2025-10-11 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d3787aa-8061-38d5-938c-32677017ae9b | -5.84306 | -43.41068 | 2025-10-11 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fc7baadd-3ccc-3294-a629-449544000c9e | -5.47392 | -43.40804 | 2025-10-11 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dfca8fc4-ad9b-386b-a465-87b847eb3658 | -3.51868 | -49.70396 | 2025-10-11 04:59:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 360a2ed9-3eb8-3e03-8436-d31655795940 | -4.43009 | -47.60241 | 2025-10-11 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README32.md)
