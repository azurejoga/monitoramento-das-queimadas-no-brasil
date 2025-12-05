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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae1ed8ce-4ee6-3f72-a0ea-de7d4e7712ed | -22.84589 | -53.01577 | 2025-12-05 04:36:00 | NPP-375D | NOVA LONDRINA | PARANÁ | Brasil | 4117107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0487ca89-2eb4-393f-9b3d-d6aa8c014de1 | -21.63196 | -56.13247 | 2025-12-05 04:36:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f34d725-2cb6-3ae8-9ddc-4eda927f8c82 | -31.5965 | -53.62527 | 2025-12-05 04:38:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| fcdecd61-2aba-3e5b-abdb-b6d57c82f63d | -31.59315 | -53.6245 | 2025-12-05 04:38:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| d77371e8-e805-3e88-bec4-106368a05987 | -31.59246 | -53.62861 | 2025-12-05 04:38:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 8e040a15-25c4-3a97-b7df-4f93a921d220 | -31.59581 | -53.62938 | 2025-12-05 04:38:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 5c464850-6439-3a90-8476-66bc4e11f757 | -29.23657 | -52.62816 | 2025-12-05 04:38:00 | NPP-375D | GRAMADO XAVIER | RIO GRANDE DO SUL | Brasil | 4309159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 919fb948-9d26-39e3-bf1f-5d6cd049289e | -29.45492 | -51.52758 | 2025-12-05 04:38:00 | NPP-375D | SALVADOR DO SUL | RIO GRANDE DO SUL | Brasil | 4316501 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 03173428-49ac-3f31-8f54-061d14fe6e3b | -29.05301 | -52.36056 | 2025-12-05 04:38:00 | NPP-375D | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1a4d253d-5802-341d-8f13-2c0a86c50def | -30.07533 | -51.16088 | 2025-12-05 04:38:00 | NPP-375D | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| ff2d13cf-4e81-347a-9e5b-0795b1fba0f3 | -6.0004 | -41.1295 | 2025-12-05 04:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 4df557b1-b2f2-3933-90f8-b5297e17a313 | -6.0004 | -41.1295 | 2025-12-05 04:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 238435ce-df87-342f-8b18-864672bb8136 | -1.17664 | -53.89312 | 2025-12-05 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abc82072-265f-336a-a080-a62b89058608 | 3.46077 | -51.25179 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1d8cc21-5d45-324c-bd3a-dddc2ce9afda | -0.3335 | -51.66995 | 2025-12-05 04:50:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0aa81fd3-c28c-3557-9d9d-995ca8ebca55 | 0.13738 | -51.07915 | 2025-12-05 04:50:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66e18cc9-ccc6-3621-9c13-aaddb54ad3ef | -4.49857 | -40.50878 | 2025-12-05 04:50:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 56f5cd00-d877-30ef-b3e1-64d452099f3f | -1.17737 | -53.90057 | 2025-12-05 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2d3efee-32e8-3e06-94f6-ad814efab037 | 3.42203 | -51.26494 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7aecb5ce-9495-3228-8228-4a16ecb61044 | -1.60491 | -48.70229 | 2025-12-05 04:50:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3a4eaf0-cc44-3278-934d-c37c5b21d9f5 | -1.46508 | -47.16766 | 2025-12-05 04:50:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fbb28c8-176b-34cc-ae9a-99d605a49aec | 3.50224 | -51.25602 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3aad92b-15dc-345b-8a89-d30c973c60d0 | -1.95982 | -52.73134 | 2025-12-05 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c6e3755-54e2-360e-9174-df6ccacee8f0 | -3.67077 | -43.60375 | 2025-12-05 04:50:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c60da3ab-d640-36f9-8b4f-8a4c3207b585 | -1.17894 | -53.9012 | 2025-12-05 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6655602-5daa-3b94-8e30-8ef82603148d | -1.96038 | -52.72783 | 2025-12-05 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84898a15-a7c3-33a5-995e-0589095b3d9a | -1.40057 | -48.89804 | 2025-12-05 04:50:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35c3413a-68e4-36a4-829a-5e7f83a0691a | -1.78806 | -54.01442 | 2025-12-05 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3309173c-6051-35fb-95fd-f3cfabde863a | -2.44122 | -47.1642 | 2025-12-05 04:50:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 063106e5-e705-383d-a5e1-15a4d2c4aa89 | -1.78866 | -54.01057 | 2025-12-05 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d4b767c-650b-35f4-9dc0-9eb9d4e40705 | -1.78927 | -54.00673 | 2025-12-05 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55cb20a2-7bd9-31d3-830d-0f1e4f19bbdf | 2.52484 | -50.85445 | 2025-12-05 04:50:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e21d0c3-6259-3e42-a25e-7cabcca45423 | -1.02373 | -46.65031 | 2025-12-05 04:50:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3510dad-4187-35ee-953b-6b0bb8ad955e | 1.66798 | -50.65936 | 2025-12-05 04:50:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b70296ad-66fe-371e-a978-afba4fb2c268 | -3.66567 | -43.60293 | 2025-12-05 04:50:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3bc2708-6014-384f-af1b-0dd2bec1aa73 | -1.95704 | -52.7273 | 2025-12-05 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7350bce5-4192-34c2-a9db-49fbde382a8f | 4.43092 | -59.88433 | 2025-12-05 04:50:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c2743eb-7ea3-3da1-9649-222e61de6704 | -0.64558 | -52.38532 | 2025-12-05 04:50:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1fa33a3-4d63-3d00-b4d4-42686ebb3769 | 3.46132 | -51.25526 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f901af3-ec7c-3833-aed9-4e097ed826ff | 1.96077 | -55.72301 | 2025-12-05 04:50:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d1e47bc-d5df-3bef-a4d0-bc0c39361ff4 | -3.71853 | -45.94872 | 2025-12-05 04:50:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c370f5b0-7aee-3a43-8d76-ab92313b5bf1 | -1.23521 | -46.73639 | 2025-12-05 04:50:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 938153dd-6860-3562-b957-a52f8b378d76 | -0.96844 | -53.76728 | 2025-12-05 04:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1049b2f9-00d7-37e9-8774-5ef12d683106 | 3.46463 | -51.25475 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a26928d-431c-3f1b-a757-0b459684d22c | 3.46686 | -51.24728 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a699aa59-e30e-39de-818a-4d42cd5d1590 | 0.44488 | -50.93982 | 2025-12-05 04:50:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35ac59e6-8c9a-3594-821d-a8f6a8696adc | 2.52981 | -50.84313 | 2025-12-05 04:50:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2908229c-a175-3d83-b77e-35383ce9c44a | -2.68205 | -51.86044 | 2025-12-05 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c02bc2c-19fb-31c8-be56-65737b0f758c | -1.4082 | -51.59994 | 2025-12-05 04:50:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c45f60bd-ca15-3462-8819-c7f21210e466 | -2.53576 | -51.23773 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e870f908-aec4-32ec-a489-115ddd127d1f | -1.60554 | -48.69824 | 2025-12-05 04:50:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46fe9e3c-3bb1-398c-97cf-87272e8ddafd | 3.49837 | -51.25306 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba3be744-35cc-36e3-ba46-e713731199c0 | -2.53631 | -51.23428 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 121689fc-50f1-39e2-a16d-2ee257c5793c | -2.12283 | -51.12014 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10d1e436-7c28-3a7d-bedb-32c7686b54fa | -3.60173 | -46.00855 | 2025-12-05 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 13d7ab1b-4f79-325f-96a1-a80668525b9e | -2.56211 | -51.8237 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d81a714-2e56-3d12-a9af-7a844b71c76c | -3.60468 | -46.0072 | 2025-12-05 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2a021d76-da35-3bf3-b747-bb6cd35475b6 | 3.4945 | -51.2501 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f105dacf-86e3-3287-b399-0c36302b3a6b | -1.41151 | -51.60045 | 2025-12-05 04:50:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75d7f6db-0c40-3f7e-a808-94defdd1bd1b | -1.67769 | -45.79774 | 2025-12-05 04:50:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d85897d1-ce80-3453-bb54-1a6ad35a0260 | 3.47295 | -51.24278 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6bf4f926-5fed-34c8-ae6a-d9c8722b3802 | -1.23469 | -46.7398 | 2025-12-05 04:50:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f2e9855-a360-3c8a-a71a-a2d87d6d0cd0 | -1.67832 | -45.79375 | 2025-12-05 04:50:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9410e8e8-b309-3f29-97cb-024d28d283e0 | 3.46963 | -51.2433 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f43f88ae-cb33-3b23-bb9c-c9b1d3827a82 | -1.12107 | -53.44291 | 2025-12-05 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f110e11-70ae-3113-8ba7-c19e83911062 | -2.97341 | -41.59095 | 2025-12-05 04:50:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dbc5593-6461-332a-ba7a-5126cd1a90ea | 3.46409 | -51.25127 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 875c2053-ab0d-3775-9180-795ba68035d9 | -2.692 | -51.64736 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f69745e-6868-3ba5-9f77-04bf5aa5c641 | -1.23071 | -46.7392 | 2025-12-05 04:50:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f596ecc2-f35f-35f1-9e26-7c23ec744dd2 | -1.17834 | -53.90503 | 2025-12-05 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7568f3c-d096-3fe6-bee8-5bef3b4bd146 | -1.95649 | -52.73081 | 2025-12-05 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 166521e6-927e-318a-923d-aa7086ca34ac | -2.40101 | -47.13758 | 2025-12-05 04:50:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8677ed5d-c8aa-3170-a5dc-a76cf377a367 | 3.46354 | -51.2478 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 180ab219-2857-324f-8931-12935e9e67c5 | -0.78218 | -52.29276 | 2025-12-05 04:50:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8ae56b0-f8a9-3f22-867e-ae19c8099544 | -3.37662 | -44.10676 | 2025-12-05 04:50:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b4b01af-abaf-309f-a5c5-b49c7b28491b | -1.109 | -53.6544 | 2025-12-05 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b269c07e-191c-3c5f-8f35-04a3cbd035d5 | 3.46186 | -51.25874 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d434593a-e5f8-36b0-9464-92b66b26e12d | 0.76671 | -50.80433 | 2025-12-05 04:50:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b179db60-d7f2-3970-bdd2-ec24f28b560a | -0.78551 | -52.29328 | 2025-12-05 04:50:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09f3220e-ce74-3d24-8643-795d9fc24898 | 3.47018 | -51.24677 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5086b998-4a9b-3a05-a5f5-152987898572 | -2.56102 | -51.83056 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76a73b6e-0e4b-38ff-8339-27ec48d99374 | -1.17316 | -53.89267 | 2025-12-05 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3679f4b6-dee5-397a-aa6e-ff965fe57e64 | 3.4735 | -51.24625 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd003038-ade6-33bd-87e3-69e6b16eddaa | -2.56487 | -51.82764 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6380a4b0-a1df-34ba-8a77-e7ca6d062cc7 | -2.56433 | -51.83108 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bedcc1c7-9541-399b-b025-6a5c0ad59ee1 | -3.60605 | -46.00921 | 2025-12-05 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e618da6-b39e-3f38-96e1-41cb62a9f394 | -1.23867 | -46.74039 | 2025-12-05 04:50:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63e45065-1bd2-35c1-8b6d-4f45c7f4e27c | -2.50482 | -51.80069 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11385033-39da-3dc4-9ce0-2cd1d76975f4 | -2.53354 | -51.2303 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fee6524f-d72c-35d2-b2b7-0374761321b4 | -1.17676 | -53.90436 | 2025-12-05 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2507495e-d248-30c3-88c5-8b91e6e97479 | -2.48083 | -51.80038 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d1f698f-c4ee-3b2b-b55d-231b9a14e143 | -4.50422 | -40.51462 | 2025-12-05 04:50:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bdac609a-68b4-368e-b5eb-4418e893b48d | 3.27389 | -51.33819 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7bc57f4e-488c-39a0-b930-9810d5d547cb | -2.56541 | -51.82421 | 2025-12-05 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d70d119-9d5b-3470-81cb-97c4f41988cc | 0.01197 | -51.38371 | 2025-12-05 04:50:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d12e35ce-796e-3342-8a68-1e178d0600d3 | 3.47682 | -51.24574 | 2025-12-05 04:50:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e29d40a4-ce4e-35a7-86d5-a1919e098310 | -1.72662 | -54.33525 | 2025-12-05 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab12c9f7-c63a-3be8-b543-32ffbebd7050 | -0.33019 | -51.66943 | 2025-12-05 04:50:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3a2633b0-2dde-32d9-8f7c-02630413b82a | 4.43145 | -59.88804 | 2025-12-05 04:50:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4363ab-fbbd-3aa1-8f89-371173cf0639 | 0.84897 | -50.18648 | 2025-12-05 04:50:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
