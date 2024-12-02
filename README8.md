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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9143ab93-4e1c-3072-bc32-3a34fdc4ca54 | -0.9614 | -47.795799 | 2024-12-02 00:57:00 | METOP-B | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48c53ee0-1af8-36e1-8e58-e7792000d94f | -3.0319 | -54.0424 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5d9cee0-8df0-3fb9-95e1-adc813145528 | -2.8204 | -54.063301 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f393302-ddcb-35cf-9bf8-02b601f013fd | 3.3859 | -60.513 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d84b652f-784f-3aa5-b3a2-9c4f4fa8ee6d | -2.0231 | -54.314602 | 2024-12-02 00:57:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28c26ce5-9f18-3e9f-8a16-995367d5b879 | -2.5647 | -53.3974 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1ed78f4-8dab-3fc5-9a8a-23f903424344 | -1.3301 | -54.9799 | 2024-12-02 00:57:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67de54f2-8217-34d8-8294-971246a4ee10 | -3.0237 | -54.186501 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74b9fd2c-8fb0-3825-90ca-0f0ad2e20861 | -2.0113 | -54.3083 | 2024-12-02 00:57:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 804eaf53-997e-385c-a96a-108dd225936f | -3.0898 | -53.2188 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 138c5b24-0e78-399b-af1d-612ef0e6adab | -2.7204 | -54.166401 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 900aadb7-fd62-3e69-bc5b-4bf48e6675dd | -3.1044 | -54.043999 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e289a6d7-a690-3f22-a16b-33a1cf55251d | -2.772 | -55.340199 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3e7f7a7-bcde-3894-ad4c-0eecc14e2816 | -2.3438 | -54.366199 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36942d2d-edbe-3927-9e76-f70af5ebc8b7 | -3.0866 | -53.249298 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4d7881c-b2d9-30fc-a4ce-729ddcb2ba63 | 3.3858 | -60.467899 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 658f07f5-ce43-3094-aa5e-e1cf916cf87c | -2.266 | -53.6208 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e47bc3-0beb-3687-a23e-9f6e5c9fa907 | 3.3875 | -60.505798 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d1074bfe-5c34-35f1-a49e-8fd3ec631f89 | -1.7302 | -52.629799 | 2024-12-02 00:57:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46d1cb40-c4dd-3c11-a0dc-5d3dcf71f5b4 | -1.2279 | -51.605 | 2024-12-02 00:57:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abf0c81e-346d-3b43-bdbd-2328338779f1 | -2.9163 | -54.122101 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 901a53cb-e2d9-3a58-afcc-3a10e27f52e4 | -2.6302 | -54.222301 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4774dec6-f175-3849-800a-48b0dd58b1c4 | -3.4176 | -54.017601 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50ac1da1-a330-3a0c-853c-3aee4b691977 | -2.9907 | -52.521301 | 2024-12-02 00:57:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a7e2aa8-a8f5-3c4e-b9ce-667452018455 | -2.0382 | -54.651699 | 2024-12-02 00:57:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a251525b-c4cf-3a0e-a6b4-649729384af8 | -3.0597 | -53.669498 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fdd8880-b43a-3cef-baf6-aea82d2dcd63 | -2.4526 | -53.626801 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e21f95a-36eb-3c14-9acf-17cdaec535f0 | -3.0927 | -54.037701 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b761e2d8-9d3f-387a-9139-6a82df842e1b | -3.4294 | -53.8894 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb68891-4773-36be-947c-106462e0e105 | -3.0942 | -53.237701 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d77a2dfb-cd91-3563-a986-282e5ccb5133 | 3.389 | -60.453602 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9358cb43-1e85-3433-96c2-bdbe29d73897 | 3.3777 | -60.503601 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5fea0bd8-bd53-3adc-89cd-0c69f1246a73 | -2.6268 | -53.353699 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84ec7b15-684b-319e-a957-8b7c00206194 | -3.1793 | -54.326 | 2024-12-02 00:57:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf77a12d-d302-3f50-97c6-9f31015ebee6 | -2.6387 | -53.360901 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c26cc691-e5b3-37e1-a266-10155f9c5858 | -2.2618 | -53.602501 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef476850-44f2-3cf3-9819-fecfb22efff7 | -2.8118 | -53.0397 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78a04254-e4c8-3f9b-bd8d-20d9eea124e0 | 3.3842 | -60.474998 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0bcb7263-19b2-3ac2-a209-109e97b34327 | -2.5353 | -53.403999 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 175d96f0-1058-3c78-b8bf-4809af1d391e | -2.8458 | -54.039501 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 055c59ab-23dc-312a-8f28-81ae68583481 | -3.2513 | -53.6073 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e1d7893-6f83-35a7-9ff1-08166d329382 | -1.0242 | -53.545101 | 2024-12-02 00:57:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68b400fe-7b5c-3a17-acfe-0090f0cbc3b0 | -2.836 | -54.0867 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5dcefda-4f86-3a9f-9739-bd2127233b52 | -2.7835 | -55.3456 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a42d67ad-e8c7-3a34-84f3-e4aef4fdb393 | -2.3632 | -54.8573 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c2011ac-48a4-3c40-982e-b088ea74d67a | -2.8927 | -54.154202 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeec0e08-1e87-3861-9f96-8bc50fc6bf66 | -2.5375 | -53.4133 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c378b375-6321-33b0-8ea4-79abd403b1c6 | -3.0944 | -54.135201 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e167c48a-4c19-3330-85aa-39ea55a516ce | -2.543 | -53.392399 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7424b768-6df6-3b10-9179-dfb072026db5 | -2.8066 | -53.061401 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee97f19-2d47-37b7-90cf-0492d72b5817 | -3.2575 | -53.633999 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 286cafc6-a912-3541-a0ed-5df9b0a35639 | 3.3842 | -60.520199 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 78c89f89-4ec8-3edf-abfc-284b8537aa78 | -3.1751 | -53.633999 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abbc61ba-552f-3b16-ba04-cd22ff8539fc | -2.8952 | -51.576401 | 2024-12-02 00:57:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48624451-ac2a-3320-a8d2-441d7f2c7816 | -1.3959 | -53.6413 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac940313-8835-328c-901a-3439d2cd815a | 3.3809 | -60.4893 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ec3a092b-9531-35f5-895c-9c5b51a9fb09 | -2.3605 | -54.4846 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd4978af-9f6a-35b2-914e-8ce3c4119049 | -1.7325 | -52.774101 | 2024-12-02 00:57:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20378544-5b1a-3adb-9538-88ff7a82ff1e | -2.8495 | -54.190498 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 416d3547-39f9-3832-9899-a2de4c9ab9f8 | -2.6366 | -53.351501 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56469aa7-e7b8-3b71-bc9b-12f7630520e3 | -2.5265 | -54.039299 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7f65c37-d6fd-3e14-aaba-889ea05af3e2 | -2.9748 | -53.883202 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8002b414-46c8-3137-9775-a3bad3baea50 | -2.8635 | -54.0266 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1adf1def-425f-3e29-8396-e0884e756558 | -3.2693 | -53.640701 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2726024b-3551-33e5-99ec-ff48666e3b51 | -3.1117 | -53.8064 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa608b39-8ec6-3783-ac5f-16103a926a84 | -2.7622 | -55.3424 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1bab3b-78d8-3b9f-852f-48c33dc399bb | -2.8047 | -54.039902 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 247f6f41-4f63-3f5d-8acb-5681fb7668c5 | -2.8282 | -54.097401 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 859c1437-fa0f-3f79-8f41-4fd1e4a0e4e2 | -1.3866 | -55.183498 | 2024-12-02 00:57:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59afaf7b-ab6a-3d44-bded-0484de6d017c | -2.8654 | -53.990002 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72e4c781-208a-35d9-a7f1-0a25714c5eb5 | -3.2534 | -53.616199 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53096fc8-b5a0-318a-aa8e-da8ea8f8dc98 | -2.2639 | -53.611698 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9135217-8ac7-31fc-a9b2-5c06487a4b71 | -2.2716 | -53.6003 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7ec5f4d-bf27-3a0c-a7e4-3f36cfa3aded | -2.2541 | -53.613899 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b283bd9-a68e-3b43-a3fd-49c1ccdb958b | 2.4288 | -60.642101 | 2024-12-02 00:57:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2aeb07ed-ab40-3a44-89b7-f67ce4e464a9 | 0.9069 | -59.4431 | 2024-12-02 00:57:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba117a9-67e7-3b07-8799-7496ca95cb03 | -1.9439 | -53.3381 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4e79934-20af-3fa9-ad28-c397c98208b1 | 2.4271 | -60.649502 | 2024-12-02 00:57:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 73d7760b-2a73-35f9-8240-7f51f3860b21 | -2.4187 | -54.018002 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95e6c670-8b2e-3cf2-ba2f-df0eb7bf9b84 | 3.3924 | -60.529499 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac7f976-1a7f-39d0-9a58-89c8fc64d348 | -2.6069 | -54.0755 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d98cefea-6119-32ab-aa63-2f182b85fafc | -2.7616 | -54.121399 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3733ee95-e513-3dc8-bd34-99b691b42161 | -2.8946 | -54.162601 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7bd647d-21fd-335e-948c-f42fccba8ca4 | -2.6342 | -54.194801 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebea4eb0-d50a-3975-83c2-6802d9fc5680 | -3.4275 | -53.880798 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e62c8b37-9d4a-3056-ac3e-002faeca953b | -2.0192 | -54.2976 | 2024-12-02 00:57:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 401e6ebe-2621-3e37-99ef-fd572c909ce3 | -2.8044 | -53.051601 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a968df7-90cf-36c7-98a1-77fdb562ae3c | -3.3306 | -53.3699 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3563790a-3578-3fcf-a106-0721a8c2a682 | -3.092 | -53.228298 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7377aef-c747-3a8d-8f0d-7f591c887325 | -1.5759 | -55.3367 | 2024-12-02 00:57:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c050acbc-d998-3078-91d5-66c9ae677cb3 | -3.2673 | -53.631802 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f12cb43-6a4a-3cb1-8200-56385ead3b1e | -2.8693 | -54.007198 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74005f6a-aba3-365d-9650-16553dfc5a5c | -2.5245 | -54.030602 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a720ceda-d364-39cc-aeb4-75067d0643d0 | -3.2554 | -53.625099 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecb2f99f-9714-3c4a-ae7f-f788b0a2c010 | -1.2725 | -54.544899 | 2024-12-02 00:57:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09e99539-1b91-30b0-b78b-a996eba1c288 | -2.8498 | -54.056702 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5728d7e8-41b2-3c95-a4c5-ad7032c5c267 | -3.2853 | -53.665199 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25c54dc4-0bce-337f-b2fb-9ce6518a05d8 | -2.7923 | -53.044102 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b6bf998-988d-3bd1-94df-4e091b210068 | -2.9826 | -53.872299 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51df39bd-5657-3313-9fc3-f442f8653341 | -2.7737 | -55.347801 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
