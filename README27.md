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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c614da9d-3adf-3e05-8999-5dc357f8a9da | -19.59127 | -46.90429 | 2026-08-14 04:36:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 145121cc-8bf8-356a-b805-48914441db00 | -23.31092 | -47.54219 | 2026-08-14 04:36:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2681db26-ec2e-35f6-9534-b579ff659dba | -18.53797 | -48.20284 | 2026-08-14 04:36:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c17c086e-d70b-3f14-88be-1210662988ba | -21.89319 | -55.37022 | 2026-08-14 04:36:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6dfeb211-f7d5-320b-84cc-7ae4fc245336 | -21.75094 | -44.03045 | 2026-08-14 04:36:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1013e55f-1ff7-3c04-b381-766691ebdace | -20.84531 | -45.79367 | 2026-08-14 04:36:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5e15a1e-bc0f-34aa-9e4e-986b4aa3d92f | -21.9022 | -55.36638 | 2026-08-14 04:36:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7bc2727c-3b6c-3a9c-989d-7d090ecf3165 | -20.32436 | -42.01577 | 2026-08-14 04:36:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0ef5db10-685c-3b85-a713-2ec1f33df7ce | -19.58777 | -46.90369 | 2026-08-14 04:36:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fefe4ca2-8c18-3193-910e-e55d9452c19f | -19.95316 | -45.55033 | 2026-08-14 04:36:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb540692-6ba4-3ea9-b8a1-29b45d922512 | -20.25972 | -46.71074 | 2026-08-14 04:36:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a3e4556-7401-391f-a7c5-7dcc03268630 | -20.99893 | -47.27245 | 2026-08-14 04:36:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ffd647c-e347-3699-ac79-e8d17d1c5229 | -21.4526 | -48.68283 | 2026-08-14 04:36:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 665c971e-a442-374b-9097-12214edea695 | -19.58893 | -46.89547 | 2026-08-14 04:36:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c19a247-6f49-3589-9827-acf30c248816 | -21.89822 | -55.36557 | 2026-08-14 04:36:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c54bba6a-1f49-33d4-a88f-d85c66a35e0a | -21.76255 | -44.04078 | 2026-08-14 04:36:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 48fb8ac4-cb28-3874-a4d7-e776e77d8914 | -21.77944 | -44.04295 | 2026-08-14 04:36:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 86d01c5e-1db2-3f0d-9323-a50931b06de6 | -21.76205 | -44.04485 | 2026-08-14 04:36:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a919eb09-2157-3f74-b22b-9e5a1e131ef2 | -23.31151 | -47.5379 | 2026-08-14 04:36:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ac53e51b-6739-3147-af63-9426824a09c8 | -20.11164 | -50.48242 | 2026-08-14 04:36:00 | NOAA-20 | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 842999b8-1f1a-3a7f-a219-ed3c58369d32 | -22.92259 | -49.2099 | 2026-08-14 04:36:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3b84192-dfe3-3413-91f3-87565ebd28e8 | -21.00243 | -47.27306 | 2026-08-14 04:36:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6546009a-4b62-3103-a0dd-80b3440f499a | -21.56156 | -48.77156 | 2026-08-14 04:36:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3b42291-fccd-31e2-8a81-ab2c5a56b8e9 | -21.89611 | -55.3765 | 2026-08-14 04:36:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 14f53132-f532-3db7-afbd-e1bbfcba9630 | -21.73754 | -44.07022 | 2026-08-14 04:36:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a7eaecf0-60ce-3974-be85-bc208b345565 | -20.2634 | -46.71702 | 2026-08-14 04:36:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5be3ee70-626f-3079-a014-d2dee71b8240 | -20.25918 | -46.61892 | 2026-08-14 04:36:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c322fc6b-a1cc-3603-abd8-e603af83aef7 | -20.09494 | -49.95345 | 2026-08-14 04:36:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4b13439d-ace3-341a-8b75-1742803a224f | -20.45127 | -46.47699 | 2026-08-14 04:36:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f322207-9e80-3851-8bdb-eff815f20613 | -21.73803 | -44.06617 | 2026-08-14 04:36:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 57027d42-1281-3e26-a350-114de636fc90 | -20.89493 | -50.5119 | 2026-08-14 04:36:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 06845c9e-feea-380b-94c9-59123974d8ee | -21.38615 | -48.63375 | 2026-08-14 04:36:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99c9d528-0941-3080-b40c-88e21562656d | -20.25914 | -46.71496 | 2026-08-14 04:36:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5385b4bc-79ef-399e-9e40-53609a75e499 | -18.55138 | -48.18226 | 2026-08-14 04:36:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caa58616-283d-39f4-8460-5e75c192b7d7 | -18.55082 | -48.18597 | 2026-08-14 04:36:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25b7a0ee-fee4-35c4-b859-ca6853c3acb1 | -20.26624 | -46.71622 | 2026-08-14 04:36:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fdb054ea-8a46-3796-be28-a983bd8880f1 | -21.74622 | -44.03397 | 2026-08-14 04:36:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 86f00a03-19f7-3ff8-ae41-8f6988398525 | -18.85636 | -47.06888 | 2026-08-14 04:36:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0832b15a-60e3-3cd2-ac70-bcaa5e17fc43 | -18.54131 | -48.2034 | 2026-08-14 04:36:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb9880f3-6f7c-3ddb-8dc6-200c6b9e30d4 | -18.85694 | -47.06491 | 2026-08-14 04:36:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f50680b-f0a4-3682-bf65-04964b0a9512 | -21.59819 | -43.69999 | 2026-08-14 04:36:00 | NOAA-20 | BIAS FORTES | MINAS GERAIS | Brasil | 3106804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 77cb9e4c-d78b-3625-ba26-34eb4580d559 | -20.3191 | -42.01999 | 2026-08-14 04:36:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 15615dbc-30eb-3355-9776-0c82d5e4c716 | -23.81913 | -48.70979 | 2026-08-14 04:36:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21de17dc-2368-374e-a1c7-192fb85f98b0 | -21.74672 | -44.02988 | 2026-08-14 04:36:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 148be6aa-baee-3067-be19-afd064e4cf2d | -22.91589 | -49.20871 | 2026-08-14 04:36:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2fe5a12-13ae-39fc-9482-cd7ad5650f36 | -21.77893 | -44.04705 | 2026-08-14 04:36:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 3aacbd63-f154-35ea-a6e6-f59d9f6b4f82 | -22.00973 | -47.21385 | 2026-08-14 04:36:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e02faf87-e21b-389d-bd9d-703433d25cce | -20.25985 | -46.71639 | 2026-08-14 04:36:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40907b0f-dc4c-3ed8-999d-d4b62bed8f05 | -20.44768 | -46.47631 | 2026-08-14 04:36:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d905a3f-d527-302c-8098-85d636de694b | -26.77837 | -52.13333 | 2026-08-14 04:38:00 | NOAA-20 | VARGEÃO | SANTA CATARINA | Brasil | 4219101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a32fc284-8ba4-36eb-a051-f9d726bacb8c | -11.4885 | -54.6273 | 2026-08-14 04:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 39348e8b-4a65-3760-8893-8237bdcc9ca2 | -14.2945 | -51.9635 | 2026-08-14 04:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 6f34f7f1-41b7-359b-91b6-586d901c1030 | -6.6195 | -59.0416 | 2026-08-14 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| cdbf4cfc-31f8-3163-b389-13493099ef43 | -6.6195 | -59.0416 | 2026-08-14 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 065fc9fa-9217-3830-a41b-62e0e4be8e9c | -14.2945 | -51.9635 | 2026-08-14 04:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| c5501337-0a88-399e-acf1-760eaa1d2c79 | -14.2945 | -51.9635 | 2026-08-14 05:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e2933921-2516-35be-a16e-12c7859a17eb | -4.5057 | -42.5325 | 2026-08-14 05:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| 33f469e6-9b8e-3a4a-aebc-650a89139018 | -6.6195 | -59.0416 | 2026-08-14 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a7806fc9-cc0d-3893-a53a-7f5dbe45aed0 | -11.4885 | -54.6273 | 2026-08-14 05:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 141b1274-fa76-3a7b-b696-c5b6a2eb691d | -2.57247 | -47.24713 | 2026-08-14 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab74262f-a896-3915-a284-da5e26cb95d6 | -3.34229 | -50.14394 | 2026-08-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cd90fda-f5d5-32b3-bedf-e77f47871b51 | -4.10774 | -50.44485 | 2026-08-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 80580d19-09d3-3e51-803d-22e0f955e8b5 | -2.74998 | -60.23691 | 2026-08-14 05:16:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b686caf-4130-3d29-a2b8-8d8da896b227 | -1.83111 | -54.50519 | 2026-08-14 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d58194ea-80a3-3e08-b99b-bac4a86d359b | -2.96147 | -49.20717 | 2026-08-14 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac74250c-02ca-391b-b782-66e8f7519763 | -3.15235 | -54.60527 | 2026-08-14 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00bc29a2-45bb-34ab-b433-f0a23b193fb7 | -2.83714 | -58.37471 | 2026-08-14 05:16:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41e77d19-f651-35db-9cc5-ca6a716689ca | -2.65061 | -47.97967 | 2026-08-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 31a6e941-650c-3fec-87d7-1028475c53f0 | -4.72291 | -56.03814 | 2026-08-14 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d10d7a24-37c9-38ad-9138-219480f994c7 | -3.26396 | -49.52515 | 2026-08-14 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ac0c330-f48f-3670-ad89-6d423aaedb2e | -2.65004 | -47.98354 | 2026-08-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25b1e436-3fca-3fee-83b4-8043b10451cb | -3.65716 | -55.54773 | 2026-08-14 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7787c68f-ec7a-39f4-89c7-a17748ca3b78 | -4.10694 | -50.45036 | 2026-08-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 701ba28d-1fb7-3ad6-a87c-c3a776552d61 | -4.74027 | -48.01927 | 2026-08-14 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13e77df2-e4e6-3a66-8057-20dea9926478 | -3.2635 | -49.52828 | 2026-08-14 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c322290-5120-363a-95f6-0e35a85125ee | -2.36351 | -60.0827 | 2026-08-14 05:16:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99952855-1a9d-35d7-8df8-b114126108e9 | 0.49539 | -60.59259 | 2026-08-14 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d9fad78-a59e-366b-8279-c6eb4d3bd4e4 | -3.19548 | -54.44696 | 2026-08-14 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 966e7f53-e652-3190-bda0-93fde37f4ae5 | 0.96001 | -59.94736 | 2026-08-14 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a691fd60-bfe4-3706-a5ba-e3a4486ff932 | -2.69933 | -48.21798 | 2026-08-14 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 322b6091-39f4-3a7c-86a1-a01086bb7eec | -2.69368 | -48.21711 | 2026-08-14 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8adecc1c-5da1-3b0f-8a41-0139311ccb65 | -2.97659 | -51.68892 | 2026-08-14 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ecce0947-2025-3746-9c87-0e792b3f1cda | -1.83242 | -54.49656 | 2026-08-14 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2431294c-f2b0-35d1-a396-6bb65dd7e586 | -3.24669 | -61.2522 | 2026-08-14 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42789a04-4ea6-389e-99a7-aebf0c3e162a | 0.49899 | -60.59205 | 2026-08-14 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8324db98-0d9e-3091-b463-bb6d5978bbb0 | -4.26949 | -49.36493 | 2026-08-14 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43cfd70c-0c22-3a98-a81e-630604941a92 | -4.27487 | -49.36563 | 2026-08-14 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06aaee47-061e-3bc4-8114-a6624c712f7e | -2.64488 | -47.97875 | 2026-08-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9538a822-f94d-339e-bf40-646bb1606ade | -3.34225 | -50.14509 | 2026-08-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 239e5ce9-b5e0-36b8-b3f8-cb3ea86ef7f2 | -3.24544 | -60.12422 | 2026-08-14 05:16:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 64753d11-d9d0-3d69-acef-2bf2193d94fd | -2.73692 | -58.18978 | 2026-08-14 05:16:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 293a9c50-6d49-3f03-ba50-fb70d4853918 | -2.64946 | -47.98744 | 2026-08-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9afb443-591f-30c3-9224-a6213d771a50 | -1.82744 | -54.50463 | 2026-08-14 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0706a710-3687-3198-830c-366d8525d8c2 | -1.78061 | -55.53022 | 2026-08-14 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd4eb111-272c-3ed5-a21f-bd60abad669c | -3.97586 | -59.63816 | 2026-08-14 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6565a23-d572-3d7e-aa2d-c1c9ea3b5232 | -3.4385 | -60.09797 | 2026-08-14 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f35afa-f361-37ea-bc33-194851830556 | -3.18995 | -59.01292 | 2026-08-14 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31ce5682-1347-349f-a4b4-d5b85013ad1a | -3.66464 | -48.98462 | 2026-08-14 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c28da84-3e92-321f-a35b-ddf530a7232e | -2.79397 | -49.58416 | 2026-08-14 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b477bc52-b9d1-34e4-8f68-17644ed37b37 | -1.7841 | -55.53075 | 2026-08-14 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)
