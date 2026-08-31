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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7480d5d9-992d-321f-b1a8-6f462e6351e1 | -14.2218 | -52.847 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 209589ca-db75-3ec6-80f6-de65db4670e0 | -12.9447 | -45.923302 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26e0eb57-6276-3c18-8c8a-f23ac085dbdb | -10.7404 | -47.9506 | 2026-08-31 00:11:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd152d91-c85f-36cd-b770-adadcce41676 | -9.4669 | -50.303902 | 2026-08-31 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 400b26c6-177e-33d8-8d4f-756bc1e5e606 | -11.1945 | -45.069099 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f965a8ab-0539-3e3c-96ac-172e1d4a5679 | -5.4773 | -57.125198 | 2026-08-31 00:11:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea5c8f9b-917b-3107-b3e2-d98ece3199cb | -4.393 | -47.827202 | 2026-08-31 00:11:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f40dc2be-5ef6-3b30-9817-fc1f7418e79b | -14.4007 | -52.523499 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15390af9-f25f-376d-9a6b-f5087dfc7210 | -1.6008 | -54.417 | 2026-08-31 00:11:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75700451-95c3-3b0e-b413-be79fb2d36af | -9.6646 | -50.873299 | 2026-08-31 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd77ed59-fb82-35d6-bbb1-249b6f7edd7c | -14.2316 | -52.844898 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59e8fcdd-e948-34d1-b740-cb4126b83850 | -12.9215 | -45.911999 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b965b6ea-4663-36b0-9092-592836f29ec9 | -12.9196 | -45.9039 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a56d0842-ae4f-33b4-bd00-b3812160e643 | -5.2414 | -55.893501 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3397c0fc-dae6-3ae0-87e1-2a14a1ec0392 | -9.668 | -50.842201 | 2026-08-31 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 040a757a-0f18-3165-be98-d58cb25b2786 | -15.0731 | -48.0214 | 2026-08-31 00:11:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b9cde249-acb2-3957-af1e-722fc2de83f1 | -1.3961 | -55.746101 | 2026-08-31 00:11:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ea28b8e-da29-395e-8cd7-4247264e0d79 | -9.2012 | -51.5714 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f587bf3-c409-38ab-8628-655880789b1e | -9.4171 | -45.669998 | 2026-08-31 00:11:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b4e8bf3d-cc19-39a6-81db-f8ea118c0ade | -9.4108 | -51.684502 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd41b0c5-8376-37c5-9acd-a408cc4a5e58 | -7.9734 | -44.2841 | 2026-08-31 00:11:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 93b51711-fb46-3483-8264-502cc594dda8 | -8.0912 | -45.472401 | 2026-08-31 00:11:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 693d9f6e-83a8-3034-8125-d6c1f33d03a5 | -7.0601 | -52.720501 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 426c4799-ff09-3db0-8ac9-3e366eedce0a | -6.3882 | -45.507 | 2026-08-31 00:11:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1867663-c42b-393c-b632-e9f4ca8bdc01 | -10.742 | -47.957802 | 2026-08-31 00:11:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18f05a5e-5157-3a82-a6ca-2cd700c7d315 | -18.268801 | -52.670898 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 39a5f2da-003c-3c9f-8332-ac2f0b07233c | -9.6696 | -50.8494 | 2026-08-31 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76a6d491-747e-38e8-b30c-5daa1dadd759 | -3.69 | -51.9916 | 2026-08-31 00:11:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a703afa9-276d-3b60-a121-dffa3eda8723 | -15.4157 | -52.700699 | 2026-08-31 00:11:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57879d8f-7dfb-3c6c-add0-f31c4eb7bc60 | -11.2008 | -43.3815 | 2026-08-31 00:11:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 19321412-1245-3bb9-8a5d-18da803e7e99 | -6.5399 | -51.436501 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4c95ef6-8fe3-3ea1-bc8d-d1f859c8cdb8 | -22.4911 | -48.5798 | 2026-08-31 00:11:00 | METOP-B | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2553a037-bf76-3033-9589-9006b3a5d7e2 | -12.9098 | -45.9063 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea707fc4-818f-3b12-bc09-1f433c8bb32f | -15.0684 | -48.000198 | 2026-08-31 00:11:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 03c4fa58-e0ac-3337-b8bd-13d85ca8d707 | -8.3894 | -44.989799 | 2026-08-31 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1149b1a0-21c8-3f77-b454-d716ef7e0d16 | -18.2981 | -52.664902 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 731792f1-71dd-3684-9140-18a4d6652673 | -7.5656 | -48.3578 | 2026-08-31 00:11:00 | METOP-B | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3a77300d-09f3-33fe-b0ae-e05e67a7f15f | -6.2537 | -53.677502 | 2026-08-31 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10bb78e0-7574-331a-a3fd-f6d0695d8cbb | -12.1473 | -47.248699 | 2026-08-31 00:11:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04687d3e-d2a4-385e-9bd7-8ef3a5fb0907 | -18.292601 | -52.689201 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a09eadf1-cb0c-322b-bd7b-479d90d2c6a6 | -12.9181 | -45.853401 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 42be5bb3-998c-3888-b622-9f23f9e4830f | -14.4419 | -52.524799 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1fbaaa69-d465-3e68-babd-c6fe1cef1eac | -5.2609 | -55.889301 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff6ea42-cd37-30f5-bf36-f574f0826831 | -16.285 | -42.5686 | 2026-08-31 00:11:00 | METOP-B | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 31384933-7990-3a3c-b20e-0c345e580f03 | -9.6728 | -50.863899 | 2026-08-31 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35c8b6bc-3fdc-3feb-b855-9ef773bafccd | -5.4509 | -47.5438 | 2026-08-31 00:11:00 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0104ab70-8a86-3638-9eae-0e745eddbe7f | -12.0902 | -47.269798 | 2026-08-31 00:11:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7803b29a-ebd8-3cc3-99a9-69147288b087 | -10.8528 | -50.480499 | 2026-08-31 00:11:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb574283-05e7-3da3-8dcd-03ef291c4ef5 | -8.375 | -45.756901 | 2026-08-31 00:11:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8aef37fe-0a6d-3269-8099-e6d5f8c0276a | -5.4491 | -47.5359 | 2026-08-31 00:11:00 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1cbce61-b7f1-3a45-b9f2-47034c16487f | -14.4321 | -52.526798 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf1b1ab7-6250-3182-a0b2-91468e527cf1 | -3.4123 | -50.122101 | 2026-08-31 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aafa73c-e21c-349e-a96d-ac3f2550075d | -7.5704 | -61.326698 | 2026-08-31 00:11:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14b01e66-b7f2-33e3-94f8-6a3a82d2de2a | -14.1979 | -46.565498 | 2026-08-31 00:11:00 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25082325-75bf-363a-9cd1-94d19bd66fb3 | -14.1412 | -52.801899 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fb10f5ac-d063-3a0b-ac8c-8edf88f25946 | -15.7708 | -49.958698 | 2026-08-31 00:11:00 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a551fc9c-0f67-3aa2-9f2a-83f67a88000c | -19.1518 | -57.401001 | 2026-08-31 00:11:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7a6047bb-d89d-399f-a9c2-470f7c736f4c | -10.8142 | -50.679401 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 721e9ce6-b7d5-39a6-a999-c71a619164fd | -11.3482 | -45.194599 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c70e54c2-0195-3f06-899b-1c98dee62e4d | -6.1251 | -57.676399 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c6e38d1-d6ff-3008-81e6-129da5259ade | -8.3796 | -44.9921 | 2026-08-31 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ba2b75e-5079-30ee-a127-3fdc75a1882f | -10.0751 | -48.697498 | 2026-08-31 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e048681-1afe-37e2-b3dd-24dcdc559631 | -15.6579 | -45.914902 | 2026-08-31 00:11:00 | METOP-B | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e047bc7e-f6bc-3936-bac7-869c201d8a29 | -6.6069 | -58.610199 | 2026-08-31 00:11:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de5d9f94-6135-3f13-a8c3-2fb7fca42f78 | -10.8309 | -45.320301 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7956205-8bf9-330e-a3c7-393e102fbdb5 | -6.5253 | -51.417198 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f00a560-fe27-30f3-857b-d0c6d0e61d94 | -10.7475 | -44.882702 | 2026-08-31 00:11:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7c10cdd1-1021-3ba6-9535-5153ea8e95de | -16.2752 | -42.571201 | 2026-08-31 00:11:00 | METOP-B | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 967b6436-47b0-37a6-ae87-1bb9eef03aae | -5.6011 | -44.009602 | 2026-08-31 00:11:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb2cd8b3-e1cb-3789-b3d0-b5dec06e0d07 | -14.6068 | -54.109699 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1da343e8-4501-36eb-b440-25c45a9d8365 | -13.4086 | -51.827702 | 2026-08-31 00:11:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 86523e08-9ac6-3634-aa01-612ae72f636d | -5.7312 | -49.126202 | 2026-08-31 00:11:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98cd6c32-fb01-36f4-b6cf-5d5149f09105 | -10.736 | -50.650799 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 37af393e-0ff0-37ef-96b1-7a768051bd8d | -4.3948 | -47.834999 | 2026-08-31 00:11:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c07715c2-14ad-31d9-b929-f4e7d999c7f7 | -3.5426 | -49.470798 | 2026-08-31 00:11:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac5463f-79b7-3697-b57a-086bf048294b | -9.4125 | -51.6922 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1cdd675-f3a3-384b-a82d-7ff7929aba06 | -13.4707 | -57.030399 | 2026-08-31 00:11:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 19b3bf73-6e3a-348f-959d-3b81e4aee3d0 | -5.8491 | -57.527901 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f27be0fc-822a-377d-b121-5cb8157489e3 | -7.9287 | -45.0042 | 2026-08-31 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 13dac4a6-ded9-3043-9931-c0deaac27c64 | -10.7343 | -54.048698 | 2026-08-31 00:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f78d09c-a275-3e80-9bba-9e50f221fc18 | -6.6252 | -53.171902 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb804a8e-3609-38e6-b420-70640b663333 | -14.5826 | -54.089699 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9564ec71-8122-3c66-a932-270f80a58a62 | 0.0159 | -60.584801 | 2026-08-31 00:11:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c2aec838-d798-3138-a722-b01e72995dd1 | -17.988701 | -44.305302 | 2026-08-31 00:11:00 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7ef6399f-2306-3e56-90b1-79cb78237381 | -7.3224 | -60.5513 | 2026-08-31 00:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebdcc9ea-9ddf-39a1-8d53-ebe6854ccc29 | -10.8287 | -45.311298 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e98247bd-0898-3d8c-b0d0-a087f5d48eab | -7.5093 | -55.269798 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16ed5cc8-e290-31e7-bdfb-1f6a67f1bd51 | -15.4177 | -52.7108 | 2026-08-31 00:11:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1bc6efa1-70db-3d17-986d-70a8a9fff07c | -11.1565 | -45.0396 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc91e357-607f-373c-aefa-05eb5642929e | -6.364 | -45.491798 | 2026-08-31 00:11:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a4bbe12-0a78-3b5e-8643-7fd1f3d18ba7 | -14.9906 | -48.159801 | 2026-08-31 00:11:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eec9771a-5faa-351c-a088-feaf77cb2871 | -18.307899 | -52.662899 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 178f1d03-348c-360d-b4ed-e04f0131dd28 | -14.2295 | -52.834999 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 27525f4d-94aa-3b02-9cec-61fd1405da19 | -7.344 | -55.1661 | 2026-08-31 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 180d3f78-b57f-3275-85e0-9958d01cc0d9 | -8.9399 | -50.201302 | 2026-08-31 00:11:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02de6971-fd1c-389d-9182-d338b7e3bd18 | -4.8552 | -55.811901 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89978977-5ea4-3391-b0bd-0cab3275f56c | -7.9263 | -44.994099 | 2026-08-31 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d25efeae-dffc-3241-8ed6-4c17e3f7b7a3 | -10.8614 | -48.347401 | 2026-08-31 00:11:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57f810e9-eb7b-3dcd-995f-618708f27392 | -10.147 | -45.745899 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af6663d2-9fd7-3a3c-a55b-3a2174614d5b | -5.4901 | -57.137001 | 2026-08-31 00:11:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
