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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95ff9dca-fea8-31d8-99aa-b41a1fcd5e05 | 2.84964 | -60.07662 | 2024-11-10 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 565e2971-deca-3354-9ac9-f0fb71915fb3 | 2.85033 | -60.08098 | 2024-11-10 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73fe4008-2a10-39b7-bde5-e7e0b38d903f | 2.85407 | -60.07588 | 2024-11-10 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec197d00-d54b-33fd-8377-aeea4a59fc52 | -1.27751 | -53.71191 | 2024-11-10 05:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 968deb11-eaf9-3c71-9e75-5f9ba8629269 | -2.0774 | -54.67875 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f255891-9926-3225-8b69-5c42c446eb0c | -1.34921 | -54.62809 | 2024-11-10 05:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a9ef32f4-6a24-35b8-81df-b5568d0710fc | -1.32484 | -54.63725 | 2024-11-10 05:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2dfa8bb-b753-3be8-a647-ad1de9e05be0 | -1.47513 | -54.30322 | 2024-11-10 05:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ddd7b510-9f15-318a-90be-3e56149a7763 | -1.34695 | -54.62844 | 2024-11-10 05:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| fe9cb961-4e8c-3b7e-ab94-93df74b84890 | -2.61937 | -54.39246 | 2024-11-10 05:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d63665a3-ad5c-38cd-8160-f16ffaf555b3 | 2.85016 | -60.08366 | 2024-11-10 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0720c249-9b05-3b8c-9b30-e34fdb715be6 | 2.85475 | -60.08024 | 2024-11-10 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70a6ba59-35f5-3d47-9953-a203c42324aa | -1.28375 | -53.71861 | 2024-11-10 05:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 2b083eba-2a3f-3502-8b61-eb257722e8bf | -1.47573 | -54.30068 | 2024-11-10 05:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71cad5c8-cd5d-380b-884c-54d76a1f9f13 | -1.28056 | -53.71622 | 2024-11-10 05:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 310d9479-ac94-34ac-8267-28c2b492c6ff | -1.30612 | -54.6691 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aeda5c1a-b018-3f69-a12b-963383e7cf0a | 2.85459 | -60.08292 | 2024-11-10 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c12d7293-2c8b-3912-9a39-4f25382d1d08 | -1.52033 | -54.9975 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2b0b0eb2-dd1a-3361-a1d7-d29dad4c7085 | -1.15024 | -53.78385 | 2024-11-10 05:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4583bc67-f47d-3814-9abc-c03a48312dff | 0.68564 | -59.27444 | 2024-11-10 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f65a2776-fab4-32be-90a9-322da7109d85 | -1.48276 | -54.3009 | 2024-11-10 05:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b0ae2e86-026b-3f52-8315-d2819ae5a22b | 2.84945 | -60.07932 | 2024-11-10 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ab484e1-de18-3986-97bc-5d548d2731ea | -1.30526 | -54.67471 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f3cd7b32-1fd4-33e0-abbc-b505e0b836f2 | -1.45018 | -55.51179 | 2024-11-10 05:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd35a43f-5ffa-3b63-bee3-c40302b785f1 | -1.42338 | -54.77496 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6bd1d813-4d05-33c4-b9ce-cf053498a553 | -1.28152 | -53.70987 | 2024-11-10 05:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7e8b5288-2082-35ef-a17a-4b6a73e7f734 | -1.34242 | -54.62728 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b8b4ccfd-f796-3648-bdca-3eac3af07d09 | -1.52288 | -54.99569 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c0c73f17-1802-36bc-be8f-c601ab40dc17 | 2.85387 | -60.07858 | 2024-11-10 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95a28d0e-1296-333d-96db-e6105d452786 | -1.2847 | -53.71251 | 2024-11-10 05:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| da05b744-987d-3310-a320-99333617dc0d | -3.15698 | -54.48092 | 2024-11-10 05:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 640511c4-6efb-3979-b257-fa8a7590a6d5 | -3.15805 | -54.48065 | 2024-11-10 05:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f23a409-ea90-3297-90a4-bb98e4964cb6 | -3.14998 | -54.48 | 2024-11-10 05:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f40419c-31c4-3745-a510-7bde49dcd577 | -3.19366 | -54.32196 | 2024-11-10 05:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ef5f237-0f86-35fa-b306-817b1b775187 | -3.14902 | -54.48688 | 2024-11-10 05:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73fae018-6952-3b07-b16b-430246762de4 | -3.18763 | -54.31366 | 2024-11-10 05:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0b7738f-bc12-34e3-abd5-5e0ac91ba883 | -3.69629 | -54.61543 | 2024-11-10 05:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 585823e5-21f8-398e-93ab-207936aa9d4b | -3.15004 | -54.48668 | 2024-11-10 05:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5433570-78dc-3249-ba95-0686416f0b73 | -2.23485 | -59.11414 | 2024-11-10 05:57:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0007e439-fa19-3142-a01f-165d71d2a440 | -3.15105 | -54.47978 | 2024-11-10 05:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd21522c-5199-36f9-995e-cc994254f720 | -3.33084 | -54.174 | 2024-11-10 05:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d5008d98-3e5e-3bb2-bfa4-02f2583a98ec | -3.37123 | -57.2447 | 2024-11-10 05:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c342538-eb57-33d6-8af0-d3f70b038938 | -15.31194 | -56.51369 | 2024-11-10 05:59:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca1c4403-923b-3171-9d75-883691e00be1 | -15.27286 | -57.68287 | 2024-11-10 05:59:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e353d30b-0cde-30a1-a98b-675d593ada07 | -17.24132 | -57.49327 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 9e08b272-357a-3148-82d5-a89f818fd4ab | -17.30449 | -57.48823 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| d9efbc69-1af7-37c9-a380-34e8af1f73ab | -12.41918 | -64.14065 | 2024-11-10 05:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4cd63f8a-f013-3ce8-bc52-1a39734cfdaf | -12.42451 | -64.1332 | 2024-11-10 05:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 60ab8438-71da-3d14-a015-8c86b85d13d2 | -17.29758 | -57.48748 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 5acee366-7642-37ee-89c8-b022efd737f3 | -14.71781 | -60.02523 | 2024-11-10 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aae9aa1f-e977-3545-b1ed-51b5d4b7f64a | -17.28951 | -57.49997 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| ab80864b-2037-3155-8981-6a46f6877efa | -15.30478 | -56.51286 | 2024-11-10 05:59:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3ed8189-23eb-3985-982a-32f41cf7523e | -17.24192 | -57.48667 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 65ddf9dc-45f7-3fff-a228-d06b45cbcd1c | -12.19749 | -64.02556 | 2024-11-10 05:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98082b6e-1b09-3fff-a441-98e7387a1958 | -12.41973 | -64.13665 | 2024-11-10 05:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5fddef34-2a32-3cb2-87b4-f5309afa7bb8 | -12.42342 | -64.14124 | 2024-11-10 05:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3354c6fc-2025-33c8-9147-a3c4a7c96ff2 | -17.3039 | -57.49486 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| b07c9b38-858c-387e-b802-03037c02001b | -17.29699 | -57.4941 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 8edc5f74-3486-32d2-a101-9ffed990a8b6 | -14.12852 | -60.43973 | 2024-11-10 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bbb833f-81f5-3e0e-a437-f3d90a90f2de | -17.30392 | -57.49841 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5fc33256-3f33-33f7-8c1c-1d618c88e300 | -17.24177 | -57.488 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| f28ed2f3-0b1d-393a-b77f-dc0ac817a6e7 | -12.42027 | -64.13261 | 2024-11-10 05:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ba1eb837-6a85-34ef-a3e3-09eb3c43ceca | -12.19696 | -64.02954 | 2024-11-10 05:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c0d62f7-ca02-3cb7-b3d9-a9a042bb6c2f | -17.24883 | -57.48741 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f3fc3af1-ff71-38ef-9130-17e6e5345e7b | -14.12811 | -60.44341 | 2024-11-10 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18a906de-d838-38ce-bbd4-a5fbfc03a189 | -17.29817 | -57.48085 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| b34a8cb9-1f33-3d59-8e36-f1b51f17a80c | -17.29067 | -57.48672 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 0e1157f8-1bc9-3809-9b96-db38c8d04dce | -9.45334 | -68.59244 | 2024-11-10 05:59:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0af3fbc1-70c1-33f5-a52d-5ab657d6c74d | -11.95742 | -63.19568 | 2024-11-10 05:59:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bcfec39-cb76-327b-bd94-e139642fa723 | -17.24867 | -57.48877 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 140bfb87-4bc0-37e2-86d1-c986085bc757 | -17.29009 | -57.49335 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 21550451-1ba9-3937-b5fa-cb8f2b005ccb | -12.42396 | -64.13721 | 2024-11-10 05:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ee6beae1-24fe-36b8-9d9c-fdde0b9a2d48 | -17.2412 | -57.49463 | 2024-11-10 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 023059b6-9f54-3f0a-bbd5-15262b10eeb1 | -15.26616 | -57.68216 | 2024-11-10 05:59:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b884df3a-4c3e-37f0-8d7e-609f54824bea | -3.2352 | -50.2855 | 2024-11-10 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| d5500597-e5b8-3ec2-aba2-c2f6c1436e03 | -1.5347 | -52.2104 | 2024-11-10 06:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 99feb79d-3ee7-3bde-9e0d-46a96c7f8135 | -3.9668 | -48.1932 | 2024-11-10 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 5cff0939-0339-3d82-a7f2-fd5722018084 | -2.931 | -52.7753 | 2024-11-10 06:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b13b0b21-7670-3b46-b436-aaa9594e4354 | -3.2243 | -53.0727 | 2024-11-10 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e9236ce2-9a1d-3685-8f5a-a4b6b3759b09 | -2.9355 | -51.482 | 2024-11-10 06:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 6b1a2a64-aacc-3744-84fb-74fa15ba5c64 | -3.9485 | -48.1508 | 2024-11-10 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ba8dcf4a-eb3e-3771-ad6b-197b90d7dc6e | -3.2353 | -50.2645 | 2024-11-10 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 10750316-f35e-3833-b903-8a6b0bcf2457 | -3.1239 | -50.4358 | 2024-11-10 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 1423b6a8-bc55-3eb6-acff-1afa796db053 | -2.9494 | -52.7748 | 2024-11-10 06:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d404a86b-ce1a-3296-a592-3d3ea8961b2a | -3.1422 | -50.4562 | 2024-11-10 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 397b0137-2e08-331e-8c29-a26badee0358 | -3.1423 | -50.4352 | 2024-11-10 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 166.8 |
| ec70003e-2db6-35bf-ae51-a0d3af900932 | -3.9669 | -48.1716 | 2024-11-10 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 9bb3dd3c-830e-3174-8439-4c8275e62dda | -2.7772 | -49.3492 | 2024-11-10 06:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 141f5262-ce2f-34eb-9c9b-c3870ccaf2a8 | -3.1238 | -50.4568 | 2024-11-10 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 4802df74-ff35-393e-ba79-77c974b2c195 | -2.7587 | -49.3497 | 2024-11-10 06:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 2d17d540-07c8-34dc-a5dd-160669d844e1 | -3.2244 | -53.0524 | 2024-11-10 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 9799bac9-eae3-3a0e-adce-ee0bd0481859 | -3.2168 | -50.2861 | 2024-11-10 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| ff7f31c3-bbb3-3322-9ce8-8d2d86cf0c74 | -3.9483 | -48.1724 | 2024-11-10 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| feb7d90b-527f-3a2f-9f26-15c40fc658ea | -3.2352 | -50.3065 | 2024-11-10 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 0471161a-7965-3fce-b726-7f140dc0a388 | -3.2536 | -50.3059 | 2024-11-10 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 876339db-4e07-3717-965a-71abb76e0142 | -17.60862 | -57.52353 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| e0997144-7fb8-35c8-823d-1d0f830e2e5e | -17.62988 | -57.51726 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.6 |
| 15d63294-f5c0-3bd6-8d10-71da9e641557 | -17.63054 | -57.51243 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 9556f982-1f6d-3bc5-b6e3-4b2505c2b7fa | -17.61658 | -57.50904 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 1ea685a1-e4aa-3794-b968-fc9f8c798b33 | -17.6246 | -57.49642 | 2024-11-10 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |


[Clique aqui para ver as próximas entradas](README121.md)
