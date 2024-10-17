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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f563703f-b5bc-393c-8161-ca7c3a02f9e2 | -2.6176 | -49.089901 | 2024-10-17 01:17:19 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1be6ac57-61f4-3799-aae1-1751acf9b6ad | -3.0899 | -51.217899 | 2024-10-17 01:17:19 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3f51aad-44ab-355d-b2f5-4c1f1a0cd4ad | -3.0874 | -51.207401 | 2024-10-17 01:17:19 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3494fe1-815a-33a8-8082-123f079bfe70 | -3.0313 | -51.2314 | 2024-10-17 01:17:20 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2149d968-317e-3a51-a0d6-00b7a09ca529 | -3.0288 | -51.220901 | 2024-10-17 01:17:20 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7237df45-fc47-3012-bf4b-c7067d540134 | -2.4291 | -48.513 | 2024-10-17 01:17:20 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e7991da-1a22-3662-a5a5-733bf549dfbf | -3.3524 | -53.219601 | 2024-10-17 01:17:23 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8877589-32b4-3041-8fdf-c8c24a120a71 | -3.3505 | -53.211498 | 2024-10-17 01:17:23 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e1429af-88a9-33eb-a961-a41ea793276b | -3.3621 | -53.2173 | 2024-10-17 01:17:23 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac1878d-a478-375d-84b7-35e862072275 | -2.8922 | -51.6917 | 2024-10-17 01:17:24 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dbe73d4-f9a5-3bbf-8bcc-59799d51a3f8 | -2.8899 | -51.681801 | 2024-10-17 01:17:24 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| becc9785-887c-349a-af07-93369aba4d2b | -2.902 | -51.6894 | 2024-10-17 01:17:24 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c62da0f5-d86f-324c-9c94-6a54a27faa82 | -2.8997 | -51.679501 | 2024-10-17 01:17:24 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46662236-0db2-32ee-9b40-7e9246f22652 | -2.8214 | -51.3456 | 2024-10-17 01:17:24 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b025380b-d807-3ca6-ace5-d0b11634402d | -3.0669 | -53.233501 | 2024-10-17 01:17:27 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79a96f61-145a-3ab4-b7a6-e785d9bb767b | -3.1236 | -53.743599 | 2024-10-17 01:17:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69c7f26c-7be6-3bb9-b383-8d353eaf567a | -3.1218 | -53.735901 | 2024-10-17 01:17:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e41e235a-99ae-334b-9f4f-d852eef446ab | -3.12 | -53.728199 | 2024-10-17 01:17:28 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2280586f-64b8-39e3-9406-7945dc535fde | -2.7844 | -52.110699 | 2024-10-17 01:17:28 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f0aebd4-1194-3a13-8af5-91a3ae869e9b | -2.7822 | -52.101299 | 2024-10-17 01:17:28 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 080c2d1d-13dd-35f9-85bc-c3d3aadd9c71 | -2.78 | -52.091999 | 2024-10-17 01:17:28 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8f967e1-c77b-30a8-a1b5-b9e96e3a19fe | -3.059 | -53.243801 | 2024-10-17 01:17:28 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0c7c3c8-98a4-368b-83d0-0955cf4d5c69 | -3.0571 | -53.235699 | 2024-10-17 01:17:28 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6d08ce7-e4cb-357c-83b4-d7c90c830359 | -3.0552 | -53.2276 | 2024-10-17 01:17:28 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 529228ee-66f6-3a5d-9084-a8bcc355b74f | -3.1138 | -53.7458 | 2024-10-17 01:17:29 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee3bf1cd-4e6f-3ded-8df1-1df5838f4bba | -3.112 | -53.738098 | 2024-10-17 01:17:29 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c673e22-7f61-3684-92f0-fe8062dc5f74 | -2.9512 | -54.1567 | 2024-10-17 01:17:33 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ece3abd7-dd73-35a4-99b6-46d939c0aa60 | -2.9495 | -54.1492 | 2024-10-17 01:17:33 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b1deac8-ac0d-3d75-af9b-28e98f06eebc | -2.9478 | -54.1418 | 2024-10-17 01:17:33 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fc5153c-ac24-3541-83e9-b6908769c4f7 | -2.7874 | -54.028198 | 2024-10-17 01:17:35 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 231d77c8-6cb2-3080-b4a7-03f6570ec657 | -2.5676 | -54.014099 | 2024-10-17 01:17:38 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca4245b-5d98-3ea3-a6b9-868230bbb1b1 | -2.5658 | -54.0065 | 2024-10-17 01:17:38 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5a3ae46-f84b-35d5-ac8b-a23e8aefc222 | -2.0015 | -52.110199 | 2024-10-17 01:17:40 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59eeeeff-2e51-365d-9da1-85f10672fef4 | -2.0113 | -52.107899 | 2024-10-17 01:17:40 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03b903a6-c589-3735-9083-1dec2b0785c3 | -2.3446 | -54.387199 | 2024-10-17 01:17:43 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b8b52bf-2fae-353c-b171-1180270039d5 | -2.3429 | -54.379799 | 2024-10-17 01:17:43 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 577a7bcd-8535-3e9c-b6b0-57e2a968eb17 | -2.3267 | -54.398998 | 2024-10-17 01:17:44 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb207b03-b5d9-3c93-9be4-355ef99c952b | -2.3365 | -54.396801 | 2024-10-17 01:17:44 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8092ed19-1f58-3626-8a3b-ad7f233f6802 | -2.3348 | -54.3894 | 2024-10-17 01:17:44 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8aa20f7b-7c27-3e58-9b9a-e83e86497092 | -1.7047 | -52.693298 | 2024-10-17 01:17:47 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d69223d7-48e7-381e-93c8-f2f7cfc4a5f0 | -1.7165 | -52.7001 | 2024-10-17 01:17:47 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfcb65ae-9ede-3978-a106-968cc72ba383 | -1.7144 | -52.691101 | 2024-10-17 01:17:47 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23254239-afc3-3199-91f2-d5689088c22e | -1.7123 | -52.682201 | 2024-10-17 01:17:47 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06ddb2d6-3556-371b-a37c-4b71799304bd | -1.1156 | -53.709099 | 2024-10-17 01:18:01 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9c519e3-80de-39f9-8093-1fb3bf331673 | -1.1254 | -53.706902 | 2024-10-17 01:18:01 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98d1235a-7e60-39ee-816b-a7e89c971523 | 1.0067 | -52.223999 | 2024-10-17 01:18:30 | METOP-C | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e1234dde-070d-34fb-92cb-baff3512213c | 1.009 | -52.2136 | 2024-10-17 01:18:30 | METOP-C | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d98d5970-28ca-30c4-9ee3-3fc8d44d510a | -2.5962 | -48.2634 | 2024-10-17 01:25:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 61d8a552-ea05-30ad-8a85-c0f4ec30ca2a | -2.6147 | -48.2629 | 2024-10-17 01:25:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c536b820-8b82-3855-adc6-35a145d89712 | -2.8333 | -49.1562 | 2024-10-17 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| c3baef63-2595-3e0f-a86b-91429ab25b12 | -2.9673 | -48.0147 | 2024-10-17 01:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| b7c0de98-e4bd-390e-860b-6c4987e7b560 | -2.9674 | -47.9931 | 2024-10-17 01:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 189.3 |
| c7002058-772d-3a77-9708-76adfc0d27ca | -3.0581 | -53.2395 | 2024-10-17 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| ed85c9ee-4c71-31e0-bfb6-357f348b0a75 | -3.2225 | -48.9306 | 2024-10-17 01:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 74e31c3e-a2c2-30f2-99f5-2a5dd0a617c6 | -3.5086 | -51.1122 | 2024-10-17 01:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| fcc788b4-0a96-3a4b-bb36-1ee96a2ac09d | -3.5087 | -51.0914 | 2024-10-17 01:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2f5063d5-e1a0-365d-82a2-401a1177a2be | -3.7007 | -45.9223 | 2024-10-17 01:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 108.2 |
| a4941b3c-6b0a-33b3-be3a-301d20c05bf7 | -3.7009 | -45.9 | 2024-10-17 01:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| af865ad0-151b-3e0c-b7fb-aec3ec56b6aa | -5.5716 | -44.8927 | 2024-10-17 01:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 084949ec-70b5-338b-8ec8-349416eee0d5 | -5.5718 | -44.87 | 2024-10-17 01:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0dc3c071-d63d-3c28-954c-a5f676fec92d | -5.6714 | -48.6872 | 2024-10-17 01:25:38 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 94062f3b-9f19-3c6d-9e88-1de34bb9e9bd | -5.9788 | -45.3621 | 2024-10-17 01:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 5a069440-73a7-33bb-9078-a71258eb47be | -6.7274 | -43.5589 | 2024-10-17 01:25:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| e66495a6-0dba-3fc4-a4e2-2ad3a6c49374 | -7.8727 | -45.3593 | 2024-10-17 01:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 298c55c6-2ee8-3acf-a718-5d850e9b513e | -7.873 | -45.3366 | 2024-10-17 01:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 7501b8d5-73af-31ed-8091-e75ca31efc8c | -9.9513 | -36.2024 | 2024-10-17 01:26:01 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| 4e895b72-9049-3423-8ad4-5a2afed2eccd | -9.9706 | -36.199 | 2024-10-17 01:26:01 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| 3a4bff93-980e-3801-8ba2-ce75165a213e | -10.129 | -56.7722 | 2024-10-17 01:26:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 4f846d62-b06b-3c46-b891-c9d01a0a86e9 | -10.1477 | -56.7709 | 2024-10-17 01:26:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b654459b-3a84-34f0-ac6a-754235369102 | -11.7309 | -64.9579 | 2024-10-17 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 8ae78181-04d5-3c5b-8978-9a15eeac3277 | -11.7308 | -64.9769 | 2024-10-17 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5e5f099c-e92d-3c06-bb65-567c54a10f17 | -11.8812 | -64.9513 | 2024-10-17 01:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e15681d6-37f5-30b2-8fa3-231b9ea67166 | -11.8814 | -64.9323 | 2024-10-17 01:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 542b2dd0-ce06-3b70-b31e-794809934d10 | -11.8815 | -64.9134 | 2024-10-17 01:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0d8b5159-93c9-368f-b392-76ede1fe0afd | -11.9002 | -64.9315 | 2024-10-17 01:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 90e48157-3ab7-353a-8bbb-a15464324f33 | -17.1667 | -56.8232 | 2024-10-17 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 3b9516dd-3827-319a-a9bf-aef3e7d77ea9 | -17.1671 | -56.8026 | 2024-10-17 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| fa384e89-8c37-39e6-bd41-7c52c5c0851e | -17.2177 | -57.3102 | 2024-10-17 01:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 4de2eff4-bc20-33be-907e-d6ed90dd174b | -17.8049 | -57.4655 | 2024-10-17 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.6 |
| a6a9f98a-0fd2-32aa-a5cb-60fecf9a3cdb | -17.8052 | -57.4449 | 2024-10-17 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| f88177c2-722f-386d-a2ad-ac102e0afc58 | -17.8246 | -57.4631 | 2024-10-17 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 682cbbc6-4139-37bc-a58e-cc02fc8ee63a | -17.8249 | -57.4425 | 2024-10-17 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 76a3e884-dc63-3b9a-80da-728dcf710a35 | -17.8641 | -57.4583 | 2024-10-17 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 50b1fcd2-2174-3c6c-8656-924c70452692 | -2.5962 | -48.2634 | 2024-10-17 01:35:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| b647c661-a044-355b-9235-de367acacc9e | -2.6147 | -48.2629 | 2024-10-17 01:35:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 7a3a6cc6-a64c-3170-b7c2-9e52fd4a623d | -2.8333 | -49.1562 | 2024-10-17 01:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| e90e215b-7805-3fa8-ae39-806655195e62 | -2.9673 | -48.0147 | 2024-10-17 01:35:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 357e6057-635f-3a56-9c96-a347ef44f70b | -2.9674 | -47.9931 | 2024-10-17 01:35:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 2ad9098b-b687-3fde-8c98-8dff268e9e04 | -3.2225 | -48.9306 | 2024-10-17 01:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c15d71fe-4a77-3837-97f4-74b4e3aff262 | -3.2226 | -48.9092 | 2024-10-17 01:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 33c661e2-06f8-3749-b905-cd00c77ab92b | -3.2502 | -46.8929 | 2024-10-17 01:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 196e09c4-a3b7-3cee-836e-4a4a0f630eb1 | -3.2503 | -46.8709 | 2024-10-17 01:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 67f1281d-525c-322f-a811-8ae69949a4ee | -3.3584 | -43.8289 | 2024-10-17 01:35:25 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 5c7f1cee-f28a-39e4-a0a2-294ec262d49a | -3.5086 | -51.1122 | 2024-10-17 01:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 9444d177-3e7c-39c4-8040-f37f0c8784ad | -3.5087 | -51.0914 | 2024-10-17 01:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 3044a0b5-3dfb-38a7-a9ce-82910b6953c5 | -3.7007 | -45.9223 | 2024-10-17 01:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 8f650d78-5033-3713-bcb7-f047f59e2598 | -3.7009 | -45.9 | 2024-10-17 01:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 1f989e4c-6533-3732-a9e2-950e89d9432f | -5.5716 | -44.8927 | 2024-10-17 01:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 73201bfc-99d5-35bd-bf50-2e102e4fa351 | -5.9597 | -43.3673 | 2024-10-17 01:35:39 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 6a8a0e54-9ee8-3170-bf3d-e345671a1b03 | -6.7274 | -43.5589 | 2024-10-17 01:35:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |


[Clique aqui para ver as próximas entradas](README12.md)
