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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba41a836-1085-3d73-a44b-0044f765468a | -13.5405 | -43.0077 | 2025-09-21 01:30:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 2c67517f-491b-3a76-acbf-d6fdf8657eb3 | -7.9256 | -44.0937 | 2025-09-21 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |
| a007519e-36a1-38f6-a34e-e2a59e69b78e | -11.4857 | -43.5692 | 2025-09-21 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 8682bd40-635d-371e-9d51-2b379505fc55 | -5.5243 | -43.8647 | 2025-09-21 01:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 699a6725-b0d2-3564-b327-38d183f66cb8 | -13.5405 | -43.0077 | 2025-09-21 01:40:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 80.5 |
| aa7d55d5-7c68-3170-b878-d07ea3ce76a6 | -7.9256 | -44.0937 | 2025-09-21 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 5bfb5e8e-7ac5-3c67-bf76-ff1d1a654f2d | -15.9586 | -59.4288 | 2025-09-21 01:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1758aaca-fd43-33ac-9bbc-718f0ba43663 | -19.743 | -49.6543 | 2025-09-21 01:40:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.0 |
| e301f8a0-0a43-321d-8579-b17a46efbc08 | -7.9253 | -44.1169 | 2025-09-21 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 550bf65f-210f-37d3-b940-820604da5a07 | -11.4862 | -43.5456 | 2025-09-21 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| f5dd4be2-2577-384e-9de9-224e9d012ebd | -23.1523 | -47.6245 | 2025-09-21 01:40:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.9 |
| edcba4f5-f567-3bb4-8fa4-0cbda64d5377 | -9.4289 | -44.7113 | 2025-09-21 01:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7640fcbe-bffa-378c-bfbd-27f7fa57f1e9 | -7.9442 | -44.115 | 2025-09-21 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| bde32b91-ca70-3337-8711-61cf5659021a | -7.9445 | -44.0918 | 2025-09-21 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 5d460611-968a-3156-bb15-4935053c02b9 | -7.9256 | -44.0937 | 2025-09-21 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 433ef7fd-d7a5-38f9-9e8c-f8b584678d64 | -13.5405 | -43.0077 | 2025-09-21 01:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 874a5ed0-1ebe-3809-9cce-a3e101ff757b | -5.5243 | -43.8647 | 2025-09-21 01:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| c0f0ae9e-d5c9-3983-82f4-0f945605700c | -7.9445 | -44.0918 | 2025-09-21 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 7765b050-ebee-3e70-93e7-b516343ce716 | -15.9586 | -59.4288 | 2025-09-21 01:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 2000e2f5-bd21-3b06-9e91-61b0a9788065 | -9.4289 | -44.7113 | 2025-09-21 01:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5041c1ad-c942-34a2-a016-dfa6651e62fa | -7.9253 | -44.1169 | 2025-09-21 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| cf8af5f4-e490-33be-9698-7ba01f315da0 | -11.2499 | -49.8341 | 2025-09-21 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 877a91a7-0f4d-3f55-9b86-aa403c5032d9 | -11.4857 | -43.5692 | 2025-09-21 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 554dd1ba-43be-3bca-b660-cdbee426c689 | -7.9253 | -44.1169 | 2025-09-21 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b1aa260e-64f7-311c-a64b-7455e009e85b | -9.4289 | -44.7113 | 2025-09-21 02:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c3dc5e2b-5087-3145-952b-640b5efc1253 | -19.743 | -49.6543 | 2025-09-21 02:00:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 220.5 |
| a2315624-5fbb-38f3-a8ac-740e043d39ad | -5.5243 | -43.8647 | 2025-09-21 02:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| e60b1652-24bf-3672-b6dc-2693a63600f3 | -13.5405 | -43.0077 | 2025-09-21 02:00:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 3bbff719-daee-3af6-bb20-683b0d1f1149 | -7.9256 | -44.0937 | 2025-09-21 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| d7c9d1fa-de1b-35a4-ba6f-e272bc8925ea | -7.9445 | -44.0918 | 2025-09-21 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ade4b139-697a-3441-9a58-fb70320f24bc | -19.7633 | -49.6501 | 2025-09-21 02:00:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.2 |
| de0dc978-6887-3c00-a4e4-311ea75fd991 | -19.7424 | -49.677 | 2025-09-21 02:00:00 | GOES-19 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 14856cb8-ef7f-3114-a75e-28ad013c3994 | -15.9586 | -59.4288 | 2025-09-21 02:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| ceaa1925-054e-3991-aef8-716dcfc3bf66 | -13.5405 | -43.0077 | 2025-09-21 02:10:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 18b58ecd-aee6-3738-bf1e-7b4e9edc02a5 | -7.9253 | -44.1169 | 2025-09-21 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 56211bbc-48dd-3f23-a6f6-101bac51184d | -3.8043 | -44.0843 | 2025-09-21 02:10:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 60788334-f000-37ed-9881-d244c2fa6725 | -15.9586 | -59.4288 | 2025-09-21 02:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 074036ee-94e9-351a-a368-480958b89e3a | -19.743 | -49.6543 | 2025-09-21 02:10:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.9 |
| 14313685-645f-3409-8bf8-291fd86800cb | -9.4289 | -44.7113 | 2025-09-21 02:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| ff6414c0-e2cf-3ee8-8a2a-d34c77578385 | -15.9589 | -59.4087 | 2025-09-21 02:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 59918976-781c-3089-86b6-e0b93c28dd8f | -11.4857 | -43.5692 | 2025-09-21 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 4838304f-3142-3161-87c6-d16e37fb780f | -7.9256 | -44.0937 | 2025-09-21 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 71fa4375-9511-36a2-9157-8d65d14ed1fc | -11.505 | -43.5663 | 2025-09-21 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 67261dee-5588-3074-9ebd-a794d154f3f3 | -15.978 | -59.4269 | 2025-09-21 02:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 1e9dce4a-2c40-3e03-b066-eb01605dd43e | -11.6183 | -50.6075 | 2025-09-21 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 2a976848-3f69-3764-baf7-76f8a688260d | -11.4862 | -43.5456 | 2025-09-21 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 5f889c86-925e-3ea5-a712-7fe160d83464 | -7.9445 | -44.0918 | 2025-09-21 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 70c71b4a-3270-3d41-b678-c1f2ea3b0681 | -11.6186 | -50.5861 | 2025-09-21 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| c2d4c114-3018-323d-9e8d-c5769642cfcb | -5.5243 | -43.8647 | 2025-09-21 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| d6fd0773-d9d1-33e9-bd13-9daac8b4fe0a | -11.5045 | -43.59 | 2025-09-21 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 0ba57752-6519-3a3f-9eb8-c821a50728e3 | -11.4853 | -43.5929 | 2025-09-21 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 1e1820c2-7aed-31ad-b4ed-1e194e3687a4 | -13.541 | -42.9835 | 2025-09-21 02:20:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 04a1495b-6198-3c3a-9567-6dc961bb839e | -15.9586 | -59.4288 | 2025-09-21 02:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| cf4ea712-9b75-37dc-85f9-09292e7ee913 | -7.9253 | -44.1169 | 2025-09-21 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 1c46e068-071f-3bca-9e75-7053d75c1ba0 | -11.4857 | -43.5692 | 2025-09-21 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 75a5ecd2-06ae-3a63-a6a5-84c275d1ea2b | -9.4289 | -44.7113 | 2025-09-21 02:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| d614ce1d-5ddb-3dd9-b389-9a410e12a84e | -11.5237 | -43.587 | 2025-09-21 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 53233e9c-5052-3c4f-8d49-f4a96831d2e2 | -5.5243 | -43.8647 | 2025-09-21 02:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| d36c8a9c-7b53-31b7-ae00-73fb09070131 | -11.5045 | -43.59 | 2025-09-21 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 33d26fb0-cece-34d9-b575-553f872e7e16 | -13.5405 | -43.0077 | 2025-09-21 02:20:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 23572677-c908-398f-b6e6-a4538ef25df8 | -7.9256 | -44.0937 | 2025-09-21 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 188e6f30-de0e-3d86-b8df-a735159a1c9b | -11.505 | -43.5663 | 2025-09-21 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 037fb8fc-25ea-3ed0-a79c-0d7bff984899 | -7.9445 | -44.0918 | 2025-09-21 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c465359d-f8ac-3f11-b2f5-5d38111c98fa | -9.165 | -44.6273 | 2025-09-21 02:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| acb85307-15f8-374a-82cf-bce504aa01c1 | -11.4853 | -43.5929 | 2025-09-21 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| ba8e729f-ba0c-3012-8651-bf8f2486e1c3 | -19.743 | -49.6543 | 2025-09-21 02:20:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.6 |
| 46a9f291-97e6-3819-a586-156d1bb4c9a1 | -11.6183 | -50.6075 | 2025-09-21 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 908f6362-c537-31e9-8d0d-cdeb3b29acca | -11.6186 | -50.5861 | 2025-09-21 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 058ce786-1ded-348b-b85f-5b7942c175c9 | -11.6377 | -50.5839 | 2025-09-21 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 932cfd4e-c130-366c-9bad-a735c1f13e6c | -13.5405 | -43.0077 | 2025-09-21 02:30:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 852dc921-7a0f-3e23-9d0a-fe2211f2c7a9 | -7.9445 | -44.0918 | 2025-09-21 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 21ca7fee-dddc-3e57-aaff-ff9f5086d1de | -5.5243 | -43.8647 | 2025-09-21 02:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 86d19154-37c3-3d61-889f-38e4db9860c5 | -7.9253 | -44.1169 | 2025-09-21 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| fbacbb3b-d8ab-3f81-9b65-0e53cd1fa261 | -7.7328 | -44.4593 | 2025-09-21 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ed01e947-303d-3ef6-b7d7-2451c8104bf8 | -7.9256 | -44.0937 | 2025-09-21 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 30765a57-8192-3af6-b06b-e6b6fa126bc2 | -19.743 | -49.6543 | 2025-09-21 02:30:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.1 |
| 98cb7dfc-e3d8-339b-baed-ab1857ea3f80 | -6.0959 | -40.9996 | 2025-09-21 02:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 8d009915-6915-3f79-8d30-310072495f69 | -11.6183 | -50.6075 | 2025-09-21 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 01a6e4e7-07c9-3283-b199-73da52b011bf | -7.714 | -44.4612 | 2025-09-21 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 14c6ec27-bcd0-3b2f-80bc-13b3925c02f8 | -8.9872 | -65.4566 | 2025-09-21 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 04fcd31f-6bfa-366b-8667-1c89f717f377 | -11.5996 | -50.5882 | 2025-09-21 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 878b5256-ff0d-376f-a012-5c0a90cb85fa | -9.4289 | -44.7113 | 2025-09-21 02:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2556b9bf-e37e-30b6-b60b-fad080caf66c | -7.7328 | -44.4593 | 2025-09-21 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 165.2 |
| a86c9890-cf14-3443-9107-391be69d138c | -13.541 | -42.9835 | 2025-09-21 02:40:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 51e824bc-e8b6-3b9f-9b4f-a4abff3c6f88 | -11.5045 | -43.59 | 2025-09-21 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 39b54776-5faf-3587-86ed-f4cf0cab6afa | -7.9445 | -44.0918 | 2025-09-21 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 1086b62d-e274-3a8e-975e-c5ee7a8c4146 | -9.4289 | -44.7113 | 2025-09-21 02:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 4de92142-3f05-3e5d-8da5-c6aad0e1b144 | -11.6186 | -50.5861 | 2025-09-21 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 6dd90907-3742-3551-98bd-d329a8f8fae1 | -6.0959 | -40.9996 | 2025-09-21 02:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 1401155b-91ec-3960-aed0-cfe981435153 | -13.5405 | -43.0077 | 2025-09-21 02:40:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 114.7 |
| c3cbb20a-a055-37c6-bd39-c0fa24120a0f | -7.714 | -44.4612 | 2025-09-21 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 9dd55a6f-e4ce-3116-954d-077cc4be3c59 | -5.5243 | -43.8647 | 2025-09-21 02:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 98a8d5b0-8cbc-3afe-b101-8258f15e4815 | -7.9256 | -44.0937 | 2025-09-21 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| da2475bf-98f2-30c5-b35f-bae85a0da1fc | -11.6183 | -50.6075 | 2025-09-21 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 4abb14c0-fe5e-38a1-ac12-40186c839da2 | -7.714 | -44.4612 | 2025-09-21 02:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 34ef6f8d-e04b-3855-9027-bfc6d109518f | -7.9445 | -44.0918 | 2025-09-21 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c56b6e53-c9b9-3d7a-af0c-09a8e253f186 | -7.9256 | -44.0937 | 2025-09-21 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 828c6bc8-2438-3cf9-8ae0-3e1be46e1311 | -13.5405 | -43.0077 | 2025-09-21 02:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 136.3 |
| 0809c2f4-faca-34a1-ae5c-fae0922b5826 | -11.6186 | -50.5861 | 2025-09-21 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| baac73c4-c8f2-3ea9-957b-5c7863b4f925 | -7.7328 | -44.4593 | 2025-09-21 02:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |


[Clique aqui para ver as próximas entradas](README4.md)
