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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef9b0cd7-ad96-3f8c-9731-5a19cae74d90 | -6.24716 | -44.01603 | 2025-10-16 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06b3e868-bf24-3299-92d8-b52de135359a | -9.58421 | -42.45338 | 2025-10-16 03:47:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a5d1a234-59f6-3ec9-a3aa-df0dcb6d646f | -3.01105 | -45.38537 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 022e7c7e-39aa-3343-beee-c4789214bc30 | -6.0336 | -41.92484 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ebfca849-668c-3ce5-b092-9404ff5fc40c | -6.04148 | -41.94144 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b5d5ab2f-4ef3-3432-9b2f-46def0d517c1 | -5.32272 | -42.92559 | 2025-10-16 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46a229cc-aa67-3623-b0b5-ebb16367999c | -5.85258 | -42.88335 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 924ce120-324a-38ec-8380-328d52bd5159 | -5.46716 | -44.64687 | 2025-10-16 03:47:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eaadfaf-ca46-372c-88f5-f89e0cc215c3 | -5.87252 | -43.90561 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08c92582-c81d-35bf-9a90-64ffd76d8cef | -6.44725 | -43.3829 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a71ee23-eed8-3b5d-99f5-a60a9dd8ddb6 | -5.86781 | -43.84781 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a5fa021-b555-3a40-955c-888100e4f466 | -4.38972 | -43.40755 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ae6ee0c3-f278-338d-a2b4-47a79ed54ed6 | -4.4985 | -45.4013 | 2025-10-16 03:47:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1aaa48c-387e-3bd9-b9fa-799e319f5661 | -4.35741 | -45.52967 | 2025-10-16 03:47:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45f90130-6dc2-3587-98e0-d0dabd7d9ed9 | -4.63915 | -43.13599 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bdf4e7f4-39ef-36ec-9032-22525b644806 | -5.71933 | -44.52718 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f42ee3c3-383d-3749-b91d-b68fbfda1206 | -10.69914 | -44.43094 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 49db8770-4484-347b-b518-2b75fbcad78a | -5.29829 | -41.17952 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 14deea9e-8745-3191-8422-f070b1f5914c | -6.14001 | -41.78413 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6c5a227d-b76b-3eea-aac6-d36f25d1a632 | -11.48311 | -44.0835 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb559ad4-2723-38c3-9538-11ca1ba2b7b8 | -10.1308 | -44.57401 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 827d036e-4266-330c-b2be-4705242bc530 | -11.58516 | -44.07059 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32272b59-10ff-34e2-a176-ed7b0638d6b4 | -10.33785 | -47.77093 | 2025-10-16 03:47:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3325940a-f74c-3f5e-94f0-b67e9d210013 | -12.92218 | -41.82213 | 2025-10-16 03:47:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64b0263e-f972-3d6e-a7ee-6fb207cfbe41 | -5.87284 | -43.87527 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec0a97ba-b8e6-3f2e-99f5-74dac32068c7 | -6.17171 | -41.71941 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6a69d6c4-5700-39c2-ba0c-d0bc9cbd6d61 | -5.23861 | -45.64275 | 2025-10-16 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 63db3477-6d76-3abf-91f8-3acaeb1e3407 | -5.62846 | -43.92427 | 2025-10-16 03:47:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f9aa4d5-4527-318a-80bb-65ceee395f2d | -5.91928 | -42.83468 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9acfddb9-6892-3345-bf33-7888e4ed7845 | -6.56503 | -42.968 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91da030c-a61e-3af2-8452-a1d77248fa6f | -12.17447 | -45.06171 | 2025-10-16 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89d90159-7b2a-3750-8dd9-04bf5592ed53 | -11.63591 | -47.56081 | 2025-10-16 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91f3ecc3-32a2-3cf7-abe3-6754e8afda15 | -4.01801 | -48.9747 | 2025-10-16 03:47:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 880c0e13-7697-3b95-9486-880805896c6e | -5.32542 | -44.83846 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 479a558a-cfdf-3367-abee-088151624775 | -5.42829 | -40.98392 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b5fb0ff5-bee0-354f-a1c6-c120dec12882 | -5.29574 | -41.18216 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 542d74b6-7c3a-3e68-a9eb-e42ea53980bb | -11.58796 | -44.07999 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e4354df7-c700-3657-b1d7-db396d5e83a1 | -11.70666 | -44.27375 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f4adf78-6661-392d-b6f4-f2f4134a9eb9 | -11.32694 | -41.67167 | 2025-10-16 03:47:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| d0717913-013c-3c78-96a1-2bf8ab643e30 | -3.60736 | -48.92703 | 2025-10-16 03:47:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dfcf623b-ff21-3e86-b2fe-0adceeb997d1 | -5.09944 | -45.48895 | 2025-10-16 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 018e8c33-f94e-3874-9831-7e415f69dba5 | -5.64559 | -45.97374 | 2025-10-16 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15efc6ce-0de7-3946-ae74-ffb09e663e90 | -3.01715 | -45.38275 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 8e070ddc-1aab-3a7b-b2cc-4ebc73e06190 | -10.03981 | -43.83043 | 2025-10-16 03:47:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dd87a07-8f37-3f74-82c9-b727dd5d0bae | -12.64304 | -44.30487 | 2025-10-16 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb461524-c9fd-3f25-ab7e-6567fc9f300f | -10.12621 | -44.57302 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 720b06c4-ecf4-314c-adb9-7b2ee2be4d16 | -10.15068 | -44.54223 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b20fb95-644c-3ac4-87d8-6f28be1e2889 | -6.33562 | -44.01799 | 2025-10-16 03:47:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34a35894-f88b-3b6f-90bb-dc0881b017cb | -3.00555 | -45.38444 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba6e9d8e-bbbd-3b16-89f9-5bc99955de4f | -10.05281 | -43.86016 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8484122f-b1b9-3a6a-af6d-9b8c0e4f8848 | -11.46085 | -44.18224 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcb5be3e-8466-3d7e-a305-da52d71641b0 | -5.7486 | -40.77154 | 2025-10-16 03:47:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f0c4b716-fbcf-3226-8c2d-ee962dbc8cf3 | -10.82051 | -44.01806 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfeda582-f81a-3b3b-b164-328bbb4dc2df | -10.69827 | -44.43566 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7cf760db-01ab-31d6-82f7-3949c359b3a9 | -10.834 | -43.99342 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a09d58b-d08c-3faa-b091-6df11581741a | -11.47215 | -47.6425 | 2025-10-16 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdfb5fff-6e71-353d-8340-40fca7b81bae | -6.57749 | -42.97461 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5d87a38-ec2d-396a-b6e1-8d3fb6c3df88 | -6.1738 | -43.43666 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84557b63-3db3-3761-aaa1-e0b3af7cd744 | -6.05948 | -44.52813 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e9f20a6-44a5-36cf-a676-0ad233b4c5a6 | -11.58643 | -44.08854 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 08138070-d753-3d2d-a74d-658a070a941b | -5.44464 | -41.00366 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cb206706-99f8-3c37-8f63-a37663ec706e | -10.66362 | -45.28862 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78b00ab6-d58e-3b48-bec9-7e3aadf68c14 | -4.6597 | -44.10636 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c206c50b-26e4-31e9-945d-1e05c012cc89 | -6.73306 | -38.26105 | 2025-10-16 03:47:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 41ee0155-6fd1-3953-803c-63349da3a6b3 | -10.8213 | -44.01368 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4739ce32-b5de-3220-8807-82e0528d0200 | -10.61076 | -42.31647 | 2025-10-16 03:47:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 66cad239-8d59-34f4-a956-702a07f9a1ba | -11.91101 | -43.06329 | 2025-10-16 03:47:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c3812fe3-9de6-3481-81ca-6bc1c3de286a | -4.11109 | -48.02282 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 4480d0cc-81fd-3934-bb2e-6701c6e6494c | -10.05416 | -43.84996 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e43e7f3-b180-3645-91cd-dad8aa414f6f | -5.8767 | -43.88118 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f02171b6-b559-3584-9e6b-60d78939fb62 | -5.7418 | -44.98743 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58c7a23b-4347-3c08-8c6a-2cf7e5ed5544 | -5.86561 | -43.88894 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 963dbd22-1548-3669-8c31-0f0365827e55 | -4.93736 | -41.71393 | 2025-10-16 03:47:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3ef487e5-2cbf-363b-aed6-3371743412de | -2.79623 | -48.94164 | 2025-10-16 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ca31f18-1342-3c92-8794-56196ccb33d7 | -4.91473 | -41.55362 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 58cedb66-1df6-385d-a54e-c80347f0e47e | -3.84839 | -41.58733 | 2025-10-16 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cd1a74ce-f578-3364-aadb-9513153a46f9 | -5.86644 | -43.88409 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfe04a7d-9294-3f3e-a649-29155f3105e3 | -4.38203 | -43.39598 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| f63a75f3-9a88-3977-b91f-b838d5850381 | -4.49907 | -45.39807 | 2025-10-16 03:47:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f869ed0-f91c-3b57-a81e-e3b8668dcdb9 | -4.37907 | -43.38509 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 10c1321c-fe5d-3d5c-89ef-cb7d2ad0e130 | -6.19166 | -44.1099 | 2025-10-16 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d32b6374-28c0-372b-ac13-29902ca69793 | -4.39698 | -43.39338 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 78fd323f-54db-3cf7-b9ff-60126dc6d306 | -4.37982 | -43.39897 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 25e2e1d9-47c1-3818-ad22-383c6833d358 | -11.43407 | -44.1547 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad0b5e42-53e8-364e-bb3d-4090eede8bbd | -5.43139 | -40.98968 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3e361d67-8a6b-313d-bbad-59aa6e4056da | -4.09642 | -48.03147 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 4bed7af0-adb9-3500-9391-ad2bfcd97621 | -6.04619 | -41.89989 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 63449b8c-ffb8-3630-9dd4-2ce3f7aec960 | -5.2636 | -37.6288 | 2025-10-16 03:47:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| da891081-8e35-3822-8bea-3af1030f9fae | -11.45646 | -44.18143 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1467bf3f-aab9-3540-a810-9b6bf47bdf0c | -4.82056 | -46.84003 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f11978ad-e0f7-3a9f-8857-92c4564ef2eb | -4.67139 | -44.09686 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab949d3d-acce-3ab7-8241-48d14e8215d0 | -9.71465 | -44.50275 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 267e4521-019a-37d7-b1c4-b00a9f2e8fb3 | -5.41 | -40.89878 | 2025-10-16 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 291828de-d713-3aab-9970-1915bc833731 | -6.04562 | -41.94214 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 805cb05f-f8eb-3bd1-a2f7-5611fd291ef3 | -4.76323 | -40.87197 | 2025-10-16 03:47:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dd48b698-6367-385c-856a-942c971371d4 | -5.73962 | -44.98535 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47169f07-6026-3097-90ad-01d4c358257c | -9.08582 | -47.95431 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d6a40b1d-038b-3dea-9cb2-a7cbeb4f7eb8 | -6.16362 | -40.91249 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 5a5d2830-10d3-3b89-a8e2-29a4d11c9c43 | -5.33787 | -42.56168 | 2025-10-16 03:47:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13b02501-18f2-367c-8046-86a65945f674 | -12.49825 | -43.10262 | 2025-10-16 03:47:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README24.md)
