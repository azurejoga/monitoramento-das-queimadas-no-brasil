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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c621d18-f851-3ed3-8e53-c6e5991598d7 | -11.12142 | -59.12404 | 2026-10-01 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 221d7a34-6b20-36b9-987f-98bfe583244d | -20.19156 | -50.90056 | 2026-10-01 05:23:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 21554d7d-c785-3289-9985-5ebf72f21fbf | -20.18557 | -50.89966 | 2026-10-01 05:23:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5728cda7-6af6-3d3f-b5bb-b85a5195e7d1 | -5.11828 | -56.0166 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13905bf8-2697-3cd4-8dbd-571d5f7fe010 | 2.08503 | -50.73848 | 2026-10-01 05:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3cae1fa-ab0e-38da-8797-6453860b3aff | -6.08235 | -56.47326 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ee5da3d-4dd9-379d-b2a9-2b54008359f0 | -1.81626 | -57.10513 | 2026-10-01 05:53:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8f137a8-7271-3cef-960b-14a6aab5bf1d | -7.54842 | -55.0405 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34098f10-7947-3360-a8c9-a06692e5d99a | -5.97446 | -55.37188 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8be17a9-2445-32cf-a973-67c20208c1b1 | -6.6833 | -58.8644 | 2026-10-01 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2db0b945-7eff-3b1f-87da-33181fb0dd37 | -6.05706 | -59.92176 | 2026-10-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 511b8881-6f60-3b1f-a906-f73e539ca10d | -6.68268 | -58.86879 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e68530d3-e9c0-3f3d-97db-be263413f465 | 1.81612 | -55.61767 | 2026-10-01 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6399aa03-fcf6-32fe-aed3-9817f235f925 | 1.87841 | -55.64559 | 2026-10-01 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5438e2ba-d105-329d-a6d1-e7d78a6da46b | 1.71874 | -55.92231 | 2026-10-01 05:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a589dfe-89b4-3f7c-8dcf-661778472217 | -5.86142 | -57.75652 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 748c6eb0-c8b9-3281-9352-fc6a2ab5f134 | -5.12542 | -56.00478 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8f70fd81-8b32-3b74-b690-35ffb69818b1 | -6.51286 | -55.88063 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb5d921e-49a2-32be-af2e-38a3e1a6b802 | -2.99627 | -51.02753 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 898aac0a-b809-3429-b4fb-f1bf9758f8db | -3.37905 | -50.93985 | 2026-10-01 05:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 254f9374-d6e9-34e4-8571-4782bd058b93 | -2.89717 | -54.14444 | 2026-10-01 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9fbaa680-6bb9-39c6-91ce-745906746dda | -2.91003 | -51.32122 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5be26d52-1c78-3fa3-b352-25fb14028972 | -7.71156 | -54.7942 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5913f87f-ef10-3241-8939-b4dda1d8e854 | -6.74196 | -55.60022 | 2026-10-01 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5cccabf-7281-3e73-82b3-fc51f494d1eb | -5.12453 | -56.01088 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74995f41-4ee5-38dd-9074-7192adb9af00 | -7.55154 | -55.03086 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90c1defb-208a-3710-a7b5-3998074850be | -6.74248 | -55.59649 | 2026-10-01 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835b04b1-9fc2-352e-ab12-73ee498fa08d | -2.89937 | -54.09245 | 2026-10-01 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7a917d0-7316-3315-8f7b-5788e54487b7 | -7.55096 | -55.03495 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 465e267d-0ce3-329a-bc95-e7af42395ccb | -6.54168 | -55.28326 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4760fb45-a20e-3320-97ce-7020d45194b5 | -6.67822 | -58.86814 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0263a6eb-f9bf-380d-8399-7aba1f36093c | 2.54137 | -60.60979 | 2026-10-01 05:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e252abe-0136-369f-9a91-8b009dae4a05 | -6.05651 | -59.92541 | 2026-10-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef40a5a8-4593-3402-af36-dfaa29d2b736 | -7.72941 | -54.79694 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4111c58b-a11e-3bbc-a915-7ccb6e9e383a | -2.98219 | -51.02534 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d7f9dc05-4e91-368c-b479-a2d94d7aae5f | -1.83271 | -54.99292 | 2026-10-01 05:53:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a384f12-6aa3-3218-9bb9-7c610d84d29a | -2.0348 | -54.05562 | 2026-10-01 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32eba1ae-21e8-302e-8c39-e2fecfb2fca4 | -7.72464 | -54.78725 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65c96354-da1a-3ad8-9816-9114bb559f9c | -2.55206 | -54.62429 | 2026-10-01 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e1c0e5c-d1b0-3c2d-bf05-ccdf276f7e2b | -1.44706 | -54.46296 | 2026-10-01 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42617cb8-b945-3d61-9286-e810d777b0f8 | -2.97415 | -51.03098 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bb30ed9-651d-3995-ade3-91cd8287eb9e | -6.67252 | -58.87629 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82fd6457-c808-30cd-bd0c-d929cb22669d | -6.68472 | -58.86678 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95b2710f-c80b-34dc-97a4-0607d0a71727 | -7.72883 | -54.80125 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98e34f70-e2a9-3d91-8863-2fa77d658467 | -7.71634 | -54.80385 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df6b6347-a744-3141-9eba-e5f0e34f640f | -7.4923 | -54.98351 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2eb87c43-24a0-32ba-848a-9148a19b70e4 | -2.90439 | -54.09551 | 2026-10-01 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a43eb14-dda7-3988-9d08-ebc5e3f9b86c | -1.63609 | -55.13033 | 2026-10-01 05:53:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e2f3cd0-49a9-3403-b12f-6a0917aeb987 | -7.3464 | -55.59032 | 2026-10-01 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e000d2e1-9781-39de-8b72-94c0d8db4830 | -6.65537 | -58.88041 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71fd4e99-d62a-360d-b751-5f1eb00ccfd8 | -7.70034 | -55.05716 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4edb474f-25ce-3f9e-829c-7e4087584769 | -2.89777 | -54.14038 | 2026-10-01 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 056fe82f-b22b-3b3f-b664-553e81ca5e3d | -2.91171 | -51.30825 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 819399b2-adf4-33f2-a3dd-fc2ce6384f37 | -5.86664 | -57.75323 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02fcaec3-d38b-36ea-b01d-639c7522d7e9 | -5.86331 | -53.4847 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a4ce8e7-5a4e-3984-9295-0304a1ba371a | -7.54897 | -55.03632 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e624cdce-206d-3355-8b74-c11ebb89bee5 | -6.66558 | -58.87296 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a6da4b07-02b7-3a58-8e16-25467865be49 | -6.6984 | -55.05632 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de3f3b14-d35f-3ca5-ad93-f4fd49dac7ef | -7.49595 | -55.00069 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e042b9f-d58c-3128-8649-57ce3a89d0b4 | -7.69906 | -54.79688 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef1daabb-db08-3ef0-b57d-97a68df5af00 | -2.98119 | -51.0321 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 89f61c9d-f87e-3518-813e-e2e750390845 | 1.87666 | -55.63498 | 2026-10-01 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c2d12b4-5fcb-3552-ab19-855ccce66200 | -2.96713 | -51.02985 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53326deb-d65c-3f50-8665-decb7a07e26e | -5.1201 | -56.00413 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5652c2a-6435-373c-9dba-15030f13b37e | -2.90982 | -51.3211 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 298c097d-e6d2-39ac-9439-0dbeadcbc70b | 1.70663 | -55.90847 | 2026-10-01 05:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d943edf-cd9e-31e2-886f-2148b7c70200 | -7.7348 | -54.80206 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4c0bd753-d54e-30d9-b12a-d35954f761bb | -1.44383 | -54.45958 | 2026-10-01 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b03bb7bb-d403-3705-9c8d-031617c2032c | -7.49116 | -54.99194 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0504773b-f700-34c5-864e-209456f9685b | -5.30068 | -56.00555 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 121bb581-cf14-313b-8dd2-2f51a9cf1dc7 | -6.11293 | -55.69614 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2852432f-40bc-3c03-8c36-f941d3fad8a5 | 1.87351 | -55.64624 | 2026-10-01 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dcd09102-3f51-38b9-bba3-0de47785fa45 | -3.00846 | -51.06964 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a06ff9ed-31a0-3308-94d5-0a05b9986856 | -3.38026 | -50.95462 | 2026-10-01 05:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e36f487c-82ee-3cbe-bcdb-b8a491925b7e | -6.51237 | -55.88417 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 596efe26-553c-3149-a39d-9f76124b377a | -7.3425 | -55.59483 | 2026-10-01 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 889b7c3b-1c0d-3d69-a997-827e2b1e8e67 | -6.13241 | -53.26887 | 2026-10-01 05:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75d4019a-d046-37c4-b761-48b812f42f28 | -6.67894 | -58.87493 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5fb2b4ed-28d6-3865-8061-c56d29a64ebc | -5.86482 | -53.49031 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d705917d-c6c9-37af-b0f1-d1212a44528a | 3.28186 | -60.61372 | 2026-10-01 05:53:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24c82429-ed1d-39eb-b056-f9f3ba8858cb | -1.83323 | -54.98954 | 2026-10-01 05:53:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a9e2dba-36cd-3699-b138-765b582650d5 | -6.66868 | -58.8712 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9771efc9-2195-3364-9e3f-3da67885d407 | -6.08755 | -56.47412 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a03d22c8-9bde-3007-92f7-8ea142607e8b | -2.897 | -54.14616 | 2026-10-01 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 143f71ad-90f1-3a1e-a64e-606ae8b042e5 | -6.69941 | -55.04629 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52362b6d-c71e-394f-8e92-f49d0add28d4 | -5.86591 | -57.75843 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe7e3307-e6d3-3df3-8dbe-c6e4adf89dbf | -5.86064 | -57.76172 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e086bf1-4028-312c-a635-218bf296cc4f | -2.90521 | -54.09328 | 2026-10-01 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03ec6e1e-f56f-380a-872b-ecd6d968f8d0 | -7.69978 | -55.0613 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e31b63c-cdbb-3e69-9774-509798e27da6 | -2.49998 | -56.90546 | 2026-10-01 05:53:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a6ea2790-fec2-36d1-9b55-75d770ec1a81 | -3.38127 | -50.94796 | 2026-10-01 05:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b96c260-7f41-357a-ba12-9c29b37d7016 | -2.90237 | -54.14941 | 2026-10-01 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c1b28a62-0f0e-3fd7-ad9b-597e51af279e | -6.1119 | -55.70344 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7eb2feb-90bb-3d51-a332-19ac88d6ed0c | -7.34195 | -55.59873 | 2026-10-01 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9351d97-4321-3ff0-a5cf-ed46bcb98ded | -6.67003 | -58.87361 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b047b45c-88a9-3a93-83b2-806aae6c4f20 | 1.79119 | -55.6492 | 2026-10-01 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c92ffbd5-62cf-3f1b-9901-5bc8ac360eb9 | -7.49058 | -54.99619 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bf3399d-9b4a-33bb-8e77-0051d7fc7e60 | -6.6776 | -58.87254 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b09e8ff5-0feb-314c-a4ec-a511f0630c11 | 3.27835 | -60.61428 | 2026-10-01 05:53:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 381670cf-e3dd-37eb-85a8-2719c9b1ef61 | -6.13591 | -53.291 | 2026-10-01 05:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README86.md)
