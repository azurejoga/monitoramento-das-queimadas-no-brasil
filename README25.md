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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 831d7d4e-40ed-348e-b75e-b0eb6c37f944 | -6.213 | -44.6763 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab8fa10d-00ef-344e-ba11-076ed8994b60 | -5.34069 | -46.06395 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7f81b8b-184a-3231-8514-c855bb9e3f16 | -4.30036 | -49.66529 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d8f40ac-ce14-3baa-9ebb-33934b536fac | -4.4465 | -43.22145 | 2025-10-19 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0910739e-cfa0-3ecc-8ea4-41e45e9a92ab | -5.1503 | -46.16512 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efec07cc-e5f8-3a21-a4ff-316393c93664 | -2.68388 | -49.5477 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c98bc156-02ec-3f78-8740-e4664b34ddf1 | -2.25575 | -51.9204 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| edf143aa-e8d0-37bf-803e-1ec879e26ceb | -6.41017 | -44.06464 | 2025-10-19 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dcc1f7f1-0542-3c44-a103-eb86083100c7 | -7.19378 | -42.18474 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e3d5e5d2-f110-31a9-8d4a-4fd979a3258b | -6.3503 | -45.74619 | 2025-10-19 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8cd4e8b-420a-3a3e-af18-91afb12c8583 | -4.41942 | -47.75172 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7657e2bd-a335-3143-bf5d-1d99166431ae | -6.99557 | -44.86752 | 2025-10-19 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 927671d9-3a8b-3fb6-8702-d0e023319d21 | -4.58676 | -46.30037 | 2025-10-19 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0eb51703-1ca7-3a24-bb7c-628b77a87165 | -8.19808 | -40.45938 | 2025-10-19 04:10:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 44e6b839-2829-3b44-aae5-4f1e3117e1ab | -5.4678 | -44.8927 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71529b47-9a34-3010-9ed5-a1eb5ac66449 | -5.53418 | -46.98603 | 2025-10-19 04:10:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 435c68cb-b870-3b4a-8266-873faf3535e6 | -3.15642 | -49.16474 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe704c37-cf24-3f24-a1c9-3e2915897795 | -7.41352 | -40.07493 | 2025-10-19 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f6e48ff6-1b22-3e24-a96d-2bffb2c4c404 | -3.98712 | -38.70718 | 2025-10-19 04:10:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3868f36c-1a22-3abb-94e1-d6153178c543 | -7.39662 | -42.16371 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b6c18aa-508d-3915-a22f-4500f97048f6 | -5.3716 | -45.94971 | 2025-10-19 04:10:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5f08b7d-d92f-30e9-a225-e2c1344917b4 | -1.66216 | -46.76689 | 2025-10-19 04:10:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8412ee27-edbf-3add-b05c-591194b05339 | -4.28736 | -45.4793 | 2025-10-19 04:10:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97077bac-3cf2-328b-a020-cb63820bec98 | -6.15087 | -44.3052 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0798889-6cf3-367c-ab7e-bd678eaa5955 | -4.46402 | -44.97697 | 2025-10-19 04:10:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0689c86-4980-3a38-9ac0-120f9bd2ef5c | -5.75334 | -43.22261 | 2025-10-19 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b75def6c-33cb-3809-9598-62601f7b35a6 | -6.31576 | -44.31448 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 052f5e2d-45f7-3fc8-8c40-05778f22152a | -7.59299 | -41.34518 | 2025-10-19 04:10:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82ceb2b5-54ae-3433-8b41-4e040232091b | -7.01599 | -41.81076 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bb508861-3fb6-37d6-b1b5-68e7833a8117 | -0.98542 | -47.07801 | 2025-10-19 04:10:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 317dbe6c-b86f-3da7-931c-ee3df7f032b7 | -5.48212 | -43.13095 | 2025-10-19 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c95d69ee-212a-3f4b-bb12-063893f4d51d | -2.64984 | -49.52574 | 2025-10-19 04:10:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2f964b0-a271-3f6e-88a4-c8608bf94299 | -6.14729 | -44.30471 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ffd04ad-9786-3830-8570-75af78161384 | -4.18882 | -45.78973 | 2025-10-19 04:10:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5ceeb03-67ba-3bd9-9470-f340dbbb7f92 | -6.05585 | -44.51701 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f3ba58a-b537-344c-ab58-111a9d663443 | -7.19268 | -42.21319 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d13db99e-63d9-336f-8fb4-f141dd00d248 | -5.17238 | -46.10725 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 958af8fc-55c1-341f-a9fe-ce61d3f02479 | -6.23537 | -44.14277 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c31a040-417d-3f89-9641-bd7e33d94d21 | -6.0208 | -41.9199 | 2025-10-19 04:10:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 90f78ab2-7ff3-3f06-9249-fda7adfb4209 | -7.4038 | -44.81198 | 2025-10-19 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2e898e9-76ca-309d-91a5-56b266896ff4 | -4.99098 | -43.84687 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 678b4a39-e429-34be-89d5-cc28d78b8ebe | -4.75725 | -45.42513 | 2025-10-19 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73c852a7-0aec-371c-9bc1-a9432a2dc46e | -2.25028 | -51.9093 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9101d633-0dac-386f-b702-a578f70121a0 | -4.23765 | -44.68248 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ac66cad-a5a6-3b99-b203-a14fdf077e08 | -6.05946 | -44.51756 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4207ff84-56d5-3a78-ad65-1dbca5294eba | -3.64338 | -49.96987 | 2025-10-19 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53be79db-ece7-38d3-ad45-8b858cd1d009 | -2.98042 | -50.30383 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8689cf2c-b5eb-3006-a9aa-50c207e32578 | -7.41751 | -40.07177 | 2025-10-19 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 085ac3a3-22c6-30aa-a9ec-e1f81ba1fe4f | -6.19582 | -44.05166 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4affa7b0-f7b6-356c-af37-345884817e5d | -1.42773 | -49.0982 | 2025-10-19 04:10:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7975a5ea-eea8-397c-8cfb-c8da78366476 | -2.44042 | -49.36507 | 2025-10-19 04:10:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 448de750-d9e4-3c94-8612-a16eeec6d2e1 | -6.60534 | -48.05636 | 2025-10-19 04:10:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 09f5a72f-a1c2-39df-a501-ab5384a31344 | -4.30064 | -48.06857 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 929fb68b-3709-3f07-b76f-7dd2440594d8 | -5.61522 | -42.73754 | 2025-10-19 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7835cd49-32c7-313b-bdcf-94714ebe84ef | -2.70119 | -49.54085 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f30ce18-17f8-38b7-af8c-1ee7c7570b49 | -6.23418 | -44.14537 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b0d4d87-19ec-3234-8c21-fb2563761335 | -4.41984 | -43.96913 | 2025-10-19 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfbc15fe-d8f7-365a-856c-7f7cf47cae47 | -4.40176 | -44.08269 | 2025-10-19 04:10:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61192407-6c18-3f95-9619-bac8aeee9c6d | -6.25385 | -42.32608 | 2025-10-19 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 90096fd8-53a8-3143-bd8a-b8a7cc2484f7 | -4.30603 | -48.06477 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86049b4e-41d1-335c-bea4-58baa5c46635 | -6.13127 | -44.22442 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 153afbf3-ec49-390f-bd08-4fd1a7577705 | -5.59152 | -42.7083 | 2025-10-19 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d394c991-86a6-33e8-96af-e3aa5cfab9e0 | -7.47743 | -45.11341 | 2025-10-19 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dcbd5b67-6bb0-3b13-95dc-e53e0a0d5694 | -4.23911 | -43.10118 | 2025-10-19 04:10:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a343de5e-5c73-3e6b-ae94-09d28a0a92c6 | -7.86925 | -40.87288 | 2025-10-19 04:10:00 | NPP-375D | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 231aa0ea-4730-3bf7-99d9-75a3e04b2a8c | -4.58883 | -46.515 | 2025-10-19 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dded0d86-b863-33ce-839f-a36ab97d84b3 | -4.28077 | -50.54807 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62fb30d7-a7da-3aea-90ab-7b4bc85c10a4 | -7.19433 | -42.18125 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4e8eb9d9-c718-3bb0-b879-b0bb752114e2 | -4.98383 | -43.85039 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca1d352c-742e-34cc-941c-da0348851201 | -5.34106 | -44.71548 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdccc559-9f90-3c4b-8f52-592042aaf31a | -7.19479 | -42.21383 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b12817b5-5b3c-3be4-85e8-4563bcd14e5f | -5.88111 | -48.17845 | 2025-10-19 04:10:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a0ebc31-5a46-3b7a-9508-2bc99d7c64f1 | -6.8599 | -46.29741 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03fe86ef-f65a-3018-80a6-70302ef89738 | -5.71736 | -43.01425 | 2025-10-19 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e82dd224-0843-37a8-bd59-f38303c7ee1d | -5.31997 | -44.84509 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| da01b01c-6b82-3e36-b06f-eba78e445e63 | -2.43943 | -48.61664 | 2025-10-19 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dc669ea-f77d-3edf-a368-dfc7d83a9b46 | -6.86072 | -46.2924 | 2025-10-19 04:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ad36eb8-abb9-3d4e-a8cb-608ebe508312 | -7.28454 | -45.40174 | 2025-10-19 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95d25a12-a76c-3e0d-877d-374438bfb75f | -6.55942 | -46.36402 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d7d4e9b-6f34-3610-9e05-fe8302e47da0 | -5.49681 | -44.19801 | 2025-10-19 04:10:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 734a11a9-7f7f-3bfd-916c-a2842e84b923 | -5.08953 | -45.42685 | 2025-10-19 04:10:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcfc34aa-4378-394a-a2aa-67d60a8241bd | -5.55245 | -44.95621 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc307d54-2b66-3fe6-8e01-d7f83fc9917a | -5.42142 | -40.89757 | 2025-10-19 04:10:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc904c36-a7d1-368b-82ba-81b80385d622 | -5.75664 | -44.00045 | 2025-10-19 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b37dd48-7e65-3264-a7bc-adf90d04e0ae | -5.08317 | -47.18484 | 2025-10-19 04:10:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d27e626-f1f6-31d7-8f10-a55f3d12d129 | -5.21692 | -43.74591 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2310da0-b49f-3460-b428-d8cc43f42a8c | -6.35712 | -43.83359 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03d2f8d4-fe56-3d89-9ea6-7b42ebea2962 | -4.41792 | -43.97187 | 2025-10-19 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 091e0eee-bbee-357e-b7b1-32050e171264 | -3.52574 | -49.9345 | 2025-10-19 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9617d5b-e692-38e2-ab10-0cc3309bd984 | -3.13055 | -50.21297 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b29e299e-9fd2-37c3-974f-338669f6c7e4 | -2.70591 | -49.54492 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33ffc137-e256-3b62-a1f6-bd57593406c8 | -3.82513 | -48.65156 | 2025-10-19 04:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e8d76eb-be70-364f-ad26-86ff8ae71f6c | -5.30497 | -45.0786 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f79e0134-22f7-3905-aafb-9922e09bd24d | -7.13582 | -44.26196 | 2025-10-19 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d5b112d9-6473-3660-97d2-9460155f2e2e | -5.05652 | -45.43594 | 2025-10-19 04:10:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ad4f5cb-8b90-3a9a-a002-8a7fcf1196c4 | -5.49117 | -43.54665 | 2025-10-19 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a4e69e3-9b9a-3459-a1c6-ec4cc5de8b91 | -7.18768 | -42.18019 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 90c02392-fa24-3b37-a406-30b156f79bbe | -6.40279 | -47.21434 | 2025-10-19 04:10:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd177c0d-0ed4-3722-87ea-d47af9f65f71 | -4.23023 | -44.68127 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9de351e-5ab9-37c6-841f-a1b42180c5c5 | -4.59215 | -45.37825 | 2025-10-19 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README26.md)
