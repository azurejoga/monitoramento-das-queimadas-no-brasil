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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29006e12-0638-3f93-bb09-de86e7a0ac35 | -10.79459 | -46.42261 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a58ec96c-aaf7-3fcc-8cde-085bdc836a56 | -8.21497 | -49.56252 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 529494b4-8f9d-36ad-89b0-644e46900a3d | -9.19329 | -59.47129 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 655f8e15-76bb-32f0-86c8-4e183c4b511d | -8.12494 | -47.12759 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 75980cc9-d99c-35fc-b631-d9140775b019 | -9.23546 | -60.92402 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 00095216-6e11-3358-b39b-59b472e81c14 | -8.8777 | -62.45181 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 12e40965-5745-3667-8056-00ebd18debec | -9.84113 | -45.96398 | 2025-08-25 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 019df249-4a3d-3857-9822-5b0e8fcc63e1 | -8.22696 | -61.42719 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 91208ded-f626-343d-aeaa-6a5c9ad274ec | -10.61716 | -55.04748 | 2025-08-25 04:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 634b23c4-d801-391c-a40b-97c9faa7207f | -13.40142 | -51.80021 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78445053-8693-3293-b548-680cbf763c1a | -11.46471 | -55.47242 | 2025-08-25 04:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bae76124-08ab-355d-b364-35b7495428ee | -8.21668 | -61.37941 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a7a7df74-928f-3b72-8652-54dea13a2df4 | -8.07922 | -61.53697 | 2025-08-25 04:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1539de5f-5053-3519-b419-e7783aa971e4 | -9.19932 | -60.79002 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 786b8487-3dc6-356c-8918-f642cc00e69f | -9.19425 | -59.47144 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11b22e6d-2696-3440-8642-95eb4a50bf1a | -9.24685 | -59.64389 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9391c566-13a0-3b87-8c3a-e889343ea6b0 | -8.05782 | -49.68362 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f19e279c-b012-3783-bd71-8e755e1d3815 | -11.05088 | -49.11906 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 918e4067-df6f-3117-93da-8527873800e3 | -8.62238 | -62.63001 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50efb422-a76f-3294-8f4b-559c619dfcdc | -8.21483 | -61.38905 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4ee24fe3-6579-3f44-9561-9c6f17918651 | -8.11983 | -62.86948 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 36fd0001-6deb-3a9a-860a-7b49bb640427 | -9.19767 | -59.48309 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0742588-7dd0-3662-b972-3f42eef93b82 | -6.6289 | -58.54556 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 198200b8-77d8-375f-b34d-74a96fab094d | -11.7 | -60.18149 | 2025-08-25 04:42:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ec40ae6-1359-3b57-b283-ddbea3559bc9 | -11.60107 | -46.3737 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad7425ae-85da-3608-af55-23996b71a7e5 | -14.25559 | -48.0431 | 2025-08-25 04:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbe5bb2e-6d3c-3717-9a62-f4e64a9df6ea | -8.68682 | -62.87339 | 2025-08-25 04:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d3c16c8-91f8-3a49-b23f-39f7acc8a30c | -9.61109 | -55.35099 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdc42507-83ee-3564-abe3-6b69a37bcd62 | -9.20014 | -60.78576 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 557fa1f3-49e9-3257-91e2-589669b295f1 | -11.17432 | -55.02596 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d218865d-93fa-3495-8e1f-935e299fafb0 | -9.05925 | -60.62231 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93a91fbb-e616-3dd7-821d-2338c9c30cdc | -8.21884 | -49.55957 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31ee2e0f-2eb0-3153-ab53-760a1a087d41 | -13.65927 | -47.98067 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37b4bc12-5710-33a9-a70f-d15c408df9fd | -8.89739 | -62.45577 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4a40cfb-3840-35d2-a8da-eb60a28371e5 | -8.54363 | -48.86607 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bb51146-77c9-30c2-9959-c6d6ab23c297 | -7.91987 | -63.06145 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f22bc596-082c-34b7-8c10-9b26c3e56659 | -10.02794 | -51.07723 | 2025-08-25 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bc06733-aad6-37ae-aa55-39ee21b4d2ac | -12.75179 | -48.13816 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4294dfa6-f871-3842-9e9c-ac7b21503fd8 | -11.60255 | -46.33553 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3ed074f-1eef-3c85-a352-eb3d965e3a54 | -7.52132 | -63.81875 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c31fb566-87bb-3cb7-971c-15d6fc68225f | -10.81211 | -46.38202 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a483ff6-816f-3944-b5d3-dc1bae5c5367 | -9.17291 | -60.81522 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2fdc07f-c1b4-3ba1-ab6b-bc03114edfea | -9.22025 | -60.93924 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed3f3b45-a4df-33a8-9444-ff91bc4c2ecf | -9.19649 | -59.45372 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c07122a6-b8ff-3365-b5ee-22544b956162 | -7.54326 | -63.86176 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e91081b9-c599-38ae-81b1-f2419379b14c | -8.24627 | -61.46207 | 2025-08-25 04:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a2a87a3-6bc8-352e-bc45-54a90835476b | -14.25592 | -48.04553 | 2025-08-25 04:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51b6d26f-48c2-3027-b0c8-3b3605f4d009 | -8.05615 | -49.67264 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d496c1a-651a-3fa4-b66f-7a366e120b93 | -9.19491 | -59.46795 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7bdf15c-c600-3244-baf6-84bf0f691647 | -8.54583 | -48.85188 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f78fa829-4d5d-3967-ad9c-9167deaaecae | -11.10704 | -44.78596 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 711912c6-a076-3b64-9171-d24f70cce98b | -10.02517 | -51.07312 | 2025-08-25 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 293889df-3416-32f3-a777-cfd9b9f7caba | -6.69161 | -58.85935 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0d78352-618e-3b71-abc2-378fe44d8965 | -7.5298 | -63.81895 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 018bd84b-7287-3901-89c7-46091d7e6da4 | -11.28076 | -44.98981 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 749775f5-648c-3604-a994-47e9acb91aac | -8.28789 | -47.2396 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89fd7127-da8e-3249-9f1b-ced2bac9b42a | -8.065 | -49.65609 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92b48648-c6b6-33a0-bf9a-bc88f2cef157 | -9.17142 | -60.7758 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f5e6873-805e-338f-bca7-f13617741504 | -6.83427 | -58.94804 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71319e7a-6187-31b8-a053-751d6a8b48ea | -9.16989 | -60.81551 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 597631d5-6249-3f9c-902a-2c77ba1ec06a | -10.88789 | -55.79035 | 2025-08-25 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b297f50a-6449-3f83-9a12-8e0a46e0c99b | -13.62684 | -48.15356 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d39f191-c2cc-37ce-9c99-c5323501d1ea | -12.74587 | -48.10447 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ac6716f-44aa-3aa6-b80f-fbe6e4dd4d24 | -10.72555 | -47.11654 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 420e4ff6-1c62-3cbb-83bd-749b39647002 | -9.74231 | -47.93319 | 2025-08-25 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5866df25-0b25-3968-a8d5-815e1e306d08 | -10.60292 | -44.3333 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 27efad8f-8102-3464-b150-02c03068ad4a | -11.27554 | -44.96629 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d055be17-d276-3b09-be3d-5bd20cf2173e | -11.60441 | -46.35006 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bdc25c7a-89d8-348f-a15b-c3be611911b6 | -13.6221 | -48.16114 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49672715-3df7-3b4e-9475-3c06bd3241f6 | -6.81539 | -58.95921 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ba1f3839-da1d-3367-843d-53dc75367f7c | -8.62615 | -62.62978 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d63b7a7-da17-33fb-8814-536e7c3ffb96 | -10.79082 | -46.42205 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d318bd2e-fe53-3285-a713-3bbec991d8e3 | -12.49057 | -53.82529 | 2025-08-25 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4cdb9ed-fda3-379c-874b-2e6f1f3823e3 | -9.20096 | -60.78144 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2d1f67b-e608-3e3d-9250-304867082a81 | -13.45541 | -46.90455 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b6169fd-757e-3f02-b8f1-ebf4cd79f96a | -8.06725 | -49.68501 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e96585c5-411a-3102-ab17-8a18f3c3d07d | -8.22789 | -61.4223 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a98514b-7b25-35bb-9866-543b1e21cbfe | -9.15199 | -59.48172 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b052cff-8f5c-3bf6-8255-591f0c3c1d1b | -9.6948 | -48.34205 | 2025-08-25 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7182ad60-6902-389d-b800-280442cefd0c | -9.22248 | -59.71412 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02289b82-5205-31d8-bbcb-81ad6502e2b1 | -8.87437 | -62.46881 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 79339582-ce08-3716-8db3-7be35a2bfc4a | -9.12695 | -60.7336 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 495e4b2a-d189-3577-aee1-6e5e0cd77958 | -10.46066 | -59.12972 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2badaf4e-f6dc-3d01-b0c9-25a46cbe7387 | -8.22203 | -61.38518 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 59a8bfd2-3953-3656-9b1c-50e8c4056720 | -7.90481 | -63.06514 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 5086617f-b9d4-3c55-b882-ab42c14e8fe1 | -10.10234 | -57.76576 | 2025-08-25 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a328e08e-bd1d-31c5-b441-9a07bfc34272 | -11.4573 | -55.46751 | 2025-08-25 04:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bbfacf62-e59e-39ff-ab6e-b240757c4024 | -9.1926 | -60.79312 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ca1cbfb0-f563-3a5e-afa6-4353af026e5d | -13.48914 | -46.88489 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 774834a8-3bb0-370b-b683-889ce8ad906a | -8.58793 | -62.62916 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c67cae08-80ca-3c7d-b7f5-1a025211371f | -12.75121 | -48.14217 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b4e560a-a9ea-32f1-a4f1-dccf4fe98e0c | -8.21048 | -61.39161 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e546d87c-fa33-39fe-b3cf-5752cc95bd67 | -12.75054 | -48.12206 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34b16cb9-70a5-3186-b055-1a3438eee80f | -8.21942 | -61.37809 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7c228eb6-5594-3a6e-84a1-89438f9f26e5 | -10.5371 | -57.96772 | 2025-08-25 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98d1c119-c42b-3fd7-8763-4ba622e18702 | -12.74412 | -48.14129 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49929965-da92-360d-a837-a4d2bed32f71 | -7.52256 | -63.81749 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ff54183-61b2-33b3-9799-b6581920452e | -10.23894 | -59.66221 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 80ba4bf0-e799-3cee-80ac-9c1ef3453a30 | -11.26519 | -44.97998 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b7356ad-358e-34c8-8d51-2f963ec87d11 | -9.46945 | -57.82326 | 2025-08-25 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README43.md)
