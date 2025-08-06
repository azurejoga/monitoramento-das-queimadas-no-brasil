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
| 8fe1ec32-c8cc-38a3-b1c4-ecfa9bd898b4 | -12.40731 | -44.702 | 2025-08-06 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91d7770a-9fe1-31b9-a8c0-ec156d74f86a | -8.51471 | -44.74556 | 2025-08-06 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3af6922-e5f1-347d-a4b4-2877e88134cb | -13.00122 | -44.90099 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69665264-82eb-3fa5-97a1-160e76762866 | -12.71853 | -48.0806 | 2025-08-06 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca4522ea-3e16-3d81-b119-0a3eaad9625f | -8.37698 | -45.80049 | 2025-08-06 03:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c9cdfc6-303a-356f-bdaf-ad3be5c14c7c | -12.53924 | -47.17269 | 2025-08-06 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c3fed62-5329-3253-b532-4940e7ef6448 | -12.73141 | -46.39167 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec0bd35f-0c73-3b3b-b7cd-b96c8645f9dd | -11.76163 | -47.53458 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2d47d29-bf8a-3626-949a-c577e4f96373 | -11.75374 | -44.95945 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d6e5632-c694-3a7a-9b11-bad74d1e2d97 | -12.9972 | -44.90019 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 352ba811-2540-36ee-a493-010e3446495f | -11.43302 | -45.13222 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 6d609529-209e-3f2b-a1a0-f859e854143e | -9.70207 | -51.94977 | 2025-08-06 03:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35064a60-f741-3f70-9622-723399fb0707 | -10.47146 | -44.38731 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 210bac5a-933b-31d3-a81c-e0e3496bb53b | -12.52973 | -47.17128 | 2025-08-06 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f145ebe-878d-34d3-ae8c-b12680826eec | -12.97473 | -44.8841 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 911a7ebd-f0d1-35f6-a7cd-f026434ea08f | -11.75667 | -45.0157 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99cb25e5-e40d-3085-9528-bd18608b8c0f | -16.25424 | -39.04857 | 2025-08-06 03:57:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 5cb7dcb1-4b0a-3cc9-9581-39598a15add6 | -10.46675 | -44.39038 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 858d1153-8085-37bb-8679-2edd25c955f7 | -12.99023 | -44.89062 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70d7cc96-f9bf-3081-9e4d-0f5027e83cf9 | -8.83654 | -47.62069 | 2025-08-06 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83ee1150-6661-3e01-8a33-d9ffa9716a0a | -9.55261 | -40.32671 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eaacbd49-8117-3112-86aa-a59f94d5fc0d | -15.12101 | -47.43477 | 2025-08-06 03:57:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7e357f81-b382-3246-80bb-d18991927990 | -12.52499 | -47.17048 | 2025-08-06 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b56ba810-7ecd-32c1-b8a5-8ba3c0debb22 | -11.91828 | -44.94175 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46ccabb9-68d7-3196-8cf5-74a316c759df | -13.29716 | -39.86448 | 2025-08-06 03:57:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a1971d59-f2da-3b91-8abe-b5b79f18caf1 | -9.54982 | -40.32253 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0fc19bd9-d61b-3dad-8415-1536d6e7fabe | -8.53076 | -47.4701 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26f08916-2112-3a83-a8a0-4e091c0c586a | -12.72845 | -48.08291 | 2025-08-06 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b531213e-bf09-3a48-bb52-372b48516981 | -12.72904 | -46.39223 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64a6b932-2448-3621-bfcb-4fd6a4adeccf | -8.52312 | -47.44943 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66f4af1e-3be1-3b5d-857e-88237f746705 | -12.71799 | -46.38932 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 064c0cda-1b10-3f1d-8ca1-927786a3aecd | -12.76024 | -44.41562 | 2025-08-06 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45cb98f6-3c48-3cd9-9f04-fd451531e8a5 | -12.03844 | -44.01658 | 2025-08-06 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 753f6cb3-c1ef-363f-b574-804b56b6641f | -9.35806 | -40.33975 | 2025-08-06 03:57:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce67e1df-5be5-30ab-a217-c83b38542f4d | -9.6961 | -48.87534 | 2025-08-06 03:57:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5302e420-6e09-3713-9acc-40b1d8ca32fc | -12.99086 | -44.887 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9550b12-ea2b-35cb-bd5e-dd7b425f2d88 | -10.46342 | -44.3367 | 2025-08-06 03:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a110916c-34f3-39a7-8439-63d1561fd1b0 | -12.73588 | -46.39245 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d00350c7-30da-3ea7-b80b-9355410b899c | -11.91221 | -44.95181 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82c2f537-b1ae-3ed0-a98b-001cd94f082b | -11.77246 | -44.97426 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0d63ba5-697b-3e3e-b58f-6be2242285db | -13.49485 | -47.73667 | 2025-08-06 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfb09cc7-6a3c-3872-b0fd-8d38e4853647 | -8.24264 | -45.06503 | 2025-08-06 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10a9ccbb-75a5-3dc7-b3d6-433d1adc6f2e | -8.06257 | -49.72086 | 2025-08-06 03:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dba7990a-78ad-35ea-bce2-16cd7bb020e9 | -11.89974 | -44.97375 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90478b5c-4a7b-3759-b4eb-47b76b197a89 | -8.51258 | -43.31781 | 2025-08-06 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9f512ab-c46d-3b58-8776-b5e1f2db7491 | -11.84456 | -43.72284 | 2025-08-06 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6992d319-7991-3f58-afba-3d03e56003db | -13.00187 | -44.89741 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08747979-cf31-3a08-8e03-1c94d589ed76 | -12.71562 | -46.38986 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7c7dffe-e5c8-3673-84f1-72011d410bf4 | -11.48889 | -50.28768 | 2025-08-06 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7956bab6-79dc-3eba-a422-f4a6194c1d6b | -13.94072 | -54.06769 | 2025-08-06 03:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30775b14-d398-3ed0-a5ab-9b0852e6065f | -11.43985 | -45.14145 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 982392cf-4973-3f8a-b2b0-443b8979940e | -11.75881 | -47.52917 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a35317a7-ef48-3f7e-9872-950b62c3736d | -10.44019 | -44.37425 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5713d4c0-40ea-3036-8afa-143e99a231a2 | -11.90874 | -44.94751 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fd94eef-f65f-3574-bb1c-f3c53dd05b41 | -13.3717 | -43.75626 | 2025-08-06 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9cae7af-00ee-31b2-8493-c27bf004d4f1 | -11.44143 | -45.13371 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21cb6321-a825-3bb6-b8b2-37c4da19fd57 | -11.74282 | -44.99718 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eecb5cb3-fb0a-330e-a677-967cbfb4d87f | -11.76081 | -45.01648 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 311b5ed6-fcf3-3d7e-92df-95b7d4cbc795 | -14.34171 | -43.65806 | 2025-08-06 03:57:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2fe2fdc-a5f3-3a8f-97c3-62a9fa83473a | -11.90315 | -44.97845 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acce5d7c-e034-3c44-862c-00f1826cb96d | -9.69759 | -48.86752 | 2025-08-06 03:57:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8aab3937-e971-31c2-ab47-3de66f614a22 | -8.52558 | -47.46923 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 964fc9da-c8cd-3791-a7e5-e931adad124a | -10.1206 | -51.68143 | 2025-08-06 03:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd8d67e5-7d75-3bb9-9637-6f2d2d99478e | -11.90243 | -44.98241 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b38edb6-3163-30ef-9d6d-faa21a15e290 | -9.62279 | -43.85389 | 2025-08-06 03:57:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a1929567-7570-37b1-80f4-d756e849588b | -12.97536 | -44.88053 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64512cac-74a4-31d1-abb0-3c07854d54c9 | -11.91731 | -44.92354 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26fe544c-9c81-381e-9d3b-8a8f5730fcfd | -8.51341 | -43.31282 | 2025-08-06 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 007a3568-7abb-35b3-8ea7-79ab0d72b748 | -11.50651 | -50.29134 | 2025-08-06 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4fa87ba-1de7-3d1b-9dfa-64a0077910fd | -12.99514 | -44.88855 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 721e3e3e-b447-3ab1-a6dc-20b6f0375bb0 | -11.44072 | -45.13763 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdb986df-7fe7-34ed-81ba-9caf99c05c07 | -9.70312 | -48.86866 | 2025-08-06 03:57:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 924fa164-fc92-33eb-a2ad-a9e017576a03 | -12.72452 | -48.08168 | 2025-08-06 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e36800fd-58f3-399a-b826-3cdcd1e25d0a | -8.51748 | -43.31052 | 2025-08-06 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11bf2700-e8b7-39a1-b3b4-f958cd1ccd44 | -10.44149 | -44.36681 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e25a985-50b2-3f28-8600-86e2dfee1fb7 | -12.9707 | -44.88332 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7158526-1a59-3a44-8789-191c23eecb54 | -10.44685 | -44.36001 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ecbb6c5d-3164-3298-bc1c-894850345ca0 | -11.02923 | -45.06339 | 2025-08-06 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7adb887-fcab-3cf9-9786-ecf0b2d07a3b | -8.87903 | -44.79423 | 2025-08-06 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f78e285-a2d5-3391-8e28-893e04ea9f30 | -8.53017 | -47.47326 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71a10625-0b91-3a1c-9c2e-6c1bc1ab3c53 | -11.44491 | -45.13841 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9266f7e7-f75f-3d25-9ca7-4e0b84458f1c | -11.0375 | -47.61582 | 2025-08-06 03:57:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e056c19b-c887-3f07-b38d-70511929e4bb | -8.39243 | -45.79395 | 2025-08-06 03:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a27d283a-7c0d-3f6a-ba30-b18411387dbc | -12.52027 | -47.16961 | 2025-08-06 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4c62ac7-c830-3515-8e2c-34ef2e521820 | -12.72351 | -48.08162 | 2025-08-06 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d70a0b9e-0617-3e7b-b952-1d12a15a8537 | -12.02419 | -44.82104 | 2025-08-06 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7bd3caac-aa3e-3e1d-b518-3864e27f38bc | -11.76136 | -44.96456 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16bcbd43-99af-3dcd-8d17-65d3e798a497 | -8.83775 | -47.61845 | 2025-08-06 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a402041-7d20-30a0-b47b-d85c96a9d491 | -8.24705 | -45.06582 | 2025-08-06 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdad8382-ec4e-3b4c-8560-34b0d7cf4fc1 | -12.99425 | -44.89143 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54689497-0b9e-3b7d-a654-9baab7e65e39 | -16.2548 | -39.04483 | 2025-08-06 03:57:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 098cc405-5245-33ea-972d-46002cab7ca4 | -12.9985 | -44.89299 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f702f53c-6c0a-3b26-a23e-e4538f266632 | -11.90514 | -44.95504 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5123dd5b-ec7d-3228-89e5-892921d9ce05 | -11.91419 | -44.94086 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad6ef9d6-ec8b-3bd7-945f-158632fdde50 | -11.74357 | -45.0172 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0bf6eea-0868-39f3-9699-fe04cbc97dc5 | -10.43804 | -44.36255 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db53f463-917d-3f13-b765-d7b2d197a3a4 | -11.4244 | -45.13061 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e739336-4238-3829-b285-eb67c1ee8a2c | -11.91545 | -44.93384 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7af71ae-3526-398c-93ff-ff9537f9fb8f | -10.4374 | -44.36622 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fed6e6d9-975d-3260-85fa-94a66531c084 | -12.97133 | -44.87976 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README11.md)
