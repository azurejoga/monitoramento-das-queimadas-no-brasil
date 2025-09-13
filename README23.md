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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dfff1c9-661c-3fca-9286-4f7a6524deb0 | -20.44667 | -46.45825 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11f55079-a58a-3dd2-a8e9-fed284a8b5d9 | -7.50209 | -44.68152 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 212f3ea6-545c-3a1d-b553-1445bad71693 | -10.77094 | -41.339 | 2025-09-13 03:47:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bca77d2b-8fe4-315b-8c40-82f14d3d98e4 | -9.8576 | -43.13299 | 2025-09-13 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fbbb9f0e-89d9-35ec-81e9-5f333d8f1643 | -17.96152 | -46.93746 | 2025-09-13 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a36aa7b1-b550-350c-8d26-1563a72f83c7 | -19.65472 | -45.86192 | 2025-09-13 03:47:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30b5a7f4-7a95-313a-8b49-d72986368894 | -8.94704 | -44.44707 | 2025-09-13 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24b567c1-33e1-33fd-bde2-b2c96dea8e18 | -19.3317 | -45.11191 | 2025-09-13 03:47:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 89b70f5e-a100-34ea-98be-cfe02c619f3d | -14.29555 | -46.07274 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 479d74cc-b036-3576-8690-c9a79bc78e91 | -13.89248 | -48.28876 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 800576ee-3714-3530-b0bd-16550eca21f7 | -11.4902 | -43.69799 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef33f437-414f-3a42-99d6-9676f4a8f426 | -9.71596 | -48.32567 | 2025-09-13 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83312849-316f-301a-855c-da0f821b213a | -17.28761 | -47.24879 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75e855e1-7f30-3f14-8454-e31a426a05b8 | -10.79277 | -44.78198 | 2025-09-13 03:47:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b3dd4c7-36dd-3b95-aee0-70bdea4f3b8c | -16.52735 | -51.75214 | 2025-09-13 03:47:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f41cdf1-9ac1-307c-9ba5-972cadd145a8 | -16.33105 | -51.53593 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a9f61dc-466e-31f9-9cca-679f974e7878 | -17.42143 | -49.25761 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d3714a6-5021-3ba0-8f73-7561ede34dbc | -19.65373 | -45.86684 | 2025-09-13 03:47:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5d9e9e8-86f1-332a-92e5-c8aa847b4970 | -14.2864 | -46.06423 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cc14be1-5e48-3884-8e53-2928bc616504 | -17.94651 | -45.26818 | 2025-09-13 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49f703bb-7e95-3bcc-8216-2f7f67bc479c | -13.90732 | -48.21681 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| feb4681e-93d8-37ef-a2fc-f5501cd5edcd | -13.88495 | -48.26431 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f96d284c-c682-36f5-b298-39937d1e4452 | -14.21614 | -46.28647 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 5d3f4169-15da-385f-99d0-5b3656543caa | -11.13774 | -50.72109 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9d0984eb-0fa5-3884-8e77-a2a354ffa344 | -7.5583 | -42.65915 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| de6ef708-a226-3b5c-99db-84535d3aaf5f | -20.34025 | -46.67107 | 2025-09-13 03:47:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 614afda9-4abf-3b9d-a3a3-d991a84f299b | -17.28306 | -47.24386 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff347cc3-44e5-390e-a469-f33ffb9fd442 | -12.89287 | -47.94757 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 485f671b-d52e-3b96-a71f-f2b139be6d46 | -19.2541 | -51.43391 | 2025-09-13 03:47:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c57c1ae6-5bca-3fc5-b9df-60a41556fef5 | -12.12414 | -44.83631 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c840b8e7-b511-398e-b386-969155851efb | -12.10898 | -44.88388 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6b242de-0604-3380-be3f-917301da64b3 | -12.10879 | -44.89089 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fde2b97-3c26-3f10-b4a7-4f59ba390968 | -12.80663 | -47.99722 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 762a72d7-1e99-3d70-8ac0-f87d8fbb79ce | -13.08144 | -48.26617 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 41b258ae-af9c-3402-90b4-f6c8f9cc0c6f | -17.44136 | -49.25271 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ffd258b-3901-3e3f-b44d-3d242ade5e91 | -14.21666 | -46.2557 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b7afd997-53ea-3bd9-b1f2-7a079b7560dc | -20.01803 | -47.63773 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6293dc6f-da28-3bca-be25-af911012009b | -10.35961 | -45.39872 | 2025-09-13 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5496534a-3031-3f5c-9495-e880795be0c1 | -11.18757 | -48.3575 | 2025-09-13 03:47:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4398fece-adc8-35c4-90bf-ac1f3ab15f7a | -12.12529 | -44.8301 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95065118-bbb2-3174-9381-28e2dd3229e8 | -7.98001 | -43.65944 | 2025-09-13 03:47:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 828edb7e-c950-36cc-9d35-ebf7e52bfb20 | -19.26197 | -51.42998 | 2025-09-13 03:47:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9579cd6-22f2-39b8-a4bb-04ea5960c174 | -11.85714 | -50.56301 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 00ed379c-7d41-32c9-8a03-c2053e6db3de | -12.57592 | -45.67347 | 2025-09-13 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c388e24-5960-3e86-a577-c35da5ff3d4f | -17.31246 | -48.73886 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3701f07-5ded-359a-8dad-f8ba07251ccf | -20.66749 | -42.988 | 2025-09-13 03:47:00 | NPP-375D | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4997cd96-f835-3cf2-bba0-415b2bc55093 | -11.84392 | -50.58984 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 35d5796d-59dc-3a29-9902-564a0a33b9fc | -11.14513 | -45.3174 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 63602af4-a61b-3911-88d5-95a072418ffc | -16.53432 | -51.75387 | 2025-09-13 03:47:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc42f1b8-f9ea-38fa-b1b1-180c9e2b3d74 | -14.75348 | -45.26481 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6432361-d5b4-34a3-9f3e-c21798b33be9 | -16.555 | -49.22326 | 2025-09-13 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f69bd02-2b69-3b46-acfd-225fc7f62a2d | -7.5623 | -42.64661 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f53f7738-51a5-3023-90f5-8b1f32774448 | -11.99415 | -47.7641 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 14081727-ee62-3d17-9e7a-9539600bf8e8 | -12.81455 | -47.96207 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f331fe12-c5dc-389e-829c-3f1cf453ab27 | -7.55485 | -43.95429 | 2025-09-13 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c15c1115-ead7-322e-895d-fa47f17546fb | -12.93129 | -47.97722 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d5e1e43-767c-338a-a782-1d83d224c76c | -16.36046 | -51.53525 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 84e6ab6f-1b27-3e0f-9fb4-90d48434253f | -20.59738 | -44.9095 | 2025-09-13 03:47:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 98ec586b-3a28-3f97-89d7-976d43376c75 | -18.47152 | -39.76575 | 2025-09-13 03:47:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 752809aa-526f-3f67-9ad0-2c156ead33c0 | -20.33531 | -46.67056 | 2025-09-13 03:47:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1565ba8d-56d9-3a0b-a84a-87d02db2281e | -11.86829 | -50.58044 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 030275b2-c66c-3655-b318-051c7535eeba | -17.28519 | -47.24596 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c37ee5eb-3b1e-3432-a3ed-bdbfec394979 | -18.90906 | -46.67333 | 2025-09-13 03:47:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec8146a4-812a-3fb5-8466-a5dd5a2fe052 | -20.33826 | -46.66748 | 2025-09-13 03:47:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc595802-35e8-325d-908b-720ec24e59fb | -12.12093 | -44.84913 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20a21c53-79ae-3c3e-9fe0-1afbe49b7151 | -12.39506 | -43.82185 | 2025-09-13 03:47:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60bcc3b0-701e-339d-8d30-7fc73b31f653 | -17.40493 | -48.22171 | 2025-09-13 03:47:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48df1727-026c-3b68-8fe6-1b6fce04f345 | -10.65124 | -46.28455 | 2025-09-13 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5de89e4-13cb-38ad-ac94-ba0fd0dcc577 | -14.20873 | -46.24006 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59429767-2eaf-33d8-a554-7c5347b4b378 | -11.44833 | -43.57408 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c144b30d-5b48-3138-bcbf-c105521052b8 | -13.2861 | -43.78341 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b879a0d5-7551-3bc7-92cc-a7403683de1f | -11.46996 | -43.61415 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 952de3f5-2071-3cb6-92a3-c0ea86558db1 | -9.74939 | -45.38854 | 2025-09-13 03:47:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44f05c49-b80d-30a6-83e5-82974ce4b551 | -13.00106 | -46.74925 | 2025-09-13 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07cb67ea-e424-3fe7-90d4-36ba5ea7f80c | -11.73324 | -44.2087 | 2025-09-13 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58f15e98-2946-3cdf-acfd-dc092c659c4d | -14.16811 | -46.16831 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8a86d8c5-bbca-3f6d-835d-af149589a8fe | -14.18076 | -46.27028 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 9f53dadc-1f5a-3f56-a2da-38d8bcbee3d6 | -14.19252 | -46.23866 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4a0b341-ee83-3caf-9dc5-b9e5bb40e863 | -11.67722 | -46.5119 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06a6639b-3b2f-3659-aa43-510d6967b452 | -11.1405 | -45.31305 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b35752f3-eb63-329d-a2f1-9859db6dd233 | -19.63372 | -43.73471 | 2025-09-13 03:47:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66b7e741-8c34-3e9d-b45d-fd895d63be02 | -13.77763 | -46.29295 | 2025-09-13 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ce3d6d92-3f0c-3b31-bc1e-7617b0cc8aa2 | -7.56699 | -42.64743 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a7087172-3cfe-32d7-902e-6c0baae6ac71 | -14.17209 | -46.25847 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 46c7a398-7373-3f9a-ae6e-684565139d99 | -11.10946 | -50.70822 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99342834-36c0-3a48-a0ad-f74f280ee078 | -13.8894 | -48.24285 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ce38366-2594-342b-aea0-a33678868d13 | -13.14501 | -47.13688 | 2025-09-13 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63443a1b-04c5-3251-8729-d00fc2f2a5a9 | -11.15037 | -45.3185 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d20ecee7-74fd-3de2-b281-e9776e2b11dd | -11.39368 | -50.47746 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c56cebe6-44ee-3eca-9cbf-f2ce370b73d6 | -9.01161 | -45.76807 | 2025-09-13 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0745d8d2-6981-3cd6-8810-e00a53531e5b | -17.4094 | -49.25052 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41c983eb-24bc-37cc-b7d4-33705d44e1d8 | -8.95046 | -44.45769 | 2025-09-13 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fa4a53c-6460-315e-ab22-62f5dab8893c | -12.12371 | -47.59797 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aec0a664-b2b3-3d35-9e24-7c8dfa055666 | -14.43513 | -46.39933 | 2025-09-13 03:47:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c555dd72-21cd-388a-ae99-d4f68633f2a1 | -11.20058 | -48.4312 | 2025-09-13 03:47:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c5a66200-bb04-3100-8f49-3f0d10777c8e | -11.70852 | -46.56217 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d9bc3f2-1832-3a5f-978a-18224e74d91f | -20.4419 | -46.4573 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e6dd057-4fcc-325b-8d27-f5ebfa9f0c5a | -11.13275 | -50.70559 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a9a56125-d39e-3ff3-9992-fb928f639bac | -14.2267 | -46.28879 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 48ee46ac-2bac-3ea8-853d-fedb7a236d66 | -14.21162 | -46.28141 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |


[Clique aqui para ver as próximas entradas](README24.md)
