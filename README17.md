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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7eb7d0f-74aa-3bff-a598-dca6c0d22847 | -14.28888 | -51.9696 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c813d709-f2b8-3453-b618-21ff33b1b5c4 | -18.4774 | -51.74841 | 2026-08-14 04:17:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9c38e56-c49b-3e7b-801e-d0e0feee5c49 | -14.03557 | -53.58444 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73b639e6-e293-3bb0-a009-ff8089d38f14 | -19.94889 | -45.55083 | 2026-08-14 04:17:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a87ec3f-2be0-3174-ae8d-e3e4b6c9e587 | -19.9496 | -45.54674 | 2026-08-14 04:17:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f44f44cb-7471-35bd-bbb7-7a74b13f7551 | -20.46736 | -45.94315 | 2026-08-14 04:17:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b604f00c-3869-3ff4-b922-50cccddc91ad | -20.26445 | -46.71693 | 2026-08-14 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2acf2114-c3c1-3ac7-b233-007b7b0bbdca | -21.28175 | -45.96664 | 2026-08-14 04:17:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ae25ac3-ee8d-33dc-8e26-379cbc693a7f | -17.7442 | -50.87675 | 2026-08-14 04:17:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5cf20a2-d157-361d-b9de-ddabfc80df8a | -16.33842 | -50.45248 | 2026-08-14 04:17:00 | NPP-375D | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 848b8f3c-f5ea-34a2-a307-5b48687356c4 | -15.16578 | -52.80488 | 2026-08-14 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76b59676-cc9d-32f5-90e2-165175d67989 | -14.71938 | -52.89975 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9906bf64-b857-37ba-98e5-2d522b1b5ce2 | -14.44055 | -51.867 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a58a036-c59d-36ce-9edc-6a9bea91e90c | -18.21905 | -44.40132 | 2026-08-14 04:17:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 167ebe7c-74ac-3df4-9d15-e9f09896d558 | -21.74878 | -44.03012 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e5f7ec2e-31cd-37df-bcbc-bd957444b6da | -17.51087 | -42.37805 | 2026-08-14 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdecb91b-b381-3e1a-9533-42a2e99bb50d | -13.92594 | -53.9542 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 201fe58b-3822-3fa2-aa24-6af4e014604b | -16.91465 | -54.14756 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab9bd869-62f2-3df1-acf4-73a829320eb1 | -14.34557 | -53.31066 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2e1ab60-e545-38cc-a1f5-0b6c0f512f16 | -20.26103 | -46.71368 | 2026-08-14 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8dcee0f-1c97-3ca5-b5a8-2ddb66238121 | -14.06669 | -53.61094 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9860f094-105a-3052-847d-6c76148771b9 | -21.7769 | -44.04678 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9b14dc6e-0476-3668-8729-b3d32c730aec | -15.51997 | -45.85813 | 2026-08-14 04:17:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ee3c687-87c2-393b-bdde-9e5488800084 | -15.86371 | -43.29421 | 2026-08-14 04:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2e0666b-eeb3-3e65-a049-58706af3887d | -14.04027 | -53.58412 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 284deea0-2d72-331f-b681-1de4683f46b1 | -20.33873 | -46.7415 | 2026-08-14 04:17:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41facbcc-c8c2-3335-ae5e-01206da28018 | -22.00783 | -47.21456 | 2026-08-14 04:17:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2003b1eb-142f-3ca3-86cc-5197cbff7087 | -21.53848 | -45.67733 | 2026-08-14 04:17:00 | NPP-375D | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae53412d-f3d1-3715-a536-88ff7aafd4d0 | -15.16522 | -52.80617 | 2026-08-14 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc2a78c8-4cf3-35ff-848e-0d09a467ac84 | -17.12225 | -51.69051 | 2026-08-14 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31dc1bba-bc49-3894-8d9d-c39b468faef2 | -16.25218 | -53.71314 | 2026-08-14 04:17:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f4a5ab2-d5e1-3339-9341-99667442f2cd | -15.69731 | -48.3186 | 2026-08-14 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1c5ac82-9a11-3495-a1b5-ee5477e93205 | -14.72278 | -52.88924 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d422b09f-4018-390d-911e-c98440bacc5a | -14.46376 | -51.92239 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32e8515a-5a40-3e06-a837-449bca139dde | -16.87997 | -54.13269 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19494d3b-b39b-37b4-8a57-bf86667f7edf | -14.35964 | -53.6935 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4410a29-0de5-30ee-93d7-9e21b67e7182 | -18.41473 | -45.19177 | 2026-08-14 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc0355ff-4c67-3a41-af28-c675b5e55660 | -18.16668 | -43.98106 | 2026-08-14 04:17:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2257253b-a3da-3b11-b26d-7cd480c8a8c3 | -14.71454 | -52.89392 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d4563a8-3a3a-3832-94d1-1230052a4ea1 | -18.55313 | -48.18216 | 2026-08-14 04:17:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36309765-8f6e-3307-a3b8-0b50081951ab | -14.05243 | -53.58731 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ec0568b-5f98-3edd-8b7a-a0d5787ca5df | -18.42164 | -45.19322 | 2026-08-14 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 855a2a09-095b-393a-bf85-fe10bb5c4bc8 | -21.76028 | -44.04372 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 819b3aa2-29ea-3ab3-aa53-0f5a09162115 | -15.12234 | -48.66049 | 2026-08-14 04:17:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65a249b4-2997-3865-8b1f-ad94a5971aaf | -17.50754 | -42.37749 | 2026-08-14 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60b0eef3-a05f-358b-b79c-7ba1a70a1a57 | -18.85673 | -47.0691 | 2026-08-14 04:17:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91531c35-5652-3844-897c-f1f57417f720 | -16.91354 | -54.15272 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 885bddf2-bf0c-31fa-8719-0bae7df8c530 | -18.41819 | -45.19249 | 2026-08-14 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9edc0a09-41fc-3e72-864d-3a02d567b199 | -14.0566 | -53.65858 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6d19f6c-19ad-338f-a6fd-961ea691fe1b | -21.73888 | -44.07045 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9eba1ddf-8313-3763-8581-16fef514fa53 | -17.66329 | -44.48281 | 2026-08-14 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e06b63f7-d066-3fb1-a6b1-2b1812737474 | -20.36282 | -41.4953 | 2026-08-14 04:17:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4e19bf4b-f28a-34f7-9bf5-bfbc7d393b02 | -21.90016 | -55.36303 | 2026-08-14 04:19:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d5eb296d-0983-3af1-8a1f-c05402e0b46a | -21.89911 | -55.36751 | 2026-08-14 04:19:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e2a1f3e9-8b25-3c70-a487-4d7580539c0e | -23.30937 | -47.54059 | 2026-08-14 04:19:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9fc8c4c9-2114-3ca3-9ac5-9ff22ecbc2e7 | -23.33094 | -46.21087 | 2026-08-14 04:19:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1331b66c-8608-3d52-8aef-62d95bd4b627 | -22.92093 | -49.21229 | 2026-08-14 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c6cb02c-54bb-342e-a2fb-fcd81b67b3bf | -22.92201 | -49.20663 | 2026-08-14 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46c97696-4362-33f8-a2ee-bf3a0fe4aa57 | -21.89703 | -55.37635 | 2026-08-14 04:19:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2763a415-8a9a-3847-b9d5-623bad6d6705 | -23.19019 | -49.15667 | 2026-08-14 04:19:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2195165-f670-3e1d-803e-f885b8b4dae4 | -21.89218 | -55.37057 | 2026-08-14 04:19:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90ea5e9b-c249-34d7-9468-04dd5884dfea | -22.91696 | -49.21142 | 2026-08-14 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c48f693-7049-32b8-bd65-d8d670ab0231 | -23.19291 | -49.15287 | 2026-08-14 04:19:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e92044e2-8c34-32fb-b870-40b6c5303811 | -23.31299 | -47.54137 | 2026-08-14 04:19:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c36c9f86-fa75-30d1-bc15-81b9a328fe6f | -21.905 | -55.36886 | 2026-08-14 04:19:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a71127cf-96b1-372a-a70d-1bb476ecbce3 | -21.89806 | -55.37196 | 2026-08-14 04:19:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f05c46d6-cbb3-35fa-aedd-ca0c405ae9ad | -23.21101 | -45.953 | 2026-08-14 04:19:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9e26b6aa-66e8-3392-9dd2-3b459434475a | -11.4885 | -54.6273 | 2026-08-14 04:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| ee167257-ee18-39b2-8d2e-b969834734bf | -13.6859 | -46.2624 | 2026-08-14 04:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| f591c2db-6c91-3a1b-82e9-589c1330ccbe | -6.6195 | -59.0416 | 2026-08-14 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 97cadbea-3ae2-346a-8ada-a8a0ac307275 | -2.90747 | -40.39086 | 2026-08-14 04:29:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0bd83ac8-963b-3041-bfc6-15b3ac166fd7 | -2.64591 | -47.9865 | 2026-08-14 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bda5c8ee-f4df-374d-824a-a6431f35d6eb | -2.64366 | -47.97825 | 2026-08-14 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e065a670-4aea-38d5-a291-de397c2bee41 | -2.90841 | -40.39144 | 2026-08-14 04:29:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c99a04bb-1430-375f-abc9-01de4d72c4ab | -2.69223 | -48.21944 | 2026-08-14 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23e606ac-fd8b-37ca-bb41-ab5ae5e47c9b | -1.78091 | -55.53471 | 2026-08-14 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd74629a-c79b-3862-9b0d-1685a4633029 | -1.78156 | -55.53067 | 2026-08-14 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99810d8a-f438-367b-9356-1284fd4bc8a5 | -2.57777 | -49.11567 | 2026-08-14 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5eb8820a-ae61-3e96-9718-711ae5c121e5 | -2.82565 | -48.6488 | 2026-08-14 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c433924-6403-3113-ba7c-061131cebb92 | -1.82897 | -54.50109 | 2026-08-14 04:29:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 16809661-3627-3572-9d61-8ea4e42223ab | -2.68872 | -48.21888 | 2026-08-14 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28fed83b-88f0-3ab1-93fd-74346f191691 | -2.68935 | -48.21497 | 2026-08-14 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e32f55fe-4d88-306b-8da4-e047c9be3ae1 | -1.8295 | -54.49776 | 2026-08-14 04:29:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 083a06f7-b1c5-336c-bf52-37c8c95691cf | -1.8279 | -54.50772 | 2026-08-14 04:29:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9e9e3bbd-be52-3a8d-9e2f-f13f4614acdf | -2.69286 | -48.21553 | 2026-08-14 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dea1b14-a6dc-3802-9bf2-e74de0d57926 | -1.82843 | -54.50441 | 2026-08-14 04:29:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6c49106b-11a1-39a2-ac3c-08dd9740de93 | -2.64652 | -47.98265 | 2026-08-14 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7da50a96-5ab8-3c69-970f-ea77f885a748 | -2.82124 | -46.71427 | 2026-08-14 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6dad3f6-03e0-3534-bee2-662637042780 | -1.82308 | -47.89692 | 2026-08-14 04:29:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 928a51d6-9662-38c2-bda5-f8c813566c73 | -2.41896 | -48.63515 | 2026-08-14 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08627b02-7b2d-3e21-8b89-73e0566c8c45 | -2.69637 | -48.21608 | 2026-08-14 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ffc9acd-1f6f-3f0b-b448-5c7d774a9920 | -2.57101 | -47.24535 | 2026-08-14 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f99cc880-fd1c-3c76-a06a-af07dfdcbd54 | -2.90431 | -40.39081 | 2026-08-14 04:29:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e9fa181b-f6ef-3bb9-b230-ac081b1d6612 | -2.64714 | -47.9788 | 2026-08-14 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f77162cb-449d-3519-8aec-c00191ed5f98 | -6.6195 | -59.0416 | 2026-08-14 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| adeed69c-dc4e-350d-a556-0d2e9282328a | -11.4885 | -54.6273 | 2026-08-14 04:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 0a00db72-3e46-3f11-8256-62bd3127747f | -6.1855 | -47.3284 | 2026-08-14 04:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 274.6 |
| d4d7f5b6-de68-30f9-847b-eaf590422651 | -13.6859 | -46.2624 | 2026-08-14 04:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 03d3482c-1de1-36d6-9443-8296945c2500 | -6.1853 | -47.3504 | 2026-08-14 04:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| ab1a41bc-169c-3169-ba93-319409e3c216 | -6.2041 | -47.3271 | 2026-08-14 04:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |


[Clique aqui para ver as próximas entradas](README18.md)
