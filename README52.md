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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1475249e-f4f4-3de5-a01e-1c64461cb70a | -12.285 | -50.38208 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b67ed7d4-167d-33ac-9158-ba5ac6926b4f | -10.83129 | -43.96052 | 2025-10-15 06:08:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a989a937-a190-3c6b-b006-bda1df1f107c | -12.20485 | -50.36949 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 484ae6d7-8239-3a51-bca5-4bf953cedb48 | -13.37919 | -43.65335 | 2025-10-15 06:08:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 01365839-4264-3783-bef7-ee24a6da6388 | -12.25687 | -50.38707 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 7e7d5729-7282-3f5b-8d45-d2ebb3a612ef | -12.26578 | -50.38847 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 36d4a80b-4ab8-33cf-89f9-ae74e0ca9287 | -12.20342 | -50.37867 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 4115fa48-5fe2-3833-8b65-58eb94cbde04 | -12.22266 | -50.37229 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 83e860bb-d2dd-3219-b4f0-e023d4db7ebd | -12.27327 | -50.39906 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9fc7b6ad-7c5a-3a64-a71e-0ff707a87f75 | -12.27609 | -50.38068 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6ffd19fd-a492-3571-a013-227cd4dcd9f9 | -12.28359 | -50.39127 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| ce588d21-2380-35cc-8ccf-8cad6cd62ccf | -12.27186 | -50.40825 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8a811598-ba57-336b-9be3-4fe865aafc45 | -12.24796 | -50.38567 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 6314b390-b285-3b13-8fd4-e35857a065b1 | -12.19352 | -50.37989 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 15b5037d-6a38-3734-b49f-072a0fa68a03 | -13.47665 | -43.70831 | 2025-10-15 06:08:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c1de394d-9963-3736-a878-ffe1eaba81ea | -12.27468 | -50.38987 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 6eb6198e-7649-3657-bd03-7c88e8574233 | -12.28218 | -50.40046 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 26053bb7-ea9f-34c8-923e-8b76548e9a9c | -12.18602 | -50.3693 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30b6c3cf-ec87-3154-b9f9-7dda406f263d | -17.20826 | -47.65165 | 2025-10-15 06:10:00 | AQUA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6392330a-a925-36d2-b649-cff57a8e65f5 | -17.60397 | -46.68897 | 2025-10-15 06:10:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3bb844db-95ca-3bfd-a872-c286701338e5 | -16.9057 | -49.9208 | 2025-10-15 08:10:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| ac7f2e60-b3cc-3d93-b051-476e900c0eca | -8.33098 | -38.08609 | 2025-10-15 11:19:00 | TERRA_M-M | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 6b230e4a-9cc8-3777-8e91-af1ebe23e567 | -8.26645 | -43.36284 | 2025-10-15 11:19:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| f2d71469-ac9f-3583-b6ee-429a5351af72 | -7.49668 | -42.72901 | 2025-10-15 11:19:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| 9c5eab7e-e08e-3798-81fb-cdc5d6fab1bf | -7.49251 | -42.72264 | 2025-10-15 11:19:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| c2bc1709-4ec6-321e-98bb-f772bf4245c9 | -7.09688 | -42.04161 | 2025-10-15 11:19:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 42.8 |
| 99453a70-700b-3a0c-abb8-09baf16e2a0f | -7.33305 | -39.71058 | 2025-10-15 11:19:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 31.0 |
| d7a75f0f-57a2-3dbb-a6dc-a50e355b81ea | -8.3339 | -38.07971 | 2025-10-15 11:19:00 | TERRA_M-M | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 19.2 |
| d61190fa-b8fe-37cc-a250-ea55a5c97fb7 | -7.42991 | -38.17936 | 2025-10-15 11:19:00 | TERRA_M-M | BOA VENTURA | PARAÍBA | Brasil | 2502102 | 25 | 33 | nan | nan | nan | Caatinga | 40.2 |
| 87e614ce-3f9c-3d12-b775-154e091d6a8b | -7.08865 | -42.03518 | 2025-10-15 11:19:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 387284ac-2c52-37b5-987e-e7c00a244ce8 | -8.26502 | -43.3568 | 2025-10-15 11:19:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 3c49b818-5a7b-3647-b7ba-e992c3fc248f | -12.52155 | -42.96135 | 2025-10-15 11:19:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 44.4 |
| 22c40731-8f6c-3c35-af7e-e12319969ba0 | -13.93306 | -42.23516 | 2025-10-15 11:21:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 0e5bbabf-19da-31e7-9963-4eea8412ce23 | -13.6414 | -43.7302 | 2025-10-15 12:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| bc2daa1c-227f-3f98-9f7f-92e98c69cc4b | -13.6414 | -43.7302 | 2025-10-15 12:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 8ec0e8fc-e7c4-388f-b58c-061097c30e9d | 1.8584 | -55.7229 | 2025-10-15 12:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| fa0d9f4a-b8f5-36ab-954b-dd1e9cc6152c | -11.5724 | -44.0736 | 2025-10-15 12:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| a9a9254c-460c-3ceb-ab81-ba8070ebdcc9 | -10.7753 | -47.2857 | 2025-10-15 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| c361079b-c064-3165-8ce0-69dc7dd9ebd1 | -10.7753 | -47.2857 | 2025-10-15 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 289dadc0-bb68-34d2-bd46-1cbc6d40e21a | -11.5724 | -44.0736 | 2025-10-15 12:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 6994f268-2aa2-3c01-a1cd-2e751e432667 | -11.5724 | -44.0736 | 2025-10-15 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 076d55f8-460f-3e3d-9f8e-80024dbd7b16 | -10.7753 | -47.2857 | 2025-10-15 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| f6d9ba97-1f98-365b-8b87-6dda8046049b | -11.5729 | -44.0501 | 2025-10-15 13:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| be9e736c-629c-3dba-b902-230f492a1283 | -11.5724 | -44.0736 | 2025-10-15 13:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 0e426716-dbfd-3fd9-89ba-db12975659cf | -10.7753 | -47.2857 | 2025-10-15 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5fe369c8-af9b-39ca-8bf8-b48cca615995 | -11.5724 | -44.0736 | 2025-10-15 13:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 855cf710-b014-3a1b-a54b-8de09d055818 | 1.0766 | -51.0403 | 2025-10-15 13:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ebcb0fbd-e2c6-3e10-bc4d-592fba95972d | -9.3221 | -46.9631 | 2025-10-15 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 329.3 |
| c0e17322-54c1-3d52-bfe3-07478b6b5c32 | -9.3224 | -46.9408 | 2025-10-15 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 2981176c-3472-315a-911c-59df9520066a | -19.0522 | -57.5148 | 2025-10-15 13:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 6cb281d1-3b6d-3dfa-b321-ef224bdf68f7 | 1.8584 | -55.7229 | 2025-10-15 13:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| bc46481c-32ce-393a-8caa-1be17e798dd3 | -11.7027 | -44.2879 | 2025-10-15 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 299f1e19-e4ba-3d78-bafa-b8edc6bcc1da | -11.4384 | -44.0703 | 2025-10-15 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 351db506-2775-3b1d-a45b-9ed800f7cc61 | -11.5729 | -44.0501 | 2025-10-15 13:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| f704cda1-53ec-3041-ac85-8ec866a66477 | -11.5724 | -44.0736 | 2025-10-15 13:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 0001fb5e-2a5c-3164-bdcf-cd39ba4939e3 | -10.7753 | -47.2857 | 2025-10-15 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 498ed3c6-d687-3bd1-a012-06894bddd793 | -12.0118 | -45.2161 | 2025-10-15 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 3b6e60c8-93fe-3b46-9a72-bfd8efce2e25 | -19.0522 | -57.5148 | 2025-10-15 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 5654217a-570a-3b3e-96e9-7c9c28d878c4 | -13.9158 | -43.6085 | 2025-10-15 13:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| fddae1f4-e55a-35a1-8c00-ac23f0a702fd | -10.8285 | -43.9717 | 2025-10-15 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 7594dd77-2f44-3221-904f-45a99f04fe98 | -11.5729 | -44.0501 | 2025-10-15 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 59a32024-6ea2-3aea-8638-458744971077 | -9.3224 | -46.9408 | 2025-10-15 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 5ac2d7f9-540d-335b-800d-da5c86e519ea | -10.8097 | -43.951 | 2025-10-15 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| d4f6f90c-650b-3c97-9932-01d135072bba | -11.7027 | -44.2879 | 2025-10-15 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| fc411e7f-02ff-3211-b317-7677fc6cc1b8 | -11.5724 | -44.0736 | 2025-10-15 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 369f55e6-278e-3fa1-b9c5-5b30c792a517 | -10.7753 | -47.2857 | 2025-10-15 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| cd457783-2a3e-3657-931b-4af61bc3929f | -10.8289 | -43.9482 | 2025-10-15 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 6a775b87-6584-3361-889e-1a61b8c8077d | -19.0519 | -57.5356 | 2025-10-15 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 48414d41-6109-3679-a11d-7e01f7b22d9b | -9.3221 | -46.9631 | 2025-10-15 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 23fdebaa-0117-3cbb-ae2b-1b2a1816da31 | -11.4572 | -44.0909 | 2025-10-15 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 3efbf833-9c8d-392a-9932-708d479559f9 | -12.0118 | -45.2161 | 2025-10-15 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 2b4db3b5-e384-3b82-9a32-4113ec5c9e10 | 1.3349 | -50.7253 | 2025-10-15 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.7 |
| d8ad5295-5abe-3b3c-a4f4-d01731aca3f6 | -10.7753 | -47.2857 | 2025-10-15 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 34ecb5ed-a3a1-36e9-923b-2d41d46cb1b8 | -19.0522 | -57.5148 | 2025-10-15 13:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 99cf0d89-c748-3df3-81f2-6db78c7fe735 | -9.3221 | -46.9631 | 2025-10-15 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 22113e0a-efe8-30b6-887f-9da675ba4507 | -10.8097 | -43.951 | 2025-10-15 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| df5ac6b0-06e3-359a-8ea7-9cd92f4c65a8 | -11.4572 | -44.0909 | 2025-10-15 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 573b44e3-87e5-3119-afaa-fdea8cd88f68 | -15.316 | -43.8377 | 2025-10-15 13:40:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 7acd2154-dc97-3994-bed5-3018e5a81eee | -10.8289 | -43.9482 | 2025-10-15 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 167.2 |
| d23cfb28-bf27-3fd3-81ab-740ae8ef4866 | -10.8285 | -43.9717 | 2025-10-15 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 620c2579-28ef-32c7-b9d2-db3962cbfde6 | -11.5729 | -44.0501 | 2025-10-15 13:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 243.6 |
| d6bbc898-7720-36de-adfb-c90a7d2d9e8d | -11.5724 | -44.0736 | 2025-10-15 13:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 347.7 |
| f8350093-a904-38ce-b441-1b214d200ed8 | -9.3221 | -46.9631 | 2025-10-15 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| dcbc52bc-c955-3b34-9172-d7cafb5ab77a | -10.8289 | -43.9482 | 2025-10-15 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 48d071f3-9190-382e-8ee4-84672975faa1 | -11.4384 | -44.0703 | 2025-10-15 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| ff26120d-d838-3af6-b184-de62f2886eed | -10.7753 | -47.2857 | 2025-10-15 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| fe88c2e5-3a5b-3616-a672-7133f1efd4aa | -10.8097 | -43.951 | 2025-10-15 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 6b29f357-05a9-3d7a-9503-e9384afff102 | -10.6734 | -45.2896 | 2025-10-15 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 589a70f5-ea28-321b-80cf-f3b7bf1c325c | -11.5729 | -44.0501 | 2025-10-15 13:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 341.4 |
| e2e56137-ab91-3cf9-a6e1-d852fd195f7b | 1.3349 | -50.7253 | 2025-10-15 13:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 6336e822-4c55-376c-84a8-c78e4fbae740 | -13.8768 | -43.6157 | 2025-10-15 13:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 9bb47110-ac4d-307a-a4b1-3f4ee1823ef5 | -11.4389 | -44.0468 | 2025-10-15 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| b7e364df-fc7a-316b-abad-bc65b85819cd | -13.7305 | -42.3185 | 2025-10-15 13:50:00 | GOES-19 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 119.5 |
| ff213516-fb54-34a6-b078-f9134aabe64a | -15.316 | -43.8377 | 2025-10-15 13:50:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 804be3bf-dffe-385d-a537-4afaa0c79445 | -11.5537 | -44.053 | 2025-10-15 13:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 414b8487-8d41-3128-97fe-fcc591d08b23 | -9.3224 | -46.9408 | 2025-10-15 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 1bb6e126-bc15-3853-a460-5546d9c9fce0 | -10.8285 | -43.9717 | 2025-10-15 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 68c1809c-22c3-3dc9-9d9d-c4eba2920b7a | -19.0722 | -57.5122 | 2025-10-15 13:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 7e7c57d0-4bef-3fac-adb3-4ec5c5474cd0 | -4.6509 | -43.1337 | 2025-10-15 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 632.2 |
| 1a58d715-d6c9-3725-937b-880cc882bc23 | -10.6734 | -45.2896 | 2025-10-15 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 162.6 |


[Clique aqui para ver as próximas entradas](README53.md)
