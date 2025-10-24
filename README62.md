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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a744598a-8661-3b15-b0c9-bc66adc36abe | -6.0109 | -48.1257 | 2025-10-24 14:20:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0579f5ce-339f-3e51-8aa7-77db5313e82e | -12.8331 | -50.9338 | 2025-10-24 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| fa5bd2dc-0a46-3641-8544-b4f57fbb2800 | -6.9479 | -44.0263 | 2025-10-24 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 5051cd83-f322-33c7-9f69-d5a9dc996496 | -17.335 | -55.0366 | 2025-10-24 14:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 8d0092b8-bfbf-3c84-863d-86b7adde08dc | -12.1003 | -46.708 | 2025-10-24 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 58df864b-860a-37ca-8f04-82722036cc05 | -8.6145 | -44.8042 | 2025-10-24 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| ffd06805-5ffd-3561-99d9-731d48cda355 | -12.8328 | -50.9552 | 2025-10-24 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| a841379e-dc4e-392f-bc35-3ba3c3a07575 | -12.067 | -46.4189 | 2025-10-24 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| fff11e51-7c26-3183-92df-23315421aa34 | -5.7039 | -49.3066 | 2025-10-24 14:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4fd42c36-f634-339c-96e2-055083af33f6 | -6.8203 | -45.4542 | 2025-10-24 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 413542e0-1612-3d70-9d56-21367468a581 | -11.8727 | -50.1277 | 2025-10-24 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 4739f06d-dcf1-3246-8f47-084909c5a431 | -4.9122 | -43.2103 | 2025-10-24 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| eda240be-44bd-3ff2-80ef-e91324672690 | -19.0319 | -57.5382 | 2025-10-24 14:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| e33cd323-c0cd-35af-a862-d903c4216909 | -6.9291 | -44.028 | 2025-10-24 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 73d4dd92-a70e-3944-a8ec-e1331ee537ac | -6.8017 | -45.4332 | 2025-10-24 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 88dc3ccf-85d5-3904-a597-90d44a0764a8 | -12.8136 | -50.9576 | 2025-10-24 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| dd8c2f30-7f61-3b33-935b-56819f089912 | -1.2086 | -49.0625 | 2025-10-24 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f69822b0-05cb-3f12-b8ac-b6fb1b3924c4 | -12.0862 | -46.4162 | 2025-10-24 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 8ee142c2-4c6e-3261-ab99-37aceb14bfce | -12.0666 | -46.4416 | 2025-10-24 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 44cd5280-1449-37ba-bcd5-c79526630711 | -8.6145 | -44.8042 | 2025-10-24 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 67f5ac15-a139-3937-9fae-fda57ce39200 | 0.3589 | -50.9414 | 2025-10-24 14:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 67e199aa-45d2-36fa-aa3f-fbacf8294157 | -1.2085 | -49.0838 | 2025-10-24 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 4aae465e-5526-3c81-9c9f-16a079d6a582 | -9.2685 | -45.3484 | 2025-10-24 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4cbeb567-3f5c-3961-82f2-c5837317603f | -19.0319 | -57.5382 | 2025-10-24 14:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 97f4ff6c-6cd6-320c-a645-471070445845 | -17.335 | -55.0366 | 2025-10-24 14:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 61c5d7c1-f2b2-38ea-b8cf-666834f614b1 | -6.2498 | -46.3958 | 2025-10-24 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 1b3db74f-af47-341e-9fb4-2accda2ce026 | -6.9291 | -44.028 | 2025-10-24 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 772798f8-28fd-3234-9b0b-3fd866dd8ffb | -13.9151 | -48.3889 | 2025-10-24 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 905fe638-7c19-3081-b3a7-36f019e75ba7 | -7.0135 | -46.7143 | 2025-10-24 14:30:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 626363bc-0078-34cc-b095-6fce2555c435 | -14.3792 | -51.5255 | 2025-10-24 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 4b073d69-5770-300e-a262-72a61c13b572 | -6.1043 | -48.0979 | 2025-10-24 14:30:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 8cad1d47-afa4-3189-907a-9e64548e2696 | -8.246 | -47.1821 | 2025-10-24 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 909d1163-4106-39eb-9525-e59e66111c5e | -17.3037 | -58.077 | 2025-10-24 14:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| effc43b4-663d-301c-9beb-7376d6456a5e | -1.1901 | -49.084 | 2025-10-24 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| b4d3f902-948b-3309-8e17-96a2c072b5f7 | -12.8328 | -50.9552 | 2025-10-24 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| f380b116-a813-32aa-9ddb-a5e8c5f2a191 | -12.067 | -46.4189 | 2025-10-24 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 2b3f6b16-9af7-3361-a21d-a9707990052b | -19.0323 | -57.5174 | 2025-10-24 14:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 166c99d7-14c1-3a9c-b902-36b4625a0951 | -7.2488 | -49.3959 | 2025-10-24 14:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 9c63d6aa-6e9b-32d8-9ecc-cd21a6b16be4 | -11.8727 | -50.1277 | 2025-10-24 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| d04fa3ce-5c2f-35fa-83ed-e5c4af858fa4 | -4.912 | -43.2337 | 2025-10-24 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| e0883bc9-ee6b-35e5-8625-1e6539b6c805 | -8.3521 | -46.1697 | 2025-10-24 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c5ac8815-2c43-306f-b770-a7ea97727697 | -12.0674 | -46.3962 | 2025-10-24 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 2e4a5e39-cffc-361d-9766-013b74e05d0f | -8.2107 | -46.9862 | 2025-10-24 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| ec9f35d3-2de1-37cb-9aea-d5170f1475c9 | -17.3353 | -55.0156 | 2025-10-24 14:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| be6ec660-9e35-3ed2-81f1-b30a0779b6d2 | -6.3046 | -40.8588 | 2025-10-24 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 170.0 |
| ad32841b-779e-32f1-9332-9d4665d467d5 | -9.3083 | -45.207 | 2025-10-24 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 613ce4f1-5e09-3113-ac70-1c4e9348c573 | -13.9147 | -48.4112 | 2025-10-24 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| abb68eba-6ec2-355b-9456-3045c32f6968 | -13.8958 | -48.3919 | 2025-10-24 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 09d3db3e-ae32-37bc-8733-b50f2fc13143 | -6.9479 | -44.0263 | 2025-10-24 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| e651afc0-330f-3fed-8a6f-ceb136ddca8d | -6.0109 | -48.1257 | 2025-10-24 14:30:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 066cb36d-6872-3ca6-a85c-f2bb2737a81f | -8.3521 | -46.1697 | 2025-10-24 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| dc05a8a9-a32e-36e6-8cf4-4381d87310a7 | -9.6061 | -46.9099 | 2025-10-24 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| a059383a-3e08-3baf-a2ee-8bf7444e2718 | -9.5872 | -46.912 | 2025-10-24 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 45057b34-81c6-32f4-8643-3ea5943961a4 | -9.2685 | -45.3484 | 2025-10-24 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b4e74d68-2fc1-3108-b9f2-d60dea5ee4e7 | -19.0319 | -57.5382 | 2025-10-24 14:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| a8f45e4e-db46-3b8a-b0ad-30c60a7bc231 | -10.0577 | -47.0816 | 2025-10-24 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 1c20a43f-e2b3-3e91-b512-1c7a1fca25c8 | -11.927 | -50.3147 | 2025-10-24 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 824a3f5d-7443-3ae1-8ba6-6c56ae49ce1b | -20.2176 | -56.2857 | 2025-10-24 14:40:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c296b89d-fe7c-343e-ac00-4bf2fabda5d8 | -6.0109 | -48.1257 | 2025-10-24 14:40:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 83f10b35-a2d7-332d-8815-d9410d61b2c9 | -8.6804 | -48.587 | 2025-10-24 14:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 44.1 |
| b27c2ed6-6e73-34fe-b27c-2340b38ab4fd | -8.3519 | -46.1921 | 2025-10-24 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 2906d676-b075-3768-908c-1e5fc59134a3 | -12.1693 | -49.4428 | 2025-10-24 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 12c8dce0-e6e6-3b4a-bea3-ed54d0b0b765 | -11.61 | -44.1148 | 2025-10-24 14:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 546e26bf-37cd-3812-97a0-e1f87bd7a824 | -10.0384 | -47.1061 | 2025-10-24 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 50334dea-19a2-3fff-abdf-24262210e705 | -7.2486 | -49.4173 | 2025-10-24 14:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| e18ea8bd-25c1-3204-80e6-65b9720de633 | -9.3086 | -45.1841 | 2025-10-24 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f6e1f713-bab0-3747-8fca-5152ed1d9972 | -14.7456 | -46.6096 | 2025-10-24 14:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1cc13489-63f2-3b20-af94-588158ff8063 | -7.2488 | -49.3959 | 2025-10-24 14:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| ac527ba7-ed8f-3ccc-b1e6-3163f16653ce | -17.3353 | -55.0156 | 2025-10-24 14:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| add1afd4-7619-3461-a755-035f38320c18 | -13.9151 | -48.3889 | 2025-10-24 14:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 626bccfc-c4c0-3e50-a31b-49641c848afa | -14.2727 | -52.1152 | 2025-10-24 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 0a0f967a-185b-3ff8-9146-685adc6d6f30 | -6.2498 | -46.3958 | 2025-10-24 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| df1e6283-0a17-3e60-bc41-d96e7708afae | -9.284 | -46.9894 | 2025-10-24 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| b9d289c0-af4c-3027-8eb9-8f46eb64a654 | -10.0198 | -47.086 | 2025-10-24 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 44cb19c7-a582-359b-82d2-a1aa2584e6df | -8.246 | -47.1821 | 2025-10-24 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 63ba0a2e-2089-355b-8c9d-8d947faca262 | -12.0666 | -46.4416 | 2025-10-24 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0f74a847-2d17-3780-9cae-c9b2b81279c7 | -17.335 | -55.0366 | 2025-10-24 14:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| dc3f7de5-3de9-3564-a733-b31eabb9aaa0 | -4.1845 | -42.9979 | 2025-10-24 14:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 11f5ecd8-0bb6-3435-a6f6-eab1a1a13ed7 | -6.1043 | -48.0979 | 2025-10-24 14:40:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 4f69a813-b97c-3473-afc0-8bdb40f08c45 | -12.0862 | -46.4162 | 2025-10-24 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 10c9ae60-4abc-3252-81bd-360f2fa0ae7a | -1.1901 | -49.084 | 2025-10-24 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 7a57eafd-704f-3f5a-bfca-a7f81b9e5d08 | -14.3792 | -51.5255 | 2025-10-24 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| a6245ae0-70d1-33be-9241-0b32a8d7c296 | -9.3083 | -45.207 | 2025-10-24 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 140.7 |
| f33e714f-b606-3e0a-972d-53a02b2ac255 | -9.6058 | -46.9322 | 2025-10-24 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6b16af33-0db4-3377-8a88-13e99eb1494c | -10.0387 | -47.0838 | 2025-10-24 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 95370d7d-3288-3fa7-b2ee-f0f87b4ea6e0 | -12.067 | -46.4189 | 2025-10-24 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 205.4 |
| a5fd2e6c-84f2-3512-a054-e3bbb41f4194 | 0.4877 | -51.0032 | 2025-10-24 14:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 6c1fdb66-734e-3928-af7d-69aaa38a7228 | -6.9479 | -44.0263 | 2025-10-24 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a6f2a85a-4ee6-3d2d-89c2-ed4d589d9e16 | -7.8159 | -45.3875 | 2025-10-24 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 4ec09114-070c-3883-b7ac-9a08c2276ecf | -12.8328 | -50.9552 | 2025-10-24 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 9cc971a2-8e4e-33ac-8799-d0d12003f541 | -9.5869 | -46.9343 | 2025-10-24 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| f8825cf4-2c6f-3632-8977-31087cc6fc83 | -13.8958 | -48.3919 | 2025-10-24 14:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 107.5 |
| b24ca859-2947-306e-9ea8-b0bbd2a93262 | -7.8348 | -45.3857 | 2025-10-24 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e199bfa0-6c5e-3915-9cc1-0049e4c2f0bc | -14.2974 | -51.7927 | 2025-10-24 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 4021cd02-3452-388f-9875-e6397fdc6f49 | -11.8727 | -50.1277 | 2025-10-24 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 2e63c141-fd37-3bcc-ae33-a9f87f5a5d13 | -1.2086 | -49.0625 | 2025-10-24 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 74736596-df8e-372f-97d2-c50d1868adec | -12.0674 | -46.3962 | 2025-10-24 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| ca4f56c4-4bad-34a6-b071-50970d5f33d4 | -9.625 | -46.9078 | 2025-10-24 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| d0e69079-4a17-3f52-b6f8-fa3e5546342e | -7.0135 | -46.7143 | 2025-10-24 14:40:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 80b5816a-ba1a-3bca-a4f9-98548c838f86 | 0.3957 | -50.9412 | 2025-10-24 14:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 63.9 |


[Clique aqui para ver as próximas entradas](README63.md)
