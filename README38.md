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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27590232-7dcd-325f-ac4e-020dbaea43f3 | -17.55613 | -54.02266 | 2025-11-13 05:08:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 997eb9d4-bc66-3d0e-95f1-a8f32df4244e | -21.89422 | -56.73722 | 2025-11-13 05:08:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 67c18b7f-bac4-392c-b87b-3a4992e24041 | -21.88659 | -56.74032 | 2025-11-13 05:08:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42169f15-8380-34e3-97cd-810d9b0e75ee | -4.2056 | -48.5706 | 2025-11-13 05:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 92219669-505a-3eab-9ef0-9b6d0bb31676 | -4.7206 | -46.4276 | 2025-11-13 05:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 528f3285-26d1-3c64-b1f7-0a08f1a9e9f3 | -12.6553 | -46.7633 | 2025-11-13 05:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 23837290-8cb9-35e1-9be4-a2573c12054f | -3.0916 | -49.2759 | 2025-11-13 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 8cf5711c-58fb-36b3-a6c7-116fbd87ff8c | -12.6557 | -46.7407 | 2025-11-13 05:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2d396ce7-5559-3f7a-8a10-babc7a190d62 | -4.7204 | -46.4497 | 2025-11-13 05:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 61e74190-c7ad-3bad-9d38-313b4f081c75 | -4.7018 | -46.4508 | 2025-11-13 05:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 40.3 |
| e25e6b88-e352-3b59-9cba-63848932801a | -12.6749 | -46.7378 | 2025-11-13 05:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f23f6778-2310-3c55-9018-3c3b13876e21 | -12.6557 | -46.7407 | 2025-11-13 05:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| ba04f2cd-f9e7-3a34-ace7-ef409a992925 | -3.0916 | -49.2759 | 2025-11-13 05:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 7caa4019-d5af-3af8-9fc5-6c61a9ff35fd | -4.7204 | -46.4497 | 2025-11-13 05:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 53a9554e-2a54-336e-94a9-574db1b9e705 | -4.7206 | -46.4276 | 2025-11-13 05:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c432c721-30d2-39a1-b470-b34a0bfa0a84 | -4.2056 | -48.5706 | 2025-11-13 05:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| fd19f9e1-c5dd-38d7-a9a5-3d9a5a5750c9 | -4.7664 | -42.7043 | 2025-11-13 05:30:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| d3d6cf46-cde0-3015-a2f6-d0e299a1cd2a | -4.7018 | -46.4508 | 2025-11-13 05:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 38b13004-05db-3a19-bc47-71cb6008cceb | -3.0916 | -49.2759 | 2025-11-13 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 329956b2-3fcc-3af4-8484-a2810d74eb0b | -4.2056 | -48.5706 | 2025-11-13 05:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 1a54b0c3-cb08-3aa0-9eaa-cf027267e1b3 | -4.7206 | -46.4276 | 2025-11-13 05:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 497e72b4-384b-3a3a-98c2-dc41d9da28e2 | -4.7204 | -46.4497 | 2025-11-13 05:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 3b563532-0136-3787-91de-7afc0bd2b00a | -12.6553 | -46.7633 | 2025-11-13 05:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| e9029e81-b579-351b-bb89-f9aba9a4f799 | -12.6557 | -46.7407 | 2025-11-13 05:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 0c18dbb1-f92d-32c4-a66e-cd5648103596 | -4.7662 | -42.7279 | 2025-11-13 05:30:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 1098ab3f-9e20-37ef-a4fc-8cd56017bb81 | -4.7664 | -42.7043 | 2025-11-13 05:40:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 7445ed85-e45e-30f4-b59f-527d2ce8da56 | -4.7018 | -46.4508 | 2025-11-13 05:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 3eac149f-f0c7-3e39-9c3b-e387543a3644 | -4.7204 | -46.4497 | 2025-11-13 05:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e6d4ed0f-342f-324a-95d8-e2594f271a01 | -4.7206 | -46.4276 | 2025-11-13 05:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 31.9 |
| e2287c88-1771-3687-98e4-ac968fba07cc | -4.2056 | -48.5706 | 2025-11-13 05:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 27767af3-1b37-3cf7-a405-5593eeddafb7 | -2.00532 | -54.45333 | 2025-11-13 05:52:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 658fd441-01b5-3944-a711-b1918590b377 | 3.30148 | -60.1251 | 2025-11-13 05:52:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7838d6ea-616b-39de-af6b-cb0a7009c8e5 | 1.4677 | -55.84412 | 2025-11-13 05:52:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c4cb00b-8fdf-3238-93d4-b45cd372246e | 3.30214 | -60.12914 | 2025-11-13 05:52:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92460bac-687c-3389-b5cf-d77dbd6351c7 | 2.95036 | -60.8445 | 2025-11-13 05:52:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66e689ce-c709-3a81-9110-f6a5356c0090 | 3.2972 | -60.12593 | 2025-11-13 05:52:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6b3c6c5-e44a-3d18-bc48-28401aee6011 | -4.2056 | -48.5706 | 2025-11-13 06:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| f85712a0-379f-3349-a4af-6a2117de7693 | -4.2242 | -48.5697 | 2025-11-13 06:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 202bdfb8-10f0-38f7-bac5-886191dc731e | -4.2056 | -48.5706 | 2025-11-13 06:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| ceb7e663-141c-3e7c-a16d-2b2ee61c9a64 | 1.46121 | -55.84212 | 2025-11-13 06:39:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ac7dcea-5bac-3d39-9072-703bd5bb81ea | -2.87499 | -51.47422 | 2025-11-13 06:39:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| a497b339-40ba-3c80-9ece-dee612822251 | -4.1491 | -45.5878 | 2025-11-13 06:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 96b2894c-9726-31ee-83e7-4197024a6def | -3.15703 | -43.54766 | 2025-11-13 12:16:00 | TERRA_M-T | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8ce872d2-3cf1-34ee-8619-074fc212b8e8 | -7.14661 | -41.25117 | 2025-11-13 12:16:00 | TERRA_M-T | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 823e293d-55c5-37fc-aa3a-a3961ff6709d | -7.22604 | -44.7331 | 2025-11-13 12:16:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| f3350c53-f873-3a73-b716-6b69abb7e85e | -4.27861 | -40.52399 | 2025-11-13 12:16:00 | TERRA_M-T | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| d76a5576-e691-3b7d-a010-68a0dd64fadc | -7.21864 | -47.98038 | 2025-11-13 12:16:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5e568ea0-44ae-3df0-ba09-70291fd844af | -7.07229 | -44.65833 | 2025-11-13 12:16:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 132a4f91-7a3c-31fc-9249-8fc1fc59df6f | -3.59997 | -39.81763 | 2025-11-13 12:16:00 | TERRA_M-T | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 36.4 |
| be160e31-90c6-34ed-9b39-02c9bfd81d52 | -7.21598 | -44.73166 | 2025-11-13 12:16:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1a18c935-2952-3337-bb2e-622a5acbd5cd | -7.21408 | -47.30419 | 2025-11-13 12:16:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b02bbdac-9c3d-309b-961e-60777762512b | -7.72004 | -47.19083 | 2025-11-13 12:16:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 77cb3cf7-699e-39d2-accb-f300462c96af | -4.74894 | -47.69899 | 2025-11-13 12:16:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 68086acb-167e-3268-90d8-89f5c35c5fc2 | -3.21007 | -44.3242 | 2025-11-13 12:16:00 | TERRA_M-T | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b4e5fc47-1709-3762-9bcd-bb278a9794cf | -3.58819 | -42.2123 | 2025-11-13 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 5e515c48-ac30-3df0-be5b-801215fb5e3e | -7.22486 | -44.7393 | 2025-11-13 12:16:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 32289289-70b2-3492-b793-7c4bb45cb975 | -4.62147 | -42.79597 | 2025-11-13 12:16:00 | TERRA_M-T | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7ab8b7db-82a5-3a91-813d-37d3af5d9f02 | -7.30356 | -45.28476 | 2025-11-13 12:16:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| c18656a4-6f20-31f8-9593-3d5faff1072a | -4.3351 | -45.49165 | 2025-11-13 12:16:00 | TERRA_M-T | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6372f19a-20d0-3842-a54f-13a13598ba5d | -5.67812 | -39.26574 | 2025-11-13 12:16:00 | TERRA_M-T | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 31.6 |
| d5b44342-94ce-36c5-b9ff-f4d98ebb7262 | -4.78558 | -44.40976 | 2025-11-13 12:16:00 | TERRA_M-T | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 0551ee32-6f5b-390d-b585-23cb02a8d58b | -6.51253 | -43.58875 | 2025-11-13 12:16:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9e369043-0f49-35d3-8c5f-c8e37154eb39 | -3.59037 | -42.1966 | 2025-11-13 12:16:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 057c8505-1324-3dde-ba7f-0ff1dcc049a6 | -6.88786 | -42.84234 | 2025-11-13 12:16:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 14380fc1-a352-3f45-95c2-810a87cb34e5 | -2.72437 | -47.40484 | 2025-11-13 12:16:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| ae205fc6-daca-3c11-bdb2-b33c3056b373 | -7.82645 | -41.76539 | 2025-11-13 12:16:00 | TERRA_M-T | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| fabde983-746d-386c-9163-2aab859482e7 | -7.77615 | -46.32319 | 2025-11-13 12:16:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a7996657-a505-38c0-8b5a-12afef419be2 | -6.90977 | -42.0752 | 2025-11-13 12:16:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| b5a30aec-bf0e-33ce-b2c3-9c1391b14129 | -7.72897 | -47.19205 | 2025-11-13 12:16:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f8031252-c117-34d6-b26c-99ba3d6b15e5 | -7.18087 | -44.98486 | 2025-11-13 12:16:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0817d741-f8a8-3993-a3cd-ee1e75e5c9d6 | -3.57457 | -41.73692 | 2025-11-13 12:16:00 | TERRA_M-T | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 70525d4e-e2a3-3841-b9f9-5a578241d186 | -4.77447 | -48.42575 | 2025-11-13 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bd3446c7-c632-3f0b-845b-56c4a58676fc | -2.03491 | -47.37516 | 2025-11-13 12:16:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f64c2b5d-2755-3adb-9c9c-c028d8e01101 | -4.37171 | -45.48303 | 2025-11-13 12:16:00 | TERRA_M-T | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 0a1999f4-bd51-30ff-8554-076f15c454f0 | -4.74815 | -48.40691 | 2025-11-13 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9d1ed34b-5577-33f6-b432-76f4dafc97f5 | -4.21803 | -48.56667 | 2025-11-13 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| caeab3b9-55b9-31ef-ab1c-d1307ad51f65 | -1.8883 | -47.04831 | 2025-11-13 12:16:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6122dde9-43a0-3bee-94ff-b023d74f30b3 | -4.25858 | -43.77672 | 2025-11-13 12:16:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a81e245b-9840-34a6-8899-4012fcc55f4f | -3.48484 | -44.04788 | 2025-11-13 12:16:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| c7ac3a88-5e77-327a-a469-6a8ccff763ad | -4.24656 | -43.78767 | 2025-11-13 12:16:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b6dbe40a-59d1-305c-8663-d5bd3a3cbde4 | -2.06412 | -47.37673 | 2025-11-13 12:16:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 32e61b27-db6c-3c93-b40f-52cc871e5ba2 | -3.56254 | -41.73537 | 2025-11-13 12:16:00 | TERRA_M-T | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| f26cf16e-7fff-324d-a500-3f4e9dd88b23 | -7.22295 | -47.30548 | 2025-11-13 12:16:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1e02b1f2-9254-3c0f-85c9-c6c86d83b821 | -5.43248 | -43.17278 | 2025-11-13 12:16:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b44e9cb8-1358-36bf-92b4-8b21b1a17a4e | -4.26832 | -42.11691 | 2025-11-13 12:16:00 | TERRA_M-T | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| ebf9ac6d-606b-3917-bdcd-9f2c9a9b0fdf | -7.38202 | -47.03565 | 2025-11-13 12:16:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 87ac305f-1866-3dda-97fc-89b1b64ba4ae | -4.78384 | -44.41527 | 2025-11-13 12:16:00 | TERRA_M-T | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 704b885c-3d8c-388d-936e-45bd5a314677 | -5.60364 | -41.06218 | 2025-11-13 12:16:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 4649cf15-638f-3780-98d6-8b5c42520473 | -3.26312 | -44.4599 | 2025-11-13 12:16:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d36bc128-4f29-3ba4-a3ec-857c6726e321 | -1.86838 | -47.45335 | 2025-11-13 12:16:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1c3bf1d3-337c-3705-8408-eb7970fbbc31 | -7.38979 | -48.65294 | 2025-11-13 12:16:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e94f35c1-2082-349c-8e7d-d98002def5fe | -4.64777 | -47.94715 | 2025-11-13 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5dc7a827-945b-39b5-bf1d-ee514f1cfe44 | -4.71648 | -46.44469 | 2025-11-13 12:16:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 64b45af3-cbe8-3179-979f-22ce01b116b3 | -2.97478 | -42.16652 | 2025-11-13 12:16:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 6958bd73-0073-3c7e-ab40-56569d296549 | -2.06538 | -47.36797 | 2025-11-13 12:16:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a003b402-67fb-3e7a-a7a8-df719e5f1c02 | -1.91591 | -47.04323 | 2025-11-13 12:16:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f51c4857-0d45-3ad7-a810-295a84e3fac6 | -6.30925 | -42.5437 | 2025-11-13 12:16:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| ecabeb3e-c958-3f5f-a3af-24cf70b15469 | -0.7843 | -47.9883 | 2025-11-13 12:16:00 | TERRA_M-T | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 63f80d90-7a1b-335a-b8f2-10f75397b0c2 | -5.68062 | -39.2604 | 2025-11-13 12:16:00 | TERRA_M-T | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 0266fb77-58e7-3a76-b46c-5515954f837f | -6.34206 | -43.65234 | 2025-11-13 12:16:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |


[Clique aqui para ver as próximas entradas](README39.md)
