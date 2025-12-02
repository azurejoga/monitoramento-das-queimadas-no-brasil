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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e43b8589-94d5-320d-ba0d-2a8c63c18660 | -7.63297 | -37.65785 | 2025-12-02 11:36:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 13.0 |
| cb22c782-4ffe-34d4-9718-c7fa90962697 | -8.22464 | -37.78311 | 2025-12-02 11:36:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 17bf99e8-cc75-3fb0-bf8b-cc9916f753fd | -6.57011 | -37.86837 | 2025-12-02 11:36:00 | TERRA_M-M | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 6d2c22be-a2d3-3440-8f8b-5c8118bdb908 | -9.132 | -37.62671 | 2025-12-02 11:36:00 | TERRA_M-M | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 29862c35-4a22-36fa-863b-83173b5e081f | -9.13328 | -37.61742 | 2025-12-02 11:36:00 | TERRA_M-M | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 6a9478b0-1f20-345f-8b87-9c744a59c6b4 | -3.57792 | -40.34972 | 2025-12-02 11:36:00 | TERRA_M-M | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 2ae3fd6b-5bfa-36c4-b79e-b678c68fc2fb | -7.97309 | -38.64832 | 2025-12-02 11:36:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| dae2595a-2d79-3c00-921f-9ceaa7c9a597 | -5.18087 | -37.0674 | 2025-12-02 11:36:00 | TERRA_M-M | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 11.1 |
| a92165d7-1119-3728-814b-1f539abd82e6 | -6.18531 | -38.30795 | 2025-12-02 11:36:00 | TERRA_M-M | ÁGUA NOVA | RIO GRANDE DO NORTE | Brasil | 2400406 | 24 | 33 | nan | nan | nan | Caatinga | 9.6 |
| b6b24b7e-9679-3c3d-a0bf-1e300f979797 | -8.24899 | -37.5456 | 2025-12-02 11:36:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 14.2 |
| ad8549de-ed0a-37c4-97d8-4ddb0adfc894 | -3.46913 | -41.50433 | 2025-12-02 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f68653d0-7455-36cc-b731-0d20ce6b2146 | -5.17842 | -38.18781 | 2025-12-02 11:36:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| d308fa78-dd3d-3918-8070-6a87362ba58e | -6.14224 | -37.69669 | 2025-12-02 11:36:00 | TERRA_M-M | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 17.6 |
| d646126a-2cb9-3964-b30f-69fb6ffa1159 | -8.24771 | -37.55475 | 2025-12-02 11:36:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 34efd6d9-780f-350f-b4fa-e63c8de6474b | -7.97436 | -38.6395 | 2025-12-02 11:36:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 96da595a-1c82-3662-bc9f-f90954d53a96 | -8.39142 | -36.05851 | 2025-12-02 11:36:00 | TERRA_M-M | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| b75c9630-f12b-3295-9f3d-9d5fea7aa964 | -5.26402 | -37.13117 | 2025-12-02 11:36:00 | TERRA_M-M | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 4a865d27-e667-3854-a5f6-4368a5127c61 | -7.52167 | -37.85518 | 2025-12-02 11:36:00 | TERRA_M-M | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 226073bc-b599-3e4f-b9cc-7b978e45e0d0 | -7.0589 | -38.96149 | 2025-12-02 11:36:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6de90dd7-f4e1-358d-97ad-3fa7a2cf8fea | -6.97683 | -37.2173 | 2025-12-02 11:36:00 | TERRA_M-M | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 79015492-6b04-37d7-aafc-c5c4577a75a0 | -6.73012 | -38.61941 | 2025-12-02 11:36:00 | TERRA_M-M | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 5672c4ef-507f-3389-a185-f4e23c266b07 | -6.40969 | -38.40561 | 2025-12-02 11:36:00 | TERRA_M-M | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 34.0 |
| d37f9886-b5e0-3ebc-9f68-0d110172b11a | -7.8522 | -37.99871 | 2025-12-02 11:36:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 4aed26e2-7de3-3d27-9c21-3742cfe1ab7a | -4.94436 | -38.5918 | 2025-12-02 11:36:00 | TERRA_M-M | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 818762d9-1117-331d-86e6-87308a88dfa4 | -5.14145 | -38.50579 | 2025-12-02 11:36:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ec1b3f23-7683-3cff-92fe-446ae012f958 | -5.67242 | -35.59999 | 2025-12-02 11:36:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 77bc452b-3077-329f-a10f-d654ffc67672 | -6.49825 | -35.24424 | 2025-12-02 11:36:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 327e72ab-ed28-355b-b17b-93654eff6218 | -6.97259 | -38.09109 | 2025-12-02 11:36:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 10.5 |
| aa4a8819-2b75-36a1-bdba-4a772060227b | -6.40843 | -38.41439 | 2025-12-02 11:36:00 | TERRA_M-M | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7117ce31-32ec-3637-9ccb-2f615800ff67 | -8.035 | -38.27861 | 2025-12-02 11:36:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| d2b8b5cd-eb18-31ea-8b57-ae0b58f3bf4a | -6.67783 | -38.91884 | 2025-12-02 11:36:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 16.3 |
| b769604a-f345-33e4-8e0e-da0e88d34dc6 | -7.37572 | -38.94996 | 2025-12-02 11:36:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| dd239a48-8adf-3fae-9933-8445a45efcc7 | -7.21621 | -38.32354 | 2025-12-02 11:36:00 | TERRA_M-M | SÃO JOSÉ DE CAIANA | PARAÍBA | Brasil | 2514305 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b7f02a12-758f-3e56-89e8-fa2579a24764 | -7.1833 | -38.03375 | 2025-12-02 11:36:00 | TERRA_M-M | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 12.6 |
| b3628ad7-5959-36a9-a481-1ce39bb0f4ed | -6.14097 | -37.70555 | 2025-12-02 11:36:00 | TERRA_M-M | ALMINO AFONSO | RIO GRANDE DO NORTE | Brasil | 2400604 | 24 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 406a4a1f-0a9f-3b87-9ee1-ba941f0a9088 | -7.40279 | -39.19854 | 2025-12-02 11:36:00 | TERRA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| a668af78-51bd-3ace-beb2-23023a3fd884 | -6.60772 | -38.70374 | 2025-12-02 11:36:00 | TERRA_M-M | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 4d56acf5-6341-3bde-844a-478779ebf622 | -6.81831 | -38.77299 | 2025-12-02 11:36:00 | TERRA_M-M | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| bde8e606-ade6-3984-a63d-9e83025a15ce | -6.98849 | -38.87276 | 2025-12-02 11:36:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 22aee5bf-b255-317f-a9df-51b696878e25 | -6.97385 | -38.08227 | 2025-12-02 11:36:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 8bcbb0fd-f143-3199-b4db-10a6d6a3badb | -8.74266 | -40.38851 | 2025-12-02 11:36:00 | TERRA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 36ec84d7-84d3-3367-ab16-2ab2bc306f35 | -6.39101 | -38.09816 | 2025-12-02 11:36:00 | TERRA_M-M | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b1f9d6c0-58bc-36e4-b4b1-9be487038490 | -6.98267 | -38.0835 | 2025-12-02 11:36:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 81a86e8c-ccc1-36c1-991c-3a06fd0bf6e8 | -7.63426 | -37.64883 | 2025-12-02 11:36:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 434576a2-10ce-35f8-8318-c1d6e0ca8d94 | -7.92401 | -37.95163 | 2025-12-02 11:36:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a863a835-67ce-39bc-acca-3cc41da2fffc | -8.54492 | -37.14463 | 2025-12-02 11:36:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 2c511d92-7b6e-37d5-b569-2d78bb117b71 | -8.23876 | -37.55352 | 2025-12-02 11:36:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 47b1dd7a-0f56-378f-8b19-43b3d884831b | -7.33199 | -36.98368 | 2025-12-02 11:36:00 | TERRA_M-M | LIVRAMENTO | PARAÍBA | Brasil | 2508505 | 25 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 1d6f087c-8be7-31fc-b2dd-3b377e47db9c | -6.28226 | -38.58764 | 2025-12-02 11:36:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 603fa8da-b0a4-39a7-a9da-084c017fadc3 | -6.24452 | -37.83173 | 2025-12-02 11:36:00 | TERRA_M-M | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 25.1 |
| b4914450-6571-3695-9b98-d30272e0cec3 | -5.46252 | -36.83762 | 2025-12-02 11:36:00 | TERRA_M-M | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 2a3e7b34-58ce-3914-9452-b92e9a78f01d | -7.33331 | -36.9743 | 2025-12-02 11:36:00 | TERRA_M-M | LIVRAMENTO | PARAÍBA | Brasil | 2508505 | 25 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 992b8b1f-0ca3-3bfc-b03a-d76c918fba2c | -6.67912 | -38.90996 | 2025-12-02 11:36:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| e918346e-1e72-3922-8e1b-a2ab0b4a5ed0 | -7.52295 | -37.84624 | 2025-12-02 11:36:00 | TERRA_M-M | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 36.3 |
| c26f87c1-04e3-3b16-a5ae-805ecec6560f | -3.46729 | -41.51696 | 2025-12-02 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| cb352580-1bb9-3f30-8235-3f82988d06df | -6.81703 | -38.78183 | 2025-12-02 11:36:00 | TERRA_M-M | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| dffa6d02-5335-3018-bab3-9deed5def8a3 | -3.46072 | -42.34961 | 2025-12-02 11:36:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 4b4e58e8-4556-366e-98cd-c65effd0c0a6 | -10.4733 | -39.41476 | 2025-12-02 11:38:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 66a93e0e-8838-3d0f-ae6e-3b3829bc5b48 | -13.07944 | -40.71584 | 2025-12-02 11:38:00 | TERRA_M-M | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4980434f-5291-3f13-bf9a-81b77713a6f0 | -10.71137 | -39.55883 | 2025-12-02 11:38:00 | TERRA_M-M | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| b21fccf8-7863-3c9b-a05f-5590349895f3 | -10.41312 | -39.64312 | 2025-12-02 11:38:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 03efb97e-e5dc-3df0-b263-c7181fd0345a | -13.07278 | -40.13048 | 2025-12-02 11:38:00 | TERRA_M-M | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 40099cc3-49cd-3ce8-b4f8-d94abbee2444 | -14.10591 | -40.06649 | 2025-12-02 11:38:00 | TERRA_M-M | ITAGI | BAHIA | Brasil | 2915106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| c9b18d68-bf5f-31c4-8b71-fc139cab675c | -10.04433 | -39.70199 | 2025-12-02 11:38:00 | TERRA_M-M | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 42aa99fa-9211-34d8-ac91-964c9090775f | -10.47459 | -39.40585 | 2025-12-02 11:38:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| d05afe86-b296-390c-bbe7-d68beab36563 | -13.0808 | -40.70662 | 2025-12-02 11:38:00 | TERRA_M-M | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 527f98be-7e31-3f41-b782-84bf1e2131b8 | -19.03583 | -39.88173 | 2025-12-02 11:40:00 | TERRA_M-M | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 7ae7b658-c245-3d38-9c38-22379be105ff | -17.8003 | -39.62921 | 2025-12-02 11:40:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 33.4 |
| 238f5f8a-1cea-372a-b8e3-1aba4c122f15 | -19.01487 | -40.30182 | 2025-12-02 11:40:00 | TERRA_M-M | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| fa760ab0-53e8-3f9c-a5ad-26b9473ec2f0 | -18.84423 | -40.13856 | 2025-12-02 11:40:00 | TERRA_M-M | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 3d42250e-dbd5-3809-9f61-f8daf3ace62e | -17.6708 | -39.76192 | 2025-12-02 11:40:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b9cbad08-6244-381d-96f3-8236d74d4016 | -17.80927 | -39.63052 | 2025-12-02 11:40:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 4dea3e0f-4957-3f8c-8d48-fdfc99346a3e | -17.81057 | -39.62099 | 2025-12-02 11:40:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| fc1e7568-e692-38e3-9b1c-ff4d54bbc694 | -19.65033 | -40.23785 | 2025-12-02 11:40:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5988f914-b7e4-3a2c-b940-daee27a26fd3 | -19.81288 | -40.719 | 2025-12-02 11:42:00 | TERRA_M-M | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| af91d5bb-222e-38ce-9ea4-306d4ce379ef | -3.144 | -41.9894 | 2025-12-02 12:20:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| d15b3b35-d2b8-3b0b-b8c1-b8c0c67f7b3b | -3.1626 | -42.0123 | 2025-12-02 12:20:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 4a0cea17-38f5-3572-915c-1751c239e796 | -8.2424 | -37.5605 | 2025-12-02 12:40:00 | GOES-19 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 93.2 |
| dc37ce9f-8ed0-319c-a007-a6794f78f23a | -8.2424 | -37.5605 | 2025-12-02 12:50:00 | GOES-19 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 25983a74-08b8-3197-85b7-8c81b6ea74b8 | -8.2424 | -37.5605 | 2025-12-02 13:00:00 | GOES-19 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 121.8 |
| 7c80b087-0b10-3c82-9aa1-a34801180a70 | -8.2428 | -37.5343 | 2025-12-02 13:00:00 | GOES-19 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 108.6 |
| 8e3894dd-b5a9-3afd-8e73-93f3875ebdab | -8.2428 | -37.5343 | 2025-12-02 13:10:00 | GOES-19 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 121.6 |


