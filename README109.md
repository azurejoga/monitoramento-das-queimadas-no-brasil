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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d54aad84-c5bf-3009-ab01-6e53a4de2ceb | -15.19335 | -46.39279 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f02f3ea4-e000-3525-91df-9dd7d997b574 | -13.74864 | -48.09861 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3cf78ab-f9bd-32d0-9d90-1ff65549b182 | -13.39385 | -47.28794 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 43968e3d-28ed-31fa-9923-f16ec2246934 | -15.62219 | -46.93809 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6262a51f-7c06-3fc9-b38b-366842057c7d | -13.31749 | -47.25501 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 227be66d-21bc-380e-8cff-779871a9c8cb | -13.32277 | -48.09296 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 982b8710-ff94-39b9-87de-baf3d902de8a | -10.80533 | -48.81787 | 2025-10-04 05:06:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0dfa17f6-3365-3efd-b63e-1686bf629e3a | -13.3416 | -48.0711 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc5f0598-576c-3752-9703-26c614a2c2db | -13.1755 | -50.92606 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| d6556d5e-6f38-3faa-9826-c1739de99d80 | -13.14798 | -47.80722 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a8cc935-aa12-3f49-9402-b3f281636e98 | -11.91568 | -46.38854 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2f11acc-a1bf-3afe-bfe1-0a0900616900 | -13.18011 | -50.92484 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 5e628335-fa7f-36e3-b3c1-22298580f8de | -15.59932 | -52.48807 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d3f0e94-4d45-319d-8bf1-753ec689ecb5 | -14.89453 | -48.35369 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 46d65ff1-eb71-3823-9878-79ab694b3a39 | -14.94597 | -46.8666 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6157547a-a27d-3203-86a0-8c1d18cbec84 | -15.22178 | -56.81674 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8526c75e-e4cc-351b-a2e3-8b89bc92fb48 | -12.30118 | -55.13565 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b7c2334-b261-3cea-bfb8-65f163edd6fc | -11.38387 | -54.35566 | 2025-10-04 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d07ca31-2df0-3447-8686-b6b9d18a8aa9 | -11.92838 | -46.38861 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d8b31372-fc8a-38c6-bebb-623cd547ae9f | -14.75365 | -54.63138 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca62d43d-ce61-35f1-beca-1a29df7624e4 | -12.99144 | -53.42978 | 2025-10-04 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 497ca907-909b-3118-916e-f00d2984532b | -11.54889 | -47.67786 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 73d142cd-eee2-3fad-a44f-0cef776f62af | -12.64305 | -46.99131 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b35b89a3-9275-3e48-bdec-a937d1649282 | -12.81717 | -46.86242 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84d56174-0114-3a8b-9b54-ff76b73d9fc2 | -10.53901 | -53.72682 | 2025-10-04 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ced4fc4-8d89-345d-9f02-b872c211c48e | -11.92016 | -46.40134 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| da658edd-cfbc-3bf3-bf9f-e79575b7cdb4 | -13.72618 | -51.31345 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54f5e6c3-c36f-37de-8f04-f9d10505d312 | -13.74243 | -47.94394 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 096210ba-c1ee-3307-8c19-48deb1b60a4f | -13.12671 | -47.83156 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 06c75317-3b67-3d1f-9680-edbcb39fe6e2 | -14.6566 | -48.23795 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d79016a3-f8cf-3253-9f05-e2e255994973 | -14.6616 | -48.24189 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86f8ab35-eeed-3e16-8081-e7f8bcbf6ba1 | -11.82527 | -48.07101 | 2025-10-04 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a823e1b-5ccb-3228-94c5-bca7c3bf7663 | -13.74363 | -48.09475 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b15cde54-f994-3b4f-ad29-49fb16ef873b | -11.1119 | -47.75045 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb13ec55-6af4-345e-9adf-8c4efee7a1bb | -15.61528 | -46.94676 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57a2673e-be2b-3820-829e-16d7a130a580 | -13.1272 | -47.82754 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3fe37837-6c52-3e70-8156-476a212f2a09 | -12.93165 | -45.07074 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a802fe32-3ba8-30d2-8504-8a50e4dd63e1 | -14.21979 | -46.06544 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe99e9df-45b3-3b4f-b4f8-380491d19422 | -14.97837 | -46.84319 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c296843-21e0-3594-90b6-9b6a4ca561a5 | -13.34218 | -50.95565 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aac8f86d-a988-3d3f-9001-9b26fad5ee67 | -14.68465 | -48.27812 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8d01fb6-a9ed-3654-9fee-1524a6f7dbb9 | -14.8927 | -48.3518 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 427274eb-b57c-3213-ad6f-2e626addb0fc | -11.13503 | -47.17379 | 2025-10-04 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4aed2ae7-77d9-3373-be11-68b57ca85063 | -13.34225 | -47.23887 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3fcde76e-c7e0-3412-be45-33f373c48e23 | -11.88486 | -44.99601 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 27cd0830-d8bc-345b-9749-d0b30acc4b3a | -11.91867 | -46.37047 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae6a73a2-79ed-3d29-a3a1-5cc4cd6e7728 | -11.13341 | -58.40691 | 2025-10-04 05:06:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10ac99c6-3fe2-3b84-b639-8598ab9521ba | -14.89327 | -48.27189 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 675a7b6a-c3d0-3c3c-91df-fd22ba77d990 | -13.2389 | -47.3596 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01686933-a6f7-34a5-bdee-0e64d9118643 | -12.92705 | -46.37106 | 2025-10-04 05:06:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bbb95f7-7033-3645-9e29-f0184b4d2a94 | -11.54663 | -47.67944 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9c315d0c-c446-3a7b-9508-6fb6f11e29ab | -13.74163 | -48.08784 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fac50a4a-52db-312c-94ef-7dbbef5edc7b | -14.98383 | -46.84824 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6aca990-2e12-3a34-9177-ff4ab5f99a10 | -14.38331 | -48.47432 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 628a830e-d1f6-3eef-8d43-5aac69568fd3 | -14.00029 | -48.19075 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 849fd8a7-71fe-31ef-b8a8-d991f7ae0cc5 | -11.92095 | -46.40078 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 88eee274-3115-31c7-aaaf-53d85cf19786 | -13.74368 | -47.93338 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1d045f8f-b4e7-39bd-8c1e-b0901aed9a40 | -9.45642 | -56.64732 | 2025-10-04 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4997947-fee8-35b1-8e17-500a7116a76c | -11.9118 | -46.37795 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84fe6ee7-a4c6-3f8e-b2a2-b7b67eca6f7e | -11.79312 | -46.83133 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3280dde4-32ac-3a50-891f-5854c4b83a4c | -12.47735 | -54.42494 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f767db21-22b6-3ec8-b5ac-848bcdb0f065 | -11.74278 | -54.72009 | 2025-10-04 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c8da01b-694b-3180-943a-c99e50a14719 | -13.32494 | -48.12113 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89e68b7f-f4b5-38d2-816c-f47320080218 | -14.93121 | -46.85433 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 37ee95b4-27c2-3a28-9f67-6b37164e8eb1 | -14.89029 | -48.29723 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2b0707d3-9fa5-3e1e-94f3-dba40f11ab7e | -14.58197 | -52.49281 | 2025-10-04 05:06:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f2be042-5247-3df3-b263-9fa514780d84 | -13.39025 | -47.556 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26f7536f-995a-33a2-b910-8de2aefea0f1 | -12.0809 | -45.19334 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1bb64a4-2de7-31bb-9c45-7acdedc1f1bb | -14.20071 | -46.07232 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 69334140-061f-363d-8b16-03cd604c520b | -14.6956 | -48.09195 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5c2d361-57c1-3f69-a1a4-3e1e51b315db | -15.57627 | -52.47217 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b28360d-d010-3506-a916-acadd6e5fd6c | -11.9278 | -46.39341 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e751bc3c-908b-3007-991f-34cb494ff0a0 | -11.47718 | -45.0335 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c1cf316-9f03-3bc4-a7dd-beffff0bf284 | -11.63016 | -45.07045 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87adc1cb-0d24-38db-a150-32a8f1cd2ac0 | -14.96133 | -50.00171 | 2025-10-04 05:06:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d18ff4f-0dd2-33b1-8d03-87cbc71ecc4d | -14.57991 | -52.4777 | 2025-10-04 05:06:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c89ac4e7-9cf7-32fb-9326-be410ed34207 | -13.33624 | -48.07046 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf11203f-48a6-37dd-bb1a-ba782b1ab206 | -13.99302 | -48.20651 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b0b903ac-c3a0-3435-9769-f1afa56fc14b | -9.45588 | -56.65079 | 2025-10-04 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 193de509-11f9-3748-86a5-1c9772e1d550 | -12.583 | -48.12418 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3006890a-aaa4-3dc4-8bd0-0f4e2fd3cefe | -16.35025 | -47.06953 | 2025-10-04 05:06:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 25753416-ebcf-392f-b79f-b3f96ee995de | -14.24228 | -46.08833 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0836d1e8-1fb1-3450-ad43-3cc7969eac97 | -9.8858 | -58.03536 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eac99b4b-38d9-36de-b248-3e1ec59f30e7 | -9.37218 | -63.4509 | 2025-10-04 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1414f906-3a20-3444-8638-8cc0ea375ac4 | -9.92698 | -62.22112 | 2025-10-04 05:06:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1964efc7-b6e8-3a01-a18f-936bf9881bdf | -13.59723 | -49.39507 | 2025-10-04 05:06:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b842694a-d127-3b04-8521-c6b9f365ab10 | -14.68013 | -48.27017 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 75702ae1-242c-3730-a8f8-dc6e249d8d1c | -12.72437 | -48.57598 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 000f7c6b-1ac7-3a02-ba91-c03f6c54f780 | -10.83021 | -57.19391 | 2025-10-04 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b08913c7-a89a-3a24-8660-a3ceafca6f4f | -13.17159 | -50.88783 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 03390daf-cc63-35a1-b880-4087a4da41ec | -14.29054 | -47.41846 | 2025-10-04 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2eaefa5-6726-3861-8d3d-c49e11c0ec06 | -11.54846 | -47.68125 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 513bae0c-202f-3816-a61b-adbea4372b84 | -13.1241 | -47.94279 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da3792be-bafc-3e68-9cbd-e3dc24165839 | -15.72208 | -46.27488 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f6b44511-1b05-3199-99b7-c6b4751aba66 | -14.93928 | -49.98197 | 2025-10-04 05:06:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45fcd1f7-4a69-3246-bb9c-7766abadfbbb | -11.70685 | -47.50717 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 884cf015-637b-379e-90d8-7612646bc91f | -9.26974 | -62.37808 | 2025-10-04 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d5e52f2-006e-3b60-b2e9-539c04516f73 | -11.5547 | -47.67505 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d27d6e03-acbd-35ed-9236-c982a3c8a118 | -15.03499 | -56.05092 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51de231b-805c-33c5-8b34-c235557eb31a | -13.35354 | -47.2405 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README110.md)
