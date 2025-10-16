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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dfbb584-d62f-3947-8266-12517978c2bc | -13.4412 | -47.9483 | 2025-10-16 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| f999d39b-00dd-3491-9318-e4c592a9bb00 | -9.2505 | -45.2821 | 2025-10-16 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 68b426bf-c978-3506-9293-6f36f8ac208e | -11.5921 | -44.0472 | 2025-10-16 14:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| cf830e92-5700-3c0c-8618-5e2af6357b24 | -6.4255 | -41.8865 | 2025-10-16 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| d98e0e84-8ff4-3a31-b13c-6b440067436f | -10.514 | -43.3815 | 2025-10-16 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 4a52e4e3-2fc5-3f22-892c-178fa9f5eba5 | 2.0782 | -55.7592 | 2025-10-16 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| d8c5073d-d627-3e1e-9359-457fca9e682a | -12.2941 | -49.9904 | 2025-10-16 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 41049d40-5199-3f61-9acf-eeb4d76b8385 | -12.284 | -47.1544 | 2025-10-16 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| ed98d6e4-0346-3f43-846e-527822475978 | -5.4561 | -41.0054 | 2025-10-16 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 501dbb73-f271-3e1c-bc13-ea339a78926e | -12.2648 | -47.1571 | 2025-10-16 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 47724161-7a0c-3820-9f68-b3b4b6280bcc | -10.5331 | -43.3788 | 2025-10-16 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 2eaff577-3c72-3dee-a895-60f992f97cf0 | -11.3599 | -45.2877 | 2025-10-16 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 590bf26d-0118-31d1-a896-15c46fd5f013 | 1.8585 | -55.6834 | 2025-10-16 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 220d51e4-faff-3428-9413-712c1471c0aa | -6.3733 | -41.4828 | 2025-10-16 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 328.6 |
| ad665f2b-0a19-3394-b8eb-2f05cdf8ed61 | -12.3112 | -45.6311 | 2025-10-16 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 45d32177-472a-3f13-9dff-9e846b9fdd87 | -11.5724 | -44.0736 | 2025-10-16 14:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 353c16f8-3d8e-3088-96e0-2eb42d550cf2 | -10.8289 | -43.9482 | 2025-10-16 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| a224c520-ec08-3d6d-894f-16ea00675b25 | -12.9179 | -47.1078 | 2025-10-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 49832d68-9f60-3409-a169-89dadca2a86f | -9.2508 | -45.2592 | 2025-10-16 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| f58d8376-94c5-3c37-a9a4-3f5297219c70 | -6.3544 | -41.4846 | 2025-10-16 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 229.3 |
| 80975c67-1c42-3416-83d0-c5ccd0d29c5e | -6.1447 | -41.7438 | 2025-10-16 14:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 89c03d88-c9e0-390f-be67-d93d737fd186 | -14.1749 | -47.9477 | 2025-10-16 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 66f4e4ec-b57e-3a0a-b73b-b7f9500925df | -10.1143 | -44.557 | 2025-10-16 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 339.5 |
| caf770af-94c4-3149-8993-0da49799ce52 | -14.2428 | -51.6079 | 2025-10-16 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 7d9de284-a24d-3839-8e15-6fec63251e34 | -12.9909 | -47.3217 | 2025-10-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 79f084a7-c8dd-3b67-a58a-be723d24ecf7 | -5.4762 | -42.9367 | 2025-10-16 14:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 216.6 |
| f9a68ef8-413d-302d-a937-60cfebf52c3a | -10.1333 | -44.5545 | 2025-10-16 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 254.7 |
| c62b57e1-cca2-3072-8bdb-3319deba519b | -10.6021 | -47.44 | 2025-10-16 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| d646635c-70e4-370f-aa3f-39157d5ed15b | -13.055 | -46.9746 | 2025-10-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c8edd351-8670-3070-a11b-6708aa7fb570 | -12.7059 | -50.5208 | 2025-10-16 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 43686ff1-57d8-3752-8604-b2d937dfc2e5 | -10.6539 | -45.3151 | 2025-10-16 14:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0bc4ff78-b240-3565-a84c-65705876ce41 | -9.7162 | -44.5149 | 2025-10-16 14:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 78b557ce-ffad-37ee-80ee-ace22a8747f5 | -5.476 | -42.9602 | 2025-10-16 14:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| aaae4ea4-62b2-3064-bf5c-c74bcd4aa762 | -12.9565 | -47.102 | 2025-10-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 91eca13f-a140-39f2-8e61-3bfb2e87709b | -12.2844 | -47.1319 | 2025-10-16 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 099d452f-ca78-33ce-8497-62cd70fd5a48 | 1.8402 | -55.7034 | 2025-10-16 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 52bf8bf1-fa16-3db7-b6c9-4dc7a69ec55a | -10.4949 | -43.3842 | 2025-10-16 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 21d5d6bd-765a-3aed-99b5-26697b422fc3 | -5.4558 | -41.0297 | 2025-10-16 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 211.6 |
| 8477d394-9f3e-3da8-ba45-a1f819d6a977 | -12.3876 | -40.7519 | 2025-10-16 14:10:00 | GOES-19 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 56788f12-0300-305d-b7e8-3f814334bea7 | -11.3603 | -45.2646 | 2025-10-16 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 3fc6fee1-e85f-369b-baa4-c7e495e2941c | -15.3269 | -45.0439 | 2025-10-16 14:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 1595f3aa-a8c6-3d90-856a-80ac671844bc | -6.3542 | -41.5087 | 2025-10-16 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 170.1 |
| 99d48197-eaf2-30a2-b0fa-27d2429a33b6 | -9.3596 | -46.9813 | 2025-10-16 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 9138d536-8f27-3ab9-86be-f562b2d7afb0 | -9.3599 | -46.959 | 2025-10-16 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| f0a10491-cf2f-322b-a78c-c66c9abbf763 | -9.2694 | -45.2799 | 2025-10-16 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 252.4 |
| fb9dd937-8487-323f-bff3-4308cffc65f7 | -10.8293 | -43.9248 | 2025-10-16 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| ec7c0b68-e932-3428-965a-99cb68417e46 | -4.3874 | -43.3827 | 2025-10-16 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 242.3 |
| 38d18050-d102-3370-b1cc-018a81d792da | -12.4866 | -45.4895 | 2025-10-16 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 1c5b9520-cef5-3486-8e05-ecfd15cd6bf2 | -11.4589 | -43.9969 | 2025-10-16 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 0464fff8-272a-3f4d-8c61-e1ed1ae517d2 | -12.2655 | -47.1121 | 2025-10-16 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| ce4474e1-5ad8-3417-952d-1fa167a161f1 | -9.3413 | -46.9388 | 2025-10-16 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ce9b2486-f46c-3d84-b440-8db22d1b2cea | -13.2535 | -43.752 | 2025-10-16 14:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1c07b2f8-b5d0-3fc1-8b18-5a2794ffdaa3 | -11.907 | -46.8251 | 2025-10-16 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 4556717f-e0ec-33fe-ae27-e2e8b75e5957 | -12.6871 | -50.5017 | 2025-10-16 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c1f49eae-a879-30b3-ae56-fbaa385b0226 | -12.2441 | -42.1048 | 2025-10-16 14:10:00 | GOES-19 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 70532f6a-24e5-3237-8f40-1c4932de240a | -6.373 | -41.507 | 2025-10-16 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 208.7 |
| b03e26e8-198c-3019-bd51-acf8a8f45ca3 | -11.7027 | -44.2879 | 2025-10-16 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 78639a98-75ac-395b-a3bb-654a1d1a57dc | -10.673 | -45.3125 | 2025-10-16 14:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| ffd8d98d-900a-3601-9eb7-a68022b7d053 | -4.3687 | -43.3838 | 2025-10-16 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 03e15f90-e0ea-3ded-8de2-728bf32b778f | -13.0743 | -46.9717 | 2025-10-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 4a8b8039-e776-3940-8921-ca34a517f4e2 | -12.941 | -47.9545 | 2025-10-16 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 0c8824e8-8ce9-356f-ab2e-0de3aaa8b264 | -3.7628 | -41.6967 | 2025-10-16 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 5ba2ccd1-3f84-3c70-8157-73a716aae330 | -10.5144 | -43.3579 | 2025-10-16 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.6 |
| cee73720-5047-373d-b579-a4963984eb8d | -12.2652 | -47.1346 | 2025-10-16 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 4fbad7b2-0bb7-3a15-8cb3-1fc3d4b94217 | -10.5834 | -47.42 | 2025-10-16 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| e36bb4cc-6638-3d81-b79f-fb8c40ac210d | -9.2258 | -48.5782 | 2025-10-16 14:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| b5af0023-8d89-3c5a-8ccf-230c123a5127 | -11.9073 | -46.8026 | 2025-10-16 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 667b974b-e256-32d4-8ab5-9f331fa100bf | 1.7851 | -55.7436 | 2025-10-16 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 06c2f588-9bdd-3066-89ee-4c5a322eee4e | -12.9905 | -47.3442 | 2025-10-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a65e3abd-226f-3a90-843a-d200c153358d | -6.4129 | -43.0958 | 2025-10-16 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 91af8d3f-8673-32b7-84c7-797d40e260df | -12.9716 | -47.3245 | 2025-10-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 288d57c5-ef56-3ce4-8420-30d009b82d28 | -12.941 | -47.9545 | 2025-10-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 14bb80ca-db8a-3292-b569-fc1f6d19e69e | -1.3932 | -49.0174 | 2025-10-16 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d1bd9b43-6773-3a49-9e5b-449e10d0e257 | -13.2535 | -43.752 | 2025-10-16 14:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 25ba4774-4de2-34cf-97b0-994db93cbf6b | -11.438 | -44.0938 | 2025-10-16 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| ad9af38b-c67f-3b35-8bdd-656ca003247c | -13.2918 | -43.7689 | 2025-10-16 14:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 5fb338d6-d88f-3aad-b3aa-cfdf33a68d18 | -10.1143 | -44.557 | 2025-10-16 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 398.2 |
| e4f2e984-ca8a-3482-a299-54f4a9b4e2d5 | -4.0886 | -43.3764 | 2025-10-16 14:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 67e84884-7628-3e87-a21d-e36479425c29 | -10.7756 | -47.2634 | 2025-10-16 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 825507f4-b5e8-3179-a325-6f4ff737f2da | -11.1215 | -45.8463 | 2025-10-16 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3db9f1f7-b224-3132-a952-ce46655158b0 | -11.5917 | -44.0707 | 2025-10-16 14:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 333.8 |
| 99c7b8d5-920b-3519-b26c-ab5fe8138459 | -11.1403 | -45.8665 | 2025-10-16 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 29624f42-44f7-3c6b-bb62-65ce439cdc59 | -10.5331 | -43.3788 | 2025-10-16 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 46b3b889-770e-3067-8b93-988c7f0d3eaa | -11.4384 | -44.0703 | 2025-10-16 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 15f90e39-5aca-3305-8a9d-5e52ca82c716 | -5.4561 | -41.0054 | 2025-10-16 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 150.6 |
| 05bf6354-2753-3dbf-9ee3-7e895bccb6c6 | 2.0782 | -55.7789 | 2025-10-16 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 96ca9c90-83bf-371f-b983-36d81d962d45 | 1.8585 | -55.6834 | 2025-10-16 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| e8f9a735-cf27-392f-8856-51000c5b3b4d | -9.2508 | -45.2592 | 2025-10-16 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 588f1216-ceb6-33e7-a108-98d086349c7a | -6.3542 | -41.5087 | 2025-10-16 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 187.7 |
| 06db5e4a-206c-3a28-ad71-7490574cfcbd | -12.246 | -47.1373 | 2025-10-16 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 895364ac-25ee-3b62-a4ef-3eadce5e8dc2 | -4.1338 | -42.2 | 2025-10-16 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 90013c92-0c7b-31e2-92fd-eca204e2c31c | -9.2505 | -45.2821 | 2025-10-16 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| f0d5213d-138b-3a3d-b7b8-8250421fbe27 | -5.6819 | -45.112 | 2025-10-16 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| c5bc5c99-a046-390b-8829-09a9d5e624a2 | -10.1333 | -44.5545 | 2025-10-16 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 287.9 |
| af714686-f9ef-3ff7-80e3-4c75e30033a5 | -9.2694 | -45.2799 | 2025-10-16 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 153.9 |
| a9f7898c-eed1-3558-ac7e-5ad1f569c416 | -4.1149 | -42.2248 | 2025-10-16 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 174.7 |
| 1dcf0052-627a-3ea0-a101-186e67f5f2d7 | -13.4609 | -47.923 | 2025-10-16 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 666560fe-265d-3068-bf13-e36ccc840271 | 1.8034 | -55.7434 | 2025-10-16 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 7267ff38-5312-3ef9-a10e-00fe70b4aa40 | -9.3788 | -46.957 | 2025-10-16 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 3212009d-248f-3893-abec-9e8aa647586e | -11.4393 | -44.0233 | 2025-10-16 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |


[Clique aqui para ver as próximas entradas](README94.md)
