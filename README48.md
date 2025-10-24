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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37313ab2-6374-3afe-9529-2484bb0a4319 | -14.44284 | -48.06205 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36e53312-1b7b-3ebe-9b8f-cf3c10930079 | -10.60606 | -54.00023 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7627c8d7-f1c1-30c3-be21-b19aff7dff5b | -11.81996 | -44.16628 | 2025-10-24 04:40:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 975ab779-9624-3959-b547-c0d1c29f5e49 | -12.81694 | -48.63178 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42515066-56bd-3a24-8072-6b26c8c877c9 | -10.66453 | -54.31306 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6876b28e-72a5-3774-aad7-dfe6b40d4739 | -14.9216 | -48.13769 | 2025-10-24 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48b99b32-8fb8-3d90-a0b8-7c9a9f6e5218 | -11.99213 | -45.42852 | 2025-10-24 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53d60c71-2f82-37b4-bd4e-6d8b92ea0e21 | -12.80318 | -48.62952 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fb449da-7bcf-3905-82ff-4907f8f11c41 | -14.69252 | -52.8281 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57d4ebb7-92f6-3062-9997-74088c1244af | -12.17864 | -46.56449 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02a7792a-948e-3c60-9a6b-ddbf255de9e2 | -13.06851 | -48.20297 | 2025-10-24 04:40:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78b09d55-801c-360d-8ea5-b726da3609d7 | -13.61411 | -47.05603 | 2025-10-24 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd8f6fc5-020a-34ae-bf46-ee08cc23ec2c | -12.07034 | -46.43182 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90654a75-108d-3ae6-a8a3-ce7cef916b07 | -14.43259 | -50.95412 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0198a2a3-9511-374c-9ef2-1187853d1fad | -12.8174 | -50.96458 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd100389-b776-39d4-bdd1-ed7a7be26093 | -12.95165 | -48.50211 | 2025-10-24 04:40:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 823780cc-f912-39f9-bdc9-646b367492f6 | -11.59267 | -47.60659 | 2025-10-24 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f4fd480-618c-3f2f-93dd-23cc1dd020a1 | -10.60447 | -53.9977 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4682c332-8952-3ad6-969f-dbfb09e65d2c | -10.99414 | -54.25151 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acdd4b56-b324-3285-8db1-a6d0cc64e5b2 | -11.47703 | -51.48241 | 2025-10-24 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d9bf050-577a-31f2-9bd2-0b33f47e9442 | -12.82562 | -48.66793 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17fe7bbc-99c7-379b-abba-e4e8f5aa998c | -12.28797 | -47.46001 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 020bc9ef-2d1d-3564-b3ae-4c0166b269fd | -16.31261 | -46.57592 | 2025-10-24 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b466afd6-957f-3e4c-9c0b-37a6f189c6a0 | -12.83351 | -48.63876 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c23f6bb-9692-338f-a8c0-7b6aa63740c9 | -12.82996 | -47.24407 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbff4a8f-1a24-3dfe-8029-adbd6fb1ff32 | -11.56144 | -54.52044 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceaf58c6-1f99-3916-aedc-6b7b92e7c2c6 | -15.19092 | -47.94672 | 2025-10-24 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f3ea968-4ecc-3382-a6ae-6fccf2131dbf | -13.89549 | -48.34678 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c997c5a-8f85-3c8b-892b-84ecfd781c02 | -12.27199 | -47.45849 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8055d542-8809-30ea-9d1f-639f677499f8 | -12.24121 | -47.49247 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02018919-b308-3f0d-9996-b8d0808a62a2 | -12.0699 | -46.40769 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 134b248d-0060-3c71-b746-5a06d89176aa | -10.97788 | -54.25041 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b4c001e-515e-3504-ac16-c42e25f9bbed | -14.91802 | -48.1371 | 2025-10-24 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc5161a7-2f33-3944-bf09-d2625c4cb016 | -14.90465 | -52.43974 | 2025-10-24 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d54b3d5-de0c-3a5a-94e8-22502229561b | -12.49719 | -55.74107 | 2025-10-24 04:40:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae5cef4b-1709-3f78-82ef-8c51a2769088 | -11.01681 | -49.84469 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 059b21f6-a131-30a7-9d23-847d3c78e61c | -14.67286 | -52.3451 | 2025-10-24 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ad0158e-63c9-35d3-ac24-6819b0f79e8a | -11.04795 | -47.89555 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b75d811-712c-3671-841d-4e6659fc32cd | -16.31481 | -46.57546 | 2025-10-24 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef1c9902-f1c7-36b3-b756-517d689d563e | -18.45712 | -44.44129 | 2025-10-24 04:40:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9da0370c-4a3d-30dd-a707-bb470465efa2 | -12.1784 | -43.61096 | 2025-10-24 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8b2d4bc-508b-325f-b092-dbc574f2a4f3 | -12.27898 | -47.02613 | 2025-10-24 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5d615ef-2ef7-3135-a750-f956fee9f4b1 | -13.64151 | -49.45554 | 2025-10-24 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 650cf5fa-5dbc-3d06-91f5-ac0e87363198 | -13.59051 | -50.75844 | 2025-10-24 04:40:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b320489-a6f6-3040-9bc3-ca9266d76483 | -12.72507 | -46.95779 | 2025-10-24 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dfebc605-596f-3a81-8120-08290a5215a0 | -14.4816 | -47.92201 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 46f43348-e7e7-3bdd-96f8-915ee1d183f1 | -11.33961 | -46.73669 | 2025-10-24 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70775289-b1a6-39fe-ac5d-72539fcc3574 | -16.47638 | -46.47562 | 2025-10-24 04:40:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca2e577d-169a-32bf-b822-341f3c7042f7 | -11.01404 | -49.84064 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8aff4d30-46b2-37ae-a0ac-e48a867034c8 | -14.44089 | -50.94456 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 055a630f-c37d-3c1c-bb33-80f370176c32 | -15.86439 | -49.37382 | 2025-10-24 04:40:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96a1e4f5-4db1-3917-903b-51c6d74a9d83 | -13.24489 | -47.88368 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65f2483d-ddd1-3105-af26-3365ddd33a53 | -12.07057 | -46.40303 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c46d7755-3c6e-3c7a-8d2a-3934581ab306 | -14.43702 | -50.94756 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21b41f16-543c-386f-8b79-dec294c60dd1 | -11.43517 | -54.09533 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ae8ee99-ee20-39db-98f8-c3744b17ea9b | -13.26208 | -47.89088 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5105d285-93d0-3206-9fd3-13dd73dc4325 | -15.84168 | -49.09393 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25a87e0d-5d2f-3b26-a5a5-dfc700412673 | -12.25814 | -47.45235 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a793fe4c-b9ec-32af-9d89-ff6a26024b30 | -10.20976 | -53.88398 | 2025-10-24 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99c1ce98-f27d-3c00-b5d0-71d9cde004f1 | -13.90712 | -48.39382 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06d6f554-81b8-34bd-a6d9-79893c139cba | -13.82547 | -48.5044 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ba6d0f7-01fd-3c15-baa4-a6da3910b13d | -10.54386 | -54.86528 | 2025-10-24 04:40:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66328d94-4eb9-3418-8641-679cabfd4b35 | -11.96915 | -49.19346 | 2025-10-24 04:40:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42cb9d8e-74a0-3c5e-aa14-e8378131126d | -13.18144 | -49.65001 | 2025-10-24 04:40:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dedb7f68-0505-3e11-9c5f-6150d102db56 | -14.31091 | -49.85711 | 2025-10-24 04:40:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8401a78a-852d-36b6-a494-1a9c9d03d772 | -13.3467 | -47.97888 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2b6ade6-047e-335d-bacc-a1468195c08a | -13.9224 | -48.38756 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 316e36f6-76a7-3118-a00c-3b6f28cfcfec | -10.74527 | -49.11907 | 2025-10-24 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e066ebbd-da68-3472-bec3-549c0caff18f | -12.36834 | -51.47892 | 2025-10-24 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d116658a-1ff4-3ad5-81e6-567ee5dd29c3 | -12.84521 | -48.56071 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b87a6ed5-ffe2-3b60-a30f-dc597340bc8c | -17.37608 | -52.01706 | 2025-10-24 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bd5a8d3-913d-304c-9d0f-15c749d83ac7 | -11.4885 | -54.0214 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f15db6b-605b-3bd1-9840-989a2de337bc | -12.71589 | -46.94211 | 2025-10-24 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7dab4cf9-7f8b-3933-9d28-2af9a20a485b | -12.82131 | -50.93991 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e2f0438-af9a-3d83-a407-5df7bffdfb04 | -13.91474 | -48.39086 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84498e91-387f-32e3-91da-a458dd985852 | -11.32301 | -54.26035 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06d4a65e-af71-374a-b39b-b5e738977312 | -11.0133 | -47.88048 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f9a7749-61f7-3c32-8351-a9dc6a79a709 | -15.84224 | -49.0901 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b622da5d-6ddb-3910-ad9c-dbafbf6a10bc | -13.18829 | -48.48817 | 2025-10-24 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fc71af5-0e9e-3a84-95a6-23f2bc9dcffa | -14.51298 | -48.34749 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 414d450d-45f1-3b51-8d9e-199c7c34eff5 | -16.53624 | -54.17799 | 2025-10-24 04:40:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce813ce7-5bde-3bc9-afec-c33cc19e1d2b | -11.48191 | -54.01575 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3903b218-0aae-3218-ad9e-ca25a69bed47 | -12.76907 | -47.38113 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 167f2e5b-115b-3bcc-a65f-18b22986923f | -16.37281 | -47.41508 | 2025-10-24 04:40:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abbc8b8a-cb34-39ae-aa01-358d5dd65955 | -12.27639 | -43.82696 | 2025-10-24 04:40:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57749d2f-ac8d-3a10-8278-6b3266e458ec | -18.45649 | -44.4466 | 2025-10-24 04:40:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f6b45db-5a32-32c5-af2a-8aef73d91601 | -12.68164 | -48.62245 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9b8d6c0-daef-3888-8bcb-5b357e96c80e | -13.61998 | -49.45263 | 2025-10-24 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 609b78f6-3c02-39ed-b776-a4a4b78dfdcd | -14.75372 | -46.60666 | 2025-10-24 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4dc8d80-4d51-3bcf-a4a6-ee2a0aa3cd40 | -15.312 | -47.85612 | 2025-10-24 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64fd730d-cbc7-32f3-921e-dd06b4832fbe | -12.66386 | -48.62355 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8b3bf06-a232-347c-ad64-f962dda60fc3 | -13.30399 | -47.44809 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54ae6e3c-3813-3429-bb7c-ff21bcbcfc06 | -12.83078 | -48.65698 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40b3bc19-548b-3484-9e1a-8016d14638e7 | -11.47928 | -43.24551 | 2025-10-24 04:40:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9e4f09e8-2a22-384b-9760-2cdae1f399af | -17.65578 | -46.67134 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c50ae9e6-7ce4-3c0d-88f6-37cd0dc813fc | -11.36527 | -45.93294 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1dc6638-d109-389b-9d43-669e78c66d05 | -11.49 | -54.01262 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e59e855e-89de-322b-9007-cc2e7a233918 | -10.6357 | -52.18385 | 2025-10-24 04:40:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c06867bd-1942-39ca-b901-33a4f19bbea8 | -11.74213 | -45.34808 | 2025-10-24 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd0a8621-3873-39e5-b326-22a5ab1aba62 | -15.21215 | -47.95412 | 2025-10-24 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README49.md)
