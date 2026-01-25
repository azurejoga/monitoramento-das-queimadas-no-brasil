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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d84a784-d891-3f6c-81db-f4ec0017fd95 | -23.46675 | -48.90041 | 2026-01-25 04:01:00 | NOAA-20 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dd2787da-57c6-39f1-95bb-0f7a6e8a05f2 | -27.13127 | -51.13383 | 2026-01-25 04:01:00 | NOAA-20 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| eff5059e-056d-3098-9b04-c2f859602d01 | -23.47097 | -48.9014 | 2026-01-25 04:01:00 | NOAA-20 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 243e08b7-0684-3d25-a22c-56d2a58f903c | -26.02824 | -52.69543 | 2026-01-25 04:01:00 | NOAA-20 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61cec30d-09d7-33f5-84d5-8e4a4a118f4f | -25.22151 | -49.66485 | 2026-01-25 04:01:00 | NOAA-20 | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1ddaafe9-1858-3d80-a47b-83b48ec79232 | -27.1316 | -51.13569 | 2026-01-25 04:01:00 | NOAA-20 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fde2a307-2e05-3566-aa4d-04436c6b52bc | -27.05941 | -48.69881 | 2026-01-25 04:01:00 | NOAA-20 | CAMBORIÚ | SANTA CATARINA | Brasil | 4203204 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b508b40b-052d-3047-b26f-44fca0195dbf | -26.02751 | -52.69858 | 2026-01-25 04:01:00 | NOAA-20 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 54e72779-b284-3d36-a41c-3d7ad71021da | -26.36898 | -48.95758 | 2026-01-25 04:01:00 | NOAA-20 | JOINVILLE | SANTA CATARINA | Brasil | 4209102 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 490add7b-4d60-383b-a2cc-870abdc3596a | -3.0791 | -40.1063 | 2026-01-25 04:10:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 94f8587f-98ca-31e9-910d-7bb6093bdd7e | -3.0603 | -40.1072 | 2026-01-25 04:10:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 1889e12c-8d0f-321d-aa4b-96a9b3cc0776 | -3.0603 | -40.1072 | 2026-01-25 04:20:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 77.3 |
| ee44bfd3-edde-3338-9167-6d0228555216 | -18.7912 | -57.6519 | 2026-01-25 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| a81d0076-a3f0-32b2-95fd-b209df4b9ab2 | -3.0791 | -40.1063 | 2026-01-25 04:20:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 77.1 |
| b0951dea-9810-348a-8838-075351dd3a51 | -18.7912 | -57.6519 | 2026-01-25 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 8a7428b0-7936-31c4-87ce-b3d4f52af2b5 | -19.6565 | -57.2472 | 2026-01-25 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.0 |
| b214e5f9-378a-31a4-aa8e-9dada6c21724 | -19.6364 | -57.2499 | 2026-01-25 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.0 |
| 80465957-ad45-3ed5-8898-7508b76a24e9 | -3.0603 | -40.1072 | 2026-01-25 04:30:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 7ec94496-c59c-394c-b1f6-889a92312bde | -3.0603 | -40.1072 | 2026-01-25 04:40:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 43c6b520-4514-3fd5-b7ed-8858a189bc6a | -6.20147 | -39.28051 | 2026-01-25 04:46:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dd1ea367-f471-33ee-af6e-5b6f195d732d | -3.07385 | -40.11072 | 2026-01-25 04:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 622a9851-6d9c-3ff4-908f-7bd0e001f66f | -5.3561 | -40.60049 | 2026-01-25 04:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9c882205-11e5-3ed7-8cf4-392ce64950cf | -6.20082 | -39.28543 | 2026-01-25 04:46:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7e046924-8b18-3baa-815c-e3a201e83578 | -3.06749 | -40.11379 | 2026-01-25 04:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| aa732ad0-85d7-321f-a83c-f368d6908fac | -3.06171 | -40.113 | 2026-01-25 04:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| b6b441d6-965a-33bf-ae4d-ee1c82acd619 | -3.06867 | -40.10584 | 2026-01-25 04:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 18.5 |
| de428040-8a1e-3417-876b-b488e19206df | -3.06231 | -40.10897 | 2026-01-25 04:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| cf6a058b-9806-3ae2-a00c-e5022e8dca67 | -9.3792 | -40.7141 | 2026-01-25 04:46:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e3dab7e6-e68b-3296-8d0b-f6461f33a102 | -6.19842 | -39.28306 | 2026-01-25 04:46:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| aecd529f-16e4-3a93-87b7-4d3cdb33ecbb | -3.06808 | -40.10986 | 2026-01-25 04:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| d7652afc-d423-392f-8c84-0d940d0fb1ed | -6.20478 | -39.28387 | 2026-01-25 04:46:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e73e4c27-d28b-3792-8611-27d3ab1a8c6a | -3.07445 | -40.1067 | 2026-01-25 04:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c24a918e-a0ec-30e5-aa6e-8e17eaa411b5 | -11.15071 | -43.32087 | 2026-01-25 04:48:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a33e9245-d562-3ae7-9a74-62918bf7df78 | -3.0603 | -40.1072 | 2026-01-25 04:50:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 054583a7-96d8-3785-9dea-b5fd3b67b246 | -19.616 | -57.2735 | 2026-01-25 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| e04974d4-62e0-33c0-8448-ba5d569bb540 | -19.6561 | -57.2681 | 2026-01-25 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.2 |
| 3f3b9398-e403-3d25-b93b-264490092d78 | -19.6364 | -57.2499 | 2026-01-25 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 60f45c04-5fd8-340d-b2cb-6b18a7e5c9c2 | -19.636 | -57.2708 | 2026-01-25 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.1 |
| 2cfc958c-2bf8-3621-a517-f356ef631ac6 | -19.6357 | -57.2917 | 2026-01-25 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.6 |
| 701a0bf0-dbb2-340c-8389-8a9ea8ada170 | -19.60625 | -57.28735 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 81a2e751-892d-3513-9173-9f20a85847ac | -17.69851 | -53.2673 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 437c30ea-8fff-30b1-8e27-dab4dbfe3c5a | -19.61687 | -57.28938 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6644e74e-f885-3fa3-b792-215a34ba9bb7 | -19.60214 | -57.26904 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4417801e-2172-3200-a3e6-624cf19de507 | -21.07123 | -49.52858 | 2026-01-25 04:50:00 | NOAA-21 | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 26916fcb-0b41-3c94-8a7c-df06fad4e3b5 | -19.67556 | -57.18291 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1ddb89aa-ff6d-39f7-99dd-007a511499e0 | -19.04953 | -52.52382 | 2026-01-25 04:50:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 751bdc81-360d-3bf7-b31f-e1e79d3c6a75 | -19.66706 | -57.18995 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 26c4d020-c2fb-308a-8532-cec2975972da | -19.62972 | -57.27871 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 27108aa0-dd61-31d8-ab36-b2901d4f4d54 | -19.60642 | -57.26548 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 55f93096-a870-3602-82e6-29890251bf8a | -19.9962 | -54.369 | 2026-01-25 04:50:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1354bed6-f8b1-33b0-b90d-162d73b89cb6 | -19.63902 | -57.26736 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 925c263e-d6c3-397d-90f2-49de6fd7f89d | -19.62354 | -57.25128 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 887a0bed-6921-3162-ab41-a334ca04786a | -19.63754 | -57.27583 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 71341344-e882-3c17-ba7c-467c02341c42 | -19.61053 | -57.28379 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| eb671170-150b-3dcc-b0ed-28ec96a3beca | -19.6517 | -57.27855 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c7ee895c-eaa1-3f95-a136-1c3d8477d4b8 | -19.64034 | -57.28075 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5c02b665-4857-31ca-b68c-44855406c84a | -17.70951 | -53.28399 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dab2bad-4e0e-3dc2-9d10-6b3a376f6418 | -17.69795 | -53.27092 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 732efd80-5658-3f93-a812-9562fa943b89 | -19.63769 | -57.25399 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e1feb009-29ae-37dc-9da0-943fe578ca01 | -19.63813 | -57.29346 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 04173cc8-363f-391c-8b71-f7c2f8c690ba | -17.70401 | -53.27565 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f29eed69-efad-3d37-bce4-1680ad8973ec | -19.61613 | -57.29362 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 323b9b5d-2b11-32e6-a956-93fc3cfc1015 | -19.6455 | -57.25113 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 4c78e09b-eb38-3801-9108-737e8f0d6571 | -19.65037 | -57.26517 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d189f494-15bc-3c68-9787-d360179ae660 | -16.4422 | -58.16647 | 2026-01-25 04:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e81c1a41-07e0-38b6-9c3c-56962751d3b4 | -18.79157 | -57.65395 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a6c1146a-2331-3b4f-92e7-9e67c7cd4f76 | -17.70345 | -53.27926 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d22b769d-41d6-3d2d-be31-d6d9d3a7b6fb | -19.29871 | -53.1791 | 2026-01-25 04:50:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94fcc983-daec-3f5b-98de-e2a9e4ded434 | -19.62692 | -57.27379 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 0f164d00-6601-31a5-b978-5fb03b914cb5 | -19.6275 | -57.29142 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c9ab3ac1-53ed-3ff9-a2b2-364d8c9c0aaa | -19.6461 | -57.26872 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 105c4211-5a2f-3d27-89ad-fa97740aae18 | -19.60922 | -57.27039 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 87fe2e9e-1a07-3fb8-9766-0483c3855891 | -19.6489 | -57.27364 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 943ca934-3625-317a-85ab-a0e600116dc0 | -19.61984 | -57.27243 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.5 |
| e2fe6614-930f-37fc-a6f1-5b6ce6586d32 | -19.62041 | -57.29007 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 57f59101-253a-3770-bd1b-21ffa07bdb6c | -19.63179 | -57.28786 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 799bb747-2540-3831-9fbf-83a2678a830d | -19.61762 | -57.28514 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 90fcf4f5-b669-3b65-a89f-92a0bd0d8051 | -18.81469 | -51.60858 | 2026-01-25 04:50:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a97919b0-a5b7-3bd1-b867-cdf55de723b2 | -19.66779 | -57.18576 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3b4c4e2b-42d4-3ec1-b321-1a547753237c | -16.0187 | -59.908 | 2026-01-25 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5837457-b41d-3b5c-854b-5e6078d9dc5e | -19.61482 | -57.28023 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4a188f74-4f03-371c-af1a-51183758cace | -18.79521 | -57.65466 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d16461ed-3ace-331f-bfe2-1d7919ac877a | -17.70788 | -53.27258 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8cc0e8e-8811-3a69-900d-fa1615648a00 | -17.70569 | -53.26479 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb9eb620-15de-3fb8-949d-bf62f3cfdcae | -20.57476 | -55.56173 | 2026-01-25 04:50:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 800e4256-15a4-39f2-8e0f-ec0e55b797ad | -19.65928 | -57.1928 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 343623f4-615b-3f12-9a1b-cb2a2d8829f3 | -19.65356 | -57.20474 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7cd1909e-841b-3534-9506-a09fa71adcf8 | -20.91741 | -56.38005 | 2026-01-25 04:50:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1db4e29e-61fe-3a85-bf2a-fcbc12ab8872 | -20.32706 | -57.83014 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 444dcd88-ef3f-34ec-bc6c-42f32bb5c1d4 | -16.44607 | -58.16724 | 2026-01-25 04:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 510d29f6-0c8d-389d-aeb7-13a600be35eb | -19.61836 | -57.2809 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| be9bff64-7b98-3cfc-8cc4-beb9fb2cebcf | -19.61927 | -57.25483 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 58b1de44-1d6a-3750-bdf7-171c875d896a | -19.63252 | -57.28362 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| fb7dcf04-2ff0-3a42-8b37-43c79146c6b7 | -19.61127 | -57.27955 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0f74289c-3f62-3126-b239-6ab8e5c72399 | -17.70676 | -53.27982 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d00f17a-db9c-34ad-a0b8-67b70e013861 | -17.58921 | -53.07102 | 2026-01-25 04:50:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b198703-36c5-3548-a0c6-dd32a57f9ab7 | -19.60419 | -57.27819 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1ccd4d19-9d56-37be-b83d-e5b212af7af8 | -17.70513 | -53.26841 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb795aae-05e5-3ebd-a049-6caf0631676c | -20.72744 | -55.16527 | 2026-01-25 04:50:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51767ddb-b3a9-3035-abae-0f864ead3ad4 | -19.61967 | -57.2943 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |


[Clique aqui para ver as próximas entradas](README5.md)
