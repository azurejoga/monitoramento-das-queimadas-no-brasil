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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78a47cdf-4f6a-3e4b-9c75-401fa54b17cf | -4.12971 | -47.64245 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc5922c4-99c6-382b-b346-8043bd1fcbfa | -7.01181 | -59.83732 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a38b6f5-7726-34fe-b92e-4aaeb557964d | -5.28107 | -44.87973 | 2025-08-04 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88e6aa6f-ea1e-3108-8fad-9c751248e989 | -7.4047 | -45.26873 | 2025-08-04 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0067d5cf-b412-3c8c-a65b-23ea7cd40c03 | -8.00664 | -43.19942 | 2025-08-04 04:34:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cd9f438-670b-3e9c-9970-3656e02c1e60 | -8.51498 | -44.74408 | 2025-08-04 04:34:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60231b3f-a711-3ef4-866a-d3e291691481 | -7.43932 | -48.94059 | 2025-08-04 04:34:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 584ec617-6d75-3753-a451-bfebc104b019 | -6.19642 | -43.75655 | 2025-08-04 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f81b955e-e3e0-3a97-927d-cd09ae7585f5 | -4.74508 | -44.43475 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e72e053-9079-301b-a8a3-70605eae20cd | -6.31951 | -45.6553 | 2025-08-04 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87875190-7df9-3ceb-8b50-ff06f14b051b | -7.07912 | -44.37027 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62bf29d5-cdf0-3f2f-87c9-65d8864e5bfb | -6.32354 | -45.65208 | 2025-08-04 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4dca560-bc21-3f7e-8330-9ce4bee5c88c | -8.01827 | -43.17603 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bc799655-3fd0-3040-9bbd-f3629b4af287 | -7.01279 | -59.83213 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0000730-f179-3d4a-800a-5a28f4912fad | -6.14956 | -57.91668 | 2025-08-04 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d15f611-6535-3753-a528-1619a598fee1 | -4.74318 | -44.44695 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ab3acb8-f897-3b91-a114-57d842229405 | -7.77399 | -45.22589 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32b2bc4b-2d8a-3ecb-b991-9ee624c3570e | -8.31003 | -47.52175 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 99525e31-51c1-37f6-ae60-5203ce4aa22c | -8.01178 | -43.13568 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 61816803-8cbd-3b11-bc1d-f50a603f7efe | -8.35603 | -46.90698 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f89af03-9bb1-389a-bdc5-0eef6fb6a341 | -8.35828 | -46.91473 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b85ac98e-e7af-3cfd-bc8e-412cd7662e96 | -8.26661 | -47.37085 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5f4a4b3-a40d-3308-917d-e186b113a337 | -7.13678 | -44.08741 | 2025-08-04 04:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a78999e-8151-3958-8120-d67e9869a234 | -7.30541 | -44.67337 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d479d62-dddd-36a3-af58-0000bc0ff429 | -6.06847 | -44.6786 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa47c377-29d7-3fe8-b4fb-b7beb539aa0c | -8.73559 | -46.4137 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94f37451-5114-3282-8b5f-743c61f9b279 | -8.00672 | -43.14215 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 5d3a0012-5fac-39a0-af01-959db337c151 | -7.77224 | -45.21311 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13d3be9b-513d-39ab-9580-5f1fb866df1e | -7.78174 | -45.22287 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b9e9b113-6f39-365b-8381-819b52fdd802 | -7.4624 | -46.57437 | 2025-08-04 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55bc5162-e179-36e5-92a7-a95f9194a7c1 | -8.73674 | -46.40622 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f2b9d50-1207-3d63-adfc-a065f420ee71 | -4.74739 | -44.44345 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fa99f9b-09de-348d-acd6-2fc2377acca6 | -8.01127 | -43.13922 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1a45ad8-2a17-3184-9b07-73cd6cd0d898 | -4.21322 | -46.35932 | 2025-08-04 04:34:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5feaccb0-f63c-355d-9f41-fa296423e330 | -6.17165 | -44.78107 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69350ceb-9c2d-3a5f-9019-3d3c89e80a80 | -4.1242 | -47.65578 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 570ca7fa-cba9-3068-a7e0-87d8c532f460 | -8.35266 | -46.90645 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fa31cd3-2c1d-3821-ad97-b4c790cf02ab | -3.91234 | -49.0834 | 2025-08-04 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 007dfb5f-1144-301d-aee8-625dbd1969f2 | -7.45846 | -46.57747 | 2025-08-04 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 30e1e990-4586-3bec-8bb6-f9781f19766f | -4.74381 | -44.44289 | 2025-08-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5a87c4ee-ba7d-3db8-bc35-e082a5a206e3 | -7.64582 | -45.29506 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a524a4dc-5529-339a-877f-87b53e03010f | -8.25874 | -47.33347 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2f97d7b-5505-3ce4-8cb4-6d6576cd2d0e | -7.01916 | -59.83324 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 356cf9a4-4e0e-347a-b3bc-9e67e74faa37 | -8.26606 | -47.37437 | 2025-08-04 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27413f94-c2b0-3ba3-9bd1-988d9b6ebeed | -6.51966 | -44.52821 | 2025-08-04 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6177579-ac26-3a1b-8490-ea99c0044a3d | -7.19897 | -44.49312 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6e87543-ad54-3f6b-8cd2-0b9ae60542bc | -9.46354 | -46.32487 | 2025-08-04 04:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e609c7fb-4d07-3ffd-bdf5-2dd950cd6f44 | -7.96651 | -45.10315 | 2025-08-04 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3942b90-329b-3403-aeef-41e5f75c7f3f | -7.5627 | -44.41566 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2e09e89-27ff-3d01-a4f7-5c444e579df5 | -7.48307 | -45.05568 | 2025-08-04 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fde45eb-a5ef-3828-9ec6-3fe8a685ef7c | -14.84598 | -48.39548 | 2025-08-04 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dff59b30-40b4-3f26-8c10-f8f456b7795f | -12.48155 | -51.76715 | 2025-08-04 04:36:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f6ba746-f2e2-380f-a24d-5f9a2ec5f798 | -10.68163 | -56.55499 | 2025-08-04 04:36:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b58d0f4-492e-3e0f-a852-36781ae33b31 | -12.41393 | -44.70523 | 2025-08-04 04:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ea8bf9f-8365-39b6-9a54-f2fbf049ec90 | -14.83982 | -48.39063 | 2025-08-04 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfd47952-fa1f-3e4a-886d-64d2dee0959b | -10.59963 | -45.26086 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04b22df3-e627-3016-ade7-91a594fd60a7 | -10.46951 | -47.23072 | 2025-08-04 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e6dcb16-97ea-3098-b082-7ff9f678739a | -15.63586 | -47.80143 | 2025-08-04 04:36:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e348de75-da80-376e-928d-87fc71450933 | -10.56596 | -45.27026 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b62f8bd-e2ac-37ba-bce8-a302e5339566 | -10.24832 | -50.15998 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0efb746a-d89f-3ec7-86ea-0b381bc6636c | -12.64946 | -45.04854 | 2025-08-04 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0ec1f90-8cfc-325b-aaec-da9714ceec51 | -10.57201 | -45.27 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 02e59dd9-9e70-3800-a159-454f7946779c | -13.04986 | -56.89799 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c15d052e-d1ad-3f52-a727-063be88821e0 | -10.57264 | -45.26561 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90af4d15-4f39-3384-b8e7-199f61171354 | -11.92635 | -44.96972 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1960d43a-c2d4-3513-ad84-abe884ea7d68 | -11.19976 | -47.704 | 2025-08-04 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93939174-c8d6-32c2-9afc-1eb7dedf7a99 | -15.76733 | -46.56371 | 2025-08-04 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43bd474c-a47e-31a3-ab28-34c78b2000cc | -11.74981 | -44.99683 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 022661db-341a-3e26-a04f-55754af0ce55 | -11.78137 | -44.99262 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e455970-3325-3a81-a2da-af8afb6c749a | -12.58917 | -45.07124 | 2025-08-04 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b505472-9340-3485-a9ba-bafd8909217f | -13.24771 | -46.96873 | 2025-08-04 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ff55d45-55e3-3ade-b84a-972458128bbd | -11.22488 | -48.43701 | 2025-08-04 04:36:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 637f7d27-3099-3a50-aaff-2a22b29d1339 | -10.24772 | -50.16364 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9370ff18-01c8-38f3-ab07-16dd1d451958 | -10.56771 | -45.27377 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a39ef71-43f7-316d-be87-88ceaa0e5409 | -11.75292 | -45.00201 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01fe2617-bdfd-3ad5-b078-4f06911d68d0 | -13.688 | -41.36494 | 2025-08-04 04:36:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 922ab275-f66d-321f-967d-9f390141a86a | -10.59596 | -45.26029 | 2025-08-04 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee69e6c6-27ee-3c9e-8501-c341ed3c43f2 | -12.75689 | -44.41526 | 2025-08-04 04:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e85e941-38f4-32fb-a267-5505c57c3768 | -11.75226 | -45.00663 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f7af8ff-b5a3-3283-8a3f-1dd94f276be2 | -13.0279 | -47.39757 | 2025-08-04 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92d3d2bf-5966-3811-81e9-6b060ec2f3e9 | -12.7014 | -48.09693 | 2025-08-04 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e0d3dcb-4c5c-3fee-9585-0fb65d6cc708 | -16.08055 | -43.62936 | 2025-08-04 04:36:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35ee0f62-1112-3ed6-81d6-0a62820191ae | -10.24712 | -50.1673 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41981a9f-127a-36a6-9b33-c541c3cc3fa0 | -13.05936 | -56.89973 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c19adf1b-5c4f-306e-b8a6-8b241705c03c | -13.05365 | -56.90405 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d97a7189-b5f0-3029-a55f-f11a6c72ff0d | -15.56548 | -47.08047 | 2025-08-04 04:36:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d67fac34-5c83-3fce-80d0-a7c8cb5653b7 | -11.22355 | -51.5334 | 2025-08-04 04:36:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 463aac91-d0dd-3847-9b3f-7c46cb8b86c8 | -10.70924 | -48.29709 | 2025-08-04 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fee6d40-871b-3ffd-b583-be99594e257b | -12.70477 | -48.09744 | 2025-08-04 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c27df1c6-f446-3b0c-856b-a16b526e0fea | -13.05082 | -56.89282 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 864cdef5-b346-3da3-b568-2521e184ffe9 | -15.56784 | -47.08913 | 2025-08-04 04:36:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ac68cb3-689a-3a7a-acc5-00055a5bdab5 | -13.2483 | -46.96476 | 2025-08-04 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33d7a8bb-492c-3d37-908f-76ac79b0a4ce | -11.92762 | -44.96078 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd19a942-b33d-3198-97ba-66853d8095e2 | -10.25171 | -50.16054 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70560d53-fb58-3c14-a857-ffbd671224f3 | -11.92573 | -44.97411 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0bd7397d-bb4e-3b09-8264-90e12c819a7c | -15.77068 | -46.56199 | 2025-08-04 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 993d74b3-1195-359c-a43d-4da86518ddfd | -11.78441 | -44.99524 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0587219-cf58-3342-8fa6-9fdd4cd672fa | -11.75359 | -44.99739 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c468569e-9bef-3e16-a19a-3571fe798155 | -10.11748 | -45.65791 | 2025-08-04 04:36:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebfb872d-ccfe-3628-bc1b-bd11a22c9984 | -11.74914 | -45.00144 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README18.md)
