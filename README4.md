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
| b4aa5ab6-bb01-3c1e-b7a7-dcc028a3ab6e | -8.87532 | -46.94466 | 2026-06-22 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcd9ce3d-5c73-3e03-a547-673151ea888c | -13.29382 | -45.20182 | 2026-06-22 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7568d494-52c7-3654-b0dc-0ecd66c4338b | -8.88108 | -46.94042 | 2026-06-22 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 53938f8b-94c0-3366-a331-3138eea6515c | -8.87438 | -46.95 | 2026-06-22 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c4dbde3-949f-3881-8329-ec256bb3ab49 | -11.7983 | -40.08451 | 2026-06-22 04:06:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e98d48f9-48a1-3b8a-aacc-02746d2667dc | -9.0786 | -44.75689 | 2026-06-22 04:06:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e326c7aa-c34a-35e7-af63-1ad8b5573024 | -12.84889 | -44.39814 | 2026-06-22 04:06:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de20cd71-7978-3219-8eec-4d08a01aebc0 | -13.37109 | -41.35398 | 2026-06-22 04:06:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d931f8a1-c813-3159-8aad-dac293e7be34 | -11.1007 | -54.142 | 2026-06-22 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18141a77-c5fa-3f47-9f4a-21d5aa0e9be3 | -13.29745 | -45.2284 | 2026-06-22 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e115c77-124b-3888-a220-400f322a5356 | -13.29105 | -45.19397 | 2026-06-22 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87b9a05a-2d07-31dc-a9f5-d9bafb7a47e6 | -11.05147 | -52.47785 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90e20fc4-811e-3a49-9c08-470e73f41be9 | -11.05573 | -52.49108 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33ac0d09-129d-3c7a-b248-453fef53d41a | -10.54079 | -47.73392 | 2026-06-22 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22200562-9312-37ed-90a1-bdf32f241dc5 | -11.11419 | -54.15262 | 2026-06-22 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6143888-0bb1-36f8-a4bf-5c6e682b1574 | -13.29997 | -45.21402 | 2026-06-22 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5b1ebeb-0365-3178-a1ea-cd23da8d0bf4 | -12.20383 | -47.97079 | 2026-06-22 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ff4bc82-3988-3086-9719-96a1a8efbff1 | -16.02843 | -43.42256 | 2026-06-22 04:08:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 918cf079-37aa-3b69-b072-b50dd6d3f26b | -13.3021 | -45.2289 | 2026-06-22 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f8b1466-8cfe-3e93-b1fa-9a5a497da3c1 | -20.10561 | -40.59535 | 2026-06-22 04:08:00 | NPP-375D | SANTA LEOPOLDINA | ESPÍRITO SANTO | Brasil | 3204500 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b2e1132f-15f3-379a-a493-ffecb9ce089e | -13.30068 | -45.21387 | 2026-06-22 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88b35228-2311-3ce5-812e-95aaaf6a67f6 | -13.30275 | -45.22532 | 2026-06-22 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f944e56-3d89-3dfb-9a4d-2ee74375f4a0 | -13.52026 | -52.16766 | 2026-06-22 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f6eefc9-e9c5-3cb3-a2fd-be178343f2d3 | -14.10655 | -49.88327 | 2026-06-22 04:08:00 | NPP-375D | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a6c3323-6665-3289-8501-983034a55446 | -16.02562 | -43.41785 | 2026-06-22 04:08:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2c71fad-5b2d-32ea-87f4-7a97a7b01bc2 | -15.72578 | -41.3568 | 2026-06-22 04:08:00 | NPP-375D | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5e48ac1a-f748-34cd-99f1-664293cffe7a | -14.79827 | -48.96173 | 2026-06-22 04:08:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d9f6012-badf-31a9-ba77-2d14261f5e7c | -13.83546 | -47.12111 | 2026-06-22 04:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0261ad1b-52d4-30a3-8e45-47a8abe05fa4 | -15.72637 | -41.35318 | 2026-06-22 04:08:00 | NPP-375D | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 139ea167-f681-34de-86b3-7c9df848d30d | -13.30677 | -45.22604 | 2026-06-22 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99234ed7-7d1d-39dd-8d51-bb22588300ff | -13.30211 | -45.22551 | 2026-06-22 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5b086c3-5e92-3e35-9ea2-a26267a8d892 | -20.45333 | -44.74811 | 2026-06-22 04:08:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7bdcdcd1-5145-366a-8b75-6aa2e1579c66 | -15.38854 | -40.82383 | 2026-06-22 04:08:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ff5a73e5-6a2f-3537-8a4e-679e9878865a | -18.25502 | -51.27809 | 2026-06-22 04:08:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0a537d7-8f21-34b2-84e8-998c21848b53 | -13.30612 | -45.22961 | 2026-06-22 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 145233a6-6daa-3290-87d5-98f11859c6ce | -13.30148 | -45.2291 | 2026-06-22 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1268c465-3673-3869-a2dc-0256467a19ce | -13.51915 | -52.17297 | 2026-06-22 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b01a45c-7032-3247-9111-74773d406949 | -20.10897 | -40.59598 | 2026-06-22 04:08:00 | NPP-375D | SANTA LEOPOLDINA | ESPÍRITO SANTO | Brasil | 3204500 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0f0bd622-b7fc-3069-a2d5-8c0a531b1e1e | -18.24884 | -51.28048 | 2026-06-22 04:08:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05a347d6-9966-3aa8-bdaf-64b4b380082d | -19.70095 | -47.32756 | 2026-06-22 04:08:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b5b6fcb-3d9d-30ed-9c48-4ea2de2c4b7b | -16.02492 | -43.42192 | 2026-06-22 04:08:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f84c693-1278-3d37-b15b-39d7da0ade7d | -17.22063 | -43.67961 | 2026-06-22 04:08:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 41f9d760-cb5c-3446-a001-a55837901c55 | -13.83459 | -47.12569 | 2026-06-22 04:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a8c6f9e-400c-3f2b-a05a-0f2a27b19898 | -18.83324 | -40.00024 | 2026-06-22 04:08:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4bd3ea0b-6875-3a83-9835-7878f7300ef7 | -15.38521 | -40.82327 | 2026-06-22 04:08:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4a6021ea-ee4f-3ec7-b812-9d7717db2b0a | -13.3034 | -45.22175 | 2026-06-22 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bf170ef-32ff-3a2e-9408-a09bbff422bf | -13.52645 | -52.16921 | 2026-06-22 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 653c73b0-2ecd-3e93-8b02-5e6356d480b7 | -19.70237 | -40.10366 | 2026-06-22 04:08:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 72811710-b492-3345-961a-b8fcd84f98dc | -13.29807 | -45.2282 | 2026-06-22 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39144d65-2fd4-3162-b79d-08f77cd7b9e0 | -13.51291 | -52.17162 | 2026-06-22 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88739a37-8b53-3c6b-a6be-e2bacb5a0978 | -13.51402 | -52.16636 | 2026-06-22 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d791cd97-268e-3b40-b79e-01654785beb4 | -13.30273 | -45.22193 | 2026-06-22 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7ee879e-f916-3d52-948b-7b3f057f8c9b | -18.25426 | -51.28166 | 2026-06-22 04:08:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e17cbac-5e17-3cdf-8259-1668c5851af7 | -14.14893 | -44.24697 | 2026-06-22 04:08:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a25750c1-13e0-3f7f-9c6d-3f77152902bc | -16.51515 | -47.79139 | 2026-06-22 04:08:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5adf8795-c3dc-3313-aa4c-f01c0efb0bf1 | -13.30003 | -45.21746 | 2026-06-22 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a8ad956-1280-3319-8aa7-4396bd4cf38d | -21.66956 | -43.60349 | 2026-06-22 04:10:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cac5c880-bf52-33a3-a7ea-62d4129a5488 | -21.66682 | -43.599 | 2026-06-22 04:10:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 39089f76-9843-35bd-8623-95531cf196f4 | -3.50991 | -48.03395 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cad90202-fac7-3a48-8a47-6c7345321f33 | -3.51293 | -48.03912 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7a54cd7-6453-3e57-9e82-edd9909e198b | -3.35596 | -43.17049 | 2026-06-22 04:21:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 642e9990-ffe3-3180-a6d3-cda5099a3428 | -3.51744 | -48.03514 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 680645e7-135a-3775-b37f-b266989ec81f | -3.50916 | -48.03851 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8165f6e9-6021-3db0-821f-21af4719b86c | -3.5054 | -48.03791 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c8050df-7a42-39fc-804b-34312dc8fdb9 | -3.51368 | -48.03453 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce454c8e-18c0-3edf-bc80-88970f4410c1 | -3.51442 | -48.02999 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 712fda6f-572d-32e1-ac7a-a24bdb4e6d0b | -3.50762 | -48.04791 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 064dd09f-af3b-31d7-93c8-ad75cf5b0884 | -3.98497 | -39.81262 | 2026-06-22 04:21:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 560e07bc-fa3e-3b6f-9a7c-9c0357d1b450 | -3.51669 | -48.03978 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c23a2622-7711-35a0-b0e2-511baeea1182 | -3.50614 | -48.03339 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14dc9f52-ce62-3e17-87f7-b52565e84457 | -3.50839 | -48.04324 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 313fbd74-0fe5-34a5-b932-36fd271fbe41 | -3.51215 | -48.04385 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69ae2de2-81af-3c28-a7cd-ea01a6980f82 | -3.50462 | -48.04264 | 2026-06-22 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7f0399f-0679-3f27-8d52-507e24a29860 | -6.50869 | -44.69876 | 2026-06-22 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0d196641-ac8b-3f94-ab96-28d51a19601d | -8.87127 | -46.95294 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69856612-f2e5-3670-af77-2d49ac7dd959 | -7.31997 | -46.55014 | 2026-06-22 04:23:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3a4149a-ade2-34e0-a541-0c7b534513cb | -6.50528 | -42.22939 | 2026-06-22 04:23:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7690e658-c37e-3ee0-b468-20d052fdc4fe | -6.25301 | -48.53107 | 2026-06-22 04:23:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69e59d53-0be7-30e8-8f47-81d66b057914 | -6.49932 | -44.69374 | 2026-06-22 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b625bd01-542f-3b27-8752-0464c0746ec7 | -9.49962 | -42.99042 | 2026-06-22 04:23:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 52dbae21-81f0-3f30-a87e-da177c28c606 | -6.24929 | -48.53035 | 2026-06-22 04:23:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 559a64c6-8a43-35fe-9dcc-8ceb19124bcd | -8.87562 | -46.95325 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 194690c9-c3e7-3802-96f7-9b8ad4a00580 | -7.32276 | -46.55431 | 2026-06-22 04:23:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6799724-b983-39e5-bbfb-3d7408282c27 | -6.50924 | -44.6953 | 2026-06-22 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 61c74c9c-0d5a-3a41-b0f6-e580c03b2d03 | -9.69081 | -47.69555 | 2026-06-22 04:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f42555c-f012-3777-899d-1cb613d2b546 | -8.87622 | -46.94959 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f52e0b27-95aa-39c4-b2a0-1d029016f3b2 | -8.87642 | -46.94253 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca174e9f-8d77-3a62-a766-19e5c8d4396a | -6.24037 | -48.53784 | 2026-06-22 04:23:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb00a116-0b9b-3863-a1aa-4a45f7b5ab37 | -9.07873 | -44.7514 | 2026-06-22 04:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f35614b-4359-3271-bcf7-6566322b686a | -6.50208 | -44.69772 | 2026-06-22 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3e81c4ba-2bf6-3491-a720-166008b256b2 | -8.70235 | -47.97416 | 2026-06-22 04:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c2581a1-1927-396e-b1b8-c8a41db7ab29 | -7.97286 | -47.42833 | 2026-06-22 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2441f91-baa8-3c5f-951c-d15bf32cb63d | -6.50354 | -42.21723 | 2026-06-22 04:23:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| cfc5f69d-df0f-38a0-97ac-01e470db41b8 | -7.96655 | -47.42333 | 2026-06-22 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5711b383-6d0a-30e2-93ee-e9cb62d4b81a | -6.24253 | -48.52492 | 2026-06-22 04:23:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d76d29ed-499b-39cb-a327-5f181e3ef528 | -7.96939 | -47.42772 | 2026-06-22 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 949a1b8b-130a-3de4-999a-06e5f8f4c172 | -8.87742 | -46.94231 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2c096db-fc1a-3d2e-8528-c0c756309446 | -8.04818 | -47.24912 | 2026-06-22 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cef7741-e6cd-32d0-9231-1ccc3491e7a9 | -8.01841 | -49.64149 | 2026-06-22 04:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd0afeab-37e9-389b-93fc-454acbbb8fe0 | -6.50484 | -44.70169 | 2026-06-22 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README5.md)
