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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8a9d2f2-9d43-3005-a10e-b8b2bef558b4 | -6.5249 | -60.051899 | 2024-10-10 01:06:57 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 113690e7-620a-344e-a35b-2364ff477aa5 | -6.5113 | -60.036301 | 2024-10-10 01:06:57 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e46de43-48e8-36f2-a99e-59f87a0975d2 | -6.5132 | -60.045101 | 2024-10-10 01:06:57 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 307edc2f-a68d-34fa-a5d0-413a984afb09 | -6.5151 | -60.054001 | 2024-10-10 01:06:57 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 724c6460-6f12-3e78-a27e-1ab5a4a7f912 | -3.7064 | -48.3256 | 2024-10-10 01:06:59 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 486f86aa-c2ed-348a-9f3f-1b1b75d9cc5d | -4.1507 | -51.030102 | 2024-10-10 01:07:02 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88737466-c73d-3039-8a66-cb43e3388af0 | -4.1325 | -51.084099 | 2024-10-10 01:07:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca495b9-e4a6-39a6-bf13-66fcf37a7e55 | -5.2722 | -56.077702 | 2024-10-10 01:07:03 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da5e1d08-669e-3f31-8ca0-7bf93c391ade | -4.081 | -50.996201 | 2024-10-10 01:07:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4035cb54-808e-3ea4-8ad4-3deea3dbaf37 | -4.0838 | -51.008099 | 2024-10-10 01:07:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 935e3587-46c8-3571-bcd7-ced1abdf5f27 | -4.0866 | -51.02 | 2024-10-10 01:07:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebadc5d5-f31b-30f4-884a-aa057196ab86 | -4.0713 | -50.998501 | 2024-10-10 01:07:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92ea1eee-0619-362c-8e0b-0d26af01b873 | -4.0741 | -51.010399 | 2024-10-10 01:07:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99e30db5-8c93-35c8-90af-e537ca257947 | -4.0769 | -51.022301 | 2024-10-10 01:07:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8763323-6dee-3230-bd8d-823033ef4de6 | -5.1962 | -56.015202 | 2024-10-10 01:07:04 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c529a160-c6a1-3ed8-8c02-1acf4b2731b0 | -5.1978 | -56.022099 | 2024-10-10 01:07:04 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e46eb6a-1cba-30db-8205-b2489b7313e9 | -5.4102 | -57.148201 | 2024-10-10 01:07:05 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 041c60c5-4aa7-3297-b3cd-ac2f939034d8 | -5.1311 | -56.000801 | 2024-10-10 01:07:05 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa30e7c6-8323-3182-bbca-47cdf0a58d40 | -5.1197 | -55.996101 | 2024-10-10 01:07:05 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94d057f8-c09f-3a92-8b4b-81ec4ee651d1 | -5.1213 | -56.002998 | 2024-10-10 01:07:05 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbd692d1-973f-3b1b-974d-3e143c5b8bfc | -5.1076 | -56.215599 | 2024-10-10 01:07:06 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93075e56-9204-391d-abfe-cc3cd642a463 | -5.1091 | -56.2225 | 2024-10-10 01:07:06 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1212abd3-7856-3099-ade7-93ab3978293c | -5.0668 | -56.217499 | 2024-10-10 01:07:07 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a863cea6-347f-3cc1-a7da-bb757a730e3a | -5.0683 | -56.2244 | 2024-10-10 01:07:07 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 695bbbc7-f647-3ee9-a865-dd604fb8423d | -3.8394 | -51.238201 | 2024-10-10 01:07:08 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44bc7de5-2ae4-34b7-9531-ea7ee6e67e71 | -3.8421 | -51.249802 | 2024-10-10 01:07:08 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46a092a4-78b9-31f0-9cac-a938086521f6 | -3.8297 | -51.240501 | 2024-10-10 01:07:08 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4011e10-7d5d-3e03-ad85-f99b5c2d0946 | -3.8324 | -51.252102 | 2024-10-10 01:07:08 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7df6a29c-4b33-3f6d-9320-8a09227e93b7 | -4.8263 | -55.792702 | 2024-10-10 01:07:09 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44a833cc-6103-35a0-a15b-e31815de72bb | -4.8279 | -55.799599 | 2024-10-10 01:07:09 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9a61f1c-df53-32b3-bfd4-60f19ae4b9d8 | -4.8507 | -55.9911 | 2024-10-10 01:07:10 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84a4aa09-3fef-3bfe-ab9d-cc0352a0388f | -4.8522 | -55.998001 | 2024-10-10 01:07:10 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e858d45e-2815-3b6e-a3f9-063326e1c0d8 | -3.6728 | -51.053001 | 2024-10-10 01:07:10 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c708b3cd-249d-3c0d-9dc2-7f12ea1079c7 | -3.6756 | -51.064899 | 2024-10-10 01:07:10 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 489ea966-fcba-3fa4-b58c-d6ee5b2b5769 | -3.6742 | -51.1031 | 2024-10-10 01:07:10 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3755c4d1-c0ec-377a-9282-d0bd4a66ff6a | -3.677 | -51.115002 | 2024-10-10 01:07:10 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5354707-ec06-3502-9843-bd8b56b35bee | -3.7917 | -52.4044 | 2024-10-10 01:07:13 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90af5dbe-b4cd-3e5a-8cc8-eca9d6050be2 | -4.5391 | -55.5261 | 2024-10-10 01:07:13 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a62852e5-14df-35f3-8f12-be2dfa063966 | -4.5407 | -55.533199 | 2024-10-10 01:07:13 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3fc6143-5b1b-3c6b-8eaa-f1500b599b26 | -3.793 | -52.3209 | 2024-10-10 01:07:13 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a389070-9054-36fd-b109-0c8f74e0ba8f | -4.6572 | -56.0924 | 2024-10-10 01:07:13 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99d67bc9-d112-34ce-b873-81517e8a2061 | -4.6587 | -56.0993 | 2024-10-10 01:07:13 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ece1ed2-26dc-3365-8d22-b3d5f18bc936 | -3.8015 | -52.402199 | 2024-10-10 01:07:13 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2626206-edef-3a36-b6aa-47adb7dcc7c1 | -3.8038 | -52.411999 | 2024-10-10 01:07:13 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9efbc03f-505a-31c1-898d-0eadb053b950 | -4.0807 | -53.611301 | 2024-10-10 01:07:13 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7415e8f-e82d-319a-b46f-8fd681bafb14 | -3.7251 | -52.294601 | 2024-10-10 01:07:14 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b19b290d-e696-33e3-9abc-cfa280237f96 | -3.7274 | -52.3046 | 2024-10-10 01:07:14 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 941e79a4-b05d-31db-8f2e-6493ba517db9 | -3.7297 | -52.314602 | 2024-10-10 01:07:14 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce04663b-1abf-3a93-acf8-7e1f80e7c36b | -3.7372 | -52.302299 | 2024-10-10 01:07:14 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71fab8da-f4a9-33e8-957b-951ad9ac9541 | -2.9375 | -49.187199 | 2024-10-10 01:07:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44993b3d-78ec-37f6-b233-b43d0ffcecf9 | -2.9413 | -49.203701 | 2024-10-10 01:07:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4ea59c2-2f0c-3c0b-8486-8ae847d90db9 | -2.9568 | -49.269199 | 2024-10-10 01:07:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b93ca368-21a1-3964-adce-ebd1e4b9ec86 | -2.9606 | -49.2855 | 2024-10-10 01:07:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71a220aa-7c36-3d84-94ed-436bb4b78b74 | -2.9839 | -49.515301 | 2024-10-10 01:07:16 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 825f06cb-8f6d-381d-aeb3-76a93bc2fa4c | -2.9742 | -49.517601 | 2024-10-10 01:07:16 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 295ffd15-f221-3a44-963a-d87e3bb22de7 | -2.7338 | -48.669998 | 2024-10-10 01:07:16 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a96778d4-462a-3b00-9cd3-9457fbf177a7 | -2.2764 | -46.951302 | 2024-10-10 01:07:17 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9632aa5-eb7c-366d-81e1-71308140615b | -2.7588 | -49.211399 | 2024-10-10 01:07:18 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 339f33a4-1259-3ad9-8d28-e573d7e81856 | -2.7627 | -49.228001 | 2024-10-10 01:07:18 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce301f0-1d3e-3791-87ee-c83cb2676551 | -5.1751 | -60.260601 | 2024-10-10 01:07:20 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47af604c-9916-3e8e-a866-d20e96b53c78 | -3.4401 | -52.798302 | 2024-10-10 01:07:21 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f52c5cb-15b2-3ba9-96b5-82aa9b65a533 | -3.4423 | -52.807701 | 2024-10-10 01:07:21 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc2cab54-94fe-3573-a79a-f97815adff84 | -3.678 | -54.056099 | 2024-10-10 01:07:21 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 022dc613-ec9f-3e0e-9343-d32c6522d8ff | -3.4954 | -53.440201 | 2024-10-10 01:07:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac519aa8-6f41-3f25-88f1-fca4b94307a1 | -3.6216 | -54.035 | 2024-10-10 01:07:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a32db65-d676-3a39-84d0-42de040b0b64 | -3.6235 | -54.043098 | 2024-10-10 01:07:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7fba0fe-e5f7-386b-b5f9-a0c640d6d01e | -2.5923 | -49.769001 | 2024-10-10 01:07:23 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 085d671a-44ce-377f-8cd7-8f6a641e6421 | -2.5958 | -49.784199 | 2024-10-10 01:07:23 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e0c84b0-9ca6-3ac5-a519-e0d240cf5845 | -2.5861 | -49.786499 | 2024-10-10 01:07:23 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 394961f5-1442-35d1-a828-12c98fb76e36 | -3.3269 | -53.200699 | 2024-10-10 01:07:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f36120d-efa5-32fc-88b3-47fe19c247db | -3.329 | -53.209599 | 2024-10-10 01:07:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc6a87a3-b950-348f-a309-48270a69cf86 | -3.3311 | -53.218498 | 2024-10-10 01:07:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7fdc92e-50a9-3881-aa10-9b8b92c4d496 | -3.3192 | -53.2118 | 2024-10-10 01:07:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb407cb8-8346-3a12-9155-5e31f71f7569 | -3.3213 | -53.220699 | 2024-10-10 01:07:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c439aed-470b-3055-b919-80f02755d760 | -3.5561 | -54.334 | 2024-10-10 01:07:24 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beadb2a2-f05f-338c-9ba5-d6aacbee7a74 | -3.5579 | -54.3419 | 2024-10-10 01:07:24 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d8b3db3-9adf-3c4e-835d-c7f916777970 | -3.2276 | -53.260899 | 2024-10-10 01:07:26 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb71a43-089c-3f81-a0d3-b5229d5dfb56 | -2.8096 | -51.5844 | 2024-10-10 01:07:26 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc377ae1-547c-36cd-82d8-9afbcfc21d09 | -2.4647 | -50.2328 | 2024-10-10 01:07:27 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9d0fe4-058a-37a2-b84a-201eeaf21c77 | -3.2507 | -54.169701 | 2024-10-10 01:07:29 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91280c13-dbaa-3b81-bec0-caf1c1f10f50 | -3.2525 | -54.1777 | 2024-10-10 01:07:29 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6612061f-92a9-3bbb-a8b8-d67b09608a79 | -3.2543 | -54.185699 | 2024-10-10 01:07:29 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52b23372-9315-301c-9c25-2c10f4b37aa7 | -3.1274 | -53.7216 | 2024-10-10 01:07:29 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 840054dd-53fb-3a81-a813-267b6622d6dc | -3.1293 | -53.730099 | 2024-10-10 01:07:29 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3151341-12f7-3a38-9df4-8e7698e1f3fa | -4.7172 | -60.791801 | 2024-10-10 01:07:29 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21facad6-57a0-395d-84e6-7ae14b3a58aa | -3.1176 | -53.723801 | 2024-10-10 01:07:29 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d67bf7e0-527a-368e-a70b-59e20b633f88 | -3.1195 | -53.7323 | 2024-10-10 01:07:29 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 059c50bd-0aad-3607-83e2-eb0d2b03271c | -2.8544 | -52.891998 | 2024-10-10 01:07:30 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4323952-0473-3eb6-86d1-e32a8b0dd7c5 | -2.8566 | -52.901402 | 2024-10-10 01:07:30 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bdeec19-9f85-3906-9ee6-7cb0367f52c5 | -2.8446 | -52.894299 | 2024-10-10 01:07:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e066a3-ba97-3fb0-9491-3d743c4ce2b2 | -2.8468 | -52.903702 | 2024-10-10 01:07:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87f7b2bc-4064-31ae-9752-1f9df385f396 | -2.8348 | -52.8965 | 2024-10-10 01:07:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fcb8e7c-2092-30f9-a8b5-7565ca8acec1 | -2.837 | -52.905899 | 2024-10-10 01:07:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20906cf3-459c-348c-b218-6743796304ae | -2.8392 | -52.915298 | 2024-10-10 01:07:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1198f8a6-1f5b-310a-bc18-2bd7db278e69 | -2.8413 | -52.924702 | 2024-10-10 01:07:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0098779-e0a8-30ac-9325-5189e0585bc4 | -2.8435 | -52.9342 | 2024-10-10 01:07:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f87a3b9-537a-39fc-ae8b-84d469f7fe0e | -2.8316 | -52.926899 | 2024-10-10 01:07:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 845b36c7-2c89-3345-a6da-cb4b00b55bb4 | -2.8305 | -52.966702 | 2024-10-10 01:07:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44b79772-c876-37b4-8d18-2b7d47159b32 | -3.0115 | -53.8451 | 2024-10-10 01:07:31 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee497e5b-41d1-3c08-bb7c-12774071e82a | -3.0134 | -53.853401 | 2024-10-10 01:07:31 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README27.md)
