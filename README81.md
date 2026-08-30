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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2eb1877-abb2-3905-a102-d72bb755ad6c | -12.9216 | -45.8812 | 2026-08-30 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| cf0d32e3-508b-3ab0-93ae-70d0ba2f2a8d | -13.8749 | -54.1361 | 2026-08-30 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 348.0 |
| 1b1dd831-df1b-322e-81ff-eeebaaf4fe56 | -6.9361 | -55.7157 | 2026-08-30 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 06a6f824-84ef-320c-84e5-4d0f118b7218 | -10.7407 | -54.0401 | 2026-08-30 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| aeec52b7-d017-33fa-8f33-404b24127e64 | -4.9604 | -55.8424 | 2026-08-30 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 217.8 |
| 5619302a-91af-33df-bd31-eebcd4829c3c | -6.8752 | -59.4749 | 2026-08-30 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 302.0 |
| e8e1e710-2658-346e-af3b-e1a8e4658871 | -10.7867 | -45.3433 | 2026-08-30 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 4662061d-e061-39f2-bca0-9d3e10544469 | -6.7699 | -55.6644 | 2026-08-30 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| ac88495e-c1d5-38b0-a37b-beacb77c2fba | -8.6154 | -54.7945 | 2026-08-30 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| d7cb97d9-ad92-34b1-846e-5f7107969790 | -4.9603 | -55.8622 | 2026-08-30 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 631cb4fe-3064-3bbe-a75f-865535a61d73 | -12.3807 | -48.2099 | 2026-08-30 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c1d093b8-1ab9-374c-9c98-82e2b2abbd0d | -12.3619 | -48.1903 | 2026-08-30 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 325ba4b3-d55f-3bf6-9b05-8850040dc70d | -9.7832 | -46.4202 | 2026-08-30 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 15f57ac2-2f52-322d-9d1e-1d3a5cd1fd8f | -3.6215 | -60.566 | 2026-08-30 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 452726f3-861f-3c2e-a438-2fec15d72692 | -11.2829 | -45.3214 | 2026-08-30 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 866b05b8-6fc7-3aa5-a85c-62d3a704f0f7 | -7.5134 | -55.3452 | 2026-08-30 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| ed2dbac3-fe93-3db8-84c8-fa3c31ec751b | -11.2638 | -45.3241 | 2026-08-30 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| fe0c90b5-bc68-3b5f-85bd-674775838607 | -14.4197 | -52.5413 | 2026-08-30 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 160.3 |
| e77dcd48-04fd-3e71-a92a-bb8b8b74260d | -5.8973 | -46.1313 | 2026-08-30 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0779c3b1-ba74-32d9-ba92-68ae06972610 | -10.1538 | -45.6982 | 2026-08-30 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 162.8 |
| eaf381fb-1621-3eef-9fdb-f180d7c7fe28 | -5.4876 | -57.1416 | 2026-08-30 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e7675fe1-1905-316c-88b1-5dd0f931fc1e | -8.2229 | -54.9412 | 2026-08-30 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 39ebdd36-a41d-3261-95ec-dffeb3ce8e87 | -8.5969 | -54.7755 | 2026-08-30 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ae99416f-77ac-31dc-b3d8-53d1c11466fa | -6.8753 | -59.4557 | 2026-08-30 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 031d3643-4120-3d65-a20f-11e5431e7a2b | -14.7605 | -48.7245 | 2026-08-30 13:40:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4ba0f9ff-8a7e-3fa6-8451-d2134f03a145 | -8.1534 | -45.4904 | 2026-08-30 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 2af62604-bacf-3a52-90f8-fa6f87efe7fa | -8.0098 | -46.4936 | 2026-08-30 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 377a62a4-45cf-3d2b-9142-7d30d65c88e6 | -7.5137 | -55.3051 | 2026-08-30 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 8214d62a-7076-3f32-bb4a-f80c03983cba | -13.3799 | -51.4634 | 2026-08-30 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 689ff39b-8901-3b67-9cbe-fa42c1be3c4c | -12.3811 | -48.1877 | 2026-08-30 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 182.4 |
| e80ae6f7-82b7-33c8-97a9-429a356ca726 | -11.2503 | -54.0146 | 2026-08-30 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 183a3a68-2715-3b14-99b6-cfc6f7663e4d | -14.1649 | -52.8058 | 2026-08-30 13:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 57520bfc-4290-339b-a9ca-a873072e4a5a | -7.5323 | -55.3041 | 2026-08-30 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 921095ee-9ff1-3e75-9bc1-7ed6e32fc2a6 | -6.8799 | -41.6754 | 2026-08-30 13:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 403407e2-df76-3272-923a-371ecb083240 | -6.0 | -45.0889 | 2026-08-30 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 99902375-4f7d-3294-80f5-bdc951ce0a2e | -11.3479 | -48.3652 | 2026-08-30 13:40:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 149ea67c-b12b-35c0-907a-409734c48bc1 | -7.5136 | -55.3251 | 2026-08-30 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 196.3 |
| b82f0ec6-e997-3bdb-bbf0-a52f6b97e16c | -10.7867 | -45.3433 | 2026-08-30 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 8048eb55-2769-3b82-a13f-72d5b703b3a6 | -10.8025 | -50.6539 | 2026-08-30 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d347bb25-b3af-354a-8a5f-438ef11bfc3c | -7.5661 | -61.3239 | 2026-08-30 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3b406285-da7b-3be8-9435-77bcf50c966c | -6.861 | -41.6772 | 2026-08-30 13:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 501.7 |
| deac36f7-efb4-33ce-9ae1-0b344a60d4c6 | -4.9605 | -55.8226 | 2026-08-30 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| bfe32987-6db3-3d8f-a588-7e659718a567 | -12.3807 | -48.2099 | 2026-08-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 2a2c5ffb-d069-3d06-80f8-50e45f218a81 | -12.285 | -50.5724 | 2026-08-30 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| a2500de3-8df2-3cf5-b13f-27a8113db359 | -13.8752 | -54.1153 | 2026-08-30 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 4f5da779-3658-3798-a341-9830be23cc2b | -12.3811 | -48.1877 | 2026-08-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| c460ea71-d4c3-30a7-8c92-6bf0ea834c65 | -6.8568 | -59.4757 | 2026-08-30 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 272.5 |
| 3913d6eb-f37f-3284-a5c3-a8aa57081926 | -13.8749 | -54.1361 | 2026-08-30 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 3704b9f5-0fc5-30d2-a24b-2ffc3f765f03 | -5.871 | -57.7715 | 2026-08-30 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 3bffe40c-7b62-367d-aae1-9d8fb6db69ed | -3.6216 | -60.547 | 2026-08-30 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d3fd8167-d907-3b60-a9a8-34a8148115ab | -14.7605 | -48.7245 | 2026-08-30 13:50:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| cfec672b-249c-3ba5-bffa-0d13e980941b | -11.2314 | -54.0164 | 2026-08-30 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 187.4 |
| 21c81092-c358-3f62-89d0-d4e2e1334129 | -10.8653 | -50.2203 | 2026-08-30 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 51238a2d-b993-33e4-9852-bed4808928b2 | -5.4876 | -57.1416 | 2026-08-30 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 3ac5607f-df9d-348a-a90b-d00fc2afaaf3 | -14.4004 | -52.5438 | 2026-08-30 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 780c8876-271d-375a-9039-a5d0db412e9d | -7.9907 | -46.5177 | 2026-08-30 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 244.6 |
| 51eac772-84d3-3619-a6c5-ae1a21f0be43 | -10.1538 | -45.6982 | 2026-08-30 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 119.4 |
| c1e21c6d-beb9-3d8d-9bc5-ac6170ab2ae6 | -7.495 | -55.3262 | 2026-08-30 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 21d3297f-1ff9-34bc-9624-3feea238be4a | -7.9838 | -45.5072 | 2026-08-30 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 840cc916-45be-3877-a325-b825221941d2 | -4.9604 | -55.8424 | 2026-08-30 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 345.0 |
| 25057557-fa37-331d-a249-5e96b64bb014 | -11.1534 | -51.296 | 2026-08-30 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| e1077e91-1254-32e9-821b-5d94810943ce | -11.2485 | -45.0963 | 2026-08-30 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4362e271-76fd-37ff-8127-c4fdea11f71f | -11.2294 | -45.099 | 2026-08-30 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 957b8f05-4b3f-37e3-9b09-ae9b8a209c4f | -10.7839 | -50.6346 | 2026-08-30 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 9763115b-03b8-31db-a739-159e7896ca85 | -8.5969 | -54.7755 | 2026-08-30 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 199.7 |
| 65701891-3b35-35ff-bbd5-d41f063e01e4 | -11.2503 | -54.0146 | 2026-08-30 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 651d473d-0c7b-3088-a7cd-6726cb65ff28 | -10.8463 | -50.2224 | 2026-08-30 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 01db698f-7687-3eea-8f1e-d2282664d0ae | -6.8613 | -41.6532 | 2026-08-30 13:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 272.5 |
| e9ce5d96-cb52-3b83-a52a-47d79d9b858e | -5.7197 | -52.28 | 2026-08-30 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 177884c7-2fa1-31f2-8b41-bd3d19bd70d3 | -8.1531 | -45.5131 | 2026-08-30 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 9a49296a-0365-37d7-9d46-60b51f730bc5 | -14.1649 | -52.8058 | 2026-08-30 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 4813d14f-778b-3ac6-96e6-2b0cfa7679b6 | -15.5576 | -56.2938 | 2026-08-30 13:50:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e90a0032-038e-3253-96d7-0eebd3149e50 | -6.7699 | -55.6644 | 2026-08-30 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4d0886a3-edb8-3b54-94f8-03328c11e5d3 | -10.8253 | -45.3152 | 2026-08-30 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 84b6bd29-e913-37de-8142-7f19486a3f87 | -8.6154 | -54.7945 | 2026-08-30 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 188.6 |
| f4c9c4c9-3c68-3bb2-b2b3-e40acad77db7 | -11.0627 | -47.1385 | 2026-08-30 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 67df27ce-f18c-39a4-9cbb-d2565411a0ec | -8.1534 | -45.4904 | 2026-08-30 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 97b41554-33c5-359b-bcce-12556e20de43 | -14.4387 | -52.56 | 2026-08-30 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 42cf0aa7-bd41-3ce9-b2bc-763fdefa49d4 | -6.0 | -45.0889 | 2026-08-30 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 9f7d985c-4a73-36e0-9ab5-e9fb97fca91e | -10.7407 | -54.0401 | 2026-08-30 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| a236fe2b-286d-36d1-8c12-55bad278f3ba | -13.8557 | -54.1383 | 2026-08-30 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 33cda6a3-0e90-38e6-9d82-9c900be4beb2 | -6.8799 | -41.6754 | 2026-08-30 13:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 4a2345c5-4cd2-3b04-a526-a57c445305cf | -8.1348 | -45.4696 | 2026-08-30 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ab8c1339-4ba6-38bb-ab59-fcfdb9969b17 | -6.8569 | -59.4564 | 2026-08-30 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 57ff4fb1-574f-33d0-b9eb-8d167d37f006 | -7.0434 | -42.21 | 2026-08-30 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| b5ee8965-5d5a-3d5e-a3ed-5834b82d7244 | -9.8927 | -60.2752 | 2026-08-30 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 94780562-fd26-39e9-9c25-6ad0af71b131 | -8.5968 | -54.7957 | 2026-08-30 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| f8674ecd-5b47-36ff-9aae-8bdbeee20d78 | -13.6422 | -51.856 | 2026-08-30 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 852d066a-1892-3ac8-bc8e-93e6ee2e9a3d | -11.3619 | -45.1724 | 2026-08-30 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 953b9261-32fa-3e42-807c-727b14799d2b | -10.8249 | -45.3382 | 2026-08-30 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| f04c0a71-5578-3c3e-88f8-88df6394967b | -7.546 | -44.3395 | 2026-08-30 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 76b95c2c-e91d-33c9-bd11-cdee8a0e9988 | -7.5644 | -49.5857 | 2026-08-30 13:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b30b8ada-eae0-3870-8c7a-4f13a673b769 | -13.8381 | -54.0365 | 2026-08-30 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 900a5a0b-9520-3b15-af47-b4a63a9ed96c | -6.8753 | -59.4557 | 2026-08-30 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 15264063-a4d8-338a-b62c-e868237d6df0 | -9.7832 | -46.4202 | 2026-08-30 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 74221bde-85b8-3c19-8e18-de99d82267c5 | -11.1441 | -50.5961 | 2026-08-30 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 1db0dc9e-bc9b-370b-afcf-3710fdc96f3e | -6.9546 | -55.7147 | 2026-08-30 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a637e504-5ecd-3af1-8720-d6ee72effdc3 | -8.6158 | -54.7541 | 2026-08-30 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 8013cb92-0c3d-3b66-b4eb-580463fc79bf | -8.739 | -45.3844 | 2026-08-30 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bc0b2b9b-ffc9-37bf-99b1-a5179b5297f1 | -14.2989 | -51.7072 | 2026-08-30 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |


[Clique aqui para ver as próximas entradas](README82.md)
