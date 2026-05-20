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
| 87fda83f-d26d-39ad-8eec-b5d03a5cd528 | -11.93378 | -46.92834 | 2026-05-20 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85267e25-d2e6-3e56-b51e-87f7328e2746 | -11.60673 | -55.32755 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa718830-6a96-3faa-a4b5-a3aa908f1999 | -11.47041 | -47.34213 | 2026-05-20 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41ab3f53-b31f-3519-b471-cfdc90a32f17 | -14.16161 | -45.30743 | 2026-05-20 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08d39dad-f7d6-303c-9859-6c70f9352c1b | -11.60125 | -55.33508 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4d61554-d03b-3950-9fea-c5cdcf557a57 | -8.71132 | -47.91838 | 2026-05-20 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd6ea958-aefb-343f-9eb7-c4b4eac23fd6 | -9.47763 | -40.49535 | 2026-05-20 04:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a51f71a6-99d1-3c78-9430-0304686347f0 | -12.22687 | -44.24533 | 2026-05-20 04:23:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8bc9ee4e-c4b3-36f9-b823-833055af9335 | -12.22298 | -44.24833 | 2026-05-20 04:23:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 023537a5-21d5-3bfc-9a29-ab78dd5998b5 | -9.89213 | -52.44287 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1616506c-7a99-3488-b91a-301681c47dc5 | -8.31965 | -48.00934 | 2026-05-20 04:23:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a53c7e5-d676-3085-864c-9a6feab436ff | -8.73246 | -47.98004 | 2026-05-20 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a898682d-7677-336c-a2c6-a22ce7f64586 | -8.70829 | -47.91307 | 2026-05-20 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1eedbab8-54d5-3300-b14e-0b24b9a4dbba | -10.32095 | -53.58286 | 2026-05-20 04:23:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92cf0d4c-8f99-3756-b4a8-d50feece62a8 | -11.92716 | -43.86924 | 2026-05-20 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0db02cb8-894e-3aa2-986c-f636a1b052ab | -14.15268 | -45.32056 | 2026-05-20 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a70ca93-c193-3248-acb3-20fd3889a589 | -11.01998 | -42.8549 | 2026-05-20 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1f64e286-b6b3-3d34-8343-265203279f75 | -11.4635 | -55.11931 | 2026-05-20 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fe0556f-14f6-36c3-ab9d-cac7f81b7de9 | -9.89383 | -52.44242 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bc120b61-bd6b-3fdc-94a4-3e7d76847e4b | -10.99986 | -44.81275 | 2026-05-20 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9104aadd-af5e-3c50-977b-a37cdef4af0f | -11.61758 | -55.33432 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2299deb-4841-3201-a871-fccd5cb3e65f | -14.15991 | -45.31812 | 2026-05-20 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0b6efa0-11b6-3cd9-ba5a-dd6a6e35db01 | -11.00097 | -54.00587 | 2026-05-20 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83502921-0d44-334f-902e-af2017412c9c | -11.61845 | -55.33001 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87f6c511-c7d7-34dc-9661-86cf023a1ba3 | -10.99652 | -44.8122 | 2026-05-20 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00aa1f2b-0d7f-3190-a5c5-8886c90fac2b | -8.7121 | -47.9137 | 2026-05-20 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82657659-5744-35ad-9638-502da47a0b55 | -9.8888 | -52.44152 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 982cdeef-6d84-3bd2-a59d-1483d469791f | -12.44436 | -44.7518 | 2026-05-20 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f1aa8be-16ef-3a71-9a4f-828a3d52bf7f | -8.73325 | -47.97528 | 2026-05-20 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 266b224a-694d-3028-8e37-c565c8ef42ab | -10.57443 | -46.65399 | 2026-05-20 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5697e442-de3a-3046-9eb9-7c4944cf6f1f | -9.9539 | -52.47445 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7aaefecf-67b3-3931-bd66-6469802d5a0d | -11.4577 | -55.11813 | 2026-05-20 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71140983-39e0-36f2-96be-7261812b8781 | -12.46216 | -54.45351 | 2026-05-20 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 588d9cf7-cf73-3e13-9c96-5ca4be0c470d | -9.9645 | -52.4734 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 903d57d8-7682-3701-940b-3ac83ef033c6 | -11.61463 | -55.32898 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33bc687f-6ffb-31d0-b791-ccc9342cf807 | -14.16105 | -45.31099 | 2026-05-20 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9025b8da-8c1e-36b5-ac36-7d2a903c6efc | -12.06482 | -45.28622 | 2026-05-20 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4476b320-8043-3243-951e-f4d754044177 | -12.35672 | -45.68374 | 2026-05-20 04:23:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa2d0e51-13e8-3209-9a0c-9c9f3fafb10d | -10.32633 | -53.58389 | 2026-05-20 04:23:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d942e867-1ecd-31fc-b382-3cbb0e573c34 | -10.11337 | -52.41425 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b888b118-0f0c-33e5-8c2b-d1c8f048863b | -10.664 | -48.25608 | 2026-05-20 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8d0f255-dad6-3244-b836-5b5ab26fcd43 | -11.18516 | -48.03496 | 2026-05-20 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5237a2b6-041a-32e1-9b7b-e4a64b3a8793 | -11.01378 | -45.13144 | 2026-05-20 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6189d1c7-e6f4-34ef-929a-07099b5fb6bd | -8.43542 | -46.92984 | 2026-05-20 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1950659-c72b-3c77-8fb1-86f1ad3c7e2b | -12.8951 | -51.87749 | 2026-05-20 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6f698e7-27bd-3ae0-9f77-016d83428707 | -8.7029 | -47.92176 | 2026-05-20 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 825e01b2-28cb-3922-8b21-6df564204bc4 | -12.05651 | -45.27388 | 2026-05-20 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| affaf4ad-9ff3-30c4-8549-14df1f49f686 | -10.32265 | -53.58274 | 2026-05-20 04:23:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e45f4145-9ab6-3763-a11a-802538ab1881 | -11.47921 | -52.91819 | 2026-05-20 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8364e70-fd40-36e2-ad6a-d10cd0f3f3ea | -11.03392 | -49.47895 | 2026-05-20 04:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f97d202f-e684-3742-bf5d-73bd094b2633 | -8.55146 | -45.98625 | 2026-05-20 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce06254d-3b34-3b4c-8d6f-5963895e3691 | -8.73628 | -47.98071 | 2026-05-20 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f1462389-613c-3ae7-8abd-935cf73e9869 | -11.00168 | -54.00222 | 2026-05-20 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a417705e-01cc-31be-b38b-ebc5def01d0e | -12.60215 | -44.52387 | 2026-05-20 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4f7be49e-84fc-383a-ae53-94c4db15e16f | -8.3235 | -48.01002 | 2026-05-20 04:23:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d9d3b85-9357-3f38-b0d2-aaeb1073f017 | -12.0609 | -45.28923 | 2026-05-20 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc5d931f-7db1-355a-a452-c332df23a056 | -17.70919 | -42.22578 | 2026-05-20 04:25:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 789147c2-9116-3ae4-a097-94e27b8bbdf5 | -17.59041 | -46.5658 | 2026-05-20 04:25:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3fa165c-adc9-383d-a9fd-55ec470cab99 | -14.16139 | -52.88649 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcf393f5-3215-3dea-b39e-d184cb41e290 | -14.15077 | -52.88989 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2da26eb-6cf2-369f-b066-2ddef74c3c6f | -14.64265 | -46.08829 | 2026-05-20 04:25:00 | NPP-375D | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f1a1af50-9cdc-31ae-beb3-29b73c69def9 | -19.31668 | -42.00661 | 2026-05-20 04:25:00 | NPP-375D | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4da35a50-36ae-383e-b5d2-6cf51e0dca29 | -16.42436 | -51.68263 | 2026-05-20 04:25:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ade21d3-b930-3c99-b685-62ce99d2e021 | -16.07085 | -45.89559 | 2026-05-20 04:25:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 84b43885-3841-3227-bd86-49fd677f0530 | -17.77175 | -41.74723 | 2026-05-20 04:25:00 | NPP-375D | POTÉ | MINAS GERAIS | Brasil | 3152402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dd9d2833-540e-32c8-9cc5-209fddf7536d | -17.71291 | -42.2263 | 2026-05-20 04:25:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c6d61ca3-992c-31e9-9218-4177344edb7b | -14.93058 | -47.75299 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9df8630d-362d-3c47-8188-8422419c89f7 | -14.85319 | -48.54313 | 2026-05-20 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 854251af-b01c-3e46-928d-3c24a22247ce | -14.15455 | -52.89613 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e2fb32a-2084-343a-a48c-ece656d701f3 | -14.16444 | -52.87068 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5481e633-cf0e-3835-b06a-12b8a14a3b10 | -14.96778 | -48.9336 | 2026-05-20 04:25:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a796318e-aa8c-35a1-9147-11ae07228496 | -14.91159 | -47.73713 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3691261b-44fe-3497-ac05-b76389c4b44e | -14.62826 | -48.65419 | 2026-05-20 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e0a46fd-5067-3a59-a3c0-9c1f9ff33b8e | -16.14923 | -51.72146 | 2026-05-20 04:25:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f1d8786-4bf9-30c5-9b50-0b17c3ec09a5 | -14.16922 | -52.87165 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74fe67df-721a-313d-bda7-ca360d0a3bae | -17.59375 | -46.56639 | 2026-05-20 04:25:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f308adcf-31df-3696-a8c7-12788bb473f2 | -16.45803 | -51.71476 | 2026-05-20 04:25:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22a49e53-948c-3038-a632-f0cc8cf2a296 | -17.80009 | -46.71487 | 2026-05-20 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59d0917b-5754-3496-8560-1c635924572a | -16.07143 | -45.89199 | 2026-05-20 04:25:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b26d2cdf-6704-3c09-9c7f-de117553097e | -14.14974 | -52.89526 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| da2eab5f-dca1-382f-9133-df30abac4eb6 | -16.45723 | -51.71902 | 2026-05-20 04:25:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a92c3b27-cdb6-3fc1-97d2-f0c3e8037df8 | -14.1528 | -52.87946 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ef98847-72c6-3498-9caa-b850547cb52b | -16.45298 | -51.71812 | 2026-05-20 04:25:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b51b7430-1ee2-3dd3-896d-a361b50e5dd7 | -17.80343 | -46.71546 | 2026-05-20 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ce38263-e0ea-34be-9c18-de455baa31e9 | -14.15558 | -52.89077 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af84d399-d506-3d67-aef9-90d5bee14888 | -14.91092 | -47.74115 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc01674c-1eff-3ed1-beb2-32b716671578 | -14.15759 | -52.8804 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca5746da-d468-37c0-bebb-d8c78e3e72d9 | -14.1655 | -52.8652 | 2026-05-20 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11ac783f-6185-38ca-bce2-a3292f404a67 | -17.80068 | -46.71121 | 2026-05-20 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c8adfbc-2a16-3a93-9cde-4b355cbbb03b | -5.30443 | -43.05765 | 2026-05-20 04:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed196954-3c37-37e7-8e75-b0a6d223e7de | -3.96019 | -43.12349 | 2026-05-20 04:40:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 888bac9d-7dfc-38fa-be6b-8d7b408a16e8 | -5.94846 | -43.49133 | 2026-05-20 04:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52754ee5-052b-304c-8ba6-e37751dfd402 | -5.72765 | -43.43684 | 2026-05-20 04:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5e9419de-5210-3c58-84cc-6d19d3e51d0a | -5.75381 | -43.40237 | 2026-05-20 04:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88131f29-008b-3579-a851-88c4d0819b19 | -5.72825 | -43.43288 | 2026-05-20 04:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 43429c35-8710-3915-9f22-56ace0180a5d | -3.95597 | -43.12286 | 2026-05-20 04:40:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dea155b-52d2-3329-86d3-cde7d5182c20 | -5.94905 | -43.48741 | 2026-05-20 04:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6b82552-9725-3ca3-ad77-32813887e843 | -5.95239 | -43.491 | 2026-05-20 04:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 10025646-e997-3bd2-9a4b-30c0f17efe42 | -5.95295 | -43.48711 | 2026-05-20 04:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c84c47a3-0fda-381a-a740-30a821176f8b | -5.94816 | -43.49033 | 2026-05-20 04:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README6.md)
