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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60c9aff1-9651-3557-a370-e75e379b553c | -17.38463 | -42.65887 | 2025-04-05 04:04:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ed4a63e-b593-34ad-852d-1c62ef8b80a7 | -15.51341 | -42.61384 | 2025-04-05 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5c93dbfb-baf8-3445-a59f-3b2922d5a91b | -13.43615 | -41.78264 | 2025-04-05 04:04:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9275acc6-1b55-3b5c-8b01-876a571bc928 | -19.38782 | -41.47051 | 2025-04-05 04:04:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9954a194-7fc1-3fc3-8a31-f740e1b4082b | -13.43559 | -41.78621 | 2025-04-05 04:04:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9ddfdaa7-a966-3dba-89c6-322a7fa59bda | -13.43341 | -41.77848 | 2025-04-05 04:04:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 300b5ea7-9db8-37a5-a5ca-3512c17dc03b | -13.43947 | -41.78323 | 2025-04-05 04:04:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e3e93853-fc2f-3e17-844e-3e07890ec849 | -13.04402 | -45.02914 | 2025-04-05 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 978703b9-66b4-38fe-87b8-a6a8a7fe09a8 | -19.63244 | -48.32967 | 2025-04-05 04:04:00 | NPP-375D | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e8e38ed-4d43-3e55-bec5-5eb20f589f79 | -16.34776 | -43.69719 | 2025-04-05 04:04:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0be6692-9500-3877-bb6b-caeeb8cc3593 | -13.04696 | -45.03429 | 2025-04-05 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57670888-c834-361b-880e-f6a3a796b356 | -13.03956 | -45.03292 | 2025-04-05 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ca8c533-20ff-371a-9586-db1c22e849c3 | -13.04326 | -45.03361 | 2025-04-05 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b826194-5761-3935-92e4-495a8ae3e751 | -17.7804 | -42.80805 | 2025-04-05 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fdb8c3f-2022-3392-9ac9-505352514925 | -13.43397 | -41.77493 | 2025-04-05 04:04:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| db8ee32c-6c47-36ce-88e1-8532966d9dfb | -13.03524 | -45.01361 | 2025-04-05 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d0ad53a-f5ee-3b2b-9514-725b96d79c2f | -19.84219 | -40.5442 | 2025-04-05 04:04:00 | NPP-375D | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 201a1370-5155-3549-9754-c698428a4b0d | -13.43729 | -41.77552 | 2025-04-05 04:04:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cb4070bd-528e-33b5-916c-87a853f1d23a | -13.43842 | -41.76839 | 2025-04-05 04:04:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 571fb629-c60c-3d60-8ebe-bb1302f2f4e1 | -17.28229 | -41.51632 | 2025-04-05 04:04:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 78a7086a-9cc0-32c7-9d27-8a77d18d72b6 | -13.03816 | -45.01881 | 2025-04-05 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f220f01-a98b-3371-ad44-f4dfb8e47511 | -19.83811 | -40.54766 | 2025-04-05 04:04:00 | NPP-375D | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 842f460c-f6b7-381f-9e0b-4e06d57428b8 | -13.43786 | -41.77195 | 2025-04-05 04:04:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 6d2a0b5f-42f6-3802-9df6-4f143ba3dfd2 | -19.62771 | -48.3325 | 2025-04-05 04:04:00 | NPP-375D | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 43.7 |
| ef277d1f-ef9f-3d7c-9b9b-d7606953ccec | -17.09311 | -43.8054 | 2025-04-05 04:04:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e23e65a1-8082-3eb4-b694-fa6d86eb2f01 | -15.65289 | -39.19074 | 2025-04-05 04:04:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cbf8a53b-b0c3-32c8-b169-05f8d855a9c6 | -13.03154 | -45.01291 | 2025-04-05 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e003664c-c6ca-3f5c-9aa6-8fec1288d45e | -13.03893 | -45.01431 | 2025-04-05 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 78ef2b2c-7d4a-3185-a80a-e3d097841ea3 | -13.48265 | -44.03355 | 2025-04-05 04:04:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2587913b-aa20-3b0e-a47d-7662b8eeb2fb | -19.84159 | -40.54827 | 2025-04-05 04:04:00 | NPP-375D | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a628e69c-4fde-3d59-810b-084c1bedfed0 | -16.68037 | -43.88606 | 2025-04-05 04:04:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb46719d-31d7-3ec4-bf71-1216b7229a4c | -20.15553 | -47.33445 | 2025-04-05 04:04:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d815d5a-bdb6-3872-8a3c-25a98757ce51 | -16.75631 | -40.05471 | 2025-04-05 04:04:00 | NPP-375D | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ce2281cf-8b3e-30a3-ae73-13d3399ff3c6 | -13.43511 | -41.76781 | 2025-04-05 04:04:00 | NPP-375D | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c4fe5e26-882e-3268-a502-65d6b38a9921 | -20.15493 | -47.33137 | 2025-04-05 04:04:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7b9c7a9-e934-3bbc-8d18-547a75f2b97f | -21.45571 | -48.70532 | 2025-04-05 04:06:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 346cdd16-c68f-3907-8d6f-35a550a4f8c0 | -20.83192 | -47.75747 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d5548137-b092-36d6-b221-30e970e3a3a5 | -20.76534 | -46.76786 | 2025-04-05 04:06:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f7d0ad03-4776-3da2-bb96-3f49d11a7143 | -20.83773 | -47.76941 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| caa79e79-2e9f-3a1a-bd6b-c8347aadbb28 | -20.83522 | -47.76537 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7bd5a59c-ffe4-3451-8090-e745a1d6b107 | -21.62658 | -48.75337 | 2025-04-05 04:06:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0f7feb5-8cf3-33fb-a0c3-2b9e5519dcb3 | -20.83809 | -47.77132 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cb3eec89-b0cc-3e76-90d1-c20b7568cf47 | -21.62201 | -48.75285 | 2025-04-05 04:06:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a42852cb-5db1-3cb0-a3cb-d7e37327e113 | -20.83039 | -47.76982 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19b92e15-05c4-3b73-9631-5aef3dd3172f | -20.83867 | -47.76418 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 866dd298-3f2e-389e-a5fc-fc07d231a634 | -20.57718 | -56.04691 | 2025-04-05 04:06:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2c4f681-9038-3b6f-997a-47dc4a9d9c9c | -20.83235 | -47.75943 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d4ee3221-d0fe-3a2b-a087-3ee1705949b1 | -20.83097 | -47.76273 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 24.4 |
| fff9553d-53f6-39ea-80fa-cdfd18182fb3 | -20.83907 | -47.76611 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 82a2f93b-2f29-32cd-87f1-9b1101455b14 | -20.58599 | -56.03801 | 2025-04-05 04:06:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcc0bf8e-e4f5-349e-8da4-a1cbe155fdba | -20.83961 | -47.75897 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f02f5a82-5368-39fe-a643-ab4a3cd867c8 | -20.83137 | -47.76465 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2e9bfdd-ee19-3331-8cea-80eda6de556a | -20.57971 | -56.03614 | 2025-04-05 04:06:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aa2eb39-47dc-343e-8745-34cad0495c75 | -20.57845 | -56.04149 | 2025-04-05 04:06:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1b22bd5-568b-3100-ba50-0c3a5a799a93 | -20.82713 | -47.76191 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 98f64953-dcac-30e3-9f5b-bdef4a99192a | -20.83577 | -47.7582 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 9e163064-9c3c-3048-90ca-22e4cda6b3ac | -20.83424 | -47.77057 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5de52bda-a41c-30a5-bb33-e48651e2c1d4 | -20.58472 | -56.04338 | 2025-04-05 04:06:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d18da27-fe1c-3b83-b8e6-d99927e8ad2e | -20.82808 | -47.7567 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5c6fb4fa-1c67-3e72-a2d7-1fd65f3fa558 | -20.83003 | -47.76791 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdbd514c-d2d8-308c-87a8-9831c23c9fb9 | -21.62601 | -48.75379 | 2025-04-05 04:06:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25db3cb1-fa74-3bca-a06b-2854ebcaed13 | -20.83287 | -47.75226 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 509468c6-8f05-355c-9b1b-5daf8d14b66a | -25.32629 | -51.48148 | 2025-04-05 04:06:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 370144d5-5afe-362a-bdd6-656fb5cb597a | -20.83333 | -47.7542 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1244b717-a5f7-3a1e-ab65-1fcc05ab40a3 | -20.8362 | -47.76014 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e9d34e66-f10b-39de-ae14-5e23b44099ea | -20.8285 | -47.75867 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0f40de6d-e6e4-32a7-ba45-4bd3e8eefca6 | -20.83388 | -47.76866 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d21622d-a6f7-380a-ac4f-3c1f3500260c | -20.82949 | -47.75346 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3853bc9b-4676-33a1-9dff-3f679db3479c | -20.83482 | -47.76344 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 5419ca6c-5b81-373c-9e30-43862147202c | -20.84005 | -47.76091 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d3bb513d-97b1-31cc-b6f6-95cdb9a273d0 | -20.82753 | -47.76385 | 2025-04-05 04:06:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2143cb34-7ac3-3f06-8551-2996e50087bc | -30.46334 | -56.38797 | 2025-04-05 04:08:00 | NPP-375D | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| ae4a11cf-66d8-3165-9f96-18bdd5154dee | -30.46658 | -56.38836 | 2025-04-05 04:08:00 | NPP-375D | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 09a6cd1f-8e19-304b-8204-03dfaf1d2901 | -27.68712 | -48.75154 | 2025-04-05 04:08:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6f1535e9-c23c-3af5-babf-60750b54066a | -5.0256 | -38.69093 | 2025-04-05 04:21:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a17d56a-7fb0-3282-849f-b485b6c3148b | -4.6098 | -43.15518 | 2025-04-05 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84ec9ccb-2012-38f0-abe7-829cfe259a07 | -9.74579 | -37.07028 | 2025-04-05 04:23:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d01b69b-ded0-342c-9b2d-b88125a1417b | -9.37096 | -40.50855 | 2025-04-05 04:23:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e9b41357-8154-369e-a53d-792d9277c023 | -10.23926 | -49.17633 | 2025-04-05 04:23:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5170dfe-c821-35c1-b8b4-0192c7e1dd37 | -10.58024 | -45.13506 | 2025-04-05 04:23:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 364d79fc-7d34-37d0-ae56-ad8b9b7b6e1f | -9.74023 | -37.06959 | 2025-04-05 04:23:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a01d89c1-2746-38f3-a94a-f6fab8f08561 | -8.10794 | -43.12036 | 2025-04-05 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c94473f8-9c42-3329-8927-a202d412c76b | -10.24272 | -49.17691 | 2025-04-05 04:23:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32b37281-93d1-3716-a982-93075b907643 | -10.57967 | -45.13881 | 2025-04-05 04:23:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2fb944ea-f518-3037-9806-7d154a99380a | -5.97148 | -43.75083 | 2025-04-05 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95224f9d-3b6a-3a90-ac3b-555900a4f532 | -8.10301 | -43.12835 | 2025-04-05 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 80132558-f5b6-38a7-be0c-fef79b223fb6 | -8.10729 | -43.12463 | 2025-04-05 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8425b463-7fa1-3be3-9cb5-9ab1338c3791 | -8.11457 | -43.12575 | 2025-04-05 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 869e7dc6-3e3d-3448-aeb5-58efad5ace41 | -10.57568 | -45.14204 | 2025-04-05 04:23:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2e9def2-47f2-31a2-8cba-52facdb4e90f | -6.24059 | -47.0088 | 2025-04-05 04:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de53396b-b660-3863-9730-04418cec954f | -8.1043 | -43.11978 | 2025-04-05 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 25c08e20-2298-3c35-99c4-78b99a5989e4 | -5.94389 | -44.3582 | 2025-04-05 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a230481c-882a-3aa7-bbc7-6af3d068ce5d | -10.56885 | -45.14098 | 2025-04-05 04:23:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47fa9531-0193-3d99-8f90-045a6e7edc6f | -6.23669 | -47.01179 | 2025-04-05 04:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70b42343-4823-3b90-80a1-9b2266ff5bf4 | -8.10665 | -43.12891 | 2025-04-05 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dfad69c5-0945-3c4e-ac69-c8fdeb7440f8 | -5.97391 | -43.75091 | 2025-04-05 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fddb474-2667-3a1f-aa08-b8c9f81e1a7f | -5.97045 | -43.75039 | 2025-04-05 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be6cd8fa-34c0-3f15-a473-094453e1b770 | -8.09937 | -43.12779 | 2025-04-05 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 834c4351-6938-359f-9750-ccda55af2ab4 | -10.57227 | -45.14151 | 2025-04-05 04:23:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bfd6071-cdb7-3afd-9c75-9fa674f2eea4 | -10.57625 | -45.13829 | 2025-04-05 04:23:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README4.md)
