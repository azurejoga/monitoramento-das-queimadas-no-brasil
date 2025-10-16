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
| ba1ab059-0194-3a0b-b6e1-5e94120f7b8b | -4.3498 | -43.4082 | 2025-10-16 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 1657310b-fb52-3459-b58d-e848e74d0d98 | -5.7863 | -46.005 | 2025-10-16 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| dcb36639-2619-370f-bf6e-5709a7ab2441 | 1.8218 | -55.7431 | 2025-10-16 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 75221077-3510-38ef-ba37-bdf75bdf6541 | -7.9442 | -44.115 | 2025-10-16 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 0ebcb085-9fbc-3f11-93e7-054c99927f68 | -12.6801 | -43.4474 | 2025-10-16 01:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 5facee0a-1dc9-35be-8fe5-6b345929a179 | -5.8799 | -43.8844 | 2025-10-16 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 288.2 |
| 0b140d7d-28d9-3025-8943-8ac2099368ad | -4.3871 | -43.4292 | 2025-10-16 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 5c16eca9-ecae-37d8-81b6-eec390d38a9f | -8.4717 | -44.1746 | 2025-10-16 01:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 0d2da139-0158-363a-8167-9de783f20f1e | -4.3687 | -43.3838 | 2025-10-16 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 300.9 |
| 50482660-7938-38ca-91e4-c2e873175bc1 | -4.4059 | -43.4049 | 2025-10-16 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| cdb01889-c5de-30f5-a5ae-889611b59225 | -4.116 | -48.0352 | 2025-10-16 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| db608fba-fe0a-3858-a2d3-efdae917144f | -12.6805 | -43.4235 | 2025-10-16 01:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 2995f0b7-c3c0-3a42-8018-9fb481d6884c | -4.35 | -43.3849 | 2025-10-16 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 4ea78b0b-9278-3bcf-ab2a-8abec3e2611a | 1.8217 | -55.7629 | 2025-10-16 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| b6d9c0ee-415b-383b-a4e4-d8e93ceec450 | -4.4856 | -45.3903 | 2025-10-16 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 303ee7de-fd2f-3457-a759-e64ab48ee7bb | -5.2068 | -43.7945 | 2025-10-16 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 99f1362d-8324-3403-8abe-1a482b556edd | -4.3874 | -43.3827 | 2025-10-16 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 323.7 |
| bc475944-5cb4-3d1b-8932-42951186356c | -5.5148 | -47.2849 | 2025-10-16 01:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 7bbbf56e-118d-3f2b-b153-7655e6e820b0 | -7.4894 | -42.7586 | 2025-10-16 01:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 79896b88-7646-344b-b207-eb424c00a0fe | 1.8401 | -55.7232 | 2025-10-16 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 57d2f81f-a39b-3e03-9cd2-0326baed586e | -4.0976 | -48.0144 | 2025-10-16 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| a07c1fba-44b2-30b0-88e4-a1d5c595799f | 1.8032 | -55.8815 | 2025-10-16 01:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 61911b3f-9065-36ef-ba91-b075e810c29e | -7.5509 | -43.923 | 2025-10-16 01:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| a0bc4f47-afff-37c0-b813-c43bd4cde8d9 | -4.0974 | -48.0361 | 2025-10-16 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| a5edc3b9-8cea-3cd9-ba3f-92ff95cb313e | -6.3733 | -41.4828 | 2025-10-16 01:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 8b76a6c3-57dc-3ace-96e7-3175fe838fc2 | -7.9628 | -44.1362 | 2025-10-16 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 0d05fc2a-3a60-3328-aba8-b021eb97c162 | -5.496 | -47.308 | 2025-10-16 01:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 536d18ab-e934-3f5c-bab9-b1eeaba68c93 | -4.5229 | -45.3882 | 2025-10-16 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1e9cb593-ad27-3177-b150-d27efab835df | -8.4528 | -44.1767 | 2025-10-16 01:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5c288a41-6e52-3829-9165-6e3dbe3072d6 | -8.4714 | -44.1978 | 2025-10-16 01:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 20998f63-ef5e-3c0a-806a-c638044b4fb5 | -5.5147 | -47.3069 | 2025-10-16 01:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 166.9 |
| d419fbf1-254b-31e7-b7c8-b3190db60917 | -4.4061 | -43.3816 | 2025-10-16 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 4e07e2f5-e05b-30f7-85f3-67f138e275e6 | 1.84 | -55.7626 | 2025-10-16 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b5690866-f5fe-352c-90e3-3f9c2e4c7264 | -4.3685 | -43.4071 | 2025-10-16 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 95cfb7b8-f0a8-3b22-bbb1-f027496faaee | -4.5041 | -45.4118 | 2025-10-16 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 4d3999b5-e3be-3ed0-a926-66381adf5b96 | -5.4575 | -42.9381 | 2025-10-16 01:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 8306f6ed-7469-3a74-b5a2-f81b87f3050d | -5.8989 | -43.8598 | 2025-10-16 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 750fbf39-5e1c-3427-a351-fbd8747d8692 | -4.1161 | -48.0136 | 2025-10-16 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 185.7 |
| 031725ad-47a6-3ba7-b3a1-dc678d0edd3b | -5.2255 | -43.7932 | 2025-10-16 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| e0073ce4-aab1-3a3e-8722-6fc756f1e84c | 1.8401 | -55.7429 | 2025-10-16 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 432a4fd1-e319-334a-b2d2-795cb9087170 | -4.9293 | -45.8811 | 2025-10-16 01:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| bd619dc5-c265-3f83-bb89-ce4b1423bd75 | 1.8217 | -55.7826 | 2025-10-16 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 4f0aa3ac-0514-3c0c-9565-919357fc59c7 | -9.2398 | -63.2489 | 2025-10-16 01:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| cd24f7c0-df3f-3cf6-b020-0ad10f0081bf | -7.9631 | -44.113 | 2025-10-16 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 49e08462-d4fb-3fc3-bf72-f9b48c890bd4 | -4.1161 | -48.0136 | 2025-10-16 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 187.5 |
| 93d4978f-a46c-3a21-8345-b02987ce7977 | 1.8401 | -55.7232 | 2025-10-16 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3811d369-3342-31e5-8ffd-9c04a6e46c6b | -4.3498 | -43.4082 | 2025-10-16 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| e209d469-ce3a-3c74-8454-532134194647 | -12.6805 | -43.4235 | 2025-10-16 01:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 88d36b7b-ccce-3810-8a32-48743e1f8e49 | -4.3874 | -43.3827 | 2025-10-16 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 817e4780-d88c-3c27-b534-3337412374ed | -4.6624 | -44.1062 | 2025-10-16 01:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| c1e2ee1c-a36b-38e7-b4c3-f8ed0f9fabf1 | -7.4706 | -42.7605 | 2025-10-16 01:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| e9b74ec8-3749-350e-a076-496c829f0256 | -7.9628 | -44.1362 | 2025-10-16 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 3a483b98-2107-3c3c-a205-33f2078eefff | -5.4762 | -42.9367 | 2025-10-16 01:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 109.7 |
| 60d1913f-a7ff-3c93-b9b1-67145a5112d5 | -4.3872 | -43.406 | 2025-10-16 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 9cf9ee14-ad46-30c1-b37f-7ac33fc225af | 1.84 | -55.7626 | 2025-10-16 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| b1d530b8-eb27-34a0-b6e1-a9e0a6f37884 | -12.6801 | -43.4474 | 2025-10-16 01:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| a08841e5-1f12-3250-a113-156f2a8f0527 | -4.5041 | -45.4118 | 2025-10-16 01:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 8bff20ec-aac3-3b9d-b9ad-264a9024e7c8 | -4.883 | -44.5737 | 2025-10-16 01:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| bc68e717-9aa5-332e-bb44-385751ac80b2 | -4.5229 | -45.3882 | 2025-10-16 01:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |
| bebb63bb-42ad-330d-ae9c-1ce47809d8e1 | -7.9442 | -44.115 | 2025-10-16 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 22993ed5-c90e-3ada-ad90-c7d0466f63b3 | -4.9293 | -45.8811 | 2025-10-16 01:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| cd3f93e4-4798-310d-89bd-96435077b042 | -29.187 | -50.1287 | 2025-10-16 01:30:00 | GOES-19 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 56.6 |
| 35a4ca2d-23e2-3250-9be8-9ba10785dcc8 | -11.4735 | -47.6427 | 2025-10-16 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| abee798d-1660-3095-96a0-68a5c8f40d1a | -4.116 | -48.0352 | 2025-10-16 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 81cd641f-6628-37a9-981d-6bc0abf51a75 | -4.4059 | -43.4049 | 2025-10-16 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 544d34e1-084b-39f2-8cee-5925835c0771 | 1.8401 | -55.7429 | 2025-10-16 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 3360af06-4c90-35ff-a630-0be1e06a0b00 | -8.4714 | -44.1978 | 2025-10-16 01:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| cb21829e-a22e-3076-a684-d1cf70e49044 | -4.8644 | -44.5748 | 2025-10-16 01:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 18f067b8-ae84-3837-8018-a2db8fce0842 | -4.5042 | -45.3893 | 2025-10-16 01:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| bfbc54b1-5b6c-3389-8540-cdfdcc3e471d | -4.0974 | -48.0361 | 2025-10-16 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| c04bbea0-7898-32ea-bc9d-1e4a95c0d9cc | 1.8217 | -55.7629 | 2025-10-16 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 57665e80-1b77-3880-bdc1-bf95e90ce6c9 | -8.4717 | -44.1746 | 2025-10-16 01:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 134.8 |
| ee94aba8-129d-3f78-a4fb-476f9a6a950c | -4.3685 | -43.4071 | 2025-10-16 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 178.6 |
| f2a24a43-cbb6-3c46-b25a-c42ffacebf3b | 1.8218 | -55.7431 | 2025-10-16 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 51d7505a-e280-3046-9846-00d624454919 | -7.9439 | -44.1381 | 2025-10-16 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 25e8f4c0-4f4f-309b-af0e-fc5bf72fe183 | -4.5227 | -45.4108 | 2025-10-16 01:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 008f7e98-bf45-3791-a199-a96f91541af5 | -7.4894 | -42.7586 | 2025-10-16 01:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 2b38ae1f-0c02-3040-a2db-c424451e7ab3 | -4.35 | -43.3849 | 2025-10-16 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| e7d7a0d4-7d60-345a-bdf3-c7ad25198e77 | -5.5147 | -47.3069 | 2025-10-16 01:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 158.0 |
| af8a6f30-59f2-33bf-97b4-e9c9c34e3bc4 | -5.5148 | -47.2849 | 2025-10-16 01:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| da49beb7-821f-31cf-a823-aba76889a4dd | 1.8032 | -55.8815 | 2025-10-16 01:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| c63ca1ad-a0c8-31a3-b44a-1755cfadfc89 | -12.6612 | -43.4268 | 2025-10-16 01:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| db34a1d4-1c39-3921-aa5b-a252dc7a2fd6 | -8.4528 | -44.1767 | 2025-10-16 01:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| da71f2c9-7f8d-34cf-bfd8-45460569dae1 | -5.496 | -47.308 | 2025-10-16 01:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| e623a5be-625c-35bd-957d-7c8a0220cf96 | -4.0976 | -48.0144 | 2025-10-16 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| ae208823-bbef-3f22-866a-63e4b1f38e86 | -4.3687 | -43.3838 | 2025-10-16 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 227.2 |
| b04dc599-5879-3f3a-99ec-fd77d818332e | -12.6801 | -43.4474 | 2025-10-16 01:40:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 855c50c0-2c69-346c-af8e-805c0653785d | -7.9442 | -44.115 | 2025-10-16 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 8676881e-323d-32af-b665-4ab6a1f30d20 | -5.4762 | -42.9367 | 2025-10-16 01:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 9ffe55c8-ea8a-3742-8086-1cd60dccce0d | 1.8401 | -55.7429 | 2025-10-16 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 5aaf476f-0b57-3257-b6af-ce4b63c4b4cd | 1.84 | -55.7626 | 2025-10-16 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 2c600158-17d4-33d2-a738-d51bf2286420 | -4.3874 | -43.3827 | 2025-10-16 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 386.0 |
| 81337358-966c-3d50-91cc-45e3a6e7f671 | -4.5229 | -45.3882 | 2025-10-16 01:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 41.1 |
| d09f3bbd-6a01-353d-9408-cd8fc6cd6476 | -4.0974 | -48.0361 | 2025-10-16 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| f2df8460-38e1-3db0-b6a6-68062f8d13f4 | -4.6626 | -44.0832 | 2025-10-16 01:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 47d0938c-1393-30d7-84e0-8c1284578f15 | -4.883 | -44.5737 | 2025-10-16 01:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| fcf16838-75a4-3394-9408-ed05b28de2ae | -7.9628 | -44.1362 | 2025-10-16 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 6aa164ee-3d48-36a0-81fb-fc8670442e58 | -4.5227 | -45.4108 | 2025-10-16 01:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 35.4 |
| bedc408e-18a6-32dd-8c09-2c53a11851fe | -4.5042 | -45.3893 | 2025-10-16 01:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 7dbe1328-dd03-3d28-bb97-12427dcc3e17 | -4.3687 | -43.3838 | 2025-10-16 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 388.4 |


[Clique aqui para ver as próximas entradas](README7.md)
