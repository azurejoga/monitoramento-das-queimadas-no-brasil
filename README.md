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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5443d1a0-5913-30ce-849e-ce5ad2442618 | -6.1606 | -48.0507 | 2025-11-14 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9ac5b69d-af72-35ad-8808-0413a771bb59 | 3.0912 | -60.7464 | 2025-11-14 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 296173c6-e82b-32d2-832f-3a9b9fb98f90 | 3.0911 | -60.7843 | 2025-11-14 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 88.2 |
| b7ccb3f8-667f-32f8-928d-47ff8f826e50 | -9.3107 | -47.8265 | 2025-11-14 00:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| a2f1e51f-3af8-35ea-aebc-bd3b8a083e1a | -11.8486 | -49.2218 | 2025-11-14 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| e66c4d9f-1ba3-39e7-ad0a-2ebacb5e4084 | -11.8681 | -49.1976 | 2025-11-14 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| ab556e91-d8c7-37ef-9afd-06ca2f5e8acb | -11.8677 | -49.2195 | 2025-11-14 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| aac42102-dbd7-322b-9191-358e44916b0a | -4.1161 | -48.0136 | 2025-11-14 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 909dec62-96a8-3ecf-a2f7-fc81f34721f0 | 3.1094 | -60.765 | 2025-11-14 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 270.5 |
| be2055a1-aa10-3ae8-9673-1d0cd8701601 | 3.0911 | -60.7653 | 2025-11-14 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 215.7 |
| f0876c54-1848-388d-92c3-58e762dd2bb8 | -4.7018 | -46.4508 | 2025-11-14 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 271.5 |
| 474ba3d2-0a3a-3f43-8a8d-8c05eb8d0eae | -4.7204 | -46.4497 | 2025-11-14 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 1378c499-3986-3b46-9cb5-c10e63c483a2 | -4.7206 | -46.4276 | 2025-11-14 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| bd34059a-599e-33c7-bb93-8eee0926e016 | 3.1093 | -60.784 | 2025-11-14 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 0c6fbd4e-379b-370f-9479-90f2b1f1dd7a | -4.0976 | -48.0144 | 2025-11-14 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| ee078293-9d61-3760-a4f7-492bd58e40de | -2.8481 | -45.4862 | 2025-11-14 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6b6b5fda-144d-366f-bdb1-607ed6d2b89f | -7.8479 | -44.2865 | 2025-11-14 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 0dab4691-aee8-3d22-a86d-9791c100829c | -2.8295 | -45.4868 | 2025-11-14 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 8bd28f2b-486a-3385-9295-eec19848dd25 | -2.1243 | -45.351 | 2025-11-14 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 8cdd39aa-8620-3ec6-940a-7e8679e3b4c8 | -3.6636 | -45.924 | 2025-11-14 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 0747c0fb-7b4d-33cc-9740-80452b2f2ac4 | 3.1094 | -60.746 | 2025-11-14 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| e9dcd013-caf6-31ca-b3a7-1a1abe18eaac | -2.1242 | -45.3735 | 2025-11-14 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 55012755-dc94-3454-ac6a-5d37cb8bcce9 | -11.849 | -49.2 | 2025-11-14 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| d07b9887-b355-32a1-8033-8dda76265d62 | -2.5238 | -47.8115 | 2025-11-14 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 6bd685f5-be5d-3334-9a5a-be975eb49909 | -3.6634 | -45.9463 | 2025-11-14 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 03d863e4-b490-3f15-aa6f-90cce9b4520d | -4.702 | -46.4286 | 2025-11-14 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 4e53562d-f785-373d-9785-588445d75abd | -11.8681 | -49.1976 | 2025-11-14 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b01fc368-f0d0-3cd9-8886-d9841b50f005 | 3.0911 | -60.7653 | 2025-11-14 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 281.3 |
| 7145554b-5a9a-35ca-9b2c-4b08b59106c3 | -7.8479 | -44.2865 | 2025-11-14 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 04e7bd2c-65c9-352f-acb2-6e775b3004e2 | -4.7206 | -46.4276 | 2025-11-14 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b7070c19-193b-362b-a79b-3a6f9a2db037 | 3.1094 | -60.765 | 2025-11-14 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 231.9 |
| 61e4cb43-27f2-37ba-bb9e-a4739c759984 | -12.7189 | -45.4074 | 2025-11-14 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f98d0da6-bf82-303b-87a5-afaa6fd44180 | -4.702 | -46.4286 | 2025-11-14 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 5ed634d7-e648-3fa8-89cf-f27a1803d8fb | -11.8483 | -49.2436 | 2025-11-14 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 44f60293-64a7-3799-a9ee-8224e6741704 | -6.1606 | -48.0507 | 2025-11-14 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 6899f19b-7455-33db-aa3b-cf30f3adc2b2 | -12.6996 | -45.4104 | 2025-11-14 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| b81e7038-06e0-3e28-b49b-d65d0d4c2c45 | -9.3107 | -47.8265 | 2025-11-14 00:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 9a4eb1cc-8016-343b-90f8-091b296975ab | -3.6636 | -45.924 | 2025-11-14 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8efec3ce-7ce4-34c7-bae7-76b1ca9ebf20 | -11.8677 | -49.2195 | 2025-11-14 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 97b2deb5-fe3d-3be4-8e27-5cc5f36c1bd8 | -11.8486 | -49.2218 | 2025-11-14 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 372.4 |
| 0d23bf88-4d69-3a79-92a3-4d7d4e8dec54 | -12.6992 | -45.4335 | 2025-11-14 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 5fa79c47-9fc8-30dc-bc53-c06602453aee | 3.1093 | -60.784 | 2025-11-14 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 26fb9f66-a773-33c8-b900-1a62af864f5c | -11.849 | -49.2 | 2025-11-14 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 152.9 |
| ae1a9e20-1134-3f7c-85a9-1312dc09605b | -12.6803 | -45.4134 | 2025-11-14 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 35d3ab13-856e-356b-b414-c2ab09166fb7 | -12.7185 | -45.4305 | 2025-11-14 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 215205c8-4b8c-301b-8129-ae3ab289c5cd | -2.5238 | -47.8115 | 2025-11-14 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 1163479e-f043-3d7a-969f-86ffc16a3ed7 | -11.8674 | -49.2413 | 2025-11-14 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 76198bad-898e-3033-9b6c-32a6aadefdc8 | -4.7018 | -46.4508 | 2025-11-14 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 244.0 |
| f3292d32-a531-35cd-9ee6-7512d7113018 | -4.7204 | -46.4497 | 2025-11-14 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 29dc5c07-b775-375d-9b78-2ec1bc43ecdc | 3.0912 | -60.7464 | 2025-11-14 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 54e2b1ca-10f3-36b0-9036-58961a75cb71 | -2.8481 | -45.4862 | 2025-11-14 00:10:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| da4b37c5-aa01-3f15-816e-438f55ac5660 | 3.0911 | -60.7843 | 2025-11-14 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 5ed04c7c-8c70-3fdf-876e-87a8d8c14919 | -7.8476 | -44.3096 | 2025-11-14 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c06d3df4-e944-37c9-a9c9-aad69362d613 | -12.6799 | -45.4365 | 2025-11-14 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9a0c15b6-97b3-32d5-8ba9-fbb9ee1516ce | -7.8668 | -44.2846 | 2025-11-14 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 5387abf5-6d90-3035-8c76-739b28afa9b4 | -3.6634 | -45.9463 | 2025-11-14 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 6b9b7379-aa56-3e81-8c46-b8a582ed9d9d | -4.7018 | -46.4508 | 2025-11-14 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 213.5 |
| 673d11ef-beb0-3416-9ed4-a69e076c9c08 | -14.9534 | -49.7755 | 2025-11-14 00:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| d07e9ccc-9391-3ea8-abe5-e76d8ecdbf78 | -6.1606 | -48.0507 | 2025-11-14 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| d96a5099-8d6e-3e4d-9c3d-89c3689d9ce7 | -7.8476 | -44.3096 | 2025-11-14 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| e0f07103-20fc-3320-a512-2ae3a08073bb | -7.8479 | -44.2865 | 2025-11-14 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| ab30c9a4-4e65-3988-a83d-9d4b0978c689 | -4.221 | -49.1267 | 2025-11-14 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| b69cc425-564e-35e6-9cb1-cbbd0078731d | -4.7206 | -46.4276 | 2025-11-14 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| eee2ff43-e0a8-3f50-a18f-45af9fbc6244 | -12.7189 | -45.4074 | 2025-11-14 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 97ae8a1b-e8c8-388e-adf3-7cdd6a413204 | -7.8668 | -44.2846 | 2025-11-14 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| be205dde-2e28-3fb5-afe0-9e0235f077ec | -2.5238 | -47.8115 | 2025-11-14 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ef924bd4-17a0-3f0d-b23f-81ce2f21d7b9 | -14.953 | -49.7975 | 2025-11-14 00:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 7e02de62-305c-3085-b550-8da9c592b5f0 | 3.146 | -60.7075 | 2025-11-14 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a248b997-08e4-3d6f-bb32-6b03c307eac7 | 3.1094 | -60.746 | 2025-11-14 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ed41262a-bac3-30b1-b896-9cf73989161a | 3.1094 | -60.765 | 2025-11-14 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 09b7a851-c897-3d8c-8073-a6ea19154258 | -4.7204 | -46.4497 | 2025-11-14 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 150.6 |
| fe3c5b1a-7e69-3fdb-a170-0a9846e48cd7 | -11.8483 | -49.2436 | 2025-11-14 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8ee02079-0926-310e-a1ea-c63ea05dafa3 | -11.8486 | -49.2218 | 2025-11-14 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 400.8 |
| 2b881758-6cd6-3a2f-b057-99370e5a6362 | 3.0912 | -60.7464 | 2025-11-14 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a9f674cd-b5a7-3167-b866-ada9876d4827 | -4.702 | -46.4286 | 2025-11-14 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3615b009-46d5-33d2-a88d-e9b38d6731d1 | -12.6996 | -45.4104 | 2025-11-14 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 7b46dfb7-e7e0-3d07-943d-6857f58f2977 | 3.1093 | -60.784 | 2025-11-14 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e45c9466-5f0b-3d2c-85ba-03304f288205 | 3.0911 | -60.7653 | 2025-11-14 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 293.0 |
| 277fc3c3-39cc-348f-9c33-0dff4606175d | -11.8681 | -49.1976 | 2025-11-14 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c6cf9f34-6b54-3719-999c-2637818c2940 | -2.8481 | -45.4862 | 2025-11-14 00:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 9ad39a65-9c46-388f-9164-a98d329b6fd7 | -7.8665 | -44.3077 | 2025-11-14 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| f45a4510-902b-360b-8ee9-d132a822a02d | -2.8295 | -45.4868 | 2025-11-14 00:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 6c6b2e37-37a3-347a-a3c0-744ac45ed595 | -11.849 | -49.2 | 2025-11-14 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 88ccc535-bc26-349a-b31c-639e543f7126 | 3.0911 | -60.7843 | 2025-11-14 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 532494c2-e7db-3b32-b3be-8840d5d5e30e | -12.6992 | -45.4335 | 2025-11-14 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 61f022d1-fdcd-3695-a47c-ea633495ffb6 | -11.8677 | -49.2195 | 2025-11-14 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 9ad62da2-2e39-3769-8ddb-77e304c5b7d1 | -20.82732 | -45.84167 | 2025-11-14 00:28:00 | TERRA_M-M | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| db5b3f7b-4017-3027-9e71-a21373fe329f | -21.49737 | -48.64949 | 2025-11-14 00:28:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1b23bf68-7b30-3df3-a835-638b6820891d | -20.26305 | -41.55577 | 2025-11-14 00:28:00 | TERRA_M-M | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| d15739c6-2658-3c5b-b47a-6ec1955e6751 | -11.8677 | -49.2195 | 2025-11-14 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 0cef06da-325e-3ce0-b24c-d30ab45737d1 | 3.0911 | -60.7653 | 2025-11-14 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 304.9 |
| 42459806-4fc3-36d9-bfc3-2858d242e56c | -4.7018 | -46.4508 | 2025-11-14 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 0378eff7-77bf-3136-999d-1a4e4ce1b6c3 | 3.0911 | -60.7843 | 2025-11-14 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 4ed33c21-fce5-3ea1-82a9-11597b123f33 | -12.7189 | -45.4074 | 2025-11-14 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| cc239f85-d121-365a-aded-3eddea231d6b | -7.8476 | -44.3096 | 2025-11-14 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e622d641-4946-3ba3-8dd5-f0ad471079de | -12.7185 | -45.4305 | 2025-11-14 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 8eab02ad-bddf-322a-9756-73eac4914474 | -2.8481 | -45.4862 | 2025-11-14 00:30:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 24d3fcb7-6918-3b51-a0b1-6733139d7c7c | 3.1093 | -60.784 | 2025-11-14 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 582587af-c533-3c96-9dcd-2ff8b9e4b652 | -11.8486 | -49.2218 | 2025-11-14 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 375.3 |
| a23b9e8e-b84d-35b8-8235-7ac8643dd4a0 | -11.849 | -49.2 | 2025-11-14 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |


[Clique aqui para ver as próximas entradas](README2.md)
