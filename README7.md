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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7cf6c69-ecd9-3e84-84be-7f380735a76f | -14.19166 | -57.65809 | 2026-04-23 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e655281-166a-3b40-946b-aeacbeda217d | -16.43382 | -54.91606 | 2026-04-23 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 516b1890-73b3-391a-bfc3-da81d34f8e2c | -18.40639 | -51.43171 | 2026-04-23 04:51:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db29723f-955b-348e-99ac-b48e6d7d9a1b | -18.27245 | -52.88877 | 2026-04-23 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41ae0b49-3e29-3052-b97d-bb9ab951dee7 | -17.16768 | -46.83484 | 2026-04-23 04:51:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 052fbdcc-6f9f-34ea-854a-07029eaa60f7 | -18.50293 | -55.50095 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ca3f9850-d2eb-3169-b421-428ae8a20098 | -20.23861 | -46.80066 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88347e77-de32-31fd-b2b4-e9a723bc5764 | -20.16194 | -46.94789 | 2026-04-23 04:53:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25826514-b3bc-3150-8880-0fbdbfc1c5ef | -19.4468 | -56.58962 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3f1bfd84-2175-3d30-8cda-d9b249aba35a | -18.50695 | -55.49776 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| defbe710-a33d-368f-be10-3ecd0ce14864 | -19.44681 | -56.61065 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 99357fb8-3d8c-3b7c-bc16-09faae856e40 | -20.2095 | -46.742 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1a05423-4c55-3b00-97a3-ab98f2deb903 | -20.18682 | -46.8952 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7d0edaf-83cd-391f-812c-28480e97a664 | -20.17519 | -46.95438 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5223d039-847e-3248-bfca-9d5180617f48 | -18.49955 | -55.50033 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f965fe7c-ad9a-3ccf-b6bd-37ff8ffda891 | -23.32824 | -50.12556 | 2026-04-23 04:53:00 | NOAA-20 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fe77177b-e280-3d84-b622-c014552c03b4 | -21.33209 | -47.07898 | 2026-04-23 04:53:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9940960-86a5-31ef-89f7-9798dcd01328 | -29.173 | -50.51374 | 2026-04-23 04:53:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e2417d55-d50b-373f-9cd2-34b6ee9ac4c2 | -21.05231 | -48.66813 | 2026-04-23 04:53:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b0d861e2-91df-35c6-8b51-2219f29260c2 | -21.39653 | -48.66993 | 2026-04-23 04:53:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b579e77e-7273-3d2e-a3fb-9b0b73f2eac1 | -21.196 | -50.65772 | 2026-04-23 04:53:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e3b0881c-eaf8-358b-9921-2efcae93e3c3 | -20.20542 | -46.73634 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7826cc5f-0cea-366a-8e18-4e9a2038a2dc | -20.24537 | -46.7825 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95443531-ba3f-3198-ab88-908adc1e83ac | -21.70449 | -48.42759 | 2026-04-23 04:53:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f71253c4-d2fb-3e93-ae01-d227bdc673e2 | -19.45585 | -56.59978 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b228fdd8-3a33-3ee4-8177-61997674973a | -20.16764 | -46.93911 | 2026-04-23 04:53:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f315cec-6ed3-3f95-8042-8778da27f12b | -22.96905 | -52.69398 | 2026-04-23 04:53:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a614ed0c-8fc0-3dd3-8407-ab841a4b0b18 | -20.23909 | -46.79633 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91581c19-da53-3644-9bfc-bd51a005288f | -21.39902 | -48.67526 | 2026-04-23 04:53:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 015b1334-cfcf-3670-b747-3c02a3dcfafc | -20.71627 | -55.17342 | 2026-04-23 04:53:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9aa6fa3-fecd-36d9-b388-5fbcfdd2333d | -18.41508 | -54.54584 | 2026-04-23 04:53:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c86d5a2-14e3-3ff4-b046-0b8750b8ac2d | -20.20072 | -46.73599 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b658899e-d545-330f-8c37-ae4eed348af6 | -18.58496 | -55.93325 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| df0d8656-5530-35eb-aba4-bd54a1a19e09 | -20.23336 | -46.80537 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e39025df-5588-3611-b220-9921c06adefe | -21.40002 | -51.83681 | 2026-04-23 04:53:00 | NOAA-20 | PANORAMA | SÃO PAULO | Brasil | 3535408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ba047098-f216-3e6a-b914-ae4699f0ac48 | -20.20074 | -46.89644 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4a52471-9c71-38df-ae79-b6f449ebebf2 | -20.23636 | -46.79467 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60bf4fdc-4f4d-3f25-a69a-265865234d59 | -18.58627 | -55.92543 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a749416c-38db-374f-a773-a0310dae0621 | -20.23442 | -46.79593 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cda5ad7-cb8a-3d88-9977-7022af0c7203 | -20.20016 | -46.90133 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03c33cb6-369e-37da-918b-1041dd922dcf | -20.17054 | -46.9542 | 2026-04-23 04:53:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a23195b-9213-3bec-8abf-a3df464f9e5f | -20.23729 | -46.77024 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e13f7949-2c6b-3fdf-95dc-df006a7c3603 | -20.17692 | -46.93964 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8243ba80-cd07-3075-af34-70adb1fb81f2 | -19.43984 | -56.60931 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 27b06fdc-10c8-350c-bfb2-c110b74a3b00 | -19.43149 | -56.59508 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 860ba66b-c9e6-38d3-9242-9e821bcfc57b | -19.44332 | -56.58895 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bbe218a5-0007-3c57-bcfa-654f59bfd62e | -19.68979 | -51.33882 | 2026-04-23 04:53:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b5af5e0-2cd6-36c7-b5f5-61ca8d51817b | -22.96846 | -52.69809 | 2026-04-23 04:53:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d616339a-0550-3b76-a5fe-965cdd26db2d | -20.2339 | -46.80051 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d516d3e-2b04-387d-8bdc-b8a89a61d075 | -20.19254 | -46.88644 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9848c833-a600-3715-8a9c-56ba2e40737f | -20.22978 | -46.79522 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebd8e78d-b186-362f-9f92-b5e64da9b87a | -20.2353 | -46.8036 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e0d968c-5465-3935-92b2-cf9d386030f9 | -20.1711 | -46.94939 | 2026-04-23 04:53:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 477b8e04-f917-3ce3-b30e-18ad71a729c8 | -20.23583 | -46.79912 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ce12305-8c44-3e6e-8dbb-dd8b599f0998 | -20.23494 | -46.79129 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95f56c5b-2ba3-3631-9f8f-ab30b8161b66 | -20.23116 | -46.7987 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b3abc7d-7d56-3dd2-8c3a-db95f6a87d77 | -20.1874 | -46.89026 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5f75f2f-0a9f-37ee-9fbe-12bd08004f46 | -20.20482 | -46.7415 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de5ca34f-1aa8-31ce-853f-f90b9bd83b49 | -19.90974 | -49.88142 | 2026-04-23 04:53:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 71fa8878-22fd-35a3-9049-2758ca5705de | -18.41841 | -54.54643 | 2026-04-23 04:53:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4962ee3-b1b5-350c-896e-9494c884c281 | -19.45029 | -56.61133 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| bdbe1ac7-2d16-3526-a3d7-55ed97cb94f3 | -20.23172 | -46.79395 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b170c0b-b86e-3be1-90b6-0a81a50764f5 | -20.1625 | -46.9431 | 2026-04-23 04:53:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18ea20e7-0e76-3b0d-bfca-353903db300f | -20.23949 | -46.76841 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f1eaee0-f85f-3e49-a26e-f6815406b231 | -21.39604 | -48.67402 | 2026-04-23 04:53:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f84e7c8-cb70-38e2-a6f7-b063c12cfa8a | -20.19961 | -46.906 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 027e9efa-1c77-326a-8f57-8aacfdaf2d0e | -20.17577 | -46.94942 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14b52fa0-1071-375f-aae0-5418530dce3b | -20.20366 | -46.90296 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7feb3c14-0958-3c6b-8f2c-f984b3dbd054 | -20.23876 | -46.77451 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4621c970-239a-3005-93a7-7b4fd0d66826 | -20.19714 | -46.8872 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5da3c80c-44c7-3969-b186-b5c41605d194 | -20.19131 | -46.7355 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 035c2b1f-88d2-3347-af2d-116d426dfd8d | -19.68626 | -51.33825 | 2026-04-23 04:53:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bff96646-6c3d-32d3-a03c-603e64c4f1c3 | -21.27579 | -54.41667 | 2026-04-23 04:53:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3796318-47ba-3183-a343-972f2342e7c2 | -24.9541 | -49.63572 | 2026-04-23 04:53:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 176a6423-11c8-3681-8b6f-869a49c32606 | -18.58562 | -55.92934 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5f6337db-2b26-3ddb-a7c7-b32c8432c59e | -21.04815 | -48.6675 | 2026-04-23 04:53:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 87cf8ffd-64fa-3158-adcf-7183c2969436 | -19.43984 | -56.58828 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dd2de2ab-ad6d-34d3-b727-bb009f81041a | -19.44332 | -56.60999 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e3993c69-c185-392d-9cdb-022552894eea | -20.2013 | -46.89172 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 031bb9c4-5abb-37c3-9e5f-64f3dd26f824 | -20.7196 | -55.17404 | 2026-04-23 04:53:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e282f85e-0919-3adb-ae8c-b1166f66a789 | -20.18981 | -46.90964 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e699114-474f-3031-ac18-c18efec2d4b0 | -20.18571 | -46.90469 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92851d4a-59a9-3f6c-b048-c4abbccb96d6 | -20.19667 | -46.73009 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95dbdf12-743e-3da2-92c0-1fdf3a358fa2 | -19.45516 | -56.60384 | 2026-04-23 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f5559466-12ec-36f7-9c9c-df8a3263aa7f | -22.965 | -52.69752 | 2026-04-23 04:53:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 002b115d-8970-326f-92c5-1629f40a32fc | -20.19494 | -46.90581 | 2026-04-23 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb455736-08db-3937-bc99-68ed21e74dd0 | -22.78742 | -47.0466 | 2026-04-23 04:53:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aad7a677-320e-3b01-8a33-5ecd138a24e1 | -20.2413 | -46.7767 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39e45a0c-0db1-3381-8cd9-476698fbea20 | -20.18625 | -46.90002 | 2026-04-23 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 841c2a94-52a3-32b0-8ae7-fd8757daeba1 | -27.94345 | -50.20807 | 2026-04-23 04:55:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b46d8093-997b-3dd4-9ac9-84af4338c00e | -27.94392 | -50.20396 | 2026-04-23 04:55:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6e3c2eb5-4544-3523-97f6-c66e6aff77d3 | -27.29488 | -50.53588 | 2026-04-23 04:55:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 08e37823-a0bb-3d7b-8210-7f94d89be8bf | -27.93563 | -50.20269 | 2026-04-23 04:55:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 53855c5c-9c9f-34b0-b608-2c5703bc141f | -5.28346 | -56.01633 | 2026-04-23 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f69a4b2f-7008-3524-ae75-e1f74d2d052b | -11.91347 | -58.07375 | 2026-04-23 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c65acd3-37a5-330d-ba45-34d8c2dcf311 | -13.71583 | -57.48191 | 2026-04-23 05:38:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b10a023-290e-332b-ae21-409618f3c134 | -12.86718 | -58.6298 | 2026-04-23 05:38:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56a34f11-80e3-3b82-b43d-9ed43eadd2a9 | -12.30686 | -57.17932 | 2026-04-23 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf03a4bb-5c5c-36a9-9e17-330a2caf94f9 | -13.66006 | -60.63333 | 2026-04-23 05:38:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81c13465-1ae3-3d89-b945-85919b15a1a2 | -14.19531 | -57.66115 | 2026-04-23 05:38:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README8.md)
