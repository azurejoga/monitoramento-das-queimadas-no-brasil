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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62ecd751-6300-3159-b9ba-3861561d6a4f | -2.5915 | -46.87256 | 2025-01-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9eba74c8-9b53-39ee-bad6-7ba9d40ed168 | -2.1413 | -53.64996 | 2025-01-23 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a72150b-8b93-383f-b73b-03280cb9d702 | -6.0759 | -35.26337 | 2025-01-23 04:25:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d52c6085-821f-31be-8aa9-53bfb1803ed9 | -6.65822 | -47.60247 | 2025-01-23 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daccdeee-8633-37e9-870e-c45b6a270934 | -3.40974 | -47.14329 | 2025-01-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 526a74e4-68f1-374b-9d1b-f54ed7299201 | -5.00758 | -56.17599 | 2025-01-23 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e619851-674f-3e0a-9885-731bfe89c248 | -2.87733 | -48.24213 | 2025-01-23 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ea5b894-dc7a-3b9d-81e7-6ed04df322ef | -7.4167 | -35.0568 | 2025-01-23 04:25:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9af13615-047a-3903-96f6-ae57166c0da1 | -3.13379 | -40.04633 | 2025-01-23 04:25:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0a6bdf9a-ecbe-3179-af8f-5021081e75ed | -7.41732 | -35.05202 | 2025-01-23 04:25:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 401d14c9-5b30-3090-bb5a-99dc11069602 | -9.76139 | -36.98148 | 2025-01-23 04:25:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b1bdab64-08d8-307f-af63-af8f42b4cfd4 | -6.66436 | -47.60709 | 2025-01-23 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10c4c335-5a8d-3fb9-98d4-5c810ca8980f | -6.04073 | -46.25343 | 2025-01-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb65846b-a6fd-3ba9-8a1c-98571d6cc800 | -6.63366 | -47.35148 | 2025-01-23 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28bf927e-63a5-3e19-bb02-22b485b3b884 | -5.36099 | -45.17731 | 2025-01-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a84cca1d-fac4-3d60-8d52-f2ce934f00df | -5.5275 | -45.04594 | 2025-01-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98202fac-ed80-3411-bf92-5bed3efddbb7 | -3.08285 | -47.79089 | 2025-01-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8445cc8e-f764-3bfa-9ea9-18dca3dea74a | -2.14639 | -53.65058 | 2025-01-23 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4308d539-29bc-3f66-bb5b-ba2026190776 | -7.96153 | -35.24313 | 2025-01-23 04:25:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5187397a-e26d-3cb1-a80c-7019418d9c75 | -3.41311 | -47.14381 | 2025-01-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94f18368-08db-3be3-8861-9d8116cb392c | -6.51766 | -47.61343 | 2025-01-23 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e0e9662-7212-39df-9750-e90fe21ebc04 | -9.75608 | -36.97827 | 2025-01-23 04:25:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f03f6345-38b0-3150-9ad5-b6b55fc8deb3 | -5.45404 | -44.81482 | 2025-01-23 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e2ad596-224b-31fb-92c2-5eb13fa7474d | -7.96216 | -35.23831 | 2025-01-23 04:25:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3d137149-1f58-3d71-8052-1c9635c718b0 | -3.41254 | -47.14743 | 2025-01-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f485f34d-a734-33d2-b808-dbb4b8ea16c4 | -6.03743 | -46.25291 | 2025-01-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfedf95f-e7ce-3dfb-a25e-1503dab7073b | -9.76183 | -36.97799 | 2025-01-23 04:25:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 94b6ffe1-7ec5-379b-8fa1-095feff56c27 | -3.13738 | -40.05072 | 2025-01-23 04:25:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ee833df6-22c0-3f5a-ae59-7b847e790b12 | -5.52418 | -45.04542 | 2025-01-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02109fc7-4e1d-30eb-8aa9-111bc978f1da | -5.4953 | -45.38706 | 2025-01-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 089a2313-367b-3719-affd-0d0199999a1a | -10.53862 | -42.43215 | 2025-01-23 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ba3689c1-35a9-3182-96ef-276da7d553b2 | -16.05055 | -39.14683 | 2025-01-23 04:27:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f885d0cc-ef09-3899-a5fb-8564d4ac03f8 | -12.85543 | -42.36202 | 2025-01-23 04:27:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd16ce15-a719-3ddc-b3d9-8d719da7d36b | -11.03133 | -45.0577 | 2025-01-23 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 701e53f0-ced1-39e1-8793-3981eacb8838 | -11.45517 | -39.27378 | 2025-01-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7174708b-db8d-37c8-be24-2bb725031573 | -16.95103 | -40.05564 | 2025-01-23 04:27:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dec35358-219c-340d-9a0a-3337333372ae | -11.02443 | -45.05667 | 2025-01-23 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ee858ee-e59b-360b-bff1-3dfadfa7dad8 | -13.03829 | -40.33661 | 2025-01-23 04:27:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 66324ed8-312c-31a9-b5ed-9e32342b484c | -12.08078 | -38.0182 | 2025-01-23 04:27:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e47fa2e3-add0-3e89-87c7-7c09d9724192 | -11.02846 | -45.05334 | 2025-01-23 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85388ec9-60b6-3b96-978c-c07463278fba | -10.53469 | -42.43155 | 2025-01-23 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ae66f7b6-08c5-3a6b-a6b0-67c2598f932e | -16.04953 | -39.14872 | 2025-01-23 04:27:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7d8c57b9-3048-3e31-b39e-0016e8d7e07c | -11.03594 | -45.05051 | 2025-01-23 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 895065d8-df12-3dd8-866d-a4a7bc8a33c7 | -13.03897 | -40.33112 | 2025-01-23 04:27:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3d344d5d-3eeb-3817-84df-cb53faebdc59 | -12.0812 | -38.0148 | 2025-01-23 04:27:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 63c1ed14-89ce-34bc-ae32-49fdc08abe0d | -16.95607 | -40.05634 | 2025-01-23 04:27:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0d956c63-bcd9-36cd-b913-c4ab1dd7733e | -16.0499 | -39.14534 | 2025-01-23 04:27:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 835f9e9a-8c24-36e7-86e7-357c539a0390 | -13.47598 | -44.01953 | 2025-01-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b6fc201-90f7-31b3-b7e8-8803e3b4b7a6 | -7.73593 | -55.19947 | 2025-01-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdd45176-39e8-3f37-9a85-f99d19479c4c | -14.05856 | -45.81144 | 2025-01-23 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26ad7d3a-78e6-3199-88f4-f240998648e8 | -10.35299 | -38.70945 | 2025-01-23 04:27:00 | NOAA-21 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8cea0ad9-8988-3fdd-811a-30cfac01711d | -14.05455 | -45.81477 | 2025-01-23 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34f396b7-ba31-39eb-a9df-8533f0864e83 | -12.68567 | -46.76634 | 2025-01-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2eb60e00-4b3e-396e-9212-8f7374ae9a69 | -11.02501 | -45.05284 | 2025-01-23 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b4319d6-ab42-386c-be8e-082bcea55d2d | -10.3512 | -47.90627 | 2025-01-23 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb3e5dc6-16fa-327b-b3b9-05e34b54274d | -20.93597 | -49.60006 | 2025-01-23 04:29:00 | NOAA-21 | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3af4dec9-d3bf-30eb-821d-67516bbe7932 | -20.37683 | -50.75686 | 2025-01-23 04:29:00 | NOAA-21 | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bb145748-ae40-3dbd-9282-148cc2ab445f | -22.67631 | -42.85292 | 2025-01-23 04:29:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 68557528-a84f-3030-b589-3b41442b456c | -18.89292 | -39.90161 | 2025-01-23 04:29:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cdf9ae62-e77e-375f-ae3d-13148b1527f6 | -21.18773 | -49.40214 | 2025-01-23 04:29:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b452246f-c16f-3859-b8fb-4378a25fb169 | -18.95732 | -53.68949 | 2025-01-23 04:29:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae48a88f-db8a-3ce2-98f4-46cc8c47976c | -17.90135 | -39.46463 | 2025-01-23 04:29:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d8761db5-3e48-3d82-bbc9-340ae04b1c81 | -17.10509 | -52.61862 | 2025-01-23 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0892c82d-3de9-3662-a456-267bbf7c33d8 | -19.73289 | -54.83282 | 2025-01-23 04:29:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bf26c5f-2f23-3236-a1da-1e768aeb9cc3 | -20.41879 | -43.55547 | 2025-01-23 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6a6ab53e-1ecb-36a4-a529-49b0263d8c5b | -19.14052 | -54.85715 | 2025-01-23 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 916b989c-923f-37ef-b4e9-757390537658 | -19.72886 | -54.8319 | 2025-01-23 04:29:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 795b40da-9c1e-39a8-8386-f88d91d61b26 | -21.18443 | -49.40156 | 2025-01-23 04:29:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 62459f96-cf8a-3840-be53-9eb1fc72d745 | -20.93927 | -49.60064 | 2025-01-23 04:29:00 | NOAA-21 | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8854dc8c-6ba9-3b97-a0cb-8006bd6e8494 | -19.02104 | -57.62299 | 2025-01-23 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 520afe96-2fa5-3302-9faf-4a8bdef5716b | -20.93654 | -49.59638 | 2025-01-23 04:29:00 | NOAA-21 | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| faa914aa-7a78-3351-a077-7f24d52a51c7 | 1.3221 | -60.0272 | 2025-01-23 04:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6f751520-4af8-3bcf-b3e0-9986a5c0f79d | 1.3221 | -60.0463 | 2025-01-23 04:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e4b12444-e1aa-382c-b232-8bef08c26b2e | -27.01699 | -51.75521 | 2025-01-23 04:31:00 | NOAA-21 | VARGEM BONITA | SANTA CATARINA | Brasil | 4219176 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a24d6fab-c07e-38e9-8779-02ec3cc9968a | -27.44917 | -48.44555 | 2025-01-23 04:31:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5c1ce5c7-defb-3838-b306-595ff1b45c23 | -27.56464 | -50.7556 | 2025-01-23 04:31:00 | NOAA-21 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ad79f160-170d-386e-a750-ffd5cb8e8b0b | -28.58679 | -49.44311 | 2025-01-23 04:31:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f6b6ace2-1822-36bc-b96f-1653bbe017d8 | -29.64659 | -54.2002 | 2025-01-23 04:31:00 | NOAA-21 | SÃO PEDRO DO SUL | RIO GRANDE DO SUL | Brasil | 4319406 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| d1118ef2-ef1f-33df-9fda-6b419e8e927a | -30.02148 | -51.31421 | 2025-01-23 04:31:00 | NOAA-21 | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 2c4215ba-22a6-3ea8-886f-23ae03eb020b | -28.01027 | -51.71944 | 2025-01-23 04:31:00 | NOAA-21 | SANANDUVA | RIO GRANDE DO SUL | Brasil | 4316600 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f0ef6413-2d68-3bf0-9820-5695509fed9c | -27.56795 | -50.75624 | 2025-01-23 04:31:00 | NOAA-21 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 058ef271-9426-396f-b477-ea1a7343751d | -26.00936 | -51.32812 | 2025-01-23 04:31:00 | NOAA-21 | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 02357092-977e-34d0-96ac-d09acaf42b6c | -22.96303 | -49.94878 | 2025-01-23 04:31:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fbf93cc4-77b4-30bd-a54a-43c5e6e4a878 | -28.73233 | -52.1027 | 2025-01-23 04:31:00 | NOAA-21 | NOVA ALVORADA | RIO GRANDE DO SUL | Brasil | 4312757 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e2503909-e5b4-38f1-887f-805850d46ccd | -30.02373 | -51.56966 | 2025-01-23 04:31:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 83f1b4f4-1d75-3f84-9443-91d70e601148 | -27.38624 | -51.51118 | 2025-01-23 04:31:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a13e5179-9959-38a9-b025-b0ab6807cb75 | -29.65001 | -54.20097 | 2025-01-23 04:31:00 | NOAA-21 | SÃO PEDRO DO SUL | RIO GRANDE DO SUL | Brasil | 4319406 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 6b7084c5-011e-3a03-83ca-1d780ccf7dd1 | -32.38589 | -52.3981 | 2025-01-23 04:33:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 65f062b9-3fdb-3bb4-bffc-8e629f220332 | -30.44423 | -53.88566 | 2025-01-23 04:33:00 | NOAA-21 | VILA NOVA DO SUL | RIO GRANDE DO SUL | Brasil | 4323457 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 210cbbaf-96a2-3f20-ad49-4f45da4f456a | -30.17843 | -53.58067 | 2025-01-23 04:33:00 | NOAA-21 | SÃO SEPÉ | RIO GRANDE DO SUL | Brasil | 4319604 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| c6efa143-982c-3da6-9f3a-74eb79a27f9a | -30.41599 | -53.06895 | 2025-01-23 04:33:00 | NOAA-21 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 073140dd-e0eb-31a4-988d-855906149ce1 | -32.38983 | -52.39473 | 2025-01-23 04:33:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 9065c7f7-2ccc-3afd-a567-e05951d9812b | -32.10231 | -52.11833 | 2025-01-23 04:33:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| fce4705d-a04a-30da-ab33-d36615b2abab | 1.3221 | -60.0272 | 2025-01-23 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 83412842-3205-36b3-a5b9-3833c362beff | 1.3221 | -60.0463 | 2025-01-23 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 611e745e-f2be-3b3a-99e7-03d3ba58e044 | 1.3221 | -60.0463 | 2025-01-23 04:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a646d4f8-5e68-32d8-a4ce-7bbc7eb93f94 | 1.3221 | -60.0272 | 2025-01-23 04:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 07b2b1bc-cc42-3060-8be6-13eee44b412a | 1.33134 | -60.04152 | 2025-01-23 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 3a670ea8-b77a-328c-9d20-07458247db44 | 2.18157 | -61.81784 | 2025-01-23 04:50:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e23926fc-5a76-38ec-a8f2-8a09e8947d3b | -3.13499 | -40.04689 | 2025-01-23 04:50:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README4.md)
