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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47f34296-7694-35d9-ba24-cb04a462553e | -9.7126 | -65.0951 | 2026-10-06 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a3b41e00-ef00-3f6d-a70e-009de73ff5e8 | 1.8583 | -55.8018 | 2026-10-06 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 440e331a-1e04-32c4-a976-cfca69ba6412 | -9.8824 | -44.8171 | 2026-10-06 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 45755240-1088-3d61-a8b8-9f9a3db30509 | -8.9873 | -65.4379 | 2026-10-06 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| fc6e9248-eac3-3832-b5a0-376c18528939 | 3.1098 | -60.5943 | 2026-10-06 14:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| bde0b4d4-55ae-3403-956e-f09e056271df | -2.7874 | -51.6719 | 2026-10-06 14:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| fb0ef9b0-b6ca-3db7-a103-f2210fad3e40 | -9.1335 | -65.8813 | 2026-10-06 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8f6ae1c3-d317-3f25-a63c-35e1dd72fdb4 | -9.1222 | -64.3843 | 2026-10-06 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9fe246dc-beef-3d3b-a6f1-cff57b2b1f1b | -10.9758 | -45.4324 | 2026-10-06 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 409.2 |
| ba3c8563-3cba-3865-b1ab-ff032c274480 | -11.6758 | -43.658 | 2026-10-06 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 211.8 |
| bb188928-d50d-343f-9cc7-2112907f499b | -11.6763 | -43.6343 | 2026-10-06 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 6bed74e7-6038-3323-b04f-fd0a765adbb5 | -7.2079 | -44.3024 | 2026-10-06 14:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 993e2637-06d3-3310-8e1e-f450c59efd8d | -11.7143 | -43.652 | 2026-10-06 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 378.5 |
| 1d79a454-e8c6-301c-afda-b51b1fda517a | -9.1407 | -64.4024 | 2026-10-06 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| fff0bc25-15ca-3dc9-9a1e-c0335e69f1aa | -11.7147 | -43.6283 | 2026-10-06 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 0b497be4-d50c-3b54-ba88-ec7559ba1e3d | 0.4465 | -60.5442 | 2026-10-06 14:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 2a5b76fe-4641-3c4f-be6a-441064d9bddf | -11.8315 | -43.5391 | 2026-10-06 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 265.9 |
| 3f2c7dac-c6e5-3f6b-89a3-95b6c21eb4fc | -11.21 | -46.2655 | 2026-10-06 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 3821ef1b-5634-39f6-ad06-f76bb878e8d8 | -9.8261 | -44.7781 | 2026-10-06 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| bdd06880-a97b-3355-942c-a3c457e8713e | -11.6382 | -43.6166 | 2026-10-06 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 0bdf4af9-c28f-3f4e-89d6-847bf3be9692 | -11.6575 | -43.6136 | 2026-10-06 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.1 |
| bc702cd1-2fb1-34ac-8332-35d7abe0f54a | -6.7068 | -45.5539 | 2026-10-06 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 52814b9d-9693-367a-b773-4d8ed538d41d | 1.7855 | -55.5461 | 2026-10-06 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 8a623275-1cea-31e7-bff5-1d8949e8e1c4 | 1.8038 | -55.5458 | 2026-10-06 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 255d5191-3ba7-3a2a-97b9-638a72f75d22 | 1.7304 | -55.6259 | 2026-10-06 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 22219f88-205e-37c3-b1f9-426c6258a862 | -9.0058 | -65.4373 | 2026-10-06 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c3d2759d-93ed-3fa7-b2af-1b21769afade | -9.1613 | -68.2568 | 2026-10-06 14:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0193632c-7ce3-30f1-be01-f7fef2ad907a | -9.8619 | -64.9958 | 2026-10-06 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 1ef6a2f5-b26f-3f46-b810-eb9bae3f9319 | -3.3358 | -44.5859 | 2026-10-06 14:50:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 01ef25c4-eccb-3aa0-8207-f53309079444 | 1.7854 | -55.5856 | 2026-10-06 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| fc77e35a-f5f2-3d43-8541-a0e28392ed67 | -9.8257 | -44.8011 | 2026-10-06 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 1c3f2087-14b5-3340-bed7-04dfb3acb6e5 | -10.9762 | -45.4094 | 2026-10-06 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 252.5 |
| 3c6ffdbb-c8f7-3ce8-81e4-00e82baf6913 | -7.1778 | -42.0055 | 2026-10-06 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 3cdf8e9f-9721-38c9-a55c-8e324f2c1c32 | -6.3311 | -43.7557 | 2026-10-06 15:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 2b5fc4cd-f407-3f66-b8ca-cd54984a3552 | -9.1407 | -64.4024 | 2026-10-06 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8f321ca4-a864-3a19-ac53-9ea17b6817d9 | 1.5832 | -56.0024 | 2026-10-06 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| a5d3e64a-126f-3b50-8dc1-1529b928a47b | -11.657 | -43.6373 | 2026-10-06 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 677.7 |
| a9bc4638-d7d2-3f19-ad21-83381cef51ce | -9.8261 | -44.7781 | 2026-10-06 15:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 424a97ac-43f6-3f12-a3ad-9689e625c5ab | 1.8584 | -55.7624 | 2026-10-06 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6bf150b5-8b88-3ef8-9bba-303e4c662ad8 | 3.128 | -60.594 | 2026-10-06 15:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f9cd9874-ea44-3b95-8cb8-902bf0194386 | -9.1076 | -67.703 | 2026-10-06 15:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| eb699025-842f-3601-a874-c0215458f8a6 | 1.7854 | -55.5658 | 2026-10-06 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| cae27901-1600-3900-8096-00c3c75060aa | -9.7312 | -65.0944 | 2026-10-06 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f0ce75a3-8b4a-3d4a-9ca1-25a2882ddf5f | 1.8038 | -55.5458 | 2026-10-06 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| fa992c27-c9c0-3ad8-9903-de8524193052 | -12.1948 | -44.6554 | 2026-10-06 15:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 502b4be4-d329-367c-9243-fb8da2ce73b6 | 1.7855 | -55.5461 | 2026-10-06 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 12b435f8-cf03-3996-98d6-d34cd8ab655a | -9.8257 | -44.8011 | 2026-10-06 15:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| af224b93-1113-3d74-a8b6-baeb56b44ff9 | -0.3952 | -52.0768 | 2026-10-06 15:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 87aaa9c7-9eb3-3765-981b-8a7c2eb2886b | -11.6566 | -43.661 | 2026-10-06 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 33a2ba4f-3eb3-379c-90af-e01ed514e051 | 1.7304 | -55.6259 | 2026-10-06 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 42478ec1-0587-341a-a2d2-9780f8195b5a | 1.7304 | -55.6061 | 2026-10-06 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 130e566a-3b7b-3ee8-a340-4361b7e3af7a | 1.7854 | -55.5856 | 2026-10-06 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 127279e6-ac1d-31b3-86d5-63f19f73b0a5 | -11.6763 | -43.6343 | 2026-10-06 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 283.8 |
| 71b6ceab-a56d-3b9f-9037-23ca177862cc | -11.4503 | -43.4091 | 2026-10-06 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.4 |
| c4a03906-86de-3e7c-bca6-6d5543fbb285 | -11.21 | -46.2655 | 2026-10-06 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| efbfa019-4c3b-39da-8552-f2b522980339 | 1.8583 | -55.7821 | 2026-10-06 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 24cd64a0-45fb-302c-b91b-9d1200c4c5f2 | -10.9762 | -45.4094 | 2026-10-06 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 75925aed-a27b-3245-8686-89ca6f235f77 | -9.1408 | -64.3836 | 2026-10-06 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| de76db71-ba98-349b-a03d-c97e2922111e | -10.9571 | -45.412 | 2026-10-06 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 035ae236-f3b2-3c1f-bb86-fa80df247b3c | -5.6748 | -53.4879 | 2026-10-06 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 81cc8ef1-12c8-30ee-8983-b97daa092674 | -11.4507 | -43.3854 | 2026-10-06 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 272.6 |
| b0f93b51-fbe7-3007-8473-a838cb49c9ed | -10.9575 | -45.389 | 2026-10-06 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| ac980946-a6ef-3bbe-a938-03edde52df6e | 1.9681 | -55.8792 | 2026-10-06 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| bd9cded1-f444-3b60-a410-bef64173595c | -9.9175 | -65.0313 | 2026-10-06 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c145260c-ad3f-3a7e-96b6-a03dd71da83f | 3.1098 | -60.5943 | 2026-10-06 15:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 1c66b66a-af0d-3bae-adb7-c5b42aba25c1 | -11.6575 | -43.6136 | 2026-10-06 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 845.9 |
| 4f4b963f-c13d-3065-9e85-56e00b3ae3af | 1.9864 | -55.8789 | 2026-10-06 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 4a94aff1-464d-3d14-8446-ed941afe52be | -9.0347 | -67.39 | 2026-10-06 15:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 11e6b0eb-3c76-39bc-9174-c7e2b08429b0 | 3.0733 | -60.576 | 2026-10-06 15:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ef979b6d-f973-3302-b298-b43f30a36076 | -6.7066 | -45.5765 | 2026-10-06 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 342.8 |
| 208758a5-c072-3cfe-99b5-29ceb47c909f | 1.5649 | -55.9829 | 2026-10-06 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 32b74835-24ec-321e-b4e8-dbf54db9fe17 | -9.1613 | -68.2568 | 2026-10-06 15:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 078e63ef-07cc-3cf2-b543-f4c7dc5e76d7 | -9.1222 | -64.3843 | 2026-10-06 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 112d784c-d861-375a-8aaa-3423d7485e36 | 1.7303 | -55.6456 | 2026-10-06 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 036c01b4-c1ba-3331-bcfd-f41113c1c7b5 | 1.8038 | -55.5458 | 2026-10-06 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a1304990-9584-35cd-a481-9a37ecef66c1 | 1.7304 | -55.6061 | 2026-10-06 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 6e7268a7-b56c-3c2f-8b72-eeeab5b3c68a | 1.7854 | -55.5856 | 2026-10-06 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 9b63a8b0-a7c4-375c-88b1-f08837c9be72 | 1.5832 | -56.0024 | 2026-10-06 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 5a9f6b99-ca97-3960-b89c-9f54707be39d | -11.21 | -46.2655 | 2026-10-06 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 6366d11b-f2b6-3fbe-8d82-d3b9f100e920 | 1.7304 | -55.6259 | 2026-10-06 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 698ca071-f965-3b24-871e-4c2e12ef292e | -9.1408 | -64.3836 | 2026-10-06 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 693ee7d3-9ed9-3fd4-b6ca-d3b0a7baa259 | -9.1407 | -64.4024 | 2026-10-06 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| dee7c98c-1dcc-397c-a787-2c9409361f2f | -2.7796 | -54.0937 | 2026-10-06 15:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 208.9 |
| 81372ef1-4835-3bff-b9d8-9000e3bae067 | -9.0097 | -69.4036 | 2026-10-06 15:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 88d49f74-d4de-36c8-8684-9f8518789fab | 1.9864 | -55.8789 | 2026-10-06 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 194be4ab-4dd6-364a-b582-9326c30be233 | -9.7127 | -65.0763 | 2026-10-06 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| d6d4f249-b674-3347-acbb-88c83c112333 | -11.7147 | -43.6283 | 2026-10-06 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| b6702d89-b584-343f-a42e-96089046339b | 3.0916 | -60.5757 | 2026-10-06 15:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 151059c0-3256-3c1f-b88d-143ef0a9ff46 | -9.0098 | -69.3852 | 2026-10-06 15:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 5d626e00-ad76-3133-a9e1-c32f8cc6dda6 | -3.0918 | -54.1465 | 2026-10-06 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| cc47c51f-3ca5-3a40-b7ad-9e64caa695b4 | -9.1334 | -65.9 | 2026-10-06 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e77b4a70-2546-35c8-af3c-667adbcc905e | -2.8164 | -54.0929 | 2026-10-06 15:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9d53165d-d9fb-312d-81de-54b0cde97534 | -3.2398 | -53.8611 | 2026-10-06 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 08850b4a-c45e-32b7-a7a3-5fac6ad1599d | -11.0485 | -45.6511 | 2026-10-06 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 283.4 |
| 9ee9257f-0c23-3042-ae3b-4817642d9245 | 1.8584 | -55.7624 | 2026-10-06 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5c3de3fd-7068-3881-a574-cd8bc77fd3a5 | -9.0347 | -67.39 | 2026-10-06 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 21b15913-f5d5-31f9-833b-d2ea4c758dba | -8.6101 | -67.1783 | 2026-10-06 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| a5a1736e-766a-33e6-9c23-2b19c4d9501d | -9.1222 | -64.3843 | 2026-10-06 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 31f4c4dd-ef54-364b-b87f-76d58c924614 | 1.7854 | -55.5658 | 2026-10-06 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 39e3ee8e-770e-3a08-834f-f5359ce4ec0f | -6.3307 | -43.8021 | 2026-10-06 15:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |


[Clique aqui para ver as próximas entradas](README86.md)
