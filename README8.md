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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7464d6a-05f8-395c-9e8f-5cdcb0b75737 | -11.59986 | -47.44675 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 87190b80-9d40-3757-9885-e98f9bb80ee0 | -8.71327 | -47.91676 | 2026-05-29 04:55:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1f1b73d-1881-376d-ade2-f7a77884a59b | -10.51966 | -48.10778 | 2026-05-29 04:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34133030-f169-383e-8dd1-38a6277e78f4 | -12.00705 | -45.35727 | 2026-05-29 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6ad7fb3-17c0-309d-8b40-7d8f70479c0b | -11.47173 | -57.11273 | 2026-05-29 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9524c2bc-3fe2-3378-81ff-2d1b7097ee4b | -11.78819 | -52.51484 | 2026-05-29 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dde67e13-6e58-311e-9540-b5558eb4e5a6 | -11.63567 | -56.8654 | 2026-05-29 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 757ec41b-be4e-3ea1-9648-c7398530dafa | -10.81628 | -56.59525 | 2026-05-29 04:55:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25963c29-0389-3d06-9edd-564df69437e0 | -11.59279 | -47.43847 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d36cb88c-b74d-3a3a-ad01-2d9ac65636ab | -10.13502 | -52.40145 | 2026-05-29 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a3aab65-8e08-3540-9e05-bdcb0370fad7 | -10.91167 | -54.11954 | 2026-05-29 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4064251-cf40-320b-b981-b2d6c2937772 | -11.79383 | -40.07926 | 2026-05-29 04:55:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b97467fd-9f9c-318e-9bb7-5c9b8bdfd745 | -10.8214 | -46.89621 | 2026-05-29 04:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5f94e8d-b07a-3393-909d-640c8e54cdc9 | -11.60131 | -55.33129 | 2026-05-29 04:55:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99c6fdb2-6aec-3af8-b388-181c5deb81de | -11.78486 | -52.51429 | 2026-05-29 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2db60a9-2c9d-3d86-a7c5-8ec9bc779d95 | -11.58423 | -47.44087 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72fcc7f4-5118-3467-866f-faf201c5b67d | -12.20787 | -47.50106 | 2026-05-29 04:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 344874c3-502a-32fb-b96b-515365c569f6 | -8.68709 | -48.30156 | 2026-05-29 04:55:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d39877df-f1ca-3efe-9aa2-9150f38b0e4b | -14.44513 | -48.90479 | 2026-05-29 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 215f2f94-aec0-3ebd-a7eb-dbbbb96bcec2 | -11.56329 | -54.58271 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56aa9ab8-a48c-3116-ac6c-ef44c7c2d741 | -8.72709 | -47.82544 | 2026-05-29 04:55:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad077582-eae0-333a-bd43-974712cda053 | -10.14358 | -52.13284 | 2026-05-29 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ebaa79fd-e4db-3e3f-8cf6-a187e237ca76 | -8.23728 | -46.36357 | 2026-05-29 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5090738a-a56b-38ea-a3a5-46fdef5a3678 | -11.58826 | -47.44147 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35ef9b36-b864-3767-9fea-a3da5c06ab89 | -12.00139 | -45.14305 | 2026-05-29 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90a0b189-c928-34c5-bca8-f1edac2ddb8d | -11.56108 | -54.5744 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85006aa5-d0be-3f08-8dad-919fa6481e60 | -11.89206 | -47.60564 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c01909a-0e6d-3913-a936-b8a538b55338 | -11.79063 | -52.51507 | 2026-05-29 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2e880df-6ffa-3104-a6b0-8ba1ad3d4f22 | -12.2648 | -48.80659 | 2026-05-29 04:55:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 330898ac-2043-3735-8ced-dd567587790d | -8.7154 | -47.80013 | 2026-05-29 04:55:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49cffc36-945f-34bc-bab5-98bb63bb8629 | -16.17204 | -58.47042 | 2026-05-29 04:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 428a0c3b-43b1-3835-b25d-b5ea7910dfb3 | -18.45942 | -54.7111 | 2026-05-29 04:57:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e618f6f-46bb-3e8c-b3e3-c8334a0f5dd8 | -20.89848 | -46.79321 | 2026-05-29 04:57:00 | NPP-375D | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39667f8a-8b61-367a-996e-4e93c3076194 | -18.46276 | -54.71169 | 2026-05-29 04:57:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e670b194-2c27-3306-8394-d94b3a675bbd | -15.90607 | -50.55473 | 2026-05-29 04:57:00 | NPP-375D | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c09fa91-97c1-3c4c-9464-b03757e7db5c | -20.89908 | -46.78781 | 2026-05-29 04:57:00 | NPP-375D | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1bf9cfd1-1b34-31ca-8098-ea647245a96b | -19.68277 | -54.35384 | 2026-05-29 04:57:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 115855ef-d8ed-331f-b30d-ddd927d5abd2 | -18.2378 | -54.59366 | 2026-05-29 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c572ca75-87b0-37a4-9945-4b822ba0ac45 | -19.68668 | -54.35075 | 2026-05-29 04:57:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13d20609-831b-39dd-bc6f-624840047560 | -16.16517 | -58.48565 | 2026-05-29 04:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 24acdc90-b819-3130-9b70-c5e8235a196b | -14.65054 | -54.52457 | 2026-05-29 04:57:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a70aab9-b73c-3583-9a84-720e0e87fbc1 | -21.38336 | -49.2639 | 2026-05-29 04:57:00 | NPP-375D | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8360004b-7247-314c-ae5d-5612d11fc3a8 | -21.14281 | -48.65375 | 2026-05-29 04:57:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 56055e18-cc4f-3771-bfbe-e8e4583c1402 | -16.1671 | -58.47498 | 2026-05-29 04:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f2ec0d17-1656-3f3f-b592-ec43f18279c8 | -19.6861 | -54.35443 | 2026-05-29 04:57:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a272d938-56c7-3d71-ac4c-7c9d3997e04b | -20.08305 | -47.45024 | 2026-05-29 04:57:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2eb040f4-2776-3fc4-b3e6-febfe93b7441 | -20.08757 | -47.45096 | 2026-05-29 04:57:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d2aa93e-655f-33a6-8f8b-12fa7fa925b2 | -18.1178 | -54.5163 | 2026-05-29 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca789a8e-d632-3098-b7ba-24182ac8cdc2 | -16.17505 | -58.47655 | 2026-05-29 04:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| a2764e51-fc0d-3556-ac45-cc298a0854c9 | -22.79327 | -49.33944 | 2026-05-29 04:57:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f4674fc-52bd-3fe0-bf16-76759cce88ce | -22.24368 | -54.15535 | 2026-05-29 04:57:00 | NPP-375D | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| addef628-1e56-358c-9b03-bc809d99e1cf | -18.46336 | -54.70803 | 2026-05-29 04:57:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b5bd644e-6c5c-3b03-87a1-74458fd379b9 | -16.17108 | -58.47576 | 2026-05-29 04:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| ed227c5b-d5c4-3454-a1ad-bd5e610728b4 | -21.81202 | -53.08506 | 2026-05-29 04:57:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c99d5df0-ba5e-3051-8559-4c0bc5925f0d | -18.4667 | -54.70862 | 2026-05-29 04:57:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6c41be13-ec44-3627-bc89-a9c8cebf0093 | -19.06101 | -47.42304 | 2026-05-29 04:57:00 | NPP-375D | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a48ff511-45d7-3013-9491-deb92de9f1d3 | -21.81261 | -53.0811 | 2026-05-29 04:57:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45011513-36b7-3e86-8f13-929d98d2b9b6 | -18.46001 | -54.70743 | 2026-05-29 04:57:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e56f4fab-b457-35a7-9b94-a6d4f2c69377 | -21.39585 | -48.71324 | 2026-05-29 04:57:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67d6969a-6198-35ad-bf41-38075147513f | -18.46611 | -54.71229 | 2026-05-29 04:57:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e8b63136-e409-3897-a1ef-0d427e3f091f | -21.4001 | -48.71387 | 2026-05-29 04:57:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7db8d2e2-fb35-3f4e-9bda-7eb6c8930462 | -22.79461 | -49.3382 | 2026-05-29 04:57:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a13716c6-2c12-3da2-97d8-0dc4a71951a7 | -16.17601 | -58.47121 | 2026-05-29 04:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 970d4290-a852-372c-8968-f532f2c3fc3b | -19.17571 | -47.35593 | 2026-05-29 04:57:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3a98556-51ba-38c6-a2ff-3c6fdba5a553 | -20.18967 | -49.56339 | 2026-05-29 04:57:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2b6684bb-e6b1-30d7-8f6e-932f78878d86 | -16.17409 | -58.48188 | 2026-05-29 04:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 3dcee6a4-6e54-3e7f-8f92-af24432b8eb8 | -19.17119 | -47.35545 | 2026-05-29 04:57:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ceddd77-0fb7-3199-985e-f4b76e729eaa | -16.16806 | -58.46965 | 2026-05-29 04:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 078b0617-e3ad-3fbb-91ef-530f473c5068 | -22.0538 | -56.21568 | 2026-05-29 04:59:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ba1b9aa-1a6f-3eb4-ab5c-2ce00caa07e4 | -11.591 | -47.4496 | 2026-05-29 05:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 3d496382-6944-3f5f-9c7f-a7e1d993c22a | -11.591 | -47.4496 | 2026-05-29 05:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 22011a1e-70a8-3e9f-b85c-81db697b4f30 | -5.32043 | -44.69029 | 2026-05-29 05:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88506426-c7b1-302b-a56f-f68711444115 | -5.32235 | -44.68953 | 2026-05-29 05:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0d49ce1f-1fac-39ff-913f-e78ed10966f0 | -5.327 | -44.69145 | 2026-05-29 05:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 41f226da-154a-36e4-8cba-de30ae93e328 | -5.32891 | -44.69066 | 2026-05-29 05:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44772c0b-5854-30ad-b800-c16080d2adf0 | -5.32123 | -44.68445 | 2026-05-29 05:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b1badd2-a206-32c9-a85d-2627ae4f005b | -5.32779 | -44.68567 | 2026-05-29 05:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f9da34e6-571f-3b7e-b599-629dc2d82361 | -7.61825 | -56.73668 | 2026-05-29 05:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a66f0c5-b342-3c23-956f-ba5ba9dc2681 | -8.70642 | -47.80222 | 2026-05-29 05:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2626fb33-7c50-303e-9844-6ce454686e32 | -11.62727 | -56.86192 | 2026-05-29 05:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ebf976df-10e1-32cf-882c-3e0225819f07 | -10.81743 | -56.59869 | 2026-05-29 05:14:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be40b85f-b77a-34e9-8beb-4e7f38bedb53 | -11.59158 | -47.43635 | 2026-05-29 05:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5b9c3466-f745-395b-b7d1-3058f26659d7 | -6.25073 | -48.56636 | 2026-05-29 05:14:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7555f55d-6d2c-325f-b3ab-5232016e08db | -11.59705 | -47.4417 | 2026-05-29 05:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f1dd1787-2b84-350e-a6f3-3048062f48d7 | -8.87385 | -48.50118 | 2026-05-29 05:14:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74ca2f4b-983a-3e24-ad56-7738d18b35f0 | -11.63745 | -56.86353 | 2026-05-29 05:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fbffef9c-819a-30d0-a603-047c2dd383a3 | -9.16206 | -46.86376 | 2026-05-29 05:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1352ad9-f36b-3302-ba4a-d3b803096aeb | -11.63406 | -56.863 | 2026-05-29 05:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f66984db-670d-3a78-b898-3bfe64ca4f3f | -11.63769 | -56.86723 | 2026-05-29 05:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d9f6e82-7786-3642-b77f-1194a81a8808 | -11.30275 | -54.02832 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e75833f-624f-38e9-b73a-afd8f05bc684 | -11.59592 | -47.4509 | 2026-05-29 05:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8014f3c0-ccea-3012-96ed-c2b369e7ff07 | -10.65736 | -49.72589 | 2026-05-29 05:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cebbd94-60fd-3d0a-a11f-9922d857c8c9 | -11.59045 | -47.44566 | 2026-05-29 05:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 31fb1c69-4995-35ee-baf2-a8b57547a2ab | -8.70997 | -47.7999 | 2026-05-29 05:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcf7f762-2abf-35b6-bf6b-635f6e7b7503 | -8.89301 | -51.85587 | 2026-05-29 05:14:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fd1c800-e062-3f3d-8803-d3fb65767729 | -8.71663 | -54.98994 | 2026-05-29 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a019e5bc-a933-3da4-8630-468e6a3eb1a0 | -11.56062 | -54.52738 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a19bac21-7edd-3ba9-9425-fd9fb6fa19e1 | -10.51783 | -48.10521 | 2026-05-29 05:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75736d0e-a3ee-3960-a014-d291ba50e32b | -11.58989 | -47.45026 | 2026-05-29 05:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 46f5cab3-9111-3066-8032-27bd23627e3b | -7.33644 | -49.85781 | 2026-05-29 05:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README9.md)
