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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a3405a3-2c51-314a-9901-d7e0bf0e390e | -8.61449 | -46.49184 | 2024-10-11 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4fa25ee8-b5d2-35c8-aeb4-5305e341c519 | -8.61313 | -46.48239 | 2024-10-11 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 555d8c06-f1c4-319e-8a73-78830b08d8ab | -8.61178 | -46.47298 | 2024-10-11 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 23218924-41fa-3a4c-966c-0b48628103dd | -8.5285 | -46.98907 | 2024-10-11 00:56:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9ea6d48f-8aea-3012-853c-86a5764e7995 | -8.52721 | -46.97994 | 2024-10-11 00:56:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4d81d092-1789-36f0-a720-cae712e7e055 | -7.99476 | -46.86422 | 2024-10-11 00:56:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b652b01c-8065-33f9-abc6-b96f512eea4b | -7.99344 | -46.85501 | 2024-10-11 00:56:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c8d0d169-992b-34a5-b1dd-22b7c67d564a | -7.98443 | -46.85628 | 2024-10-11 00:56:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9e066b68-c6e6-3659-b3b2-e0e019a31e66 | -9.46647 | -47.29703 | 2024-10-11 00:56:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d6950f6f-a885-34ef-8208-c6ef0caeec3b | -9.46521 | -47.28806 | 2024-10-11 00:56:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7e62dc41-709a-3635-9672-e7a19acdf093 | -9.45761 | -47.29831 | 2024-10-11 00:56:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 82146e40-20f0-3246-a3c4-43e2c2ce6fe1 | -9.45635 | -47.28936 | 2024-10-11 00:56:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cb3ff876-1954-39f2-863d-fc3d058d7ba9 | -3.36015 | -46.4926 | 2024-10-11 00:56:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4c5f9abc-19e4-3ae0-ab14-dd782cca8cf0 | -3.30416 | -47.0136 | 2024-10-11 00:56:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f2a06c98-a6c0-33ff-904a-ca5b5d982048 | -3.30162 | -46.08334 | 2024-10-11 00:56:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 262.7 |
| c2fb9472-2344-3a0f-b18f-a0b886111b29 | -3.30003 | -46.07227 | 2024-10-11 00:56:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 37b98a41-b6d7-3357-9b8d-52b309b6fb43 | -3.06718 | -45.94636 | 2024-10-11 00:56:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff27d21a-2a12-360a-81b9-dc2a8786b8be | -2.59031 | -46.12151 | 2024-10-11 00:56:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5f62729e-b34e-34ea-a313-d538dad8f0d9 | -2.54308 | -47.22847 | 2024-10-11 00:56:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 446a71a7-7277-38c1-aaec-63bdf3bbca9c | -2.54169 | -47.21868 | 2024-10-11 00:56:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| de197a55-2fd9-3acd-b871-94d3646721e2 | -2.42926 | -46.21407 | 2024-10-11 00:56:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 86e9c23a-b52e-3017-9a23-e61ad2f01657 | -2.39693 | -46.70879 | 2024-10-11 00:56:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e39ce9ca-5a09-389f-b21d-49e960ca44f6 | -2.35199 | -46.83801 | 2024-10-11 00:56:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 24ed6e25-22f2-389b-8b4e-878473463302 | -2.24528 | -46.73218 | 2024-10-11 00:56:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d194f853-e35a-3e75-b4e1-cbcace1a3c94 | -4.20885 | -46.89276 | 2024-10-11 00:56:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| c6ba0bd9-c714-30c1-9bcb-9d6533280171 | -3.92913 | -46.4691 | 2024-10-11 00:56:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f1558e59-c596-346e-8c8e-ef8f10756f2a | -3.92771 | -46.45905 | 2024-10-11 00:56:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 221.8 |
| 41ac3cb2-2b05-3117-a149-0618d4aa2baa | -3.80546 | -47.48469 | 2024-10-11 00:56:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 0348c990-4c21-3d9a-83bd-c3b7fb0f6238 | -3.70181 | -47.60086 | 2024-10-11 00:56:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| fcfd6df1-6275-322d-b378-7da5320a7901 | -3.7005 | -47.59159 | 2024-10-11 00:56:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0a87192e-2ab6-3040-85d3-e43be590c7e7 | -4.94727 | -47.41187 | 2024-10-11 00:56:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| facd5782-ce3b-349f-b2f7-db9202edb9b5 | -4.94595 | -47.4026 | 2024-10-11 00:56:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9edefcb2-15a5-37a1-b1b5-ee1eaccb451a | -4.91724 | -47.65605 | 2024-10-11 00:56:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1b7515d2-1bed-30bf-b71d-19e1ef740055 | -4.91302 | -46.70795 | 2024-10-11 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d06c4249-4c26-32fe-b7ef-f6187ac9d985 | -4.9037 | -46.70914 | 2024-10-11 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 59f91159-a3bf-34c7-966c-ec83fd30adab | -4.68099 | -46.43672 | 2024-10-11 00:56:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1ba06c92-68a4-33ec-ac99-3a77bbcc75f2 | -4.67153 | -46.43813 | 2024-10-11 00:56:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| defc3c2e-f7e6-37b1-9a6b-4bb7a22a3ed7 | -4.6568 | -47.44354 | 2024-10-11 00:56:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 163e715e-1e7c-3a5f-949d-03e1e0c05dc4 | -4.21025 | -46.90245 | 2024-10-11 00:56:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| caf39747-021c-34ec-8e39-1f39fa726895 | -3.80677 | -47.49405 | 2024-10-11 00:56:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6708cd14-c990-3ee3-b389-0a8096687c2b | -5.64843 | -47.93344 | 2024-10-11 00:56:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| be45e0d8-ccb7-3e1d-8a21-54d5f0037ba4 | -6.12634 | -47.27425 | 2024-10-11 00:56:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 2a8f6a1c-1b72-3b6d-817e-623933146607 | -6.12503 | -47.26506 | 2024-10-11 00:56:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| dbe35854-8e13-3025-a227-43e11e519908 | -5.97401 | -47.11038 | 2024-10-11 00:56:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f7283eb6-d88b-318c-991c-1d759d2e24d2 | -5.67004 | -46.53177 | 2024-10-11 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09b24ffb-681f-36dc-a568-5445a786e828 | -5.64717 | -47.92451 | 2024-10-11 00:56:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 0dee44ed-42c3-340b-9707-ec62cc4f2eab | -5.55564 | -46.69094 | 2024-10-11 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 964be417-9357-347c-af68-e0d7573a7fc2 | -5.52127 | -47.10233 | 2024-10-11 00:56:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e9d61690-8cc6-3341-bb57-a0f81b297bda | -5.30082 | -47.56677 | 2024-10-11 00:56:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6ebbd20f-ea48-3a57-a31b-59d432c3b7e0 | -7.21178 | -47.65007 | 2024-10-11 00:56:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 43e0e45f-eae5-3b11-8c1a-c5b977a740b0 | -6.94252 | -48.16635 | 2024-10-11 00:56:00 | TERRA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a46ab2e-7d01-31af-8043-b574e208339a | -6.93369 | -48.16763 | 2024-10-11 00:56:00 | TERRA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8c726dc8-e15d-32d6-9d02-5b92d7c2d2fe | -6.93314 | -47.76316 | 2024-10-11 00:56:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 923d5dd8-bd10-3e1a-b90e-6a47bb7d7c32 | -6.92051 | -47.73767 | 2024-10-11 00:56:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 39b4dd5b-1758-3921-9862-17f149cbfac2 | -6.91798 | -47.7198 | 2024-10-11 00:56:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 84190ace-a869-3ad2-b36f-dd46102b5ea6 | -7.69021 | -47.25026 | 2024-10-11 00:56:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 35aaddb8-ee31-3143-a8d3-fe1588904b29 | -7.46769 | -47.18033 | 2024-10-11 00:56:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 60c5c66e-8cf8-3202-a1a7-2bfcd35ecd19 | -7.43714 | -47.35133 | 2024-10-11 00:56:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cce8e929-d19c-323d-a880-782e0a4e845e | -7.09571 | -47.87901 | 2024-10-11 00:56:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 569bc04f-8034-30c2-b81a-811230d291e4 | -6.94129 | -48.15751 | 2024-10-11 00:56:00 | TERRA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 6.4 |
| de417921-eb17-3cb5-93c8-6a653b460eec | -6.93188 | -47.75423 | 2024-10-11 00:56:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| e8f3e70f-1d43-3bb5-94af-f1896858dff7 | -6.93063 | -47.74533 | 2024-10-11 00:56:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 9a53a6be-96ed-34eb-84d1-39bd14b33ac9 | -6.92937 | -47.73642 | 2024-10-11 00:56:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ed16c222-afa4-3e24-92cd-e42aa3ca454d | -6.92428 | -47.76442 | 2024-10-11 00:56:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 839c8184-d89e-32d5-b3d4-2697951094bc | -6.92302 | -47.7555 | 2024-10-11 00:56:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 193.9 |
| a5898107-56fb-3789-b4c1-e7a3d32d07b2 | -6.92177 | -47.74662 | 2024-10-11 00:56:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| a1550e89-143a-3566-85d8-e14a7bfbdf52 | -6.91924 | -47.72872 | 2024-10-11 00:56:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 0a9b40dc-8a8a-323b-b955-2ad28d9b3dc6 | -9.16769 | -47.60189 | 2024-10-11 00:56:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 72b17d31-8b1b-33a5-92f0-1e8622b24462 | -9.11207 | -47.65541 | 2024-10-11 00:56:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 68feb08f-0e3b-3db3-9eec-06d2269da586 | -9.09636 | -47.94528 | 2024-10-11 00:56:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| ff7a65a5-2961-3a2a-b4ae-d7f12c30362f | -9.09513 | -47.93638 | 2024-10-11 00:56:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 00730bd7-b6d4-3fa3-94c8-47c2be238d0e | -9.04271 | -47.68991 | 2024-10-11 00:56:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 267ba984-e798-33e6-9eae-0f034de6282c | -8.99357 | -47.73928 | 2024-10-11 00:56:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d93e5494-c5a7-3491-92af-18cc40b249d3 | -8.94497 | -47.19921 | 2024-10-11 00:56:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8249b8b2-b693-33af-947b-baecd8646bcb | -8.91754 | -47.91983 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f21b31db-9a1e-3e1a-8192-228124435c49 | -8.55366 | -47.82455 | 2024-10-11 00:56:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bfc5e147-fc17-3f19-bd26-1f6bf05726d1 | -8.54269 | -47.21827 | 2024-10-11 00:56:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3fff8248-9a5f-3adf-ab76-a073d8dfd56e | -9.21804 | -47.56138 | 2024-10-11 00:56:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4ad4390-3d3a-35c6-8dad-23e2408af193 | -9.16679 | -47.9832 | 2024-10-11 00:56:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c449ddd4-c7ff-3d7b-b34a-2e2b1d9b43b6 | -9.07856 | -48.48191 | 2024-10-11 00:56:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b4afc286-5169-3dea-8246-b4e409626039 | -9.04245 | -47.817 | 2024-10-11 00:56:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a3681f5f-cd92-3342-bf86-f643a3ffe480 | -9.04146 | -47.68101 | 2024-10-11 00:56:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3feb788f-1401-396d-882d-25a24cb3c1f1 | -8.9163 | -47.91094 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 06990246-c447-318e-8e40-3233bb7a0e7e | -8.86656 | -47.55512 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3a19ad3e-cd79-3f6a-8cb8-9460e278698a | -9.82041 | -48.04673 | 2024-10-11 00:56:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e9f70bc6-4401-30a8-8543-ea5b29d48e5a | -9.65098 | -47.82849 | 2024-10-11 00:56:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 48b8fe8d-aec1-3e08-8e81-e1c7c60c7a46 | -10.31286 | -48.89011 | 2024-10-11 00:56:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c91474bd-2971-3e8d-b223-50247b5e8ca0 | -10.01247 | -48.8459 | 2024-10-11 00:56:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7f068139-6acb-3268-a7b4-68968eefafbc | -10.00395 | -48.8534 | 2024-10-11 00:56:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4c5b8e2d-6c99-3274-8569-d11d9df4e8b1 | -10.00268 | -48.84415 | 2024-10-11 00:56:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 234c77f1-2aa4-36c2-9d89-aa46156ffa7c | -2.88076 | -48.91108 | 2024-10-11 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ee14979d-7a16-3c3b-9c1d-f6036b00cddb | -2.87953 | -48.90228 | 2024-10-11 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b7c6c946-c36b-30ab-a4e8-105bf681e90b | -2.8539 | -48.65409 | 2024-10-11 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cb21c595-d0f7-3896-b0e0-b45e79adb63f | -2.80698 | -48.70582 | 2024-10-11 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 2ee42def-f97c-3d59-b604-be7e0a2e2d4f | -2.80574 | -48.69699 | 2024-10-11 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5092f221-db1f-301d-a330-725ad97ebbc3 | -2.74785 | -48.68449 | 2024-10-11 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9cd1feff-15d3-3057-94ac-c7a9b07ead44 | -2.69397 | -48.63483 | 2024-10-11 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fa019f80-2148-3869-94bb-4d4e9b1bfab5 | -3.70443 | -47.61938 | 2024-10-11 00:56:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e41be23c-ede3-3b8c-9e2f-a52dbcae59f1 | -2.97473 | -48.00317 | 2024-10-11 00:56:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| cb0a7280-0753-37c9-a629-5d37ca3bec09 | -2.97346 | -47.99404 | 2024-10-11 00:56:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |


[Clique aqui para ver as próximas entradas](README17.md)
