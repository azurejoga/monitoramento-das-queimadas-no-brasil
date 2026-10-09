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

## Dados Diários - Página 247

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd77cdac-7bc9-36eb-b183-a6029a862971 | -5.4958 | -42.8413 | 2026-10-09 14:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 125.1 |
| 67b7f147-f4cc-3872-8960-0ea7b9c37aa9 | -8.9299 | -45.2269 | 2026-10-09 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 264.6 |
| 34e88e9e-e2c2-3536-a6a4-18e3780acdc9 | -12.193 | -44.7487 | 2026-10-09 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| a53419e8-02f3-3ffd-b0e5-71bc068360cc | -12.2145 | -44.6291 | 2026-10-09 14:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 114e1b1c-c5bb-3f98-b884-d52455c0ac82 | -6.3842 | -55.265 | 2026-10-09 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0fbb2d8f-019a-3827-bf73-6b9adbe0ea34 | -6.7365 | -55.1474 | 2026-10-09 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| a0a7bc97-c6f1-374c-8ed0-102edc3115b4 | -10.4724 | -47.2333 | 2026-10-09 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 314c5dbd-62c6-30ef-91d8-1ab9469c65db | -9.2781 | -47.4333 | 2026-10-09 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 461eece9-ce0b-3059-b1e7-7110807fc8fd | -8.9687 | -45.1542 | 2026-10-09 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 3feca052-5545-32ce-aa72-8a8662c967ba | -9.2973 | -47.4092 | 2026-10-09 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 93fbd335-4f42-33a7-b028-0abd059b9d67 | -1.1991 | -55.6909 | 2026-10-09 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f46909a6-abd7-3e0d-a7d4-751cd8cabdec | -1.5306 | -54.5359 | 2026-10-09 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| d7cba398-ccf4-38a0-938a-ad15beeb1aa3 | -10.5091 | -47.3179 | 2026-10-09 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 6830db37-40eb-3cb4-bd81-a9ce0506ffa1 | -1.5123 | -54.5361 | 2026-10-09 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 1aa6f5bc-ef69-3cbc-9892-42153eb36c3e | -6.7366 | -55.1274 | 2026-10-09 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| e0589fe4-97a5-3149-9e6f-a137b304d5f0 | -1.3933 | -48.9534 | 2026-10-09 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1b32392c-a293-3ddb-a02f-c2cde40c73a6 | -10.4914 | -47.231 | 2026-10-09 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 319.7 |
| f732322b-22a5-3740-a41e-026a45338000 | -1.3264 | -56.398 | 2026-10-09 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 33b4497e-375b-341a-b7be-18171b948720 | -6.9851 | -47.6858 | 2026-10-09 15:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 56706838-ddf5-3757-9753-9406f26daf6b | -2.3849 | -57.885 | 2026-10-09 15:00:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c2de33bb-110a-3f5b-9a1b-72c3adfee9a4 | -1.383 | -55.1944 | 2026-10-09 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 197.6 |
| bd3fe84d-30e0-361e-80e6-8dcd4e09928b | -10.9575 | -45.389 | 2026-10-09 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| d464a882-aa35-35ad-bff7-5527d5628299 | -14.3611 | -55.0114 | 2026-10-09 15:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 9afd09f9-3c46-3de7-8fb4-1482db0b6db9 | -6.6814 | -55.0903 | 2026-10-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b85cb715-e2d7-37c5-8d82-2fc4b5f1ac0a | -8.9753 | -47.5305 | 2026-10-09 15:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| ec9892f8-2bb5-3acc-a4b6-5db1e2aea438 | -9.0829 | -45.0957 | 2026-10-09 15:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| b628b3e8-11d3-34f3-869b-02e4101e57dc | -6.3665 | -55.1461 | 2026-10-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 307e2e7e-54dd-331e-a6c2-50effdbbce39 | -3.1285 | -54.1657 | 2026-10-09 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| ebe7ba2c-e789-31b5-a955-e93b98c87f21 | -6.0625 | -59.9088 | 2026-10-09 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| f34a61fa-323b-31e4-82fa-a3bb3a6e11ba | -6.7365 | -55.1474 | 2026-10-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| ff3635a0-3dcf-3230-a72e-551f0e7075e5 | -8.8899 | -45.3907 | 2026-10-09 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 7a5751c0-ddb5-39c4-848b-e8b1ce1bfa1f | -2.1544 | -54.4668 | 2026-10-09 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 4d94b5ac-7dfe-368f-a609-27043b5b613e | -1.4569 | -54.7761 | 2026-10-09 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 49bc2517-8195-3bb0-8379-ae3a06a6acf6 | -2.3481 | -57.9824 | 2026-10-09 15:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 004ee9cd-857d-31d8-b9ce-30097430f49e | -13.1644 | -54.2972 | 2026-10-09 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| df1a678c-67f6-3be2-86b2-57a18f12f07d | -12.2316 | -44.7427 | 2026-10-09 15:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 965e4d2e-859c-3db7-8c69-373fe80510a7 | -2.4623 | -56.0879 | 2026-10-09 15:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| a0871e33-3677-3728-81ea-19fd8c64ba1c | -13.1444 | -54.3612 | 2026-10-09 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 80d7d04d-c9db-349a-89ee-fefed202fe75 | -2.4623 | -56.0682 | 2026-10-09 15:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 70323b9c-77b2-3bf1-931b-7b33906b5978 | -11.318 | -46.6573 | 2026-10-09 15:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 3d081f23-caca-37c2-86d7-5893f7e0dcb7 | -6.4413 | -55.0224 | 2026-10-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 09534997-5c92-3175-8a66-1217bd69d1e3 | -1.5306 | -54.5359 | 2026-10-09 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c9e90169-f45e-37d6-b687-7c6fae5f4b0b | -1.3829 | -55.2142 | 2026-10-09 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| f160d050-6efd-35f1-bcb3-07656a310cd4 | 3.968 | -60.9004 | 2026-10-09 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 2bd07d95-7f37-3319-8516-9462e77af7cb | -3.6044 | -54.6936 | 2026-10-09 15:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 65419b43-b721-385b-8604-bd023dd7dfc4 | -14.3608 | -55.032 | 2026-10-09 15:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ce550792-ff7a-3e13-b324-2c1bff4975e0 | -2.9817 | -54.1091 | 2026-10-09 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 9baf0183-1e8b-3d00-bd71-2e8be4fa6273 | -3.5677 | -54.6746 | 2026-10-09 15:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 172fb5b3-503a-3b9d-b87c-27b0b25ed7d2 | -15.2535 | -42.3741 | 2026-10-09 15:00:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 514.4 |
| 191eb21c-289a-3b11-b764-e6252ae41f44 | -2.5492 | -58.0373 | 2026-10-09 15:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3ab36303-a370-33d6-b7b3-8d6efa8424be | 0.543 | -50.899 | 2026-10-09 15:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a4291ffa-66d3-3cee-a3b3-29f89baa38a0 | -11.0758 | -44.0299 | 2026-10-09 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 287.3 |
| d908128f-6294-3e7b-9e73-07b44c936682 | -13.1641 | -54.3178 | 2026-10-09 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 654f9422-bd49-33a0-b0a4-06e3128f6f31 | -3.0926 | -53.9254 | 2026-10-09 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| dbcd6d87-ed3e-31c9-b63b-6da89a6b7ba1 | -1.4569 | -54.7562 | 2026-10-09 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 205f0db1-9616-3ea6-83b7-d9f45382e51a | -9.1015 | -45.1164 | 2026-10-09 15:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 177.8 |
| af630f53-6ebd-369e-856a-44b1a74c51b5 | -6.3842 | -55.265 | 2026-10-09 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| daf18ce9-0d4d-37c7-bda3-ea6e268b7c26 | 3.6212 | -60.6989 | 2026-10-09 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| ccac4150-0ac6-3fcf-ab20-383a13ba0e22 | -11.2849 | -45.2063 | 2026-10-09 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| a3204844-242c-37ba-8539-b7eed5470ea2 | -2.1361 | -54.4671 | 2026-10-09 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4651accf-31ef-3f14-abf0-6598429140c5 | -1.4118 | -48.9318 | 2026-10-09 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 342af4d8-2f56-3c20-a159-35a6b36d8e66 | -1.1094 | -54.1802 | 2026-10-09 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3571b476-399c-38e4-a135-8b2c06ec2c03 | -12.0448 | -43.434 | 2026-10-09 15:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| c799cabc-006d-3bb7-a6fd-961dae099776 | -8.6551 | -54.5291 | 2026-10-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ec3d668f-031d-361c-8a08-94b9ae82ed63 | -6.0423 | -42.5859 | 2026-10-09 15:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| 803d2335-6bda-3ec2-b5b2-77a6fdc26987 | -14.3415 | -55.0341 | 2026-10-09 15:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 0b97145a-164c-3c07-8189-da6cc9027a9e | -5.4958 | -42.8413 | 2026-10-09 15:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| c0b9ee5a-b256-33b6-ae64-7603ae53693e | -9.0826 | -45.1186 | 2026-10-09 15:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| fb6a5211-5d2c-384b-a68f-2c58ab7b1e93 | -5.7315 | -41.7069 | 2026-10-09 15:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 7831661e-3944-3ee3-b52c-86832a6f853d | -11.0566 | -44.0327 | 2026-10-09 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 523.1 |
| 7481e112-052c-3bd2-90f1-801e79918275 | -5.5127 | -43.0512 | 2026-10-09 15:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 190.3 |
| f6c9dfbc-ba55-3974-bfe1-1c8060d0e1e1 | -11.8783 | -47.3892 | 2026-10-09 15:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 602.2 |
| 974d1d6b-9613-35e0-b7a1-8f55fc167ad5 | -12.1922 | -44.7953 | 2026-10-09 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 9313a8cd-105f-30a3-90da-e4f9d677c7b6 | -6.663 | -55.0712 | 2026-10-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 92bb4856-c649-37b1-827b-09e71cc80597 | -2.4806 | -56.0678 | 2026-10-09 15:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8845411b-4767-3caa-8304-f1d9c8d32263 | -1.2175 | -55.6512 | 2026-10-09 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 449.9 |
| 013cabcb-451f-3aa6-915b-f3410417b85b | -8.969 | -45.1313 | 2026-10-09 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 278.4 |
| 05264493-4f89-3fb4-9db9-b8873758ebbe | 3.5492 | -60.2823 | 2026-10-09 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 35d0dc90-35cd-324e-aa12-a2148dc428cc | -10.5091 | -47.3179 | 2026-10-09 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| f81461c6-f503-381a-9adc-6263227f9594 | -1.1991 | -55.6909 | 2026-10-09 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 1ca2281a-efed-35f8-b5dc-b2e9e53be0cf | -11.2068 | -45.3091 | 2026-10-09 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 740a7e7e-5054-33bf-a1b3-55fc5159a9f9 | -1.1094 | -54.1601 | 2026-10-09 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 3d671e9f-d77b-364c-885e-f295b0eee95c | -2.9818 | -54.0689 | 2026-10-09 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| edb50015-01eb-3f48-b84e-09e0a2ea3bd3 | 3.5493 | -60.2633 | 2026-10-09 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 80f49fdf-b1bc-37ee-ac44-872291f1fd9e | -6.0609 | -42.608 | 2026-10-09 15:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| ddcfb03f-29a5-397a-9250-0ec3f711a24c | -9.2778 | -47.4554 | 2026-10-09 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9f27f0dd-c161-3944-85f7-d97d2dbd4f4a | -1.1992 | -55.6712 | 2026-10-09 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 77a3f6a9-79e8-383a-9bd5-85f579727dc9 | -9.297 | -47.4313 | 2026-10-09 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 15d5d195-841b-3dbb-a764-432fe6148234 | -1.4939 | -54.5563 | 2026-10-09 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 13a61f5a-4af4-3da5-99cc-92ebc8c0d31f | -6.4599 | -55.0015 | 2026-10-09 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 94846fc0-2611-3cee-b3cc-0cbfed7482d4 | -1.3447 | -56.3979 | 2026-10-09 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f260c4ca-15e9-3e3c-9e35-eb6d37448b02 | -3.019 | -53.9473 | 2026-10-09 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c54d2ccd-e1e3-390c-90e9-0816f8a9a0ce | -1.3277 | -55.4525 | 2026-10-09 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c856105f-aa1b-372a-a82d-f3e72c5fda05 | -2.348 | -58.0017 | 2026-10-09 15:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4e63e710-85e9-322a-b93e-068235574a76 | -8.3014 | -45.7019 | 2026-10-09 15:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2a61cb52-a18d-3528-bd8c-b299d68ef283 | -1.494 | -54.5363 | 2026-10-09 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ee798dbe-670e-3f00-a16f-c27293b79600 | -13.1447 | -54.3405 | 2026-10-09 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 067cba02-afe1-3f8d-9c39-d5a8a95dfa1c | -6.0624 | -59.928 | 2026-10-09 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 50c0cb10-c5b8-33eb-b2e8-467f1957090c | -10.7475 | -46.6184 | 2026-10-09 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 25eb0672-a684-31ab-92e7-904fc9f7eb8f | -9.9208 | -44.7893 | 2026-10-09 15:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |


[Clique aqui para ver as próximas entradas](README248.md)
