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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05f40168-da14-3f7b-bc70-85bfbcbfaa08 | -22.72128 | -43.59272 | 2025-06-29 03:47:00 | NOAA-21 | QUEIMADOS | RIO DE JANEIRO | Brasil | 3304144 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a0494d7d-ab78-33d7-a3f0-5e9f2ed7a837 | -21.18192 | -44.27569 | 2025-06-29 03:47:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| da7d3d99-f7bc-387f-b2c0-13cc27462972 | -22.5863 | -43.65172 | 2025-06-29 03:47:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5c69fc92-7f77-3a9f-a69b-db28f8f3f0f8 | -17.40158 | -42.62662 | 2025-06-29 03:47:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1265d176-ef06-3a1e-a3d7-c724b1f2997a | -15.72863 | -49.559 | 2025-06-29 03:47:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65612528-75a4-3bde-98a9-66864a0e1a6a | -22.8571 | -42.98058 | 2025-06-29 03:47:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 02bcbecf-fd2e-3111-b9ee-7bc535c98b06 | -15.72539 | -49.55326 | 2025-06-29 03:47:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1bc11c9f-5cd6-32fb-88b2-20fff4a301c2 | -18.79226 | -52.58285 | 2025-06-29 03:47:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3260204b-befc-3e8a-bc48-dc88b5248e3a | -17.06757 | -43.72691 | 2025-06-29 03:47:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 492b41a9-49e8-371a-aef6-e895ae8e4150 | -22.40671 | -46.82576 | 2025-06-29 03:47:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 07f5da40-b855-3c7c-ae6e-c2b6b607e412 | -22.69525 | -46.50777 | 2025-06-29 03:47:00 | NOAA-21 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7ac9dac6-2382-3fc9-9c6d-36a1af4db200 | -22.55533 | -42.11997 | 2025-06-29 03:47:00 | NOAA-21 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 574edbbb-4a4e-382d-bba8-4fca9e3d41f9 | -20.34173 | -45.72454 | 2025-06-29 03:47:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b38eb8ad-6e54-3200-96c4-a0e61809d518 | -14.88395 | -48.39145 | 2025-06-29 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 256aa8a4-ea17-3a90-b6e1-51c5a2a78661 | -17.39768 | -42.62588 | 2025-06-29 03:47:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| fdf6f0c4-a0df-337e-90cb-384fa50374b4 | -20.76455 | -46.76878 | 2025-06-29 03:47:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9f83099b-a04d-304e-bdde-2128b3500468 | -18.78654 | -52.58165 | 2025-06-29 03:47:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 996409c3-43d5-352c-80cb-191c839de94c | -17.76162 | -52.45088 | 2025-06-29 03:47:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 475f8d08-2d23-3305-9450-af36b7502a1e | -14.88187 | -48.39212 | 2025-06-29 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2798dd6-028f-3c05-8cf8-195c4fc2d229 | -21.12804 | -48.59154 | 2025-06-29 03:47:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1dcaa5c1-190d-3227-be39-a4f905b1e1fc | -17.0969 | -43.80401 | 2025-06-29 03:47:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 370f5dce-95a7-3f3b-aa70-aa6585fcdf60 | -15.72347 | -49.5529 | 2025-06-29 03:47:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f281883f-bf7a-3415-b61c-c250738c4a26 | -21.02081 | -50.17639 | 2025-06-29 03:47:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ad78a3ba-27de-38e9-9a57-215e0363193f | -16.34919 | -43.69612 | 2025-06-29 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57f2f22b-e736-366c-bea3-b4671bd113b2 | -16.28512 | -49.94353 | 2025-06-29 03:47:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce4f59c8-7ed3-324e-87c6-f90979605f2f | -19.43708 | -44.34187 | 2025-06-29 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3965b82-be18-367c-944b-04c9ef37ad65 | -16.582 | -49.33334 | 2025-06-29 03:47:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30b37a41-9da3-3c42-8dc3-8dd8b0b50583 | -21.53715 | -45.46622 | 2025-06-29 03:47:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 3bf0d0a7-6f7f-3def-b392-c7e0a00ebfb5 | -17.19394 | -44.43623 | 2025-06-29 03:47:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d653106d-28ef-328b-a611-32924c0958fd | -17.92421 | -45.55715 | 2025-06-29 03:47:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d49d15ad-3605-3b33-a52b-33485a8dfc34 | -21.53629 | -45.47064 | 2025-06-29 03:47:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| e20d8676-5bfa-3d1f-bbd7-fbadccc092ee | -16.47285 | -43.49681 | 2025-06-29 03:47:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c5be09a-e290-3b28-8c45-9e09589bbbb3 | -18.79059 | -52.58967 | 2025-06-29 03:47:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 39c5018e-d987-3593-bb9b-36ee43930f4a | -22.40581 | -46.8223 | 2025-06-29 03:47:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 04494856-4b68-3306-975d-fbc5a0577b61 | -22.93612 | -45.69753 | 2025-06-29 03:47:00 | NOAA-21 | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| df0dce8f-6e12-3fe9-a636-ee26bcf24fbb | -22.40778 | -46.82046 | 2025-06-29 03:47:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 00f30f8f-c912-3dd5-8b0c-128d37fc0609 | -20.64781 | -41.84946 | 2025-06-29 03:47:00 | NOAA-21 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae55d493-ed1c-32af-a5f2-47ade540c922 | -19.51406 | -44.27761 | 2025-06-29 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3b05b42-5660-35e5-99cc-3afd4c3f8b1d | -21.17802 | -43.98151 | 2025-06-29 03:47:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 11fcd8de-6487-37c6-96e4-2be7dcf6cc00 | -21.1333 | -48.59278 | 2025-06-29 03:47:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ccc45d8d-e77c-3191-8fc6-401297db753c | -17.39676 | -42.63105 | 2025-06-29 03:47:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 292da3af-5963-3649-b2d5-004b7a9b9388 | -17.76342 | -52.44337 | 2025-06-29 03:47:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a086de44-a159-3412-815b-df49bbb96a74 | -18.96063 | -44.08766 | 2025-06-29 03:47:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94e1ad07-f78f-3221-8bbb-bc1b6b49346e | -15.7297 | -49.55407 | 2025-06-29 03:47:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc25d603-ee76-31d9-8043-7786b008320e | -20.51171 | -49.05052 | 2025-06-29 03:47:00 | NOAA-21 | ALTAIR | SÃO PAULO | Brasil | 3500907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| da591178-e767-3b97-9e54-1614f850a90f | -15.73057 | -49.55943 | 2025-06-29 03:47:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5e8ef81c-48c1-33e8-9461-3866fff123c2 | -20.24979 | -46.7333 | 2025-06-29 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87d70aa0-64d9-3f74-a4a1-f462b8eae316 | -17.19427 | -44.43473 | 2025-06-29 03:47:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fb9a6bb-c1f8-3fa5-a9b4-adc99c05837c | -15.72951 | -49.56441 | 2025-06-29 03:47:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dfdfaf43-3296-3d0f-8b46-3169f492f324 | -17.3986 | -42.62072 | 2025-06-29 03:47:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 89c5ac16-905e-30a3-9cf7-664b131c262b | -21.0168 | -50.17193 | 2025-06-29 03:47:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| e310f39a-f00c-3824-8c00-a19ce668f0e4 | -21.19184 | -45.06178 | 2025-06-29 03:47:00 | NOAA-21 | RIBEIRÃO VERMELHO | MINAS GERAIS | Brasil | 3154705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0447f513-db96-391c-b68d-9b41e38b8935 | -21.02258 | -50.17344 | 2025-06-29 03:47:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ea20190d-f40f-30d6-a617-3d72c7befacf | -16.21388 | -43.41378 | 2025-06-29 03:47:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5462dc84-c0fa-3a1a-aa8c-d9db0150170f | -19.20897 | -40.09754 | 2025-06-29 03:47:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3af91b1-bc0a-32f3-bf45-37b2ad81e088 | -18.7849 | -52.58849 | 2025-06-29 03:47:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d16fa100-36a6-3656-a69c-db81eb9ea0ee | -22.7881 | -43.75626 | 2025-06-29 03:47:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 072c2b3e-d32b-3e33-9d8f-961cedbbb994 | -22.58538 | -43.64946 | 2025-06-29 03:47:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 494a2298-3a1d-3e93-8f5a-8cfa55495f7c | -19.63257 | -45.19184 | 2025-06-29 03:47:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1592b943-14fc-365f-9bc1-a55195c0103e | -25.1933 | -49.3283 | 2025-06-29 03:47:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c92b64dd-b51c-312c-8c40-3b5454bf1f44 | -15.72752 | -49.56404 | 2025-06-29 03:47:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0cc2bac3-0295-338f-aa3d-efcb8ea2dbbc | -18.3807 | -44.50346 | 2025-06-29 03:47:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f8dbdee-fb6e-3c50-970e-00067e1324d2 | -22.97395 | -44.03689 | 2025-06-29 03:47:00 | NOAA-21 | MANGARATIBA | RIO DE JANEIRO | Brasil | 3302601 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 910b3437-3387-3c69-a839-a8b1df2cd335 | -18.37849 | -44.50246 | 2025-06-29 03:47:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f96c81fc-56fa-3e2c-b837-eb3b03bfecd7 | -18.04153 | -39.92556 | 2025-06-29 03:47:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 371e4f8f-18b7-304c-b265-ab14effe9592 | -16.28826 | -49.94356 | 2025-06-29 03:47:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86e7cba9-3862-3e70-a426-cbe91e1894cf | -19.83774 | -40.08382 | 2025-06-29 03:47:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 606acafe-a8ee-3826-b06d-097de6fca923 | -17.40066 | -42.63181 | 2025-06-29 03:47:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 1368451e-6cff-35c1-b26f-706c13d4f0ae | -22.67617 | -42.85563 | 2025-06-29 03:47:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 575fd965-1327-3442-a2db-4337759bd4fa | -22.35087 | -45.77786 | 2025-06-29 03:47:00 | NOAA-21 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cde3408a-cd28-3a35-a274-6f5f5087eca1 | -16.68059 | -43.88222 | 2025-06-29 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 263c515a-5053-3350-990b-17ba3de0f6ba | -22.78538 | -43.75875 | 2025-06-29 03:47:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 58c5fa14-7663-36ad-adf7-0106dfb2ce48 | -21.02183 | -50.17195 | 2025-06-29 03:47:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2d7fc7e1-51c7-3cd9-998a-269800ee72f5 | -22.53919 | -48.81496 | 2025-06-29 03:49:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5a1e403-3692-3040-a41d-495d197d4678 | -23.40754 | -46.55836 | 2025-06-29 03:49:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f6da894e-0418-3209-ba83-024fdaa7b850 | -23.11285 | -45.82096 | 2025-06-29 03:49:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2732a905-9b88-3345-bd7d-8299db3a6f0b | -23.30523 | -46.50014 | 2025-06-29 03:49:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 10a3b56b-158f-3ed1-bd9d-e1fa6442548f | -23.40979 | -52.76886 | 2025-06-29 03:49:00 | NOAA-21 | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d701382a-6b69-31dd-93a7-630b57605475 | -11.5312 | -52.7678 | 2025-06-29 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 7a668abc-aed8-321e-bf80-0da2471c7da3 | -11.5688 | -52.7848 | 2025-06-29 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 95b9f801-1b1d-3788-8e5f-d47f8334fdd4 | -11.0356 | -56.2644 | 2025-06-29 03:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 835d2e88-9d6a-3578-a097-6b6fc2a1a825 | -10.9811 | -45.1104 | 2025-06-29 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a8f09533-79f1-33a1-8038-3d804adca940 | -10.5579 | -52.0289 | 2025-06-29 03:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 445ac10c-5af4-3f67-82f4-4fa19ecbd92d | -11.5309 | -52.7887 | 2025-06-29 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 8944a1b4-6305-3be2-a560-490b6c14b0f7 | -11.5502 | -52.7659 | 2025-06-29 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 94e28ebc-f077-34b6-bfbc-af5cafef50fd | -11.5499 | -52.7867 | 2025-06-29 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 187.1 |
| 62c9d0af-f80a-3912-82e8-738636d40c06 | -10.5576 | -52.0499 | 2025-06-29 03:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| e4b85680-7472-3833-a8d3-88ca05759a62 | -11.5496 | -52.8076 | 2025-06-29 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 41f23c31-9878-3ea0-8265-2d5b6ef1b4e2 | -11.5502 | -52.7659 | 2025-06-29 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 157.2 |
| af7e80bd-fed7-3212-b81e-975b89ecb97f | -11.5496 | -52.8076 | 2025-06-29 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| fe746abe-9f96-3f75-bae8-7eb9bbac263c | -11.5499 | -52.7867 | 2025-06-29 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 205.5 |
| e29cfa77-d6e4-31e6-82df-e3fdf8e78e42 | -10.9811 | -45.1104 | 2025-06-29 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 2c2ca692-fd95-3ac4-a514-69432f6cd16e | -11.5312 | -52.7678 | 2025-06-29 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d372655c-f92a-35ed-becf-f59ac9e2e5c7 | -10.5579 | -52.0289 | 2025-06-29 04:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 3e0b4bfc-62f6-3fe4-b834-1779c701bd5a | -11.0356 | -56.2644 | 2025-06-29 04:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 50ad456a-2265-3b31-8697-186871603fee | -10.5576 | -52.0499 | 2025-06-29 04:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 12c5b879-b903-3b6f-8be3-8be935ff290d | -11.5309 | -52.7887 | 2025-06-29 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1990ea5c-9313-3392-addc-bb5b6b275243 | -4.54168 | -48.02114 | 2025-06-29 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0a9ba4af-7b70-3078-a14d-472b45ae902f | -3.42131 | -47.60326 | 2025-06-29 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a08e6c68-1419-3253-b8dd-0b4ea2633035 | -5.74813 | -46.26045 | 2025-06-29 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README10.md)
