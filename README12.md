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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a333475-9a04-372a-8d04-2df043cafb45 | -13.05645 | -47.81001 | 2025-07-16 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9d46271-d79f-366e-8a35-1146034e5a14 | -11.94578 | -48.41777 | 2025-07-16 03:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6337fbef-f023-3d35-97d2-197fc8a25995 | -12.47793 | -46.93316 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffa69243-20b3-3a4a-b2d3-d9e0dcdbf79f | -22.83137 | -42.06545 | 2025-07-16 03:53:00 | NPP-375D | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bba96668-9946-39ef-b003-8743c2dd83bf | -20.36445 | -46.59264 | 2025-07-16 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7ce97d71-4bfd-3a0f-9fa3-42ec63d5718e | -20.07878 | -47.64264 | 2025-07-16 03:53:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 4bcd9eaa-fa92-3545-9993-2d5f7f5e79e4 | -18.596 | -52.40467 | 2025-07-16 03:53:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8fe26082-ce54-390f-a66e-ebed549e4330 | -20.02948 | -47.39376 | 2025-07-16 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 443cbcff-1a09-3fbc-b579-681b4475065f | -20.07776 | -47.64767 | 2025-07-16 03:53:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 57.7 |
| c3ef1821-98df-3548-b44b-26b65366b43d | -20.34689 | -46.54463 | 2025-07-16 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e5e7aa4-b043-32f0-a627-c1ad99becd53 | -18.59475 | -52.41005 | 2025-07-16 03:53:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4433291b-2943-3eb2-9b36-fcfb7734cbe8 | -21.34354 | -48.62505 | 2025-07-16 03:53:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bf04607f-91de-31e3-8331-ed56549af76e | -20.07977 | -47.63775 | 2025-07-16 03:53:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 302bb3a0-7e66-3628-b094-ba7d3f1e1a9a | -19.78758 | -47.4683 | 2025-07-16 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 742c937d-0bb9-3a17-8881-6fa397a293e5 | -18.49934 | -39.96903 | 2025-07-16 03:53:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8caccdd3-bc37-340c-9a07-95cc495ae7d2 | -20.35058 | -46.54772 | 2025-07-16 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03b2c7fa-4bb0-3723-96c5-6a7d076ec31e | -21.01288 | -43.23304 | 2025-07-16 03:53:00 | NPP-375D | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0139e53a-9459-30eb-bec2-03a1df210cff | -18.73682 | -39.92353 | 2025-07-16 03:53:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5aea8368-e78c-3e81-9b08-e6f6fd22c4d0 | -20.35827 | -46.60101 | 2025-07-16 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 797c9ab7-05d1-324d-a4f0-213cb8e54969 | -21.34836 | -48.62621 | 2025-07-16 03:53:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 26f28335-cd14-3f12-b716-16a6f736a3c6 | -20.3592 | -46.59634 | 2025-07-16 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 298e33a1-656b-3510-94dc-c96185bc7377 | -20.41124 | -46.60769 | 2025-07-16 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ba80ce3-8dea-3476-9056-32ddc430a826 | -20.34598 | -46.54922 | 2025-07-16 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7522c8e-d877-3182-b7cf-a8c004169191 | -20.39 | -44.34706 | 2025-07-16 03:53:00 | NPP-375D | CRUCILÂNDIA | MINAS GERAIS | Brasil | 3120607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7e4f4bf9-859f-30f5-88b1-52827c945463 | -20.08349 | -47.64345 | 2025-07-16 03:53:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 425854aa-7398-33de-95b2-b95c770142a9 | -21.34717 | -48.63186 | 2025-07-16 03:53:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 30d336bd-469e-35c9-821e-3907eb4124bf | -20.34617 | -46.54722 | 2025-07-16 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90da44ce-e96e-32ef-b012-7fd199bb6359 | -20.08446 | -47.63866 | 2025-07-16 03:53:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 597e8ff3-f829-30cc-93e0-c0a82191044a | -21.34613 | -48.62468 | 2025-07-16 03:53:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2bb5ad47-dab0-3226-9e1a-c5393dd670b1 | -21.11348 | -48.62508 | 2025-07-16 03:53:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3ddbd478-be08-39ee-bd6d-0b742e0a77d6 | -21.11006 | -48.62695 | 2025-07-16 03:53:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e9266a9f-9ffe-3b02-8169-52aaaad9e3da | -20.08246 | -47.64854 | 2025-07-16 03:53:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 44928d7c-b4ae-3f6c-9079-292ff4b9dfa8 | -20.03063 | -47.38799 | 2025-07-16 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| de89c96c-a1cb-3335-9245-bd905644e278 | -19.19625 | -42.04054 | 2025-07-16 03:53:00 | NPP-375D | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 758628f4-2a9c-3678-b1bb-67ec2819abe1 | -21.99977 | -46.80436 | 2025-07-16 03:53:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcc2d9cd-992a-3ea0-843b-7444de9f076c | -20.03173 | -47.38247 | 2025-07-16 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8f00a259-3b9f-3d69-890a-aba7b9dfde6f | -18.58963 | -52.40302 | 2025-07-16 03:53:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 295d9796-8cab-3aa8-a27e-32dedbefbb4b | -18.41125 | -44.18827 | 2025-07-16 03:53:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 126a93b6-f511-356e-ae47-105af92721b0 | -20.02495 | -47.39243 | 2025-07-16 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b4a0df4-3d88-3d90-8f1b-6937c42703bd | -18.4079 | -44.18581 | 2025-07-16 03:53:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8029a23-db73-34ed-aa50-e16742c47af9 | -20.35035 | -46.54991 | 2025-07-16 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4c41985-e6a0-37a4-b3e8-ee0a70e75da0 | -20.38621 | -44.34628 | 2025-07-16 03:53:00 | NPP-375D | CRUCILÂNDIA | MINAS GERAIS | Brasil | 3120607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ee7ca579-8c01-3b30-80f7-8e78b0a58cf6 | -20.02382 | -47.39811 | 2025-07-16 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b4b0154-b3d7-3dbb-94c8-a5577b1f9eb6 | -21.01644 | -43.23376 | 2025-07-16 03:53:00 | NPP-375D | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9596b484-5b25-32c9-9204-5137270169e2 | -18.74015 | -39.92412 | 2025-07-16 03:53:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dfd2c946-17cf-31a7-a604-5ca52cec2bb6 | -21.34498 | -48.63027 | 2025-07-16 03:53:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7e962c4a-bab9-3be8-be36-f0f44885a35f | -21.16286 | -43.76064 | 2025-07-16 03:53:00 | NPP-375D | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b7afe575-6f0f-3a50-bd08-a0f97f7248f5 | -24.35426 | -50.82177 | 2025-07-16 03:55:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f090b5a5-afd6-31fb-bcfe-f6ed896fda2b | -22.39555 | -49.79434 | 2025-07-16 03:55:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d1c0a3f9-6f1e-3add-bdd8-102195df67fd | -23.57287 | -51.42003 | 2025-07-16 03:55:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f00ffd49-4499-3abb-af5f-19f31c2c8a4a | -24.35472 | -50.8223 | 2025-07-16 03:55:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ecfad6f7-b434-3b12-a66b-7d0ff3b83285 | -25.33562 | -52.53209 | 2025-07-16 03:55:00 | NPP-375D | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| edad24ce-9d97-37c2-9c79-5a0a28699bbe | -22.55663 | -54.95242 | 2025-07-16 03:55:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| da1c01c8-bd84-36e0-94d8-b02c04859888 | -23.5783 | -51.4216 | 2025-07-16 03:55:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 695577b0-da61-361b-9ea3-25a6f0e4b1ba | -22.39485 | -49.79764 | 2025-07-16 03:55:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 52b64ef6-d37d-3725-800e-77ce84d42c2a | -23.2191 | -45.7429 | 2025-07-16 03:55:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b84f7cc1-d330-33cd-860e-b3afd5e677fd | -22.55993 | -54.9394 | 2025-07-16 03:55:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| b6979e04-f475-3e0d-b58b-6c25bf6e9d01 | -25.3346 | -52.53641 | 2025-07-16 03:55:00 | NPP-375D | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5c508b7b-c302-300b-8052-e05fb447e6c1 | -27.15615 | -51.05018 | 2025-07-16 03:55:00 | NPP-375D | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 615961da-9ef7-3528-87d9-1db0f0898d0e | -25.06454 | -50.04758 | 2025-07-16 03:55:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bc65b2a3-45a4-38f5-a495-aa401a53d83a | -23.62115 | -47.12401 | 2025-07-16 03:55:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 764177b6-8742-37dd-ba4f-7f5e093a3c13 | -22.56407 | -54.95 | 2025-07-16 03:55:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0300ff1c-f69f-35d4-bba9-528443637d75 | -22.39635 | -49.79999 | 2025-07-16 03:55:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 276d9212-f04d-3c20-8996-4e786673a084 | -23.21966 | -45.74619 | 2025-07-16 03:55:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 34066912-3f04-37e4-bb25-d6ca473ba1ac | -25.06421 | -50.04667 | 2025-07-16 03:55:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| def2d0ed-18ea-343d-ba5e-0f2ab1450372 | -22.39996 | -49.79878 | 2025-07-16 03:55:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 53ecd56d-aa40-3ab7-9921-115c96523bd4 | -22.39706 | -49.79676 | 2025-07-16 03:55:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3cffb610-ed6d-3e17-84fc-244776ab65d9 | -22.55829 | -54.94589 | 2025-07-16 03:55:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 61228230-218c-39fb-8379-484e7dd5f113 | -22.56506 | -54.94774 | 2025-07-16 03:55:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 9cacc52d-7493-3db6-9347-2bd4c072a7db | -22.56578 | -54.9434 | 2025-07-16 03:55:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1cbb5f3c-6ce3-35fa-a320-82b5b2f942fe | -27.21147 | -50.66378 | 2025-07-16 03:55:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d7179d6b-1dc3-3299-85de-27dc45de20b8 | -21.79569 | -52.76449 | 2025-07-16 03:55:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25755f80-ff4e-32e9-b2f6-e955da779a15 | -27.21289 | -50.66551 | 2025-07-16 03:55:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 537c5ffe-c615-31c4-8a23-f3d93c7d8431 | -21.78959 | -52.76281 | 2025-07-16 03:55:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c164e93-4335-39ba-ac0b-3d07ee438593 | -20.0805 | -47.6319 | 2025-07-16 04:00:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 0ef80ba4-927f-3106-8b2b-f3b7674fe5f6 | -13.0146 | -45.0593 | 2025-07-16 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d53555d1-740a-3b3a-9a80-42993643f5c7 | -13.0339 | -45.0561 | 2025-07-16 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| dd33cf9e-007f-33c4-8075-dced767d0367 | -9.4383 | -40.3668 | 2025-07-16 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 55.3 |
| 0c334e73-79bd-3cec-bfd1-9d872f838c73 | -13.0146 | -45.0593 | 2025-07-16 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 4896f643-c66e-36fc-8c1e-3022f727ff31 | -22.5538 | -54.9361 | 2025-07-16 04:10:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 48.4 |
| 5b5fd564-148c-3f94-95ff-7cc1d0d61c0a | -13.0339 | -45.0561 | 2025-07-16 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 7022aec1-3e30-3152-9d39-52f6bbdc3fd4 | -4.30129 | -48.10028 | 2025-07-16 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2ee96d23-4e27-39d4-843f-05d2cfbf31c3 | -5.57146 | -46.5273 | 2025-07-16 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26112a5b-0cf2-39bd-8ceb-5c4227ff6b40 | -6.34127 | -43.43659 | 2025-07-16 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4e15446e-b727-3b41-a214-4a5b69d18a39 | -3.2162 | -48.97036 | 2025-07-16 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 76de2b7e-f79f-398e-9058-fed82ed9c4b5 | -6.43966 | -42.81152 | 2025-07-16 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 273709c5-5bfd-3158-980f-575ebfc6ebf3 | -5.71947 | -44.8287 | 2025-07-16 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 448f693e-f659-3d44-b93b-061ef7eb7001 | -6.34567 | -43.43021 | 2025-07-16 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9d0f4bb-98fb-3fd6-8e67-1a0ebb70a662 | -5.73209 | -44.51072 | 2025-07-16 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63d3bcdb-6389-3a19-9f86-f028cefb610f | -4.86436 | -37.45377 | 2025-07-16 04:12:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 634703aa-9bb4-39a3-a0b8-243feeec5571 | -5.78105 | -45.08084 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 955e59fd-89e2-3d21-86cf-a3759cf845d3 | -3.51674 | -47.21404 | 2025-07-16 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a5041cf-f3f8-341c-a3b9-7ac64c494b73 | -3.58337 | -47.51815 | 2025-07-16 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba72da40-8cd2-3b83-84ee-5f64f271966c | -5.78269 | -45.09259 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb0ff421-fee5-3a9e-9bbf-0b75120187c2 | -4.00768 | -49.47047 | 2025-07-16 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43d27f47-bf2b-3863-bdac-2da7f08676ea | -5.87802 | -42.40723 | 2025-07-16 04:12:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c2ea37c9-98d1-3def-8379-53e28caed304 | -5.46508 | -45.34143 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cdf2bf2-b31c-318d-b24b-deb01a70fc5e | -5.79133 | -45.08249 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e4dce5a9-b28e-3051-a5f9-3ed839e87d51 | -5.3613 | -36.89603 | 2025-07-16 04:12:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9a1a599e-b1e0-3b3a-98df-c9446500d6cb | -5.18483 | -43.20792 | 2025-07-16 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README13.md)
