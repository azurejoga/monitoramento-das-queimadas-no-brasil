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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68a510be-43f4-3457-833a-bc8850101090 | -10.514 | -43.3815 | 2025-10-16 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 174.3 |
| a770563d-224f-3a4e-b1a7-e8632e7c9351 | -6.373 | -41.507 | 2025-10-16 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 132.3 |
| 3389abc9-ee49-3eda-a1d8-a5e0403f8132 | -5.4558 | -41.0297 | 2025-10-16 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 218.0 |
| d14a3553-52fa-367a-8141-5810e01e6cf1 | -15.3269 | -45.0439 | 2025-10-16 14:20:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 6001dcb7-b90d-33cb-9500-02cf78bacc70 | -12.9372 | -47.1049 | 2025-10-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 2b677b3c-823a-34ab-b0c5-0fe8c3b113a0 | -13.0743 | -46.9717 | 2025-10-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| b5238931-ca5e-3dd4-82b3-22e773506f51 | 1.8218 | -55.7431 | 2025-10-16 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 3d21f063-862a-3d92-97e1-e76c732d4178 | -9.3596 | -46.9813 | 2025-10-16 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| ad5ce130-83e7-303d-910d-0b1a503bdb4b | -13.055 | -46.9746 | 2025-10-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 23f6eb8a-601c-34f5-b13f-a3d7f20da645 | -12.2655 | -47.1121 | 2025-10-16 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 7dcd3ed3-4211-31cb-8694-ef024010e484 | -11.7027 | -44.2879 | 2025-10-16 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| dd4a0c40-4a78-3722-b38d-ccd7172fa883 | -10.1528 | -44.5289 | 2025-10-16 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a7ecc90b-3076-3ed8-a5e4-382011629064 | -9.3599 | -46.959 | 2025-10-16 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| e6023f87-7de8-39f4-80f1-9902836b1f89 | -12.9565 | -47.102 | 2025-10-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 7ac42f0b-06f9-3398-b9e4-51b7b3e55e39 | -11.3603 | -45.2646 | 2025-10-16 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| e3bd29ef-a5a6-341c-8cbc-2abe80ff3987 | -11.907 | -46.8251 | 2025-10-16 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 229.4 |
| 3b4dfa9e-5f68-3a4f-9e0f-372b9247d363 | -6.3733 | -41.4828 | 2025-10-16 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 232.2 |
| 09ce0771-9a30-3f96-bb0f-4fc206c946b7 | -14.2428 | -51.6079 | 2025-10-16 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c7e81838-0df8-3f20-97e1-9ea1b9bae76e | -10.673 | -45.3125 | 2025-10-16 14:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 9f5a4ef2-fe76-3e67-ac9f-ff63e1f36084 | -13.4412 | -47.9483 | 2025-10-16 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 88a3c18d-be7a-3c6b-b29f-9bf7d8e93c94 | -13.1129 | -46.9658 | 2025-10-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 2414f552-c293-399b-8039-9a2bbb7602aa | -11.5921 | -44.0472 | 2025-10-16 14:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 9561c292-fcdf-3843-9c48-4f89eb4194b5 | -11.4589 | -43.9969 | 2025-10-16 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 4e02216e-d7db-36a2-9efb-cb29206a24f7 | -6.4476 | -43.3736 | 2025-10-16 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 777e50ae-db5b-3af6-a499-21cc68622e26 | -4.7752 | -46.6017 | 2025-10-16 14:20:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 5d6d17a7-ba75-3436-a7a2-264718e00bbc | 1.7851 | -55.7436 | 2025-10-16 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 24ef66ef-0c1d-3767-a0c7-888ab58e1b59 | -5.8799 | -43.8844 | 2025-10-16 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 7460e775-e2f6-30b9-8438-1fdfd52bcc8f | -11.4176 | -44.167 | 2025-10-16 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 284.0 |
| bfe29835-f770-3bb0-8bbe-33f50e30fc2e | -10.6539 | -45.3151 | 2025-10-16 14:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 2946dedf-5cd3-39a4-bf30-30255385c78e | -12.3112 | -45.6311 | 2025-10-16 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| ac6a4f6a-f4ad-364e-b0e5-dacc91862b11 | -7.4781 | -42.1419 | 2025-10-16 14:20:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 723.0 |
| b92402a2-7310-3882-ae6c-6576fbe8cd1b | -11.4368 | -44.1641 | 2025-10-16 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 5fe0587b-a1d3-3c44-bfb3-f29def3a476f | -10.6543 | -45.2921 | 2025-10-16 14:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| ce073975-12f5-394d-839b-0ac96f9ec3cf | -4.3872 | -43.406 | 2025-10-16 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 588.4 |
| d565516f-91df-33da-a511-368e88df1a0b | -9.7162 | -44.5149 | 2025-10-16 14:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| c440ae02-5d30-3e6a-a971-ea780139467f | -11.4197 | -44.0496 | 2025-10-16 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| ed770614-5cf4-3a60-84ca-aacd90de5bda | -5.739 | -44.9945 | 2025-10-16 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 7402dbc2-00a9-3daf-8a73-1fa7956bf1a1 | -7.497 | -42.1399 | 2025-10-16 14:20:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 238.0 |
| 0a29eddb-eb86-323e-ad43-8ba0f3673345 | -12.9909 | -47.3217 | 2025-10-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4b32615a-717d-3fdb-b1e7-de508cd35dcf | -11.4389 | -44.0468 | 2025-10-16 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 202ffeec-cebd-35fb-8de3-24687b81466e | -4.3874 | -43.3827 | 2025-10-16 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 372.7 |
| 02ce619c-97c7-3e2d-a1c0-055e5fb8dab7 | -10.8154 | -47.1471 | 2025-10-16 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| a839bc92-901f-3df0-b44f-015c4adcbd52 | -10.133 | -44.5777 | 2025-10-16 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 429.1 |
| 0c8d7a3b-fbbd-3e1a-a022-ec4fb04c948b | -4.115 | -42.2011 | 2025-10-16 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 202.3 |
| 4ff14849-c761-3f75-9c17-b8e3ad9c855c | 1.0582 | -51.0198 | 2025-10-16 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 8e8b8f38-d8bc-394a-9121-5390fc8d3902 | -9.2871 | -45.3691 | 2025-10-16 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 179.9 |
| e55966c6-fb8e-37be-86bf-821a9552529b | -12.2652 | -47.1346 | 2025-10-16 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 4a051a5c-7703-3f6c-81a1-ee084be7dafa | -6.5903 | -44.1039 | 2025-10-16 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| c1646561-09a8-3eb3-9113-d7ab8ba24c11 | -11.5724 | -44.0736 | 2025-10-16 14:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 249.9 |
| 9fb5ce5d-ecbc-3222-b4ed-58f3bf9face2 | -11.7031 | -44.2644 | 2025-10-16 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 5c019bc1-a3f1-3fa7-8601-9a83c3724ba5 | -6.1758 | -44.2992 | 2025-10-16 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| bc680db2-53ff-3ef5-8103-a29d4a35887b | -11.4576 | -44.0674 | 2025-10-16 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| b7acb0c4-27fb-341b-a5e1-902f24aeb726 | -11.418 | -44.1435 | 2025-10-16 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 341.4 |
| 9b22fec4-5681-332a-9973-438c5b500d51 | -10.8289 | -43.9482 | 2025-10-16 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 8deaf6cd-79c8-3761-b21a-1f044ee72b24 | -12.2919 | -45.634 | 2025-10-16 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d31f9183-5f2d-3600-bcf4-9c9c2c05c6a6 | -10.7753 | -47.2857 | 2025-10-16 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a5e7dd66-68bf-35e4-a63a-4a13d28aae97 | -12.2844 | -47.1319 | 2025-10-16 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 222.4 |
| 22e7e983-1129-3e6d-8a14-364b21380050 | -11.4572 | -44.0909 | 2025-10-16 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 6e47f0ee-9706-3f4b-868b-9ba0b8f3930c | -10.1524 | -44.552 | 2025-10-16 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| a0cd3368-6b99-3ad7-a484-2150abfc0cb0 | -10.5144 | -43.3579 | 2025-10-16 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 397e8f6f-affe-364e-900b-97fb4852fb50 | -13.4605 | -47.9454 | 2025-10-16 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 903e61cd-239c-3306-8fd5-9ed6cf91d985 | -11.4372 | -44.1407 | 2025-10-16 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 9e17639e-fb0b-33b3-8d2e-21b491e158bf | -12.284 | -47.1544 | 2025-10-16 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 09729a97-6d8c-33c1-abac-233dbac47be1 | -4.4061 | -43.3816 | 2025-10-16 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 9485a0b5-2a0a-30b1-adb4-80c298b663fc | -4.7938 | -46.6007 | 2025-10-16 14:20:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 3da95ade-da08-3ef4-8817-a982a7e42d53 | -4.3687 | -43.3838 | 2025-10-16 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| a48dd226-c001-3653-bf4a-1d243cb271b1 | -10.8289 | -43.9482 | 2025-10-16 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 13b06c2b-b605-3b78-8a8b-5a3c0003f54c | -12.2844 | -47.1319 | 2025-10-16 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 6096df30-b75d-3211-87d0-7ae654822c59 | -19.0726 | -57.4915 | 2025-10-16 14:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 65.0 |
| fa7d71b3-7792-341b-b78c-08fef4921854 | -12.9372 | -47.1049 | 2025-10-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 6cd5eaef-d591-37a2-a44d-a2501f46de18 | -11.4389 | -44.0468 | 2025-10-16 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| e75e721e-0817-33dc-8f24-e725349d31a8 | -6.892 | -43.9851 | 2025-10-16 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 209.4 |
| f019dfd6-ef83-3b31-9eec-7f130a70e003 | -4.7938 | -46.6007 | 2025-10-16 14:30:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| d9999827-39f2-3298-b3fc-7d81c3cbcac5 | -5.6097 | -42.6914 | 2025-10-16 14:30:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| ee6eb426-2f6c-3502-8299-287b6ee00f48 | -11.1215 | -45.8463 | 2025-10-16 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 65b0fcae-b5c2-3538-9fa3-5bffe1fe4ed3 | -4.1149 | -42.2248 | 2025-10-16 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 161.6 |
| e6ea09f9-46f7-3bd3-8287-da8c52505dd1 | -5.4561 | -41.0054 | 2025-10-16 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 124.7 |
| 95f6b3c0-fbd0-3d8d-a2ff-3e4f0579ac51 | -4.115 | -42.2011 | 2025-10-16 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 188.4 |
| 6100550d-8900-34e5-bb7a-5c177fbb9244 | -19.0319 | -57.5382 | 2025-10-16 14:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 87.2 |
| f047928a-d0c8-37e3-aa12-ccfd4e7ebc2c | -11.4384 | -44.0703 | 2025-10-16 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| e68327e9-e517-3afd-b69e-707e6b21f1e8 | -5.6095 | -42.715 | 2025-10-16 14:30:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 26860e26-7220-3c5d-a417-59e0e20a18b4 | -9.2505 | -45.2821 | 2025-10-16 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 8b93816c-487d-3e8f-9c8f-7120dcd7b187 | 1.8585 | -55.6834 | 2025-10-16 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| edabce5f-7bbb-3a4f-996b-cb7f432fb5b6 | -9.2871 | -45.3691 | 2025-10-16 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 2bea80a4-8e15-34dd-83ef-1ffe8f55b67b | -19.0323 | -57.5174 | 2025-10-16 14:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 7bc2ecc4-d363-3842-b15f-916b7f6dcbfc | -3.7629 | -41.6728 | 2025-10-16 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 3ddb581b-3790-3f26-86bb-8e19553a366b | -6.373 | -41.507 | 2025-10-16 14:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 128.8 |
| 237f2393-6858-3c32-9d23-b4c92617815a | 2.0782 | -55.7789 | 2025-10-16 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 3c7f3cf5-5cd0-375c-b2dc-d40cc245deb6 | -13.2918 | -43.7689 | 2025-10-16 14:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9201ea20-27ae-3aad-b77f-15716f17776f | 1.0765 | -51.1026 | 2025-10-16 14:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 832026b0-af5f-3ca3-a1e7-d3b9bdacc4c8 | -4.3871 | -43.4292 | 2025-10-16 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 42bfd829-ea3a-388b-87ed-72f5e846378b | -12.8017 | -50.5088 | 2025-10-16 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 4ad2f063-d112-3fac-859b-ebc8b26dce15 | -13.8572 | -45.4515 | 2025-10-16 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| e8a8c506-aa9e-3439-85da-18ff3ad19e07 | -10.5834 | -47.42 | 2025-10-16 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| ddafcb44-2d3f-38d1-ac86-fa0e33cd5253 | -12.9565 | -47.102 | 2025-10-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| c493a00d-1a9f-3e8c-ad63-1e5816e616db | -4.1338 | -42.2 | 2025-10-16 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| bd2769b4-bb28-39ff-af01-762f2e3cbbd9 | -10.1333 | -44.5545 | 2025-10-16 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 1762ad64-aa20-34e4-bf4e-57080133faa7 | -11.7027 | -44.2879 | 2025-10-16 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| a7c9f880-fc5a-3c39-b89d-3ab19b2f5452 | -10.4949 | -43.3842 | 2025-10-16 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 145e446b-956a-3958-b571-e6cde8152825 | -4.6905 | -45.4013 | 2025-10-16 14:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |


[Clique aqui para ver as próximas entradas](README95.md)
