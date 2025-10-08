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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd82220d-48e3-3143-bef7-bb7a119896ec | -17.94535 | -57.50672 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cb939b35-9b2f-3f0d-a9e3-6b5c1955a339 | -18.08175 | -44.45826 | 2025-10-08 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 819d9f1e-dfff-3da9-9e8d-e76c0bd47ad6 | -7.03039 | -47.90989 | 2025-10-08 04:19:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 712d32fa-717f-3346-b901-51f2b25495cc | -16.00046 | -50.82347 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20567a62-ad2b-335b-9e98-8e3eaceb3d26 | -7.82286 | -44.14876 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee729569-61ab-3e2e-aee3-58c1d0922a94 | -17.38051 | -45.06148 | 2025-10-08 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2586721-0bb7-38dd-b533-497967598ccb | -17.45407 | -43.38796 | 2025-10-08 04:19:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce38d913-9838-30f1-9598-ea2429a72002 | -16.76438 | -43.97795 | 2025-10-08 04:19:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4d22bde-ab00-3d0b-bd28-925a158304a3 | -15.97556 | -42.97879 | 2025-10-08 04:19:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15b64742-c6e0-387a-a4bf-60cf1f9242d4 | -16.07775 | -45.77545 | 2025-10-08 04:19:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c37b7813-9991-380d-a500-b83b082dad18 | -15.78062 | -46.25294 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5494201-670f-33a7-9ac1-886a0440130e | -17.93844 | -57.50939 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c566e1c9-d57f-3cd6-b40d-2d8d33d4b663 | -15.37812 | -47.30866 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48946b9e-cce1-30e6-9282-93f530145d32 | -15.80192 | -46.24911 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d520548-4acd-3eab-9008-f3a10620ef5e | -9.20107 | -46.89956 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 103fda44-4cae-3fbb-bde6-d15ff52f1f96 | -17.29999 | -58.07548 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3d1ace9d-364e-3529-904e-8661c6685d93 | -16.13793 | -48.23751 | 2025-10-08 04:19:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42e179ab-e6f7-37a1-81ba-5858fa7b1e18 | -14.14663 | -43.17625 | 2025-10-08 04:19:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 659282cd-17a6-3db9-9df6-d3e0c37d0999 | -8.15353 | -54.84981 | 2025-10-08 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d385165a-fb5d-3d66-828e-2dbf1fed3146 | -8.68089 | -44.72543 | 2025-10-08 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 478e3021-6fc8-3a6c-84a7-b02249d4ef25 | -15.24585 | -46.36145 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d872803-98c4-36f8-ac09-ee0a15ab9cc3 | -15.99175 | -50.9638 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e07e34c9-8290-3941-b6cb-3a993deb67b5 | -15.37187 | -47.30364 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9fff22bd-2e8b-34e3-b667-ff657af16f08 | -7.65316 | -43.89896 | 2025-10-08 04:19:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1d872e4-ffb2-3c1d-9f49-961d492d988f | -17.27242 | -58.12009 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 989f23dd-658a-3be9-88d4-a025dc1284a9 | -16.14147 | -48.23817 | 2025-10-08 04:19:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1515cd2-7103-39d1-9cdc-de32a585714c | -17.83254 | -57.64264 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a1df7f58-96e8-3a89-81d6-c7c533eabbec | -14.95903 | -46.82886 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6aec309-a3e6-3704-b696-2f82f14687f0 | -13.7383 | -45.72306 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7961f593-cf94-36d2-abd9-c8ced4e547d1 | -8.52122 | -46.23313 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0f1b07c-e11e-3461-8322-dc976f537f80 | -18.07891 | -44.45405 | 2025-10-08 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2c040924-91e6-3133-9d2d-b5bc4651a8e1 | -14.71032 | -46.06106 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b781abf-9cfa-3cb9-9dff-79ba93b4666a | -8.47571 | -46.29184 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6d6194db-22f5-3042-bdee-14893c6a0834 | -15.25255 | -46.3628 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 193e6e47-af79-3843-b0d6-3f39b2bb0db8 | -13.29843 | -48.03352 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 01c6fdfa-e556-3e26-955f-68b24a07afce | -15.3155 | -46.16683 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d083c4f-21c0-3401-aff3-9e62420b9e65 | -15.39691 | -48.00481 | 2025-10-08 04:19:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ade1fb16-fcae-344a-8d3c-57ed1b1cf2ab | -14.52536 | -46.64009 | 2025-10-08 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d42d2e0-6cfb-3ecf-8b9e-48db6b7cc920 | -8.26611 | -43.8283 | 2025-10-08 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a2e1a0e-d7f0-3638-8456-9e5b3ab9e0f4 | -15.56018 | -46.85015 | 2025-10-08 04:19:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68ca567c-f21e-305c-9852-96d5292b04e8 | -7.78547 | -44.21117 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6381ace3-6738-3dde-891a-d0254f450f83 | -21.35483 | -45.41767 | 2025-10-08 04:19:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d323246e-7333-3308-90e2-47d0c5bd402c | -18.65092 | -43.90882 | 2025-10-08 04:19:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 965e77eb-9ec7-3f11-b9aa-3a67e3c2397e | -9.18515 | -47.80082 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a3c51709-55f1-3c7b-9256-006a907811e8 | -8.53605 | -46.23119 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d21c1565-873f-3719-acc0-dcf9f4bdc818 | -13.30544 | -48.03303 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ce31992e-83bc-3b8a-b6b3-e3a5244ec6cb | -17.99822 | -44.9825 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6515a26-a790-3aa4-a23d-35d867b9dd72 | -14.91647 | -46.81051 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7fcd3d52-1d54-37d5-98a7-a4845b01316b | -18.05938 | -57.53553 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7225b18c-11aa-3255-ae62-b10f212ff521 | -14.7005 | -48.40076 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 391e7093-72e3-35e4-9d62-2fc32aa4cdbd | -18.04259 | -46.43812 | 2025-10-08 04:19:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7be2a5c-4977-314d-bc5f-9361e4b70170 | -8.2265 | -44.16267 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9fe4a8a2-227c-3b6f-aa0e-915fd0f01e20 | -20.39232 | -43.07193 | 2025-10-08 04:19:00 | NPP-375D | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 506be521-338d-3844-9ae5-ba0007a21905 | -15.31214 | -46.16625 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6590a11f-d22a-3d9b-a17d-cde551aca75f | -17.16723 | -56.60459 | 2025-10-08 04:19:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 100bda6f-2dd9-32b6-b426-50b17232ae1e | -18.19583 | -43.04776 | 2025-10-08 04:19:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 94a457b6-dc87-3151-bddd-e7568d33b3c1 | -18.49761 | -42.90168 | 2025-10-08 04:19:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 05bc869a-e6e0-3268-9bba-40f449799fb9 | -14.71242 | -46.00531 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ab428124-1df7-3c86-94f0-71cc7c049238 | -20.5934 | -45.15622 | 2025-10-08 04:19:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3283a5f2-2559-3c01-b00d-3a15127361ce | -15.06918 | -46.62799 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78b81c63-49b1-3c65-976d-9e4e85d27619 | -8.92088 | -46.58875 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18856560-c5f7-3c20-93cf-1fe76ae613e9 | -17.92407 | -57.51722 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a8597c5f-3956-350a-bf78-6762b0047a6c | -7.80496 | -44.21788 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ac2ff75-262e-3590-b844-f3c52ce0d620 | -15.3673 | -47.30008 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f50d507-d37d-3ed4-81f2-a1ab50304ac7 | -9.29918 | -45.6521 | 2025-10-08 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f740d0f-7f84-358b-a4d1-9c73bb049dcd | -13.38172 | -47.56952 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 010ffe81-359f-3fa7-bd17-751e3203266f | -16.58456 | -46.55242 | 2025-10-08 04:19:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4582a6e2-be37-3743-a0d2-e209205b2d15 | -18.02459 | -44.94531 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b6530a6-803d-3f9f-8eb3-d3979818db48 | -7.0281 | -47.90783 | 2025-10-08 04:19:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6eda6d3f-9aa1-3dc6-9c22-9773ab0e65f3 | -20.26657 | -43.25727 | 2025-10-08 04:19:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1da00405-e6c6-3ff0-9dce-01d368cf5df6 | -16.27317 | -47.12364 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b73c8e33-d94a-315d-b2b0-cbcbe671225f | -13.38591 | -47.56639 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef03fea2-05e1-3e0b-b0aa-71c31ed018ac | -13.2063 | -51.69271 | 2025-10-08 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10ef4a6a-7987-3a33-b2dd-593d3e26eb00 | -8.51482 | -46.29334 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82ff1a24-7f76-370e-87a8-2fa7856cd31d | -13.80733 | -45.79755 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0673ec90-bd7e-3d97-8108-1cbde3c4bab7 | -15.99634 | -50.82279 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0659e934-c2a2-3571-abfc-d5abc94b749a | -13.84747 | -51.86311 | 2025-10-08 04:19:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b13ab53f-d612-3096-8338-e02e804762dc | -19.85145 | -46.1676 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1d62a1c-ae79-33f6-af1b-152bdffb836e | -20.20082 | -48.7047 | 2025-10-08 04:19:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f498dfb5-3b7c-34cf-b5bb-68dbf0da9d8f | -8.37562 | -47.05543 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a1f6286-1113-32cf-8915-a0e924124fa1 | -15.95157 | -42.59932 | 2025-10-08 04:19:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 01da106f-f15d-37c1-b48e-c8886a461d85 | -15.36689 | -47.32402 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec8cac7e-f8d5-31a7-9e2e-b161a81fc449 | -17.99766 | -44.98615 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7474e6cc-dd05-305f-9647-70d7f07718c6 | -9.17742 | -47.82354 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 262014de-a595-3247-99e9-71efa70c3302 | -7.80936 | -44.25471 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adf4711e-ca8e-362f-9fa0-cfa36175fd18 | -20.38484 | -44.44427 | 2025-10-08 04:19:00 | NPP-375D | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d5e96a71-8e7f-3723-95b4-44f883d97e2e | -15.66735 | -43.65194 | 2025-10-08 04:19:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4c25c55-5701-3f20-943e-b1b9e5530cb8 | -7.81114 | -44.1792 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34794b94-c4d4-386c-9462-7d2b731fff8e | -18.07331 | -44.4682 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19b27278-525c-3114-915d-d7d4385b3465 | -7.78604 | -44.20765 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e3cccb9-84d3-3de5-907a-c6c5cfd4b55d | -15.31668 | -46.15952 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbb118ed-d199-3343-ad12-399edf42be81 | -17.94461 | -57.51159 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 235e904a-72cc-3109-8d0b-154b30f46ede | -16.33277 | -47.06037 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96459f18-64ce-392f-abe4-6811f345ed8a | -14.95471 | -46.81266 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f042963d-983a-3c89-8120-a3b41d08c783 | -17.96776 | -48.553 | 2025-10-08 04:19:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d2be2754-5dea-3356-acf1-0233acfe999d | -8.558 | -44.62527 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 152a61e2-1d5b-3cb0-9731-544d1ecf3490 | -20.00077 | -45.29225 | 2025-10-08 04:19:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9299179f-7c72-3497-aa1f-3b205009eb03 | -14.93048 | -46.78964 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ec6e899-43d7-3bb4-a82c-a8ce435c9545 | -18.65841 | -43.90603 | 2025-10-08 04:19:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e012f9e0-3788-388c-9aed-a817af92ba89 | -18.06367 | -44.46305 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README56.md)
