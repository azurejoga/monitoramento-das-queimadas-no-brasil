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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1000ecb-3b31-320f-abf6-bf8cee71d9db | -20.7402 | -44.48791 | 2026-08-22 04:29:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 31fc1ff0-3e54-3c5f-aefa-28e69577032e | -14.31704 | -53.00489 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fc9f2aeb-4e15-3286-a5a7-595feb5ab828 | -17.9868 | -44.41824 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb5c0ae5-6d02-3ad4-9231-01cb3d9bb778 | -18.08605 | -46.95134 | 2026-08-22 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cc6c966c-6adf-3ff6-bb76-0bf96b7e4373 | -18.75968 | -43.80414 | 2026-08-22 04:29:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2994321-e3ba-3198-99e5-fdd433f8bcc6 | -16.02707 | -52.17553 | 2026-08-22 04:29:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 402acdb3-2b8d-3d9d-8fc8-c58922c788df | -17.97278 | -44.37437 | 2026-08-22 04:29:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c46e5f20-6db1-3b25-bc4e-deefbe5e4a5e | -19.46273 | -46.81274 | 2026-08-22 04:29:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5771977-63b3-3820-bc3b-3b72f14164ad | -18.33627 | -42.46323 | 2026-08-22 04:29:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d1a595a7-768d-3fef-8165-43563782b414 | -15.68003 | -53.77566 | 2026-08-22 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 96d2fc29-df37-3bf5-9cfc-0c496d555d45 | -15.69955 | -53.78288 | 2026-08-22 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b20e8eb-a6b3-305a-9985-fe802e6ef166 | -19.784 | -45.6649 | 2026-08-22 04:29:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04d6f77f-e06a-3a13-b0cf-66b21034a725 | -16.49752 | -55.18484 | 2026-08-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dfb77e6b-f8ec-3b94-8feb-fd060b246b78 | -18.10257 | -47.17752 | 2026-08-22 04:29:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca684882-389e-3820-8a24-16d9f5be165d | -13.83239 | -54.00421 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70272934-0ad4-349c-b13e-0fb2f81bdf69 | -13.99881 | -53.70743 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0cfda0ee-2d7d-387d-822d-00c3894445db | -18.95101 | -50.63495 | 2026-08-22 04:29:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d09dfeb4-b6db-3f6c-99ab-539e701011c8 | -14.56454 | -53.04422 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 406d6cbc-088b-3f30-944e-6184153f9f8c | -16.71924 | -47.69916 | 2026-08-22 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97a9c194-06e7-3eca-a191-62f7c2863148 | -13.94744 | -53.84996 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a859e01-da93-352c-bfd2-10c544cad0a0 | -17.97416 | -44.36388 | 2026-08-22 04:29:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12c4f286-3040-3f2b-81e7-42c3ebd57e2f | -15.07026 | -45.32783 | 2026-08-22 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51faa162-2a39-33f5-b4b2-d1e3f322e213 | -14.5588 | -53.05382 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 618bc49f-c36f-3a82-85e2-bca9b4698229 | -20.83 | -45.41543 | 2026-08-22 04:29:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8c04fc4e-198d-3552-8349-134255835ba4 | -16.50184 | -55.18586 | 2026-08-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 83dd7c41-34d3-356b-ae58-4575c8bee6c8 | -13.99197 | -53.6743 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8568d3f2-5f6d-318b-aa87-ef6c8181cba6 | -17.91878 | -44.42303 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e392bec-f914-371c-b48b-460774666775 | -17.95768 | -44.3985 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24e8dfdf-6ed7-3972-99a8-f8a9829ad4e2 | -15.21712 | -52.78091 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81ded72f-c35d-3e0c-82d7-1438533ebdac | -14.56213 | -53.01187 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83080f3e-6781-33da-959a-159bc0aa8717 | -18.76375 | -43.8048 | 2026-08-22 04:29:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edcd61ea-5e70-377b-bf56-3556c1ee0efd | -18.63142 | -47.29464 | 2026-08-22 04:29:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4db687cd-ff75-3465-9bb0-066075b5b0ed | -19.46215 | -46.81683 | 2026-08-22 04:29:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a767e2b0-3149-38fe-81f1-6f33e70d04c6 | -13.99128 | -53.67815 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a333bb98-69ae-3d21-b021-a4757ae7a75d | -15.34352 | -52.92967 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c9800a4-0916-381d-be3c-534d2027d856 | -15.86474 | -55.56217 | 2026-08-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e521235-bdf0-37bc-911e-c8b898ace43f | -13.87887 | -53.98801 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af6bef71-f6f2-3bea-aa7f-6eb5950f6ab8 | -13.53563 | -58.11417 | 2026-08-22 04:29:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f58ac4d-46aa-3257-bb9a-ddf744933a86 | -18.6354 | -47.29132 | 2026-08-22 04:29:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17827e70-2ccc-3efd-b6ab-4217c0c3fb10 | -14.44335 | -53.06796 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a3f6654-bf93-380b-995e-f162508580fc | -13.93979 | -53.84462 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15d775f1-c71e-3f7d-80c9-ad87bab4d9ba | -16.29362 | -57.66804 | 2026-08-22 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fda66d65-0cf2-3b0c-bd75-d4162ffe5162 | -14.98644 | -52.67367 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ec502ff-bbcf-3458-bc2d-a7cb4719c055 | -16.43132 | -39.52088 | 2026-08-22 04:29:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5e61f435-121b-3504-8825-959d0512bc79 | -17.69239 | -44.44477 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f23d2fee-dcc7-334f-8148-41c93d0a856f | -17.69108 | -44.4548 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16fc917f-86e1-38eb-94af-90993828dbf7 | -18.53122 | -48.24781 | 2026-08-22 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4dd90d8-1c04-3b3c-b389-39cb8f48257e | -14.39639 | -51.79873 | 2026-08-22 04:29:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9b3501a9-20dd-3bd9-b5ff-8b160ea6f054 | -14.06577 | -58.81633 | 2026-08-22 04:29:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45e39747-2b52-3f21-bb5e-cf8ae6901f85 | -18.63881 | -47.29188 | 2026-08-22 04:29:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15db67c6-4fe4-39fe-a8af-307dc0171ffd | -14.31394 | -51.86383 | 2026-08-22 04:29:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 32d1b599-53fc-366a-8c9e-cd729b17b5e5 | -19.10788 | -42.17645 | 2026-08-22 04:29:00 | NOAA-21 | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f925e554-f775-39e2-87b0-24875fb23890 | -13.99469 | -53.70667 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5c89a10-a739-31a6-a93c-58aa0f0d57e9 | -17.95873 | -42.73318 | 2026-08-22 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 54f2cf86-eb93-3874-aff0-c40727da48a9 | -14.42648 | -51.79952 | 2026-08-22 04:29:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ace91f4-ab8a-3f0a-b568-e981d6381f2f | -13.82884 | -53.99971 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89e75551-90c3-3d78-9c14-db951c8a260a | -13.82814 | -54.00362 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf485494-ef99-36b0-b2db-71ec3f397b28 | -16.81422 | -49.28343 | 2026-08-22 04:29:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7c6ac82-b9b2-3614-a3f8-6b8425db584e | -16.52451 | -42.13239 | 2026-08-22 04:29:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d646dea2-9070-3b0d-9d78-d347c14aa17c | -15.18253 | -48.74039 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 79465e97-6fe4-33c4-8523-2734d4d0ed5c | -17.91875 | -44.39268 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b25e537-1c83-31dd-9f47-ea8fed31bf8f | -15.17147 | -48.74588 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8235ae43-75b6-3658-a346-0f7d922d09d5 | -15.0631 | -45.32674 | 2026-08-22 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1e2d306-bb17-3480-a347-cba564fd8df0 | -16.27725 | -57.66989 | 2026-08-22 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c4132ed9-95ff-3ac4-816e-cd01209ab48b | -18.09005 | -46.948 | 2026-08-22 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 719c2e31-001a-3adc-bcee-b35f15a82d7c | -15.23984 | -52.83135 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66ab9ea9-32a9-37e4-912e-7dae1ba1b886 | -15.20648 | -52.77415 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bb5b116-9dba-33cc-8ebc-47a53cd7d04f | -15.34278 | -46.06706 | 2026-08-22 04:29:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a44d846e-fe16-3e75-b5de-599c98a32099 | -20.44358 | -43.60699 | 2026-08-22 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e442b2c9-0ce5-316a-bcd8-49ef75fd4c29 | -16.48797 | -47.94894 | 2026-08-22 04:29:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a10f6853-1dff-30a9-8ea3-0441cf7d1e21 | -15.24279 | -52.83704 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f55ae264-b0e9-304c-a4ed-6c51977f86e2 | -17.96871 | -44.40515 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9fdd8f1-3f2d-33af-9823-c5e77705ad93 | -18.7145 | -47.58669 | 2026-08-22 04:29:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ce9f59d-4fce-3dbb-84e6-fde40083881d | -13.88012 | -53.98065 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8909a48c-af1f-3c0b-ab66-54dd7dae384d | -15.21414 | -52.77545 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5f7f00e-d306-3e41-be94-f759704c8114 | -13.87814 | -53.99199 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea97c929-50e1-3c83-b0d4-b9c343845113 | -15.17809 | -48.74697 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 55838ced-bb99-3d44-8ce2-b12318d78dbd | -20.63062 | -47.44564 | 2026-08-22 04:29:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 438d84f8-0264-34f3-9a01-66945ecca160 | -17.92073 | -44.40805 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d32a1cd1-c6e2-3067-8fbf-3bd06dcc3225 | -18.08783 | -46.94466 | 2026-08-22 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| fc0d0418-950c-39a8-b921-fdd009aba911 | -14.00707 | -53.68503 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2905f7f4-b7a3-34e4-9b63-cc4d4cb719c0 | -14.55704 | -52.99492 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6372fb12-2b9f-3609-aad3-6ecf6d2adf59 | -14.72918 | -47.13981 | 2026-08-22 04:29:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b5031fa6-e683-3062-a10c-e036a73e2a96 | -14.55128 | -53.00466 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea34b71b-ec12-3aeb-b385-279645030dd3 | -17.68979 | -44.46476 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e450a1ea-96cb-3ba3-96c4-1d4f41c3b6a6 | -19.64953 | -46.03338 | 2026-08-22 04:29:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edb8e3bc-53ba-302d-9d32-bb0c11bdbc51 | -15.18859 | -48.74505 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 970ad420-ef7b-3f58-8bd6-2cb510ab7407 | -14.00706 | -53.70893 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 89ffb0b0-4d07-3730-bd65-edd0287e5f3e | -16.30716 | -53.16341 | 2026-08-22 04:29:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e436d436-4150-3888-8af6-1dc55c1544d9 | -17.43738 | -44.94527 | 2026-08-22 04:29:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a446070-3dc6-376d-8686-156ad65fdeca | -14.56513 | -53.01783 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2ceedb3-8c64-33ea-bd35-b7ac3d4eba88 | -16.95755 | -46.11887 | 2026-08-22 04:29:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6c582f11-d678-301a-88fd-2c346bc68bd2 | -17.96308 | -42.73362 | 2026-08-22 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ac8f89ee-1c56-3a04-860b-673da0dbdcf6 | -14.33675 | -52.93933 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9fb804b-9d11-3cb6-99a9-6132b8e4c266 | -15.1759 | -48.73929 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f35d8f09-b598-319a-8a83-b80a0ad982d4 | -15.5734 | -46.42738 | 2026-08-22 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9d55461-5207-3240-b586-97fd8c141143 | -14.00294 | -53.70818 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0aad0504-9325-39a2-a258-f76b2e53927f | -14.31318 | -51.8683 | 2026-08-22 04:29:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 49599814-f509-3e9b-bce1-7d60d593042e | -20.62716 | -47.44504 | 2026-08-22 04:29:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14f51221-27a1-328c-9bc0-26791976d5d0 | -17.69625 | -44.44536 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README33.md)
