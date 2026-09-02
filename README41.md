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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9977fa4-678a-3b6c-807a-8bc24f434465 | -8.45901 | -54.71497 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e590fd90-3f9e-3c1e-b67d-244a551b561b | -7.7632 | -61.19838 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27bfb200-67f5-3680-b9b1-636146f0a92c | -8.44164 | -54.70778 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42e568c0-b11e-33cd-8f02-2704c485863b | -7.53443 | -60.71913 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79cc88bd-2d86-3bbc-8e01-3da14759dcec | -11.31179 | -45.15283 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f561903c-122d-3cd1-9a31-e146f3c738a9 | -11.36111 | -45.40923 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc2a25e0-31b7-3964-ae9b-c09a42dc5ba5 | -11.67307 | -50.19859 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c1c4cc2-ea1c-35cc-98a1-0d31fc44aaa5 | -10.79108 | -44.7527 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bb949a9-8ec6-3c56-8591-9f2f4d40cf1d | -11.33179 | -50.6151 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec942aa2-3af9-3910-9909-55ccacba97c5 | -8.44887 | -54.70898 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cd0b801-556e-3e78-916b-13c5781113e5 | -8.92028 | -63.27736 | 2026-09-02 04:57:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a471ea2f-8d56-3d50-aa97-cfe14e8b084d | -8.55822 | -63.18585 | 2026-09-02 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 173e1aaf-bc99-3c33-a45b-e36c1e6a689b | -11.05832 | -51.52715 | 2026-09-02 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7964f1c7-6e48-3393-a208-7b3cf3bbb094 | -12.13182 | -47.09847 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60aafb0e-9133-3412-a5af-c3dca68ca9e8 | -13.41345 | -43.87923 | 2026-09-02 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c6beb257-c568-30ec-a48d-a486441055f5 | -8.12767 | -54.95622 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff95ad73-5ffa-3bfd-9ba7-fba0cd5ed276 | -12.12928 | -47.14705 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 07af6f94-2adf-3db7-81cc-bb57339196e6 | -8.45389 | -54.70121 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96432a5a-e894-3aa9-9525-dbf360124fee | -6.93537 | -59.64144 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07e9f93c-02a4-3e5b-b01d-c7258d544278 | -6.93979 | -56.45902 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7144900e-b133-33d1-85cb-00dcb2adf155 | -12.12924 | -47.05624 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 785ca3e6-22cb-3926-88d2-f973f2af8589 | -12.13902 | -47.13719 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f5d29445-0d6d-36e6-85dc-afe16c929dba | -11.31699 | -45.14921 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c54d087-a4e9-3ee0-9f75-c820657d6395 | -7.44228 | -61.41574 | 2026-09-02 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5280965-908c-3ede-8165-9d48e8b275cb | -13.71069 | -43.87811 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2b9c625-a091-3fdd-a743-010507793dc2 | -8.43152 | -54.70171 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 23431705-6d28-3e01-b0bd-dae46078f47e | -11.762 | -50.55355 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9ec3a4f-0cf1-3c65-83df-7fce8e193a13 | -9.72637 | -47.77092 | 2026-09-02 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57fae219-f95c-3304-9de1-f8a7e1e8c7fd | -8.90865 | -50.57011 | 2026-09-02 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f59364f5-d3d5-38bc-b8b3-a66041825bfc | -12.63628 | -45.07397 | 2026-09-02 04:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 56e4ea35-9c20-3ea7-8d88-b710a80fd757 | -11.82589 | -46.06023 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f44864c-1af0-3d43-aaee-a46086c3a790 | -6.31723 | -54.75075 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a02b84a0-0712-3304-a0a1-e5788e4aefa9 | -11.30592 | -45.16153 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16b14f80-ce8e-368c-b4b9-51cd6b3ee6df | -10.78497 | -44.76212 | 2026-09-02 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 3e0e7e5f-c2c5-321b-b727-ceaeee36eeb4 | -12.34493 | -45.66112 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a4b7b72-a435-3527-8679-beab6c1924d9 | -8.45178 | -54.71375 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25494c58-87da-30b6-ab7f-17dd40f1d5e0 | -7.66097 | -45.87502 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f613d12e-ead0-3ec3-8eb2-e9a5ca286580 | -10.33859 | -49.95887 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d0c2ff2-8b4a-3b47-9492-019e5729a6ef | -11.33803 | -50.61987 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34bec4a2-1037-392f-96ed-02b86b9a3df3 | -9.39624 | -51.69013 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9b10542-1a5f-372d-b705-b921ac9af434 | -6.05314 | -53.83468 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5844a7f3-e4c8-3fec-95cd-1686ab597813 | -10.97083 | -50.48255 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7782aa85-bb1a-31c5-b286-a62b37659308 | -7.65206 | -45.87767 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e3c25e40-d6bc-31d0-bb82-945911933f06 | -11.35281 | -50.59183 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1689499-86e4-3ebc-ac80-e6127dd09b36 | -10.78255 | -50.48067 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc7e3aa0-ab6a-312d-932f-32a869713d0a | -7.20069 | -60.68651 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed4b6ec0-4482-3b33-8d3b-f04973e01eac | -6.68923 | -58.76314 | 2026-09-02 04:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8ef9a92e-3f46-31fa-9c43-97828deb0c69 | -7.21346 | -60.67775 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b9c8ea4-9812-3f22-916e-67c339eda824 | -8.46705 | -54.73352 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2996ef9c-129e-3ccf-9487-7fd050db2875 | -8.43803 | -54.70716 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da77f6a6-d97f-3017-9d58-a81a65ce8d48 | -12.11048 | -47.28226 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1ece8c6-5e7f-32b4-93b4-54b76c9f38d0 | -9.44381 | -51.56165 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45ca86fd-85d8-31ed-84dd-4270d4610a75 | -10.76234 | -54.00199 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac8a7898-883d-30f6-b680-f00d664d55d2 | -9.46172 | -56.74483 | 2026-09-02 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6788f402-fe33-3d9b-b18f-7eec6821aa66 | -9.95147 | -53.99052 | 2026-09-02 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c37a3e8b-5fe6-3178-9ee3-b5138acd3b17 | -10.48609 | -64.32969 | 2026-09-02 04:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5e0a1c5-5542-3056-8f16-62b2e64f662c | -7.20672 | -60.68409 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e36309bc-f40e-35c5-8e0f-e68281091fea | -8.47988 | -54.70121 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 12cadfa4-8aaa-301f-8249-47d33ab8a5c4 | -8.71619 | -52.36707 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64d75542-7372-3c0a-8c88-07d20644f4b6 | -8.42703 | -46.89935 | 2026-09-02 04:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec1785d4-48ac-38e1-ba10-b9cd5f8f2904 | -11.32725 | -50.59921 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bc6d576-4da3-3166-9c6e-e3f7678e2ded | -8.50034 | -50.30083 | 2026-09-02 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 51d0ff09-9983-3417-8d77-5323394f03f3 | -9.39845 | -51.67616 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 258c74b5-bff0-368c-b752-943d9c12cdbb | -5.82899 | -57.63741 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcf169e4-64a8-36b3-a25d-204fc7e33a7a | -9.93987 | -53.99642 | 2026-09-02 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 429790ca-10ed-3262-b837-f0a61cf9bf6b | -6.04959 | -53.83401 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5f956d4-dc7f-3760-9203-c27f0462c6a1 | -8.71677 | -52.36348 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 211897bb-f16a-3aa8-a821-dd610ec29e7c | -12.15243 | -47.07104 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd76e462-77cb-39d1-813c-5a6e587357fe | -6.20162 | -55.42442 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 959a33c2-2618-3dfe-9ee3-ef711d82b899 | -6.14395 | -55.67325 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8186aaeb-9d76-31af-b301-b2b8e61cf6e5 | -10.40077 | -50.00659 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8853fab6-9b9a-3d3f-9ffc-a447f249b34f | -8.2499 | -49.5055 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fef1545-e602-33fc-b80e-a9bc0e6bd634 | -7.28974 | -49.82632 | 2026-09-02 04:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34662159-c0c1-3f1e-8bef-bf8f0b9b9d30 | -9.00137 | -50.78163 | 2026-09-02 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4ea4482-2fae-3ee1-bd65-0bba0db36018 | -12.1344 | -47.14029 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8497c71-e2f9-36f5-8f3d-05ffb0a2c2fb | -6.81038 | -59.09674 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd0014f1-36b2-352d-b34d-76f188e406f1 | -8.47708 | -54.71803 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| c532f8cd-58d8-3cfb-9dd1-b72fb50bad14 | -6.85917 | -59.48315 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 54c5022f-6a04-3743-b957-e409091454d6 | -6.59569 | -59.11598 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77f8562d-93d9-3394-be8c-88baa80ba917 | -6.94365 | -56.45546 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 007dfe9e-0bc7-302c-adad-d493cef3f474 | -8.28738 | -54.91371 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79a4d94a-28dc-3e45-94bb-2d8a137b8578 | -10.87622 | -50.46403 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36b2e4c4-66b9-33dd-b7f9-d4f81552dcd9 | -10.90613 | -45.33529 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 65deb1c4-dbfa-35e3-a9e6-807fd5b97912 | -6.43256 | -53.56449 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 705f5aba-a67d-36db-a3b0-ba4ba36ba78d | -11.52453 | -46.91093 | 2026-09-02 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49d801eb-b5ef-326d-a7df-6d0f429a7232 | -11.83641 | -46.04844 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc9f6833-3651-3cfa-80c9-c54842a00800 | -12.11327 | -47.05001 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5153c625-414b-38c9-be13-d7cbcbaae0be | -10.79179 | -44.7475 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2beae84a-cefd-317e-aa57-e7ae5fc0776f | -11.67365 | -50.19475 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f03b7c4-05b8-391a-a7a4-791c208672e5 | -6.64344 | -59.43345 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a669a9fc-b98c-3b94-a801-c83911283a31 | -10.37602 | -49.98331 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ada95288-1cd3-3c8e-9c5d-f2eadba3473f | -8.46041 | -54.7066 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 3509e4b7-5105-3943-ab65-721ffd7ff23b | -8.11871 | -51.66039 | 2026-09-02 04:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76457578-213b-3a06-b1ee-86928355992b | -5.58509 | -60.20266 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d10bb356-3eb8-3d97-bfe3-281860b15b59 | -9.69402 | -47.20626 | 2026-09-02 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea131511-9082-34dc-bad3-039913f635e8 | -7.72602 | -60.97194 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 656e1acd-dcad-3a77-84d6-882c2117a35e | -7.65789 | -45.86668 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40779e21-3137-3fc0-8198-9ef26aa7d4e6 | -9.86886 | -64.97984 | 2026-09-02 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6047bf4f-2a93-3ac2-b601-fa6e4ab9e75e | -12.17665 | -47.07824 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97485c3d-2990-3aa1-aedc-6e558e696dd0 | -6.76634 | -59.43489 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README42.md)
