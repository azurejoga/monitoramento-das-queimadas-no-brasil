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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41277500-155d-33aa-a4c5-42ccdca5a822 | -13.08331 | -54.84509 | 2025-10-11 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e806096-ae12-3277-b536-59e63cfc1ce6 | -15.21938 | -56.74103 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fffd6f26-c672-3d47-9f1a-d43974f3ebe9 | -15.19188 | -56.7844 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0d8abc5-d9c8-38cd-a074-b72edc606e4b | -14.99 | -45.56285 | 2025-10-11 05:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1f409b9-68bb-325a-8825-3ab4178b9a90 | -16.29887 | -47.16529 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39c72337-e86a-391f-b9da-d9e0c4b423e0 | -17.26225 | -46.90205 | 2025-10-11 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 063491a9-c7c9-3f47-b1f0-4110c23caffc | -15.16151 | -56.83133 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e4d23ca-90d9-36df-b33a-8b47fb025a2c | -14.98465 | -45.55786 | 2025-10-11 05:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbbbf133-52eb-3122-87b5-8b4732f4e7f0 | -15.01558 | -56.01976 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc37c802-fecc-32f0-9038-601fbffe9b67 | -12.08992 | -63.86034 | 2025-10-11 05:04:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f9f9448-1a0a-3b95-8fcb-4d3bf32fde09 | -17.84636 | -57.57862 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5d813a71-c99f-36fe-a7db-97cffa23c547 | -14.9524 | -46.74442 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a97e0fde-d35c-3a28-8ce2-31d9033eef72 | -13.59791 | -56.93567 | 2025-10-11 05:04:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1b7dd2e-be8c-3d7b-b559-daf3b63b6335 | -15.19348 | -56.79575 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c1d4548-3d39-3ee5-a250-e4ad92260cdd | -15.68823 | -46.63981 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 697a7633-fc1a-32e6-a3ef-8d6d423a6b18 | -14.43851 | -50.34677 | 2025-10-11 05:04:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2314d31-3eaf-3cf9-92af-ccc39f654b41 | -16.75918 | -56.28886 | 2025-10-11 05:04:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 584b1271-c989-3d49-832a-4bdbef348ddd | -12.39653 | -63.70617 | 2025-10-11 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbbeb423-47dc-362c-b0ec-1bc3efabf2ec | -14.95582 | -46.75232 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 459e8b48-e4da-3505-a433-0c3788fd6dc3 | -12.40053 | -63.95733 | 2025-10-11 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a403eba9-9e60-33ad-a927-35a7580745aa | -15.19028 | -56.77304 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97a227c4-851c-3066-a5a3-a1d03dc32fc2 | -18.0782 | -57.54751 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b91622ae-6d20-3ed6-a11b-9b2f73ecc8d4 | -15.22634 | -46.38786 | 2025-10-11 05:04:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 104b74d1-092b-36c4-809e-bb150c4c133b | -14.94102 | -46.74778 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8e8f7a6-42a9-3bb1-b7d9-2332023ecda2 | -18.07387 | -57.53163 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f1ddf4bd-5ab9-3925-aa76-f6da469d072c | -15.19306 | -56.86229 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9221b0a1-787c-3504-8089-068c5994257f | -15.69531 | -46.6277 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9e92aa1-6902-3a30-9137-edd88c8aaa74 | -18.06491 | -45.00848 | 2025-10-11 05:04:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e550fb75-6ab6-3086-ac8a-1147512a537e | -15.69441 | -46.63601 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0b9e5f0-8d9b-3f7f-a242-b7e7d885cdf2 | -15.69769 | -48.39845 | 2025-10-11 05:04:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f6369f5-a781-31d6-a72d-d55cb7a0fca7 | -15.1726 | -56.84032 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a82158e-baa1-314b-97f0-0e5521bb5b35 | -15.18755 | -56.85395 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33500405-de7c-3353-9cb5-3934211e6788 | -12.39427 | -63.88176 | 2025-10-11 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2643c218-998e-331c-bb9c-b275c15f5a42 | -14.95159 | -46.74173 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78fe59c4-9107-330b-a717-8166106cebea | -16.01568 | -59.54409 | 2025-10-11 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc646411-9800-38e0-93ff-c8f02c204533 | -17.21888 | -47.65539 | 2025-10-11 05:04:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e822b57-002b-3323-b1af-9eb29920639a | -11.84001 | -63.71167 | 2025-10-11 05:04:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce1ae645-7a5e-313b-af06-6e297c578930 | -15.1676 | -56.83605 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e138c474-b8a7-31c2-8ca1-e3b78c735305 | -15.18173 | -56.8049 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 953b372a-57b0-333f-8515-0350c808083c | -17.90384 | -57.66046 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8d08806f-5676-3821-a5eb-0aee2d7f16b0 | -17.90718 | -57.66106 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 817362bf-79d0-3e9b-8dcb-21cd457488d0 | -18.06542 | -45.00326 | 2025-10-11 05:04:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3586d61-78a7-3d02-9e68-2b802138ed74 | -14.95541 | -46.75568 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fd33d25-b997-3797-9cee-50d0277b3a95 | -18.0727 | -57.53896 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 127e479d-1d4e-3acf-ab8f-f34b9248f268 | -14.28166 | -45.89733 | 2025-10-11 05:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cf0f3bf-3504-3cf6-b831-20f7d081cb6c | -16.01435 | -59.54459 | 2025-10-11 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab5ab0f5-9202-315f-a8b2-02397bf54944 | -16.30457 | -47.16295 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 512d27d1-fe03-3e40-a225-91fd6f90ad9b | -15.01104 | -56.07045 | 2025-10-11 05:04:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7e4802d-8c82-34e4-af3e-7d88813d6a50 | -14.93981 | -46.74831 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2503558f-d792-36a3-a340-4f88ddb0db10 | -15.16542 | -56.7211 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63f1d98a-186f-32e5-b47a-46b08d5a0b6b | -18.04522 | -57.56042 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 164fd8c1-fb8b-3b37-9b7d-6d71a90b2387 | -17.81215 | -57.66273 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2fc7077f-e501-379e-952b-7fdcb4c01dcc | -15.18145 | -56.84924 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbc73d1b-94b8-3eab-8a49-afd7065348bf | -14.95203 | -46.74767 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68ed34dc-3f78-3db4-9200-23a0c5f35d99 | -10.69819 | -68.55658 | 2025-10-11 05:04:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49b68c82-273d-3d93-8aff-c4cc950311b2 | -14.92701 | -46.76363 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f096ee9d-e380-33ba-bba9-f9b67ce797ba | -15.40935 | -47.29858 | 2025-10-11 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e863e47a-26d8-34bd-aaa5-cf65c3f89e18 | -15.17646 | -56.73775 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beca9f35-ded9-3b02-b418-7bcfbb9c853f | -15.26976 | -56.90808 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f881045-db72-3d69-89a4-1ec352683acd | -17.89018 | -57.51118 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d33f6d20-704c-37c8-ada2-1afdcbf68f66 | -15.17201 | -56.84394 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f29edc8e-b027-3de7-a7cd-b167529dfd24 | -15.24156 | -56.75219 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d47083a-2b50-3b1f-a585-a0951eb10065 | -18.04462 | -57.56415 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| faf2e487-3a04-3043-9d38-46e213046d1e | -16.30994 | -47.16356 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d483d8c7-4223-31b9-a0c1-5ed26d1de274 | -15.7011 | -46.62515 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5021471b-89c6-3b33-8b45-e32e4864721b | -15.01493 | -56.06742 | 2025-10-11 05:04:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49db8d9a-2084-3c4b-91fb-d93361464d43 | -17.9063 | -57.51767 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9a042f7e-85ff-359d-abd9-b0745800f2da | -14.2812 | -45.90129 | 2025-10-11 05:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22ecdd37-5ce4-3f9e-975f-a7e80c0ddcbf | -17.21362 | -47.6548 | 2025-10-11 05:04:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9dec8d52-e8e1-39c4-a424-c112c6d92bef | -17.48477 | -43.3383 | 2025-10-11 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35ce70ec-697c-3476-83dd-889bb87eaea3 | -15.15932 | -56.82355 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb549e56-70fd-3ae5-976a-bd7c22ccb69d | -18.07211 | -57.54263 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7922e5da-5bbc-3776-9fc6-9b06d6902dbb | -15.22605 | -56.74217 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c89521c7-a8e7-35db-98d1-b5e446ca4429 | -15.11535 | -56.22707 | 2025-10-11 05:04:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1748d3a1-9fc4-3c63-a182-841890b15deb | -17.84577 | -57.58227 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f82971bf-3492-3d4d-920b-2021ff921951 | -18.04916 | -57.55725 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0e7d9651-93f6-3ac5-a86e-93b39e2cd8cd | -15.21605 | -56.74045 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5a017c5-7ea6-39b2-bb19-01e608a89a92 | -14.28026 | -45.90924 | 2025-10-11 05:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e31ec813-ffce-3ca8-9dd4-45a29012d37a | -15.20157 | -56.74538 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7665c9dd-9012-334e-830f-e984d0adc41d | -16.30651 | -47.14548 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 953f4d8a-54a3-37d3-9303-7acfeae87947 | -18.81663 | -54.96516 | 2025-10-11 05:04:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52812696-40c1-3ba7-95d1-9cc1252915f4 | -15.18591 | -56.75755 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb5ae75b-0f9f-3143-8a79-81d22b51159f | -15.19086 | -56.76944 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a389a4d0-0b7e-3344-afcc-f19d3164612e | -16.75528 | -56.29192 | 2025-10-11 05:04:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b3615528-78cd-3d39-9951-2e37bf8d7939 | -17.81942 | -57.66027 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d12cdfa2-4b12-325e-b919-a7199741e0ad | -18.06768 | -45.00947 | 2025-10-11 05:04:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81218448-1660-3d80-8d44-8491f3034fb8 | -16.75861 | -56.29248 | 2025-10-11 05:04:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 4bd4c900-9305-3b29-b178-53b8da150ce8 | -15.1897 | -56.77664 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af018dcc-2fef-3c1d-9324-1c81467ffdcf | -15.70592 | -46.6329 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e66666-2c31-3851-8470-12bfcd07efe5 | -14.98356 | -45.55953 | 2025-10-11 05:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 864e4731-f132-3859-8d6d-7fb7ab7c8f82 | -17.88741 | -57.50701 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b1adce17-61b9-3b68-b60f-0fa7b3a8a495 | -14.28073 | -45.90525 | 2025-10-11 05:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a00cd923-f685-396f-9a97-d78e385bfefb | -14.93895 | -46.75552 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7bfa390-4c3e-3c0d-8017-eb76edb25cb7 | -17.81392 | -57.65178 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bdaba38f-da3b-3080-9ee9-9ac445469790 | -17.84125 | -57.589 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2cbbd8fd-f624-362e-a950-241210432059 | -17.84734 | -57.65786 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c0603bfd-17fe-363a-98be-a2599c5a8223 | -17.90325 | -57.66413 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3d2fd759-a52d-3ad1-8fce-26c33a1842ba | -14.95632 | -46.75829 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bf8062f-4fd8-3ab6-b830-f98e2e7555bf | -17.83337 | -57.65911 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2fc69929-3eb0-36d0-a2a7-e9c739b78f89 | -15.70083 | -46.62833 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README41.md)
