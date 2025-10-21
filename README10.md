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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e80b8bcc-8990-3ab1-b9b1-247e6021e723 | -20.48379 | -54.68388 | 2025-10-21 03:57:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 12def420-2d67-3ade-89cf-fe65b0649e4a | -18.59306 | -51.7213 | 2025-10-21 03:57:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a142e23-d036-3a2e-9b3a-587df63de34e | -17.41831 | -55.06332 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 5b56e52e-561f-3a29-b71a-89f82e093cf9 | -20.07011 | -45.49036 | 2025-10-21 03:57:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e48ed163-7daf-3a4f-82ff-434826ebe39a | -20.47742 | -54.68205 | 2025-10-21 03:57:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 151bc2bf-17b8-3fbe-b740-c25947882865 | -18.59392 | -51.71741 | 2025-10-21 03:57:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d090d559-7d7d-355f-abae-adf3eb6d508a | -19.93603 | -47.62179 | 2025-10-21 03:57:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 977f7316-1ca2-3002-ab27-86e86ba63ce2 | -17.41301 | -55.05466 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 9687528f-69cd-3651-b296-4c447aad7716 | -18.18015 | -52.97195 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46e02af4-ee1e-3eca-90ae-095fcf3004c4 | -20.4824 | -54.68959 | 2025-10-21 03:57:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8c5cfbf7-aab2-318e-a301-f47845068fc0 | -20.95384 | -45.81555 | 2025-10-21 03:57:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa9c3190-c002-3219-bc1c-a05033432fda | -17.437 | -55.0463 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7f183e8b-7726-3e4c-a49c-948ae514fa9d | -17.40445 | -55.05978 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| d63ae86e-bc4b-3fb6-b403-ef3fe30eaa5b | -18.17293 | -52.9754 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 705235db-0455-3007-b0bc-197cd386324f | -18.19114 | -52.98018 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1daba95e-f544-35d6-8cf8-fbfa8ef477f0 | -18.44707 | -46.39447 | 2025-10-21 03:57:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9a7158d-7aab-38b5-9c15-47101158a421 | -21.65754 | -41.32598 | 2025-10-21 03:57:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2646100b-f1b4-3962-84ee-0f9e7ce6cdf9 | -22.29915 | -51.51245 | 2025-10-21 03:57:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3353114d-6f2b-3c34-af57-f2ed708a59b8 | -17.6821 | -52.2602 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c099e91e-4deb-38a7-94d5-c2eda8b8d357 | -17.67998 | -52.26971 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 99021e9b-4d48-3634-9117-a5761f305dc3 | -18.19228 | -52.97518 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3316988c-4989-35bb-a26f-e5a8dc6927ae | -17.68291 | -52.24331 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d443857b-e219-35cf-8b36-9fb84f7f88e6 | -20.47816 | -54.67949 | 2025-10-21 03:57:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4cdd968a-4804-32f4-b256-f904cbb89f54 | -17.67937 | -52.2446 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d316e53-049f-38a4-9157-409d78fd1462 | -20.42988 | -48.03586 | 2025-10-21 03:57:00 | NOAA-20 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4f7e998-0933-3b06-9b16-c1df35663c53 | -18.19121 | -52.98384 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac84808b-339d-3116-b9a5-e92590541ebb | -19.33781 | -44.68871 | 2025-10-21 03:57:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4607e00e-da04-36df-bcac-6c5331ecd273 | -17.4439 | -55.04813 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3354a246-4c5f-361b-95ce-da0b0920e41f | -17.68272 | -52.273 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| daef9a4f-b745-3a37-974e-6811e6cc0c23 | -17.67735 | -52.25365 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 932869ad-5ab6-326e-872e-f31de4156d50 | -17.77099 | -50.85727 | 2025-10-21 03:57:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 480d3399-e073-31d7-995b-7dd17c1743fe | -18.16455 | -52.98389 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 181ba2ec-8ef0-3eb0-ab95-8cad78db9ea2 | -18.58832 | -51.71596 | 2025-10-21 03:57:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99c13c71-5371-37bd-b1e4-a9d3a3a6152e | -20.4768 | -54.68524 | 2025-10-21 03:57:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3b5e2421-4da5-3239-8272-870f20da129d | -18.19229 | -52.97893 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| accf13ef-4989-3f4b-86aa-ae183cdcf566 | -19.33703 | -44.69312 | 2025-10-21 03:57:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1948ab99-c6ba-34da-804c-ec7b883bab43 | -18.58746 | -51.71989 | 2025-10-21 03:57:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da38f124-d106-37af-a8fa-c70136bb299c | -17.44553 | -55.04119 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5e5c8c33-e464-3d8c-a15f-a61474feec23 | -17.68192 | -52.24794 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 59b6d0fa-a243-3870-b3cc-5003f26e3fda | -17.41993 | -55.05644 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| ecc90807-c414-3664-b740-4f1e5c5bcf24 | -19.87338 | -44.9332 | 2025-10-21 03:57:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c3c5f5d-3ef8-3f6b-91de-b9d01ceb1604 | -18.79909 | -47.01704 | 2025-10-21 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 02764658-f974-3657-b448-00c366f38b67 | -17.77218 | -50.85489 | 2025-10-21 03:57:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01b57544-9449-35a6-b388-9900005c72c9 | -19.90879 | -44.35532 | 2025-10-21 03:57:00 | NOAA-20 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5e6300bb-a1c1-3a80-9db0-653dc6b0cfb9 | -20.00455 | -46.13204 | 2025-10-21 03:57:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02975b16-9c12-3ab0-8246-c37bb76685d6 | -17.6852 | -52.24632 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| be76ea84-1abe-3b44-87f5-94423cd3082a | -19.38428 | -49.22618 | 2025-10-21 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52947150-4e13-3163-bcbb-1f00f04dd94f | -17.68042 | -52.23988 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f25c9063-10bb-377b-84ff-907c3615fd4a | -17.67628 | -52.25846 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47dc5cbe-4aef-384f-90a9-43480e245889 | -19.91234 | -44.35599 | 2025-10-21 03:57:00 | NOAA-20 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c3d7c6a4-ec49-3c98-a1fa-9ddfc83b9b9b | -18.79987 | -47.01296 | 2025-10-21 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 897e4c5a-4a9d-3923-a6e1-1d42c177b4f0 | -20.95359 | -45.81667 | 2025-10-21 03:57:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb927cba-e821-35b1-8b69-331fab514d56 | -17.4028 | -55.06676 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| dff3f360-da97-34c1-b900-cc885f7f3d88 | -17.67992 | -52.25719 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 44651b0e-5b71-340d-95bb-54b3a82cb048 | -21.9491 | -43.03039 | 2025-10-21 03:57:00 | NOAA-20 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d9452ab6-61fa-3e16-9a23-9a661875c2a5 | -21.04229 | -44.66832 | 2025-10-21 03:57:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 80396bde-fce6-3042-b584-f985813b66b7 | -20.53073 | -48.07757 | 2025-10-21 03:57:00 | NOAA-20 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6637ffb8-65ab-396f-b257-3d83b90b7302 | -17.40749 | -55.05537 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 62d9f1ea-be78-364d-b211-8a6581e290a2 | -22.2999 | -51.509 | 2025-10-21 03:57:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d03d8ac9-a52c-39e0-b1fc-251c1dee3b96 | -18.17409 | -52.97404 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58b9ab60-826c-3e34-8fca-0ff1290f5968 | -17.7714 | -50.85852 | 2025-10-21 03:57:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c31f817-60b2-34cb-b224-ea02c63c7b91 | -22.17193 | -45.85014 | 2025-10-21 03:57:00 | NOAA-20 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 44b75ca1-bed8-3dd7-93e0-d05d9f14f867 | -20.06924 | -45.49516 | 2025-10-21 03:57:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d440c82b-aa4b-317e-ae8b-54d81203d4cd | -17.77174 | -50.85362 | 2025-10-21 03:57:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 484859d8-31c6-3658-9957-f15044555c48 | -17.40972 | -55.06857 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 076785cc-5eec-33c6-86ff-50455eacc30f | -18.1934 | -52.97389 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e2945a1-5430-318d-afec-d7c749ca874f | -17.68094 | -52.25243 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f5627bc5-2234-3959-bb76-9ba875d6c7f5 | -20.48452 | -54.68137 | 2025-10-21 03:57:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 76ed0491-abec-31be-8a77-f39fe90336e4 | -18.72899 | -47.54427 | 2025-10-21 03:57:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b78d7745-e390-369c-8260-55b73bea57b9 | -17.68591 | -52.27103 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d23d3418-e136-38c3-aead-46de2f2d5323 | -18.65746 | -46.48034 | 2025-10-21 03:57:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39eef4ec-0e8c-3cf7-96e1-e6fcbbf8b1e8 | -17.40589 | -55.06235 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 8dd39cf6-709f-325e-b394-a4ff20c36263 | -17.43863 | -55.03934 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 28ca0d2b-e1a4-3d5e-8e5d-7dfe07286651 | -18.17296 | -52.97914 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34a2366c-bffb-3605-b838-71017af92756 | -17.68375 | -52.26824 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b43deed0-856f-328f-81f6-8d1b1f0d6d0a | -17.40427 | -55.06936 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 33f9e212-d049-3521-b674-5c3138b6bed5 | -17.68419 | -52.25082 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 978004ac-cde8-3e01-9b31-8dad56740a57 | -18.16577 | -52.98257 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9f3be07-34e9-3116-8239-588472de1c84 | -22.0095 | -45.44034 | 2025-10-21 03:57:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ec5cfa26-9789-3030-b92c-1f933032e7ba | -18.16569 | -52.9789 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 104481ca-33e3-36a5-8c5c-595a6221373d | -17.68318 | -52.25537 | 2025-10-21 03:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b198f984-7267-3444-ad3a-59a1a6cd2488 | -20.48318 | -54.68707 | 2025-10-21 03:57:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 178a31b4-a64d-3261-89cf-580e7b72fa8b | -17.41137 | -55.06159 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| a0349425-1953-3d4e-ace7-334f8387b0d1 | -21.04152 | -44.67263 | 2025-10-21 03:57:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 47448c20-17ad-3b75-bf58-7ead7835bb1e | -17.42156 | -55.04955 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 15749031-b78f-390b-af5e-de53028d1f53 | -21.03948 | -44.66909 | 2025-10-21 03:57:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7e2be6a4-f38d-3ca3-bf8d-b22abad0f839 | -17.4131 | -55.0678 | 2025-10-21 04:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 08ca572a-3036-3e84-8e1f-2f4baca20834 | -17.4332 | -55.0441 | 2025-10-21 04:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 75e06aad-de9c-37c3-9d4f-58e2a7270d70 | -4.8222 | -42.7477 | 2025-10-21 04:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 367f2474-2028-34c5-913a-6f1090d1f196 | -17.4135 | -55.0468 | 2025-10-21 04:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| adbdcd4b-80d5-3dd5-8b20-6a594b955d14 | -3.5154 | -45.8187 | 2025-10-21 04:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 5a385fe4-670d-3b7b-b834-0daef9fd1e13 | -4.8033 | -42.7725 | 2025-10-21 04:00:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| d37c9fbd-73f9-3454-b15b-ffb6ceb88175 | -4.8035 | -42.7489 | 2025-10-21 04:00:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2ea2ca12-249f-367e-a38c-13fc5f486135 | -10.9393 | -50.3407 | 2025-10-21 04:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| e1e2f163-2a3c-3ca9-9d31-da7df3de7b7f | -3.4968 | -45.8195 | 2025-10-21 04:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 241.3 |
| cbb234a3-b1a8-3c8e-b83d-a18c26a1b7d9 | -3.5153 | -45.8411 | 2025-10-21 04:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 56b50a9b-5d86-33f3-9dc6-b3f5d292fb02 | -3.4967 | -45.8418 | 2025-10-21 04:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 5b2cc6f5-3813-3940-9553-d5d37f27a6c6 | -4.822 | -42.7712 | 2025-10-21 04:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 94bc3eec-4107-3540-ba97-20d90a7026cb | -33.05226 | -53.16425 | 2025-10-21 04:02:00 | NOAA-20 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 3a147a74-63d3-3e0e-8bcf-06b144f4a87d | -3.5153 | -45.8411 | 2025-10-21 04:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |


[Clique aqui para ver as próximas entradas](README11.md)
