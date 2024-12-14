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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd669c1d-4961-35f6-adf1-d7d6c17ecb8c | -6.28975 | -37.24218 | 2024-12-14 03:59:00 | NPP-375D | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a396425b-6b03-34c4-bc86-2b0f7192dddc | -3.38854 | -44.15209 | 2024-12-14 03:59:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bd58e0c-456d-361d-a755-03147175cb6b | -4.40396 | -41.43197 | 2024-12-14 03:59:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7a92bb43-a4d7-3e9c-b05b-ece415eebbb3 | -2.92279 | -41.46589 | 2024-12-14 03:59:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 33ea0aea-2312-304b-bb8e-3a4931a846a7 | -4.17701 | -42.42966 | 2024-12-14 03:59:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f29875d-40bd-3e1e-8c12-70e95f0a6c36 | -5.50741 | -45.49044 | 2024-12-14 03:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68d96dd6-6fb3-3bb7-91e5-78e2c0d6cfa1 | -6.78018 | -38.32657 | 2024-12-14 03:59:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2e8aa330-a483-32fc-bfdf-8eea2c853d6b | -6.6255 | -38.42399 | 2024-12-14 03:59:00 | NPP-375D | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 80c6c53a-a8e4-32eb-bd5d-c63ea5154e5c | -4.17636 | -42.43375 | 2024-12-14 03:59:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4af3375f-70a1-3b07-8c7a-42b080e2334d | -3.56535 | -43.65993 | 2024-12-14 03:59:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 364e40fe-f86b-3277-af47-85d4b86f156b | -5.24381 | -37.68987 | 2024-12-14 03:59:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f357d72-7d5d-3a10-b7e5-05a078dbdb40 | -4.09797 | -46.61085 | 2024-12-14 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3aef66bb-fbe2-3625-a705-2524ea6af58b | -2.96446 | -39.96369 | 2024-12-14 03:59:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f1f87b84-3d52-3b80-885d-3b0adc989671 | -5.11254 | -43.146 | 2024-12-14 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a207e9b-63df-3f7f-bb14-e1b8ef5dd7a6 | -3.45359 | -40.8143 | 2024-12-14 03:59:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 29e32c88-a8f9-3b1c-b40e-9cd937495c75 | -3.2515 | -46.85492 | 2024-12-14 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0e561f10-c557-3ece-8249-3c78baa08a3f | -2.92217 | -41.4697 | 2024-12-14 03:59:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aba0f62a-7b71-39d2-800c-73fa22954631 | -4.71634 | -43.19275 | 2024-12-14 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec3c6edf-9fa9-3d5d-a23c-7eb7d1ee8340 | -7.20013 | -38.41228 | 2024-12-14 03:59:00 | NPP-375D | MONTE HOREBE | PARAÍBA | Brasil | 2509602 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 73cdbdf2-3d0d-3f74-86bf-6e4a98959b58 | -4.17342 | -42.42909 | 2024-12-14 03:59:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 5b17349b-2574-3aa4-8a6d-533995f59239 | -3.882 | -44.41758 | 2024-12-14 03:59:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5df8c567-b3e9-3653-ba6b-1b01df82615b | -3.45641 | -40.81845 | 2024-12-14 03:59:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 978aaef3-79c2-363b-a47a-92a4c0300f15 | -1.33268 | -45.31417 | 2024-12-14 03:59:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 047271e5-268f-34e6-ba4f-4b31a38f7b21 | -6.4559 | -39.70363 | 2024-12-14 03:59:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d80f3433-c9e3-3291-b65d-3500017d5bf8 | -6.09867 | -44.75856 | 2024-12-14 03:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fc155d9-4fdb-3ba0-b775-f68b9e56aa12 | -4.17399 | -42.43212 | 2024-12-14 03:59:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 69cb543c-f097-33ca-930b-96de5584a07c | -3.38454 | -44.15143 | 2024-12-14 03:59:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11ddb48f-1560-34ff-9a00-a002c2af0766 | -5.26481 | -41.3912 | 2024-12-14 03:59:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 53b97409-a9e7-3774-afd0-bc2b291f22a1 | -6.09053 | -37.62138 | 2024-12-14 03:59:00 | NPP-375D | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 81b6ac50-47a4-3c99-baed-273004e6d441 | -2.89152 | -44.36995 | 2024-12-14 03:59:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f648390d-a63a-3094-a5bf-708a24ac947a | -5.06427 | -42.61402 | 2024-12-14 03:59:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b87bb1a2-fe9e-3cfb-bd28-32e7931c1ffa | -4.96569 | -38.73641 | 2024-12-14 03:59:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dd3f02f5-2732-394d-870d-87ecd4f0eed6 | -4.16853 | -42.43669 | 2024-12-14 03:59:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd7a9eb1-759e-3c73-bb68-67909de185af | -2.92511 | -41.4667 | 2024-12-14 03:59:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7a99f44c-de84-3f73-a6c8-078e946929d3 | -5.09643 | -46.02847 | 2024-12-14 03:59:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 129dec55-a418-3c0b-b905-f632e66f4314 | -4.52849 | -42.06994 | 2024-12-14 03:59:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2c5636a9-17b2-3f72-a00e-e6408fd9996c | -5.09489 | -46.03027 | 2024-12-14 03:59:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19b47f47-9a32-373a-abf1-5cd21c508162 | -2.53959 | -45.37947 | 2024-12-14 03:59:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5f32b66-ade3-37c2-bd5b-fca90711066f | -3.24906 | -46.86066 | 2024-12-14 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5cbc3f14-eb91-3510-b587-ee501549d004 | -5.30892 | -46.06794 | 2024-12-14 03:59:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 838f3606-01b3-3547-9e94-885ecfbc9483 | -4.16983 | -42.42851 | 2024-12-14 03:59:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| bc64d21d-3dba-34d8-ad6f-7853b860dad3 | -4.10647 | -46.61756 | 2024-12-14 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2f7e80d-c938-3337-8bcd-b7e8ccad18c2 | -3.59958 | -41.67457 | 2024-12-14 03:59:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ed5c1b19-c3a3-3cff-abdb-091507b8e8d4 | -4.09716 | -46.61578 | 2024-12-14 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| fa344eff-eb34-3650-abcb-0a33cae3fb4b | -6.52541 | -41.28181 | 2024-12-14 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e6d7d412-9755-3b56-b7a7-c04b84834fab | -4.72005 | -43.19334 | 2024-12-14 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32a36fc6-2334-344a-94bf-7e5f51d94330 | -6.51867 | -41.28074 | 2024-12-14 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e0c7cedd-e913-3038-9270-1b981129b96d | -3.46092 | -40.81536 | 2024-12-14 03:59:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 30a21279-91c0-3a48-a053-6b091a5e3357 | -3.29621 | -42.51987 | 2024-12-14 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf9c74cf-3886-3716-9d5e-ace6ddcf9aad | -4.16918 | -42.4326 | 2024-12-14 03:59:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 4f8ce8eb-3244-316a-b083-e4c7bb7412e3 | -5.2654 | -41.38751 | 2024-12-14 03:59:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e96e604-c34b-3465-9ad4-3ff30e27b152 | -3.24994 | -46.85546 | 2024-12-14 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 93ad6b86-aae1-36bd-83b7-7b25641aa681 | -5.26879 | -41.38813 | 2024-12-14 03:59:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 135f1a43-dbfe-37ca-9cac-41591e0bec2c | -3.25388 | -46.86147 | 2024-12-14 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6728478b-f6d3-3355-9693-6da1ea5d6bd4 | -2.26218 | -44.81323 | 2024-12-14 03:59:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fa2b6c2-1f76-32a2-b2d0-e1cb3155eecd | -4.40337 | -41.43567 | 2024-12-14 03:59:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 81049780-82b2-3249-a5a8-15fc46ebd0ac | -5.05644 | -42.6169 | 2024-12-14 03:59:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 24a771a0-d349-337e-9766-b54d5a23f673 | -4.17758 | -42.43269 | 2024-12-14 03:59:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 70e0d40b-be43-3fd3-837a-de876652cfec | -5.01413 | -39.7142 | 2024-12-14 03:59:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e83ef7f8-3a28-3bbd-b841-527a4586d367 | -6.67212 | -39.40511 | 2024-12-14 03:59:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a606a663-171d-3bd0-8f1d-e57e53776bb6 | -3.56456 | -43.66472 | 2024-12-14 03:59:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58c833fe-9801-3984-a845-894fc9c2454c | -6.51078 | -41.28684 | 2024-12-14 03:59:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5b882f38-4d92-3eb0-9109-073ac374fde0 | -4.77446 | -37.81346 | 2024-12-14 03:59:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 59b81d24-0fb8-3f84-b797-5d54f2dc1718 | -5.53944 | -42.85866 | 2024-12-14 03:59:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 91241d93-4394-305f-bb6a-e6fe8731d5a5 | -5.93249 | -46.05977 | 2024-12-14 03:59:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af77ea88-5df4-3297-850c-5b5641139075 | -3.29689 | -42.51753 | 2024-12-14 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02e5af0f-f7ff-3a89-ad05-c3f82d64bded | -3.90421 | -44.15919 | 2024-12-14 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f69a6d6e-0fe7-397a-9d03-d7d8abca1854 | -4.10181 | -46.61667 | 2024-12-14 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2f731ede-3b19-3113-9948-565e8797b2d8 | -3.25066 | -46.86013 | 2024-12-14 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 637fb711-6db6-3807-b429-d26f2f2e3560 | -4.52083 | -42.07273 | 2024-12-14 03:59:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fefc4ad3-d3fd-3b53-a831-2520fd4378ed | -4.71933 | -43.19774 | 2024-12-14 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fcc00e88-f90e-34fe-a6a0-bc57820b4840 | -6.62001 | -39.17822 | 2024-12-14 03:59:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4710e27e-314e-32ed-9847-7398a6bede27 | -3.18259 | -39.41909 | 2024-12-14 03:59:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c55d82fb-94f8-3021-bdeb-a758eb89e752 | -4.77103 | -37.81293 | 2024-12-14 03:59:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9326e32f-7385-3c9b-93bb-e9d407849ff2 | -5.0956 | -46.0261 | 2024-12-14 03:59:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a9aface-899a-3ae0-b703-0a978e371c70 | -1.90334 | -45.71826 | 2024-12-14 03:59:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3520b07c-2c19-389b-9991-9686943b6b74 | -4.101 | -46.62163 | 2024-12-14 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dbefff14-5d22-34f0-b5bb-fa367cbc5771 | -4.52497 | -42.06939 | 2024-12-14 03:59:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dbfd3e7e-6320-3064-a2b3-66575f485d6d | -3.45698 | -40.81484 | 2024-12-14 03:59:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 521f9000-b775-3d79-be8f-2a6c18cbc0bb | -4.77788 | -37.81398 | 2024-12-14 03:59:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 68e8fae4-cc5a-3f16-9c0c-2f73fedef0d9 | -3.25081 | -46.85026 | 2024-12-14 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 271355a6-a398-32a9-8132-f34179b9ee80 | -3.00416 | -44.41717 | 2024-12-14 03:59:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e93585c-d060-3e88-b4fa-0272ee8f101d | -4.66463 | -46.49274 | 2024-12-14 03:59:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8eff75c1-b871-32a7-a4ab-8574292b4b4b | -3.7414 | -43.12962 | 2024-12-14 03:59:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3076aa0-ef95-3f79-b994-12d63fdc16a6 | -1.33556 | -45.31235 | 2024-12-14 03:59:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b9e96b4-8011-3533-ab05-7c0d98de9cc3 | -3.479 | -43.34108 | 2024-12-14 03:59:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 897d40e0-dece-3820-af54-21342bf134d5 | -5.43474 | -37.8493 | 2024-12-14 03:59:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c9b314b4-a316-39db-81ac-a8a0e7e19513 | -3.0159 | -41.12934 | 2024-12-14 03:59:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 075ede45-7244-3d3b-95ed-614aa68955ed | -3.74109 | -43.12688 | 2024-12-14 03:59:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d84ecf2b-e078-3499-b019-ef177d2d8bba | -4.65986 | -43.8211 | 2024-12-14 03:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56b1ad4e-1ee8-3f65-ab1e-f942d89fa041 | -3.29188 | -42.52349 | 2024-12-14 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd3f5f31-dfda-39a1-929f-a51f2b1fccd2 | -3.17927 | -39.41857 | 2024-12-14 03:59:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 33677c1f-e199-3cc8-8027-9491cfc95b34 | -4.09837 | -46.66671 | 2024-12-14 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30057682-b338-344f-96dc-f4e30804e009 | -5.53584 | -42.85803 | 2024-12-14 03:59:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0eb74540-02ea-3925-9724-7f3f064d4e81 | -4.12556 | -43.2397 | 2024-12-14 03:59:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9357f6f-1ec5-3c5a-a188-5d82e717586f | -3.29325 | -42.51695 | 2024-12-14 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72ea0068-e8e7-3b60-98af-c20e6edcc65f | -3.90694 | -44.15785 | 2024-12-14 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 524e35fc-3fa6-326d-918d-6a2605c6a941 | -3.00006 | -44.41651 | 2024-12-14 03:59:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4540a4bc-2d9b-3880-b11f-6dcbf14027b0 | -3.56148 | -43.65929 | 2024-12-14 03:59:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe50d7d1-6fb7-3ae5-8492-ccb79b3a3a34 | -6.56134 | -39.11486 | 2024-12-14 03:59:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
