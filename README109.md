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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f0592b9-6454-36f2-bcc4-2484e02cec4b | -1.43475 | -55.19391 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fb5d4a8-bdd9-3315-a97e-50da01b033f7 | -1.15245 | -53.66289 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 36546a92-040b-3a0d-a5d2-6ca0fe4daeb0 | -2.99582 | -49.2426 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8feb7991-9e5f-334a-bba9-aeacc27a258d | -2.40943 | -48.52685 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 264981e6-a6e5-301d-b07f-3c4a71bf217e | -2.36232 | -54.75819 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| aa507cd5-abbd-30b0-a0b3-09481f410279 | -3.24067 | -50.27078 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 38ce11a6-9564-390e-9a22-c4076141a581 | -2.23643 | -53.66897 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fa5de5d-d874-3ead-b9dd-7dbf9869fe9d | -1.51289 | -52.18295 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ab615d7-08f5-3b83-b21f-9a9f50b5011b | -3.58409 | -51.20648 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1e4f5035-4e62-371a-b54d-99b206f549c3 | -1.59726 | -52.49079 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8e52e58-d61d-3045-badc-89722fcc21b0 | 1.31079 | -50.73135 | 2024-11-09 05:20:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67aa9c5c-866e-3c4a-a774-e36f5a2de84e | -2.97634 | -47.92987 | 2024-11-09 05:20:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb31bae6-6648-37cf-9ba5-05acca952f99 | -3.74421 | -50.17913 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 013f303e-e90f-358a-bd09-c6b204644a11 | -3.01217 | -53.44464 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4971d3d6-4656-367a-82bb-fd40975816d7 | -2.61212 | -51.75392 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 996f718c-d402-3f66-b77f-0d567092035a | -1.14974 | -53.65193 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8aa3b256-c6a8-35d3-bddb-7b466ef51d72 | -1.51759 | -52.18367 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| abe7b964-c8a8-344b-9731-91ebb2b6841c | -4.40013 | -49.41127 | 2024-11-09 05:20:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14ac5ea5-5e7c-34e4-9c53-174a85491a6b | -5.31235 | -50.70523 | 2024-11-09 05:20:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bce8050-f8f5-365b-a76e-d2867dc86aa7 | -1.12637 | -54.19025 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 425d1b72-fd47-3686-8da6-3029efb7746a | -3.38606 | -52.35994 | 2024-11-09 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ce8f992-6c0b-3eaa-af74-409fee1d9e9f | -3.12581 | -51.10623 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b75ac9ab-6fb8-37b5-8812-157a6c8df310 | -3.17122 | -51.30935 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f33a4aa-19c6-316b-8bb9-ef256921a14b | -1.75485 | -52.6876 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e9e614e-938b-3b12-ab17-75d513b548c8 | -3.05059 | -50.37894 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b1f1061-30ab-3188-b6b7-0b631e9b2a29 | -3.03566 | -51.53107 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07fe595c-5e0b-350c-a37f-4111bc34d7e5 | -3.15065 | -51.12703 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 163d2c1a-c794-3dfe-bb9d-8adde084db9d | -4.60707 | -49.58181 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4843da49-63f4-370d-8935-6ab240064b96 | -3.58864 | -50.24464 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fb5a88c-6247-3043-9844-e10c8aa24e86 | -3.89386 | -50.08126 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0447bc26-0bbf-397f-8c37-442e340c127f | -2.85303 | -48.45295 | 2024-11-09 05:20:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bbd7efb-5a24-39f7-8adc-4d6c2ba33aee | -3.80729 | -52.02325 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8819cdb-c2f8-301b-9450-74590fae0e8e | -3.75026 | -52.10489 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b82cd26-516f-3e87-ad63-965a3c6ef2f8 | -3.59423 | -47.35283 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| f7c201bd-8135-34fe-a872-516f58bf135c | -2.87487 | -51.30909 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ff61b6f-15bf-3f76-add6-7145649349f1 | -2.84087 | -51.81094 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fed58185-0a22-373a-8217-8e1e762c51c2 | -1.68707 | -54.25517 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5764ed84-012b-37ca-b983-59406aa5d42b | -3.88003 | -53.39071 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f40d9448-ccad-32ed-a427-fc08ae82cedb | -2.0465 | -52.08588 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf3c328e-38ae-3d3f-9cc6-446cde98d07d | -1.14075 | -53.65413 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 875a3f94-5374-302b-8d45-315502fecc2e | -2.60371 | -48.19748 | 2024-11-09 05:20:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0300ae5-fb65-397e-9a0f-8ae1ceddbb7d | 3.18112 | -64.20265 | 2024-11-09 05:20:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6257057c-2a7c-3a36-9dcb-1a83800c4472 | -3.09176 | -51.29642 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5897fb60-a8dd-3452-ad0f-d2c4825b416d | -3.03443 | -50.36525 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53ea0556-f461-39ec-815f-64dcdaf2c9b2 | -3.97964 | -49.89291 | 2024-11-09 05:20:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ac01349-938e-3383-8cb8-e0b8cf56561a | -2.62548 | -51.914 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55364610-3203-30af-86fc-de43eb328284 | -2.92265 | -51.67017 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53a0c2d5-7de3-3199-bf27-4fce1cc939ab | -2.23417 | -53.77113 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 4dec0dc2-2a10-3cf7-bc2c-3e97e833a70c | -2.95544 | -53.72541 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f0a263a-44cc-3496-9968-47fff7da2c6d | -2.93419 | -51.05807 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1c5dd44-17b5-3265-9007-f129557a73ae | -3.39937 | -53.80682 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0a96e4e-3064-363f-897e-1498bb0bb7dd | -2.61455 | -51.75065 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0141f26-3d3c-335e-b3c9-d7129d4aa429 | -3.02272 | -51.19537 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 144bdf98-e64d-3b41-a765-4c36d9c963c6 | -4.89325 | -48.61724 | 2024-11-09 05:20:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9eeb7680-a9f2-320d-aa3d-6b4e7fd0685d | -1.18681 | -53.66401 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab616509-6f9b-3352-a22d-457de7d38dce | -3.27211 | -51.06496 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 404bf88d-24d9-3592-bde8-d07a169abea9 | -2.87572 | -50.41298 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b8a2d4f-df1e-3b32-ab05-87037ac1745f | -2.1553 | -53.69453 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e039b95d-1906-35ff-b595-5fa1ffd28e08 | -3.75182 | -52.09408 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b651e4d-2743-35f7-b466-279e293453f4 | -2.24562 | -53.66623 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4179d373-b86a-3846-8c94-f02cf238d994 | -2.88084 | -51.46913 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03b95545-e275-3a67-ac0e-15b18a079324 | -3.14238 | -52.97063 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3aa40338-544c-3848-97de-50f5b7cf49d8 | -2.97292 | -47.9243 | 2024-11-09 05:20:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 97dd986a-e8e6-3a7e-ac42-e9a5461b48d8 | -3.45843 | -54.53556 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 777b8176-6c1b-3986-9f8c-cc8e83b604ea | -2.41027 | -50.31117 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dffca26e-d698-359a-8856-8bec7ce54ea7 | -3.28858 | -53.24947 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae3daf01-e0ac-3cf5-9e6a-766a0ad44942 | -3.10913 | -51.35407 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e175c838-3b70-3f43-9f4d-ac9480ec4872 | -2.76259 | -53.22009 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9a64449-862b-34eb-a1c2-0748b2fc2710 | -1.0441 | -52.45795 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62cc36d1-15b7-3bc3-b9f3-02bd1bce626b | -1.48083 | -51.75007 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c225fc99-41f4-3843-b5f8-ce1f34da85c2 | -3.27897 | -53.67277 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e60ade30-ba8a-306c-b8a4-364e2ff4ea01 | -3.09236 | -51.11702 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4295279d-ede4-33ea-9eac-cae1de6a9f3f | -3.03626 | -50.3625 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b65ef893-5317-3069-9f50-7950d65b7c5d | -2.62488 | -51.29963 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3425257-7eaf-3365-a5d1-559c5cfdc18f | -3.60557 | -48.92153 | 2024-11-09 05:20:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5872f149-f3e9-3e38-923e-6506a2c7bf0d | -3.63087 | -50.18274 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3143849e-a035-3f68-bc0b-6d443adafc14 | -2.41065 | -48.84377 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f999eed2-f17f-3c26-97cd-bf898d81da5a | -4.07935 | -49.29189 | 2024-11-09 05:20:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67992d3b-dab0-3533-a7f2-64f2406a6584 | -2.40675 | -50.3113 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e69d202-edaf-3c95-9b01-6edf3d9e1cda | -3.76838 | -51.76698 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a51926c0-cf2d-3fc4-b644-45e744332e56 | -3.02504 | -51.09827 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da797c17-3e3a-3b65-95e4-c10ae87d36e1 | -1.77726 | -52.35068 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 435ccad2-3edd-33d8-a27c-92a0cacf1e50 | -3.44749 | -52.72427 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b44d07c2-3be4-3c64-a169-490af700636a | -2.19579 | -53.63073 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d6f148d-f547-31fb-a45f-91996bb3d757 | -2.9888 | -60.98418 | 2024-11-09 05:20:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b0d95f3-7eb4-3b7a-bacf-e5c165e3e28d | -1.18983 | -51.98932 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c73427b5-be9a-378f-92de-945dd5b739c2 | -3.23536 | -50.45448 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6400b18c-f70f-3cd3-9195-7eb750a2135e | -3.17678 | -51.30713 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48070966-2988-3f0c-b297-f556db1590da | -2.45982 | -50.40025 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c0b5521-dad0-31ef-ae04-cf8a56859449 | -2.47623 | -54.05395 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e0215e8-550a-36d8-87c5-a0bbb0aec6a0 | -3.11265 | -50.14676 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b266e329-cc53-30ed-b3f9-3946b1c8fec2 | -3.02793 | -51.00904 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7121b65-3168-3b9d-a87e-bf1b03021ef3 | -3.23588 | -50.45107 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5095069-8544-3138-9349-162d1ad69911 | -1.14428 | -53.65907 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0a3e3a93-23ba-3679-8c04-e0a11acf418d | -2.39771 | -53.86421 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50a2caac-fe07-338b-b8e5-12647e7c9ded | -1.18432 | -51.99371 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8d20a84-67e4-3c49-ad3d-c6479d1b36c6 | -2.80754 | -54.01148 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c89fe3ec-5c7d-31ae-9524-20ff7c9f0848 | 3.18602 | -64.20634 | 2024-11-09 05:20:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cf1a149-e5f0-3373-a157-24d1ea986506 | -2.68825 | -51.82939 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2a5081b-510d-389c-aa68-709f9902218a | -2.91314 | -49.36249 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README110.md)
