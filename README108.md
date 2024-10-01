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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d8d75e3-fba1-3239-9548-69f350bc3144 | -12.14163 | -50.05396 | 2024-10-01 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f8967032-285f-3402-ad87-680751a0b83a | -12.141 | -50.05873 | 2024-10-01 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 160e7d0c-0ed9-36b9-ac9a-810b1e173628 | -13.22814 | -51.20861 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 53256ac1-4893-3530-b008-95c27925c371 | -13.2276 | -51.21281 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 154d8b8c-d82c-361a-92f7-0e9ca08999eb | -13.2233 | -51.21219 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1a991830-6cb3-3b2e-8ab9-19dbc5a7276c | -13.219 | -51.21158 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 25bbbcb7-3fb9-3187-b2e9-1cb16740c6da | -13.21655 | -51.20927 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 76d54b22-4526-3aba-9933-ae2a0fa62726 | -13.21598 | -51.21344 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d27b1bbb-89ca-3261-b9c8-f06eef0a0835 | -13.2147 | -51.21095 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 3bf1c6ee-bc4f-343a-ab44-644715a6a9b5 | -13.21168 | -51.21283 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 64f88922-464f-3bb0-b0bd-891556cfb72c | -13.2104 | -51.21033 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 28ccccd2-269f-30da-b60d-5b54e1eb776a | -13.20739 | -51.21222 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8b24508-04b2-3eb8-9f63-e515d79c4861 | -12.40109 | -50.97693 | 2024-10-01 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4dc120dc-bc73-3d8f-812a-fbfc446f0657 | -12.28283 | -50.64634 | 2024-10-01 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efdc688c-41e9-33e6-b420-eeac67229571 | -12.54512 | -50.62746 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb172f31-fc6e-327d-b863-483b69f7cead | -12.41625 | -50.96202 | 2024-10-01 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 954201d5-473f-3325-8e60-6a7576917866 | -12.41193 | -50.9614 | 2024-10-01 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0cb36bb-e1d8-34db-9f26-73428c986dfd | -12.41138 | -50.9656 | 2024-10-01 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f8057b5-6af7-36d9-bb1d-d703acbc1187 | -12.40164 | -50.97274 | 2024-10-01 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84c4a6ea-a8fb-32da-ae07-b0aba5ee7a00 | -12.30691 | -50.43186 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b13b14a3-5c3d-33f2-9ef5-1549e4dd5cc5 | -12.27711 | -50.45068 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85f6b5c3-24c2-3337-a374-fc5f963c4cb2 | -13.64987 | -50.35363 | 2024-10-01 05:06:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36ad5046-e647-394a-bb05-52332a7458f0 | -13.64977 | -50.35505 | 2024-10-01 05:06:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57a2e80f-4e45-39fd-b438-e427e9a3e2cf | -13.64639 | -50.34466 | 2024-10-01 05:06:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5de3d16b-c266-3c78-a2a6-24a0da8258fb | -13.64592 | -50.34812 | 2024-10-01 05:06:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab9179d2-8564-3514-96a7-6736ac50491c | -13.64578 | -50.34953 | 2024-10-01 05:06:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34b09360-ce18-38ae-b463-db59566a88c9 | -13.64529 | -50.35298 | 2024-10-01 05:06:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f266ce9-61b1-36c5-a26e-a5a13f61fc89 | -13.64198 | -50.34262 | 2024-10-01 05:06:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 649b8927-8a41-3076-ac42-a5e87bb589a3 | -13.6418 | -50.344 | 2024-10-01 05:06:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b6b3b82-383c-37fd-acb4-793753463be3 | -13.63866 | -50.3323 | 2024-10-01 05:06:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 689747d6-b18b-3652-a52f-6c5a8375a8b2 | -13.6384 | -50.33364 | 2024-10-01 05:06:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 716aa4f5-c40b-3a0e-8855-eb396bbd9336 | -13.64439 | -51.10302 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c9ef737-defd-3848-a94b-fa970be03cbb | -13.6413 | -51.15916 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 41bb1df6-b14a-3c03-894f-5a32212eea40 | -13.64003 | -51.10241 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ee46c44-6630-3550-ae4d-da1532703e59 | -13.63696 | -51.15854 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23843dbd-d12c-3ff4-bef1-879db00212c3 | -13.6364 | -51.1628 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79530448-b56b-3feb-86e6-a82d598bee0b | -13.63624 | -51.09751 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d444310-d2b6-3a09-b5df-25b1ad3e37d4 | -13.63568 | -51.10179 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09efc680-925a-3944-9cca-18bc18b39c48 | -13.63526 | -51.17131 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 033c9781-6124-36f4-8aa2-8fbf3ed47951 | -13.63511 | -51.10607 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf5a3d82-4e55-3635-8897-f6231e67ea13 | -13.63469 | -51.17556 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 04568213-7414-393a-ad35-91bf26d3f06f | -13.63412 | -51.17979 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4f156a11-6f84-3173-9d17-2a66f94cb027 | -13.63206 | -51.16218 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26658e69-e771-3188-bd0f-6ddcb48ee691 | -13.63189 | -51.09689 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3452db42-7317-3a60-ad83-80373d42b325 | -13.63149 | -51.16644 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2511bfff-2248-3fa4-9438-4ed515e93fb6 | -13.63132 | -51.10117 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 570ad4eb-4f80-30c0-a22f-2a4812c4a9cc | -13.63092 | -51.17069 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 46ff8dc5-70ce-34e4-b00a-692db8349604 | -13.63075 | -51.10545 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c999c016-65f7-36f9-adc2-32fea7886aa9 | -13.63036 | -51.17493 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 157a8479-6f1a-3582-9ce7-b220d5bff2a6 | -13.62979 | -51.17918 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5e07f369-e364-3ccd-92fb-8621c557134e | -13.62942 | -51.1488 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 259d9e2d-5b7d-3687-8b0c-302b22c8a99a | -13.62753 | -51.09627 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4dfc4180-e0a8-30cb-88c2-3feb70d25417 | -13.6264 | -51.10484 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 190648ae-4313-356f-925c-6ca0bf8bd03a | -13.62564 | -51.14392 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 495c46da-1f07-30eb-8a62-278918b05640 | -13.62508 | -51.14818 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0d51c47f-c28d-3a16-81b4-a2d3f3661cfb | -13.62169 | -51.17369 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01e63770-d70e-3571-ba6c-0d7a387c96c6 | -13.62113 | -51.17793 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19950b19-8145-3da4-8ce8-c6f2376b857b | -13.61938 | -51.09074 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc32fca9-4519-3b11-b1a8-3ba61d5bbaf0 | -13.61502 | -51.09012 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 138bbc40-cba1-34bc-b658-41cfdd80b549 | -13.61123 | -51.08521 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d02ac96f-44e1-3847-a8c2-0d07e3b66be5 | -13.60687 | -51.08459 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cda0d24-b62c-3ea4-a2ca-cbbea9ac7b37 | -13.60419 | -51.07106 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f030e4c8-1260-30d4-93a2-8165d9e9f607 | -13.60363 | -51.07537 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6076d599-9cec-3f5d-bcdd-b701fc4d2464 | -13.60307 | -51.07967 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a537b16a-8fec-3548-852c-de5541248b89 | -13.59983 | -51.07045 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f454b94a-30aa-35ce-bb79-9014854e320a | -13.59927 | -51.07475 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c412f16-a7b7-3cf5-a437-e0b4a9256f51 | -13.59871 | -51.07905 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ee62dc8-6707-33b0-a9ce-407d7295683f | -13.59603 | -51.06551 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a63882e-f9be-3da6-b14e-aeca2f9b06f0 | -13.59246 | -51.16092 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 51747161-a0c7-3581-b12c-75156ebc60f0 | -13.5919 | -51.16516 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd2e8325-25b6-386b-b2f1-7f0702d33d09 | -13.59166 | -51.06488 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05574c61-5ead-3420-918d-858eef8a1740 | -13.58868 | -51.15604 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9f7034df-446a-36d9-a319-ec05467a2e9d | -13.58813 | -51.16029 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9e297028-73f3-3a06-bb52-e59da8a5853d | -13.58379 | -51.15966 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4140ee62-7530-3f3c-beec-e488a09e417c | -13.58349 | -51.05933 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5311e728-c7be-37de-b4a2-05517d79e256 | -13.58324 | -51.16391 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8bc5686e-b5a9-3f5a-85a3-f5582544f2ff | -13.58001 | -51.15479 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f2b32675-97b4-3d54-93d7-0bd215919d03 | -13.5789 | -51.16328 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 73f03e10-8b45-32bb-b1e1-dc1c8f9bdc8c | -13.57139 | -51.11883 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2b4cb1dd-61c7-302a-8d50-be0267ed2b58 | -13.57084 | -51.12311 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb490e89-6a91-3fe3-98c2-7185be3f2706 | -13.56919 | -51.13591 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c1ae359-093e-3052-a683-8eb4ba41643c | -13.56704 | -51.11822 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c2c57c88-f574-32e0-a253-c7ac1db97b69 | -13.56649 | -51.12249 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8261e44b-c9cc-390c-987e-a657d0853bb3 | -13.56594 | -51.12677 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 158a0d5c-7e7c-325b-8d4f-cec49f90de53 | -13.56269 | -51.1176 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8edcc4fa-5761-38ef-a02d-3d87fa5afd20 | -13.56214 | -51.12188 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c185c08-c825-3250-9949-58bb27305472 | -13.5616 | -51.12615 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f494bdc7-5d63-3168-a4ac-f0d73bc1c68b | -13.56156 | -51.1608 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 645a450d-03a0-391c-9ab1-45e5f158b18d | -13.55889 | -51.11269 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 995d4f5d-ea38-3176-a3c7-96b7007eef83 | -13.55832 | -51.15169 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0624e873-ef44-36d3-8945-c143dc641f94 | -13.55777 | -51.15594 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38a65dc5-c0c0-36c4-bc70-a33903496ae7 | -13.55562 | -51.1383 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 279664de-79ba-365e-b038-f661cad415c5 | -13.55507 | -51.14256 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8824079-948d-3f1e-aa69-721cda5af793 | -13.55179 | -51.12265 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0a4d43b-da74-38f9-86a6-f7a5c89970bc | -13.54744 | -51.12204 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f4b1fa2-566f-3398-bef8-64f1da400320 | -13.93351 | -50.88223 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6013a1b-32c1-3d2c-b57d-b17f1f4e6cba | -13.93078 | -50.86813 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad3fe757-99fa-30c5-ad63-b27ccca9bf19 | -13.92964 | -50.87712 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ae93603-2c8f-37ea-8af7-77c32989899d | -13.71297 | -50.9596 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8d90fff-157e-3de6-a2f2-7bcebc356bef | -13.69976 | -50.95767 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README109.md)
