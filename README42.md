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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca951fbe-6d28-39b3-b649-3a43af3a1b81 | -13.68281 | -48.62187 | 2025-10-04 03:53:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2cfe8a88-71a8-30b7-8cee-e37b98fbd8a1 | -12.07671 | -47.99281 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3ab82ce-93d7-3953-a4a6-42bafb84b36b | -14.97499 | -46.84832 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc7670ec-d140-3029-84b3-704a569a3ab4 | -12.22569 | -43.773 | 2025-10-04 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6f89def-b86d-3178-883f-ef34e50a491e | -12.65094 | -46.99455 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7db10212-e746-39a8-865d-f8a77db76188 | -16.38876 | -52.17002 | 2025-10-04 03:53:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2251746e-a854-3da6-84e8-dcf55bfd00a7 | -14.68025 | -48.0676 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05221704-3e8f-3646-9d36-ed3f82549996 | -14.44003 | -46.10167 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5b83d2c-18cd-3b1f-a0f7-b5a4c875011e | -13.60477 | -48.18262 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 748803d9-6f41-30bb-9b38-55e93b639de5 | -13.31851 | -47.61438 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 638427dc-6465-312f-a422-bff0e5f6fb0a | -11.83406 | -45.02135 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb53e489-86d6-3318-96ab-f7208336a9f6 | -13.12316 | -47.83578 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1c840db9-a657-3f03-87f7-25c98b457fa8 | -11.79939 | -45.02998 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 783ae3b0-2f50-30b0-b6d2-8ed24f3f6842 | -11.83624 | -44.93298 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9a3d211-2554-3cb8-b73f-1baa9347af5f | -12.07601 | -47.99645 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b7c7127-bd23-3c62-afdb-bfd6a67a071c | -13.12443 | -47.82938 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ad3885d2-5261-3483-a722-dc3f753e8166 | -13.11583 | -47.87268 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94118f03-6f17-3cf3-b8ea-7604ead121b4 | -13.32646 | -47.18883 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 062d3302-9420-3b0e-973e-61219c409f03 | -11.78732 | -46.82016 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b40c9b42-25bc-3e47-9edc-13fc3646fa7c | -13.11048 | -47.84336 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9b573a2-9964-35fe-a7eb-9bf78bede4da | -13.47239 | -47.26914 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f67371bb-c53c-35e7-9221-4aa44ff0d420 | -12.86287 | -46.98907 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9cd14577-6d1d-36e1-b82b-566a27911508 | -15.31051 | -46.38255 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1ca41b4-1f09-3ba3-9f80-c08105c53de9 | -14.63412 | -48.25927 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 67c7bff8-0cb5-391d-9f4c-03de6aaafee9 | -13.22686 | -47.82748 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28beb749-826a-3803-9046-ce2b717c8ef1 | -17.08336 | -43.36651 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 851fee4a-319f-3d3a-b046-1188c21a3a52 | -11.79574 | -45.02423 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81049087-4a21-3dfc-9b08-716ea9540777 | -15.9963 | -50.92875 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f498ed81-9a4d-363c-8364-753f36c417a3 | -13.99478 | -48.1913 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0146c59f-738c-3639-9f04-7226f267234e | -13.28716 | -47.83196 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34320136-e3a4-334a-b1cf-04db81286a81 | -11.92038 | -46.37856 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6dbbf45c-6615-3a80-817a-e7e223c9eb95 | -13.32615 | -47.57511 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5ac221de-2f00-3ad0-8eec-c66330b91d2d | -11.80142 | -45.0234 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 027c9dab-0ece-3142-9dc6-625041270b6c | -14.21327 | -46.0783 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 722e2371-541a-3edf-aa52-4dbc29ff15c0 | -16.03233 | -50.94115 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 75213c6f-fa04-37e9-b2f3-1219bff3bf34 | -11.79058 | -46.83138 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eda2c5dd-8b96-32d0-94c7-99f44e55d8cc | -11.45314 | -49.71739 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cc428af-ff3f-3164-bcac-f498d459d197 | -13.73508 | -47.91908 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7691b47d-d903-34df-a9c8-4254f803c9e3 | -11.55291 | -47.67842 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f56c144-bcf4-3e7b-8bb2-b83b583f14fb | -14.96605 | -47.26381 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3f04226e-0cde-3469-91a5-ab6da86c881c | -14.87038 | -48.36022 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 494e7365-df4d-3ffb-97ce-bd27332eda90 | -13.33124 | -47.79139 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55a93ca3-abe7-3c0d-a24e-3fe50cb5e21b | -15.30072 | -47.94467 | 2025-10-04 03:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 292688c9-0364-3cc1-a623-4fa892dad4e2 | -14.89308 | -48.27555 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 363a09ff-5f92-34ea-95b9-068e15c3ebff | -17.58554 | -44.46297 | 2025-10-04 03:53:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03e28159-e3b4-3fb4-a115-8095219248e3 | -12.92491 | -46.36768 | 2025-10-04 03:53:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6726b8ba-4a7f-35e7-a104-8f77f3c0abdf | -13.73533 | -47.93172 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21d7515c-44ec-31a1-8e2b-9fdc0f2dd7c1 | -11.82497 | -45.04501 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfa30ec8-208a-3228-ba9d-d7f45d26b9ad | -15.58044 | -52.47339 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 549eeda0-0705-3eb0-a1ad-36a72c390cc2 | -14.87272 | -48.13023 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28788fb7-3be1-3e8b-80f5-7327638b4eb3 | -16.75704 | -43.95689 | 2025-10-04 03:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f636452d-108d-36b5-b6c1-62fc4ec1143c | -15.79467 | -46.257 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7a5fb2b-8642-327c-82a8-32f4030db132 | -12.03593 | -45.20239 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 25b55876-e9ff-3a75-be3a-ba42a368929a | -13.20638 | -47.81857 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90199f43-4e00-3578-9f40-0e374bc56da4 | -13.26362 | -47.20449 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 107e6514-155e-3d00-9587-a329a30be658 | -13.34916 | -47.23606 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3ecde64-b623-314c-ad2f-b862e8326b8a | -13.75467 | -48.05832 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c85d1405-c017-3435-b9c4-1442d4cf8fc8 | -17.61842 | -44.46384 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf548ace-ad3d-31a2-adfc-6bf30e2a0048 | -13.24969 | -47.24857 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3afde9d9-84a7-3e12-bb4f-c67497639210 | -13.3151 | -47.24612 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70c3952b-bb7d-3550-88d3-af9d9a390e76 | -14.9911 | -42.01662 | 2025-10-04 03:53:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3efd11c-7712-35d0-a2b5-b5be7fa59ab4 | -11.5651 | -47.67403 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8adf6c15-3743-30d9-a4d1-0f8264e91280 | -16.29107 | -45.24609 | 2025-10-04 03:53:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e56c97d-a294-38c2-9514-d9493c9d40ff | -13.1316 | -47.93457 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3011317-3cdc-3ad4-b712-28b869999ab7 | -16.0645 | -50.90156 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ebc5fbb4-de46-3475-bfa5-50007c39ee49 | -13.13175 | -47.82055 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1c096fc9-ca17-3cfb-8956-8d0a0b590c7e | -12.84336 | -46.85569 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 608b04d9-2e39-3432-b7e4-d88b78951805 | -17.96084 | -44.39456 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 767c887c-f206-3faf-9fd8-3ac33d262d23 | -11.81132 | -45.04212 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 824621ca-d029-3808-aa3f-e56ae5c48b39 | -13.38326 | -47.28065 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62384dc8-d5b9-3cbe-82f6-409807b7016d | -13.99784 | -48.20444 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b7f3c4a-53d5-3af9-b212-98f2d6ade1ff | -13.12413 | -47.94398 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7eefc6f-f68e-3ee8-b9da-661c748f71f6 | -13.29092 | -46.98286 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f14c1052-5833-39b5-b658-afed8d62f336 | -13.31695 | -47.26059 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b04c1201-16ce-33d8-aec7-74d7a6e056c5 | -13.10816 | -47.91125 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7240a34e-c639-3ee2-a945-cb7447d0949f | -11.92142 | -46.37307 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1fd2aee2-51a5-3587-89f9-7dbf82c168b1 | -14.23593 | -46.08702 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f55cfbc1-6649-33a6-a0b9-17cfd10c55f0 | -16.01095 | -50.94001 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f577f4d3-4dd3-352b-9b1a-36a5b24d1a86 | -12.02672 | -45.20068 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 03537901-e541-33c9-b6fd-d8e8ed435e7a | -13.22196 | -47.82415 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95643e17-1a61-31db-b900-5b9ec9b339e3 | -12.03681 | -45.19761 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| e52a9e3e-f271-395c-a47f-0097f32ad649 | -17.15466 | -47.03182 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c332e948-7288-3c88-b2b4-05ba2511cbaf | -11.91312 | -46.38964 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 7d630069-4b74-3d4d-b885-87cb768a4793 | -15.29441 | -46.28873 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b858123-3c01-3cde-a5c0-cb1ef8dc409c | -14.98464 | -46.85073 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ffdebca-85ff-3cfc-8880-17ee8a5e84a0 | -11.90527 | -46.37649 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1af7821-15e7-39b2-8aa8-e6e82e1fe5b6 | -14.92398 | -46.87618 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52dc9675-f4ad-3c1f-ae24-329df653741c | -13.52718 | -43.71069 | 2025-10-04 03:53:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0da4c88-3c97-38b2-b15e-82c0d5ac404c | -13.69437 | -47.3488 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfdfc9f1-62b8-31dd-860e-e470b09a534d | -12.8714 | -44.62859 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| de1f146c-a06c-3e30-bc32-1be824a47e4e | -13.74446 | -47.94164 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d61b91e2-a26e-3147-b80c-3f3e77af8b8f | -13.58825 | -48.18031 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cbcc47e2-736e-3fa3-9b9e-a31e0f6c4344 | -16.75311 | -43.95621 | 2025-10-04 03:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5df98156-933a-34aa-9edb-fba76c77481d | -11.79181 | -46.82475 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c64da89b-97b7-32ee-8105-db8312400594 | -13.31952 | -47.25085 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 143ce45e-b033-336f-9324-eb09fc65b0b8 | -12.82016 | -46.86722 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d66e9ccd-3155-3229-94d0-bfb683135bac | -13.93695 | -48.17102 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1c21982-7b37-36ce-9aac-3f017a5126bc | -13.68356 | -48.61811 | 2025-10-04 03:53:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a66a6bef-7c43-3f0f-be29-0a87f39e5ea1 | -11.54345 | -47.66872 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcd83344-dee9-3bbb-8ff1-cc0fc4763509 | -11.8747 | -44.97943 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README43.md)
