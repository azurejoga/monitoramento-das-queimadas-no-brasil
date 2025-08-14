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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a216de7-4ffb-3a4f-9b59-cf20344d0aed | -11.69123 | -51.62319 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74e1678c-fcb1-373f-a0e6-7f0e603f620e | -7.88073 | -61.82049 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 29adaf8d-1bdc-3776-b5f4-8144ff9f2103 | -7.88304 | -61.80812 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05c992ab-9031-38c7-8ecc-99bca5ab6e6a | -9.13107 | -59.65891 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd177cda-2c9f-3432-b7e2-ce72c3470087 | -12.58745 | -46.97296 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3083fa2f-6bf8-3a6c-8c59-d7eb892ed445 | -9.16968 | -59.67196 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 809c5b37-9218-3bf6-ab4c-d936beb40e91 | -9.20447 | -59.64921 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54b0c8e5-bb01-3cb5-a679-4994a0dd6f27 | -6.877 | -59.1663 | 2025-08-14 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| cf9f92fb-1b5d-3e13-b69a-857585a8ff27 | -6.0807 | -59.9465 | 2025-08-14 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 7e266ede-7a4e-39ac-886e-724a153c6839 | -6.8771 | -59.147 | 2025-08-14 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| f1bb810a-350b-378f-949f-0ab3d20f9172 | -6.8955 | -59.1655 | 2025-08-14 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a9b46c74-29bf-36e3-890f-fc9275a2fe6d | -6.914 | -59.1455 | 2025-08-14 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| c6408813-9caa-3f84-87d4-656c951d7174 | -6.8956 | -59.1462 | 2025-08-14 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.6 |
| e0d773ed-633f-3277-a339-c67f83e07ad6 | -16.31429 | -52.92208 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77310a7b-4fa3-3a06-b1ff-01284e07e0b2 | -15.55452 | -43.15471 | 2025-08-14 04:51:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 511c639a-65aa-3da0-a2bf-50f641bfedcf | -21.71029 | -44.37009 | 2025-08-14 04:51:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 38347088-7a69-3cec-8e1f-447f6046690c | -16.31096 | -52.92152 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5bb475c-5dc3-32e9-bd85-0b886c197bd5 | -18.24723 | -47.26273 | 2025-08-14 04:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 973fb25d-2648-38f3-ae7b-c4c5051b9e60 | -16.30487 | -52.91681 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7495b185-0676-3fa5-b0b1-e925fd53467e | -19.6087 | -45.98665 | 2025-08-14 04:51:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40ac609e-73a9-3f0c-b094-3750e3349897 | -15.54898 | -43.15399 | 2025-08-14 04:51:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b2ebccba-e941-3d74-95dc-70dafca258ca | -16.32038 | -52.92678 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36839d05-2202-34b5-a510-dc494babb052 | -16.31152 | -52.91793 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73319c39-c6ec-3b19-aa37-0ecaf602f422 | -20.46624 | -47.41148 | 2025-08-14 04:51:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e3b1015-c113-3358-817b-fb1925a7ae3c | -21.36065 | -45.04443 | 2025-08-14 04:51:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29a24968-11cd-322e-aef5-48e86997e7b7 | -21.00862 | -51.65788 | 2025-08-14 04:51:00 | NPP-375D | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3fb14016-52be-308c-bc92-94d7e3a7c5df | -13.054 | -57.10028 | 2025-08-14 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87e8c39b-96f4-321c-828b-4c8bf4e1472e | -13.70818 | -53.03713 | 2025-08-14 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97edae11-43df-34a9-8cfd-a563a626c71f | -19.08117 | -48.15658 | 2025-08-14 04:51:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04408196-0ad3-364c-bb2b-cb03726a5840 | -14.4745 | -46.06684 | 2025-08-14 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abb31519-b2c0-3316-a3c9-bf052220ef38 | -16.31373 | -52.92567 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e2d619d-71bc-33de-9eed-b01d57a0776e | -18.53226 | -46.05046 | 2025-08-14 04:51:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ce4ae03-f506-3188-92ed-75805cd0a8ba | -17.049 | -51.79605 | 2025-08-14 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68069ad7-84ca-3a1e-ab8d-cbddb1411c3c | -21.31937 | -48.56752 | 2025-08-14 04:51:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8092d1d-01b8-3871-9d8d-f45992099b05 | -16.80869 | -49.25396 | 2025-08-14 04:51:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf09221c-1331-37f1-bc77-d3278e07458b | -21.01724 | -48.90687 | 2025-08-14 04:51:00 | NPP-375D | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c8bcd03e-12cf-3b87-b09b-8234fea59c09 | -21.3157 | -48.56277 | 2025-08-14 04:51:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34aecf0a-a712-3894-a204-a8388225189d | -16.31317 | -52.92926 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 580f912b-b1cd-354b-8517-251d13a48051 | -20.45225 | -54.53886 | 2025-08-14 04:51:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e2693a7-6bad-3be5-bbc1-ccd11a327266 | -14.45675 | -48.81938 | 2025-08-14 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43ae018d-2005-3d77-9d6d-247cac8d6405 | -15.70054 | -56.41291 | 2025-08-14 04:51:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e195f369-ee2f-3973-ae7a-2c2e391587b4 | -16.28824 | -52.91402 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ed04e81-e886-3401-8161-451b44fed274 | -17.05297 | -51.79282 | 2025-08-14 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ed1d0142-59f6-35f4-83d8-843e05c77f5f | -16.3215 | -52.91962 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2b70ecde-d75c-32cf-a867-839f7a1de8d7 | -16.31705 | -52.92623 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58571a14-af0b-350f-a4c3-cdaa876e1856 | -18.53639 | -46.05641 | 2025-08-14 04:51:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2508b75a-a205-3ae9-bedf-22088f5b3cdc | -15.68098 | -56.3959 | 2025-08-14 04:51:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e9e8e4c-66d2-302a-80bb-1bcb96b8382e | -14.368 | -53.37465 | 2025-08-14 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 350bb7ba-1c21-3a7a-93de-f82f0e76c7cb | -20.09003 | -47.44199 | 2025-08-14 04:51:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2addbad0-c8e6-3e3c-90a3-b80553ae0f09 | -16.3082 | -52.91737 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d06e48ea-7979-3d35-8f6e-256d833c186b | -16.54063 | -47.86005 | 2025-08-14 04:51:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18530117-7191-3cd0-b00f-5924710c9bcf | -16.30876 | -52.91378 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fffc911-9c42-3233-9c44-f3fcdef84f23 | -16.31485 | -52.91849 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b83ab46b-e19d-3b93-8de2-07645b51e8ca | -16.29157 | -52.91458 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 732e0e90-7c64-3ee4-ba52-6146614872f8 | -17.04617 | -51.79174 | 2025-08-14 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| df161795-4238-3180-a6d0-8e32fd43c7c3 | -16.30764 | -52.92096 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc13fe11-4efb-3f19-a48a-5643bc13b6d5 | -17.05013 | -51.78849 | 2025-08-14 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c1b9323d-e3d2-3290-85f8-92201ce7e1a1 | -14.10669 | -48.20156 | 2025-08-14 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a7e6722-4059-3965-ba4a-c9a0e952dc4d | -21.01172 | -48.91798 | 2025-08-14 04:51:00 | NPP-375D | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d7ed2533-e2ab-330e-9210-db024acbc0be | -14.79372 | -42.72406 | 2025-08-14 04:51:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fa1625c-9f6a-3b00-96a3-8d556edd20ce | -14.36524 | -53.37051 | 2025-08-14 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 072b62ae-b506-3b51-b6ba-8335aaa0f419 | -16.3104 | -52.92511 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25620840-0127-33ec-9f3c-ea3be88685fb | -16.54114 | -47.8561 | 2025-08-14 04:51:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a55b8e4d-4cbd-3206-be0e-ea6580e2808d | -14.0185 | -52.05087 | 2025-08-14 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9857ecb-ee6e-369d-b851-8e3bb854c432 | -16.32094 | -52.9232 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 36875b56-5c1a-3fc5-85e3-13629e88214a | -16.29878 | -52.91211 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaa28bc2-d386-347f-8a17-012947ce8536 | -21.0158 | -48.91857 | 2025-08-14 04:51:00 | NPP-375D | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 805293fc-6930-3c99-b300-71672e2cab97 | -16.501 | -54.33598 | 2025-08-14 04:51:00 | NPP-375D | SÃO JOSÉ DO POVO | MATO GROSSO | Brasil | 5107297 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a8b00e3-312e-3313-a8de-eff6f8915c40 | -13.08603 | -56.92008 | 2025-08-14 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd8731c7-feac-314f-95c1-89f05294722c | -16.76939 | -49.31599 | 2025-08-14 04:51:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 199c951c-9ff9-38ed-8131-84cef6e6f2d8 | -14.38076 | -53.38047 | 2025-08-14 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7766f13c-9e3e-3edb-994f-5ab133dbb611 | -16.38767 | -50.90503 | 2025-08-14 04:51:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c56d10b-9cd8-361f-aa1c-c77a261dbc39 | -16.31761 | -52.92264 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9692df25-c1d0-39f8-aa3a-8d40b04e5b67 | -17.86687 | -52.19872 | 2025-08-14 04:51:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6b638df6-1b18-393b-9269-a78e5e2b6ec7 | -13.07605 | -57.13585 | 2025-08-14 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c5af67b5-0c2f-3d78-a6cd-bd9e535b1d38 | -18.92635 | -46.78886 | 2025-08-14 04:51:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da2879d2-af20-31fc-8666-608ec8d47f20 | -13.07515 | -57.14092 | 2025-08-14 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bfea793e-cfb4-3122-a408-9e99d228677b | -15.57751 | -47.32014 | 2025-08-14 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7220592-5330-3849-bfd9-6d8f92d0b089 | -15.30116 | -59.23642 | 2025-08-14 04:51:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba44d865-71d6-39fb-a6df-7cf06dd2e98d | -15.55496 | -43.15083 | 2025-08-14 04:51:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 620d7972-c29a-3646-bd98-4e07b52b554a | -17.63806 | -44.50275 | 2025-08-14 04:51:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02de1440-173f-396d-b0e2-69ff875b494a | -15.57279 | -47.32358 | 2025-08-14 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcdddc2b-547e-3622-a4fa-aee47ea5fdd9 | -14.45677 | -48.81651 | 2025-08-14 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59d4424a-a7f5-32dc-8df7-d5cdec36c1fc | -15.57699 | -47.32413 | 2025-08-14 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46bfdc42-4a5b-3131-9ea1-c5b260f701cb | -18.54114 | -46.05701 | 2025-08-14 04:51:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dc18b636-1a59-3ac4-a9bb-f47e2965dd5c | -16.31541 | -52.91491 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 853b9da2-3af0-31eb-b7a5-904e6e0f90c5 | -14.67067 | -46.61695 | 2025-08-14 04:51:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb39a3b1-db96-3ef5-a9f0-df7cb63c7d82 | -21.71004 | -44.37024 | 2025-08-14 04:51:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bc898361-b1ee-367c-81eb-ef96a9fc7d8e | -17.87081 | -52.19553 | 2025-08-14 04:51:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c206128-57fd-3639-b2f7-a2ebdd7b9389 | -21.3152 | -48.56685 | 2025-08-14 04:51:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1c1ecdb-542e-3c3a-a169-4c57137df444 | -14.3204 | -48.63876 | 2025-08-14 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54923689-208a-37b1-be3b-8f41536fd70b | -19.03376 | -46.59153 | 2025-08-14 04:51:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b823aa7-8dcf-3cc4-b462-7d90285a80ce | -14.49504 | -53.27792 | 2025-08-14 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80589137-36b4-3b20-b976-2d987b222cdd | -13.70428 | -53.04015 | 2025-08-14 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87e72ad1-bd42-321c-ae4c-aeb5a25ca0f5 | -21.01532 | -48.92242 | 2025-08-14 04:51:00 | NPP-375D | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9c2eb3ed-7404-3b2f-aa38-ff9ce40eac5a | -16.29489 | -52.91514 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0799a312-ca8d-3ae7-aff7-b1d858aeb192 | -15.58172 | -47.32066 | 2025-08-14 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a125a8f-2a18-3583-aea5-eebff2f818b9 | -19.08167 | -48.1526 | 2025-08-14 04:51:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef044a74-164f-30a3-ab8e-49745a86b5a7 | -17.61336 | -46.70457 | 2025-08-14 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c340410e-cc48-3039-a39f-d354816f6728 | -13.07998 | -57.13657 | 2025-08-14 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README25.md)
