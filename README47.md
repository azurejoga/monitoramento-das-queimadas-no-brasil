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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6fcb654-68c0-31f3-957e-e4fb1b210ad5 | -8.44888 | -54.70726 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 830cbdeb-31fc-3300-b60a-7bda5263d926 | -4.36132 | -47.77617 | 2026-09-02 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a2ccf8c1-eb5c-3992-9af4-bc2edfb53aa1 | -5.86001 | -57.55155 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75cfc9dc-d1fd-331b-a861-21d2ec49a100 | -9.42289 | -45.61682 | 2026-09-02 05:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 640ee925-a4af-38f4-8478-fb5026451b95 | -6.14736 | -57.75365 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9541c3b-23fa-3f96-8bc6-fec752660538 | -5.24983 | -55.89928 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8ebd821-40bb-31fb-9fed-c0f20287acad | -4.97648 | -55.85057 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de726059-34f4-3f84-890e-10918f39c36f | -5.57727 | -60.20056 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae2fba44-1371-313c-8052-f590550bd213 | -8.4445 | -54.73704 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 834fd2dc-ce35-3620-befd-fad6be8ecc71 | -7.35925 | -60.6037 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 748cbd4d-bfdd-3e4e-831e-1180a5546766 | -6.96636 | -59.74573 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54c9b80c-95ac-340d-980e-bd936f3f086a | -6.82558 | -51.1534 | 2026-09-02 05:16:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6061c17d-5f38-3a12-bb62-2a0143bcfa6e | -7.66009 | -45.87238 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0abbd9ae-6bbe-3600-a1ea-479511f7ab4a | -7.57693 | -61.3299 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87bdc9fb-ff60-364f-bb12-414f4f20f1a2 | -6.67679 | -56.15837 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7c06a6b-87cf-321f-aee1-30fc02462b69 | -5.86139 | -51.71175 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d7f38f8-cf77-3f11-8d1a-46000887d1bf | -7.28758 | -52.3574 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18215273-52af-30d1-9af7-b0035ccf9b6a | -5.24927 | -55.90287 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a55b5bf1-ca08-3c79-beda-7121a6e0a2dc | -7.20956 | -60.67543 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d7f9138-7d1e-3b79-a55d-a96caa3ec259 | -6.05887 | -57.64715 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf178f6-8711-3194-8881-9f69ff74fb16 | -4.69963 | -56.05547 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f467e081-80ad-3e4a-a85a-4d292c3984a8 | -5.89496 | -57.75889 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cab398f5-ded5-3f3f-b06a-0f21a81aa943 | -3.2396 | -47.24752 | 2026-09-02 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 460272df-690a-3782-8ad8-926a3033d27d | -6.88189 | -59.40083 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cdb43e22-7fc2-39ed-9717-2c522798c3df | -5.87456 | -57.7805 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 973fa4be-8c73-3ba5-9277-0483f100020c | -8.46821 | -54.72763 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4855ff6-54d7-37be-b468-4924605f8c87 | -8.46771 | -54.70584 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f05db81-d8c1-3466-90f0-0c932ea6f218 | -6.94339 | -56.44944 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b83d8a48-6b84-35d7-9922-0c7b38fa7a9f | -5.22382 | -60.05576 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f686061-261c-36f7-81fe-0204f189c52d | -3.97382 | -60.03606 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb75a933-420d-3035-8a5c-21130a2b5e61 | -7.21023 | -60.67136 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fbf47cd-7eb3-3ddb-8f4f-ff0a7165c043 | -6.15732 | -57.77645 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15bd75d7-0d2a-3df6-82d8-575fc0fce434 | -5.85506 | -57.56138 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d433ce7-118e-39ab-abf1-3cf3255e1980 | -6.14393 | -55.66619 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45d692a1-6674-3a09-b582-8a4c9d0b79de | -3.57749 | -58.74944 | 2026-09-02 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17902862-0a88-3d24-a2d2-4036744babf2 | -3.09229 | -61.21324 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93f5e234-1b49-3cbb-a5d6-4acb1619b0ad | -8.25003 | -49.50805 | 2026-09-02 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93db158b-e086-3079-bbde-5fb8aa6d2786 | -8.71058 | -52.36025 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8de0efa8-bdf1-3cc3-97fd-342255e8f7dd | -8.46583 | -54.71854 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 35725f02-7b8a-3512-8ec8-40198a546f36 | -5.58212 | -60.19312 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f2bb26f-af62-312e-98ca-5085ca855593 | -7.6594 | -45.87772 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e3b0198-07b8-3a78-a57a-3ad3a11af610 | -9.15045 | -49.97704 | 2026-09-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dc087ee-2d42-3e52-ae8a-e53ccac4aa70 | -8.45189 | -54.71212 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d35ad04d-787d-3f39-985b-ab9483de35ab | -6.85974 | -59.47266 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 147f5764-fa90-3c3b-b3ff-41381ae06e04 | -4.40474 | -59.85701 | 2026-09-02 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7522a94c-cea5-3b90-81c2-5d1f55ebec53 | -7.34906 | -60.57715 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c8d60b7-03eb-3940-bb63-fe1ebee3fbb8 | -6.17823 | -57.73019 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c3b6e1f-949e-3bd0-8566-31d4c1efbc31 | -5.95243 | -57.69754 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ef9657b-a6ce-3e66-a845-e7c062b62f02 | -7.33778 | -60.57934 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a862a31a-3541-3aef-8d06-3f05632b4ca7 | -5.87235 | -57.77306 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 078110af-8866-3e1e-990c-e5759f3690e0 | -5.87125 | -57.77998 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ab8f5dd-c144-3a77-b308-280ba44da81d | -4.09685 | -60.66506 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a157e5f1-579b-3cf7-ac6f-80da242c0552 | -3.19502 | -61.14119 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 000191e5-2694-3f6d-84a0-70fd095b7502 | -3.7135 | -58.86454 | 2026-09-02 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4a0c9b0-fe30-36a8-9a13-f214826f2f6c | -4.12228 | -51.03043 | 2026-09-02 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb07e0de-32de-38f1-84fc-f0f46b64d50d | -8.43055 | -54.72853 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d8f19195-3dd5-3caa-acb2-c2b5488ccc53 | -7.54019 | -61.30158 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c885733a-0c1b-3181-b1b9-d6873f4c8260 | -6.55387 | -58.56843 | 2026-09-02 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0fcaa18-227c-353f-b52b-212d1444b4ac | -6.69416 | -59.95165 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38bc9c80-9d2e-325b-9d29-5f9735aa4346 | -6.7716 | -59.43236 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7bc07d8c-969a-38e0-b7de-90f973199414 | -7.20039 | -60.68651 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78edf00f-c8d9-30aa-a9c0-2e1c9b18f9c8 | -7.43129 | -59.77747 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb59c5c8-870a-31b8-b815-060267e79e1e | -6.2505 | -55.43065 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa97863b-c435-30d2-abeb-a78f6a1ba289 | -3.74876 | -59.32135 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 495dd981-62b3-320b-bd13-96430998b94c | -5.24871 | -55.90646 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fb313c0-10df-3fce-8dcf-208262cad1f3 | -5.94912 | -57.69701 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e932def4-d2ff-34fa-a4be-035da5248a8f | -9.00685 | -50.7808 | 2026-09-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| f0c29d58-13e9-3827-8b14-a5fa018a79d6 | -6.88249 | -59.39716 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 820d1ac6-81dd-3fcf-9fb1-ffc1859cb6f7 | -8.48229 | -54.70803 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| efe8733d-89b9-37dc-959c-56659d097a1d | -6.17768 | -57.73365 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa05fd45-288e-321b-963e-0d627c7bee26 | -6.42968 | -53.56174 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 365c0019-c78e-3dad-8eb0-c29550fa6254 | -3.75286 | -59.31807 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60bea39e-7c4c-346a-8fcf-0476524f5646 | -6.85573 | -59.4758 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c58c8e40-d741-3676-ad9b-93593932f3d6 | -6.8792 | -56.50881 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da658b50-bc28-32ab-9649-fcb11a31ebd7 | -3.90613 | -59.64818 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58108a8d-5291-3830-beab-50a700d249ac | -6.0263 | -57.6809 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c5e27b5-5d9e-351c-bfc8-8465e7c3c13b | -3.79439 | -59.34835 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7c977f2-0212-3168-a18d-cd7ece64c0ec | -3.37379 | -52.79766 | 2026-09-02 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d93f30d2-c6eb-3888-bb3f-95475fe46520 | -6.25512 | -55.42363 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fb1696a-5a03-3659-99f3-72c0e2b195b4 | -6.24576 | -55.48379 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d605eb2d-b637-3d78-b9ba-9697ccd490c0 | -2.12047 | -56.81515 | 2026-09-02 05:16:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17bedc03-e12e-3aba-a4d4-7bdfa646a543 | -4.12287 | -51.02642 | 2026-09-02 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c4934fa-8cea-3c2f-b1e6-7f628c582977 | -6.76019 | -59.43807 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b9bab8d-9de7-3554-8da6-3cd26872cb3e | -2.94574 | -60.90211 | 2026-09-02 05:16:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e8521d6-21c5-3d80-bb77-32b03094ecec | -4.26494 | -55.15672 | 2026-09-02 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f3e18616-8dd9-32d8-8765-059c56cb8fc1 | -7.06301 | -52.73208 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3970fd25-e1bc-343f-a9c8-62ac860dadaf | -6.77441 | -59.4366 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0d11f2f-1f5b-3f64-a17f-6b17d50e00c0 | -6.15291 | -57.78283 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 309e6cd4-186d-3d04-9127-8c7d5ab85621 | -7.2573 | -61.10924 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88212376-def1-35ce-a8a3-26a96844cce5 | -6.14403 | -57.7106 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1396c0a2-c5f3-31e6-b536-31ab00486100 | -7.5751 | -60.48125 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5dac02f-a6e0-3cd5-9504-e985568cc3ce | -9.43622 | -45.61839 | 2026-09-02 05:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cf5a86d-d37f-3f46-a314-541d8c224a90 | -5.94857 | -57.70047 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf329a0b-f271-3d10-935b-7753f1cedc54 | -6.08982 | -53.80753 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8574e9e9-13c8-3658-bdd0-1f8ab25ec814 | -6.2249 | -55.61783 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7639e388-a357-334f-a7c6-9fa432761cf1 | -6.15617 | -57.71961 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ddf5a4c-cde1-330d-a287-117c67600bcb | -8.44963 | -54.70105 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4878006-4666-331c-941f-1e34cbb809af | -7.35859 | -60.60775 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9e0ef2f9-ef40-306d-9730-04e50c41efec | -3.37492 | -59.39441 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c00496aa-26e5-30fc-ba3c-cfa2acaf8917 | -6.08126 | -53.66439 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README48.md)
