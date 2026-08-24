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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9952c2c5-0b00-35bb-b1e6-06e0533659c0 | -13.16868 | -51.39291 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 146c13cb-f451-3260-a51b-b77f1da7c8cb | -16.39347 | -51.82458 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aab0fec2-0b92-3cc8-be71-a43a5c7fbd67 | -15.29102 | -52.81595 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 98e21ac2-9cd1-3746-8b11-74c50edcd3a4 | -16.0536 | -50.4201 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd6a718a-be53-317a-b54e-d51d131c7b8e | -15.26393 | -52.86095 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e39f4916-06e1-30f8-ad84-8fb794952e7e | -18.69773 | -47.47365 | 2026-08-24 04:27:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a267cd98-35f1-3f58-848b-24ee716e329b | -14.28747 | -51.7868 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adc8388b-bf48-3835-a445-a7c0f22d3e27 | -13.1753 | -51.39683 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6b38d1dd-7033-3a8a-a4cf-258de2e1ecaa | -16.05158 | -50.45314 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| faa0bda9-b40f-3ba8-901b-30bb50655467 | -16.06549 | -50.44478 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 84ca7964-7671-3cfe-8343-22cf8fded75c | -16.41712 | -51.84157 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a2d7763-7545-3d10-9dc3-6f9ef8e8d32a | -18.56771 | -44.42718 | 2026-08-24 04:27:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee76ed08-512d-3aca-8192-3591bf90e132 | -12.10612 | -50.63251 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc3a8e9b-29f7-3f3a-aa20-6304a7e00254 | -15.26579 | -52.82051 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d7287ec0-39af-3a99-930f-0b0060dd98d3 | -17.42575 | -48.84347 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ee3c407-d8b8-3904-9dcd-79b8555ce04a | -20.23242 | -44.20357 | 2026-08-24 04:27:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b29191c4-07ba-33d1-a3bf-b3d2e0495a47 | -14.31612 | -51.76612 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a525620-e957-3c16-a6d6-35790c7c20ab | -19.01373 | -42.12317 | 2026-08-24 04:27:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 2d5393ae-2d82-3faf-afd9-f3ce4d754623 | -15.26862 | -52.862 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03b99669-cf1f-37a1-a68a-38bde970595f | -12.74138 | -46.46461 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92cf8d9b-02f3-3607-9985-56a4b7c8aa0b | -13.0976 | -43.34991 | 2026-08-24 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 574eb7d5-d033-30ca-bea6-3179f1d8bd61 | -15.27615 | -52.81727 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e6e6d4b-b897-3799-9afe-ea13055aed3f | -15.04619 | -48.69151 | 2026-08-24 04:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 118e7674-dac7-3150-8202-d5b68c6b6edf | -13.16643 | -51.3951 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e2162314-f2bb-31fa-ac43-94a2dd7bc1bc | -12.74074 | -46.46841 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95fc5533-c46b-3530-9af2-cef27fc331a6 | -13.15981 | -51.39117 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b86a00e9-b033-3f45-88a5-c26829a016e2 | -15.2827 | -52.81539 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e5ba66f1-cc7f-3e7e-a9b5-1ec6dc25f86d | -15.26508 | -52.87564 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7d1d706-e405-35b9-ba85-89681198af75 | -12.0799 | -50.58058 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72bfa6f2-1d69-3137-80f5-2a70edf8fd16 | -17.44081 | -48.84196 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 13c31239-6584-347a-b5d1-646999b0f6a3 | -12.10833 | -50.62008 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dc3a9cc3-b83d-3858-8ca5-e324eacc6363 | -17.91765 | -44.50936 | 2026-08-24 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a583fac-9377-31ab-859b-f3128d475e01 | -12.10759 | -50.62422 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| eeecef8b-d350-36e9-93b7-4b943b992106 | -13.10436 | -43.35098 | 2026-08-24 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb9d8ebb-8351-3e27-9961-35e0940c4204 | -12.74481 | -46.46513 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e77889c8-b81b-3390-8466-52c409046c78 | -12.09055 | -50.59536 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ae7a800-16ee-33d6-961d-096bc82c4dc2 | -14.34455 | -51.76238 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5e8e329-d666-3477-b1dd-700f86254fdc | -17.70351 | -46.38725 | 2026-08-24 04:27:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f5ee1b81-e425-3be4-aab0-ada216651f19 | -12.74201 | -46.46079 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0cdbb35-ce5d-3413-8ddc-142b0a957916 | -17.42933 | -48.84417 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a640b09e-816b-3fd0-99b4-06df8deeb608 | -12.89093 | -48.48375 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aeb7fce-ffa0-3506-ba75-3f10c02896d6 | -16.46404 | -43.4395 | 2026-08-24 04:27:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23c6eb10-ec22-3222-b320-749f6723262e | -12.11189 | -50.62504 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 87dbc78b-fd5e-37fe-9018-fb34715ca8b8 | -22.9968 | -49.38372 | 2026-08-24 04:29:00 | NPP-375D | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 25c5cbea-8c49-3be8-8dbd-0af08f180373 | -20.59968 | -52.46003 | 2026-08-24 04:29:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3445c3a0-92bf-3027-aa6d-57b6789b43aa | -23.00782 | -46.47376 | 2026-08-24 04:29:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fd04e358-0ab3-3115-825d-acf7c43140bd | -22.0183 | -45.73991 | 2026-08-24 04:29:00 | NPP-375D | SILVIANÓPOLIS | MINAS GERAIS | Brasil | 3167400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fc2ddb68-1351-3a7d-980d-5b30f9a8a08d | -22.99821 | -49.37563 | 2026-08-24 04:29:00 | NPP-375D | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a2b32153-c563-3303-a41a-c67a70f102c2 | -20.32754 | -46.60999 | 2026-08-24 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5876947c-7a8a-36ad-842c-f98c834f62f9 | -22.49897 | -48.59229 | 2026-08-24 04:29:00 | NPP-375D | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4f43e5b5-dfc5-3968-8aca-0425421db177 | -22.50476 | -48.66175 | 2026-08-24 04:29:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 82cd1786-94bc-3c0d-a3b5-be242f3bd2e6 | -20.71886 | -57.86469 | 2026-08-24 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ff689161-7de7-392a-aa02-153309b5d2a5 | -23.26718 | -46.82485 | 2026-08-24 04:29:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 90c59717-0c58-3253-b6af-42d333c17d37 | -23.19654 | -46.60725 | 2026-08-24 04:29:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1a0242b7-0575-3f0d-8d7b-45d077cf337a | -20.71759 | -57.86497 | 2026-08-24 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 25d0d24f-5540-3efc-bf54-e8d64c3ebe9d | -19.98055 | -50.38451 | 2026-08-24 04:29:00 | NPP-375D | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a60788d2-df05-3d7c-971e-5cf25659e71b | -20.53908 | -47.45884 | 2026-08-24 04:29:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1460b326-4a9f-31e4-8974-3c0fcf015596 | -22.95047 | -51.78044 | 2026-08-24 04:29:00 | NPP-375D | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| aa6da86c-b317-32fb-ada4-001482e6e679 | -21.551 | -47.68805 | 2026-08-24 04:29:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24375119-dfe8-3a73-be5b-639dc2a7774d | -23.8866 | -51.2366 | 2026-08-24 04:29:00 | NPP-375D | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e8d85baa-3e7f-3e33-a125-5cc7280051f8 | -23.82481 | -48.71785 | 2026-08-24 04:29:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8db66b8b-8e61-3dac-9a48-bd218ba0f593 | -20.71985 | -57.86032 | 2026-08-24 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e06b20bc-02ac-3f3c-b955-162f01ec9f94 | -22.99891 | -49.37157 | 2026-08-24 04:29:00 | NPP-375D | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8c178fe0-d4c2-3f39-abd1-e158a2c988a9 | -23.34348 | -47.64389 | 2026-08-24 04:29:00 | NPP-375D | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fb4fbeb3-0ee6-3f0c-a4d3-35221e4cca4a | -22.83163 | -47.63209 | 2026-08-24 04:29:00 | NPP-375D | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d74641ad-b172-320f-960e-f2b4edcc0b98 | -22.9975 | -49.37968 | 2026-08-24 04:29:00 | NPP-375D | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f938f13b-56dd-3f61-8e33-5425faa9ec6a | -20.32422 | -46.60939 | 2026-08-24 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7a738660-f81f-3d52-92d6-a145a9a75ec0 | -22.49963 | -48.58841 | 2026-08-24 04:29:00 | NPP-375D | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5dc8a505-4c93-3e00-b5c4-e691d82f79e9 | -23.00235 | -49.3723 | 2026-08-24 04:29:00 | NPP-375D | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 59eadd6e-1ada-35ee-aa48-ec130c4b8dbd | -23.00165 | -49.37635 | 2026-08-24 04:29:00 | NPP-375D | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 15e7e874-1905-3174-9354-46b877bbbbcf | -23.52051 | -47.36611 | 2026-08-24 04:29:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 27cc23de-dec7-39a2-8270-ceb1e2364414 | -21.55435 | -47.68866 | 2026-08-24 04:29:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e900cca1-5d93-3e69-9778-31008789d5bc | -23.00095 | -49.38039 | 2026-08-24 04:29:00 | NPP-375D | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 15c8eee9-12de-3616-af89-14a1ef1b3fb1 | -23.26385 | -46.82425 | 2026-08-24 04:29:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d65eaab6-36ab-34d9-ad86-4078a8bc78d2 | -22.6387 | -47.81324 | 2026-08-24 04:29:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8974480a-b368-3621-8242-6a6c6af4501d | -20.91182 | -57.62401 | 2026-08-24 04:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1e1a9efa-f912-346e-9df5-93428deda782 | -20.39297 | -46.54224 | 2026-08-24 04:29:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1645501-7781-3449-b230-7f98205f9f21 | -22.44014 | -45.43781 | 2026-08-24 04:29:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 65e02ca4-e764-3f67-93c2-8542dafbeb78 | -20.48825 | -47.12819 | 2026-08-24 04:29:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 396f0835-2aa4-3423-bf4f-ddb94a745008 | -23.12762 | -48.68184 | 2026-08-24 04:29:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50381415-fe6c-31af-bab5-5c24c0fad971 | -19.98116 | -50.38173 | 2026-08-24 04:29:00 | NPP-375D | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8d3103fb-15d1-36e2-b98b-b270457f8bc6 | -21.55497 | -47.68489 | 2026-08-24 04:29:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f4ac677-a77c-3d4c-af97-50fa8a9a01aa | -22.95431 | -51.78129 | 2026-08-24 04:29:00 | NPP-375D | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 04607f72-1432-3511-a504-2a90b2b0feb8 | -20.65372 | -45.84321 | 2026-08-24 04:29:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5234ec27-d19d-3ff3-a325-bc3001a14915 | -20.71861 | -57.86062 | 2026-08-24 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b1cc6679-98c5-38ab-8671-30685c439432 | -20.6498 | -45.84639 | 2026-08-24 04:29:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 833b7ec7-6766-3639-abb4-b3b0e2a46204 | -23.42275 | -46.90662 | 2026-08-24 04:29:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1131ae33-8858-3a84-aa45-e43e0a13aaed | -23.00509 | -49.37706 | 2026-08-24 04:29:00 | NPP-375D | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 834f0eab-9712-3230-835d-56496fdf8554 | -20.91087 | -57.62818 | 2026-08-24 04:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bbc167f1-82cb-38ef-a7e7-c0f36b489f83 | -22.9495 | -51.78562 | 2026-08-24 04:29:00 | NPP-375D | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| dedca690-527e-3695-a83a-d73abea9c52f | -14.3171 | -51.7688 | 2026-08-24 04:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| ae9847e2-109e-3500-866b-478943e0b46e | -7.685 | -63.3255 | 2026-08-24 04:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 803ae499-58af-3bbb-ba17-4d3370a3af51 | -12.0941 | -50.5951 | 2026-08-24 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| f1ecdf17-d186-3a3c-8edd-dbdd95598861 | -12.0938 | -50.6166 | 2026-08-24 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 51526575-3beb-3059-9b91-b73e43940e5c | -7.6665 | -63.3261 | 2026-08-24 04:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8077bbb6-be6d-329e-a675-a8b018eb59a9 | -12.1132 | -50.5929 | 2026-08-24 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 26bdda57-6346-3651-a3e5-29d0e6091c63 | -12.1128 | -50.6143 | 2026-08-24 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 0a61085a-15d9-31ac-bd20-a953c04d1e7a | -25.80346 | -52.57994 | 2026-08-24 04:32:00 | NPP-375D | CHOPINZINHO | PARANÁ | Brasil | 4105409 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 49c0c714-c002-33d9-95b6-daa494289392 | -29.11902 | -50.12756 | 2026-08-24 04:32:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d2ba5184-13ef-32a2-93df-66f9a44b43e7 | -29.03485 | -50.64269 | 2026-08-24 04:32:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README25.md)
