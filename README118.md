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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cea03a7a-1f8f-38e5-8a54-c2581498dc08 | -9.15436 | -49.96308 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ab0ca781-b440-305b-8ca0-df0205575fad | -8.76279 | -46.46137 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 2d451b3a-4beb-321e-942f-f7b1b602e108 | -11.2365 | -51.25335 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7f35a2f9-12cd-3ffd-9a64-6edb73261a0a | -11.15825 | -45.04407 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 878260c8-787e-3b39-ad0a-435a4cf0cd97 | -9.1902 | -51.55408 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c2ee15e1-f29f-3c17-9525-eccf9c9929ee | -12.09668 | -47.15622 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 124c1b5d-8da8-38e7-a264-3bad88e86181 | -8.86558 | -47.08348 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5c6fec94-e745-3179-90ee-839fc85d528c | -9.64507 | -48.26007 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2baf8d19-e254-358e-8bc1-14d2cba81a05 | -12.09502 | -45.00487 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 6e22dc87-1ba7-329c-af24-3985b67eed22 | -14.52388 | -52.29132 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d2d32e32-4282-36e8-89e8-66c37cdd6e97 | -10.17904 | -42.22317 | 2026-08-31 16:30:00 | NPP-375 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c6f9b730-ddc3-307a-916d-5c81428ab9d7 | -12.17444 | -50.53139 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4716d8d0-27b5-3643-999f-76afd2678c2c | -11.51511 | -46.94636 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1f778be1-160e-3d57-a9ab-41b2a2cc80eb | -11.20388 | -45.05633 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 6100c750-42b3-3a24-80dc-b19799c0a2de | -12.78906 | -46.46215 | 2026-08-31 16:30:00 | NPP-375 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8a2922c-2959-32d0-8e10-2287f28ee7a4 | -8.79113 | -39.85421 | 2026-08-31 16:30:00 | NPP-375 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7e6b7c73-c437-3d3d-bd29-03341ff5b4ab | -14.11385 | -42.1342 | 2026-08-31 16:30:00 | NPP-375 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 26eb049c-9b4f-37f3-9736-df0b3c828b7a | -10.12652 | -50.32248 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 556b56e0-9bdf-3fc8-8c4b-c337ef8a79d4 | -11.04222 | -49.67482 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7dc45664-0725-387e-84fc-c96b14d721f3 | -14.56491 | -53.5937 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 396cd19b-7f17-304c-bbad-3ed42cff77e8 | -10.33288 | -49.96046 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5e8ac11b-b945-38d4-852c-4c075aed1081 | -14.48171 | -49.03773 | 2026-08-31 16:30:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9d0fa3bd-d50e-3d48-be32-a44f31986d6b | -9.8325 | -46.35961 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| cbc6d106-7f2f-359a-bd7e-126bedceae68 | -11.49802 | -50.34809 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8e056067-4217-3bf9-81ef-417e4c938c9f | -8.86133 | -47.08807 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 269110b2-d703-3265-ab65-d56c8c92b5da | -8.60641 | -37.65318 | 2026-08-31 16:30:00 | NPP-375 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a52b958c-1b62-39a5-9155-f6f83228bf65 | -9.41966 | -45.68019 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 1a43418c-a6ab-3a2a-8ea8-c04fb2618eb6 | -11.33336 | -45.16038 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b3a002c0-9609-3b45-893b-a806e13c2816 | -8.86655 | -47.09059 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6f470c38-e84f-391e-a46f-dd713bb192c8 | -9.66506 | -50.86066 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 2a41a296-1833-300c-a151-55d6229ed64a | -11.49279 | -50.34875 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 856448bc-0f98-3af7-a981-dd993b7be0e7 | -14.96633 | -54.58982 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8266f4cd-9a93-3110-a30a-9baf857936fc | -12.89257 | -45.84276 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6318ee29-9393-3656-90b6-f24339573b83 | -13.19618 | -44.07237 | 2026-08-31 16:30:00 | NPP-375 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5149be1f-4184-3121-a52a-2ab6d4a50bc5 | -12.09002 | -47.14242 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 73ee4ec2-460d-3591-810a-1d51f079d0cc | -11.24221 | -51.2632 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 24c71644-0772-32c2-9466-05e09753b69f | -9.89673 | -46.62304 | 2026-08-31 16:30:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c8c6417f-99c2-3af9-b1d0-c7d09aa724cc | -11.92105 | -45.08273 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 77080ec8-889b-3858-9269-bd23df41ca68 | -13.94315 | -54.41534 | 2026-08-31 16:30:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 43ea57f5-5061-3a05-be24-93cb4aa13c30 | -14.47229 | -52.20608 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7ed74f78-561c-387a-9cb7-18610e9c3846 | -9.32286 | -48.25324 | 2026-08-31 16:30:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a2e7d079-124a-3605-8219-fd97619770eb | -10.57638 | -50.38544 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 1579fd22-7ac3-38c6-affe-1e510aa9b107 | -11.97931 | -38.21299 | 2026-08-31 16:30:00 | NPP-375 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 073e12b1-5710-3286-b8c2-095901cdcf41 | -15.26816 | -53.88514 | 2026-08-31 16:30:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| f74efd7a-0791-392e-8c31-ed3f81b593ce | -11.22738 | -45.14264 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9a557445-1a8b-3484-b961-87ccc6cc287b | -11.93077 | -45.06369 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e84bd105-eb7c-3cfa-a3b7-5c6988b0107d | -14.47842 | -52.20534 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| db39b2e5-82f7-3235-b334-f8bfb3fd1ddb | -13.46956 | -51.41121 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| efe714f2-df73-3dc9-957a-7ab27dcc99df | -9.42713 | -45.67918 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6c7e096c-3ec1-396e-9486-6eb16937aad7 | -10.96882 | -48.40834 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bce9a8db-2d42-3d31-b93b-2e8e28b1ef89 | -10.85075 | -45.33582 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| cb134647-2aac-37ed-83ea-7e1728e9579c | -10.57314 | -50.36063 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a215d600-dbe0-31ad-9594-b0f29e556ccd | -11.63619 | -46.75453 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16f3cb44-8cd0-3f63-b430-daadd711221f | -11.23418 | -45.13722 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| ddb1d324-f4c4-3447-9b6f-157f6bbc8fa8 | -11.51767 | -46.93424 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b7439588-d314-3f2a-b1bb-b406f2730cfe | -15.40573 | -52.71172 | 2026-08-31 16:30:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 136d41ce-d634-3888-90f0-790f1beaa1aa | -11.32102 | -45.18048 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 7720f850-0148-3cb6-a8da-34de9fcc66c4 | -11.16456 | -45.04405 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 92220c42-8e78-36e4-a5c6-eb98df1cb2f7 | -8.76457 | -46.44639 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 70f624f7-dfb0-3689-9bc8-0424745f4970 | -13.43041 | -51.69355 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 44a735e4-2085-359e-8420-6703fa39a48f | -11.17162 | -45.59429 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 03514a85-6581-37a7-89de-84426b864ebc | -10.68505 | -46.27909 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f5d69911-eb0c-308d-9f64-e78f6de82c6c | -9.68232 | -47.94325 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fc149042-159c-3ee3-8f46-6e80ad929c22 | -11.23912 | -45.1454 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ac2f041b-2955-3d49-924f-6ab697566d98 | -14.95787 | -54.57598 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bcbf0a75-dcba-349d-b6d3-2945f07aa270 | -14.95547 | -54.58437 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0c608727-d2a7-37f8-b30f-53f9d501c37f | -11.2024 | -50.62291 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c7c2df76-5649-3430-9253-b4e842751a68 | -11.19998 | -46.08363 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| d48ef618-1bb4-38a2-9967-a1e9ab9cce85 | -11.7888 | -47.67473 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9aa731d6-3def-3755-981f-b7f305ff4175 | -9.64624 | -46.05714 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1f58aa52-74d1-36c4-a51b-198cbd6c7f15 | -8.73961 | -46.46506 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0d966ed4-f0d0-39a1-b422-ccd039f8b080 | -8.7273 | -45.37747 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9c27cbd2-a4e3-35e3-8251-a2cbd213b2dc | -12.42153 | -42.88745 | 2026-08-31 16:30:00 | NPP-375 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 49584395-6dbb-3207-a2ac-0df05e67879b | -10.50759 | -45.04384 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a733cae0-a5be-37e2-a383-68f7c2ea9414 | -10.74807 | -54.03095 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 789a48c3-95b4-3348-8b03-57cb7cb7de5f | -11.54801 | -45.48959 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 39021815-ba17-32a0-a01e-3c09e3af20d2 | -9.65906 | -46.06487 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9133c239-5472-39c4-b9aa-702d11f5ea8e | -9.17268 | -40.4752 | 2026-08-31 16:30:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f6beed32-a990-3df8-a682-2f58c6305914 | -9.22464 | -48.58409 | 2026-08-31 16:30:00 | NPP-375 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 891f5ce8-1992-30b9-a4fc-a357b2fcca4f | -10.0839 | -46.62869 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4f1ba8db-8fb4-35e5-b531-4b4623414e5e | -14.96848 | -54.57096 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 75445252-1812-3130-a8ef-15cb0521229f | -11.20176 | -46.12426 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f950c9b1-b842-3b5e-9c8d-43aa65ba1cbd | -9.40808 | -51.685 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98580d42-4f4d-3cd7-9525-20fc271649e1 | -11.37374 | -45.20436 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d26a4f5d-9ef1-3ffe-8624-73611b558f6e | -13.41375 | -51.39085 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b68e7f52-100e-3677-b25b-b9025d0011cc | -8.75505 | -46.46249 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 307adb7c-414a-32de-b1c7-55d453266f86 | -10.76354 | -43.61412 | 2026-08-31 16:30:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 002ff67a-24f9-3ada-b599-15863f8c9a2d | -10.15469 | -45.76929 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9da8bb73-1dd8-3ec9-a117-e4358051a815 | -8.91607 | -44.16814 | 2026-08-31 16:30:00 | NPP-375 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| a7375f2f-e516-361a-aed9-ba992fdb9e73 | -8.3824 | -44.99528 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 36622843-756e-3668-9569-d9052103cd31 | -12.11322 | -45.02611 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 830d945c-7bc7-3eb1-8b73-7a71e0ec62d6 | -15.25201 | -53.86137 | 2026-08-31 16:30:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 94b709fd-55f3-3d4b-804d-57fae4076a04 | -10.32678 | -49.95332 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| fb7326fa-ebb0-398f-8882-17f9e96d8ad5 | -14.94833 | -54.58468 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bd1ec873-e8cb-3e4a-9a27-42d2ad903c2c | -11.32351 | -45.17116 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| d8eed176-5b9e-3ded-aa0f-38584448053e | -9.42272 | -45.64774 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 75da1978-9154-3add-8f80-dd24737aac04 | -11.91496 | -44.84175 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b200e10a-5ae9-3bb4-8fba-065f8d1b2f93 | -11.07627 | -47.15464 | 2026-08-31 16:30:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 89f4f887-6e3d-3894-bd1a-4e2c4040f482 | -11.24177 | -51.25957 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 67edca39-1cf5-3219-ac69-de9878a7acac | -11.21066 | -45.10442 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |


[Clique aqui para ver as próximas entradas](README119.md)
