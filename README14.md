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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57dfa638-58a5-36f1-ab22-1c68412fc02d | -8.22916 | -45.75099 | 2025-10-22 04:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 845e74ce-7913-367f-826e-d0538091b462 | -9.90653 | -65.0248 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22db40a1-2e8b-3a3d-9e0b-fc9aba30e9ee | -7.9298 | -46.01583 | 2025-10-22 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 36cb1e05-092b-3b89-9ff8-4c8e43686c9b | -9.01036 | -65.92226 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca83e4a0-2f39-3ae9-8a43-7c82bebab715 | -11.08252 | -49.62461 | 2025-10-22 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6ef2e58-4963-3eb6-aacc-7f40bd025595 | -8.98738 | -65.89996 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a474d36-4171-3746-9ae5-9051b5f74d82 | -9.00701 | -65.92154 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 48c896cf-cf0b-335c-89e8-b383a523150d | -9.7305 | -67.4763 | 2025-10-22 04:55:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 034f9a2f-3078-3136-a730-1b3f104bd055 | -9.0059 | -65.92731 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fff9ecbf-1990-33f0-896b-8c64ef9d4095 | -8.22444 | -45.75023 | 2025-10-22 04:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6e9f906-048e-3a4a-957f-f104e4286d0c | -9.55405 | -66.65173 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b81cb49e-5eb6-3071-90c4-3e9ffbe0576c | -9.57633 | -65.22134 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3af9597e-038a-3b71-8410-3b77d079a2af | -9.56738 | -65.22127 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4bf7908-5048-3e75-9e8a-4e50a51bc43b | -12.99844 | -48.81108 | 2025-10-22 04:55:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30aa6707-f1fa-3192-9709-b7d5517fffe1 | -9.00693 | -65.93955 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7b366e3a-a0d6-304f-a7a0-99429fc7619d | -9.91176 | -65.03086 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94678918-eeac-3da5-803e-b320a69518d7 | -13.37738 | -48.79816 | 2025-10-22 04:55:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 528ad34c-19ff-3a89-97de-916737526a78 | -7.93894 | -44.84534 | 2025-10-22 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d691d50-428c-3fa9-a201-ab87f83cc468 | -12.51486 | -48.58062 | 2025-10-22 04:55:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93b45c67-7831-30e6-918d-9deaf78cec62 | -12.31649 | -47.83601 | 2025-10-22 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36883eb8-42d8-374c-8bcd-33de61b65215 | -8.11514 | -55.08503 | 2025-10-22 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f16c8894-0fe7-3b00-9d7f-6dbedb92b079 | -9.72343 | -67.4746 | 2025-10-22 04:55:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7370bb70-9eba-3e91-9415-09316fde9a09 | -9.58985 | -63.49845 | 2025-10-22 04:55:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0cd3cfd-6c58-3ffb-b3e4-679ddb1e5456 | -8.99055 | -65.9184 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b84a602-42a9-319d-8059-6ae39d340ee3 | -9.0049 | -65.91522 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91a8e3d2-549c-39e0-9aed-a632f5a0a9f2 | -9.01029 | -65.94022 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9d322967-35ad-37cf-b85c-1f993a4825f0 | -9.00921 | -65.92802 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6a363834-48cf-3185-8e5f-8fcbfe6a836d | -9.79756 | -67.03485 | 2025-10-22 04:55:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb45e7e6-4eec-3410-a6a7-1181cb0d1f7c | -9.72702 | -64.93767 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db61fb9b-9245-30cc-8cb8-9942e4232f2e | -7.93511 | -46.01168 | 2025-10-22 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb58022e-90b0-37eb-b083-231a5e41e622 | -8.99931 | -65.92598 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e7d186c-d4f3-3991-871f-d02c132b8e32 | -9.54727 | -66.65012 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 988736ce-49f0-3942-98e8-d1b18fcd226c | -9.0037 | -65.93884 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bba5b4e9-c20a-376c-97c6-c6b7a12a4e7a | -12.81893 | -48.64658 | 2025-10-22 04:55:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b99fc7d-cf1f-3c34-95ff-1d295289076a | -7.94476 | -44.84008 | 2025-10-22 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d0bcefe-835c-3173-ab64-1e9f20d6aa07 | -9.77962 | -63.81405 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d08f023a-2f75-3a19-a5cd-73cfa027a01a | -9.72587 | -67.47409 | 2025-10-22 04:55:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e626d83c-4322-3f60-8226-f058f6a82ba2 | -7.65348 | -44.58998 | 2025-10-22 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9292f212-ff1b-3383-96f8-ac0af54cf425 | -13.11843 | -48.2422 | 2025-10-22 04:55:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb535e3a-5ec6-3beb-975d-832ac7c6b709 | -7.6555 | -44.58846 | 2025-10-22 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cb1504e7-99c7-3551-9706-92f59812c0b5 | -9.00917 | -65.94611 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dfb2f178-fb16-35d2-82b4-913a61ad7a1e | -7.15927 | -44.9972 | 2025-10-22 04:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84c013a0-86ec-3205-aa69-863f9a587ec9 | -9.48565 | -65.64809 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 691263cc-3a66-3164-92d9-1b3ce4b92756 | -13.46336 | -48.82877 | 2025-10-22 04:55:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99eb5851-f81a-3aa3-b1db-833fc9fe7b2b | -8.11859 | -55.0856 | 2025-10-22 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 191a9164-dbe7-3f98-8781-0a4d3d44eb11 | -8.99397 | -65.90126 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ab4beb3-a526-3ae0-bc3f-097d815d9f02 | -12.50346 | -48.57096 | 2025-10-22 04:55:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d8905d8b-5ebc-3482-9505-7df6bc0f4f1e | -9.57007 | -65.22005 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31d60e55-7b18-3321-8cdd-3e3807d0224c | -9.0048 | -65.93307 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fa630ee5-b85f-38f0-ac44-f396adcdd387 | -9.08688 | -67.69162 | 2025-10-22 04:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c5dac29-792e-33b0-b14b-aad6d2083c32 | -7.93442 | -46.01653 | 2025-10-22 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75d11e8c-c47d-3143-9b99-589c372fc4d0 | -9.911 | -65.02792 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 375a7d48-8677-37c6-a0cf-4baeb8ff2558 | -13.46284 | -48.83255 | 2025-10-22 04:55:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 645e542a-05b4-3532-8c77-f7d188494ff9 | -12.64092 | -47.58042 | 2025-10-22 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d86aea84-d787-3080-9a97-31f41c94428f | -9.00807 | -65.93377 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 04e4e655-7e97-3682-9244-8e9b6e7f9929 | -7.65509 | -44.59138 | 2025-10-22 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f8851ba-b968-3576-8cc3-37056e23cfd1 | -9.09415 | -67.69314 | 2025-10-22 04:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66a5b687-ca7c-3b51-ac4e-fd7c6fbaa001 | -12.4988 | -48.5741 | 2025-10-22 04:55:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2014401c-5b64-3e60-8ca2-428cf6f2a3bf | -8.34783 | -46.19112 | 2025-10-22 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 175a428e-87e7-39f6-ada3-0b269e909a1a | -12.51071 | -48.57997 | 2025-10-22 04:55:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d12dcfc-70d3-3cbf-bb34-52a1b7834bce | -9.01352 | -65.94091 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 30be53f7-ea02-38e8-80d4-2abfc941c100 | -13.46388 | -48.82497 | 2025-10-22 04:55:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d7206ba-c836-3267-8400-dccf786be910 | -8.9982 | -65.93173 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71b8c232-3d4d-3d6c-abfe-69069bb2b092 | -9.10386 | -65.93462 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f5ac4be-f232-39db-8e76-ef340630a0ba | -12.81939 | -48.64324 | 2025-10-22 04:55:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81798a16-a16f-3053-bf39-e8c5f0e8860c | -9.43715 | -49.19666 | 2025-10-22 04:55:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f92a9540-924f-3fcd-87db-ac4ecbb2f1a1 | -9.11042 | -65.93615 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77b820e4-7c11-3c36-939e-dfbf9d321b2b | -9.1085 | -65.93175 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95d950eb-cc86-3ce2-aa9c-c1e26f524184 | -7.94396 | -44.84606 | 2025-10-22 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52aa4c5a-5d26-32fa-8d0b-dc8454fada8f | -9.00147 | -65.93247 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 99a78d45-072a-30d2-bd57-2a029d8ac976 | -9.59547 | -63.49961 | 2025-10-22 04:55:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b22d910f-36a8-3ec4-81de-f37f3d9fa0d2 | -9.11414 | -65.36317 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05208986-3ab9-3569-ba11-dd4c0f7f83d1 | -8.22601 | -45.80691 | 2025-10-22 04:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89c065b1-04cf-31e6-9505-cbb5eaeb1edc | -9.00041 | -65.92022 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 26088b0d-5cb7-3edd-af9a-61f8ab388854 | -9.09469 | -67.69168 | 2025-10-22 04:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e160da0c-fea5-35e1-84d6-8158f2ed0b29 | -9.00811 | -65.91579 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bd575f6-783a-3ed7-a446-f27b6409d4f7 | -9.64395 | -65.2581 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9069b919-a4b0-3a0c-b03c-adc34186a3e6 | -7.16172 | -44.99474 | 2025-10-22 04:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2a0e7ac-124d-3aa6-95bd-4c6463f21a6d | -9.79894 | -67.02803 | 2025-10-22 04:55:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64b1d4a4-b4d5-3d54-aa1e-c7695fbc63c8 | -6.17667 | -52.06462 | 2025-10-22 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e0b3f561-1768-3266-bd35-187499d7b475 | -9.01141 | -65.93438 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 10770dec-627b-3742-8637-d54ff11bfadb | -9.57363 | -65.2226 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aed71742-5f18-3d63-96fe-a51059262672 | -10.06058 | -63.52806 | 2025-10-22 04:55:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8872e795-f8c0-31a0-9178-ec0e45904ee8 | -7.073 | -44.10609 | 2025-10-22 04:55:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d644a4e0-3fc9-380e-885f-f59898e9edb5 | -8.34327 | -46.19021 | 2025-10-22 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49c001f4-cddd-36ee-8299-aa2064cd8820 | -12.63587 | -47.58427 | 2025-10-22 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c0894ec-70f4-343f-a7ca-ab790b4214a5 | -9.71489 | -67.48019 | 2025-10-22 04:55:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b30cc59-ef6c-311d-a9fb-6f2db604035f | -9.10736 | -65.93747 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5cbe27c-aede-3377-9fcb-123e31fbcf66 | -9.01251 | -65.92859 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 66d5e65d-d071-32f8-bd1c-a97b0f750e04 | -9.08742 | -67.69012 | 2025-10-22 04:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c4b97b7-ecbe-3154-a017-01f84a6d8173 | -8.99601 | -65.92542 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 54c39c01-35e3-36a2-b98b-7a47e6ab1f84 | -7.07252 | -44.10941 | 2025-10-22 04:55:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76823b0c-6ba7-3578-be72-675087963e06 | -12.50294 | -48.57476 | 2025-10-22 04:55:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6559293b-80e5-3326-be95-18f9fda3b16c | -7.93048 | -46.01099 | 2025-10-22 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2f4e64e4-5f6b-3670-9e3a-3960d1680673 | -7.48942 | -47.03413 | 2025-10-22 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b42ce779-6310-3d5e-b504-15a64e4770c2 | -13.12271 | -48.24283 | 2025-10-22 04:55:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cacf69b9-dbc0-373c-a537-f11d41820ee1 | -15.49069 | -49.00106 | 2025-10-22 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1513c9fa-e516-33b6-aee1-c663dcd24733 | -15.28075 | -59.24191 | 2025-10-22 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e457bcf-87c4-3c34-b94d-516ba6ba98df | -17.41779 | -55.07944 | 2025-10-22 04:57:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f0a140cf-b38a-3b77-a4a4-83f1e0102473 | -14.69156 | -48.78616 | 2025-10-22 04:57:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README15.md)
