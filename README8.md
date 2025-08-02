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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 619d5291-d9b1-3058-a607-84dc52fdf56f | -5.5742 | -43.59716 | 2025-08-02 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27fb04dd-086f-3cf4-aabb-4a697133371d | -8.44364 | -47.48349 | 2025-08-02 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8190801a-ff55-36c9-88c6-97f69cdfb3b5 | -3.51318 | -47.22096 | 2025-08-02 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c226e09d-d1bc-34dc-9a2b-15df301b9e22 | -8.38188 | -44.03023 | 2025-08-02 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8a6d9cd-624f-347b-a029-a5d456550437 | -8.43967 | -47.47652 | 2025-08-02 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f1582c3-5641-3eeb-961c-28b960097a8d | -4.77359 | -45.33736 | 2025-08-02 03:53:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e172b93-3da4-32f9-a2c6-208a05f159eb | -5.65871 | -42.57888 | 2025-08-02 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a82d66ce-b003-32cd-b496-738a24513683 | -5.56889 | -43.60375 | 2025-08-02 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 0377f007-07a3-39df-b471-f163d3af35c0 | -8.03227 | -43.11721 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 01a9514f-dd21-3546-80d0-13a403c1aecb | -3.58132 | -47.51862 | 2025-08-02 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 049a64ce-9f8f-395e-b58b-9e669a3fe56e | -4.0878 | -39.8264 | 2025-08-02 03:53:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 29135abc-78f2-3091-8a4f-43c564064b85 | -7.5789 | -44.80658 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 075f30ce-f2be-3633-96b4-74933cadb750 | -6.68367 | -44.35439 | 2025-08-02 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a74aa2b2-9e61-3f0b-963c-86acf31f2bdc | -6.69589 | -43.0708 | 2025-08-02 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f6301857-08d9-3c80-a0da-230922606628 | -5.74241 | -39.76849 | 2025-08-02 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d43aa8fa-75c0-372f-a18b-66eb1aeb4231 | -9.16539 | -40.59694 | 2025-08-02 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f8edc389-b11f-3e6e-8586-1d768aaec00e | -6.53109 | -42.80821 | 2025-08-02 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11e06353-57fa-3a92-828f-c1b63f01d3a8 | -7.87821 | -45.53974 | 2025-08-02 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b3f964b4-1382-3c87-9442-adb3b6d9f6d7 | -7.80755 | -44.92065 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69adc1a7-a438-3acf-ad2a-f735ba25112d | -5.69053 | -38.92483 | 2025-08-02 03:53:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 29c4ac83-192b-3044-bc32-af197ba65e60 | -7.28887 | -43.06134 | 2025-08-02 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67f47ee3-a47e-3011-ab99-7ee1d6a79569 | -8.0353 | -43.12263 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 2b8a7fe0-300d-39f8-bfe2-faa1309fb80d | -8.02601 | -43.1309 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f7034b26-b0d8-3164-8713-3f26b18b6bbc | -5.00217 | -38.6804 | 2025-08-02 03:53:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 65fe9bad-0735-376f-83f0-981f2c231b96 | -7.74951 | -45.13177 | 2025-08-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b91a8828-aaa6-3478-8250-5b0606dbcf32 | -8.38128 | -44.03381 | 2025-08-02 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60680cc6-2f45-3b39-9ab1-26460f78e0b3 | -8.03065 | -43.12677 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 38393733-5064-3251-a1aa-ac4357975c2b | -6.52642 | -42.81244 | 2025-08-02 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3447b7d7-0e11-3461-9faf-79222a3cf9ae | -7.56957 | -44.8093 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c1550fe-610d-3b2d-92c0-a4f111dcb4df | -7.57273 | -44.45924 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e217421-a1da-3e4b-8d62-54d3f93b66cf | -3.51137 | -47.22174 | 2025-08-02 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| da668b67-1197-3ad4-8d0f-86fa851d3958 | -6.56416 | -43.91164 | 2025-08-02 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 332f127e-02d5-312f-bf87-d221657374de | -5.74183 | -39.77209 | 2025-08-02 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| da9805ba-ea43-3001-a077-b4b63a7e1c66 | -4.22802 | -41.1497 | 2025-08-02 03:53:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1ddf5b03-80ef-3aba-84d5-08d88c0ce79b | -6.66408 | -44.74417 | 2025-08-02 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11f9f9d3-4632-36e7-9cc5-fcfe8bdebabc | -5.00162 | -38.68386 | 2025-08-02 03:53:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4c84da24-d40c-3878-adc3-cd690386f97b | -7.60426 | -44.80124 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d86443a9-834a-37c1-9d81-9a12c5087ed3 | -3.58082 | -47.5179 | 2025-08-02 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e20c319-5e63-396b-886e-4217e5860848 | -7.54309 | -44.40267 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 343101b6-e958-39df-8203-39b97bd7e96c | -8.03146 | -43.12199 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| c5e015fa-dd3c-3dac-8ebb-41e07385612f | -6.88474 | -38.97991 | 2025-08-02 03:53:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3d6a11ba-5206-389d-8527-e71547b5b649 | -6.79002 | -42.98601 | 2025-08-02 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| deb8b2b7-5ee7-3be0-b448-b252ba2c31f1 | -3.51735 | -47.21934 | 2025-08-02 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56333d9b-c7ec-3682-aa5f-2b4d1d492db1 | -7.74367 | -45.13956 | 2025-08-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a401c3ee-9b07-3119-b0a1-825aa3b9063d | -3.40566 | -43.01233 | 2025-08-02 03:53:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1642a6a7-531c-3f3d-8664-fa1f83a7c25f | -7.74215 | -45.14853 | 2025-08-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e74c91a-8b0d-34d4-b65c-a3a2c130ff01 | -7.58252 | -44.81133 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e89a407f-8fe9-3cfa-8e12-3723da31d738 | -7.54728 | -44.40341 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc6482c8-f87e-3915-837c-16207fe05121 | -9.16597 | -40.59331 | 2025-08-02 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 72943206-42ae-339c-8b93-e92daf9e92c9 | -3.51377 | -47.21754 | 2025-08-02 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c8f84378-bd40-3431-9bfb-bd22afee4239 | -6.69893 | -43.07648 | 2025-08-02 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a78d1be5-69e8-3b03-b8bc-dfb40a1088a4 | -7.74878 | -45.13607 | 2025-08-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe380095-9a11-37fe-9d04-17ae77564a3f | -6.69978 | -43.0715 | 2025-08-02 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d5de0e2-c5f9-323c-b71c-a8b85b93e725 | -6.88525 | -40.87858 | 2025-08-02 03:53:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 58f38a8f-b688-3390-9d98-fec3e6239307 | -5.5695 | -43.6001 | 2025-08-02 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e856066f-d828-3ec7-babd-24f212fcc48c | -6.7655 | -36.98577 | 2025-08-02 03:53:00 | NOAA-20 | VÁRZEA | PARAÍBA | Brasil | 2517100 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d7f22cbc-7acc-340d-9083-b9a23d72d8f5 | -3.51794 | -47.21576 | 2025-08-02 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ef187d1-3130-3bff-9a9e-1a73d604cad1 | -3.58361 | -41.65379 | 2025-08-02 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca3211ea-e5c7-353f-9f0a-487c48ad560f | -3.43232 | -48.95445 | 2025-08-02 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e9bd451-8741-3bf1-b1fa-56cc268df3d5 | -6.5256 | -42.81728 | 2025-08-02 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eec131d0-2b08-3390-bdfb-27a044ea529e | -7.29152 | -46.03666 | 2025-08-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 220bd6ac-941d-3394-a190-e78e955e50a9 | -7.2425 | -43.38486 | 2025-08-02 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a91cd6c0-b581-3852-b06f-44fecff786bb | -6.69505 | -43.0738 | 2025-08-02 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7de33751-f176-3243-9e13-ec8a860933a8 | -3.58735 | -41.6544 | 2025-08-02 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4fb657ff-583d-3fed-9f00-166e75f5208a | -8.04921 | -43.11026 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 762ec2b8-1309-3dc3-b7ce-e9ac7ebdb851 | -8.02984 | -43.13155 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8e846da7-e38e-3e3e-b629-3410a339d901 | -6.41664 | -41.1286 | 2025-08-02 03:53:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 81d17746-3039-3132-824e-643a417e0b47 | -5.91169 | -45.58651 | 2025-08-02 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8179987-b2b2-3275-a10b-49738bb5ee56 | -8.50109 | -37.94439 | 2025-08-02 03:53:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e096aabb-069f-31c2-ac24-3a2ee5c6bebc | -7.57251 | -44.81811 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65a571c7-e725-3d85-84d3-ada899752ddb | -7.74515 | -45.13082 | 2025-08-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c63a6fe-4238-3186-a703-68d451fe2cc0 | -5.6525 | -42.5927 | 2025-08-02 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7ac9dd1d-65fc-329e-aa40-f26f1ad00caf | -3.59182 | -41.65052 | 2025-08-02 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4a071fbf-f0ae-36f9-937d-2575ef1f2a72 | -5.91256 | -45.58138 | 2025-08-02 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9ed5a5f-6e4a-30e8-aa97-87166795832c | -4.25434 | -38.12408 | 2025-08-02 03:53:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9de62f24-1846-3efa-abcc-3451655a9254 | -7.22123 | -43.78238 | 2025-08-02 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b036944c-af9c-3aa4-ac0f-71421d4d2789 | -8.44309 | -47.48649 | 2025-08-02 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a34b8e31-0286-3060-87bd-48a4e460243f | -7.87898 | -45.53524 | 2025-08-02 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f427ec62-bee6-3052-93b8-67ebe58f9043 | -3.58192 | -47.51498 | 2025-08-02 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 246ba8dc-1fb2-3310-b0b0-76f83a0bffe2 | -8.59305 | -45.50368 | 2025-08-02 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9e158d0-568a-34a6-b14e-67e415ea6074 | -8.04538 | -43.1096 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 4a993ddd-f193-378e-90df-24f01bc1b93f | -3.99523 | -43.23104 | 2025-08-02 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6773832-cd66-329a-9c72-0acddee00747 | -5.56827 | -43.60743 | 2025-08-02 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| dd2c73cf-ffcb-3767-b708-90a57be5e5f3 | -6.52419 | -42.81492 | 2025-08-02 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| febb0bbe-7c06-3be3-bf22-658ad5307e6d | -3.59864 | -44.79623 | 2025-08-02 03:53:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a18ac04e-8814-318e-bec0-d77c0828f35c | -5.15114 | -37.73546 | 2025-08-02 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 40ec5012-81a5-38c9-9e1e-8dfbd6414cc3 | -7.74803 | -45.14047 | 2025-08-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40bd7725-81a1-356b-86d5-e9e8254dc8b7 | -7.29497 | -46.03553 | 2025-08-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67c782bb-39e2-366a-b806-25cd8c711726 | -7.28583 | -43.05583 | 2025-08-02 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1f8d43f5-06e0-38c3-a595-1aaede80422d | -6.69504 | -43.07581 | 2025-08-02 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80dc96ab-393c-3044-8eea-0c5fabe1aa9f | -8.44133 | -47.47832 | 2025-08-02 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a00c2f8a-aa4c-310d-ad2e-a1142bba27e2 | -5.57359 | -43.60082 | 2025-08-02 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22519539-bc3e-3292-9beb-aa90bf4c4f28 | -7.68887 | -45.11664 | 2025-08-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bad03df9-4863-3f32-aa4d-3092db616827 | -5.06946 | -37.71569 | 2025-08-02 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e377cb3-da85-3de9-8aaa-60aa26794ba1 | -5.48338 | -42.1577 | 2025-08-02 03:53:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6fdf53c0-28d6-319d-bd4a-5ef61ed42c09 | -7.57027 | -44.80521 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5879a904-05a8-3193-a828-d19a4c43c7aa | -3.43155 | -48.95905 | 2025-08-02 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72e9ab30-69a5-39fe-b3aa-c4fb1ab0d28b | -6.66625 | -44.73158 | 2025-08-02 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4877b966-121e-3ace-8ceb-30047324e58d | -7.26926 | -43.39455 | 2025-08-02 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da65bae9-fcd7-3c89-92b7-916e55662c29 | -4.26831 | -40.85673 | 2025-08-02 03:53:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README9.md)
