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
| c54b06a3-d5c6-348e-98e8-2fbe7c8fb410 | -22.57655 | -44.89423 | 2025-03-07 04:50:00 | NPP-375D | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bb188dba-0aa7-3e48-82e7-88ff40b1daae | -19.70235 | -44.77391 | 2025-03-07 04:50:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d10487cc-dc6d-34f3-9c22-30f57c6d63ac | -22.76236 | -52.99324 | 2025-03-07 04:50:00 | NPP-375D | NOVA LONDRINA | PARANÁ | Brasil | 4117107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 73cee96b-09e2-35c3-9299-e20e521d9bfe | -25.32286 | -52.02024 | 2025-03-07 04:50:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 72962bc6-0684-3092-9a8a-5d68f96820f3 | -24.03778 | -50.49857 | 2025-03-07 04:50:00 | NPP-375D | CURIÚVA | PARANÁ | Brasil | 4107009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ed847d9f-257d-37a1-995a-58d28c960352 | -18.87733 | -52.41985 | 2025-03-07 04:50:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 634e4790-6e0d-3364-b8b8-6d6be882157d | -23.20251 | -50.80905 | 2025-03-07 04:50:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b5d75cfa-0471-360b-9540-00fef1b76a1d | -20.8081 | -49.52187 | 2025-03-07 04:50:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d5a9521d-6e0b-34b0-9c47-8a87226b17e8 | -20.72377 | -49.43708 | 2025-03-07 04:50:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3be7806b-1289-33de-a4bf-b03f9593fc96 | -18.97715 | -52.30988 | 2025-03-07 04:50:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ea74d93-9a7c-3be3-ad64-5759a35fcb53 | -20.80616 | -49.52272 | 2025-03-07 04:50:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f4da55ff-d548-34e3-9a5b-58b4c329267c | -21.58433 | -57.58557 | 2025-03-07 04:50:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8206952b-9668-33b8-83fa-94549df71091 | -18.98055 | -52.31044 | 2025-03-07 04:50:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b09bd834-ddc5-37e7-b9e6-5b07d39cfd54 | -25.32288 | -52.02299 | 2025-03-07 04:50:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b8d43d61-db42-3b2e-9e71-e1a5ca404af5 | -22.76579 | -52.99381 | 2025-03-07 04:50:00 | NPP-375D | NOVA LONDRINA | PARANÁ | Brasil | 4117107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5f1c267e-6a4d-333b-8ac1-9b6b97b47d43 | -19.67939 | -45.3811 | 2025-03-07 04:50:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ba3bec2-d495-3edf-afbc-b31c3eb2f86d | -23.73528 | -53.24722 | 2025-03-07 04:50:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 99291ac2-d8df-3063-8d35-8885d1c7fb4a | -30.36576 | -51.96785 | 2025-03-07 04:53:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 6.8 |
| 07dc3a09-ae5a-33d1-87f0-ee2f516ccab5 | -27.66478 | -50.65529 | 2025-03-07 04:53:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f4fd5bb8-14c2-34aa-80e8-fb680f8b9a1e | -26.30812 | -50.8429 | 2025-03-07 04:53:00 | NPP-375D | IRINEÓPOLIS | SANTA CATARINA | Brasil | 4207908 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 426a9e50-9d4d-33a4-a122-14ba89bf1807 | -29.77873 | -51.1734 | 2025-03-07 04:53:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| ba8ce2e7-3fc5-3b54-b44e-65e663e219fa | -30.2933 | -54.99002 | 2025-03-07 04:53:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| ce74ec01-689e-340f-869e-de993a9ed8f1 | -30.08947 | -53.80252 | 2025-03-07 04:53:00 | NPP-375D | SÃO SEPÉ | RIO GRANDE DO SUL | Brasil | 4319604 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 934dcec4-dfb3-3e94-a969-39171da6e606 | -28.53922 | -51.82191 | 2025-03-07 04:53:00 | NPP-375D | SÃO DOMINGOS DO SUL | RIO GRANDE DO SUL | Brasil | 4318051 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 28d06401-30fd-3a55-8690-bf0a6deb5b05 | -28.58359 | -49.44262 | 2025-03-07 04:53:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 526fe101-3b2d-3068-91ec-afaa953a59da | -30.37 | -51.96777 | 2025-03-07 04:53:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 5.3 |
| 37107ece-f1f4-3cee-b1cf-94eb6c431278 | -27.41889 | -50.96271 | 2025-03-07 04:53:00 | NPP-375D | VARGEM | SANTA CATARINA | Brasil | 4219150 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5427e1f5-52d7-3e7a-9956-24572236a545 | -27.72226 | -50.0731 | 2025-03-07 04:53:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ff40ad7d-2da7-331a-be86-cab79ec614af | -26.95097 | -50.77169 | 2025-03-07 04:53:00 | NPP-375D | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 760e43ba-30bb-39d3-93d8-3ab3f980d9e6 | -27.59218 | -49.97585 | 2025-03-07 04:53:00 | NPP-375D | OTACÍLIO COSTA | SANTA CATARINA | Brasil | 4211751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1d4d6385-55a2-3118-be02-bb76b3acaaca | -27.68592 | -48.7506 | 2025-03-07 04:53:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8e6347b3-75fe-38e2-9160-8892d3c04b4f | -30.2989 | -54.99438 | 2025-03-07 04:53:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 34de9e9a-bf6d-3d7a-beb0-6b783e500c5c | -30.29608 | -54.98949 | 2025-03-07 04:53:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 9280ea3a-320b-33b6-8b98-2e2769d90097 | -29.77805 | -51.17934 | 2025-03-07 04:53:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 958a13b1-b48d-398c-817f-981589d0b3fb | -30.2995 | -54.99014 | 2025-03-07 04:53:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 5cad9dfa-631f-3b05-be27-79cc81ee2701 | -30.36964 | -51.96853 | 2025-03-07 04:53:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 6.8 |
| 23022c47-fd98-3fc8-9b99-0b6554efa3b1 | -28.93628 | -51.40273 | 2025-03-07 04:53:00 | NPP-375D | NOVA ROMA DO SUL | RIO GRANDE DO SUL | Brasil | 4313359 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4e2afd56-54f5-399e-ae69-24d835ff7474 | -28.93902 | -51.39952 | 2025-03-07 04:53:00 | NPP-375D | NOVA ROMA DO SUL | RIO GRANDE DO SUL | Brasil | 4313359 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3d44acf-37cc-37ce-bf8c-10c9ba186803 | -30.36929 | -51.97356 | 2025-03-07 04:53:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 7.4 |
| 278582ff-5ce9-3e08-a263-b3890e794107 | -30.36613 | -51.96708 | 2025-03-07 04:53:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 09f21ec6-2e41-30a6-8e4b-766852a07c61 | -27.02094 | -50.84625 | 2025-03-07 04:53:00 | NPP-375D | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e650fa30-8508-329c-a39f-e81a6399aa51 | -29.58263 | -51.98625 | 2025-03-07 04:53:00 | NPP-375D | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 68a4c7e4-d888-390e-ba46-c85b7c7c4d45 | -30.29265 | -54.98884 | 2025-03-07 04:53:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 513777f7-8ffd-3c26-8a99-6689f2fb5bdb | -10.39297 | -47.98438 | 2025-03-07 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f566b2cc-c0eb-38f4-8e17-ac52dc37a3f9 | -12.91023 | -45.07772 | 2025-03-07 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 200fb783-d2fd-3bb1-8e20-ec5d391b4108 | -10.39249 | -47.98816 | 2025-03-07 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 912e2da7-279c-3721-b314-1ebca80bcd45 | -12.90946 | -45.0846 | 2025-03-07 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8006b9db-abe8-34a5-b268-09443f9e7871 | -12.9073 | -45.08574 | 2025-03-07 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 53079f46-72e8-3089-a54a-ec41cf6aef98 | -13.72743 | -47.71323 | 2025-03-07 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f2ab2c1-53be-3f40-937d-6f84d9a93509 | -11.57498 | -47.63467 | 2025-03-07 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1df9fbe-3f47-3764-898a-e5dcdcebaf3d | -10.39201 | -47.99195 | 2025-03-07 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 449f0570-158c-3ecf-a408-d1294bf31bd2 | -12.90802 | -45.07884 | 2025-03-07 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b01492dd-db5e-3348-baf6-b1b307a89cb3 | -10.39822 | -47.98893 | 2025-03-07 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f9bf906-a290-3fe8-916c-698abf58666b | -16.1058 | -60.05301 | 2025-03-07 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6094c1d1-9b0e-375e-bbb9-5b12f7ee7b80 | -17.91436 | -55.54726 | 2025-03-07 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5e5b4741-3f7d-3b36-9a6d-dc138cb5d5d8 | -15.40276 | -60.17807 | 2025-03-07 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b60407a0-14f1-3832-a4d6-1b86a52707d7 | -18.9774 | -52.31032 | 2025-03-07 05:12:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b8058fb-f62a-36cd-a901-a867389aecc6 | -16.10249 | -60.05244 | 2025-03-07 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87e55d12-58d0-306e-89a5-6ee525a6ae0a | -23.73307 | -53.25021 | 2025-03-07 05:14:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8d1d0fce-87b4-3b4f-b9da-2edf0ac083b6 | -23.73366 | -53.24453 | 2025-03-07 05:14:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 55069f2b-d5c8-3705-a60c-af35019431ca | -30.37256 | -51.97231 | 2025-03-07 05:16:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| e448dec1-08d6-33eb-9667-ad1147abe9d1 | -30.36492 | -51.97002 | 2025-03-07 05:16:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 9eab0a9f-27c9-3c34-82cc-b0ed36d5bc11 | -30.37053 | -51.97081 | 2025-03-07 05:16:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 8.0 |
| ca48f1aa-8b3b-30f2-9262-d1a6c0a3bfdf | -30.36696 | -51.97158 | 2025-03-07 05:16:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| cd813386-44bf-37bf-a840-22f4926db60e | -23.72724 | -53.23363 | 2025-03-07 06:26:00 | AQUA_M-M | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 40.5 |
| 807a936b-116d-3bf2-a0d2-97b02c3dd5d1 | -23.72752 | -53.23811 | 2025-03-07 06:26:00 | AQUA_M-M | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 48.7 |
| 81545312-4546-36fc-ad81-cba9e1e0777d | -12.9179 | -45.075 | 2025-03-07 12:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 5f31d275-c6eb-3d99-b5a3-402ba66ff6ce | -10.2212 | -49.83177 | 2025-03-07 12:42:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 092bda85-2ac8-37d2-8f36-635431ff77ef | -10.13806 | -49.8315 | 2025-03-07 12:42:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 880d00dc-9b4c-3a2b-a857-68cbefc59a65 | -13.54446 | -47.93428 | 2025-03-07 12:42:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 188e13b3-8e22-379c-8ae4-79c873d8be7c | -11.96613 | -46.74163 | 2025-03-07 12:42:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 63526c28-b2d9-3e83-ba12-06f7e7a4b6ea | -13.16903 | -45.2217 | 2025-03-07 12:42:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 081553e9-7063-33f0-86d8-29a931a79b9f | -11.5911 | -44.84702 | 2025-03-07 12:42:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 4f8a4454-e08b-3a7d-8c36-f5714224492f | -12.16274 | -44.13628 | 2025-03-07 12:42:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 98fa8343-9cec-3611-8342-b38d039f3c68 | -11.59309 | -44.8314 | 2025-03-07 12:42:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 8de14494-81a3-3e23-bc7e-3f20cf299569 | -13.6168 | -43.65976 | 2025-03-07 12:42:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 89598e6a-3969-3b1f-a517-9e527886dea2 | -13.18041 | -45.22319 | 2025-03-07 12:42:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 23adecc5-2c3f-39af-ac5b-8365e677a43e | -10.21861 | -49.84961 | 2025-03-07 12:42:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6665f8ea-747a-3156-acb0-8877be229df0 | -12.16659 | -44.14244 | 2025-03-07 12:42:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 6ce69bd0-f6af-3a12-a99e-c3844ddb3126 | -12.16872 | -44.12446 | 2025-03-07 12:42:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 3aaca7f2-b184-3750-b9ff-c37fc43b2a21 | -12.47254 | -46.92839 | 2025-03-07 12:42:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 72d61ef8-fd82-37ce-a499-b48236891f6b | -9.82612 | -50.38215 | 2025-03-07 12:42:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3419703c-81b2-3b5b-8f30-4208081833c6 | -10.21991 | -49.84069 | 2025-03-07 12:42:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ba8704b7-71d9-3e19-a4dd-e28635be1dba | -13.15389 | -47.09787 | 2025-03-07 12:42:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5a232f3d-f70b-3cd7-915b-804e7c381677 | -10.31615 | -48.64847 | 2025-03-07 12:42:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 205fbe08-7865-375d-affd-afffc534510a | -9.83503 | -50.38345 | 2025-03-07 12:42:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 71d50da9-3714-3eec-83ff-ff1433be8940 | -13.17848 | -45.23866 | 2025-03-07 12:42:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| fb5437d4-47b8-3997-aeb8-d50d3af0c738 | -16.00047 | -51.18773 | 2025-03-07 12:44:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df768892-8000-391f-a963-7eedef39dc07 | -19.40024 | -44.87794 | 2025-03-07 12:44:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 6fe8687c-d0ec-361b-943a-18fb7caf297b | -22.76367 | -47.38393 | 2025-03-07 12:44:00 | TERRA_M-T | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 5ef4a041-8ac9-38b8-a8f7-8bfa413053f6 | -15.52042 | -48.50174 | 2025-03-07 12:44:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| af3dddc8-92f4-3cb6-a3d3-07da46dbf247 | -20.86195 | -48.6198 | 2025-03-07 12:44:00 | TERRA_M-T | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7a02c57b-f403-394d-83ba-ec8b79246648 | -23.7339 | -53.2518 | 2025-03-07 12:44:00 | TERRA_M-T | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 886621c4-bed6-32c0-bda2-40ca949f592c | -21.68349 | -50.19215 | 2025-03-07 12:44:00 | TERRA_M-T | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 8dbf368c-b969-3107-a7b1-997c77469398 | -16.30233 | -53.82961 | 2025-03-07 12:44:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 924e1fd9-c568-3ce5-a59c-c9e3596350bc | -23.45246 | -47.23845 | 2025-03-07 12:44:00 | TERRA_M-T | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| ecb4d6e0-8d30-3442-93ba-a7757f0bf720 | -18.34011 | -45.63968 | 2025-03-07 12:44:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7394eda5-937b-36af-aca5-bce8ad755241 | -23.73534 | -53.24213 | 2025-03-07 12:44:00 | TERRA_M-T | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 2d7483e4-467b-3418-af04-26b1c8e0f481 | -15.29828 | -47.87587 | 2025-03-07 12:44:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8047f4cb-7511-3aa5-a9d8-e4f0cbd27ff7 | -16.90336 | -48.73019 | 2025-03-07 12:44:00 | TERRA_M-T | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README5.md)
