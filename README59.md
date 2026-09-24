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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 519e5697-396f-3dd1-baa6-b4a71f1fb241 | -12.41377 | -46.94613 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e5138f8-9724-38cb-a54b-143db790a580 | -10.62219 | -53.99178 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa3ea01b-9eb7-3a14-ae8e-a16d94fb6d59 | -10.27035 | -49.95415 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19daf927-07f5-3f24-8c44-0b7f2b6615ec | -6.62138 | -59.93315 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5dc2379e-878d-3893-9002-192bcbdc759a | -9.25906 | -46.24519 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 17958a1d-04e8-3f65-b041-39887ce44e35 | -11.40653 | -47.40065 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abe2743a-6c37-3591-9293-fafee6252ed0 | -10.09951 | -46.06729 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6578d92-7655-396d-94ea-136065e4264a | -11.99661 | -52.46607 | 2026-09-24 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 30511043-d787-318e-99f1-fd065f1b4f35 | -13.38644 | -41.31902 | 2026-09-24 04:46:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4dfb5f6c-3ec6-3474-b156-a37af397b1aa | -12.41318 | -46.95001 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a2c5522-0ad5-37c7-8ab4-76f7d3ab83d2 | -6.08085 | -57.62596 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 382bb579-4392-3bb3-910f-a530292b5ca3 | -9.59202 | -47.77274 | 2026-09-24 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54be1d49-93b2-3f22-bc76-127a7336dfce | -13.7828 | -54.04992 | 2026-09-24 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9eaa82f8-5909-38ea-b418-3206b5629d4d | -10.08066 | -46.0481 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 84fb1092-68c9-3cf7-bad3-f6b2c360c28d | -8.42014 | -45.84464 | 2026-09-24 04:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1f200c9-9a6c-3bd9-bb74-281eb911eddb | -13.1824 | -51.54245 | 2026-09-24 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74be9527-1b0e-360f-ab25-104acad8a4cc | -12.10596 | -50.73801 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 927791d9-c8f1-3d5b-8659-b50a34f7b217 | -6.67114 | -58.57598 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b082a27-e315-3cef-994d-d75c01b0ea15 | -9.26542 | -46.25022 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1be5513-95a3-3290-8beb-364dcaf116a3 | -11.43179 | -44.19245 | 2026-09-24 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f43f37e0-4a6b-3b59-8bf9-de141e4ee4ed | -14.07802 | -44.01238 | 2026-09-24 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab8b12a9-ede0-3136-b625-694a68d312a2 | -9.25746 | -47.34107 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18a17b70-e1bf-3815-a20f-e55575556252 | -12.0039 | -52.4674 | 2026-09-24 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| beffed20-3f56-377c-b9cd-aa4aa2292eb6 | -7.99714 | -45.02344 | 2026-09-24 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 205a3b3d-955c-3da1-a8d0-9454a855f723 | -6.04559 | -57.77306 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec4f42c1-d430-358d-8e2a-d3d5001f9669 | -7.88971 | -61.17091 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6c550e76-bc2f-35ad-99e9-77c0ffc9a380 | -7.8977 | -61.16589 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 014d61f1-c64e-3f61-811a-107372bd83a0 | -13.93069 | -47.82699 | 2026-09-24 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35f196e3-8d09-3580-911e-667805136107 | -9.85336 | -48.50382 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09e4f837-a84c-3f0c-8173-63234306836f | -11.68148 | -50.18981 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 411915be-ab66-3f73-a372-6a34c7cb0ce0 | -13.94038 | -47.83242 | 2026-09-24 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42aaa35e-76b1-35c4-bc8b-8c1b700abd21 | -9.86885 | -48.31932 | 2026-09-24 04:46:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d49f70d9-9387-3055-a64b-77b91b14a3b6 | -8.27552 | -54.75969 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9f992dd-be82-3c23-a6e1-a1a1a2575e33 | -8.39017 | -46.29593 | 2026-09-24 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 60d83644-e9fb-3a1c-a7b7-c7226ba61951 | -15.23757 | -43.2686 | 2026-09-24 04:46:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 47d5762f-b1a7-310f-8082-87a866d51cd9 | -11.66523 | -43.49443 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f945cb5a-21a5-372d-b7ef-9f58bd05596b | -11.13357 | -48.3152 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84bc909f-0dbd-35a9-816f-e0f58808348c | -11.64851 | -43.492 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| efc8cc07-815f-3d9d-b1d7-77e5ba22f158 | -11.79427 | -50.99359 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bea2b42-2b10-337e-a58b-4eba025a176b | -8.1416 | -46.82188 | 2026-09-24 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1e53917-436e-33ee-afd5-3ab26bcd6a73 | -9.35217 | -50.10053 | 2026-09-24 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2641d931-3074-3e28-baea-c01814bbbe29 | -13.78697 | -54.07153 | 2026-09-24 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5051f3e3-fb7f-3c54-af9c-cae55e330274 | -10.61875 | -53.9874 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71c38b50-4923-39dc-bd28-f97ed9964a54 | -6.06695 | -57.79787 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87454005-20fd-3323-8da6-39ba6675a4d4 | -6.88473 | -55.56169 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0f25dc2-6ab8-309b-abab-765ba2096ae5 | -6.12671 | -57.75734 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 287aaebe-29d4-3c8d-848c-3573431768b9 | -6.88861 | -55.5677 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a5954dc-cfaa-319d-bb6f-88b11291eeb3 | -12.85376 | -44.39217 | 2026-09-24 04:46:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb0ec812-ba7f-3fab-a0c7-bceed5b52c6a | -9.26482 | -46.25407 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0b135a13-1cc9-379e-8bba-a846cfb0dd3b | -7.88047 | -61.17648 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a3ba8ca-cdee-314b-ae34-828f197767b2 | -9.17252 | -49.67587 | 2026-09-24 04:46:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 845f5df5-4001-3574-b252-93ea265ed408 | -6.44453 | -59.94986 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 17a823ae-e1b0-3ad3-8bba-ef69438fde33 | -6.46341 | -55.00433 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb25f1e7-00b4-3da4-bc89-86ff6d18145d | -13.46226 | -46.26021 | 2026-09-24 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 638eeeaf-b323-3a8b-9d2b-e64b164b50ef | -10.43445 | -46.25829 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 955c8af6-007d-3012-aa3c-c79071ad5563 | -11.99007 | -52.46044 | 2026-09-24 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83279b15-017e-3152-9f23-086beeae691f | -10.44143 | -46.28343 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75bd510b-e14b-3ec5-9b3f-88c29f115352 | -8.93123 | -45.94227 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4b5c92b-9cb4-3212-98a1-4aa1a297d6ab | -9.17419 | -49.99244 | 2026-09-24 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef07cf69-1cfc-37a4-b64a-af26685894d8 | -12.91705 | -50.90666 | 2026-09-24 04:46:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1863c855-95d1-34a2-b313-4c5674de5d02 | -9.2246 | -47.34669 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39de9611-ffe1-35cb-b4d6-e9fc434ff8c8 | -16.54686 | -49.90557 | 2026-09-24 04:49:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee10c258-db8d-36de-9539-b870bde2e133 | -14.57538 | -54.13198 | 2026-09-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afc249ba-ea09-3197-8d08-70c2e1decf5f | -18.34811 | -46.41419 | 2026-09-24 04:49:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f24829d-97d8-3e81-b938-af20dbd37a4a | -14.56555 | -54.12 | 2026-09-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ef5be15-3319-3345-b316-edcd0ebe25f9 | -17.84704 | -52.38972 | 2026-09-24 04:49:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1427c7f-db01-3b2c-a1f5-fc474dd034fc | -17.85046 | -52.39035 | 2026-09-24 04:49:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19d688dc-93df-3ae3-b7e4-900bee6ccfb5 | -18.88585 | -47.17169 | 2026-09-24 04:49:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 515b28fe-bd87-3686-9acc-0f26d8225df2 | -16.616 | -46.20176 | 2026-09-24 04:49:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff90f6aa-7602-3248-b3ad-ae5ee405737a | -17.97594 | -47.85183 | 2026-09-24 04:49:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea6f83f8-242e-38b1-8fa3-0cf56871b0f5 | -17.57393 | -43.77426 | 2026-09-24 04:49:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05f283cd-7cba-3a61-a5c6-abbef6a55553 | -16.87058 | -43.20737 | 2026-09-24 04:49:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 105353ea-d38b-33e8-bdb2-e6f3f721f7e6 | -14.56642 | -54.11509 | 2026-09-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54726f79-d463-30e0-9bf5-9eeb836ea0ad | -14.56468 | -54.12497 | 2026-09-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f0899de1-0114-3048-929f-71bfd42aff50 | -14.57923 | -54.13274 | 2026-09-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 132b6f9e-4cb7-32db-94a7-98b8aa900db5 | -17.02049 | -51.00696 | 2026-09-24 04:49:00 | NPP-375D | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 351feada-1cbb-388e-b646-033ae882dc04 | -19.18567 | -47.36216 | 2026-09-24 04:49:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c677c05f-4e97-35d5-830b-29d08519fa6e | -14.56081 | -54.12434 | 2026-09-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 17fc8e66-8334-3331-b37b-02873b5cc525 | -18.88522 | -47.17627 | 2026-09-24 04:49:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fd4115f-e1bc-3b17-b342-50d7a90b53ee | -17.56948 | -43.77359 | 2026-09-24 04:49:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3820a73d-dead-30ee-84ff-6232af0f1d34 | -17.97301 | -47.84709 | 2026-09-24 04:49:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2262d3b-bf5a-3f63-8ff1-4a6bf7cd8a19 | -18.34877 | -46.40928 | 2026-09-24 04:49:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8abe8bef-4012-386b-b1bf-c85f7db827da | -14.56169 | -54.11936 | 2026-09-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec2e7040-e145-3b9c-b3ae-46b7f6d2f34e | -17.95863 | -48.79079 | 2026-09-24 04:49:00 | NPP-375D | ÁGUA LIMPA | GOIÁS | Brasil | 5200209 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 296439fe-9a08-37d3-918a-b6ded979b0b3 | -18.88513 | -47.57543 | 2026-09-24 04:49:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1c26698-1d6b-3a69-83b3-9e2e751d07f8 | -19.67509 | -44.59117 | 2026-09-24 04:49:00 | NPP-375D | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26b6d28f-39a1-337c-aa88-bf1318925eb0 | -16.9971 | -45.46471 | 2026-09-24 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f845369b-8900-3a91-9cb6-b100470097e9 | -19.0013 | -43.75619 | 2026-09-24 04:49:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| daf8c8de-2ef8-39ed-b7d7-43c67008760e | -14.56257 | -54.11438 | 2026-09-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec2c5fc7-dd8f-3766-89e6-c8bb61c73c9c | -17.96948 | -47.8465 | 2026-09-24 04:49:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 205c51d4-5202-382e-abc0-88212bac97e4 | -18.24097 | -45.60621 | 2026-09-24 04:49:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e4548e2-bf82-3c99-a601-8c241ab7836b | -16.61593 | -46.19979 | 2026-09-24 04:49:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19732138-b0df-3d0d-bce2-552d5a755f19 | -14.57066 | -54.13617 | 2026-09-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8822dbac-f3dd-3aeb-bb9d-bdf3be6ee7fb | -16.54629 | -49.90918 | 2026-09-24 04:49:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 149c8437-1780-3285-b10c-dc9e316841bc | -20.28768 | -50.40697 | 2026-09-24 04:49:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 735c421f-18f1-399c-9fb7-f89857be5cd7 | -17.96654 | -47.84179 | 2026-09-24 04:49:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9911985a-585d-3e33-a7c1-1e31f61ac46e | -19.36816 | -50.90572 | 2026-09-24 04:49:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0eb39196-8171-3968-8fb2-49fbe426f7a3 | -14.57154 | -54.13121 | 2026-09-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58c300ac-1138-37a4-8e96-9bf66298e0d3 | -14.56767 | -54.13056 | 2026-09-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37005e28-fe23-3cf8-86b5-9d73ace42ccc | -21.21141 | -45.40683 | 2026-09-24 04:49:00 | NPP-375D | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README60.md)
