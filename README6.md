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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37de85dc-f4a5-3ef3-b891-0dc9ea766051 | -3.7994 | -43.895699 | 2024-11-15 01:08:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a38ab91-d143-3a84-a00f-20b736a5f460 | -17.577299 | -57.5443 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3805adb7-0e93-346a-bc6b-1698c53047d8 | -16.955 | -57.6441 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0490f51a-550f-37bc-b345-22654d232420 | -17.576599 | -57.438702 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 066b2282-9e5c-3538-8336-defcf943a176 | -17.5716 | -57.566799 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2b446b8b-9be1-3f72-bd65-15aa77b69d99 | -17.567499 | -57.546299 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fba61e12-55a4-3aee-aa25-20865c0abba0 | -16.132999 | -54.0299 | 2024-11-15 01:08:00 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b977e21-9cc9-31d1-87d3-ce20acda803f | -22.8736 | -54.669601 | 2024-11-15 01:08:00 | METOP-C | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf4af8be-840e-3257-8e93-813f6d4f5c02 | -17.585501 | -57.5853 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f2348822-4611-3935-925f-62a403afc417 | -14.2879 | -57.636002 | 2024-11-15 01:08:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff27731-34be-3337-8b25-ed4277532f97 | -17.7106 | -57.5481 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5459ad26-9cd7-3708-bc01-e2658b34994c | -17.7085 | -57.5378 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7ed64cf3-cc54-3f35-9862-0c8d3caf4b49 | -17.6022 | -57.464802 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6c4f20cd-6c3a-3636-abe0-27c9d88c7ed1 | -17.587099 | -57.542198 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8878b9bd-6af5-3ea5-8c3e-c617e220a861 | -17.719999 | -57.492802 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 040bd3f1-e3ce-35e0-9e5f-cd111578a8d9 | -17.236 | -57.469101 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a38b0f4d-2198-394f-9f40-efb36de1d5c2 | -17.5814 | -57.564701 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1f622455-bde3-3995-ba18-564c8c8a0461 | -3.7898 | -43.897999 | 2024-11-15 01:08:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0ecc69d-a1f0-3712-9ba3-2e1144a8ef3b | -17.630301 | -57.554401 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 37b80fec-beec-3476-a405-f22706b5ad19 | 1.0488 | -51.103901 | 2024-11-15 01:08:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| dae8a2d7-a497-3143-a548-e78ecbc82ab9 | -22.055599 | -56.0131 | 2024-11-15 01:08:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 14a37fed-4870-3c37-92b1-b33d28e3fb86 | -3.7978 | -43.93 | 2024-11-15 01:08:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e641656-981e-3af1-a82c-382ad345d9b4 | -16.131399 | -54.022701 | 2024-11-15 01:08:00 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 33a7799d-8773-3150-bfc5-83c1fcdaf078 | -16.0944 | -60.094601 | 2024-11-15 01:08:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a503f55a-ce35-3dc5-af7d-ad859926fcc4 | -17.2418 | -57.446999 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f4351ce0-784a-391e-b334-10eda02fb66b | 1.3073 | -60.3988 | 2024-11-15 01:08:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 85d082f7-031f-3bc0-89e2-41bb21cad3af | -17.6947 | -57.519501 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 92d370c2-df1d-3856-aa7a-43871536558f | -19.770201 | -55.402901 | 2024-11-15 01:08:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 72344334-e7c8-36fa-8b9f-5fda0c7d4797 | -15.2917 | -56.5154 | 2024-11-15 01:08:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8191769-6aa5-30d2-8c72-64febf53f9b0 | -17.610701 | -57.558498 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac5f5891-911f-379d-85e7-f4bbe52e4c14 | -17.233999 | -57.459099 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12e71850-1523-37ba-95ae-d4529c17ab2e | -17.6043 | -57.474899 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eff6c618-d463-3f0b-8b42-f502283d669e | 1.0516 | -51.091599 | 2024-11-15 01:08:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c071f37f-f203-3d83-a50f-3bbbc884d539 | -17.5912 | -57.562599 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eea8e30f-3647-368a-8829-a038573bed88 | -17.688601 | -57.488899 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 65b82c9c-5b08-32c7-a061-2d0b401b120e | -17.6185 | -57.5462 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1818022a-b946-3fe3-9c2b-4cfeb3c4cf92 | -17.6674 | -57.5359 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 703e83ce-3fea-3838-b676-19ea48ebe638 | -17.649099 | -57.444302 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3741d381-81bc-3c5e-8d87-58ab60346323 | -22.4869 | -47.672501 | 2024-11-15 01:08:00 | METOP-C | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 52ad8137-0193-31dd-8577-3ba45340c18e | -16.943199 | -57.636101 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 35b9dcdb-8fec-37d2-8e7e-ba187a406f44 | -14.2898 | -57.645302 | 2024-11-15 01:08:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ffd83968-ec4c-3777-93be-9c7f7a2258d2 | -17.221701 | -57.195499 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 535e0ce2-588e-35ba-83ca-df076e1f4a91 | -17.5655 | -57.536098 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 99cb586d-fea3-3084-b992-342d9cbeb477 | -17.257601 | -57.474899 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3147d05b-a5a3-33ab-ad7b-bc813596a46a | -16.104099 | -60.092602 | 2024-11-15 01:08:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79f9d9cc-b472-3881-a09e-b5d0068bbb32 | -17.5557 | -57.5382 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93ecc4d4-7953-3c95-81b7-072bcebdf13d | -17.5835 | -57.575001 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9b5a7bc-0e89-35f0-86e6-3ca7d84a5676 | -17.5753 | -57.5341 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f221a12-04af-336d-b0ef-ee4ebaba1112 | -17.2516 | -57.444901 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e202ee17-d01b-3580-90bf-4b03a0ecccb8 | 1.3035 | -60.415401 | 2024-11-15 01:08:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 091cf802-607b-3845-951e-c94c6756d0b3 | -17.580601 | -57.4589 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b1993d0-e40a-37bf-ae66-f1f1ba33b801 | -17.669399 | -57.546101 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 917e51e6-5e98-326e-a6f6-cbdc181c0e50 | -17.5786 | -57.448799 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c88b8db3-10d5-3bc7-a3fb-9efd88626765 | -17.6471 | -57.4342 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ab41583-80a4-3369-a785-4ba290bd8d24 | -3.7802 | -43.900398 | 2024-11-15 01:08:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94479fbc-7657-3058-bda3-b40dc0ae8ce9 | -17.6401 | -57.552299 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e82d1754-fee8-38a1-b8c8-a14685e0f668 | -17.5867 | -57.4893 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 96b2ca29-6fe1-359d-84c3-9ff788186907 | -17.5945 | -57.477001 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7419b846-d2a1-3bcb-9207-b13ca33a14a1 | -15.2935 | -56.5238 | 2024-11-15 01:08:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57d6e599-e6e1-3f75-b2ce-10f6fb236afe | -17.5737 | -57.577 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5d332f3c-2d66-3d41-a7a5-5ac3e5aeff9e | -2.3267 | -46.881901 | 2024-11-15 01:08:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db7947ae-f45b-3ea7-8c89-50f1b3497491 | -17.7008 | -57.550201 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 63d09762-221f-3dfc-95ea-205ea94f9361 | -17.632401 | -57.564701 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 24e1e83d-007e-3a63-9b77-61c26ee5d9d6 | -17.2654 | -57.462898 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 136859f3-60ca-39e0-aa9a-0459835f4587 | -19.773701 | -55.419998 | 2024-11-15 01:08:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6250335f-05de-3adb-aa19-2ee481bbb0f9 | -17.243799 | -57.457001 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21a513b5-9956-3962-9035-629a77bb28e2 | -17.7045 | -57.517399 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 71dbe080-b868-35e2-ad72-8def96eacceb | -22.871901 | -54.6609 | 2024-11-15 01:08:00 | METOP-C | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2f125557-f67e-3549-b51f-52d1c8497853 | -12.5751 | -57.813 | 2024-11-15 01:08:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39cd6ea0-fa85-3a3a-877d-7e9f4cd129a0 | -17.6283 | -57.544201 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 55675042-b08c-352f-a4c0-b23192cde6e1 | -2.3216 | -46.860802 | 2024-11-15 01:08:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5893ec62-2be6-3bed-8907-23b35d2af77a | 1.3054 | -60.407101 | 2024-11-15 01:08:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 09b038d0-1382-3c38-b8b4-18f5da7cdd0e | 1.0649 | -60.600498 | 2024-11-15 01:08:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 036c7669-3fd7-36ab-a995-f736c43b1c87 | -17.2458 | -57.466999 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea9daa05-e588-3235-adbd-0f1c3d229fcc | 1.0795 | -51.148998 | 2024-11-15 01:08:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 07697606-727b-39fa-8da3-25d16e3b9703 | -15.2953 | -56.5322 | 2024-11-15 01:08:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a7fe680e-dd03-33f3-a38e-02a5ad4e9e68 | -17.5933 | -57.572899 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f722f98f-cb49-3e27-b024-f1d0536dddc9 | -17.590401 | -57.456799 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d0538e51-9380-3a6c-849f-5e7b78bb839a | -2.3313 | -46.858501 | 2024-11-15 01:08:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42a8e968-36af-3d09-86ca-e65a4ddde765 | -17.6381 | -57.542099 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 274a4d83-fd42-3add-978c-62cd0572ae00 | -17.232 | -57.4491 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a09db652-e69f-3ca1-9e4d-d2e436ec8c25 | -22.04887 | -56.00663 | 2024-11-15 01:17:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a9f46c38-84a6-396c-9f2b-cb7aaf970981 | -22.0595 | -56.00534 | 2024-11-15 01:17:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 79985860-d3d1-3ffd-ad29-bbc819814b1c | -22.26667 | -49.71365 | 2024-11-15 01:17:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| b75c8165-14e5-311b-bee4-86c0d2347cbc | -22.48581 | -47.66497 | 2024-11-15 01:17:00 | TERRA_M-M | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 94817a05-bf5a-3327-a16a-384fae8a9710 | -22.2338 | -49.62285 | 2024-11-15 01:17:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| a3de9e3b-1abd-36a2-be87-8931d3e6f224 | -22.86846 | -54.66284 | 2024-11-15 01:17:00 | TERRA_M-M | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 36.9 |
| cc81d579-9c29-3e6b-a53d-07b071b2831b | -22.48797 | -47.67806 | 2024-11-15 01:17:00 | TERRA_M-M | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 5adbf6ac-09a4-3429-a1e7-91dd547ab0cc | -21.90547 | -56.46118 | 2024-11-15 01:17:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fbf3c629-295b-38d9-84d8-4fdf2f968736 | -17.60056 | -57.46223 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 747b0b18-1f6a-34e4-a531-8318b76351bd | -15.62784 | -57.5155 | 2024-11-15 01:19:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 439618fb-2b92-3c71-be57-125974846e1d | -17.56479 | -57.54223 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 4560d1c2-f054-35a7-9a19-b1ae019813e6 | -17.64577 | -57.45075 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 72a062fa-e71b-3178-aeb5-3cc61758e86e | -19.77511 | -55.41185 | 2024-11-15 01:19:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 39.0 |
| 1a041907-a76c-3fad-bdd2-153e195027d4 | -17.24731 | -57.47206 | 2024-11-15 01:19:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.0 |
| 1e44f5e2-e876-3e10-b844-b67f339f0838 | -16.1314 | -54.03679 | 2024-11-15 01:19:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 96851ad9-b411-394f-94fd-61efd84ed8a4 | -13.48811 | -60.67307 | 2024-11-15 01:19:00 | TERRA_M-M | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 20.3 |
| c195f46f-ff57-3906-b096-040423375a24 | -16.09907 | -60.09663 | 2024-11-15 01:19:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| d95871e2-2f59-37df-9087-7f07760e55fc | -12.57762 | -57.81424 | 2024-11-15 01:19:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3599ac51-e702-3ebd-b6a0-5319967f2030 | -17.71159 | -57.53304 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.3 |


[Clique aqui para ver as próximas entradas](README7.md)
