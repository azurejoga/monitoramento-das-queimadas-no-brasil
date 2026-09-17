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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09ea1a70-ca57-310d-b4fb-22a41c82138d | -9.59958 | -45.34402 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a1fd98b-ff3c-32ee-a1c3-4df52b5d54dd | -10.46104 | -44.94809 | 2026-09-17 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e6b43bd-4600-3c86-9e68-3c33f778ade7 | -10.78125 | -46.20216 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 01e475a0-2329-3b6e-8ab4-52c07e239869 | -9.58723 | -45.27569 | 2026-09-17 03:55:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8fead76c-b74f-3673-916d-c9992a9f5280 | -11.88965 | -47.58432 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ea6346c3-0122-3e0e-88fe-25b45c996a55 | -9.60671 | -45.33199 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b673017-4f3a-37ed-83f4-92a47ba8478e | -9.11764 | -45.73602 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2aeb0626-6c43-3164-a76b-4b34fabcd45a | -12.52119 | -45.96825 | 2026-09-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39a444d2-3f5a-3f02-91c5-ab59c376a614 | -12.19829 | -43.48065 | 2026-09-17 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74fa4601-3f24-3ca8-8781-d5d6604e5da6 | -10.11907 | -45.57368 | 2026-09-17 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9d08ceb9-61fd-3604-9ea1-b61822c2fa49 | -9.88935 | -48.3926 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39b96ead-28ec-3c06-84e5-c66edb45b342 | -9.55709 | -45.41622 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 506562b5-92f3-352d-98ad-bd81a9290604 | -9.83067 | -48.3554 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50b1f23d-ad12-312f-b10d-5bcc666ed7de | -7.48885 | -42.12691 | 2026-09-17 03:55:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e0ebe4ca-58f9-32af-a953-78bbd7bb7185 | -9.85215 | -46.91578 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3eec5566-1a05-3701-8db1-4fc01863ff4a | -12.46217 | -50.78426 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 70d6500c-9fe7-31ce-b08f-de86a0ff8e01 | -12.48923 | -50.84723 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| f58b17c2-c7f7-3ca9-a51d-f3f22ffbe63c | -8.47603 | -44.55339 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3e3eb98-aa8b-3cad-83de-a40b92b40d21 | -11.58717 | -46.88994 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 778d5d5f-0ba9-3354-80c7-bf476afadaa9 | -12.46999 | -50.84295 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| c9b3f8d0-5c56-3f84-8ad4-37c1fa2568ec | -12.46771 | -50.85388 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| b83f0723-f89b-3583-9968-59535e6b3fad | -10.82738 | -46.14663 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a56108b-1e40-3ef9-aa6a-ec22ab771ea8 | -12.45304 | -50.82775 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 9043ac6f-2ea2-30f8-af05-af83dbede813 | -10.61477 | -46.09693 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16dc4f0a-d677-36c2-bdd2-d1e33a23ca97 | -11.20511 | -42.82399 | 2026-09-17 03:55:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 03b482ca-9413-3be6-a65d-33cc805952b5 | -11.53632 | -46.87871 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04b3c5e1-f216-313c-a7f6-80940e2c5dfc | -7.44664 | -45.2928 | 2026-09-17 03:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 52a03e90-dccd-3268-99a5-bd39c4f20fca | -12.98958 | -44.83841 | 2026-09-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14ee8bd8-ee24-3a5b-a9d6-0b32002b31d8 | -10.55272 | -43.67298 | 2026-09-17 03:55:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7226d0f0-3365-36f2-838c-bfe5a1ea3b0d | -7.03046 | -42.07388 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3fe211ed-133a-3c8b-9e12-87b8870fef8a | -11.22051 | -43.45451 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae089f64-51ac-3f40-931e-5371866fea13 | -11.20905 | -42.82468 | 2026-09-17 03:55:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bafcb497-0a5c-3a3d-bc97-646fdfc9a36d | -9.87719 | -48.39502 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7654247c-abc9-3d38-8fe8-53c24398fa45 | -6.65547 | -43.64008 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd571ae9-60b3-39a0-9208-7a84dd8e8b48 | -7.3045 | -42.35035 | 2026-09-17 03:55:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8eca8ae1-dfde-3488-af00-c7efb31b6e2f | -9.90462 | -46.51178 | 2026-09-17 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ebc4a20-c775-342e-af00-ee5f6d1c7359 | -11.89212 | -47.58839 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f0042e3c-a7a6-391d-b4c0-fe70eeea093c | -9.62147 | -45.3592 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9ced8ce3-ac3f-38f4-a52b-d5e6f9d674c6 | -12.48768 | -50.88706 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb2d94bf-40ed-387d-8ff1-0859b38588a1 | -12.44109 | -50.91726 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29fcfdb7-fc44-3d19-ae3b-06941cacb768 | -12.44363 | -50.87162 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b54e0d57-af69-3056-83b2-8eefbd6f7e7b | -8.46772 | -44.5466 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c23dc942-f1ef-3a64-bb33-7c63d138fdef | -11.31633 | -46.78459 | 2026-09-17 03:55:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 060adbef-7fc7-383c-93e3-1e303d17891a | -10.5083 | -46.28279 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84c9eb70-a4ab-3ed0-b45f-ce6a88bf85ac | -12.47783 | -50.90212 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| accac4e1-fb7e-33b6-9cdb-87e027d0f4c8 | -7.12819 | -42.15537 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| da35253e-6c8b-3de5-81d9-c3ad4a21bfc6 | -12.4496 | -50.84413 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c58fccc8-8338-3924-8a07-a106c4576fab | -9.60631 | -45.33433 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef12b6bc-261a-3bf3-a763-ae65366ec33f | -6.87976 | -45.47173 | 2026-09-17 03:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 291e5103-244a-3785-9617-a45b2e9cd584 | -10.30908 | -45.31794 | 2026-09-17 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac7b0a49-3dbd-3a8c-acca-feb5f7b49ecd | -11.89409 | -43.82887 | 2026-09-17 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47225fa2-a545-35c5-8cf0-bc67fad538e9 | -9.58695 | -46.65115 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 453b2cfd-af18-38f5-a1f9-2222cde9ee4b | -9.09883 | -45.7269 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e94773f3-79b0-3a9b-bd27-458ef1cbd88d | -6.11811 | -47.17604 | 2026-09-17 03:55:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d92bbbce-fd15-3050-8c29-c39bb4934e78 | -13.43128 | -43.8164 | 2026-09-17 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e7576d79-e4d3-3986-a609-e3406d34b759 | -7.12702 | -42.16248 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1bbfbda6-4110-3289-a364-7d9c3c33b37e | -9.04442 | -45.09108 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3228e23e-dcd5-3535-8437-d5ca80b22b24 | -7.84802 | -44.81571 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5aebefc6-03b5-3b32-b80f-c32063e0fff7 | -8.13575 | -44.85627 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfa73137-8aa6-3150-bf14-c3f253a779b6 | -12.50129 | -50.82138 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e0053a6-20d3-3356-8244-d30553f6490c | -9.96253 | -45.32656 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 4c222c27-8efd-3b29-b575-039a8b33d6cd | -9.36141 | -36.95001 | 2026-09-17 03:55:00 | NOAA-20 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9d2addd0-5d53-3664-a98d-59d2939a8b93 | -12.51835 | -50.70676 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea606d16-a5c9-347e-83dd-e9096e6330ff | -7.17164 | -42.10096 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0f2eca8d-771d-3952-85de-48b11c9a5ed7 | -8.77805 | -45.87763 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d8af9d5-a2d7-382f-9d20-98b84156f2fe | -12.45894 | -50.82919 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f2b6651e-91a9-37d1-be85-e7e70541366b | -6.95491 | -42.58397 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a018121f-a3ee-3f42-b979-4f259cccc65a | -12.47298 | -50.86079 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| d25505da-2721-3b28-bcc0-137462bdc5ed | -8.78607 | -46.90214 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| db73ad08-b8bc-3a4b-b1f8-7e8284cace33 | -12.47682 | -50.81025 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 047ea2ce-5b30-3206-b508-4b8c819af40a | -8.2673 | -42.16525 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c55c93a1-abc6-3cc6-b627-72220cb47048 | -8.56466 | -44.48111 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9236a98-791e-31f0-9757-398374c3468c | -7.0243 | -44.63064 | 2026-09-17 03:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93fe260c-cea4-3ceb-b8e7-3557b3c6149e | -12.46174 | -50.81828 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 2bcb9bd1-df51-3dfd-9362-4fd0b4f81299 | -7.96286 | -44.83087 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65b99841-7a13-38a9-8601-209a770b4a8e | -7.64344 | -44.33202 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a7fbb6d-667b-30f2-9d7f-d0016a13319d | -10.54357 | -44.85648 | 2026-09-17 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e1223dc3-b05e-386c-87f1-1403d8fadac8 | -12.3733 | -48.46533 | 2026-09-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5bcd0f1-8d66-3a73-95d3-38c8247251d8 | -7.6443 | -44.32711 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5063ca6-1520-3329-9879-d4e44f1d86d1 | -7.09061 | -41.84255 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d3153ea0-4854-3f30-9833-2618abe70b77 | -12.47184 | -50.86627 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9eb7ef3d-4ef4-3a9d-bc6a-7c17183faabb | -9.60387 | -45.348 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 794c44b2-4dad-3e50-bb96-38f79f3367db | -11.64352 | -47.3379 | 2026-09-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0a33ac8-21de-381c-9156-83b7cb04f879 | -9.62049 | -45.36452 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 8c1350ad-9240-3d6a-a0f9-651abc8b52fb | -7.38493 | -44.51328 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 413a95c8-e8fa-387e-8d68-cc38f8ab1a3b | -12.4979 | -50.83774 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 867dfd14-3040-3828-a247-8d8ebb13c047 | -10.3913 | -46.63254 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7cd784c-d27e-3bfc-9e6d-1704011516bc | -8.39264 | -42.21019 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3324928b-23e6-38af-9e67-a360374b34e9 | -9.4875 | -45.42248 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8680039a-86f6-3272-bf4e-bccefac02f4a | -10.80728 | -46.17242 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2c81908-bbad-3eb8-a600-f7f80756ba43 | -7.17564 | -42.10167 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2bea964b-5918-3058-a819-01f77c98da23 | -12.46656 | -50.85936 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 02b43096-87c7-3289-abf1-c0c6a16c17ad | -7.12584 | -42.16961 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 27d6d078-50e8-3a5a-af70-41140129f080 | -10.76527 | -46.20535 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0020096-5d5e-3ef2-bdaf-8d61e3e9fb7a | -12.45918 | -50.79503 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 9b398263-f01c-3d8f-97c1-0bdcb7ad8418 | -8.60887 | -44.49566 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f1e7db2-fe61-34fc-82b3-3d327a385fe6 | -14.76713 | -40.9338 | 2026-09-17 03:55:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 59aec01c-ecda-35c7-999c-71f3644bd7d3 | -11.88575 | -47.60489 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c234485-24b5-32cf-8b6e-aac558c89628 | -12.46557 | -50.79647 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 6eb8d173-0d89-3aed-a96d-1ed72dae6c49 | -9.56115 | -46.58601 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README26.md)
