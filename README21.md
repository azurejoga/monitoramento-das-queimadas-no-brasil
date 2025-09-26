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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13020f32-a439-3d91-953d-4d93c1393ec2 | -13.37531 | -43.64063 | 2025-09-26 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 674d7cfb-170b-3643-9336-e299f146561b | -13.77518 | -42.74096 | 2025-09-26 04:17:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b62692a3-1fd0-3168-a4da-b582845080e9 | -11.61804 | -44.43285 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| af86319c-d0a0-3706-8c16-9d6917759864 | -22.61125 | -49.02256 | 2025-09-26 04:17:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8d3ef26-1eb0-3c4d-a7f7-7db7636994cc | -12.87391 | -44.7089 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3748b10e-048f-3efb-a41d-e016bcd685eb | -11.97811 | -46.6233 | 2025-09-26 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ca7d83c2-55d1-335c-9c08-5118804d105a | -14.82904 | -52.9238 | 2025-09-26 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e83edd81-7643-3d4a-93fa-d395af4a3812 | -15.54007 | -44.3361 | 2025-09-26 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3a7857d3-e128-34ff-83b5-aef06cb25804 | -11.78732 | -44.91262 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e0ab869-6a74-39a7-b58c-b2fe691ccd72 | -14.95879 | -46.76239 | 2025-09-26 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5064534f-d59f-38d6-bac7-10280f96be51 | -11.39892 | -44.93564 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 027bf2af-572c-36eb-80f0-4a5b635a33ef | -14.80319 | -45.40359 | 2025-09-26 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c0edccb-b7f1-3886-a97b-d97f114c7247 | -12.0509 | -44.85868 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b503ef8-ae7b-3e7b-bee1-b7d73e5dcc51 | -11.69722 | -44.40255 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd61939c-d5e3-33a8-965d-6cbd2f9bf157 | -11.02441 | -44.33296 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc4b7b5d-aaba-3cd6-8ae6-7ffbd845353e | -15.53674 | -44.33556 | 2025-09-26 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 50059dfe-cad4-3376-baa3-25f7764e949c | -13.83885 | -45.62593 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d30da2cb-4e58-3ee1-a332-dcb648db7233 | -14.04045 | -45.49146 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a316413-79ca-3861-9102-e87e7bbd3f1e | -13.25222 | -50.66049 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b63505c-4327-3a49-9cdc-2aa2fb02c000 | -20.99552 | -50.01329 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d878cbe1-7a71-311a-958d-4ad3e6cfea0b | -16.30974 | -48.73098 | 2025-09-26 04:17:00 | NOAA-21 | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 594216f9-c484-35a9-b5d0-b2b2e6fa3efe | -11.78676 | -44.91611 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 765d7a71-303a-3bd9-80d9-a33b22161e09 | -21.00629 | -50.01551 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| dd2b5ea4-f88f-307a-9f84-13872400bfc6 | -11.42725 | -44.97267 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fda3582c-b900-310d-bf74-fe43a3ae3403 | -12.56415 | -45.84782 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 60c75d09-dca7-38a5-906c-d4c44b6c9226 | -14.95499 | -47.50289 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e18443c-bf54-3391-84be-c492cb558316 | -11.24647 | -45.54855 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 001e3bc7-3811-3368-99ab-3407f44ee4bc | -11.23135 | -45.55716 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44edc523-f8de-3b16-990f-af901c4a33cb | -21.84455 | -50.57629 | 2025-09-26 04:17:00 | NOAA-21 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 715a4281-c10a-3980-8687-d806af3d0b09 | -12.87666 | -44.69133 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad3bddda-1d6e-3011-8867-0e295846f049 | -12.35126 | -44.35372 | 2025-09-26 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f31fc30c-c100-3f05-b34b-580014f05344 | -11.19379 | -46.30305 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf76ccf9-3c87-32f3-bbdc-2dba5a19f9f5 | -11.01015 | -44.33776 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3eabf08a-3a77-376b-b1a6-01a76df79ccf | -11.23862 | -45.55465 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 265.9 |
| ec53c545-8058-3c61-a615-a321f9563d56 | -20.99472 | -50.01781 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| dcd3df62-9980-3647-a657-01721b055c2e | -11.02111 | -44.33243 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d31998bd-f5d5-355e-a833-86bca5cb038a | -11.68733 | -44.42247 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74b43355-098d-3561-948c-73e4c843925c | -17.59813 | -48.55784 | 2025-09-26 04:17:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb787f56-2a1d-3cc0-a801-692cd8556359 | -15.07053 | -44.97882 | 2025-09-26 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7c8ac6f-4890-32a6-97b1-c035d2eb97e6 | -12.37025 | -44.14447 | 2025-09-26 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6e80110-a12b-3626-80ba-31a6bf6c4439 | -21.03489 | -51.11773 | 2025-09-26 04:17:00 | NOAA-21 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| ff7f584f-4548-33df-bdbd-1c6e2a287b32 | -12.06743 | -44.83976 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bff5b41f-b205-3ede-98f0-9735d40d16bd | -20.61223 | -56.73523 | 2025-09-26 04:17:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9e19869f-7a51-30a3-8031-fa7e6ca2cf9a | -15.5125 | -50.42041 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c38341f-24d4-3f8b-8a77-4e088934336e | -14.29959 | -43.84567 | 2025-09-26 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01352f8e-3dfc-3426-a7cf-604a142c66a9 | -15.06998 | -44.98237 | 2025-09-26 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d9bf375-786f-387c-be34-2fbf2a9699d2 | -21.03397 | -51.12278 | 2025-09-26 04:17:00 | NOAA-21 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.1 |
| 68c590d3-d63b-3ba5-8b96-e846738172af | -11.48775 | -47.32396 | 2025-09-26 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e68bcf5-1dba-3511-bf8b-f2a7676774c4 | -11.78621 | -44.9196 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 759c7345-db9d-3bcd-a05a-f0331af4da58 | -11.23469 | -45.5577 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50770e01-5e05-3a24-81ff-2c50687c9272 | -11.61619 | -42.11116 | 2025-09-26 04:17:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb7abe12-e713-3e8c-a1e4-88c036d5a50f | -15.51613 | -50.4331 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 175b90c4-c5d3-393b-86c2-b63fc3c64228 | -11.61032 | -44.4347 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 567c82e7-1bca-355f-9625-f02d0d200e10 | -12.05972 | -44.84569 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10a8514d-7dfb-3072-9ea0-86f056d8df51 | -15.13886 | -46.43322 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65aad62f-13f5-3c3a-aebd-5cbeb5f7133e | -17.03138 | -52.23973 | 2025-09-26 04:17:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 645926dc-f48f-3957-af03-e85bbe73336c | -11.24428 | -45.54081 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7fdf7db-ae58-3070-925a-f4ef369c5028 | -11.98127 | -46.60402 | 2025-09-26 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9923663d-3495-35a4-8272-6c80b70c208d | -17.87107 | -48.78991 | 2025-09-26 04:17:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ae8e3c41-d754-303b-8929-26dc5ee0fdbd | -11.00136 | -44.35066 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29bc094f-25fe-3b37-9de5-5212ecbe8213 | -15.51515 | -50.42873 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 821254d5-ac56-33d2-bdbe-f617e2d91c6f | -15.26701 | -51.46989 | 2025-09-26 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d8657e77-f0df-396b-8166-e936d4132516 | -10.62834 | -53.89195 | 2025-09-26 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d82e4f05-440f-3b63-a597-a4e09aef214d | -22.20325 | -54.83904 | 2025-09-26 04:17:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dc15bd72-dcae-3cee-bb41-475451bc736c | -12.05258 | -44.82656 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50af1acc-817c-3a35-a8a9-159819db2c9b | -12.37301 | -44.14852 | 2025-09-26 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 720d7746-6f91-34c1-abc4-c5ae6a7a9760 | -11.97784 | -46.60345 | 2025-09-26 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bceae35-e347-3cf5-9487-5b33d322a8e9 | -15.51381 | -50.43632 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7a5a4265-009a-3566-8bc0-906a65c70418 | -15.58782 | -51.69627 | 2025-09-26 04:17:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7caf6c5a-c96b-3d2e-b1e2-b33656883431 | -15.51448 | -50.43251 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d4d521c4-389f-349e-ae71-7e5d97648c9a | -15.59466 | -46.45873 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dde73e52-dc5a-39b5-a86c-804a1b313bbd | -22.40518 | -49.63408 | 2025-09-26 04:17:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f884ca9c-037a-3028-9f3f-22c4a3a1e5ae | -11.24763 | -45.54136 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0fa910c7-dc62-3193-808e-712429be23be | -12.86015 | -44.60216 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc2b855e-029c-3d09-9ed1-a5243f914b82 | -11.96485 | -47.88007 | 2025-09-26 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ea8d228-9b3f-3068-a1a5-e21dd172ad29 | -17.03143 | -52.24257 | 2025-09-26 04:17:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ae9d236-a408-3f67-bae0-ca1f63801ece | -15.27249 | -46.42958 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f9d3cf3-4d76-341d-9916-ec5fee2c1c6e | -16.22095 | -48.80795 | 2025-09-26 04:17:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1062290-82b6-3ff3-bf59-23bfe2d8951d | -11.96046 | -47.88384 | 2025-09-26 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4f8baff4-5d89-39f7-91ec-756202bc5532 | -11.68239 | -44.43244 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3e50f53c-1a0c-334e-a384-3d51b64f4900 | -16.85535 | -50.49826 | 2025-09-26 04:17:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a541506c-7ff7-3ee7-9ef2-b86e62d5d19c | -10.86744 | -47.78989 | 2025-09-26 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 85dbaa22-bfba-373b-835e-07479182b1f3 | -13.54296 | -47.70473 | 2025-09-26 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ae0a684-365f-3709-9cca-357ffe64e6d5 | -12.56473 | -45.8442 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 70e9d3c3-1b55-3d7f-87ef-2609ee548365 | -20.55874 | -57.08014 | 2025-09-26 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f7027df-fed3-3c42-b360-f3b6b708fb91 | -20.99911 | -50.01403 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 74be0e35-54bc-34d9-902e-607635614c6b | -11.70597 | -44.34656 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 04ac1622-19c4-3658-b896-056fa5364d81 | -11.23745 | -45.56186 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7724e1cc-52bc-37c9-b441-70aeefffbcb6 | -11.68512 | -44.41495 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57f85eb6-0e38-3b3b-94e1-786fae9338ed | -13.85825 | -45.6109 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59fc6e82-faec-38c5-880b-6ead95099e5a | -11.02499 | -44.35087 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8535f301-3370-3f9b-9ae4-6f09af8126ec | -21.03869 | -51.11852 | 2025-09-26 04:17:00 | NOAA-21 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 51a75134-5c4d-3a9b-818f-68af5d0208e8 | -10.628 | -53.88834 | 2025-09-26 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27c94784-1815-3999-bd42-d1a4fa1577f4 | -15.03151 | -46.9397 | 2025-09-26 04:17:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ffa42d4-6c40-3d70-bfd8-6bb26664cdb5 | -11.41383 | -44.92718 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a20f302-53e2-3464-a43e-9a247973cb70 | -11.24588 | -45.55215 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| c4e8f7d7-0570-329e-a7bd-0d75017a84b8 | -20.99247 | -50.47205 | 2025-09-26 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 93891849-7bbb-3829-926a-3815bdb6290e | -12.77272 | -47.50773 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce283efc-88c2-3925-966b-794c3d4a013b | -22.41284 | -50.64536 | 2025-09-26 04:17:00 | NOAA-21 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f9b2b73-4c8f-3861-92db-0f208ed41bdf | -15.51818 | -50.42196 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README22.md)
