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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9fb8dff-62bf-38ad-9e3c-dc10edaf4fbb | -1.5285 | -55.40617 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6e2dd52-44f6-3db1-853d-0f773baa27b7 | -1.52464 | -55.40912 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 354fb18d-62ed-376f-965d-fe5f84eb6863 | -1.48735 | -55.12725 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4afb5aaa-c99d-37c7-8bf0-5cf331b5245e | -1.48404 | -55.12672 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f521a913-57ce-34f9-90db-160488dc814a | -1.46528 | -55.33221 | 2024-10-25 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4183f4d7-0748-3d5f-a649-ec5f5595d7c3 | -1.40476 | -55.22012 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c185c597-f0f7-3c49-a508-bb01d0f6c72e | -1.28574 | -55.71792 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 948b998f-a124-3821-8661-0d5a5e29a188 | -1.28519 | -55.72144 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 796e4a86-e01f-3459-8b0c-e3b30a62857c | -1.28241 | -55.7174 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d159663-3e54-3561-a472-406e3b87d9b9 | -1.28185 | -55.72092 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47b9b862-055e-30ec-a0a8-8fed73e98322 | -1.20027 | -56.06371 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8af33999-d82f-3c8a-9a2a-1bc8ef9bcbde | -1.77531 | -55.09129 | 2024-10-25 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed0b32bf-19a1-30a5-a6fd-aa4ebdf0c3a1 | -1.77254 | -55.08735 | 2024-10-25 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea8dbc4f-a598-3975-8f6d-22c92fcaa98e | -1.71336 | -55.13759 | 2024-10-25 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cae9477c-f4ff-339b-8f52-87a5c6e4bb65 | -1.71089 | -55.04568 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23893153-6a73-3912-8f19-42d84fdbf97f | -1.68351 | -55.30581 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8a54935-476b-3ac0-b112-a28a4af16e19 | -1.62387 | -55.16649 | 2024-10-25 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 772a4bb4-5272-3b8a-8254-432b1f69939c | -1.62057 | -55.16598 | 2024-10-25 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ddbc424-84be-395b-a6ba-4b9f07412461 | -1.62003 | -55.16942 | 2024-10-25 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7413b702-060b-341e-8271-c913704c4d3b | -1.60314 | -55.40656 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2d80e7d-66b6-3762-a76a-1ee29a79bd0d | -1.56633 | -55.89809 | 2024-10-25 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c702f4fc-8da4-3cb6-aedd-3db1c3f6c460 | -1.52796 | -55.40964 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78ae288f-da75-3f61-a748-953b952cb87f | -1.52519 | -55.40566 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0be5ccc9-8207-32ef-a1d2-5e72dfc1d3b5 | -1.48789 | -55.1238 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c7afca1-ab59-32ae-aded-b817244af162 | -1.48458 | -55.12328 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06e8f3d5-58c9-361c-bba2-745b4da48bfc | -1.46101 | -55.16543 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6566d19-42c5-3468-9c03-8f1ccd813ccd | -1.45768 | -54.9502 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f3f1fd2-b377-3c33-9c45-7e0830a26304 | -1.39249 | -55.8824 | 2024-10-25 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf451ec6-dc10-3400-9524-2d28ea43cfcc | -1.36906 | -55.85704 | 2024-10-25 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1b2cc66-9219-36dc-a259-5166a3c492e0 | -1.56146 | -54.89252 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f445c879-b7be-3d1f-be8f-6c110c482897 | -1.45714 | -54.95364 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1188a20-7325-3f98-bd03-818468ec9816 | -1.20084 | -56.06013 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 913bebd9-efae-3ff1-8437-4162d49e6237 | -1.19691 | -56.06315 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ec98ba-506a-3bca-b96d-9b4101a1f409 | -3.68787 | -55.46177 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 311ae5f6-dfd5-35a3-b6c4-b03a42597335 | -3.67135 | -55.45919 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f2765f0-683f-306c-913b-4b7e95627346 | -3.67081 | -55.46263 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b15de5b-cd36-3ce1-92d8-4c5aa833fc90 | -3.64729 | -55.50137 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62534001-68a9-3c69-badf-a74a75eceabe | -3.62638 | -55.50515 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2501f9e4-f84b-38a5-acb8-a8a9c14e4402 | -3.62584 | -55.50859 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0671523b-2f0b-3ade-abfe-808fb834f6c5 | -3.62307 | -55.50464 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4502efb2-7db0-3536-a663-063e92dbffa1 | -3.62253 | -55.50808 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32cb1b53-6bcc-344a-862e-0ce4a46a7341 | -3.61977 | -55.50412 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e073aee-a0fd-3379-a69d-2cee92d36c26 | -3.60493 | -55.5124 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec73f953-60ef-3a2c-834c-3f6975c0ba4e | -3.50214 | -55.47516 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07aa508a-ccd2-3124-8fa6-873d12013817 | -3.49884 | -55.47465 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f7814f37-b722-30d3-9ec7-853551fe87d5 | -3.49554 | -55.47413 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e162fba-9628-3a66-8851-fae2487adc00 | -2.57671 | -55.30859 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68a7adf1-df23-380d-a6f3-b9171aee3072 | -2.48498 | -55.71904 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4b10fcf-f9f5-3548-8f16-b4a84f4bc6f9 | -2.48443 | -55.7225 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2e5910f-0240-3f96-904c-255c0a741355 | -2.48388 | -55.72598 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 029ea1c0-6e35-3a2c-82aa-c3e7d2d5193a | -2.39072 | -56.12092 | 2024-10-25 05:01:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1233391-d8ac-33ed-89e1-a51a0bf54d95 | -2.36674 | -55.28244 | 2024-10-25 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f43f2eed-a407-3d4d-b052-13d8c5842a1a | -4.19967 | -55.55626 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5ee327a-0cb2-3322-a4f2-3f41084e94d5 | -4.01317 | -56.04823 | 2024-10-25 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 867856e9-f515-3e73-8f49-447d81e5667a | -3.99051 | -55.43912 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57ad0112-6b67-3dd3-b11c-d4d1fd7d1798 | -3.98997 | -55.44255 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f441eec-093b-39b4-89e5-fb76e7d5372b | -3.92025 | -55.92643 | 2024-10-25 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 457ea06e-9270-3187-80b8-a2504da590c3 | -3.89745 | -55.81285 | 2024-10-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c78de82-f140-33a4-916e-053d1ad814a1 | -3.89004 | -55.98933 | 2024-10-25 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44d4c2b4-46c0-3d1c-a11a-f1c57a3818ed | -5.07192 | -56.2295 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdc55b2a-720c-3ad7-b401-3dece914c228 | -5.0089 | -56.17643 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5216e6fd-7e59-3835-a4c8-fb909b023da1 | -5.00552 | -56.0905 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f49edad1-dc6b-39f6-8a03-318bf1040978 | -4.99666 | -56.0607 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d48c59e6-2c62-3cda-b6fe-ea338faada60 | -4.99611 | -56.06416 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 245b5f84-21c2-3b4d-975c-acb1c72ca001 | -4.9289 | -55.80214 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e719d12-220c-3fde-bde6-72d23ca4bf3c | -4.87519 | -55.83925 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa7cc00b-7458-3003-80b1-e1ad653099cb | -4.56466 | -56.19204 | 2024-10-25 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a064757a-d731-3c78-bf2b-27369a1f5ada | -4.41429 | -56.00419 | 2024-10-25 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f95e3af2-f545-372d-b23f-b3512828d36b | -5.24624 | -55.96508 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2abb928a-f800-3339-a22e-ad19b63827fc | -5.2457 | -55.96853 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5807425-5158-3a7f-a8b7-e4c7db68afdc | -5.24515 | -55.97198 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e56004f-59a5-3067-baa8-02666b55ce11 | -5.24294 | -55.96455 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 757ce04c-a0bb-3a42-ade3-d8045cfe2dce | -5.24239 | -55.96801 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1252c2b-734a-33e2-924d-23d9e9036bde | -5.24184 | -55.97147 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54b23067-4797-3bc4-932b-e2a6fbe21280 | -5.23908 | -55.96749 | 2024-10-25 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4c68996-ba60-383d-8999-d0bbcb38294e | -1.99094 | -56.58501 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c45b2fa-ea8c-3d07-b655-b10e67c5b626 | -1.99036 | -56.58867 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 275735e4-a861-3db8-9284-1e6a0d9d4052 | -1.98733 | -56.91814 | 2024-10-25 05:01:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3316c6a3-9c83-3832-ae68-5e356389d80b | -2.57565 | -57.32233 | 2024-10-25 05:01:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bc731a0-b645-31fc-b32e-59f5fcbde352 | -6.33623 | -58.32184 | 2024-10-25 05:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2000bc6f-be98-3c81-9a9f-77f38ce96f7d | -6.16474 | -57.7927 | 2024-10-25 05:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85ab990b-7443-3bbd-90ee-b406a8577c90 | -6.54761 | -58.47406 | 2024-10-25 05:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a378f28-20a0-3076-af07-f7a5a963d763 | -6.54706 | -58.47496 | 2024-10-25 05:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8634930-e47a-3b1f-b6ca-5d025990f9e6 | -6.54419 | -58.4704 | 2024-10-25 05:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62529736-61d1-3768-b003-f22aaf92d3c8 | -6.54355 | -58.47436 | 2024-10-25 05:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34cfe532-478c-3713-8c6f-430ac82a4603 | -2.95381 | -58.97818 | 2024-10-25 05:01:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59481920-65c5-3ad5-aca4-8ea6496d116f | -4.32315 | -59.98725 | 2024-10-25 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e104bed9-e2ff-3768-a6ad-b116347197b1 | -4.32235 | -59.99228 | 2024-10-25 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 815f7c58-5907-331d-bd57-bdf4e62573ad | -6.39107 | -59.97542 | 2024-10-25 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c07146bf-2644-3d66-b8c0-015ed6d80100 | -6.7619 | -59.12154 | 2024-10-25 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a889786d-49c7-37a3-b472-3f6a656de7e5 | -6.75829 | -59.12092 | 2024-10-25 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e44fcf16-164e-303f-b250-10e45c14550c | -6.75535 | -59.1161 | 2024-10-25 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2781f8f8-c9f3-3b9d-a711-3eda3738a8e5 | -6.75467 | -59.1203 | 2024-10-25 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d6f1d48-429a-33a3-b014-d32187a770bf | -6.75173 | -59.11549 | 2024-10-25 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53164e3a-acf7-38a6-9fe3-d0cc50face0e | -6.75105 | -59.11972 | 2024-10-25 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9834a1d5-5a4d-39e7-aa38-a87def6d6016 | -6.53137 | -60.03795 | 2024-10-25 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd97f411-9688-3c83-b730-05dfcfdc2712 | -6.52754 | -60.03737 | 2024-10-25 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c34a876-60b6-349e-bfd8-230a372df3ec | -6.52451 | -60.03208 | 2024-10-25 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99bdb786-d4db-31d3-ad35-d98439d9fa94 | -6.52372 | -60.03679 | 2024-10-25 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ca0c0177-f078-31e7-b08c-f90209f37ec5 | -6.52293 | -60.04149 | 2024-10-25 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |


[Clique aqui para ver as próximas entradas](README95.md)
