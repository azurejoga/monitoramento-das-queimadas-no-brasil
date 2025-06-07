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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 727d40e9-bc98-3f42-8177-80763dcabbb2 | -10.97161 | -47.1411 | 2025-06-07 12:44:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| f647b101-a8ac-33ac-9fcc-7aa1d469ebdd | -10.44086 | -49.60931 | 2025-06-07 12:44:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d94b847c-8c1d-38c8-bffd-bc01f08e1c75 | -10.49691 | -53.66989 | 2025-06-07 12:44:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 01446a13-68b4-3c2c-96c7-c77874483756 | -10.46455 | -50.96756 | 2025-06-07 12:44:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e2a1faf7-a468-3af5-842e-5f24b19c8665 | -13.06167 | -49.24964 | 2025-06-07 12:44:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5d12037e-a74b-35f6-9674-f2b878c79ba6 | -14.68754 | -54.34054 | 2025-06-07 12:44:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4b2d12c5-b22b-3f31-8157-393ecc482cfb | -14.03876 | -55.13601 | 2025-06-07 12:44:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 870355ae-a6da-3af3-86fc-313658311add | -11.54523 | -56.4397 | 2025-06-07 12:44:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| a528a387-c412-36d9-8315-dec3521fe0be | -8.45569 | -46.4913 | 2025-06-07 12:44:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0a256b56-40ec-337b-98cf-f8cffe9a960c | -7.73085 | -44.16611 | 2025-06-07 12:44:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 8107b61a-83fc-39ec-b97c-7cb905b97bd5 | -8.79016 | -45.08425 | 2025-06-07 12:44:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 9459e758-c6f4-37ae-bdd8-75e9aa3269b5 | -12.54357 | -45.4027 | 2025-06-07 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 6bf4a7cd-2320-3291-b907-e5f8672cd4a1 | -6.9624 | -42.88698 | 2025-06-07 12:44:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 5fd271be-8f19-3ae4-8374-947a6b57d8ab | -13.72805 | -45.27026 | 2025-06-07 12:44:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| ff8fd0af-e674-3881-80b2-ca5476681764 | -8.7894 | -45.09814 | 2025-06-07 12:44:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 0f9c7230-91c8-381b-8e14-be3c449b0238 | -9.06735 | -47.15586 | 2025-06-07 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a4ffcbc8-9f4a-3e94-b40c-9162c81d7653 | -10.30113 | -57.14674 | 2025-06-07 12:44:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4e1280d0-24cb-37da-a3e4-641d54f3eba9 | -14.59674 | -49.99777 | 2025-06-07 12:44:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 52f18cbc-a67c-3145-ace8-630e0c5e8aba | -10.88015 | -54.31487 | 2025-06-07 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 1c676124-7f97-31bf-b834-e2dbff743c30 | -7.72404 | -44.15977 | 2025-06-07 12:44:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 05cdf863-ecc6-3fe4-8720-703a3b6f7969 | -9.49764 | -47.39121 | 2025-06-07 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f71f9f8a-680a-3ef1-a164-eb820bf227d5 | -15.37309 | -48.17521 | 2025-06-07 12:44:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| d58b5948-7830-3cfc-b3d4-2a9bb4c5f21a | -13.47679 | -56.85245 | 2025-06-07 12:44:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c95ff13f-dcff-31d4-b8d4-8a7abb2d572a | -12.28573 | -50.10584 | 2025-06-07 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 84ab2bcf-d5ad-380f-80ce-67d9b2c62c5c | -10.44226 | -49.59896 | 2025-06-07 12:44:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 36656d52-1862-3116-a207-71994420b47d | -6.55073 | -45.32421 | 2025-06-07 12:44:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 4fab063b-1767-36ed-a42d-028d4579b332 | -11.90545 | -47.44917 | 2025-06-07 12:44:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 1f4386fc-775d-3f2e-9dd5-81299e568d36 | -9.50853 | -47.39263 | 2025-06-07 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d81e61d9-d608-333c-9cc8-f433afaca423 | -7.73472 | -44.18476 | 2025-06-07 12:44:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| fa09a34d-57c7-3e03-ba6f-66fedc2386db | -7.6927 | -46.2888 | 2025-06-07 12:44:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 0cdc216b-7c11-3eb6-8a66-af6a419606a6 | -10.40538 | -47.00099 | 2025-06-07 12:44:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 457ac554-d3a3-3e20-959a-cb0a09bb5e91 | -12.29551 | -52.47304 | 2025-06-07 12:44:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 51b28e75-f383-3105-854d-d37a8e476323 | -6.23297 | -48.5479 | 2025-06-07 12:44:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eafc0179-7501-3943-817b-b44fbf487c12 | -14.88908 | -48.11059 | 2025-06-07 12:44:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d8c57567-9f1d-3b3a-8843-30d8d6eba9a6 | -13.89134 | -54.66593 | 2025-06-07 12:44:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 5549ba4f-6288-3970-be01-c22613cbc3e1 | -7.12705 | -43.65586 | 2025-06-07 12:44:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b8cc1d11-6acc-3302-b276-5e404c09d794 | -13.52399 | -56.56424 | 2025-06-07 12:44:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d8fee5d7-b97f-3cd8-b064-634e1ca97c87 | -10.40345 | -47.01627 | 2025-06-07 12:44:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 613cdac6-3b9e-306e-9c89-3d33dd20c3c7 | -14.59528 | -50.00905 | 2025-06-07 12:44:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| da851ac8-9072-35ff-aa38-5fcfb36f1030 | -11.78498 | -47.40631 | 2025-06-07 12:44:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fe0b5351-5c55-388c-a0f3-9b40d5862649 | -13.47443 | -56.56342 | 2025-06-07 12:44:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f0456632-2a3c-333b-88ff-0690d799d8bc | -9.54144 | -50.78556 | 2025-06-07 12:44:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 5455a2bb-bf82-37fa-b480-c21f8aedd2fc | -10.88322 | -54.29457 | 2025-06-07 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2af5204e-52a2-3949-9b03-d0bd81365cb2 | -12.28711 | -50.09553 | 2025-06-07 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| abdc5f7e-05ac-3a77-8e9d-686b7c0e0465 | -9.07023 | -47.14833 | 2025-06-07 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| ca48967d-77ec-340d-a2c9-b1883348c032 | -10.88169 | -54.30471 | 2025-06-07 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ec2100fd-56d3-3bf2-ab8c-1d3789425756 | -7.36679 | -46.8525 | 2025-06-07 12:44:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 83515753-6e60-38f2-95ed-dca5947d49d0 | -14.87784 | -48.10954 | 2025-06-07 12:44:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a3b2b03d-f018-3ad7-b743-c988ca35cbf6 | -7.02858 | -44.58566 | 2025-06-07 12:44:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 41c7f1f9-f769-30be-8fd0-9b5b04faddd4 | -10.96023 | -47.13972 | 2025-06-07 12:44:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 33192945-5016-3ef3-9376-1d5e26d55b84 | -7.1203 | -43.67369 | 2025-06-07 12:44:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 41.3 |
| ac72908f-41e6-3886-826c-3afcda51a17f | -9.07204 | -47.13404 | 2025-06-07 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 71ba0945-c546-3be4-8fd5-62c2b9bcc755 | -12.54095 | -45.425 | 2025-06-07 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 0651e4d9-33a4-3b8c-ba3b-62cd5f6ee00d | -9.54273 | -50.77639 | 2025-06-07 12:44:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| fc771496-2047-3d0c-b36d-a21b2f6cf945 | -7.74469 | -44.1671 | 2025-06-07 12:44:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 7f6df74f-ccde-32e1-9611-a7a1dc14e0b3 | -13.71686 | -45.24516 | 2025-06-07 12:44:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 4a6f92c3-7af1-3553-b926-b7d90bef5597 | -13.73074 | -45.24642 | 2025-06-07 12:44:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 967286c3-aac9-37da-bda0-433007c7554c | -9.08028 | -47.14314 | 2025-06-07 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c0cd9ec2-5cc5-3b83-913f-e24057228494 | -13.88984 | -54.67583 | 2025-06-07 12:44:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 93fb0b71-2ab2-3473-9dcb-6554d3afbb40 | -9.12568 | -46.89072 | 2025-06-07 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 994f2ba1-2a47-3c08-a550-d85a3055762f | -6.93983 | -47.78304 | 2025-06-07 12:44:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8f1be5d9-5316-32be-bd19-c3551d13c660 | -6.55409 | -45.33129 | 2025-06-07 12:44:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| d44e85fd-6df2-3b41-8345-362c29f02391 | -7.36514 | -46.84631 | 2025-06-07 12:44:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 93bbf175-7b84-38eb-bc9e-b0be64054a83 | -11.37576 | -56.5532 | 2025-06-07 12:44:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 162.6 |
| 7278af89-f711-3a64-90bc-e7343009d005 | -7.73787 | -44.16087 | 2025-06-07 12:44:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 516b4fd5-e119-3262-9059-eef1087b1904 | -7.02552 | -44.5921 | 2025-06-07 12:44:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| a5ae8407-aab2-39b4-9ed6-4db1acaf6a2a | -6.95894 | -42.91552 | 2025-06-07 12:44:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 9e51d7e0-1884-3b12-b3c9-e6c2fff64406 | -9.50624 | -47.38646 | 2025-06-07 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bb9a31e0-4a74-3ec3-9bee-d1c9ee139789 | -14.90021 | -48.11254 | 2025-06-07 12:44:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1fbd1b5a-b741-3da6-9074-a7d6aba86ccc | -14.14295 | -49.1614 | 2025-06-07 12:44:00 | TERRA_M-T | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b97613ed-ce31-3e39-aaa1-728a94cbc3ab | -6.94147 | -47.77109 | 2025-06-07 12:44:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| db3c8f29-dcc0-3c7c-9ee9-8c1414758883 | -9.06925 | -47.14174 | 2025-06-07 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f7fcbade-80ce-3042-99b2-462822741166 | -6.54829 | -45.34232 | 2025-06-07 12:44:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6de5f1ca-044a-3b16-b59e-7b17eb8a400d | -12.5236 | -58.35509 | 2025-06-07 12:44:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 7d3b4f1d-135d-3317-9254-bde0514fcea3 | -13.37113 | -54.25656 | 2025-06-07 12:44:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 50d39862-9aaf-3d06-91c1-8d5b06b1d1df | -7.36859 | -46.83858 | 2025-06-07 12:44:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ed9b5088-33a7-3b8d-8d60-df37fd229ac4 | -14.02932 | -55.1345 | 2025-06-07 12:44:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5219ea96-d99e-360b-900a-ea662ad42ea4 | -13.47281 | -56.84578 | 2025-06-07 12:44:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0d5a1743-8328-3360-93c7-b068e31bc009 | -10.8723 | -54.30329 | 2025-06-07 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5781a7b1-cfdd-337e-a16f-1dab68c80e41 | -10.49835 | -53.66028 | 2025-06-07 12:44:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 3ba9580a-93df-3a41-b1eb-a3be2b463217 | -6.28828 | -48.50143 | 2025-06-07 12:44:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b796748e-3d12-39b5-b6b5-1fe26ca9b11a | -11.54308 | -56.45314 | 2025-06-07 12:44:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 889b9eff-da76-3eb2-b53b-c6a5dcd53bf0 | -6.96009 | -42.91013 | 2025-06-07 12:44:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 0b7e3cd8-9b97-39d8-8929-ad7d44f98d93 | -9.50436 | -47.40033 | 2025-06-07 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a37d99f9-b7ed-3f0d-aa01-b8115aab24db | -7.12402 | -43.68081 | 2025-06-07 12:44:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 58f641ad-8c02-3ed1-89c5-ad87e24d16e4 | -8.7877 | -45.10442 | 2025-06-07 12:44:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| c4302d62-8fce-336d-9bcf-b290e99affff | -11.90359 | -47.46407 | 2025-06-07 12:44:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 20df325f-d44c-3820-9e1a-617a39289ffd | -11.78583 | -47.39744 | 2025-06-07 12:44:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7500a1b3-dde1-3532-93ee-f88a66023ab8 | -13.75737 | -58.59336 | 2025-06-07 12:44:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| fb6723f6-a754-367d-bbe5-76ea7e3318c3 | -7.01264 | -44.60531 | 2025-06-07 12:44:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 21778e29-4355-35e7-a40f-055fcee4565c | -17.26093 | -49.12378 | 2025-06-07 12:46:00 | TERRA_M-T | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 390b04b5-b696-351f-94b7-6385a8253fba | -17.256 | -49.13063 | 2025-06-07 12:46:00 | TERRA_M-T | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 28.3 |
| fa2da0e6-9588-387a-812c-9918c2b0e83b | -17.25929 | -49.13762 | 2025-06-07 12:46:00 | TERRA_M-T | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8b9e134b-ae7d-38c5-b1a7-7c1865f3c2ad | -19.84639 | -51.20424 | 2025-06-07 12:46:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 21.5 |
| e272d5c9-dff0-39e3-b5a9-9b1a3dc890f5 | -19.55028 | -47.75414 | 2025-06-07 12:46:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 8fb8153e-7f32-361a-9f8b-4edf4ce65633 | -19.84782 | -51.19285 | 2025-06-07 12:46:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 335de7fb-af03-3696-ba94-cd2299df226d | -17.61796 | -44.63368 | 2025-06-07 12:46:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 46.2 |
| aa9a9a6c-a8ca-3bbf-a16d-4cec8513b283 | -17.80996 | -51.00746 | 2025-06-07 12:46:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |


