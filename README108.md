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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e64129d-117c-36b1-96b6-44c7342a51e1 | -16.59927 | -58.21866 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| abfe7f45-a9dc-3e32-b899-8a23dd2e0ce8 | -16.5981 | -58.21527 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 26a95a06-52e8-34a6-874a-ff06f560e092 | -16.57201 | -58.21671 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dd7fd0f8-9d21-332c-a7a8-1b7dca815e8e | -16.56211 | -58.21098 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7d5ca340-89bb-3cf0-bd57-1b988b1d3f6b | -16.5614 | -58.21445 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f40d3970-ef64-3a6a-b0fb-de1b3e7ad58a | -16.5607 | -58.2179 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 611b85b2-1a27-36f2-8ad4-4f57a6a921a0 | -16.55752 | -58.20639 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| ffb6c93d-1399-3ff2-93b1-cddc1966a12a | -16.55681 | -58.20983 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 394cc1ea-998b-36f9-807b-c4e8d087ced7 | -16.55611 | -58.21327 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.3 |
| 17d68672-361e-3e64-9295-2cdf2944de16 | -16.5554 | -58.21671 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.3 |
| a75b1002-ae1d-3f81-ae18-359cf7d1ad54 | -16.55293 | -58.20177 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 0c84fb0a-8a07-38ea-8b3e-0bc0f3b6452c | -16.55223 | -58.20522 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| c7bff950-5d83-3a6f-8a69-736e95fe5be7 | -16.55153 | -58.20863 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| de7dcc95-3422-3e1b-bcc7-b60f08e75c17 | -16.55082 | -58.21205 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.3 |
| 92340184-7368-315b-aa7e-19fff545c9eb | -16.54694 | -58.204 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 117a415a-5d26-3ac5-9fad-5bb84928895c | -16.54624 | -58.20741 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 08378417-3154-39c6-8dbb-f4942fa21f6f | -16.54412 | -58.21772 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7505baf1-8b77-32c2-9232-bbe9fc95ee24 | -16.54166 | -58.20277 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4571ed35-7ac9-32de-9550-d20718f1d8c0 | -16.53955 | -58.21303 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 08b36ed6-f30a-38fb-9453-385a95c1fd76 | -16.6025 | -58.2301 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 667473e7-802e-346b-8f8c-847a94f21e57 | -16.59046 | -58.23487 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b4a57c2b-97c0-34a7-88e2-33bfbcf12815 | -16.58974 | -58.23842 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ff5d19f0-5e57-3ee2-9c0f-6ca0b9b7dfd3 | -16.58903 | -58.24197 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| f709485e-8583-3f70-9aef-b82935a1b31c | -16.5877 | -58.23842 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| c7f6b098-e2f9-3a84-a5bc-bb421e16f0a5 | -16.58696 | -58.24196 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 940e72bf-3167-35bd-ac85-6026e084c77c | -16.58657 | -58.22675 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 363625c9-2e86-3342-a418-533ea5042a7a | -16.58586 | -58.23025 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0903d3d4-0a4f-3503-aee7-7cb588f3c19e | -16.58514 | -58.23379 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 331e9f8c-e580-3201-83b0-2275c0ef8c35 | -16.58123 | -58.22577 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5c647898-1a51-3720-8ff5-97a87aba2330 | -16.58053 | -58.22926 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9e702621-acd6-3bc3-82f9-c13b3eb7576f | -16.57982 | -58.23275 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6120a16d-224a-3d14-881f-32fff418e59b | -16.57662 | -58.22126 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5cd14bc5-cfe6-38d1-9260-2e5639462c3a | -16.57591 | -58.22471 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 57e1a6c6-85e9-336f-922b-831972f9e5f0 | -16.57521 | -58.22818 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| bddd2672-2d91-3552-8695-2e32b21da590 | -16.5745 | -58.23164 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ba5d10ee-290d-3ed1-a837-44eae3962769 | -16.5738 | -58.23511 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ae559972-0a7a-31d8-a662-690c6dcb8309 | -16.57131 | -58.22015 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 610afc80-82b7-3763-8ca2-259d776f9e79 | -16.5706 | -58.22361 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ad53d147-9c0b-3c80-92d4-26a686198283 | -16.57059 | -58.27813 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 09368e66-5b8b-3a42-b0e5-5eae185b1afa | -16.5699 | -58.22706 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 79a63b28-e6d5-3462-a060-c0fca834ec5c | -16.56919 | -58.23052 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 148d2dcf-cb5d-3a63-ba21-4f3b0e259f40 | -16.56849 | -58.23399 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| fef35704-bb6a-37ac-9523-5926af4d27ab | -16.56778 | -58.23746 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 1070f307-c72f-3da4-a24e-a6a55ca749bb | -16.56529 | -58.22249 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 1ab9bb4b-4156-3d3e-b5f8-b2661d37e054 | -16.56459 | -58.22595 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 551b18cf-04d3-3b45-94c7-92574a6e86b3 | -16.56388 | -58.22941 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 11b2ba84-eec8-34fe-a204-9f3804d998e8 | -22.24905 | -43.89836 | 2024-10-03 04:32:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6953252b-93e9-39df-bdd3-730bab9c7b84 | -22.2871 | -42.48006 | 2024-10-03 04:32:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c3191cd3-3149-3209-8c65-7d1dc43ea04f | -22.28664 | -42.47672 | 2024-10-03 04:32:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bd0529db-2622-3b21-85eb-372e9b626249 | -22.2865 | -42.48535 | 2024-10-03 04:32:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2bc8b46e-c812-3545-bcdd-34c5cbd61bf2 | -22.28609 | -42.48198 | 2024-10-03 04:32:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c0399d37-fa0c-3c5d-98ed-496d7416e14b | -22.28553 | -42.48726 | 2024-10-03 04:32:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4238b3f2-b581-3dd7-bae5-9e7361c084f4 | -22.16338 | -42.54176 | 2024-10-03 04:32:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0690ebe8-2e3c-308d-93a2-32c7b4d79584 | -22.16333 | -42.54581 | 2024-10-03 04:32:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| fc4daae8-5473-3aa2-8fdf-e2ff0ed8b550 | -22.16284 | -42.54681 | 2024-10-03 04:32:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ca7e61b6-5481-30dd-a7c5-882c833397ad | -22.15931 | -42.5401 | 2024-10-03 04:32:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 501d24ea-5a29-3987-ba31-5556a76546e3 | -22.15879 | -42.54103 | 2024-10-03 04:32:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0993e0d7-17b0-3854-9d9b-ac064714f15f | -22.15416 | -42.54435 | 2024-10-03 04:32:00 | NOAA-21 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6ebac570-96a0-3f5d-bbb5-3fc3abc91dba | -22.15362 | -42.54918 | 2024-10-03 04:32:00 | NOAA-21 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 04c46b68-6dae-3ac6-8818-c966c783be01 | -22.05975 | -42.97314 | 2024-10-03 04:32:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c8ce8ff2-adda-3ea7-9818-7d150676a3be | -22.05533 | -42.97205 | 2024-10-03 04:32:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d4dfc447-e790-33c0-a4a6-679742979e14 | -22.78446 | -43.75831 | 2024-10-03 04:32:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7a7c46e9-7c6e-3bcd-82b5-8061985334a5 | -22.76308 | -43.76751 | 2024-10-03 04:32:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c0460eec-8462-36bc-b530-e2b316abe06c | -22.64591 | -43.70333 | 2024-10-03 04:32:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9a579f7d-c893-3b68-bd16-d5d39fbf5e80 | -22.19531 | -45.04419 | 2024-10-03 04:32:00 | NOAA-21 | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bea160ea-0df2-33d3-9c59-964bcdbda445 | -22.18748 | -45.04287 | 2024-10-03 04:32:00 | NOAA-21 | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 98eea869-2728-3ccd-a017-6e41f5463f5c | -22.18724 | -45.0437 | 2024-10-03 04:32:00 | NOAA-21 | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 05a04ec4-b89c-3843-9bf3-94ee443a7866 | -22.12126 | -45.09276 | 2024-10-03 04:32:00 | NOAA-21 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 92634c1d-0c4e-33ba-84d5-9e35865f9242 | -22.11733 | -45.09232 | 2024-10-03 04:32:00 | NOAA-21 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| fc2a99a7-de59-3365-b34f-40b29d7800ff | -22.0076 | -44.50357 | 2024-10-03 04:32:00 | NOAA-21 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d704a7e0-980a-3941-aecc-c2e598c7a1f9 | -22.00361 | -44.50256 | 2024-10-03 04:32:00 | NOAA-21 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 708be043-02b6-34e3-bb31-536b928f8823 | -22.31565 | -44.06699 | 2024-10-03 04:32:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 705190dc-6986-3a99-a940-b5111415a13e | -22.31519 | -44.07097 | 2024-10-03 04:32:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3bdade44-fd2f-3d95-bdc9-ad9c078e1e91 | -22.31402 | -44.06888 | 2024-10-03 04:32:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d4c0f3b3-56de-3171-8a81-05246557f1b3 | -22.30714 | -44.05569 | 2024-10-03 04:32:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 49d7ee6c-6426-3891-a8ae-d3e67344cc57 | -22.30667 | -44.05952 | 2024-10-03 04:32:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4504e1b0-7cca-306a-8d91-9a98d59b9b72 | -22.30207 | -44.06242 | 2024-10-03 04:32:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3ef6f105-0f40-3986-b9e4-8e185050b19a | -22.30158 | -44.06639 | 2024-10-03 04:32:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 90cbf2b0-f4cc-3fa1-9873-710093da8570 | -22.30109 | -44.07045 | 2024-10-03 04:32:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0a87d794-06d0-3cd5-b47a-de0f94c7b93f | -22.29745 | -44.06548 | 2024-10-03 04:32:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f881e097-5e95-3149-a4fc-16a76ac42041 | -22.29694 | -44.06967 | 2024-10-03 04:32:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5b1fadb4-69fd-36a3-a8d6-2e5a71c7ea60 | -22.12172 | -44.10537 | 2024-10-03 04:32:00 | NOAA-21 | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d3e9f724-6c0d-352e-9d23-7b334fdd2160 | -22.54945 | -45.36728 | 2024-10-03 04:32:00 | NOAA-21 | WENCESLAU BRAZ | MINAS GERAIS | Brasil | 3172202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 42a1d28e-a643-3b71-bc8e-c007d20ed34f | -22.41241 | -45.12708 | 2024-10-03 04:32:00 | NOAA-21 | VIRGÍNIA | MINAS GERAIS | Brasil | 3171709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fce3dd5c-fa6f-3818-904b-7af65cad1a7c | -22.94855 | -45.14487 | 2024-10-03 04:32:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 54415de3-583c-322d-8c70-2da5722f0485 | -22.76987 | -44.66705 | 2024-10-03 04:32:00 | NOAA-21 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| bbaddd8b-5f85-3f5b-98cb-29dbd7895a31 | -22.73589 | -44.90575 | 2024-10-03 04:32:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| fc1a8a79-1eef-3123-b2c9-bb599dfb4f6d | -22.73432 | -44.82076 | 2024-10-03 04:32:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c466c32-1f02-39ee-be5e-e4e2a151ab91 | -22.73332 | -44.89382 | 2024-10-03 04:32:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7a921476-3f81-3cbd-8486-1d7881bbfbfb | -22.62588 | -44.66035 | 2024-10-03 04:32:00 | NOAA-21 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8cdb9a11-a1d9-3499-b7ff-6ca4fadb04e1 | -22.6218 | -44.66003 | 2024-10-03 04:32:00 | NOAA-21 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0308be22-52c2-33de-b15a-d446979b9192 | -22.53725 | -44.83645 | 2024-10-03 04:32:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b8d06d03-2d28-3484-9295-7f3765183ea5 | -22.53679 | -44.84016 | 2024-10-03 04:32:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0e0a2660-6fb5-3c28-8351-0ba71e6d68a3 | -22.53325 | -44.83598 | 2024-10-03 04:32:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3d82465f-6d08-3730-a546-17e43c43479d | -22.53278 | -44.83965 | 2024-10-03 04:32:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 305bedb1-df13-3815-8b3a-b309a779c34b | -22.5282 | -44.84373 | 2024-10-03 04:32:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8a95e609-67b9-3df1-b512-43fbdeb2c1d8 | -22.62053 | -44.16673 | 2024-10-03 04:32:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 18eb63c3-00fe-3f25-ba7a-db5f84bbb3d4 | -21.94148 | -46.03362 | 2024-10-03 04:32:00 | NOAA-21 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 95bdf11c-1254-363b-9a9e-eb6a96fda55f | -21.93778 | -46.03307 | 2024-10-03 04:32:00 | NOAA-21 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 83b77069-d106-3ea3-9407-679e7c8d8019 | -21.71449 | -45.71393 | 2024-10-03 04:32:00 | NOAA-21 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README109.md)
