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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ac003c9-5186-3593-9dd5-e9d53b7702fe | -11.33656 | -43.59525 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 079a276f-3847-3880-a163-34cd795601ab | -11.87246 | -46.45454 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98084f9c-865d-3ea2-8f0f-fe2ed9a1a6bc | -9.49885 | -37.96298 | 2025-08-30 03:30:00 | NOAA-20 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 52f191cd-390e-3ecc-aa22-dd513a543763 | -11.32848 | -43.60641 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03c3477e-99ce-3d64-9911-3af0a60cb4b6 | -9.67939 | -45.97769 | 2025-08-30 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b30a3a7-34ad-3584-8b23-8ea83d3c2d2c | -8.04818 | -45.4184 | 2025-08-30 03:30:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b50ce612-d8f4-3d10-aafb-3331d2aa1606 | -7.19985 | -43.70618 | 2025-08-30 03:30:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b061627-4053-3c9d-a314-09022f6103a6 | -11.7722 | -47.56592 | 2025-08-30 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 073e1056-0262-31fc-810c-4b92e471480f | -11.33501 | -43.60326 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1672aa4-30c2-3406-8c43-254f5a4acb28 | -11.8462 | -46.40026 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f94f461-8f24-303c-b561-1866b732beda | -11.31082 | -43.63628 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3b19f4f-5368-35eb-972f-7a3090344668 | -10.0246 | -46.03476 | 2025-08-30 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c9794e89-7009-357d-a838-b211e48411d6 | -11.84987 | -46.38251 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 091d5c87-3539-3114-a72c-27878f77a6e3 | -11.88527 | -46.39392 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fea600e9-cad5-3e4d-a98d-472a01b956ce | -11.32068 | -43.64663 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 166baa64-f793-31d7-8312-c186e2da5012 | -11.85995 | -46.40117 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aca5fde7-4826-31bf-b7c1-8c599430d1b3 | -10.99611 | -46.95135 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73fa7ef0-35d7-3262-a4d0-206cfbcd4904 | -12.00971 | -43.98793 | 2025-08-30 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| f211638c-0137-384b-bfcc-3875ea34349d | -7.11344 | -44.60463 | 2025-08-30 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7096b11f-44f1-3d96-a373-4c371d565144 | -11.08284 | -45.13669 | 2025-08-30 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82e3b98f-6ee6-3c24-9142-61467a6605bd | -10.72517 | -47.01403 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 575c2382-0a19-35a0-a4d2-2d9efdb45c63 | -11.86311 | -46.43275 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be1a72ef-8c0d-3756-b9e8-d758d39b0c1a | -8.44367 | -43.65081 | 2025-08-30 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 595cb62b-382b-38a4-a403-63a797734256 | -11.30768 | -43.47136 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c098fc2-1b86-3bf0-87a1-9fad9b07be97 | -7.61181 | -42.73437 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9927e4bc-ac0f-3c08-8eba-48d0906b6383 | -13.43025 | -46.94702 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66b5efc2-511d-38b2-a144-73df2855ed57 | -13.67286 | -46.88462 | 2025-08-30 03:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8609e6db-0e07-30ce-8ad2-b9c8dedc9b3a | -14.25329 | -45.24561 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbecac2e-ec13-36cb-9f4b-7d11ed1b9b3d | -14.00244 | -44.5634 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b42f99f0-5fcd-3150-a92d-1d0472d22b8d | -13.39873 | -46.96302 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cf98e2ce-d2a6-392f-9e1a-742e6edb1789 | -13.99729 | -44.58921 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 16e2fbfb-476c-35e5-8167-df67871d512a | -14.00738 | -44.56878 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df4562ba-7706-32fb-ae41-5ad367c07886 | -13.36894 | -47.02641 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| df0b205b-a72d-3765-9e92-884c851f6f2b | -13.36367 | -47.02718 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 9cd5abf4-219b-3a6a-86af-eea7e87dcf36 | -13.36758 | -47.03285 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0486ea60-ffcc-3512-b12f-bb9630a33e04 | -13.38287 | -46.97135 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 599dfbe5-99a8-3e25-b986-b121db2e62c4 | -13.37483 | -46.97599 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d07a33d-4bde-3806-bbe1-8dda70f08176 | -13.48713 | -46.84422 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72346540-c07f-36d9-90a9-7c5558048297 | -13.96443 | -46.33677 | 2025-08-30 03:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5ec4028-e238-3da6-9caf-ac6aa3ad2043 | -13.36938 | -46.99099 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cd696c63-a5d3-39dd-a77e-80d617a81066 | -12.94095 | -46.14531 | 2025-08-30 03:32:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d69cc845-54f1-3719-b80b-297a0d05d58e | -15.72017 | -42.60057 | 2025-08-30 03:32:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 98ac1c09-1766-3d96-b306-1bacae932c48 | -14.00075 | -44.57187 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2891f323-89d4-39c0-8fa3-6d9d82deeaae | -13.36366 | -47.01803 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d6253fee-3af0-32cb-812f-e91458c4e6a3 | -13.46838 | -46.9654 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33b6f1fd-5a96-393b-84ba-377265709124 | -13.37625 | -46.96947 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfde139c-851e-3b38-a17b-0ad25774aca7 | -13.37965 | -47.009 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 75d1d365-3f40-332e-b93e-9db16abd3cbd | -14.00178 | -44.56574 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f1a156b-e682-3f13-a739-a08a584ca6be | -13.67388 | -46.87988 | 2025-08-30 03:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6963aa0f-db99-3165-9fa2-0fe9efebf014 | -19.1482 | -40.48538 | 2025-08-30 03:32:00 | NOAA-20 | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| aa46451a-7317-3a67-8d29-65a31389b9f0 | -14.25423 | -45.24105 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 46144e2f-8de5-3c74-a7ab-b5501a6d9d88 | -17.69652 | -47.28233 | 2025-08-30 03:32:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69208b01-f917-3154-9f5e-6b267980a135 | -13.38932 | -46.99645 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c0bbae9-7119-3c5e-9d69-9c02bbdb181a | -13.99989 | -44.5762 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f51241e8-0613-339a-909c-9f2c87283f8b | -14.04001 | -44.526 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb885fbf-b153-3da2-a3c0-7453cd5773c0 | -13.59891 | -46.88956 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0288e4a7-941b-30f9-912f-4880d38cdfbd | -14.00567 | -44.57735 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1f84bb41-f920-34d3-8e12-31f47e6d4fa8 | -13.37072 | -46.98463 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4908eed8-46f0-3d89-994b-499d820dc85d | -14.00329 | -44.55917 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b67d1a1-10fc-369b-813a-cfe920a150a3 | -15.30749 | -46.09577 | 2025-08-30 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f6fab5d-4d0a-3235-9956-67e2035ab493 | -13.36925 | -47.00161 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9ab94864-7f46-30cb-ade9-c06f34145c61 | -13.37164 | -47.02296 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e3da551e-8d8a-3287-9aeb-824fe3f6394e | -13.9941 | -44.57507 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 590eea96-1b57-384a-89a3-4e101eea90c1 | -13.45809 | -46.94788 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 156dfc91-f0a9-3cc8-97a7-6025ad5e3dcd | -14.00797 | -44.59406 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9716c57a-9ffc-3808-a8b7-ca23f7251413 | -18.92497 | -47.06894 | 2025-08-30 03:32:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cbcfa17-c713-35a8-8436-d070b58ad7ec | -13.40774 | -46.95383 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1093fa3a-14fa-3de0-b046-195e18f8d090 | -14.00491 | -44.57972 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b905daee-c8ae-39c7-85b4-74ccb5f8cdd3 | -14.00002 | -44.57426 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6b003548-321e-3d40-823c-9b8c2d8d2265 | -13.56056 | -46.93856 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0341b670-b0ea-38ad-a512-227eebb221ca | -15.17319 | -48.03227 | 2025-08-30 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ed9be89-d540-3c96-b2c8-a9c31bce69af | -13.99732 | -44.58727 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ad2c38f5-3879-39c4-8471-4a01f6f3e8af | -14.00653 | -44.57303 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4b655c0-bd9a-311f-9351-41ff2761e31f | -13.9739 | -46.32693 | 2025-08-30 03:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2fb2fe9b-930b-3b42-a302-b627b00c49e3 | -13.59476 | -46.89154 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 15a48cca-6f3d-3518-9789-c8d80c1c0bb2 | -13.99334 | -44.57743 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 640d2b61-3b87-36ff-9cfd-d5e137bf24ac | -13.36013 | -46.86938 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 513010b2-0726-3a33-ac04-8e49e841908b | -15.30862 | -46.09053 | 2025-08-30 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3b39ddf-d862-3e55-9c9d-4b12416030f3 | -13.388 | -46.96931 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9dd8667c-1e06-396d-9e05-19e1b3e9abbc | -13.59088 | -46.89457 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1717bea-5e0f-3a71-a709-a88a2b8db169 | -13.38112 | -47.002 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8e30141a-bca9-384b-ba2d-fc7001ab9213 | -17.70292 | -47.28344 | 2025-08-30 03:32:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02d37892-3c70-36b8-892f-03e5bd4f75af | -15.07231 | -48.16578 | 2025-08-30 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe377fb7-28e9-3a08-bd55-0b93d1ae1aec | -14.00049 | -44.60107 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d7d561c3-ea55-35f8-9299-cc20a8f5296f | -15.07897 | -48.6314 | 2025-08-30 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ccceb14-821e-3711-902f-37de1fe3d6eb | -13.39442 | -47.00569 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2215b4d3-a2b3-37bf-83ac-e759c4993133 | -16.98455 | -49.3029 | 2025-08-30 03:32:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0592a6eb-9e51-36e1-9bf3-67f329beca69 | -17.90985 | -46.84213 | 2025-08-30 03:32:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca7e25ca-edd6-3d2f-81b7-29131b26c3ee | -13.195 | -45.29295 | 2025-08-30 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec509794-9493-375c-99c2-6939a1165bbf | -13.63021 | -48.18371 | 2025-08-30 03:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8bb410e8-a10b-3aa5-b47b-825984d949c5 | -13.56472 | -46.9191 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ef581117-1d94-320f-b6be-ffff6a17b312 | -14.0022 | -44.59477 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| c13e3683-5cae-3578-9cb8-192d67b9180b | -17.91591 | -46.84394 | 2025-08-30 03:32:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23a4d44f-8c2b-3d5e-9f69-26a52caeda0f | -13.38112 | -47.01181 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c60a29d8-fefc-3d35-b350-eefae7181179 | -14.0409 | -44.49246 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93139d9d-deb3-31c1-8cd9-19f990013863 | -13.37299 | -47.00722 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aea8466e-21ce-3a5f-8684-7ff91e381391 | -13.19192 | -45.27719 | 2025-08-30 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f66074c-64c4-3e9d-9c18-1d2a7c3837bf | -12.92217 | -46.36375 | 2025-08-30 03:32:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff47bffe-c89f-3471-bf45-9aa4138685fc | -19.14852 | -40.48623 | 2025-08-30 03:32:00 | NOAA-20 | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4907e8a2-d357-3325-aa41-ca96d03b07cc | -13.41264 | -46.9521 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README15.md)
