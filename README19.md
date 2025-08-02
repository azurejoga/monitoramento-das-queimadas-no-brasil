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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4ec5455-c3c1-3323-8e73-df16c036e5e9 | -12.672 | -44.48658 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 672db57e-2e0c-331a-8f6f-79e5e4496e04 | -13.2171 | -47.24812 | 2025-08-02 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e371443e-11b1-3a49-a0c9-7f71bd21dca6 | -13.28165 | -51.65241 | 2025-08-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27947c84-e1bf-3d54-9798-fb6e582ea3dd | -12.66428 | -44.50857 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0d3ed168-a321-3650-9a18-db003445e5b3 | -11.19027 | -55.01863 | 2025-08-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7fe5e2c-d423-31d5-82bd-e2d255b00a69 | -12.65508 | -44.50159 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 98d5849a-4a46-3727-b390-da5c4995a2eb | -13.90037 | -42.12802 | 2025-08-02 04:49:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 38b62a4e-524e-35ff-95f3-f4a35b2617d6 | -13.05356 | -47.44323 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 057806c1-c155-38c3-8e8e-32260863ecbd | -14.79514 | -42.72471 | 2025-08-02 04:49:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7052f03-c2d2-3f93-bd32-5c13b116b0f8 | -15.37256 | -44.28263 | 2025-08-02 04:49:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5562e6ff-d65c-379d-823c-5ae81b86dbff | -12.46046 | -47.0721 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ebeb578-6fa9-38b8-b876-d0a321a10057 | -12.66566 | -44.49724 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1286172b-5ed4-3ca0-928d-db08e9318ec8 | -16.47035 | -54.67859 | 2025-08-02 04:49:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 955b7f83-8a3a-3af1-8db3-fe1336df3fff | -15.12302 | -55.22518 | 2025-08-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 68809ae7-dc2b-3c2e-acd8-cfde8394f9e5 | -12.54069 | -44.72162 | 2025-08-02 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee891379-7ccb-3f69-857c-e0713fefd824 | -12.6595 | -44.4882 | 2025-08-02 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 32f5af1f-e0d2-38e6-bce5-c86e718af6d3 | -12.6784 | -44.5085 | 2025-08-02 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| ca25357d-b195-3581-957d-8a2f16857319 | -12.6789 | -44.4851 | 2025-08-02 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 065ee1c4-3c82-3037-a713-dcd8c399ddd3 | -12.6591 | -44.5117 | 2025-08-02 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ed4dcceb-1fe1-37c0-8565-374776b755f2 | -8.0321 | -43.1257 | 2025-08-02 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| e09a023c-5c7d-31fe-9ca1-83d0ba1abbc0 | -22.23231 | -56.04637 | 2025-08-02 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5e0ccfa-3be2-3806-8d94-bb87a9b6ea79 | -20.87738 | -56.37513 | 2025-08-02 04:51:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20fb880b-166a-35f8-95f5-a1fcecba96b6 | -24.69025 | -49.89393 | 2025-08-02 04:51:00 | NOAA-21 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8f0c34ee-c7c5-3a2b-9034-0620981282f6 | -22.40319 | -46.7915 | 2025-08-02 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bcc11a5c-04cd-3018-b238-78c8c3277edc | -22.3232 | -48.71502 | 2025-08-02 04:51:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f83e623e-8c04-3df4-9426-2c2a396e8fa3 | -19.74563 | -46.02486 | 2025-08-02 04:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 480a8b47-8ce0-3542-a51d-04a49d28e8a4 | -18.33244 | -54.28788 | 2025-08-02 04:51:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daa03c95-63ba-3baa-ae9a-d7a081d2df7f | -22.32839 | -48.71692 | 2025-08-02 04:51:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b7258a36-eb0d-339d-bc43-9fe6ec3dd773 | -19.75611 | -46.04216 | 2025-08-02 04:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6778bad9-0cec-3ff1-83f7-e59f87c4366a | -22.32413 | -48.71635 | 2025-08-02 04:51:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bf6f8d42-48b7-32ff-aee7-99e7ffbf37b5 | -22.21535 | -56.19237 | 2025-08-02 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0f63a02-7be2-3edd-b784-946c3a2a7ef4 | -21.54578 | -48.71983 | 2025-08-02 04:51:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 534c936b-b702-3c33-b29f-b77c2ec36aac | -22.59708 | -54.97521 | 2025-08-02 04:51:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8c8bfb61-3d28-3139-b7db-71c0a06da2eb | -18.3369 | -54.2812 | 2025-08-02 04:51:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48fda0b4-c6ae-3d17-bca8-c4d1536cce01 | -22.32747 | -48.71561 | 2025-08-02 04:51:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| bbab43ab-4fd3-3c66-87d8-b1821f7efd26 | -18.46631 | -49.10839 | 2025-08-02 04:51:00 | NOAA-21 | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bd2f0d8f-f32e-3026-915d-d865cfb9c106 | -22.97817 | -47.04139 | 2025-08-02 04:51:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 558d7058-6cb8-3190-a9bf-34d7fa227f4f | -21.66443 | -46.93351 | 2025-08-02 04:51:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5df4b4a5-40ed-33f7-be49-0838f7c0cb61 | -18.93308 | -52.48639 | 2025-08-02 04:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35c9da75-f472-33e5-8783-b30c1f041668 | -21.33335 | -55.63006 | 2025-08-02 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12420355-a5cd-362d-84bf-a96d75be4fdd | -22.66606 | -53.37666 | 2025-08-02 04:51:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0ef889c1-e7cb-38ba-8626-d4712c3ef0b3 | -21.14226 | -48.01775 | 2025-08-02 04:51:00 | NOAA-21 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ede24eed-c42b-3d44-a864-533047f6552a | -20.57491 | -48.53972 | 2025-08-02 04:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e8d278b-9bb2-32c0-b40c-89e1d1d688ca | -19.30882 | -48.90845 | 2025-08-02 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1d2692a-d9a5-36d0-bffb-395ac36bc4be | -18.33575 | -54.28846 | 2025-08-02 04:51:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d61af07-2d21-3d93-a3a7-de51314f2e67 | -23.0016 | -48.63575 | 2025-08-02 04:51:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0776ea6a-6cca-318f-90d4-1f9b6d96b1fa | -22.66887 | -53.38115 | 2025-08-02 04:51:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 412ae4fc-5e1d-3002-bc2b-ced4a16fceb0 | -18.92914 | -52.48965 | 2025-08-02 04:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c37ff0d2-b2f1-316c-aba1-ff183df64931 | -19.75677 | -46.03598 | 2025-08-02 04:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dd894f7-b93e-3af6-8f62-aaf591a109aa | -20.77341 | -48.56904 | 2025-08-02 04:51:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3f9c1c7-1e6e-3a2f-9a55-9123d492c79f | -19.74307 | -46.02459 | 2025-08-02 04:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 269f0e2f-feed-30d8-917b-119b8bb67ca9 | -23.70899 | -51.7801 | 2025-08-02 04:51:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b9a7295a-9cea-398c-b90c-83aba7012da9 | -22.66945 | -53.37724 | 2025-08-02 04:51:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ee63c70b-f280-3a20-8e02-6ab4023a6416 | -20.87803 | -56.37125 | 2025-08-02 04:51:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71fbe828-7440-385d-9466-b19c6b32afe3 | -22.40379 | -46.78591 | 2025-08-02 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ef159825-ebef-3432-8993-da7a30a94a83 | -23.08776 | -55.18559 | 2025-08-02 04:51:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 94a7a845-9b55-3e5b-bf1f-e26d58e7c43b | -22.74659 | -47.03034 | 2025-08-02 04:51:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5cf4a543-3da9-3492-ac01-3d0145a6cb07 | -18.92631 | -52.48527 | 2025-08-02 04:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5c7eb77-0147-3965-b169-1c3ef21305cc | -20.26763 | -50.53761 | 2025-08-02 04:51:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f041a5ea-cf74-3c83-8cc7-d1b430187c20 | -18.73584 | -49.09803 | 2025-08-02 04:51:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7100966f-5a84-3eb4-9f65-6a6a5dfc29b0 | -21.0198 | -56.0054 | 2025-08-02 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7fd4e27-24a7-370d-bc5a-dc85e70b72a3 | -18.53492 | -49.49818 | 2025-08-02 04:51:00 | NOAA-21 | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8186ed9f-a620-3485-bc17-21ae19a24d63 | -24.63959 | -51.16957 | 2025-08-02 04:51:00 | NOAA-21 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 770e6f70-6e59-3a47-911d-91956fcf6d6d | -21.38816 | -48.67429 | 2025-08-02 04:51:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7b39a03-4dc4-35e2-8988-34a9a352dcd9 | -23.70838 | -51.78472 | 2025-08-02 04:51:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 284745b1-ebde-3406-9533-23c29314e198 | -20.45469 | -46.41333 | 2025-08-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48b5abc7-02ab-3954-aca8-6c17217f72a2 | -20.32274 | -46.63159 | 2025-08-02 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4283b037-a399-354e-9bff-ee142acbe9fc | -20.47966 | -53.67608 | 2025-08-02 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68c1b988-9edb-39e4-b579-164615ec757a | -22.80649 | -46.17554 | 2025-08-02 04:51:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c8f92bcc-04ee-39fb-9334-ff85c3c61294 | -19.15554 | -49.12523 | 2025-08-02 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a428d2f-bbe4-3a05-b892-72c796ccb41b | -18.32633 | -51.67734 | 2025-08-02 04:51:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42654e4b-d733-3fba-b9a8-9845363ca828 | -18.33633 | -54.28484 | 2025-08-02 04:51:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 340496e4-19c3-3083-8926-4737ec736d35 | -23.70708 | -51.65316 | 2025-08-02 04:51:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| fafa678d-08e1-3ecc-9d22-3a5a3a2563d8 | -20.26926 | -50.54084 | 2025-08-02 04:51:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| da2e468f-6333-3968-9bc4-90661c3b973c | -21.65968 | -46.933 | 2025-08-02 04:51:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ce6fb43-c446-3ea4-a965-f68d66c67824 | -23.70768 | -51.64856 | 2025-08-02 04:51:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 7c8e4f21-0035-32e9-bae8-e99cdd2c2274 | -20.32423 | -46.62666 | 2025-08-02 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e2d7a5a-c299-32a1-a8dd-bc62f308e917 | -20.86681 | -54.95108 | 2025-08-02 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1be7f246-edee-3f83-8a18-4e737d422cd5 | -18.53106 | -49.49759 | 2025-08-02 04:51:00 | NOAA-21 | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 46206c21-0ae6-36e0-b8fd-4a590df691c9 | -20.87673 | -56.37902 | 2025-08-02 04:51:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bef84066-970e-380b-b052-1ff43acb227a | -19.30101 | -46.21109 | 2025-08-02 04:51:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| beceeea0-5716-3e1c-ad71-0e2b88db4f15 | -23.09107 | -55.1862 | 2025-08-02 04:51:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 67442603-5004-3b0b-937a-b2abb736fe64 | -18.92575 | -52.48909 | 2025-08-02 04:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d43cf87d-4042-3cc1-8153-50045181d32d | -21.35601 | -53.38153 | 2025-08-02 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77eca7f4-40ab-368a-9904-bd976123072d | -22.82604 | -53.8556 | 2025-08-02 04:51:00 | NOAA-21 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 445a4a0c-4ecd-3589-b0cb-5774df4ac909 | -18.46233 | -52.16198 | 2025-08-02 04:51:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ae2baf7-8513-3ec9-af90-0d60e465be18 | -23.09049 | -55.18994 | 2025-08-02 04:51:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9b45568d-fecc-321a-a3be-ded4ffdb9fc2 | -20.31893 | -46.6311 | 2025-08-02 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53905c5e-1701-377c-99b2-9dbe8d61f633 | -20.76919 | -48.5685 | 2025-08-02 04:51:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 731947c9-b0fe-308d-86e3-87a55077a8a1 | -20.32338 | -46.62603 | 2025-08-02 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e53abf8-d6d2-3c69-a409-0cbf4ab4376b | -18.9297 | -52.48583 | 2025-08-02 04:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 690aa31b-d108-3a91-a973-2334d84ec2ca | -21.66052 | -46.9337 | 2025-08-02 04:51:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5df4d620-1355-345a-b264-5f154fa8392b | -29.77372 | -53.84771 | 2025-08-02 04:53:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| d6e2b6a8-6b0d-345d-a986-bbad311de5eb | -29.0104 | -50.7041 | 2025-08-02 04:53:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 324ef0e7-60db-333a-87ce-636aeb47cb4b | -26.02505 | -48.97655 | 2025-08-02 04:53:00 | NOAA-21 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 58a7f6f7-fae0-3788-b328-c6e3fbedf21b | -29.77432 | -53.84312 | 2025-08-02 04:53:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 3c5c02ca-5815-3ddf-9520-bccf4370353b | -28.17721 | -50.44415 | 2025-08-02 04:53:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8eb415be-dc98-3e5f-89db-427f11f68837 | -28.79146 | -54.75841 | 2025-08-02 04:53:00 | NOAA-21 | BOSSOROCA | RIO GRANDE DO SUL | Brasil | 4302501 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 3b343f83-3363-3460-ac6c-e667f4662859 | -26.02944 | -48.97716 | 2025-08-02 04:53:00 | NOAA-21 | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a90f5822-f8b5-391a-a18c-5c8586e51004 | -28.75144 | -50.4046 | 2025-08-02 04:53:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README20.md)
