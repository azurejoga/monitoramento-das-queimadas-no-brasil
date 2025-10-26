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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03ee92aa-a223-3888-931c-9d6221a13d0d | -2.8036 | -49.13892 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c6f25a1-7b13-3648-b25a-ed9677235674 | -5.70994 | -49.30491 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 82baaaba-c6a5-3e67-964c-a00375451b6c | -3.23306 | -45.93564 | 2025-10-26 04:49:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d134a090-1299-328d-b573-5bcf3c6e9beb | -5.64312 | -47.62204 | 2025-10-26 04:49:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74c86fc8-6152-3a52-b1ba-8aedb94fa246 | -3.86857 | -52.18853 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e19bcd5-6d30-31d4-82c8-8e8c985e70fb | -6.702 | -42.04601 | 2025-10-26 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 5e26a905-5074-3f7e-a524-ba1232b5a5ee | -5.64162 | -51.09664 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47365490-daac-3cc8-a543-61a8868586fd | -4.78323 | -42.77913 | 2025-10-26 04:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 15f784e9-6fb3-3811-bed6-d9e7556fcea4 | -4.27235 | -40.69938 | 2025-10-26 04:49:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2f968c42-e35a-30f9-a7a2-13b286a39f82 | -5.61144 | -42.77878 | 2025-10-26 04:49:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f7e345cb-1b37-3068-bf8c-1d537948bb7b | -4.8697 | -48.64785 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4253dcec-cfe8-3ac8-8052-d554b03697c4 | -2.77584 | -50.4051 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7126528-13e0-3854-a0fa-07f8874510a0 | -3.54409 | -52.45869 | 2025-10-26 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1af6982-5b7d-3544-acc2-52f3ab59ad57 | -3.26597 | -50.05019 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9b9ae90-a29e-3d45-bbb7-c10e5ba22e24 | -3.76333 | -47.57096 | 2025-10-26 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57cc4653-a26d-3688-b055-acb6fe14119f | 1.16092 | -60.67341 | 2025-10-26 04:49:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a593039-b3c3-368c-a565-d43fb6ab6991 | -3.10407 | -49.45795 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fff939ec-7250-3775-b7f4-53421ce81da7 | 1.14169 | -50.99694 | 2025-10-26 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0bce85e-042a-33fd-af65-b3e464a4c629 | -2.73638 | -49.38848 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 708d1ea3-6646-3eb0-9d0e-023bf9071350 | -3.10579 | -49.46988 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8317df05-6048-3b80-9433-49a802222dba | -4.31354 | -50.33527 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4be3f4ed-6c94-3760-ba63-3ceccea01ad2 | -6.99527 | -45.99677 | 2025-10-26 04:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f05d90d0-3238-3295-8f97-3abdb8f73197 | -4.7279 | -49.09214 | 2025-10-26 04:49:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 562feb56-984a-3937-9568-5b4a9b79a4a0 | -3.10088 | -49.46224 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4688865-f8fd-3d5e-b5a7-9ac8c1c69183 | -7.34951 | -42.44093 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0971a3bd-54df-3064-a642-a3eb2979c5be | -6.39256 | -45.77963 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e987f2ac-3c39-3cad-9408-2244f940641a | -4.15956 | -47.66442 | 2025-10-26 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 239bb13f-cf18-37ff-852b-49c58b280186 | -3.54425 | -53.32086 | 2025-10-26 04:49:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4924f95-e486-34c8-b818-410033f80f41 | -7.11762 | -45.38912 | 2025-10-26 04:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dabaaf46-11f1-3ee1-9e15-ae29e55dc82d | -5.9255 | -45.40396 | 2025-10-26 04:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b2c42b5-3a33-31ba-9e86-d103e80bd60c | 1.61472 | -55.74398 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a32f9e5-9040-3243-82ba-6982502e2eeb | -3.8484 | -51.38348 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 18be8363-cbb7-3e4a-8bc7-bdfa3604e92c | -3.51936 | -52.85318 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 317472ba-f646-3fce-9af7-af3dbc9e4f0e | -6.78183 | -45.41212 | 2025-10-26 04:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3b70847f-f302-3247-9eb7-dbd87d50184b | -3.74051 | -42.2972 | 2025-10-26 04:49:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 21f1f8b2-238d-36df-994d-4a2bf15c961a | -5.71372 | -49.28015 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 133e2774-a9c6-30bb-86d0-6ea28e798435 | -2.32394 | -48.58539 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d1f419e5-c0b8-36df-99f1-fc429f243370 | -2.22651 | -48.36962 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d062d3a-18f1-31e0-9d31-a0fb30b463f3 | -3.06334 | -54.61584 | 2025-10-26 04:49:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5383acf5-b0b5-3c1a-a0bd-c962b258601f | -2.69132 | -54.76898 | 2025-10-26 04:49:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 35dd9169-3e77-3547-a74e-237742ae8356 | -3.81594 | -54.72104 | 2025-10-26 04:49:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd29d78c-66c4-330e-b69c-bb18e769b89d | 1.53321 | -56.00291 | 2025-10-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a21987d7-4c46-3ce8-8d98-b5be884d8c03 | -3.10003 | -49.46122 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ace4ddab-5063-3556-a1fb-3352b28d6000 | -6.7911 | -45.41384 | 2025-10-26 04:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9dfdd6ad-efd6-3804-a2de-8c06c1361753 | -1.38168 | -55.34991 | 2025-10-26 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baa26a0e-e1dc-3491-baa9-18c50f212297 | -1.37772 | -55.42454 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 112a7316-7364-32eb-b87d-28de151c3d56 | -6.73678 | -44.15384 | 2025-10-26 04:49:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46906f47-6168-3917-beef-9f04b454e2ad | -3.72034 | -49.30816 | 2025-10-26 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc6bf124-e370-3de3-a0d4-7b01585301fc | -6.01766 | -43.30471 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e04e7533-1d20-3e87-a0ec-376bfff9ed05 | -6.60011 | -42.05545 | 2025-10-26 04:49:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 27b3af88-34a8-3641-b572-4f9775f3052b | 0.42215 | -51.07125 | 2025-10-26 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce22a041-e359-3d7e-9abc-2854b86481f0 | -5.01162 | -46.85597 | 2025-10-26 04:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcbd2903-512e-35a5-adf9-ce20090340cb | -2.98161 | -49.1162 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d95ddaad-c5ba-3667-8b64-2e72095f32f1 | -3.10522 | -49.45033 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71b9f103-0bec-313c-a2c7-75cf778450fb | -2.20229 | -56.95132 | 2025-10-26 04:49:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b059a343-e976-317e-a2e5-4731d44e1242 | -1.19139 | -53.38549 | 2025-10-26 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 005f4ce7-1ad1-3e84-80fe-f56aab9e975c | 1.63453 | -55.71224 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4e6b148-f85c-39b8-b345-e6bdbdf2fc50 | -6.17779 | -49.24196 | 2025-10-26 04:49:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc12ad87-23a8-3409-8b73-39081432f398 | -4.54852 | -46.55223 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e79c7c3e-02c4-382d-a4d3-cf02a72208e6 | -3.10697 | -49.43881 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96d68a50-4051-3db8-b939-16a1f4e1359d | -3.10386 | -49.44318 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c944e761-da72-3b90-b31b-d01a82ca6516 | -4.89904 | -43.24887 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 40945405-f0f7-3480-8e12-c653c13bdd70 | -5.10483 | -43.19493 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b306f14d-9e45-342f-8b60-1f36d00e8b08 | -6.2129 | -42.5466 | 2025-10-26 04:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a8c2301f-a960-3293-8054-369c06fc38d9 | 0.41348 | -51.06564 | 2025-10-26 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b8651db-0046-3a51-a684-66ec3520f2fb | -3.33875 | -52.83184 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b016bf9-31da-3a7a-9942-64ed603effa2 | -2.30144 | -48.56521 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0476c44e-6dd0-3683-bd7a-bfd8d6a841e5 | -3.40261 | -49.53002 | 2025-10-26 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 82962437-5718-3bfd-b38c-15f08bf9998f | -6.13068 | -41.71627 | 2025-10-26 04:49:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0b1aad20-ef69-3d84-a0a5-024fb36ef675 | -7.0482 | -39.74241 | 2025-10-26 04:49:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b5a2c53a-28f1-3991-a099-cdf77ced9f3e | -6.71314 | -42.05171 | 2025-10-26 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 17b18b2b-e34f-340c-86f4-fe12c6d1d309 | -7.02061 | -44.68688 | 2025-10-26 04:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f832e29-4346-327e-8ac5-f3fcc9494c09 | -6.47531 | -47.55335 | 2025-10-26 04:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| da7578e6-bb34-3361-a1c1-74568cf2962f | -5.10766 | -43.17989 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d050464-8cae-3758-95d1-1125d04feb61 | -4.90655 | -43.23352 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 370fb74f-8b67-342f-9b46-0fe11f5a27b8 | 1.64203 | -55.70753 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9e93933-3298-3002-b79c-41a7db0666c5 | -3.10639 | -49.44265 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f289ae45-8bce-3d56-a630-69bd7fb0d2e4 | -5.7129 | -49.30955 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ac028eb-626f-3f83-adff-73fc3a3f844f | -7.05322 | -43.88401 | 2025-10-26 04:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f1ccbe6-acd0-3e4f-bf5a-507ccdf3a63e | -3.82589 | -51.70057 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ed0218a-4795-37ce-aec2-9006dd2f5af7 | -3.75689 | -51.75312 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8d74b4d-0792-390d-9f61-2d52cb721086 | -4.71273 | -46.43419 | 2025-10-26 04:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cf40e903-bfc0-3032-8875-8ffc2f4ac3b0 | -3.2258 | -42.22717 | 2025-10-26 04:49:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d4454e2-8217-30d1-8d2b-c82118c8bf05 | -6.62803 | -44.63285 | 2025-10-26 04:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d8da65ac-a6e8-337a-ac56-b698469d0ffd | -3.38372 | -52.37301 | 2025-10-26 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93bb3968-db1a-399f-bf4f-e684e27551ec | -3.13666 | -50.16028 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 27e60486-7eb8-3fea-b727-ea57759dca68 | -0.73261 | -48.06868 | 2025-10-26 04:49:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f9d1081-e8f6-318c-a5f5-a88ffed8e536 | -4.81064 | -43.30365 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0b7757b-2b09-3a9b-85bd-e16b306b679d | -2.6666 | -49.49773 | 2025-10-26 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccad64a2-12cf-335c-b417-fb36d310c78b | -6.71433 | -42.04285 | 2025-10-26 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 629a765f-81db-398a-af0a-8202060a3c48 | -3.7412 | -43.37962 | 2025-10-26 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b90bf78-7e4f-3dd4-a172-d3ac560d5737 | -4.89121 | -43.22799 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98c98b89-8618-388c-a4a7-933949cb2270 | -3.27332 | -50.04758 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5027fc5c-75d2-3b16-af39-0d644c26587f | -2.8077 | -49.13556 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 300b1e00-19df-3f49-8f54-6d4ff8e5b1ea | -3.74076 | -43.38262 | 2025-10-26 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a1982e91-193a-374e-b993-ee8a090908b0 | -3.10464 | -49.45414 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d328e453-1984-37e8-867d-f76306b280c5 | -4.93256 | -48.55503 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48180e00-7efc-3566-b8f4-5d40f5649db9 | 1.53023 | -56.01083 | 2025-10-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7af737e-097c-3762-ba68-15abb2750e7e | 0.41885 | -51.07176 | 2025-10-26 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b2b6797-a814-33fc-a84d-39bb485145cf | -4.64088 | -42.50966 | 2025-10-26 04:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README34.md)
