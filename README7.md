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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d712ace-346f-367f-947c-5905b061e667 | -3.9812 | -44.277599 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 601184fe-f1b8-3d73-b011-904745de4f94 | -4.9202 | -44.7854 | 2025-11-15 00:18:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 006e8c05-1f0e-3ddf-862b-a2930567ef49 | -2.519 | -47.8176 | 2025-11-15 00:18:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5a5a3b5-6a65-34f2-8ee7-dc55545c90d5 | -7.3089 | -39.776001 | 2025-11-15 00:18:00 | METOP-C | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 32c25494-908a-3a1b-9dec-5eba2d2b1ff9 | -7.4833 | -42.546398 | 2025-11-15 00:18:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1e0d62fa-5293-3af0-9c54-26d9036b8bed | -4.4851 | -44.091599 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8be8199d-4210-3646-91d3-ea82d3a935f1 | -4.9088 | -44.780201 | 2025-11-15 00:18:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d5f6610-9844-35b4-b90d-86fa4320e823 | -4.7211 | -47.153 | 2025-11-15 00:18:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e40ed2c2-8c94-3cdb-86af-7ae615608900 | -5.4829 | -40.976101 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 693fcf13-701a-3785-aae2-d69b669edff1 | -7.3087 | -43.826199 | 2025-11-15 00:18:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 28c8d7e5-d0b5-359f-8446-bb7df6b34bc2 | -6.0689 | -39.593102 | 2025-11-15 00:18:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| af3a85c0-d587-31de-bdc0-5091c6a3e4a4 | -9.0153 | -46.879299 | 2025-11-15 00:18:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aaa4c45f-7c37-3efc-a546-5a7ec2073bb1 | -3.8828 | -46.209099 | 2025-11-15 00:18:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 50744b1e-8af4-30ae-a1ca-8ae67b9045b0 | -7.8708 | -48.405998 | 2025-11-15 00:18:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6486abe2-bc4a-39e9-b541-371a75af8806 | -3.3528 | -46.868401 | 2025-11-15 00:18:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| accda23c-8816-3f31-99f8-fc68ffda784c | -4.6418 | -47.9492 | 2025-11-15 00:18:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5a13ac0-4a91-3a44-9b5f-b864f6847e21 | -10.1778 | -44.3871 | 2025-11-15 00:18:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 892268a7-3aae-3edf-ad0b-bd930e48e4e0 | -9.7141 | -48.890598 | 2025-11-15 00:18:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bcabeb99-c085-3b92-8d2b-97a60a19c171 | -10.3322 | -49.628601 | 2025-11-15 00:18:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ce5cf07-4755-3ffa-bf68-ce0330046c5d | -7.3103 | -43.8335 | 2025-11-15 00:18:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5e4f65ca-6424-3a7f-8630-1b12ecc00dd9 | -3.2706 | -45.457699 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9070490-d5f5-3868-8305-25ec702719d0 | -6.0918 | -41.6022 | 2025-11-15 00:18:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2466cb9-8390-39db-80ba-c48baf35b59b | -13.8994 | -42.8988 | 2025-11-15 00:18:00 | METOP-C | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a3c60d42-75af-3dd7-b3e1-9e0cbd132e37 | -9.8539 | -44.173901 | 2025-11-15 00:18:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 46ec033a-da30-3041-9cb3-eea749705269 | -10.4226 | -44.946999 | 2025-11-15 00:18:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8f577728-e8a0-3b1c-b5f0-b76a7dd82888 | -10.9922 | -44.688702 | 2025-11-15 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 60629c0f-d183-35f7-b62f-5c3775f60ef5 | -4.4655 | -45.644501 | 2025-11-15 00:18:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bec7a823-20ed-311a-9584-873b69844503 | -10.3703 | -47.737701 | 2025-11-15 00:18:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afa58bcd-312c-347f-a87b-05c83c9b1e7b | -3.6094 | -43.369801 | 2025-11-15 00:18:00 | METOP-C | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71cc9b8e-88a5-35e9-a1d7-bf0c2faaa9e1 | -7.2589 | -48.029301 | 2025-11-15 00:18:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f24b4ae-5811-3d88-97e1-a805702b339a | -12.7606 | -43.661701 | 2025-11-15 00:18:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fb666164-91f5-3866-850f-03c01cd4d86e | -2.8567 | -45.358601 | 2025-11-15 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8dad5b2-f3ba-3a6d-8cdf-9b05b4984660 | -3.3622 | -45.453499 | 2025-11-15 00:18:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| acf5b87a-8029-3e9c-ac59-51acc697dfe3 | -3.3834 | -47.186401 | 2025-11-15 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9949678-2fa3-339e-9e60-81b99de50b9c | -6.4485 | -35.067299 | 2025-11-15 00:18:00 | METOP-C | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 354ef773-ea96-31c7-bab1-e0c9fe35f9f9 | -4.6005 | -41.7565 | 2025-11-15 00:18:00 | METOP-C | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9341bad7-5522-397c-a872-641bfbe5cc7b | -6.3074 | -41.822399 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c35d65a9-4ee4-36e7-964f-ec59f7220706 | -3.9878 | -44.261299 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23ef0d17-4ff1-3059-b4c1-acebdb9b34f4 | -3.697 | -47.622501 | 2025-11-15 00:18:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b8084aa-e9fd-3577-941f-9cb8cb39ec08 | -11.6796 | -44.739399 | 2025-11-15 00:18:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18b2593b-ada4-30a4-9262-08354818b7d3 | -12.4329 | -43.1917 | 2025-11-15 00:18:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e0530b3-c34c-36ad-bf20-1eeb2b95e76e | -13.3528 | -43.745201 | 2025-11-15 00:18:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad568d48-10a7-3683-883a-567fd0d3127b | -4.1017 | -48.009998 | 2025-11-15 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75310cf4-213f-3e2b-b690-e8fd0e2eab7e | -12.7572 | -43.645599 | 2025-11-15 00:18:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a23ceac9-70b1-3fbf-ba54-f4fe2d2e59d1 | -10.0483 | -44.264099 | 2025-11-15 00:18:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe94f0d2-a43b-377f-87a8-519f2f3ede8d | -4.9084 | -38.694199 | 2025-11-15 00:18:00 | METOP-C | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fa9ad2ee-62b2-3bc4-9891-9f4cd1dc6a9e | -4.2232 | -45.482601 | 2025-11-15 00:18:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fdf435d2-49f0-3472-ae6e-8d7739ffb0a1 | -4.4742 | -42.868099 | 2025-11-15 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df26292a-e4a2-37a7-825d-f2b007ba6140 | -4.2603 | -44.599602 | 2025-11-15 00:18:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2af5b403-6310-39f6-87f6-0ee81b329419 | -7.4253 | -45.226501 | 2025-11-15 00:18:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13d26e03-b0df-3bec-89a8-2b76d949cd13 | -3.1021 | -45.4869 | 2025-11-15 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a016d5a-350d-396d-9451-0ba02c338fde | -4.5989 | -41.7495 | 2025-11-15 00:18:00 | METOP-C | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 743ff77d-287a-3266-80d3-210a215abdc3 | -6.4522 | -35.0821 | 2025-11-15 00:18:00 | METOP-C | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2740c52f-e9d8-3e58-9ee7-c5034da1c179 | -7.5333 | -45.856201 | 2025-11-15 00:18:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ffd9d9a-819b-311f-ae52-4671c9d8d57e | -3.8847 | -46.217499 | 2025-11-15 00:18:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c084183a-d0b1-302d-b98d-f5bf8c1b2c37 | -8.3809 | -43.835098 | 2025-11-15 00:18:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e41d95df-6aa9-36f1-b258-8554832e83f3 | -9.4811 | -47.291199 | 2025-11-15 00:18:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9edb264-3d4b-3f39-9c60-c16c59ffd6e0 | -5.5842 | -45.175301 | 2025-11-15 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8a32c5d-3121-369a-b794-00fc99e04bed | -4.4867 | -44.098701 | 2025-11-15 00:18:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9bca453-fe73-3a6a-98a6-a0b1234a3c20 | -3.3359 | -45.292099 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d78a0f20-07c6-31c7-a3a3-dae6fde6b7e8 | -9.7489 | -43.9767 | 2025-11-15 00:18:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a572fbc4-8ccb-3d87-95f4-c4756f6ffe06 | -2.7366 | -45.283298 | 2025-11-15 00:18:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b217825d-b5b9-3484-a0c5-8dcba0ddfd4c | -4.3353 | -45.2953 | 2025-11-15 00:18:00 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5fcde14-6c1f-37d3-9164-32366aae0277 | -11.8271 | -49.205601 | 2025-11-15 00:18:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec3fa80c-d1b9-38ef-b8b3-18f0520ff575 | -3.2216 | -45.468498 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9dc8efc8-fba8-39c0-a9c3-b62d1f314da6 | -7.8806 | -48.4039 | 2025-11-15 00:18:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1b60866-68a3-358a-b4d5-fb06f7a7b65e | -3.2117 | -45.470699 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d4a72ce7-5dbe-346f-bc1f-38a5966d68b7 | -4.8519 | -43.258099 | 2025-11-15 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 905fb7ec-7857-306f-8580-6d436cd24e70 | -11.8334 | -49.186798 | 2025-11-15 00:18:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d661bafd-c2d8-30df-885d-0711c488d1ee | -8.589 | -46.088799 | 2025-11-15 00:18:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f655319d-b05d-3da5-a285-e4eaab4c48f5 | -2.74 | -45.298199 | 2025-11-15 00:18:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff62044-abf2-3a36-aaec-78768e1076f2 | -4.5228 | -43.216301 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2d7d3de-1ed6-392a-809b-e67bb5c284dc | -6.2818 | -41.755798 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 125aea26-6ffc-3414-86f8-8250607aab9c | -4.2748 | -45.528702 | 2025-11-15 00:18:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81c7fb23-868d-3194-bfe8-5c3537d67622 | -3.225 | -45.483799 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb7a6322-50e7-3a66-9d2e-5791b11da200 | -4.5295 | -43.200401 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d618822-f866-3c14-bbce-36ff7bb62125 | -10.4411 | -45.0802 | 2025-11-15 00:18:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3531c28-92eb-3440-b15c-1dba77b22970 | -4.4203 | -43.354401 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79796836-ee0a-327e-b034-abe5a8e98ea5 | -3.39 | -45.439301 | 2025-11-15 00:18:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64ccabcc-1bba-3a1c-b42e-de055e6fed06 | -5.5378 | -42.6945 | 2025-11-15 00:18:00 | METOP-C | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db65088b-0a58-3a02-8190-398afde92a23 | -6.096 | -41.710499 | 2025-11-15 00:18:00 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 125dfa90-25f9-3f55-b9ce-d0444bdada4d | -12.2385 | -49.393002 | 2025-11-15 00:18:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc5bffc9-123a-3b52-8434-46cbf5b63cbf | -6.6766 | -43.762199 | 2025-11-15 00:18:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a22138b5-030e-3cd4-880f-daf3f568c1cc | -8.302 | -46.229801 | 2025-11-15 00:18:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4a9cb31-f808-3dbc-9eaa-1a1629b5671f | -4.7233 | -47.162701 | 2025-11-15 00:18:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9c70a46-4885-3e40-8486-4f9df482bdc7 | -6.3231 | -47.256001 | 2025-11-15 00:18:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75cf6b48-249d-3080-8bde-87b36728e524 | -4.6021 | -41.7635 | 2025-11-15 00:18:00 | METOP-C | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 35d8c06d-0682-3ef6-a738-6c1762def074 | -12.6648 | -46.762402 | 2025-11-15 00:18:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9759ae37-3b9d-3152-9569-751fdb028f1e | -6.7112 | -42.958698 | 2025-11-15 00:18:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b5860a7e-cc8c-3618-b1c0-60b3730d7e67 | -3.978 | -44.2635 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38df818d-7e38-3e17-af9c-f3bb365c7030 | -5.0365 | -43.6161 | 2025-11-15 00:18:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 467398ad-e16d-368a-9aee-e7e41985b96b | -6.4106 | -41.464001 | 2025-11-15 00:18:00 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8ab82c54-1c30-340e-9d91-17ab2ba519ea | -7.442 | -42.7733 | 2025-11-15 00:18:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f055f029-e52d-3c31-873d-495d743d365f | -6.2802 | -44.747002 | 2025-11-15 00:18:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25df47ed-5457-3479-a3b5-82d4da784ef1 | -5.5196 | -41.760799 | 2025-11-15 00:18:00 | METOP-C | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd19836c-9541-3d30-bedd-7227462b7fef | -4.4002 | -44.080898 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d10d4081-edcb-3dd7-b3aa-8db3abdb54b9 | -6.7241 | -42.970299 | 2025-11-15 00:18:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5bb0d5bc-b065-3d8e-ab9f-99bd3b2176a3 | -4.0539 | -46.420799 | 2025-11-15 00:18:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6514ce86-bdec-329b-a290-86a98b3edbb7 | -7.2687 | -48.027199 | 2025-11-15 00:18:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31fdbc56-a211-3bbd-815e-f7904dc4e9e6 | -4.3622 | -45.460201 | 2025-11-15 00:18:00 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
