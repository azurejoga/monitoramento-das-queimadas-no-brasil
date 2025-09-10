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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 855318fe-a653-3f48-9723-0f4c2ced183a | -20.97977 | -48.00321 | 2025-09-10 00:28:00 | TERRA_M-M | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 088e86ec-18ae-3ae4-8ad2-5e23f99b2f56 | -20.01676 | -47.63735 | 2025-09-10 00:28:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a36db65e-d2b3-3086-83c9-b206586783b5 | -19.34086 | -47.45153 | 2025-09-10 00:28:00 | TERRA_M-M | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 90172281-046b-3a82-998d-d5a841c762f0 | -16.88643 | -45.75926 | 2025-09-10 00:28:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6f0af037-3763-3aa0-91a9-fb76226c10fa | -16.53447 | -55.1376 | 2025-09-10 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 22.4 |
| 19a23bbe-85ca-327b-ab36-22ed208a5808 | -20.11271 | -47.82268 | 2025-09-10 00:28:00 | TERRA_M-M | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 891788a0-8907-310b-99bf-57279df3ffd6 | -19.99417 | -47.60892 | 2025-09-10 00:28:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 31efce9a-1eb2-3791-b5eb-d360df384975 | -19.29838 | -47.99235 | 2025-09-10 00:28:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0cd4e5ad-1fa0-3c31-9788-e9561779ab17 | -20.988 | -47.99062 | 2025-09-10 00:28:00 | TERRA_M-M | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 6a11f5fb-a51f-38af-9ec3-0eff0f8c3bc1 | -20.11405 | -47.83347 | 2025-09-10 00:28:00 | TERRA_M-M | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eff344a7-7b5c-33c9-8419-d629a7ca5fe0 | -17.30939 | -46.75805 | 2025-09-10 00:28:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f1d817b9-e193-3d44-b920-dca230748a67 | -20.54481 | -47.68638 | 2025-09-10 00:28:00 | TERRA_M-M | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1330d770-7aba-3ccf-b765-116a57b96a9f | -19.17453 | -43.07253 | 2025-09-10 00:28:00 | TERRA_M-M | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 61587b46-db8e-330f-b8b2-1598b05611db | -21.18919 | -45.11369 | 2025-09-10 00:28:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 2b2faf9b-4e19-395b-9937-7e44764711e0 | -20.16775 | -43.65611 | 2025-09-10 00:28:00 | TERRA_M-M | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.7 |
| 2990c8ac-2ce4-3422-ae0e-e3c923f01593 | -18.6649 | -47.54732 | 2025-09-10 00:28:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 261edca8-eb56-3941-a9b9-60f67ef9941e | -18.4664 | -46.46572 | 2025-09-10 00:28:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5bd959fe-9048-3f25-a87a-2d8f201a6ca5 | -16.45587 | -50.6646 | 2025-09-10 00:28:00 | TERRA_M-M | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| ed2af893-6153-3326-a9a7-449940133a09 | -20.53556 | -47.61182 | 2025-09-10 00:28:00 | TERRA_M-M | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 97ad0f95-98e7-313f-a2ce-06fdab8a857a | -15.8089 | -52.27636 | 2025-09-10 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9513d0a4-5c4c-3718-907a-2ecfe38c9204 | -18.0212 | -47.1288 | 2025-09-10 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d4e3d704-9145-39b5-a066-9f46933e90d0 | -20.15943 | -43.6532 | 2025-09-10 00:28:00 | TERRA_M-M | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| ce971e5b-34cf-3333-83b2-9575c2669bf6 | -17.25253 | -46.07887 | 2025-09-10 00:28:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9582424f-9431-3f80-9ddf-6939bf2fc1df | -15.95591 | -50.22872 | 2025-09-10 00:28:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5290d554-d9db-3978-9b06-195a7f7c61a0 | -18.52032 | -46.18511 | 2025-09-10 00:28:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d9057bc1-a987-3b28-adbe-a44fc956e512 | -16.45014 | -51.97635 | 2025-09-10 00:28:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| a8ad07a4-89d6-3da1-b149-d17b05e079e8 | -21.10228 | -47.08204 | 2025-09-10 00:28:00 | TERRA_M-M | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8a2477ad-34fa-307b-9181-9944a6a5f830 | -20.1248 | -47.69024 | 2025-09-10 00:28:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 615df9c9-a69b-3554-86e5-cfe94fd4ea36 | -20.2954 | -46.24773 | 2025-09-10 00:28:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c596975a-19a6-38e5-9150-c44460f22fe6 | -15.82099 | -52.27456 | 2025-09-10 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6d47a9e2-fc96-32e0-8baa-9bb793a39073 | -18.35218 | -49.3445 | 2025-09-10 00:28:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 01f4af2e-e760-3e8e-8d50-3413c4780220 | -19.17073 | -48.78899 | 2025-09-10 00:28:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e09349fb-43f4-33ac-bc39-58d16a44b3e7 | -16.67812 | -48.52282 | 2025-09-10 00:28:00 | TERRA_M-M | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 356955a8-62fa-36fc-8e29-b79a0a1552a9 | -18.76157 | -49.62544 | 2025-09-10 00:28:00 | TERRA_M-M | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 55dd56c2-6ad5-3ee3-8871-49845aa310fd | -17.30821 | -46.68233 | 2025-09-10 00:28:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 686507c3-ff63-3ce1-9fa0-0a3ae4f852f0 | -15.83076 | -48.96451 | 2025-09-10 00:28:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dcbe09c1-8981-3a94-828f-36c01cbacc95 | -21.03023 | -48.41847 | 2025-09-10 00:28:00 | TERRA_M-M | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 44.3 |
| c38c2109-4351-3294-b676-b240be8096e0 | -19.92398 | -46.15472 | 2025-09-10 00:28:00 | TERRA_M-M | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ac5fa701-6670-3b08-98db-aec687ad183b | -17.24499 | -46.08942 | 2025-09-10 00:28:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 637c6d4b-9b81-3dd9-85ed-1ad0b85a4005 | -20.93479 | -45.79891 | 2025-09-10 00:28:00 | TERRA_M-M | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c33d30a8-b0cc-3c8a-8148-cf9f892181a0 | -17.30562 | -46.73012 | 2025-09-10 00:28:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2b6841d9-44c5-3d69-8992-d0ec9d67fc34 | -16.45577 | -51.96994 | 2025-09-10 00:28:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 662a7679-c3c8-34ca-939e-770997d8abdd | -15.48129 | -49.36723 | 2025-09-10 00:28:00 | TERRA_M-M | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 19f86913-1cf7-3d15-9453-b241848d8b4a | -21.18675 | -47.30254 | 2025-09-10 00:28:00 | TERRA_M-M | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 8c786703-480b-3de9-8393-fc78361b085c | -16.61241 | -49.77292 | 2025-09-10 00:28:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 09a06339-b475-34b1-bc91-0004c47c9b12 | -16.63477 | -51.82826 | 2025-09-10 00:28:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ddfb168f-00bf-3906-8006-b3532a4d883b | -16.28415 | -45.67902 | 2025-09-10 00:28:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 930ffc11-07a0-36d9-80ca-cf546ac5f441 | -20.41706 | -43.71416 | 2025-09-10 00:28:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 0ffdc40f-f17e-3fe0-a227-56a7d7fc0aef | -18.0327 | -47.14645 | 2025-09-10 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| b3f44440-fbb3-3e86-8eb1-54533aafef70 | -16.83344 | -49.17224 | 2025-09-10 00:28:00 | TERRA_M-M | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 29c4f2ec-d5e7-38c5-9f50-7c49c00837bc | -15.16865 | -47.95326 | 2025-09-10 00:28:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 716b9782-5c05-3db2-ba00-c8bff8343437 | -16.46667 | -50.66322 | 2025-09-10 00:28:00 | TERRA_M-M | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 91fb4be9-40dc-3d3c-b5cd-7ee520e5fc60 | -19.17285 | -43.0617 | 2025-09-10 00:28:00 | TERRA_M-M | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 4e65e3ea-e306-3be5-b070-677f64886450 | -16.40108 | -50.87993 | 2025-09-10 00:28:00 | TERRA_M-M | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 92b4a7e3-9fc6-3d50-868f-f544ea05f69e | -15.17769 | -47.9519 | 2025-09-10 00:28:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 92a0622b-1371-3d0a-a581-7e502d5b1481 | -15.8475 | -48.0099 | 2025-09-10 00:28:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7f9b0f14-1308-3fee-99bb-9b333797379f | -19.35134 | -47.46027 | 2025-09-10 00:28:00 | TERRA_M-M | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 39.7 |
| e0da35cd-25e0-38ae-aa06-9eca1f12bd78 | -18.0007 | -47.11243 | 2025-09-10 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 03bba569-860b-37be-aeed-7a732df16958 | -15.14277 | -44.03386 | 2025-09-10 00:28:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 80f41d9f-1482-3528-842f-a1bf7eaeebc9 | -19.35004 | -47.45013 | 2025-09-10 00:28:00 | TERRA_M-M | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 73ef2f40-941d-3c7d-adbb-bfff8e0c1c0b | -16.27388 | -49.18035 | 2025-09-10 00:28:00 | TERRA_M-M | OURO VERDE DE GOIÁS | GOIÁS | Brasil | 5215405 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| a23334f3-aab0-3f28-b127-52467bfefc7a | -18.65142 | -46.5405 | 2025-09-10 00:28:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 37b827a2-3caf-34c4-9c98-cf365aed52bc | -17.41183 | -49.88752 | 2025-09-10 00:28:00 | TERRA_M-M | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ec1baeb1-bf2a-3ace-9fd1-ba742207ba0f | -17.73574 | -44.48721 | 2025-09-10 00:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 37917de0-deba-36f9-94d1-474ffcbf89b2 | -20.06767 | -47.53857 | 2025-09-10 00:28:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 14d1134f-6c1d-364c-9151-d65aa1e211a1 | -20.98939 | -48.00187 | 2025-09-10 00:28:00 | TERRA_M-M | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 707c2c4b-1942-32c1-9514-ff33419bb236 | -18.46766 | -46.47503 | 2025-09-10 00:28:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 29.3 |
| b6cb3c3f-0248-3aee-be48-8032a6ff9279 | -21.02177 | -48.43164 | 2025-09-10 00:28:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b8b06261-ece6-30f9-9388-0ee019066010 | -17.40829 | -49.8818 | 2025-09-10 00:28:00 | TERRA_M-M | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1953f916-1be6-3bb0-9672-9b61fb0717aa | -15.1466 | -44.02688 | 2025-09-10 00:28:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 797cfdec-37d1-329d-ad4a-639ef36687f4 | -15.38127 | -49.70051 | 2025-09-10 00:28:00 | TERRA_M-M | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f62d481a-8fa3-3131-98b7-818c51970045 | -19.92525 | -46.16412 | 2025-09-10 00:28:00 | TERRA_M-M | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d9f0bce3-692f-38e6-bc2c-aea6e98b2a88 | -15.94555 | -50.23027 | 2025-09-10 00:28:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6c9c9136-cefc-39e4-9009-d44d93d50fdc | -18.1193 | -51.7291 | 2025-09-10 00:28:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 63622886-0232-31ca-be40-ef2779eee5ba | -11.4465 | -43.6224 | 2025-09-10 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 48e97c3c-ff9a-3c73-915d-34a4586e4ebb | -18.1325 | -51.7096 | 2025-09-10 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 78e211ee-3556-3288-bd00-977c264a73de | -8.0414 | -48.6873 | 2025-09-10 00:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 0e281f4c-b3f0-3e5f-9558-d546dbe86693 | -13.937 | -48.2522 | 2025-09-10 00:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 5409f89b-e9b7-393a-ad56-2cd919bf6ed8 | -5.6788 | -43.3425 | 2025-09-10 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| c71f5873-4898-3824-8c8a-893f883c8d6c | -8.0602 | -48.6856 | 2025-09-10 00:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 96.5 |
| aefd6b0d-7d53-3d71-9733-b5998f08d852 | -11.4469 | -43.5988 | 2025-09-10 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 9c7ba4d3-5a3b-3f12-8031-091e2dc9310b | -9.4578 | -46.7032 | 2025-09-10 00:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c387e5ae-32aa-3142-93bd-9c6c378a7f7d | -15.8873 | -51.8059 | 2025-09-10 00:30:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 147.5 |
| e1716099-ccd1-35ab-b1d8-dae4caed7b09 | -15.8869 | -51.8274 | 2025-09-10 00:30:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 228.9 |
| c499f8b4-c829-3aea-b9a5-f6c7125b1455 | -13.9564 | -48.2493 | 2025-09-10 00:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 051489ec-30ed-3226-92ae-a41b58088355 | -11.4657 | -43.6195 | 2025-09-10 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 07d3eca9-e41e-335f-b72f-118e1e7788bf | -7.7705 | -46.0684 | 2025-09-10 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a670e158-7790-33ba-957c-0a2a3d54b46a | -6.2595 | -43.4129 | 2025-09-10 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| d08265eb-d304-3cc0-987b-fd22d19a0954 | -13.9762 | -48.224 | 2025-09-10 00:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c854e4f8-6b3a-379b-854f-8fd5008fe502 | -18.132 | -51.7315 | 2025-09-10 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 6927ee3c-7a2e-37b1-8bb9-dede4c4904df | -13.1837 | -45.2865 | 2025-09-10 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| cd03fe53-317a-35c7-99ec-6749311d702b | -11.3393 | -46.5193 | 2025-09-10 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e39ea736-3689-3fbf-87bc-deb71ea0c78d | -5.6786 | -43.3659 | 2025-09-10 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 4de9fe34-ba74-3072-af38-4685adb279b0 | -11.3397 | -46.4967 | 2025-09-10 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| afce22a4-837f-3113-b2dd-d3ef01d88a00 | -5.6598 | -43.3673 | 2025-09-10 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e60cb2c1-5a04-32cd-ab43-42d131c84540 | -15.8397 | -52.2631 | 2025-09-10 00:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 973d6be6-c62f-3a37-bf21-1a08c10d17ab | -11.3205 | -46.4992 | 2025-09-10 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 486a9524-f524-33b9-9e6a-f8c6a0c0920b | -10.0346 | -51.6804 | 2025-09-10 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d7426cb4-050a-3b00-bf5e-8facbd469beb | -18.1519 | -51.7281 | 2025-09-10 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ce7ea5de-6d04-3e9f-bd0b-3574f8e65d9f | -5.5892 | -45.0278 | 2025-09-10 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 185.0 |


[Clique aqui para ver as próximas entradas](README5.md)
