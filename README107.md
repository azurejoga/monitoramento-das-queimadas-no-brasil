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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25c9c98d-4a91-3add-9f28-d4d1556444aa | -1.07416 | -53.6517 | 2024-10-25 05:25:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e43e3737-460f-34cc-a827-c0525227c457 | -1.06088 | -53.65685 | 2024-10-25 05:25:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 090af494-23a5-3d20-ac1a-454d89f40dee | -3.09986 | -53.70565 | 2024-10-25 05:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1776711f-81ae-3330-bc14-a6d0ed209044 | -3.09611 | -53.7292 | 2024-10-25 05:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 33df7038-233f-3c5b-a6e5-31f843507748 | -3.09245 | -53.72131 | 2024-10-25 05:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b8a2c388-6ed5-3b8c-8352-57262212ac35 | -4.13149 | -54.62144 | 2024-10-25 05:25:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 033d98d0-785d-3cda-9f29-4e05e59e6936 | -4.12987 | -54.61575 | 2024-10-25 05:25:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 7e17973a-405e-3da0-8e0d-3da506b27cbb | -4.12565 | -54.64282 | 2024-10-25 05:25:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 7a251786-e202-3bc0-9872-3608f6bb1a1d | -1.1834 | -53.6569 | 2024-10-25 05:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 41ecf4dd-95f3-3486-a898-6b526a4b87b6 | -1.5878 | -53.3089 | 2024-10-25 05:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 4cd15577-3d30-3424-b80c-748d97f714ec | -1.6062 | -53.3087 | 2024-10-25 05:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 81365fa7-e8c4-345d-8737-cdbfaf31d1ca | -5.9788 | -45.3621 | 2024-10-25 05:25:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 78070e67-90fe-3893-9a74-a8ebfabade75 | -17.24073 | -57.50722 | 2024-10-25 05:27:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.7 |
| cf7f480f-b23f-317b-8bc3-7ca1439f4231 | -17.23312 | -57.21108 | 2024-10-25 05:27:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.0 |
| 2d4d8c7a-cf51-314d-8e70-760d11ea5518 | -17.22841 | -57.23582 | 2024-10-25 05:27:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 40fbdd75-1855-3aab-b5c8-9c645d4e31cf | -17.21453 | -57.23295 | 2024-10-25 05:27:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| 62a4cb8e-c174-302f-abbe-b424f3415df2 | -17.085 | -57.40339 | 2024-10-25 05:27:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| 7ab8e899-8f36-3f5a-9291-f3eb144f9114 | -17.07536 | -57.40633 | 2024-10-25 05:27:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| fec527cd-9ab3-3b33-ac9d-0264b4b5fd9a | -16.99615 | -57.33178 | 2024-10-25 05:27:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 0d7ffb59-56b9-3805-b06f-364bb02b6662 | -16.99123 | -57.35727 | 2024-10-25 05:27:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.0 |
| b87cb228-b041-3809-9791-ca2ded8faa61 | -16.98929 | -57.3492 | 2024-10-25 05:27:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.6 |
| bcb9eed1-8fe0-3cab-b6e5-0da19915fb22 | -16.93266 | -57.50687 | 2024-10-25 05:27:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.3 |
| d9e35b95-36eb-3fcb-bbd9-81522a84f181 | -16.93183 | -57.49895 | 2024-10-25 05:27:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| ed7664c7-0f92-37a8-aa51-6f0dd14c781d | -16.92685 | -57.52532 | 2024-10-25 05:27:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.9 |
| d596d055-255d-36de-9fac-e9db7e216088 | -16.90334 | -57.49302 | 2024-10-25 05:27:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 2e791ee3-bcf3-3d21-b881-d4479253e43d | -15.26023 | -43.62362 | 2024-10-25 05:27:00 | AQUA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 9ee5b91c-90c5-38aa-8554-e9c8485f696e | -11.5761 | -43.96921 | 2024-10-25 05:27:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3cc24146-94b8-3558-aba6-55e3fcdcd938 | -11.57432 | -43.98258 | 2024-10-25 05:27:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 85a5b308-fbd7-3e26-8c5b-8fd58cfea9da | -12.58069 | -43.83486 | 2024-10-25 05:27:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 67e5cad5-7d1f-38a1-b777-c5e9fd6d7976 | -12.57858 | -43.82916 | 2024-10-25 05:27:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 11377c8b-89d2-3e92-99ea-dfca86b606d8 | -12.89733 | -45.07029 | 2024-10-25 05:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8a21cdce-3593-3c30-ac1d-3cd622bec1a5 | -12.17072 | -46.9813 | 2024-10-25 05:27:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 13db6dab-525c-3dd0-a34b-7971f8149d21 | -12.55808 | -47.04375 | 2024-10-25 05:27:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 80f9787a-aecc-3b55-ac6a-ecabedebfd5e | -11.62799 | -48.46481 | 2024-10-25 05:27:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cf89098d-a2e4-3d35-b561-22a384b5494e | -11.62664 | -48.47382 | 2024-10-25 05:27:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f30751ab-9459-3f40-b20a-1a3c6892d1d2 | -11.6001 | -48.58964 | 2024-10-25 05:27:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11ee17e9-9285-35fa-bffc-bc015afe68ae | -11.59667 | -48.55219 | 2024-10-25 05:27:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3bfb1a41-61cf-3450-925b-7977eb686bc5 | -11.58981 | -48.47741 | 2024-10-25 05:27:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d1ff4609-7408-3c11-a59c-30edd1159fb6 | -11.29266 | -48.4875 | 2024-10-25 05:27:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e272a55e-8c61-3ea5-a2cd-3e0d995e941d | -11.2913 | -48.49647 | 2024-10-25 05:27:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f3c9ebda-a4bc-3a32-b095-c297908da4bc | -11.28378 | -48.48617 | 2024-10-25 05:27:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e342eade-d673-3899-a109-5d014ccb88cc | -11.07552 | -47.89762 | 2024-10-25 05:27:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5831f70e-ed11-3ff1-af42-1e1fd3c3b172 | -15.67118 | -55.96436 | 2024-10-25 05:27:00 | AQUA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 665870e5-fae4-3b93-a4c8-345c447c8938 | -15.66935 | -55.96918 | 2024-10-25 05:27:00 | AQUA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 702dcde8-7cd6-3808-99fe-6b0f31dd21c8 | -15.6674 | -55.98559 | 2024-10-25 05:27:00 | AQUA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 2b5e703c-eb43-3adc-9088-982dd2cddeb2 | -15.66541 | -55.99039 | 2024-10-25 05:27:00 | AQUA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 33.2 |
| c80ae6d7-9a60-33ba-a3a7-c5af95ac3568 | -17.01131 | -55.99975 | 2024-10-25 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 303c1da6-d53d-3d15-91fd-a0bfe273c3a3 | -11.89698 | -56.40034 | 2024-10-25 05:27:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 92f8bdde-9a40-373d-b7c0-ec2c8aaaa358 | -17.24575 | -57.48133 | 2024-10-25 05:27:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| ce16ceb0-f798-399b-a25d-49012539da98 | -18.26514 | -56.01188 | 2024-10-25 05:29:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| e73773e7-ed8b-32a6-9cb0-11357d51a266 | -17.68701 | -57.33586 | 2024-10-25 05:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.5 |
| fe12864a-ffa4-3b34-b7c3-bf9cc8d20da3 | -5.9788 | -45.3621 | 2024-10-25 05:35:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 88d7e362-b420-36c5-b61a-8047ec2b40bf | -1.6062 | -53.3087 | 2024-10-25 05:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| fc724125-4424-37ce-bc47-cfd98eb8e232 | -2.75056 | -67.02729 | 2024-10-25 05:53:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe7058f3-0992-39e9-aaf8-7f8b642719dc | -2.74779 | -67.02332 | 2024-10-25 05:53:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6289948f-21c8-3ad1-a48e-9bc85772574c | -2.74725 | -67.02678 | 2024-10-25 05:53:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eec28ef2-86d3-3e6e-a827-47c87510689a | -3.44425 | -54.63313 | 2024-10-25 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f0e64a7-9434-3a7c-8aac-2ab3eecf553b | -3.44331 | -54.63961 | 2024-10-25 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9048c341-ba13-3544-ba4c-39fff8eeede3 | -3.13581 | -54.27617 | 2024-10-25 05:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24976d5a-73b9-367b-bdb4-168942866aab | -3.10349 | -54.16647 | 2024-10-25 05:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4de52197-479f-3478-98c4-c7c130f68f4e | -3.10325 | -54.15285 | 2024-10-25 05:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d67cefa8-0a6f-3524-aeb8-75066c9d5e28 | -3.09757 | -54.15789 | 2024-10-25 05:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 828338f3-31d9-3db7-9ef3-2c07d0888bcf | -3.45179 | -54.63267 | 2024-10-25 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4defb39b-9bf2-3906-88e6-cb338608888b | -3.45112 | -54.6342 | 2024-10-25 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b8df70e-c3fc-3e05-aacf-71486d521ffd | -3.44403 | -54.63803 | 2024-10-25 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59ed841c-3555-359d-9295-595bb0c96ab7 | -3.10921 | -54.1615 | 2024-10-25 05:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce56aca6-4d5d-36d4-a5de-1b498754d106 | -3.10818 | -54.16882 | 2024-10-25 05:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c593c9d-eb97-393c-b4ed-84ef98911f0b | -3.10566 | -54.1518 | 2024-10-25 05:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fc828a8-bc7b-3aa9-8517-da030c0924ce | -3.10458 | -54.15908 | 2024-10-25 05:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce896493-9a83-3173-95f6-a3554aff9fb9 | -3.10221 | -54.16024 | 2024-10-25 05:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e27be01-1c3f-3fe5-9abf-435322c8cf83 | -4.29799 | -55.08614 | 2024-10-25 05:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aaf35e43-b184-3c18-bdfb-98959a077b69 | -4.2972 | -55.09174 | 2024-10-25 05:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8832a09e-68da-3b42-8c84-49826772a3c3 | -4.12898 | -54.63045 | 2024-10-25 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| da6ff163-d8fc-3b0c-b85e-0b65dfd05882 | -4.12894 | -54.63485 | 2024-10-25 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 48f71003-5c35-3969-95f6-b5021a75fe06 | -4.03293 | -54.61428 | 2024-10-25 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50b0a16a-4564-3fc5-b450-34c18d1b1387 | -4.0322 | -54.61847 | 2024-10-25 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 87e43574-d328-3645-a8a0-f4b6d955f025 | -4.03191 | -54.62123 | 2024-10-25 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dba353fa-d863-35fd-8f8e-979a3032bf0d | -4.12808 | -54.63687 | 2024-10-25 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 70ac8592-0530-3ba5-90c3-9a21fcbb19bc | 1.57509 | -55.65464 | 2024-10-25 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a03af7df-c186-3387-b8af-2c7035c02b2a | 1.57285 | -55.65388 | 2024-10-25 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8dbc9527-b782-358e-a6f6-6bf418f975b7 | -1.97574 | -56.4235 | 2024-10-25 05:53:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 677a237b-4226-3649-ba7a-3fd9d5b571e1 | -1.97506 | -56.42801 | 2024-10-25 05:53:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5a20e0c-9296-3a09-b008-bab3600c73ad | -1.96697 | -56.44079 | 2024-10-25 05:53:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce818755-b27b-3398-943b-e8f9c6aae5e1 | -1.96628 | -56.44542 | 2024-10-25 05:53:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76a62771-8cf5-3788-9932-51f5a63e96d8 | -1.96094 | -56.43989 | 2024-10-25 05:53:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92f59af4-df5a-38b0-bb1f-fea0d7713af0 | -1.96025 | -56.44451 | 2024-10-25 05:53:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8880e4da-ea7e-3fe3-94ab-7fe5e181e193 | -1.28401 | -55.71712 | 2024-10-25 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4784d87f-81fe-354e-84e9-86942c44933d | -1.28329 | -55.72197 | 2024-10-25 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e38473f-6c6d-3392-9b3e-b24e0eb76306 | -1.52773 | -55.40889 | 2024-10-25 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54becea4-95e4-325b-9619-3b46c3c9fc5f | -1.28545 | -55.72014 | 2024-10-25 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a80b7c73-5531-3fd4-b590-e0391735df65 | -3.50023 | -55.47582 | 2024-10-25 05:53:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7489c4b-1da2-3e82-a483-5a7999f6ed02 | -3.49363 | -55.47527 | 2024-10-25 05:53:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0ebdce2-2019-3301-94b2-9b8a239520a3 | -2.732 | -57.45802 | 2024-10-25 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e6b92bc-bb4f-3158-91cc-e81eeb6da6db | -4.32653 | -59.99068 | 2024-10-25 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea135990-88b6-3150-9932-6ed3c73c7177 | -1.44662 | -60.31906 | 2024-10-25 05:53:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 490c9764-300d-36c3-a5ae-7217765943bd | -1.44591 | -60.32383 | 2024-10-25 05:53:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f73f9528-479f-38dc-9343-e26971b8820f | -1.75066 | -60.54551 | 2024-10-25 05:53:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 955deabe-f299-36c6-8440-b5fab3f7bca6 | -1.44631 | -60.3227 | 2024-10-25 05:53:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6d5d966d-4b07-333a-a6ee-d5ac27124e21 | -1.41925 | -60.40529 | 2024-10-25 05:53:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0cb3d7a-37ac-3b9b-b1a7-39248490f9e7 | -3.01481 | -61.69805 | 2024-10-25 05:53:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README108.md)
