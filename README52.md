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
| 76e72f46-922a-3c12-a80c-9b776d2b4a53 | -12.94591 | -46.53658 | 2025-10-29 04:25:00 | NPP-375D | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e173a580-0bef-30d6-a90f-44cacdf3e7f9 | -12.55658 | -44.96625 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39c90297-3446-3ce4-96a5-cf48d04fcea5 | -12.09466 | -47.25499 | 2025-10-29 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a430c854-65d6-3447-916a-51e111c08a04 | -17.25943 | -45.28627 | 2025-10-29 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1add9fa7-2dd2-3bd4-afe2-35798cb84c0f | -12.87027 | -48.6286 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61c3d431-c6ae-31d1-bb18-089a458d2b60 | -12.00275 | -46.78238 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 328aee6e-574b-3207-8ea5-ae13cba8c279 | -14.88897 | -46.75842 | 2025-10-29 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25ed5cc8-951f-3b91-bf32-93e33ce3ae5b | -13.71844 | -42.9165 | 2025-10-29 04:25:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e47489c3-0302-382e-a70e-5d3cdadf9dbb | -13.02361 | -48.77018 | 2025-10-29 04:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6add3b82-6abf-37ca-8517-a494dee3e297 | -13.63934 | -46.49004 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ac1439b-90cc-3c89-9c52-e8ed4c28a227 | -12.87658 | -48.6338 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bce9bc9a-4dca-3107-a00a-dd812800a324 | -12.77046 | -46.65699 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32ab1101-7a20-3561-afa5-9f10ac17bb69 | -11.28633 | -47.55499 | 2025-10-29 04:25:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f562a60-8739-3660-9da5-ecb14755ba06 | -14.29417 | -43.47763 | 2025-10-29 04:25:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78d6ae72-588d-3c1b-a1ad-a82cb6361bc2 | -15.16506 | -47.21584 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dbe475b-dc29-3992-b402-d2d56b188429 | -13.32553 | -47.43734 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 514afc52-acce-38bd-bdc4-ee146e918d63 | -14.24323 | -48.11171 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1fe099c-6873-3cd1-8d5f-368343298dcc | -13.04183 | -48.4655 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99a4b68f-2d71-331c-a429-852da431fa95 | -14.26932 | -47.3124 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7ac702c-e6a8-37be-adaf-1feb0f878549 | -13.57109 | -49.60851 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96f388a1-8f3d-32c5-8c1c-52d63dac0964 | -15.09977 | -43.84091 | 2025-10-29 04:25:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3df14c43-4b8b-30ab-a172-03250bf7f54a | -12.08404 | -47.99564 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c40dab0d-1ca0-3654-9476-2bd4e28b9516 | -13.24462 | -47.99827 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b03996d4-c0d0-3c7b-9696-1ca69bd716b0 | -13.6443 | -46.50179 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69c27df3-2eb3-3efc-bf1a-f8e9d2ceb38d | -13.61985 | -46.46886 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0353212-13e9-3e43-b958-17f3d8449312 | -11.58764 | -47.95677 | 2025-10-29 04:25:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b8175d1-de31-3bea-bf40-af1ddb4c4095 | -13.22891 | -47.73237 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b83cb0fb-60af-3b4e-af16-54d54aea3199 | -12.36031 | -46.68437 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4f7a59c0-4efa-38c9-81c1-67d00eca9651 | -16.11634 | -45.74989 | 2025-10-29 04:25:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c10989b0-2b53-3a3f-b621-4034508496bc | -16.67663 | -41.35266 | 2025-10-29 04:25:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 71abf697-edd7-35ce-95ef-ebebb93e66aa | -13.93989 | -48.4492 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94d36817-d854-3fbd-8014-1d2045ef119c | -13.53291 | -47.1339 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac36f820-8610-3dd5-aa90-e1c2d822a3e3 | -10.64226 | -52.18182 | 2025-10-29 04:25:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a073b33-b448-366a-8a0e-c33968252235 | -12.12343 | -45.20069 | 2025-10-29 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 310bbef6-aef0-30ac-a986-4b13b1984193 | -14.26017 | -48.11479 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 266750f8-6242-315f-bab2-0d0460ec548c | -13.61608 | -48.41888 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6674578d-de4e-3961-9e1c-a9244918a93d | -13.55294 | -47.13723 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a16e2f1-f5d4-39af-96e9-0394e65f0263 | -11.83544 | -47.61949 | 2025-10-29 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1da063e-d1db-34d6-8930-ba98d7039ffe | -12.98174 | -48.38799 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c185de1-d22e-3525-b8db-3a3efec3df51 | -12.82584 | -47.26503 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19becfef-60ff-3c5a-9ec2-7c844346ac14 | -14.31579 | -48.00965 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5b62ef3-56ac-3914-a1b6-9669c10e17cc | -15.09681 | -43.83621 | 2025-10-29 04:25:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 49576574-ad8d-3afe-82b4-09f42a19ae2e | -10.84626 | -49.14784 | 2025-10-29 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba8757ce-01d8-3f8e-b9cb-3ff88f3568d7 | -14.32454 | -46.52299 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 969b02a6-7a43-3dde-a407-2a36eff787a4 | -12.20813 | -46.49507 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 054e1824-6559-3909-abf5-021a52ae255d | -18.92451 | -45.04442 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 5dd5b30a-fd5f-38e3-8a3e-4c8685b7afd3 | -13.57184 | -49.60416 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d2c51bf-8fa8-3a11-8ea6-f45102697d24 | -19.34552 | -43.04865 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 06522bb9-c859-3875-a59f-dd4cf994b069 | -14.54334 | -48.00669 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6011fb35-d92a-3056-b847-fe0737dd5c15 | -19.38356 | -43.63024 | 2025-10-29 04:25:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d63d2c0-4739-3cb7-aaf8-bf582fa18b0c | -12.75674 | -45.16795 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 071d36c1-5233-371a-927f-c34e4a82ad8b | -12.52805 | -47.55199 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbc6a03c-061e-3864-88c4-e1c1e07b020b | -12.08023 | -46.38345 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 337398b1-c503-3c65-9d5f-c8e73e8d048b | -12.64344 | -44.24068 | 2025-10-29 04:25:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbf75069-18ef-36e8-a5fa-0863026c259c | -10.90804 | -50.26313 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9291fd39-a6f3-3371-a384-9c6b219876d0 | -13.26852 | -47.72402 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 899931b5-dbe3-3d05-83e1-26a7a5247ad1 | -12.06653 | -45.71932 | 2025-10-29 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e750ddbc-4d28-3643-93f4-5873584b6103 | -12.87375 | -48.62926 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 453448d4-8164-3b8e-9dbb-a770787aa41d | -18.58342 | -44.02972 | 2025-10-29 04:25:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8a2d66e-8fe8-3623-8462-ae1c58781764 | -12.08341 | -47.99943 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd732612-de36-3900-a778-160256c9e866 | -13.55453 | -47.14864 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b0580d7-1ef1-37ff-81ab-5906f4c651d6 | -14.27769 | -47.30305 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdecfe44-3528-3c2a-b2c7-0e571630b96d | -13.46286 | -47.45905 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9be6a802-2b09-3a72-8cee-1e9bd0905ca8 | -14.98479 | -47.87251 | 2025-10-29 04:25:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8926fc4-d2c7-3f31-98e1-04a258d3519e | -14.31789 | -46.52188 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e66e866b-f4ab-3727-8882-eee28a58ec01 | -13.23099 | -47.99595 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 667256b7-54ab-3b54-b75c-240e899098d2 | -13.30683 | -47.46745 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c98a2b8e-9258-3621-93c4-2dc7e531bd6e | -15.11954 | -47.92948 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0523eadb-c498-32aa-a4fa-8a5bdfb842c6 | -12.16174 | -47.69617 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 40b4ef6b-9689-3bfe-a9bd-5ff58a8fa5f1 | -13.60927 | -46.49261 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d850330-018b-31f2-b3ba-14167add8d67 | -15.35907 | -47.91722 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e05f6d73-0dee-3abc-8259-a5329b7765b9 | -14.65056 | -48.39667 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2df92922-b805-3d25-981f-0ba33772af02 | -14.12067 | -44.18707 | 2025-10-29 04:25:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2484c208-72e4-33b9-9472-8c6bd86d5436 | -13.22148 | -47.07199 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 755ca737-780c-3b6d-9a09-ca910704d9ec | -12.68885 | -48.43888 | 2025-10-29 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e86121d-a34e-3afd-a451-9ab18de2676c | -12.64269 | -46.71594 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 788573fa-05f3-3d4c-a1fa-d19a5e1a5836 | -18.05886 | -43.1819 | 2025-10-29 04:25:00 | NPP-375D | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77165da7-f31f-32e8-b3dc-eb9e555d8981 | -14.61291 | -48.43283 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60b48ba0-0e3f-3030-8bb5-0b70d9f8d0e1 | -13.65433 | -48.27179 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa1c3108-394a-3d87-9e8f-dc04b44e2bdd | -11.99549 | -46.78485 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0872cbde-8cb3-380c-b159-a5de5bcf89f7 | -12.21215 | -47.89973 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21eaa875-07de-3fe3-99b3-a2a0aaca3e76 | -13.47293 | -48.01333 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69f2baae-0a75-3499-a97c-126875429fc8 | -11.99607 | -46.78127 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f15aeab2-6855-3836-bbdc-ec9bf23c05d7 | -17.2086 | -47.00474 | 2025-10-29 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e25a7dc-9f46-3a89-a0d2-b56e3f947f99 | -13.56062 | -47.15342 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6b29178-ba70-39d5-8a48-79f6f4bb948c | -13.81838 | -41.68753 | 2025-10-29 04:25:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6653489c-728d-3ede-9ecf-4188a94556f7 | -12.36364 | -46.68492 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 218697f6-224a-31d3-9cda-37609b7ae077 | -14.314 | -46.52489 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76695ec6-bea1-37bb-bf01-bae70b681c90 | -14.26356 | -48.11542 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39bac012-db89-374d-810c-ce4aa3c7ca6d | -11.02868 | -47.84461 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ec2b9b1-8c54-3a53-923d-8893042dbe8e | -13.04064 | -47.58037 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27747297-6182-345e-a21d-8441150a4ac4 | -12.22239 | -46.48641 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1379c7dc-cbb9-3bd3-91a3-64bb2a57e87a | -13.56778 | -47.3433 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 517d01bc-ba3a-358e-b625-ca206c8cbdec | -15.64613 | -42.91401 | 2025-10-29 04:25:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 12940b88-3b79-385f-a94e-72f0beb3039f | -12.18204 | -46.71653 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12a557b9-fffc-357c-a674-afa4bac372f6 | -14.2318 | -48.11745 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c6b6911-cca3-33ef-8f54-c3a1ea184d1c | -13.23558 | -48.56116 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ee1faac-460e-39b5-ac25-f4fbc17fbe87 | -12.91492 | -45.04459 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a9950b5-4936-3f22-a46e-6a357dfdabf0 | -18.89099 | -43.35543 | 2025-10-29 04:25:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2ed7683a-c8a2-35ce-93c6-3308806d8682 | -15.19456 | -47.20243 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README53.md)
