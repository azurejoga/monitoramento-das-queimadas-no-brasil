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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9a62e14-7e46-346b-b336-01368af85017 | -6.45949 | -59.98654 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b8153fb4-6aff-3d9e-a23a-c27139c6a367 | -10.87111 | -53.96394 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee5237fb-ea90-3f91-b2c3-5687d00cd066 | -9.73544 | -54.81385 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3eb8e50-6335-301a-9133-eb80b4782ee7 | -11.13257 | -54.00935 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8874f47c-7e72-3f6b-9981-bd9576e3061b | -8.80044 | -60.80069 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 283448a0-c347-36cd-a14b-d68102c1ecb0 | -9.29637 | -60.53297 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fab5142c-32d8-3979-97fe-4b4ad84c4b83 | -8.79356 | -60.79469 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f9b3558d-5a0e-32e5-acc8-ae55a93bef2c | -10.41331 | -50.23381 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f20109f7-5212-3ce0-91bb-1db7570c6190 | -9.58229 | -55.1078 | 2026-09-21 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff95604d-4eac-3300-861b-ed58147b83a1 | -10.40822 | -50.23767 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 58a92afb-5e89-3a88-854e-b0e34836cf01 | -7.40446 | -55.17062 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bc4b05b-ab2e-31a2-8165-d23656cefe86 | -10.75728 | -50.80054 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 366df903-0d9a-3ac4-afe8-f6e219e06520 | -10.42597 | -51.86989 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5800f3f3-98e2-340a-8828-e3eab43bee3d | -10.4872 | -51.28223 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e1a56737-ea73-33aa-b549-7074e866cc8e | -9.03403 | -48.15165 | 2026-09-21 05:06:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 89238cc8-7653-3f03-ac6a-2df838c44b46 | -8.09288 | -55.35655 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0745fc1-8e79-3508-bade-a67ae096a484 | -10.34411 | -50.20562 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56a722d8-1006-391f-a1c3-0aa66f07f3b8 | -8.26773 | -50.87436 | 2026-09-21 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bfa1f40-ac58-31d5-8216-a3eb5e22c392 | -6.45873 | -59.99112 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c66c1a8e-ab52-3953-9d1c-e2ee1fe219d7 | -8.60398 | -54.7873 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 595c9358-065d-327b-bd05-a8a4c794467b | -7.32689 | -55.20924 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dbe79835-c68a-3054-8c23-1448390a801f | -6.44975 | -59.97291 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 74b3138c-54dc-31c3-87db-05801f8719d2 | -6.79702 | -59.13952 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ced9836-ac09-3362-b67c-77a58168f72c | -6.44293 | -59.9698 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af88c106-939e-3275-832e-fb6d69caed51 | -7.57677 | -57.67994 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c8068800-14c4-30e4-b326-90ccfd124bf2 | -8.1689 | -54.76663 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e486030-6491-3333-972d-ffce7163768a | -12.45984 | -54.45339 | 2026-09-21 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90260c22-45fa-3c1b-afcd-9a543125799a | -6.68778 | -58.45978 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63a62d47-e52b-3b6e-be86-1a8954681f49 | -10.53609 | -54.49869 | 2026-09-21 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1de23904-f2b1-36f1-8fbe-f766e76e85cf | -8.61182 | -54.59583 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57d03e5d-7638-35a1-a52a-cbcf20f6c22f | -6.99149 | -61.34975 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88782630-25f3-3d6d-b6e6-0a06b551da48 | -10.86729 | -50.93161 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb75b419-0c91-3ee3-9e47-1e78d74221cb | -6.4625 | -59.99175 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6a23621-4652-301d-870a-2fae9a0db034 | -10.7417 | -50.78551 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21815ea5-8266-3ed0-90c9-7e1698aafec2 | -11.75711 | -54.56471 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fefb2700-c354-36a6-a297-c41adc6d17f9 | -8.19183 | -54.7066 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 910bfcfb-485c-331d-b626-547fa5f5540e | -8.61238 | -54.59211 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78abb421-03d9-35b1-a7fd-037ec286c0b3 | -8.17739 | -54.77913 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e52e0761-3804-3867-98d2-50a31c50e988 | -6.46553 | -59.9735 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6148e051-f3fd-3d0a-b19c-243d20a95e41 | -11.72794 | -54.56159 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6587d195-0356-3282-bb5f-72822f81b1de | -9.67475 | -54.33007 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18c321a4-c45f-31ba-a418-2dad2e2b0421 | -7.32299 | -55.60973 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1a3a5e8-d04a-34ef-a3c4-5a446c583312 | -9.12755 | -61.50027 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cf510ed-b698-3868-af2a-75b276199daf | -9.68516 | -54.33173 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 822d3110-420e-3381-b909-f7977c37d0fe | -9.53125 | -45.40251 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2bd1bba-c937-3461-9652-c2f199b7c461 | -9.02343 | -44.91465 | 2026-09-21 05:06:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0f8cbc0-9c0f-37ef-9df4-622aab3cec82 | -6.43015 | -59.97451 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46f45545-3398-3b74-9f00-71d81b231288 | -10.46783 | -61.31397 | 2026-09-21 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5b2523a-bf7d-3b6b-810c-812f9711775c | -9.66722 | -54.33287 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21c9d49c-1fbd-3fd5-a07f-e8ee1b90604c | -8.17284 | -54.7635 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f983000d-e103-357f-9648-2b44582e48a2 | -10.77168 | -50.82389 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91a7cd95-6f99-3ecc-b2a1-05b56749e396 | -7.12798 | -59.64804 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d50bc7c5-4d8a-3a16-9e24-32fe70316f69 | -8.78253 | -44.29385 | 2026-09-21 05:06:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74c852f4-175d-3674-bc4c-357b2e900970 | -11.129 | -54.0088 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a6a017c-aaaf-31f8-ba7f-12b754a6d7aa | -9.58002 | -55.09999 | 2026-09-21 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09e3667a-f3ef-31dc-a869-3da002b95bad | -11.05696 | -54.90606 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 831348f6-822c-3439-b2ad-ed154aca8702 | -11.93942 | -46.5037 | 2026-09-21 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a89ec4d8-161b-32c0-bc88-440737a6822b | -10.47192 | -50.29418 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2a044ff-60c6-3279-abae-04e7c568ed7e | -10.87652 | -54.07829 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1de0fc44-3d82-39fd-9182-1be51426a037 | -11.75654 | -54.56869 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 339c3aba-8120-3e27-b9e1-a89d983b34dd | -10.87273 | -53.96148 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa8734d2-85b4-3069-964b-43a6ad69cb0a | -7.88343 | -54.7273 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b504fcd-88c8-3a66-b044-1592a6f8185f | -9.17445 | -60.30396 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80450849-a211-324f-9d68-72a0ff05de0b | -11.83274 | -47.61926 | 2026-09-21 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3799f54-d69e-34a7-802d-1f33fd06662b | -7.87945 | -54.70797 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cd2dc8c-e2c7-377d-82c5-fb5f356b8fb1 | -9.82424 | -48.43156 | 2026-09-21 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b038b4b2-9e26-3424-b9f7-82bc5c9724ea | -12.28078 | -50.15921 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51da624d-1bc5-3980-b276-a0ba0b7337fd | -11.94375 | -46.50924 | 2026-09-21 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c2f2486c-39bb-3dc9-ae59-77be1dbcc02d | -10.34859 | -50.20626 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da99cc97-87f8-3ea9-9d19-79172abb4349 | -10.58639 | -57.49561 | 2026-09-21 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5d150e1-2ef6-3191-a640-c33bf6995b27 | -10.48085 | -50.29545 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7b8393f7-85f8-3032-bb9b-4abcd237a1af | -10.85626 | -50.15709 | 2026-09-21 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64121343-d7cb-3dc2-b91f-4e54d3f84470 | -9.2783 | -60.63595 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 304dcc92-e2b4-33a7-bb61-3460e4c74269 | -11.4702 | -47.76905 | 2026-09-21 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 63e368dc-fd5d-33e8-81f9-bf7afc45e86e | -6.76023 | -59.11671 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37e83411-e9f7-3a2b-a5db-c6dab69c34fd | -10.4398 | -50.26216 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ad52247-fbf2-312c-ac84-69f0c2ff8e28 | -9.03971 | -61.65515 | 2026-09-21 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2597ee43-728d-3af4-901d-34a360de4c6f | -11.82674 | -55.21687 | 2026-09-21 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 035b26d7-a172-3751-bd93-54a162715277 | -9.02513 | -60.36283 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45ac6a18-e16a-3b78-8895-7850b3c93bd3 | -10.11465 | -48.4379 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d28dd1b-6ec6-31c9-9392-e93110ab3f36 | -8.61698 | -54.79305 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b681a7a2-f0c0-3933-a1ce-9087b5b1a9c7 | -9.55167 | -66.00518 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e82d5f4c-9e7a-3a06-b22b-a050a7c17540 | -11.02738 | -54.13696 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5033f21b-28d5-344c-9fa2-1abd1988fb26 | -8.85867 | -68.51201 | 2026-09-21 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1be9add2-eb59-3f02-95f1-29aa5da76552 | -11.73906 | -54.55921 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10ae9c6d-61b1-369d-a375-881564e22ed7 | -10.87039 | -57.16076 | 2026-09-21 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b88ba94e-7ccc-37c2-943f-a58a6e0f2185 | -11.05045 | -54.15283 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19716905-96dc-3f12-9361-d4fdf6318e5f | -9.69328 | -54.32499 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64921479-964c-329c-9256-8076797efaa8 | -9.81446 | -48.30723 | 2026-09-21 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 542d2b76-aa40-3470-b6b6-4009cab0fe20 | -7.33302 | -55.21375 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d5b4137-3224-3921-b016-ad650f4e86d0 | -7.61034 | -57.61192 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2e9d0a2-3b87-328e-8add-960c004493dc | -11.09632 | -48.30729 | 2026-09-21 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4ef403cb-6d94-3296-8b28-8701d9f4dc6e | -11.35929 | -51.41546 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afed9a12-02ad-3a4e-b9c4-bb16cf6e48e8 | -8.60681 | -54.79152 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a1b84a2-d5ec-379b-91a0-06c8bf772f1f | -11.98537 | -58.07158 | 2026-09-21 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 766dd9c6-859c-3874-b0b5-d50dd2d74171 | -7.33292 | -55.61126 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb76cee4-4c67-3699-87d1-dc7431a52158 | -11.25485 | -54.13991 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e48b51c-6851-31d3-820a-c42328d0f653 | -10.4636 | -51.32916 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5750eece-dfc6-3091-b474-536af454dfde | -9.01856 | -49.82567 | 2026-09-21 05:06:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bda98b73-6329-367c-a71c-09c14c8bd98f | -9.58173 | -55.11145 | 2026-09-21 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README75.md)
