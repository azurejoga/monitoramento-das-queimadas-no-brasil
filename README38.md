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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32aadd9e-951e-35a6-b079-74b080856e18 | -2.94122 | -50.48474 | 2026-09-10 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c048339c-d837-36f1-ab0c-2fac9603eb73 | -3.58992 | -59.0791 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 666a95aa-7897-3966-80ec-3eaf60b73ce5 | -2.73378 | -57.62789 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5e8fd99c-a0bf-34bd-af9e-70b7c4f89969 | -3.89841 | -59.60236 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ba3f8b0-f02e-35c9-abff-9a57f9fe642b | -3.765 | -59.39032 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67fa168e-35a7-33ff-8b27-52547e1e9453 | -1.70391 | -55.02709 | 2026-09-10 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dfc5709-82eb-3c15-9f9e-c9dc52f84010 | -3.37037 | -59.42787 | 2026-09-10 05:46:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae1460c7-b668-3c47-aa9f-019ce2a94504 | 1.00776 | -51.10347 | 2026-09-10 05:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c55ee11-b31b-3580-8141-8175b74acf31 | 0.24877 | -51.45311 | 2026-09-10 05:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b020aa95-19eb-3db1-91a1-a6fb9a88b15c | -3.41183 | -59.23286 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8900e5b1-f79a-36f0-a264-25fc42f2311c | -3.40413 | -59.76312 | 2026-09-10 05:46:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80162352-9627-3db8-91c9-cc1509cff231 | -3.41559 | -59.23344 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee000489-3f12-3087-bb83-520d60b371b3 | -2.73436 | -57.62421 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cff341f8-7b07-36c7-8468-d0ba29bf745d | -2.58811 | -59.44982 | 2026-09-10 05:46:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 248f888a-218c-3371-ac43-438ba2a270ef | -2.73023 | -57.62358 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 053c0917-1e94-350c-9cd8-5e78a795657a | -3.44852 | -61.08759 | 2026-09-10 05:46:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7714e574-0972-3f8b-9f29-b0e10efb1aaf | -1.72953 | -57.15797 | 2026-09-10 05:46:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4391c608-3a7d-3b75-9a0f-65e1f8b8c332 | -2.72725 | -57.61558 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e60a03d-285f-395b-81d2-7a9578f4712b | -3.65519 | -58.89879 | 2026-09-10 05:46:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f012b7d7-ac02-39c9-848f-116477c4d3e9 | -3.7657 | -59.38585 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d95f3a4b-41d7-3cd4-bd13-01e090c8b482 | -2.74898 | -60.23324 | 2026-09-10 05:46:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48180175-0864-3e48-87fd-a1a77e7dd03a | -2.93539 | -50.47825 | 2026-09-10 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7036acba-0e1b-3c0a-8501-71f233620fd7 | -2.92043 | -54.1114 | 2026-09-10 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13947802-af1b-3b48-bff5-e26070c121f7 | -1.31368 | -54.21986 | 2026-09-10 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1581b507-e844-381c-a21d-3f1a7294769f | -2.73791 | -57.62852 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| abd58467-9302-3f92-b5ea-7df6419f76f8 | -1.18981 | -55.72036 | 2026-09-10 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cef47933-ecdd-30a8-b9c5-cf532737100c | -2.9429 | -50.47357 | 2026-09-10 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 893b11ff-a1d2-30df-93fc-98ff72a5a663 | -3.14925 | -60.65147 | 2026-09-10 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17459b2a-b01a-3cf1-8d96-694ed4457bcf | -2.72667 | -57.61926 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 175d300a-3b6b-3b0d-be2f-233b4dfa743c | -3.41629 | -59.22889 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ee58b36-eaa9-3b54-a2a2-b17aafd21e2e | -1.31322 | -54.22279 | 2026-09-10 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55cfefa2-5a64-3f5f-8f3a-a5bdbc7934fe | -2.91516 | -54.11058 | 2026-09-10 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1db56837-e41c-370f-9a64-b05b800b2f33 | -3.15274 | -60.65202 | 2026-09-10 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48c1a530-d61e-3a47-9888-32a53c7c6cb9 | -3.03841 | -59.22609 | 2026-09-10 05:46:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14dc6f94-46cb-3b12-bada-aa251215cbd6 | 0.25477 | -51.45216 | 2026-09-10 05:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0baffe54-1d72-3de2-b7e3-143798d9e724 | -2.94375 | -50.4679 | 2026-09-10 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bafe00e5-1bcf-3155-900c-de38e449df21 | 3.51997 | -60.63355 | 2026-09-10 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af416054-6ded-3537-b0c1-7832efc43f9e | 2.42793 | -61.3867 | 2026-09-10 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ea1b89b-5841-3d44-a2bc-12926c626020 | -2.73196 | -57.61251 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 907d590c-556f-3e89-a257-e5bcc8a3500d | 0.24563 | -51.46086 | 2026-09-10 05:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c8f1846-64cf-3534-b8ff-5777ba57ca49 | -2.93794 | -50.46122 | 2026-09-10 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4095a4fa-b45f-33d1-b3de-3619f6b031a7 | -1.70126 | -53.69388 | 2026-09-10 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9099671-a3a8-3cd7-9ab4-66db7f781f4f | -2.91994 | -54.11463 | 2026-09-10 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b588de9-8075-3e54-ae94-df85e8a9d3f6 | -3.43539 | -59.25499 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79985fda-b4f4-37bd-8cc0-a46a6bdc080d | -3.13743 | -60.62994 | 2026-09-10 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62710229-2641-3a5c-8eea-1e23c99c6a57 | -3.15564 | -60.65644 | 2026-09-10 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39c11ac6-ec22-332b-9cd3-3c85af938a15 | -4.00367 | -51.02852 | 2026-09-10 05:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec5f7d90-060f-358f-9fe2-5a422fb11d07 | -3.59374 | -59.07967 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd9bddea-2df3-3aba-ad68-e24af2dfabcf | 0.24417 | -51.46284 | 2026-09-10 05:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3264c15-7759-310d-8618-7a07a139dcf2 | -2.94785 | -50.4859 | 2026-09-10 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d5c69fc-8cd8-3f2a-995d-5676d6c418aa | -4.85376 | -56.01767 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e8c8d1cd-516c-309b-84dc-149ea3c2d721 | -8.89191 | -61.43259 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 861b57f9-4674-3780-b459-a8c5291572c2 | -6.40495 | -54.96437 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08d59a33-a9df-3934-bfaa-0f5e0eb98ceb | -9.0355 | -65.73883 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28fdadeb-a38b-3081-9fe0-0c22bb52c5ec | -9.23406 | -65.59351 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4536d4b-1189-332d-84eb-3b8b4ffb8c7e | -9.21728 | -63.63811 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc7eede6-2ee1-3a32-a0d6-3d56cbe22c96 | -8.83513 | -62.35967 | 2026-09-10 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a3757f3-ac0b-345a-8900-325d904dca4a | -6.65316 | -58.82241 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad9249d3-be98-37bc-afe9-fa5eb49bdbd9 | -9.14983 | -60.36074 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48b85ece-185a-3007-990d-50ca8a164dc0 | -8.89488 | -61.43723 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9195f0c5-8790-373a-b180-6e3652f9bc6a | -8.89313 | -61.4244 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f02bf5d-e635-30bb-b31c-a0d8f873e109 | -8.90143 | -61.44239 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c232319-f4dc-3378-ab7c-8afaff6688ce | -9.20891 | -64.50645 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92b2ea94-6a8f-3320-b62c-69280070573e | -8.73426 | -62.38335 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 799f53dc-afa8-380b-9880-f3fe7e2ee469 | -8.62897 | -66.51415 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4767cc5d-bcd3-35ba-8dec-6471900e06f4 | -8.8913 | -61.43668 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b59ff1e4-b81b-3d01-a5ce-d08907a8931d | -6.24989 | -51.67171 | 2026-09-10 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b239667-bddb-3624-b7e6-c94acec5afc8 | -9.22231 | -63.64978 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f5e2262-b8b1-39cd-b16b-bbae8c9ae855 | -9.03947 | -65.4146 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08ce3d2d-9f77-3c93-a9c7-a9dd9799f285 | -4.86396 | -56.01445 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 035c794d-fe5a-3c8e-a94e-4bb10112c495 | -6.956 | -59.76065 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b872166-2343-30fe-932a-d26b5e3365dc | -8.99059 | -65.41063 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f349547a-d5db-3643-954d-8465c05a0991 | -8.09043 | -54.84763 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69ab97c9-f4d1-3f5e-8c93-a29a77c02027 | -6.09341 | -59.97174 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a4934a7-4153-34ff-ab82-c8c74549e2fc | -9.05127 | -65.40554 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 416339c8-36bd-36ee-9ac6-472c1293f92d | -7.16966 | -59.54974 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68afa828-a091-3f4d-968e-d42600649d8c | -9.22007 | -63.64218 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c09d202-4910-325f-a8f0-161bce7cd021 | -6.77967 | -58.89174 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65e9aa17-349d-3b62-8ef2-358ec654af61 | -8.88772 | -61.43613 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6313bcaf-84d9-3dd3-af8d-dca59c73e9ee | -6.76826 | -58.60795 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d29b39b4-3c60-377b-add4-205ba255b076 | -6.5558 | -62.88546 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9aa62f0d-9c50-3e22-b827-0d50cf073092 | -6.79966 | -58.95175 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1e605acb-0cb4-3f92-93c0-1e2350d0eafd | -9.2014 | -65.77336 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d4d258f-d261-3150-9e5e-701d3fca18bd | -7.24186 | -59.52305 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f951e6d-3bcc-3f12-9507-767abcccc16e | -9.13954 | -64.41309 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8603557a-62eb-38cd-b2bd-4028a51ce488 | -6.50432 | -58.38161 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0dce19ea-c600-3d7c-924e-b265beb331b5 | -6.6358 | -59.43939 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 109b1e34-432c-39a5-9078-b2f2287d55dc | -6.78217 | -58.90284 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ede855a1-169d-30fb-b9ff-b00c5f0ef4ff | -7.56208 | -61.37633 | 2026-09-10 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a6ad650-ec77-3bc1-a9e7-114502ed48d3 | -6.09715 | -59.97231 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae8b063b-63f9-32de-a926-2ca7a3da6f33 | -9.03888 | -65.73937 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16e5c6c2-7bad-3f61-9879-229ef1d67c6b | -8.62265 | -66.50917 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ae46bf1-6a9c-3a4a-a1f8-085e0319c621 | -6.65719 | -58.82304 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3df5d0c4-8768-3f5f-a4c6-f70b8244620e | -8.99903 | -65.40102 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27c21ca8-933a-3ef4-b3e7-a15b78f41fbc | -6.27042 | -62.74368 | 2026-09-10 05:48:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 470be29d-6def-37ea-a5bf-9d79aa623e78 | -9.15067 | -58.30293 | 2026-09-10 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 032bddf6-892c-388c-968d-11cdcd548707 | -6.95983 | -59.76123 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a495040-52be-3911-8a0e-b2459e7dabd0 | -6.55189 | -62.88846 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0c83fdce-533d-3462-8c8a-9b68a30e87d1 | -6.54577 | -62.90558 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56ba3a5c-d84a-36bb-adec-824d1ca3a722 | -8.67763 | -62.45866 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README39.md)
