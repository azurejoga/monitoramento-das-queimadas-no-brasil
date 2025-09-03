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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2e05e11-e479-32dc-b70e-5d8eb8662e9e | -18.05899 | -45.99968 | 2025-09-03 05:16:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 3d79b461-e1f9-3d4b-8d0b-3dceba1384e1 | -15.54835 | -48.38302 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe004ab7-2603-34f4-8bbe-3e0153fc042f | -15.73217 | -53.69197 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6e9f7da-cc10-31fb-8d5d-f9ab8e9ad6d9 | -15.90507 | -48.16889 | 2025-09-03 05:16:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9b3c61c3-ffaa-3424-9f97-98f7cc5fa9e7 | -16.07985 | -47.97496 | 2025-09-03 05:16:00 | NPP-375D | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea337e27-9b16-3459-b47a-ed64c27e8cdb | -15.14545 | -52.33762 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6484e39-8071-33e2-b3a3-6c7ab293d1c8 | -15.72574 | -53.64312 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7ef1efa0-0527-3803-9836-8a03be78ff37 | -20.89205 | -50.10062 | 2025-09-03 05:16:00 | NPP-375D | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7f4f0800-c502-3dbd-ab8a-e1d809d103a0 | -16.03541 | -59.76317 | 2025-09-03 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b485faa-573c-3549-a804-0467cfd8fe0a | -16.29247 | -52.96327 | 2025-09-03 05:16:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01d4ead2-cb1b-3e38-a532-c22dbb962e09 | -15.5583 | -48.40279 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea8ce9ba-a381-3688-be58-7dae0f27ad1e | -15.89852 | -48.17263 | 2025-09-03 05:16:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50c335df-3025-32ef-bce6-0cd1277016ad | -15.2459 | -53.79922 | 2025-09-03 05:16:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25a282a7-227b-3c14-95cf-037d6a7b842c | -15.55229 | -48.34642 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 417c8b56-d38f-322e-9cb9-5e94a027bd8c | -15.16475 | -52.36488 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64634e92-c366-3cc9-b21a-b15cc84682cd | -17.3606 | -49.18173 | 2025-09-03 05:16:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 094e9fe8-e7c4-3a38-b2a8-13fd1c4e05cb | -18.06295 | -46.00269 | 2025-09-03 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7f3c28fb-8b74-3d2a-be25-eccc7d259726 | -17.36102 | -49.17762 | 2025-09-03 05:16:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac06f226-37fb-33aa-a693-0098571beecb | -15.54579 | -48.35056 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b1c3e49-47ac-3fbc-9a48-d19304ac2768 | -15.15069 | -52.3658 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9683ef7c-e80d-3074-8b0e-ca8e66e207d2 | -17.94584 | -47.23069 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 31888453-c5d3-3e0e-a013-26d2c448553f | -18.65726 | -49.09223 | 2025-09-03 05:16:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d4bfb74-0e5f-389d-8010-aba3fd35bf2a | -15.90554 | -48.16447 | 2025-09-03 05:16:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 85c90367-018f-3ae5-b24f-887b99def554 | -15.72206 | -53.63852 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f4e897e-f04f-3e9d-a24d-2fa4e48f71f0 | -16.5398 | -55.07258 | 2025-09-03 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9887439e-6860-3ebd-a137-79acffb20225 | -18.66907 | -49.09395 | 2025-09-03 05:16:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85434b47-e460-36c2-a815-3355f961353f | -15.24123 | -53.80253 | 2025-09-03 05:16:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fafa316-0825-3f6f-8e5b-2fcb414a2a45 | -18.66317 | -49.09305 | 2025-09-03 05:16:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e8c8aff-0193-3129-9d6d-952cce40783d | -18.13976 | -51.74085 | 2025-09-03 05:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d78405d-4ec3-39e1-9c52-47e98ba5d72e | -17.94669 | -47.2362 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87077d64-daae-3d24-a505-b0024cbaea2e | -17.43819 | -47.20646 | 2025-09-03 05:16:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22297bdf-e7b3-347a-bf1e-bc18ac9b98f0 | -16.00495 | -56.59867 | 2025-09-03 05:16:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ea1d566-856a-3f4f-bb1f-4a557501d7fb | -17.94637 | -47.22495 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36ec6be5-be0a-35c4-adbd-683dcf690b9b | -22.18154 | -48.82683 | 2025-09-03 05:16:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 15ed5598-de2e-3013-ac9c-8bc467f6e83e | -15.56893 | -48.41619 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdb92349-2fd5-324f-8578-a53ae52b92c8 | -16.3058 | -52.96542 | 2025-09-03 05:16:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30748fba-fd5c-36e7-a28d-ebd19ffaa61c | -16.29692 | -52.96392 | 2025-09-03 05:16:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a6c39ad-e5cd-3e6c-b7e3-af5e28bf872e | -15.55331 | -48.39306 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 09967cd1-d58b-37fd-9c44-267e6ae96b82 | -22.17993 | -48.81778 | 2025-09-03 05:16:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 72b01de7-db62-391d-858e-7b7af8fbdf41 | -17.94122 | -47.22408 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca70053e-43e2-3559-b2d2-da5868742ed4 | -15.75007 | -53.68625 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 53e98c6e-e2fd-3f5c-8d8f-3efcd4e4dd95 | -19.36665 | -49.1164 | 2025-09-03 05:16:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| def004e7-7af9-38ef-9ced-acb4deca8210 | -15.58396 | -54.32086 | 2025-09-03 05:16:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80c01a2e-ce3f-330b-bd70-dc1c5688aa99 | -15.71671 | -53.64627 | 2025-09-03 05:16:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5521541f-9dfd-3d30-8470-d8b3facf8552 | -15.16155 | -52.35324 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74b7ec3f-4a41-3a55-b60f-1ff573cab05f | -15.57957 | -48.31877 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d36c65e-cfc3-3d07-a997-23daa01a2675 | -15.24174 | -53.79867 | 2025-09-03 05:16:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3952aae5-57be-3d7f-90ab-8e0962fb920c | -19.3607 | -49.1156 | 2025-09-03 05:16:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e73ce707-5b14-35c8-8765-dd2c7ba225e2 | -17.94608 | -47.24242 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3b25d155-6f9e-3d89-8563-64f70f5d4304 | -15.89947 | -48.16373 | 2025-09-03 05:16:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2aeb061-2f80-365f-8c27-e4ffe6c9acae | -18.06046 | -46.00195 | 2025-09-03 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 05a4cdf3-6f43-3343-b42d-4b4e358d4d0d | -14.32547 | -60.35635 | 2025-09-03 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21dcbcc2-8a84-308d-a7f7-0e60c5e4fbf0 | -15.14427 | -52.34663 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f272b7f-2382-3ee8-8fb8-608f4e0942b6 | -15.55428 | -48.38417 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da85cdd3-59a9-3fd7-a2e6-482b125615cd | -17.91589 | -47.21081 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd810c6c-bd84-34a0-917a-e95a536bd47e | -14.32785 | -60.34179 | 2025-09-03 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8945942f-2ede-3a1a-9653-6ac4de921151 | -16.71548 | -49.07799 | 2025-09-03 05:16:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 846c956a-8b02-3495-beb1-1fe46bfb4f2a | -15.74054 | -53.66022 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4e26fd5-029a-3305-b5a4-24987c392ace | -15.55021 | -48.36575 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9a2939af-af4d-3419-8d66-2d0471fe6ec0 | -20.94821 | -54.95791 | 2025-09-03 05:16:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd015a02-8f31-3e68-b70b-9f5559ac9acb | -15.60333 | -52.67671 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11761ae4-67a3-3bd2-9c0f-6e7cd7a0405a | -15.56291 | -48.41598 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56f108bd-3231-32d8-8e39-eccdf95e4b19 | -18.06356 | -45.99601 | 2025-09-03 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b61bbd28-de98-3924-869e-f5db9faa4b94 | -16.82132 | -52.13677 | 2025-09-03 05:16:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd9caa9c-64a5-3d76-bdc2-8a6055af8b50 | -14.84738 | -60.0446 | 2025-09-03 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b44d9c6-46e7-30c5-b045-fb9c41e38956 | -16.3922 | -50.40587 | 2025-09-03 05:16:00 | NPP-375D | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dc95995-93b4-393c-a3cb-5f8572874950 | -15.5507 | -48.36119 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6285de87-b59f-3931-acbb-322e8a15d04f | -22.6584 | -50.6699 | 2025-09-03 05:16:00 | NPP-375D | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5a079205-33ca-3894-a1fc-83db6685bb50 | -15.56939 | -48.41194 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e423869-9aed-3bc7-95e2-97b4da77c09f | -15.74483 | -53.69363 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e14ace65-d0f9-3246-a6f6-dc7422df68fc | -15.7215 | -53.64266 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8992f5e-2ad1-3c9b-865b-74efeba78532 | -18.13909 | -51.74673 | 2025-09-03 05:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4caeeb5-c43d-31ee-a94f-2472f55e09e4 | -17.54007 | -47.5841 | 2025-09-03 05:16:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95942914-daf8-3b76-9d9c-fcc8def4e15f | -15.57312 | -48.32219 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a90cdf77-12a8-3743-8c3b-0d246f99afb9 | -17.92096 | -47.21173 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b8bbbc5-548c-38ef-ab9c-243a364e2964 | -16.8207 | -52.14194 | 2025-09-03 05:16:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ea86ac2-f230-3361-a3e3-0283e5192985 | -16.19464 | -47.94484 | 2025-09-03 05:16:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1955304b-7cb7-34cf-8abb-3e58893cf0db | -16.54624 | -55.08392 | 2025-09-03 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 49f2d0eb-e94f-3aed-b63f-aeb43195c09a | -15.57354 | -48.31837 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a32b6eec-4941-3620-8759-acff6c346774 | -16.30136 | -52.96466 | 2025-09-03 05:16:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c580f24e-ae4b-3282-aca0-a761ea6613e7 | -20.9487 | -54.95388 | 2025-09-03 05:16:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddb14c83-e1f9-3daf-aabe-62fca49854cb | -15.71777 | -53.6364 | 2025-09-03 05:16:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f99037e-67fb-3508-8932-e803ed42c6a2 | -15.57998 | -48.315 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2536a74-3bca-3db5-bfe2-c3e17d47a215 | -16.53589 | -55.07207 | 2025-09-03 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| eb76d8bf-2860-302a-baa8-ae9dfe4e5aed | -17.36644 | -49.18204 | 2025-09-03 05:16:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a82d3a6c-eec5-3625-9443-0dc22779b7a4 | -15.99597 | -54.13487 | 2025-09-03 05:16:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a6f13bd-24f7-3b3e-8246-eff185d3e8de | -15.72094 | -53.6468 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e74feb0-c5f2-321f-a2a8-3158855f74f4 | -15.89899 | -48.1682 | 2025-09-03 05:16:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b54c19a6-5249-3f72-ae6a-ffb702fee403 | -16.29483 | -45.692 | 2025-09-03 05:16:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 106a092a-eeb7-3e88-8d9f-90041cf9d583 | -15.16538 | -52.35983 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e20a0729-b4b2-3602-9784-e64599e0a6b1 | -16.39259 | -50.40247 | 2025-09-03 05:16:00 | NPP-375D | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3e1e560-9f6a-3eb3-be8c-7a1c526b8b96 | -15.55284 | -48.39741 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0aafa8d4-f5c6-3ffb-83f7-767e0b1ea04b | -14.33124 | -60.34227 | 2025-09-03 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 83c34066-1107-32bc-ae33-ad5d52c6e76b | -15.54366 | -48.31367 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f81c047-2477-3af1-ab2f-74a0f50f877d | -22.17951 | -48.82303 | 2025-09-03 05:16:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5d321e80-f371-3359-8c74-1629fbc7d34a | -15.74112 | -53.68912 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15e6ad56-b28a-39bb-acdb-6bf7d5df6cf6 | -16.29861 | -45.69052 | 2025-09-03 05:16:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 95debf83-2b48-3c54-af49-c7077d96c5c1 | -15.56335 | -48.41198 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f53cf51c-bfb6-3e0f-9948-155c605074d4 | -15.59821 | -52.68091 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c27c1da0-ec36-32ce-9c4b-f32d018af18e | -15.55475 | -48.37978 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README100.md)
