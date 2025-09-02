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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05c1f081-e28e-3bda-8a64-2b211196133f | -14.79631 | -48.22344 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e4c364da-5d44-3137-9f31-d4ade4ee2664 | -15.67868 | -48.94801 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 534250cc-d0b8-3580-8747-42e8434adac5 | -14.99537 | -50.20376 | 2025-09-02 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f723c28-3717-3762-b798-000eb8bd6c1c | -14.98935 | -50.20227 | 2025-09-02 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 277b8029-799c-3fd6-992e-b68b88594568 | -15.55768 | -48.33905 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06618ddb-fa69-3963-bfe8-b44be059034e | -14.77014 | -48.15971 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c885711-a18c-3b34-93a0-20df770a8cb6 | -14.76895 | -48.15678 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65a4fdd9-62b2-3687-8075-404f76d6bf12 | -16.80379 | -49.52296 | 2025-09-02 03:53:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95da0400-85b4-3bb9-acad-4ec03adb416e | -22.39591 | -47.1802 | 2025-09-02 03:55:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 69311bd6-727f-3b25-b2f2-68c3250395be | -22.67639 | -47.2975 | 2025-09-02 03:55:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 944eaae4-1d0d-367e-8c7b-a9fca1ed15a9 | -22.52634 | -46.81539 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6b0d864a-2a24-3d5e-91ff-1b0fb806da81 | -23.05098 | -49.87218 | 2025-09-02 03:55:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4b29819e-e07b-38c6-8115-63e137cbd961 | -23.05026 | -49.87546 | 2025-09-02 03:55:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 96548ea8-969e-391b-af07-01291e11a290 | -22.39936 | -47.18567 | 2025-09-02 03:55:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 692ed0ac-57dd-3676-8f8c-46e6986a2657 | -22.53141 | -46.81212 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5fce3b62-1288-3056-a56d-e013e695b632 | -22.5288 | -46.80275 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 53a1e4f7-7e8a-3e66-87d4-7e63411519c1 | -22.78853 | -46.31725 | 2025-09-02 03:55:00 | NPP-375D | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5bd7b22c-f76f-333a-a0eb-c46888204120 | -23.49961 | -50.79912 | 2025-09-02 03:55:00 | NPP-375D | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 39cced5d-cfc7-3286-9d5b-917821893b7d | -22.52579 | -46.80922 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 745ec6e2-f5fe-37d5-9600-e4cf4830bda2 | -22.52663 | -46.80501 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 528c65a8-5cf6-3434-a8e3-cc60c7e78bb2 | -22.40026 | -47.18124 | 2025-09-02 03:55:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cd388609-c6c8-31ee-8a06-9f6b062d123c | -22.52493 | -46.81346 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 948f6963-d8fe-3fbd-9058-8eb207161856 | -22.52032 | -46.80075 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 066c8181-27d1-3993-842d-1949f229ec50 | -23.31997 | -46.03607 | 2025-09-02 03:55:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4938d4ee-c040-3915-9ea4-6b75858ea6f1 | -23.23597 | -49.51884 | 2025-09-02 03:55:00 | NPP-375D | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 33a565d2-b7ea-385c-b4cc-ac532fe88fdd | -23.34718 | -47.1456 | 2025-09-02 03:55:00 | NPP-375D | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a08c5b8d-72e5-38ae-aab5-9107d4d91610 | -21.86005 | -46.89232 | 2025-09-02 03:55:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfa93280-a649-3819-a088-f36c7bad0166 | -22.9551 | -49.73763 | 2025-09-02 03:55:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 46c02a49-a070-39cf-a0cb-8ae1a00f2a98 | -22.52748 | -46.80084 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cbdf4e1b-e6d9-33b1-8b57-0d0de982c21a | -23.04524 | -49.87399 | 2025-09-02 03:55:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 8447ed3d-e148-35f6-98d1-e6b99fa35ed2 | -21.3264 | -48.72945 | 2025-09-02 03:55:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 8e9c217e-1a4f-3206-8844-4f590d1b5b4f | -23.50498 | -50.80022 | 2025-09-02 03:55:00 | NPP-375D | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| fe014dd8-016f-323d-bf81-750fee9ae231 | -22.52456 | -46.80174 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d85dbf26-db1c-3db0-b47e-a967f018dce9 | -21.55529 | -47.69061 | 2025-09-02 03:55:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5b5d61af-b3d9-308f-9cdb-e61a188a383a | -22.53003 | -46.81018 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5de1c210-c3d9-3690-ad08-6c3a6bfa10c5 | -23.93859 | -48.84642 | 2025-09-02 03:55:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97dcc7ab-2340-3be7-b86c-8362d0918ee7 | -22.52324 | -46.79983 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c7bf65f0-1f05-3df7-af48-a47b9cb98403 | -22.10834 | -46.96429 | 2025-09-02 03:55:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fe4cdd6-3e3c-397a-827b-bf8365c6db3b | -23.04596 | -49.87071 | 2025-09-02 03:55:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 93fdb9c7-b359-36e0-9d16-229e4263f88e | -22.52798 | -46.80694 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7c7c329d-2934-3a12-b004-aa0dfd32161f | -22.52068 | -46.81253 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d04d4008-4754-332c-b256-60c5fe407232 | -23.26831 | -46.88641 | 2025-09-02 03:55:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a8b4e773-509d-334b-9c77-3ae5a654d229 | -22.52716 | -46.81116 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7b463f05-b734-33d9-abc2-96160927953f | -23.93746 | -48.85181 | 2025-09-02 03:55:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b888b94-4098-312a-bb86-10dcf2bf51dc | -21.85897 | -46.8941 | 2025-09-02 03:55:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52e715b4-645e-33d3-a1fa-b17c59525ea6 | -23.93393 | -48.84521 | 2025-09-02 03:55:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59377b0f-9d22-306c-a1e1-c58db50c8285 | -23.38499 | -47.29206 | 2025-09-02 03:55:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b18f73be-edbd-3183-a389-b29d8af675ad | -23.39691 | -47.00887 | 2025-09-02 03:55:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7ae17281-39af-36c7-bb03-acf54755f08d | -21.85577 | -46.89116 | 2025-09-02 03:55:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 575c4912-71f8-3080-bdc6-5bdf021ab31e | -22.39502 | -47.18464 | 2025-09-02 03:55:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dcaa8ed1-0b85-33b0-b626-c8f93805292e | -23.35141 | -47.14673 | 2025-09-02 03:55:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 11bd8da0-589e-35f6-b98b-dfa9b4ee5469 | -22.88531 | -49.70522 | 2025-09-02 03:55:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8c79e96e-9c5e-3a0a-b825-cf7ea2084157 | -21.60333 | -48.2776 | 2025-09-02 03:55:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac3629d8-cfb3-37c6-912e-45243bd76f53 | -22.52291 | -46.81022 | 2025-09-02 03:55:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ea14d3df-201f-311f-9f95-957374ab6b76 | -22.886 | -49.702 | 2025-09-02 03:55:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 49726507-943c-3340-91b7-a9d109c3903c | -22.10745 | -46.96874 | 2025-09-02 03:55:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b48bd254-3df2-33f4-b8bf-3106702f3011 | -23.93279 | -48.85063 | 2025-09-02 03:55:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc40308b-44ae-3a0a-bac0-759a0e660d01 | -22.17297 | -46.61628 | 2025-09-02 03:55:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 32b15fc3-ee81-39c8-bc4d-4bef3a7f740f | -6.8911 | -45.8538 | 2025-09-02 04:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| dc6fb7c9-1b54-3c0c-a977-850516dc464f | -6.8724 | -45.8554 | 2025-09-02 04:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 274511d5-1679-3c86-93b6-4e5adc43fc4a | -7.5476 | -61.3437 | 2025-09-02 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 5e1b548e-9d15-345c-9512-fba7c53d5809 | -3.2305 | -47.135 | 2025-09-02 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7b85f891-1a87-3f0a-900e-a55b38c223e4 | -9.1207 | -61.4864 | 2025-09-02 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e196e8a3-db43-3463-ae4a-38487d5396f7 | -6.7909 | -52.8165 | 2025-09-02 04:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 96e3c1f3-b3bd-32a6-a7a0-29cd2509252b | -6.8095 | -52.8154 | 2025-09-02 04:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 3352973b-8551-3c16-8a48-4d8213cf7664 | -11.6647 | -57.3533 | 2025-09-02 04:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| dd36b47a-8ae4-35b3-8535-965ad227d27b | -7.5477 | -61.3247 | 2025-09-02 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| c9b4215d-b69c-337c-b7a0-d26b3fd50cec | -7.5477 | -61.3247 | 2025-09-02 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 5056796b-9c0e-394d-a2fd-5ffb9ff9d0a3 | -3.2306 | -47.1131 | 2025-09-02 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| fe9e27e0-9abd-3de5-bb26-936391da54aa | -6.7909 | -52.8165 | 2025-09-02 04:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 37cb41d4-a7cb-3b0a-b2c4-041d304ef315 | -3.2305 | -47.135 | 2025-09-02 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e7bf6a28-6281-3a56-a260-aacd3672c2d4 | -7.5476 | -61.3437 | 2025-09-02 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6653494f-91cd-3a67-80d4-99c9fd61dd11 | -6.23999 | -42.4213 | 2025-09-02 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 90cd5df0-3bec-3963-b0d7-66760cef4e56 | -4.31099 | -48.08388 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee10a179-45da-387c-8e1f-46efd9964c07 | -1.97938 | -47.98043 | 2025-09-02 04:12:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed048802-315d-36ed-b1b8-d2d491a5be2c | -4.09374 | -47.32787 | 2025-09-02 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c438160c-ab9f-3cb3-8a54-a087a0016f3b | -6.13045 | -44.12356 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 087529a4-638f-378b-a61b-d982e90744ec | -3.79133 | -49.4277 | 2025-09-02 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c89d0918-cac6-308e-8ec3-e694acc4ec4c | -6.0261 | -46.01523 | 2025-09-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e3c7be1-fcf2-3341-a5f1-bf538fd414ef | -3.16817 | -49.47644 | 2025-09-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 012461b7-a6d9-3d83-bcd1-57e0690bb4bc | -4.22547 | -47.21225 | 2025-09-02 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ca9a544-85ff-35ef-978f-f2b6b91e8108 | -6.42563 | -43.95752 | 2025-09-02 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec20b51f-397c-3145-a669-37e56e901464 | -5.16439 | -37.98347 | 2025-09-02 04:12:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eca8a6d1-a39c-3691-82a4-3aa539859f7d | -4.22156 | -47.21159 | 2025-09-02 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d24f90e6-bf5d-3980-b23d-7b025ada16a8 | -5.57306 | -47.428 | 2025-09-02 04:12:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51e9e93b-5b9f-366e-a162-6122fae214cb | -6.15163 | -44.11963 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 522845bb-48cd-3d28-8e59-7ade61da84bc | -6.27287 | -43.2925 | 2025-09-02 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb07b71b-d2e6-3d56-a526-965b1674d55f | -6.13199 | -46.32497 | 2025-09-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c30dd963-4854-3927-8461-a73bf5a86f51 | -6.29086 | -43.56491 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfdccc51-4af4-3a90-957d-08b9fb258ad3 | -3.90593 | -47.80833 | 2025-09-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1767c51b-018e-3bd9-a819-2b2a4944ead4 | -5.91603 | -44.97598 | 2025-09-02 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17ad19c8-99a1-382e-acf4-32d5097fd129 | -2.44051 | -47.3327 | 2025-09-02 04:12:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca122d75-2054-3e2b-ac47-e24eabd99bec | -6.12598 | -44.13008 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d00d361-5d6c-37e4-9e7d-5e8de0ab925a | -6.17439 | -44.14879 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a27e5222-786b-3de1-8f80-b69ac20227d5 | -4.90997 | -43.18972 | 2025-09-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5870cd8c-2223-34a7-a444-9f4afb7af232 | -6.25367 | -42.61609 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 276ab332-7b35-350f-a1d7-61cd587f908f | -6.30244 | -43.5561 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb4d06a5-07de-3575-a1ce-2d29b6a173ca | -6.2509 | -42.6121 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4255ee25-a69f-3904-b97b-9ec1623d313a | -6.71656 | -42.26224 | 2025-09-02 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52d9f791-57c7-36cf-9812-dd4725aa0779 | -6.39692 | -43.49629 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README29.md)
