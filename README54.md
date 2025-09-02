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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 155f01bc-4f30-38ff-a03b-924f9d7989a1 | -7.87634 | -47.96456 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96514490-070e-36f2-92fa-87b3434a7525 | -8.34631 | -52.53924 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b72f54df-1fa8-3ccb-8219-fdf920bc6459 | -7.81499 | -52.14631 | 2025-09-02 05:04:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9545ffe1-cf4a-3986-8394-863cdaa520a7 | -4.1293 | -54.89768 | 2025-09-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 177a3f01-185a-37c0-a474-b29d3b1fbf0d | -6.82936 | -52.80783 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7a3c44e-447a-33e4-b8d4-a2c417bf3f7b | -7.72544 | -50.25548 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c00e5613-260f-3d6d-8bf0-0aae20e1e687 | -5.49298 | -51.16898 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d840e51-ee74-3b8c-a794-fd581ca6b686 | -5.8498 | -43.01192 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 136eaa4a-8b7d-37b4-9abd-8751e0f0f24a | -7.63243 | -46.55481 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a744f7f2-02cd-334a-9180-200d5666b98b | -6.81898 | -52.8277 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0cafef77-9621-3f9b-9641-fb665e2ac11d | -5.6939 | -45.9501 | 2025-09-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c53382e-8608-37e3-80d2-0c3e8824e74c | -4.31056 | -48.09939 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9eb6923-47c3-33e7-bfb0-b8e799861cc5 | -6.79855 | -52.81602 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ec21eff-e378-3b94-acbd-3ee210421ca7 | -8.13685 | -49.82835 | 2025-09-02 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b740c50f-1b4a-30c0-8186-1e311649e195 | -6.99448 | -43.22599 | 2025-09-02 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 70fb0da9-0056-3dd3-9350-bf7a8f4b2980 | -6.20192 | -45.39706 | 2025-09-02 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 269f03e7-6f5e-378d-87ce-def0a0d4e688 | -6.80278 | -52.81245 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 76228656-873b-38cf-9693-5e9b37c94690 | -3.40728 | -52.66701 | 2025-09-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 627fe18c-7d51-3c6a-b86e-89e8ab9c7d4b | -4.47948 | -48.11172 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1a84625-de07-30ce-9a68-8782282e3659 | -7.9282 | -46.44785 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90e028b5-42aa-31fd-87b9-56508be9e521 | -8.05136 | -52.35815 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f87d4157-0058-3010-ab18-a0768600d9e7 | -4.48347 | -48.1175 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2640342-880e-3e59-845e-33ef262fa670 | -7.70928 | -50.3077 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b6f08e9-9006-30db-ad4c-d72bc2182973 | -8.20404 | -49.52595 | 2025-09-02 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea7171e3-9e69-395c-93b4-05d675637961 | -5.69487 | -45.95378 | 2025-09-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac488860-19cd-3a82-8ce3-9769fda0a412 | -5.00879 | -47.64383 | 2025-09-02 05:04:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01dd8dae-d1ce-3351-ac3c-2619e65002bc | -2.2581 | -47.8476 | 2025-09-02 05:04:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29f5001d-14df-3667-bde4-6b8b17b44ef0 | -6.06821 | -45.58578 | 2025-09-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46ad9271-8201-3219-8aa4-3e236b054c1d | -8.87653 | -45.76667 | 2025-09-02 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9d69e10-eb49-328d-9fad-fad8ae05a8aa | -9.28467 | -47.08422 | 2025-09-02 05:04:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54fcb9a3-c2a8-3f21-a2dd-f8ba56a5c8c9 | -6.79618 | -52.80711 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc85bdd7-bf84-30b2-a09e-ab81147702d5 | -5.1175 | -43.22512 | 2025-09-02 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c1d384a-d1da-3256-8cd0-f643eaae1c54 | -8.70966 | -50.43177 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 903d7f68-5e9f-3b9b-aa75-cbc64fe5ffe5 | -8.35577 | -52.52678 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81e3934c-fc6c-39a0-8f78-f1a0db13f8dc | -6.34513 | -53.42749 | 2025-09-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bc47cba-6661-316b-b0db-37adddc8abd8 | -5.1521 | -44.84464 | 2025-09-02 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb128594-4c9a-333d-8cfc-99737c673839 | -8.70091 | -50.4448 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a1ad08b-604d-32e0-bcfe-7abefd3da6d4 | -7.94124 | -46.43537 | 2025-09-02 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8de645cb-9d87-3610-8232-2da0febfa5dd | -6.99108 | -43.23016 | 2025-09-02 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 18c60436-aba1-3434-a8a0-e7c280870670 | -6.48024 | -56.00986 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faa210ba-2c7f-36d3-b881-a1577f0d68f5 | -7.79402 | -45.45614 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99c19d1c-25f1-37f2-802d-0a74b302d1bd | -8.05202 | -52.3536 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e40961e3-b732-3799-a78c-34b05a01d842 | -6.84915 | -52.82372 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71116664-2c50-3acf-b991-a2852c92c26d | -5.00964 | -47.65009 | 2025-09-02 05:04:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36470643-343e-3068-8601-2ea913397add | -6.83597 | -52.81308 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ed3b212-3998-3451-acaa-7e3a1b962af9 | -6.88829 | -45.84798 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e030fb7-9b30-38d3-9403-cad7acf8021b | -8.87488 | -45.77954 | 2025-09-02 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c6cac52-2eac-31a5-84ec-9ba37383871f | -7.87089 | -47.96677 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53b442e3-c9f3-3ca1-9d55-ed03926b5de5 | -8.46808 | -47.37181 | 2025-09-02 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa533d6d-7c95-379e-b880-be917175d246 | -7.63286 | -46.55284 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5097f0e4-1574-3059-b4d5-e383e30f1a50 | -6.83533 | -52.81729 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f88fc37-50b2-3b50-a067-7989fce37f09 | -6.79317 | -52.80246 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b9285f1-1443-3049-a28f-524a60a699eb | -4.90986 | -43.19304 | 2025-09-02 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 159d7924-761f-38eb-91a6-67e1be73ca31 | -6.2012 | -45.39843 | 2025-09-02 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c305db8b-2f2a-3d02-9726-16854cc9db27 | -7.77739 | -45.44481 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e297a25d-feb6-341d-a7d4-ee71415e22c2 | -6.98473 | -44.34161 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e89bab6b-9a05-367e-b734-95c9701dcada | -7.5832 | -45.21347 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3240acd3-4445-3cf6-bf58-3b3f20163b4e | -7.11149 | -44.76129 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2b3529e7-8898-3327-8902-c990a3baaae4 | -5.8561 | -46.61052 | 2025-09-02 05:04:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e954ac54-8b69-3fe2-afd5-cde81ce71dfb | -6.78831 | -52.81031 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ca797038-ea56-3efa-8550-5aa290c776e1 | -4.47874 | -48.11676 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22c2277e-1dc7-3752-8812-235ddce1e884 | -6.85956 | -52.80395 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 647b4e25-d3d8-3c6f-8cbf-d227a17ff26b | -4.29736 | -46.26372 | 2025-09-02 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 112bee1d-2a4e-3e6e-9eda-2aa59642f479 | -7.60835 | -46.03622 | 2025-09-02 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 56fd5a1c-ca44-3dd5-a320-3a76f87bf666 | -5.11819 | -43.22927 | 2025-09-02 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d5b6351-89c5-3a1b-9ca3-b41392b7fa15 | -6.27512 | -44.51616 | 2025-09-02 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 90be915b-db88-3ae8-9a9c-105e997867be | -6.82323 | -52.82401 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fc41697-535f-33f7-a876-e2f150625dc4 | -7.28176 | -60.65657 | 2025-09-02 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ba0c1a2-481d-33e6-bd75-1ef22882f996 | -7.72976 | -50.25586 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b50da010-857b-3442-a801-db34c1987639 | -7.27788 | -60.65593 | 2025-09-02 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 668bc8e5-088c-3c42-a65c-9627a2b7aced | -7.71624 | -50.25864 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa7109b1-0b3e-33ae-8660-8386fee0428c | -5.31948 | -55.88231 | 2025-09-02 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 237f4326-0b51-38ac-9bfa-09ac3edbc601 | -8.46764 | -47.37508 | 2025-09-02 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 130736c9-e32c-3855-8ecf-00194667ca96 | -6.87687 | -45.84616 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc9e357c-95d8-332e-b1d8-b22298305cbe | -6.78108 | -52.80917 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 263e1f99-cc43-3886-9bec-2fc7da8e9cb4 | -7.78686 | -45.44695 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38a2fe84-3fa0-3e45-b515-d8dc317fdf3c | -7.28483 | -60.66209 | 2025-09-02 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a507eaff-9931-3c64-bf85-e5eef8cd1a3d | -7.98574 | -46.47598 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd15e37e-b4f3-3797-87af-eaa820ea13d7 | -4.30583 | -48.09868 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcb973a5-844b-3148-8bfa-6bbfa5aefc65 | -6.8432 | -52.8142 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a35093f-7a80-3106-a079-bb0945497b3e | -8.85503 | -45.79376 | 2025-09-02 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 866c4a65-dfee-398d-a239-addbe0ef0c45 | -8.85721 | -50.58836 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 610de8bf-6770-3f65-8c16-837bb69c4665 | -6.34129 | -58.18224 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b27db16-276e-368c-9f4d-9a1638890d87 | -6.43601 | -55.617 | 2025-09-02 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 131e5652-83f4-32d2-838e-9c5d34bdb143 | -7.55939 | -45.6992 | 2025-09-02 05:04:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a694b8a-c9aa-3a38-bf5d-36b54da3bee3 | -6.85213 | -52.82847 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d22aebad-1f5d-3537-aa6c-07fff6e0f0f8 | -7.71791 | -49.57998 | 2025-09-02 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f556bd6f-3daf-32e2-aaba-b8ff4afe544d | -6.813 | -52.81828 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 30b858b7-757a-3cf8-90f2-f71a1796baa7 | -6.7221 | -42.26406 | 2025-09-02 05:04:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 50ec23fb-2761-3582-87ba-3b6768b629c2 | -8.13304 | -45.03297 | 2025-09-02 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b86560bd-17d7-3937-9882-3606f23aab7d | -7.6999 | -50.28147 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dea24907-89e7-33c4-9ac2-4d786c6fabae | -7.63745 | -46.55919 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cf74ac3-85dc-3f14-9dc8-8c5340189020 | -6.82748 | -52.82035 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed2d309e-b291-3a6c-9be0-2b6bcd5b3b5c | -6.33498 | -58.17734 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f41c075-0489-31f3-8ec4-55dd2df84e73 | -7.99229 | -46.46935 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f557a63a-aa29-3652-b379-f4f0648731fe | -6.77386 | -52.80801 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92ab1a93-562e-35fc-913a-070207b51eef | -6.84193 | -52.82258 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7a13c6f-2a94-39d7-b9cc-045fb717db21 | -6.34338 | -53.43919 | 2025-09-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af81d6bc-c700-3842-96c2-09936597e9af | -6.80515 | -52.82132 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48aff300-d75a-3489-9d14-ceaf1cd38a12 | -6.85426 | -52.7972 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README55.md)
