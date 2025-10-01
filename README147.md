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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39f188d7-15d5-32d2-86da-d23e345c54ca | -14.81417 | -45.83412 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 225be823-5716-3b39-a346-a958fa7e461f | -15.24628 | -46.96541 | 2025-10-01 12:00:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4e49bbdc-30ff-3b70-b462-42fac8d37a49 | -15.01863 | -42.4501 | 2025-10-01 12:00:00 | TERRA_M-T | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 315bec68-8b12-31e4-af43-3099b7efa6db | -15.30467 | -45.02356 | 2025-10-01 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4a9d2b9f-4a87-3211-ab36-26b362af4989 | -18.4549 | -40.50101 | 2025-10-01 12:00:00 | TERRA_M-T | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 45.3 |
| 3ba0633b-185d-3172-8e53-938a40e3bd86 | -15.23382 | -48.74787 | 2025-10-01 12:00:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7ddaf848-08d6-307c-ae7e-39826baf07a0 | -14.80491 | -45.83252 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a3eb1ff7-2321-3943-a6cb-650020abffcc | -17.3805 | -47.15471 | 2025-10-01 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4ec22e65-019a-3aa6-8781-176df28204a7 | -14.48737 | -48.44174 | 2025-10-01 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 9a7444b8-ea5c-3665-9d90-0ca6190b9bdc | -14.49357 | -48.47344 | 2025-10-01 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 02fe3552-c6f8-3d63-9fe0-91b3a6208224 | -16.70503 | -44.97155 | 2025-10-01 12:00:00 | TERRA_M-T | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 1b5dbd43-4729-3492-be4f-c0aa904705dd | -17.97249 | -45.00913 | 2025-10-01 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c9242256-c98a-3206-b495-1caf3c62e32a | -14.49597 | -48.45859 | 2025-10-01 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4fd148fb-2b31-3bfa-93e8-e5a7e0de5e61 | -14.80338 | -45.84259 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b9849c8c-a46e-3806-8c36-4575f3d87f39 | -15.50443 | -45.90169 | 2025-10-01 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 223df9ed-5bc8-3a61-98ae-2bff4424c0dc | -15.86026 | -43.08572 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 26131f12-17ec-37d3-9101-f3a1936f59fa | -15.17612 | -46.42284 | 2025-10-01 12:00:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dcdb91b1-1077-3210-87e8-fd3efcc06093 | -14.51569 | -48.47692 | 2025-10-01 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.5 |
| cdce069a-185d-3c7e-b68e-532eabcb34e8 | -16.17781 | -46.51215 | 2025-10-01 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1bfd6b65-21ca-3e51-b4d3-7f189cba34b2 | -14.68536 | -45.27821 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 70d3a329-62a5-3947-ad99-26dc32fd60da | -18.3312 | -44.76742 | 2025-10-01 12:00:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 36c4781e-5859-3765-9518-d3577819c9a1 | -20.23199 | -43.89026 | 2025-10-01 12:02:00 | TERRA_M-T | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 96d33a21-bcef-3cda-97c8-202845fb210d | -20.12766 | -46.3368 | 2025-10-01 12:02:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 9c501f17-eef4-39fb-bbaf-16accb773483 | -22.62982 | -49.05821 | 2025-10-01 12:02:00 | TERRA_M-T | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 251b1345-e544-3744-927d-ddd1bf52dac5 | -21.11203 | -45.79683 | 2025-10-01 12:02:00 | TERRA_M-T | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 7ad226ee-b22a-3b0c-8de2-4f47a206e1a3 | -20.5139 | -47.72256 | 2025-10-01 12:02:00 | TERRA_M-T | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2035ba64-5f27-3302-84ec-7c4573589bb5 | -20.50439 | -47.72074 | 2025-10-01 12:02:00 | TERRA_M-T | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0c0b56c9-5351-378a-8084-a0469442f5db | -21.07491 | -45.61611 | 2025-10-01 12:02:00 | TERRA_M-T | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c61a570b-9b11-355d-80a4-f5477558ceaf | -22.87604 | -43.72132 | 2025-10-01 12:02:00 | TERRA_M-T | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 61a6a905-f35a-311b-9ff1-f0edc99ee29a | -22.20976 | -49.98382 | 2025-10-01 12:02:00 | TERRA_M-T | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| 239ef08c-0e84-3268-a832-fdbe13fbcd75 | -20.66437 | -45.0695 | 2025-10-01 12:02:00 | TERRA_M-T | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 5f0bc680-579e-3600-b159-53e4bbdb4bd4 | -22.12013 | -46.5894 | 2025-10-01 12:02:00 | TERRA_M-T | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 40.4 |
| 4066d67a-3d12-310b-b111-ecc126b8afc5 | -20.59229 | -45.88493 | 2025-10-01 12:02:00 | TERRA_M-T | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e7054442-5cfc-3a6b-a5e5-e8a7ceaae72a | -22.37785 | -48.32804 | 2025-10-01 12:02:00 | TERRA_M-T | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 2598f3fa-4f77-389a-846d-835bc5a15047 | -21.47305 | -46.35008 | 2025-10-01 12:02:00 | TERRA_M-T | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| ac0db5c2-6b50-38e2-a63b-9b65fbdec026 | -20.56034 | -44.83562 | 2025-10-01 12:02:00 | TERRA_M-T | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| a5ac6982-0d03-368f-aa19-4cb3428695ba | -22.21301 | -49.99039 | 2025-10-01 12:02:00 | TERRA_M-T | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 0de32a46-e43f-3618-8dfe-5492da9ab302 | -21.06744 | -45.60521 | 2025-10-01 12:02:00 | TERRA_M-T | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee6ecfe6-fb87-3c4c-bfc3-50a14028be2b | -22.11005 | -44.68921 | 2025-10-01 12:02:00 | TERRA_M-T | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 50f503ee-7b51-34a6-a321-c1918f788199 | -20.86186 | -49.4268 | 2025-10-01 12:02:00 | TERRA_M-T | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| 5a8e24a7-fcf1-391b-a2d4-e15f0dfeb7cd | -23.62991 | -46.23373 | 2025-10-01 12:02:00 | TERRA_M-T | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 5beffebc-78c6-3172-b29e-9d1feb0d673b | -21.92691 | -45.4619 | 2025-10-01 12:02:00 | TERRA_M-T | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| b8ae96af-805a-3ce8-8988-4b7d7fe831ed | -21.0763 | -45.60666 | 2025-10-01 12:02:00 | TERRA_M-T | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 5d72a2b1-100b-37e5-b2fc-115be4f1c1eb | -22.87465 | -43.73173 | 2025-10-01 12:02:00 | TERRA_M-T | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 32.1 |
| 65318c35-e142-36b1-8af9-38f62e7945b0 | -21.67431 | -46.23742 | 2025-10-01 12:02:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 3b053d59-3fba-39db-a41b-f267422872e7 | -21.57653 | -44.21655 | 2025-10-01 12:02:00 | TERRA_M-T | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 41a46a4c-e1c8-3118-8656-5daeae112419 | -18.9287 | -46.45055 | 2025-10-01 12:02:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 23e250c9-2a2f-33e9-a29d-b89459ee791c | -21.79759 | -47.19176 | 2025-10-01 12:02:00 | TERRA_M-T | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| de148c85-5669-3844-9365-86345a94dbfd | -20.63707 | -46.20342 | 2025-10-01 12:02:00 | TERRA_M-T | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f118968d-6bf2-3519-b8b3-235bf1fe914a | -22.20484 | -49.97398 | 2025-10-01 12:02:00 | TERRA_M-T | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| 0718cda0-6c1e-3107-9807-6cab60a78db8 | -19.31096 | -46.24436 | 2025-10-01 12:02:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6ce95358-5f14-3df1-ba5e-46cbdc214035 | -20.74542 | -43.49417 | 2025-10-01 12:02:00 | TERRA_M-T | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 5e223627-7d07-3dfe-ac3f-5207cbfae6d4 | -18.24396 | -47.53695 | 2025-10-01 12:02:00 | TERRA_M-T | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e367f814-532a-332b-be65-c21ac3b93b18 | -22.09871 | -44.43412 | 2025-10-01 12:02:00 | TERRA_M-T | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 2bd9b0e8-7124-30a0-9aa8-14aaf16b56b0 | -21.30737 | -45.22157 | 2025-10-01 12:02:00 | TERRA_M-T | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 944973dd-a579-3255-ae0c-7f24b9c42418 | -20.52373 | -47.00792 | 2025-10-01 12:02:00 | TERRA_M-T | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 1590d23c-de9a-36ea-b5d7-79c6e0bbe61b | -22.21555 | -49.97582 | 2025-10-01 12:02:00 | TERRA_M-T | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| cec007fe-4e32-38f7-b3fe-d879650fd06b | -18.40291 | -53.23364 | 2025-10-01 12:02:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 349.8 |
| c453768d-3a61-319d-a23e-51bba4f34ba1 | -21.42244 | -46.38124 | 2025-10-01 12:02:00 | TERRA_M-T | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 9ed62e7a-aeae-30c1-ad90-f367a983cdd2 | -20.51216 | -47.73357 | 2025-10-01 12:02:00 | TERRA_M-T | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0509ce3d-e4f5-3852-a40b-529c0f69b07f | -19.45872 | -44.28648 | 2025-10-01 12:02:00 | TERRA_M-T | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c59401db-d620-3754-ba42-9fa4c52fe7dd | -21.22164 | -43.91778 | 2025-10-01 12:02:00 | TERRA_M-T | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 73e9413d-d066-36ed-ace7-89abaf7396c2 | -20.13175 | -44.01612 | 2025-10-01 12:02:00 | TERRA_M-T | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| aaa23be1-e0b3-3c20-9c3a-5272e7e2a2e6 | -21.76784 | -46.22932 | 2025-10-01 12:02:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 9186cb65-38f1-368e-8c96-ce3fb014bf3c | -21.31344 | -45.93668 | 2025-10-01 12:02:00 | TERRA_M-T | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| 4a2930b8-e5e5-3c70-b8d2-5c3fd3aabcde | -20.38689 | -46.02519 | 2025-10-01 12:02:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 23bbba12-38d8-31c8-b0df-a47ac7ac1d1b | -21.31203 | -45.94623 | 2025-10-01 12:02:00 | TERRA_M-T | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| 76a93f3f-a049-3120-bb18-22f3a3ef9742 | -22.27733 | -46.70924 | 2025-10-01 12:02:00 | TERRA_M-T | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 46971b0f-0fe5-3d83-85f5-49cec682ede7 | -20.52215 | -47.01817 | 2025-10-01 12:02:00 | TERRA_M-T | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 6f24a83a-6bdf-3b9d-90dc-148fcb3ddbd5 | -18.85029 | -44.09285 | 2025-10-01 12:02:00 | TERRA_M-T | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ee2dbf02-f05f-3797-9bb9-ef6c8fece976 | -20.48325 | -43.93696 | 2025-10-01 12:02:00 | TERRA_M-T | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 8872a49e-719f-3f54-80a5-c5ef11501265 | -20.85954 | -49.44053 | 2025-10-01 12:02:00 | TERRA_M-T | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.0 |
| ab6f78a1-d902-355b-b52e-bc77c95ba0af | -21.92828 | -45.45242 | 2025-10-01 12:02:00 | TERRA_M-T | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 1d2840f0-0b0e-34ce-acad-72a185546a57 | -21.42099 | -46.39088 | 2025-10-01 12:02:00 | TERRA_M-T | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 3c76800b-6a27-3650-a3ed-5ec2e12273b7 | -20.12914 | -46.32706 | 2025-10-01 12:02:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dcfa0e6c-f5f1-3f0d-9366-a5e00f3851d5 | -22.12162 | -46.57962 | 2025-10-01 12:02:00 | TERRA_M-T | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 9276a10c-aade-3e40-ae6c-efe68e40eae2 | -21.45762 | -45.64524 | 2025-10-01 12:02:00 | TERRA_M-T | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 83e6e5a3-e319-3968-9213-ab231db67451 | -22.60941 | -43.65272 | 2025-10-01 12:02:00 | TERRA_M-T | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ead3714f-bddc-3d01-9966-4892a06cd0e8 | -22.63185 | -49.04574 | 2025-10-01 12:02:00 | TERRA_M-T | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8c7e34c6-74d1-3f93-90cd-82ecf1052107 | -19.16608 | -44.5288 | 2025-10-01 12:02:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 534a6457-ccd4-3e86-a2b9-ad79bd0be493 | -22.47511 | -44.02997 | 2025-10-01 12:02:00 | TERRA_M-T | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c3678868-ac60-3716-958a-209fae03f2ad | -21.22031 | -43.92762 | 2025-10-01 12:02:00 | TERRA_M-T | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.5 |
| b8139200-c1e2-36f5-a38c-d7ce82209b42 | -20.49959 | -41.67717 | 2025-10-01 12:02:00 | TERRA_M-T | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 37ba0368-e213-3372-ad73-9d2a2c2afc53 | -18.40224 | -53.24037 | 2025-10-01 12:02:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 3a7c0b3a-824b-3537-a147-c6b4a21a85bc | -22.58046 | -46.78033 | 2025-10-01 12:02:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 420a3701-a57c-3373-b570-21db6e17d854 | -20.12617 | -46.34652 | 2025-10-01 12:02:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6e95761f-690b-30c0-8850-4d08bd72c7ca | -22.09308 | -45.26172 | 2025-10-01 12:02:00 | TERRA_M-T | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| e44684ac-6d17-3706-9330-4a9e34c625b3 | -22.27582 | -46.71916 | 2025-10-01 12:02:00 | TERRA_M-T | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 0ec2316d-499e-3b27-a40e-90093fb1e415 | -21.66356 | -44.18618 | 2025-10-01 12:02:00 | TERRA_M-T | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 6bf23dea-2b8b-3d60-a5f9-471fe1b5e4db | -19.68056 | -49.23664 | 2025-10-01 12:02:00 | TERRA_M-T | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 323da974-fdd0-36ce-ba8e-a0a5ade4213c | -22.20224 | -49.98882 | 2025-10-01 12:02:00 | TERRA_M-T | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| d4c89205-5711-322d-94fe-3524cd19e2d8 | -21.65647 | -45.98882 | 2025-10-01 12:02:00 | TERRA_M-T | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 1f3240de-a7fa-3031-b4d8-65166a637084 | -19.60477 | -44.23461 | 2025-10-01 12:02:00 | TERRA_M-T | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8020aaa4-28ec-3194-825d-f130dae55596 | -20.44931 | -45.35583 | 2025-10-01 12:02:00 | TERRA_M-T | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 25908238-9248-3f7b-8390-dc0dea750441 | -8.483 | -47.7983 | 2025-10-01 12:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 49333174-d999-3a7e-b456-ce69229ce684 | -8.8609 | -47.6521 | 2025-10-01 12:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| df80801f-b1a4-33f5-8458-43630fe64440 | -10.1084 | -50.299 | 2025-10-01 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b4129c09-9aab-3047-b38b-f4438ac0ae50 | -11.8482 | -48.0595 | 2025-10-01 12:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 329e7fd1-0965-33f2-90aa-6f427fb86b82 | -9.9376 | -43.6953 | 2025-10-01 12:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 2be7cd49-60a1-37bd-919c-9b1a4722072d | -11.8622 | -45.0075 | 2025-10-01 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |


[Clique aqui para ver as próximas entradas](README148.md)
