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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d82b96d8-3411-343c-9fbe-b53da89f5ad6 | -7.87503 | -44.87022 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d198692e-cf0e-3375-b28d-79e71564dab6 | -6.29911 | -47.63123 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 88170827-38ce-367e-bc85-19c83e30d6d7 | -9.70807 | -45.87225 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c95c52b-32a5-3e39-9196-435504babab7 | -12.16097 | -47.03751 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ef3ecee1-4f3f-322f-8a9b-4f97bab603f9 | -7.43398 | -44.73472 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a797b540-e0a6-38d1-a609-4a8bd676710e | -8.50582 | -47.43622 | 2026-09-20 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 981417c5-257d-326b-b6af-42f25a684095 | -6.5143 | -46.78362 | 2026-09-20 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5436a161-9b7d-3463-90a4-6f40234d4980 | -9.78907 | -45.05414 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 411703c8-32ce-3a6b-ae2f-8ba827e2883f | -11.23696 | -48.37968 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 26d3994c-f242-31a6-a42b-94640e101b19 | -9.26455 | -46.21257 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 26c2fb9f-1aea-3a09-af7f-6ebdc6f21f87 | -11.85602 | -47.66658 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 82305f66-e97b-3878-9f9d-8c7b203cbfd0 | -6.92659 | -42.90824 | 2026-09-20 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 71f0cc30-7037-35a0-a5f9-acc825597b17 | -11.85343 | -46.8743 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 91693368-8607-3338-8fcb-c0f58c380851 | -6.30082 | -47.62247 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1be6548e-c3f3-30d2-9030-c004455de43f | -10.1305 | -45.55566 | 2026-09-20 03:45:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b808a606-0136-39b3-b3c6-f9141ac40ddd | -6.32593 | -47.63076 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 7fd12b34-8734-3034-9673-43c015bc5a4d | -12.75939 | -46.12349 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ab6d9c0-af24-363a-9810-3c7329ca24d9 | -10.13846 | -45.56074 | 2026-09-20 03:45:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff0a3beb-9bd9-3fcc-b13c-5271d5a074df | -9.71926 | -47.26365 | 2026-09-20 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f91e8d88-ea72-3fc8-8bfc-96930413ee62 | -6.91886 | -42.89653 | 2026-09-20 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 18267389-d5ac-383e-a7b9-24d5bd5d7bb2 | -12.11606 | -47.01348 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acd9e3dd-42d1-3d74-948e-44bee787534c | -9.12164 | -45.71877 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd9985fb-9620-321a-9d66-c0bac12cdf35 | -7.36251 | -44.86947 | 2026-09-20 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e5d0c4ba-5ff5-39d8-b501-f4f49d5e7023 | -6.207 | -47.36432 | 2026-09-20 03:45:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bebde988-6e02-31dc-a4ee-b132c8f8ea6c | -9.79908 | -48.32183 | 2026-09-20 03:45:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2f43c6e8-8ba2-382a-857b-36327544b23e | -11.23799 | -48.3746 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 525bfbed-429f-3b33-8b95-9b0b1fe5ffa9 | -10.60703 | -46.52967 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fcbe4695-c7f1-3cf4-9687-c137dae5ac56 | -10.30702 | -50.25504 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 9e9ab05b-f1f3-34a5-ae64-ff8aadfcba93 | -7.62404 | -45.45034 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1aaaf9b8-cfcd-39b8-807d-a492b57b2027 | -6.30009 | -47.62581 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| edc79218-7405-3c3b-9092-bfb127241fe7 | -9.04971 | -48.72037 | 2026-09-20 03:45:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 226d757b-1a37-34ff-b687-b1eb523b4e2b | -7.02339 | -45.25189 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 1af5cf5c-3ae6-3df5-831d-f24760984f20 | -7.0887 | -42.08272 | 2026-09-20 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03aefe58-4a91-3187-9917-6856efe54b5c | -11.665 | -43.41581 | 2026-09-20 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b865af49-8a3a-3462-b239-dd39d4f9e5f8 | -13.03588 | -46.9129 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8eafaae9-41b7-3714-a9e7-e2379d68794e | -11.09007 | -48.29519 | 2026-09-20 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8bdab20c-42ca-39a9-b185-f0602203889d | -9.26598 | -46.20476 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac70a012-2563-376a-9853-3e2cf85d1e95 | -7.96967 | -44.06788 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bff92d3-9d63-3272-82cd-eaa3cb39790a | -6.1767 | -47.49449 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cad21f1f-2120-34db-a7a8-ef850d66d6db | -7.36134 | -44.87622 | 2026-09-20 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 02ee4eb7-ab70-35f0-8960-898aef7ef7a9 | -11.85788 | -46.86703 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7ab899cf-91bc-3b84-a613-e5e342c4ad3e | -7.86247 | -44.84859 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d373a2a-5de4-3b9f-8425-157aecc088f8 | -13.03515 | -46.9165 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e6868a50-1d10-3e18-948b-760b12fba227 | -9.26527 | -46.20863 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2ae4e926-7b20-39f3-9444-15f8426d14fa | -12.15453 | -47.04031 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 27135417-5d1e-3cfb-991e-60f0290e6388 | -10.29671 | -50.32202 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3dc8ad67-0e8f-33fd-b4d0-c7688d3e3f91 | -10.77689 | -46.33199 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10db6b21-17b2-335f-ae88-07394ae98fd7 | -6.32026 | -47.62576 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 39249d16-b079-3c01-b7d7-b2c4ebd9e92f | -10.29389 | -50.29942 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 914ca539-e578-3490-be11-ef53f8579e88 | -9.73044 | -47.26999 | 2026-09-20 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43db1388-d1dc-3e77-ad7f-c2f62457a090 | -6.6492 | -43.63115 | 2026-09-20 03:45:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e33435e-de84-3549-9dd7-a9bf11c6fd22 | -7.55651 | -45.44809 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbfcc5f4-549c-37d7-a68a-c4616fc75b40 | -13.02418 | -46.91711 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a29eff98-cb11-3471-b26c-f997c6e3b251 | -13.02615 | -46.90694 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7faff100-e184-3c71-8c24-e74db9ed92c2 | -7.77363 | -44.83195 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f83c86bc-60cd-3585-872a-b7e7c03e38b1 | -7.52941 | -45.43991 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 9dca4e7e-deb9-3a00-a61a-845ed75e0210 | -10.29684 | -50.30394 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9502af6b-34b3-3c23-b379-40a2ba3b2778 | -6.45101 | -44.57628 | 2026-09-20 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cb2c14d-4d53-3690-ad64-1d88e0234032 | -9.03048 | -48.72511 | 2026-09-20 03:45:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb6cabb1-31bd-37fb-a82d-6af3631ebcf6 | -6.46816 | -48.43966 | 2026-09-20 03:45:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a06aa06d-588a-34bc-b5da-e37ae8b5d33a | -7.74664 | -46.76616 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02408b48-cce9-39f9-9227-590a0c8d2306 | -7.57686 | -44.89818 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4097fc78-c216-366a-8f00-da6b1889d583 | -9.71424 | -45.86958 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a87fc293-d122-3e1b-9e68-6b5cd35a4a0e | -6.91533 | -44.90786 | 2026-09-20 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7cea84a-e2b0-311c-b604-3fb0abc5f98b | -9.73069 | -46.08974 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f014ef86-d125-3719-a3ba-fe983ae172e2 | -6.31377 | -47.62471 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 64f1dd3b-cf42-3a26-b3a8-b22dfee24449 | -12.28848 | -47.11877 | 2026-09-20 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b55e9def-8729-3ed9-a69e-6e725d670dd5 | -13.02571 | -46.90631 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 150dce6e-0ca7-3dc4-bf15-a5009fdb01e7 | -7.54866 | -45.42808 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3ea1ba58-0ae0-33fb-8b43-6fe837746241 | -10.19391 | -44.14935 | 2026-09-20 03:45:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dffaa7f2-6048-3307-8baa-9584e0f53ed1 | -11.87469 | -47.66539 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 86999900-4612-3292-a432-ccf7688e1ecf | -10.29851 | -50.26059 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 4e1ba649-6d37-3742-8069-a3c535c4f98e | -6.77454 | -48.65937 | 2026-09-20 03:45:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d385123d-8a68-3a77-bc1f-cf6429f15920 | -8.76627 | -48.66177 | 2026-09-20 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2d1e80c1-5da4-365a-b32c-6d881ab24718 | -12.13076 | -47.02853 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cbcd3985-f4d8-374d-8531-3de5fecf1a9d | -6.30556 | -47.63251 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 38e30621-0787-35da-a2c0-ce4cfffabada | -11.48443 | -47.77949 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d388ac73-df58-3d15-a618-f44904e48a6a | -6.47529 | -43.91866 | 2026-09-20 03:45:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eedcab61-b364-3814-85f4-66c1b91075cd | -13.01944 | -46.91192 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bab1876-eed0-31fe-9029-9eae0501c984 | -11.45172 | -45.3804 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcb9b637-0f2c-38d9-8714-0fee59caa5b5 | -11.45802 | -45.4039 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98a4f2ae-081c-3064-a409-e71646464c24 | -9.72851 | -47.26717 | 2026-09-20 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 988ddcca-d307-3c26-ade6-2cc7a39ddd9c | -9.23681 | -46.23618 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a08a947-a733-3735-9551-cf79d9dec57c | -11.86021 | -47.67646 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 75a75d6f-aaae-3d7a-afaa-454c20040f08 | -11.77477 | -47.43735 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ecbc5611-2482-308f-97d6-d17c17715882 | -7.8809 | -44.86796 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b7c3afd-5c31-3837-9459-5c97d311de7c | -9.26666 | -46.20105 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5faf7b01-6bca-3339-8e0a-60c52bf8e367 | -6.75538 | -47.91823 | 2026-09-20 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1d32f4ea-ab60-3a98-a7aa-fed14c7a232b | -11.28763 | -41.99533 | 2026-09-20 03:45:00 | NOAA-21 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 45b4eaca-1a3f-3767-9521-6b45e1f3c21b | -11.65966 | -43.41959 | 2026-09-20 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1bc52c3e-dd05-3ddd-bb62-371ff5465df2 | -11.4557 | -45.70554 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 690afbb1-2f8d-3c00-9bb0-10257b3a1f8b | -10.30412 | -50.26899 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 62acb8e1-1bd8-34d3-9d89-8e86044133a1 | -7.30905 | -42.26833 | 2026-09-20 03:45:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5c1a43f9-7a56-3b8e-9f33-7a6213ce06fd | -7.62793 | -45.4288 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11a10df3-edb6-3ec5-b82d-508d4ecde9b8 | -11.44443 | -45.33391 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db4455e3-6843-3105-b7eb-8a28001b95b0 | -10.5622 | -46.56549 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fcaf3d8-a257-3c0c-9691-1b1f2d0bb77a | -12.15508 | -47.02412 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f239b4ab-4689-3da1-ac19-d411fdef1e23 | -7.16088 | -47.42877 | 2026-09-20 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ecff9ba8-fb6c-3e6b-8728-7936071c4100 | -7.75515 | -49.20438 | 2026-09-20 03:45:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 65479498-40b0-311d-8b8c-0981af1716a6 | -13.02348 | -46.9207 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README14.md)
