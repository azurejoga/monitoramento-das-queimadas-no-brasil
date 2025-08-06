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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7086d5f-aa6e-3ed4-93af-a30cb9b1e2e9 | -7.77372 | -45.2094 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5ffb24a-40a8-3e27-8c65-72564de73ff9 | -8.38768 | -45.79598 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d08c754-d871-3bd3-b4be-1f7b36900d5e | -9.07263 | -45.04988 | 2025-08-06 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7312eee2-e76a-38a2-b7cd-f742b5026ef5 | -5.72332 | -49.09991 | 2025-08-06 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7945f3e0-b368-3fd9-8de5-a2c5be228830 | -8.84083 | -47.61683 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd76b9d1-cdd0-363e-90dc-f8de4d8a15a1 | -11.43365 | -45.12846 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb439e90-aa03-3d56-9866-3253d740cca9 | -7.51753 | -44.85322 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85d1413f-e911-32a8-b0a4-9af997149cd8 | -7.3866 | -44.62612 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2303803-ebdd-3852-bec3-fa6ad68e960f | -10.4754 | -44.34452 | 2025-08-06 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1fe21f3e-5939-3f62-95bf-44ed36de70e4 | -11.02954 | -45.06451 | 2025-08-06 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89af40cf-210e-3017-9207-2650bd85f463 | -12.3818 | -47.0393 | 2025-08-06 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 152d6a19-64e9-3c86-b8bf-745671061149 | -9.70754 | -51.95127 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e29c240-172e-3253-bab9-bac024dced18 | -11.73019 | -47.52122 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d77575c5-08ec-305a-87e2-cd1bb69d764b | -8.62448 | -50.0132 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87474db0-b36c-3113-a611-fdc0a3b15544 | -10.11788 | -51.67764 | 2025-08-06 04:19:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd0e911a-77b7-34f2-92d7-71a4acf5b08e | -11.51274 | -44.36428 | 2025-08-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 151f8d4b-d53f-353a-afe0-44163670a330 | -11.74255 | -45.01683 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87ff5416-4169-368e-a402-c4acfbd92a4b | -6.98798 | -42.09418 | 2025-08-06 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c8f12cda-2187-308f-905a-06a5b6d518a6 | -8.8361 | -47.62394 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aceb72e8-6865-339a-bdb0-b5df5b0679b0 | -6.67312 | -42.99316 | 2025-08-06 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48509772-5d5a-3380-a465-f590af5958b8 | -10.42955 | -44.37416 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9c49c8e-f674-3eb8-b26f-102cb08fee2a | -8.00529 | -43.23378 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ccd2b29f-41d4-317f-8caa-7f3c602e31af | -7.9138 | -45.52716 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5fa2f24-c0d9-3928-84ae-2ecf28498914 | -7.58459 | -45.31127 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6db66258-3268-3c6d-809b-e44ed9fabdfc | -6.41881 | -53.36544 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c85248a-3099-3696-a638-e8172a770aba | -8.00572 | -43.13835 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 39ce38d2-b2e3-3b6c-9bfc-d11c20089171 | -11.5133 | -44.3606 | 2025-08-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2701aa32-c37b-33b7-9c6f-258b8d1f47b9 | -10.44072 | -44.3686 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9c4fe8f4-b246-303b-98b9-51ef5e50dcdb | -6.78186 | -43.23872 | 2025-08-06 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8f58da85-0677-3bb9-8244-bb896a413176 | -12.5515 | -44.73834 | 2025-08-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa28936e-8d95-3895-880f-aeb4d3acb613 | -11.83909 | -43.72607 | 2025-08-06 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c8c4a19-8367-3e2f-893a-9f7d59a087a1 | -8.83736 | -47.61626 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5ca8dfc-8f98-3527-abfc-c0e2ab6e1606 | -7.70421 | -45.13445 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 270e3f86-aa6b-3dff-b6c4-75d1b9a9f73f | -11.42977 | -45.13147 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f0dabf5d-57b6-3a65-9f9d-4721344e8224 | -12.76062 | -44.41798 | 2025-08-06 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e4e3fa8f-e3c2-3948-88c5-3461900f66be | -7.6377 | -44.58412 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffd5b365-1127-3b3f-b7ee-b101a41bfd2d | -11.74031 | -45.00915 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e5df51d-a7f2-3b6b-97bc-a449fe02e272 | -11.91292 | -44.92592 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2216e67a-7559-3397-a255-470ad79599f7 | -11.4381 | -45.14368 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3b8a8343-5d51-3d37-9d8b-592129b08284 | -11.32674 | -47.30473 | 2025-08-06 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7152cb52-3fde-3375-b766-4fd829ca752d | -4.81947 | -47.31701 | 2025-08-06 04:19:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e48ffc95-ae7d-31f6-b527-517a3ca80215 | -9.46604 | -57.85157 | 2025-08-06 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cbcfd14-af00-346f-851f-ff2cd3c73c1f | -6.50475 | -45.86079 | 2025-08-06 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59de0e2a-ce64-3ed9-bf13-fd143f969041 | -9.5087 | -46.73014 | 2025-08-06 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36aeba27-b5be-3f16-a3c4-5cfb65307fc4 | -9.64818 | -43.84855 | 2025-08-06 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57887b39-0034-3e4f-abe5-681fa502da11 | -11.7296 | -47.52487 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1527acb5-1883-34cf-ac27-e6618cbda016 | -7.63824 | -44.58065 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b26bab3-7e57-31af-85e7-2ec5cb8f1bce | -8.00187 | -43.23325 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e8d029a9-3fec-3305-8545-db4bface272c | -7.38937 | -44.63012 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98ad0948-a9a6-3883-bfe7-41ec1e452fcc | -11.76468 | -44.9618 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c86f595e-4005-3b25-b971-b5307c072a5e | -10.4698 | -44.33615 | 2025-08-06 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed060fa2-86e6-386b-85e3-dcb1cd72f7bc | -7.99845 | -43.23272 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0b14817f-6fc1-3c13-9a06-edc246a653f1 | -6.78914 | -43.24361 | 2025-08-06 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ca98cd62-f2d0-30f5-bb28-0449a781d5b4 | -11.74644 | -45.01378 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d9b1eb5-e0d2-3f4a-a4f4-ab883a2a760a | -7.63216 | -44.57613 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 605ff215-c770-38a8-9e15-4708e810f089 | -11.75979 | -45.0159 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a419559-3428-31b0-b204-c5d8e414feb2 | -11.9051 | -44.95443 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5263a7a6-af7b-3681-ba02-a4fe3593515a | -7.37993 | -44.25748 | 2025-08-06 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa7f787c-6894-35e0-b440-1f6c69340694 | -6.41262 | -53.37061 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac9c9054-56fa-327e-b095-081049c39bb0 | -11.75257 | -45.01841 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b25ee6c-7788-3fb3-88be-7765e66c0286 | -11.62595 | -47.71216 | 2025-08-06 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87edc2dc-a587-33e0-9d96-c07ad0e88f21 | -7.30115 | -44.67311 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53a85880-a900-365b-ad43-4c57a4881e28 | -8.75411 | -46.41785 | 2025-08-06 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ae3a512-8756-352b-bf6a-8f701a780689 | -7.82398 | -45.08633 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfbb76fa-ca87-3deb-99dd-2478bc03e964 | -6.91608 | -43.68294 | 2025-08-06 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3e0b955-84f0-3f74-963d-75f63b99cfac | -7.46527 | -41.12034 | 2025-08-06 04:19:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6493b515-cf8c-3787-8714-52ad7a931c30 | -9.07153 | -45.05688 | 2025-08-06 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddef6b81-97af-3cb2-8136-b2bf70d348e0 | -8.51528 | -43.31019 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4fb6e90b-1ad3-3a87-81d3-ee63baf9d4a8 | -10.47604 | -44.38527 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4226d850-9644-3d3d-b2aa-e302cc73d0a4 | -7.65291 | -46.59084 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c408c5d-9efe-3c8e-acbb-485646fc2c81 | -10.43456 | -44.36391 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d01dc8ee-7a26-3416-a6ce-cd8ad4ef8caa | -11.91736 | -44.94157 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95afbbb4-f5fb-3fee-b39b-2b4debd1dadd | -6.27302 | -45.26896 | 2025-08-06 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3fa5c62-99a8-319b-996c-065f93af315c | -8.39154 | -45.79305 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc0a9a32-0ef4-3501-ac5d-7142c304e522 | -11.75027 | -44.98879 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31236579-b7ba-30d4-9b8b-e25e68235124 | -11.90455 | -44.95802 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| da733527-159a-3e02-95af-b3580326f2f3 | -6.72167 | -43.58034 | 2025-08-06 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 742e7e2f-e3ab-3214-a57b-f18254429cd8 | -6.48343 | -45.54874 | 2025-08-06 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f12d990-da05-3b24-839a-edf509e93428 | -8.24582 | -45.06097 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70d40258-ef03-3683-98cd-aa21a6406011 | -12.66846 | -44.91015 | 2025-08-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ae3d095-2552-3cd4-a4b6-d68c2d1c7893 | -12.03745 | -44.0155 | 2025-08-06 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 217a8f61-f7f7-3ee7-9d86-2ae85b6304b7 | -7.38374 | -48.16997 | 2025-08-06 04:19:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 717ed104-3636-31f4-8908-04e351c5f70c | -11.4392 | -45.1366 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59955aa6-8167-3cfc-b0af-ca0de9dadea0 | -7.18437 | -45.47808 | 2025-08-06 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 814c9b86-ef25-345c-a840-165c4dd2b4ab | -6.68845 | -44.33543 | 2025-08-06 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0fde877-2cd2-3d6b-b3b7-32ede57bdb0c | -7.51313 | -44.85962 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db28e49f-655a-304d-870b-bb15fc5b53f9 | -6.41528 | -53.3694 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7efbadff-25d0-3223-b992-e951bb771a2e | -11.73674 | -47.54498 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c02fb45-af1d-3985-8111-cfc5eb5c9d65 | -6.68391 | -49.78601 | 2025-08-06 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d502bc8d-f625-3798-92fc-b3baa2e36033 | -8.06205 | -49.71977 | 2025-08-06 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eaf334e2-84b4-301c-b090-ddf7359b71e7 | -11.90236 | -44.97227 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2087557a-14e4-32d6-925c-f599803e4d26 | -7.35212 | -43.71756 | 2025-08-06 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9519857-2f38-3134-8729-d5749c14af0c | -6.26797 | -53.63397 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c75bb7b-6c8c-3493-980c-3e5bbceaf217 | -12.04089 | -44.01601 | 2025-08-06 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da8b0420-d315-3fe2-8025-c5e5b431d382 | -11.74699 | -45.01021 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7ca22cb-d7fc-327c-a4a3-ff43eaf066fc | -11.76411 | -47.53444 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2286284c-e24b-3e3d-8dfc-11e54abe5de1 | -11.50517 | -50.29084 | 2025-08-06 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 057e5c0b-c460-3a06-99f0-80cdf92277d3 | -10.43181 | -44.38187 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e50bea82-7ce5-3bde-be39-8c46b3d1e2b1 | -11.72622 | -47.52435 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a33ecfb-d08d-33bf-bd4e-0f77c76414c7 | -10.90211 | -48.37511 | 2025-08-06 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |


[Clique aqui para ver as próximas entradas](README16.md)
