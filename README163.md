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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 218524bb-3c5c-3c1a-bae2-133bf4b5449d | -18.81131 | -54.48382 | 2024-10-02 05:14:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 86e4a36e-f0f6-3358-a4fc-3c024d20c85f | -18.80864 | -54.47146 | 2024-10-02 05:14:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76b37194-227c-32e9-89c0-8162e3966058 | -18.80813 | -54.47546 | 2024-10-02 05:14:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1edc229f-ef02-361c-8cad-e8201f660060 | -18.80762 | -54.47947 | 2024-10-02 05:14:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8a30c769-dcd4-3569-9677-a40eb99a5dd3 | -18.80711 | -54.48346 | 2024-10-02 05:14:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| de4eff83-3548-3f68-86a8-fe9e99f2aa71 | -18.80661 | -54.48741 | 2024-10-02 05:14:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 49bb6a8d-2a69-3489-abfa-d34b4e420fe9 | -18.80444 | -54.47103 | 2024-10-02 05:14:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ac71b65-b8f4-3f03-a60f-4aa22fcec7d0 | -20.77404 | -54.84098 | 2024-10-02 05:14:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb83ea0f-35e3-3ceb-bd45-9225e700a9ad | -20.76982 | -54.84066 | 2024-10-02 05:14:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a97c6e9f-5740-368c-a7ed-6a58915786f4 | -20.76806 | -54.82015 | 2024-10-02 05:14:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d91c0f8-fea3-316e-9441-84372e899aed | -20.76385 | -54.81964 | 2024-10-02 05:14:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da75f86a-f970-3889-a044-adb41a93c878 | -20.01306 | -55.46367 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0f40116-78b7-3fce-be2a-1abbeec9234b | -20.01152 | -55.46212 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 325fb04f-ff89-3007-a8dc-b1a47e8fee6b | -20.01097 | -55.48032 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3132b298-305c-30d0-ac5e-7492bf16a943 | -20.00906 | -55.46311 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2bb73a1-4ebe-3a41-a871-804dd893322d | -20.00753 | -55.46154 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e550f48-c552-33ae-b972-5ca92233c173 | -20.00507 | -55.46252 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8b828e69-9406-3f21-87d3-e173fa7d0e4c | -20.00437 | -55.46816 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3a28021-d871-3b88-908f-8fe3cb7b76e6 | -20.00354 | -55.46094 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f12627b8-98b5-35b6-854a-6ce20769b91e | -20.0028 | -55.46655 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffa8e6e6-f40f-3243-b4a8-1c3b69cc3ab5 | -20.00039 | -55.46742 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 636b3a22-9a17-3e78-8d17-e85f52b15c20 | -19.99883 | -55.4658 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76b38ff1-83cb-304a-99a1-d8ce74de72de | -19.99642 | -55.46666 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab405ece-fd0d-36f8-91dc-60f647a15276 | -19.99485 | -55.46513 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61a8b3a3-8e9d-3e41-bc51-4d19b3e9c275 | -19.99242 | -55.46614 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cb7dc45-699c-39e9-af3e-022382116132 | -19.98542 | -55.47503 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2ce0b2ae-8928-38f4-add8-c52db8f93b0f | -19.98143 | -55.47449 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 47c13111-6798-3a5b-8150-5bf8e6a36b5f | -19.98069 | -55.48012 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e3a90e38-30fe-348e-a728-47a978aff475 | -19.97745 | -55.47388 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae3af8e4-904a-3b8b-8729-292210f15932 | -19.97672 | -55.47947 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b68209f-1120-3f4e-beac-be4523b1c219 | -19.96805 | -55.48365 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1127a1b1-fa32-3d56-b6b9-32b386874977 | -19.96341 | -55.48812 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c1b0de09-f8c5-3d3f-b924-16e9ef152e77 | -19.96276 | -55.49317 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 74485c3d-ed61-3761-b45a-cd97721cce54 | -19.74862 | -54.52148 | 2024-10-02 05:14:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d62daed-2951-39a3-83b5-501a4c4bdafd | -22.16962 | -56.03899 | 2024-10-02 05:14:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 643d59a9-d975-3ddb-92ec-1eba4b18c461 | -21.89241 | -56.10854 | 2024-10-02 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de63de44-022d-31e9-8951-a613ddcbdeef | -21.88847 | -56.10802 | 2024-10-02 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9241f58a-8798-35f6-8139-6b0bdbd1756e | -21.3592 | -55.69171 | 2024-10-02 05:14:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 8e41fda2-f7fd-35e2-8dd4-b5849cb4098c | -21.35644 | -55.68675 | 2024-10-02 05:14:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 05fe08c1-e0f3-3e9c-8a57-8a6403598cf1 | -21.3559 | -55.6857 | 2024-10-02 05:14:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5d229bdb-1f44-3497-a0c4-31c6118334e2 | -21.35577 | -55.69221 | 2024-10-02 05:14:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 1ad5dbbe-fcfd-30b6-aa79-6cc1caacbbd7 | -21.35519 | -55.6912 | 2024-10-02 05:14:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 41.0 |
| e678c756-00b0-3829-8f08-7a2e3592fca7 | -21.35188 | -55.6852 | 2024-10-02 05:14:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a1baf535-450e-3b0c-a81c-9ff713141569 | -21.35117 | -55.69073 | 2024-10-02 05:14:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 23.2 |
| d74ecc0b-5a9a-3f88-ba1b-1d2ddc34833a | -21.34786 | -55.68471 | 2024-10-02 05:14:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 10b5aa3a-179a-31e3-9b0e-8ab07287ec1a | -21.34715 | -55.69025 | 2024-10-02 05:14:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 62c8b89a-bdc9-387e-b5d2-4526f3d421d0 | -21.34646 | -55.69562 | 2024-10-02 05:14:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 08ade295-b232-35ae-8244-e31f605ac72e | -21.34314 | -55.68964 | 2024-10-02 05:14:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b26f2e2-1524-3e53-ab2a-04302b5f88e5 | -18.69537 | -57.32224 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 437013cc-f4fb-3069-a5a0-618a731d33d5 | -18.69419 | -57.33064 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| abc34239-5104-356e-8be5-5acfba09840d | -18.69361 | -57.33483 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 15c25ad7-73b3-39db-b3eb-bf40f5e4a64e | -18.69181 | -57.32168 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| eb66527b-1bb2-34f6-a7b2-83b979f766b6 | -18.69064 | -57.33007 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0a85c36f-a8cd-39fc-b1dd-8f5ad812716f | -18.69005 | -57.33427 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 73ee4479-80b5-3ecf-979a-54ebfed69d02 | -20.38546 | -58.06724 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b33feb4d-be62-35b1-9827-c94a7f04ed79 | -20.38136 | -58.07079 | 2024-10-02 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9afea897-d48d-36a3-97dc-f239ffffe220 | -20.04802 | -55.96679 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 4766f54e-61be-3bc5-a7e5-a090349c3ab3 | -20.04794 | -55.96522 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 19c4e17b-c783-35ae-ad11-c736ac6ae0fa | -20.04736 | -55.97189 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3cdcb225-4e83-319b-a840-11bc5af18a98 | -20.04725 | -55.97031 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 4bdf9b7d-f9c4-3820-a9bf-1afc5e4e80e6 | -20.04414 | -55.96621 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 18a8e8b0-2dc8-37a4-9b3d-313a3d89ae2b | -20.04406 | -55.96465 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6660e7d5-93ab-3f79-9553-37d479a4cd17 | -20.04349 | -55.9713 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e93f3c3a-3f18-30ac-b16d-3da08e74e85b | -20.04338 | -55.96973 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 93315804-ae9b-304d-bf6f-84d165e69bba | -20.04153 | -55.98655 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c93f207a-8b28-30f9-b638-3e5f1913a704 | -20.04133 | -55.98495 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3698a740-8b3f-347c-9724-6d0854b4bf43 | -20.04026 | -55.96564 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 59e7bd98-470e-35c3-b7e5-592e784ae7dc | -20.04018 | -55.96408 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 29387b89-887a-3870-b21f-5f38d980388c | -20.03961 | -55.97072 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 71438546-5dfb-3f4b-a3f6-9f5ad61ce6ae | -20.0395 | -55.96916 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7aace257-c3c2-3fe3-9952-edfe53608d24 | -20.03896 | -55.97581 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3a9a55a4-9a40-328f-8b47-dcd41b99e3a0 | -20.03882 | -55.97423 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 09b666ee-7a60-3d65-a444-4857213a92c4 | -20.03766 | -55.98598 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9cdae183-e50c-33e6-9553-a0cb3d91bb02 | -20.03746 | -55.98438 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1bcacaa4-c87b-323f-a230-ccdd8f543ac0 | -20.03638 | -55.96507 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1238b6e9-f31d-322f-a0d9-66e68d295182 | -20.03573 | -55.97015 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| efd21407-069c-3870-831a-1c029eb241c7 | -20.03563 | -55.96859 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 54c1f453-8f1a-36d8-9656-3ecc97cc6448 | -20.03508 | -55.97523 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f9a63cf9-b786-3602-b9fa-49e91df74fd1 | -20.03495 | -55.97366 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5a3da52b-4da0-3497-805d-3d45554c9fe7 | -20.03444 | -55.98032 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b6588741-5c18-3dda-9e2f-c09410561658 | -20.03426 | -55.97874 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a702a98a-81e4-3637-97ac-1c0a379cb28b | -20.03379 | -55.9854 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4e1e053a-c527-35a9-9823-722d3318f884 | -20.03358 | -55.98381 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5c87a513-ebfb-32a5-a220-495ea2cb9301 | -20.03175 | -55.96801 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5c69eb82-03ab-3626-a012-2d2531f1d28f | -20.03107 | -55.97309 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ea6fc0b3-c292-3b80-8cbc-ebec84afbcd4 | -20.03039 | -55.97816 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ec8d3db8-c9c1-37c2-a583-e57346e5990e | -20.02971 | -55.98324 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e9ce2617-b257-3963-87bc-21d982f65b76 | -20.02719 | -55.97252 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 22c97e8d-731e-3d28-9f40-50441e739ff1 | -20.02584 | -55.98267 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 76143f33-6939-34f5-a1f8-ae6a9984cefd | -19.65663 | -56.47281 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| cfe622e2-c348-39f8-a874-2a8b9a42c2d6 | -19.65654 | -56.46996 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0a6f701b-f419-3c60-83e4-4fcc7d80b810 | -19.65589 | -56.47468 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0b17e81a-f316-3f84-b002-d38091b1b190 | -19.65288 | -56.47224 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| bbbeeb54-8d14-35ab-bbd5-5f0d611c1ffd | -19.65279 | -56.46939 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 332f2af8-0303-3e38-bc38-13e47c59b02b | -19.65226 | -56.47697 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 4d18e840-ca19-3f33-8bf4-38790950d2c0 | -19.65214 | -56.47411 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d19800bb-b11f-30e6-99e6-cd09115b1f9d | -19.65149 | -56.47882 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6d277b65-331b-3687-b8b8-4fac3db992e7 | -19.64354 | -56.56388 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 26ed81e5-0622-35f8-9c73-15d4d61311a7 | -19.64044 | -56.5663 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5c2a26ef-5118-370d-a7d8-40386bd9b1e2 | -19.63981 | -56.56332 | 2024-10-02 05:14:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |


[Clique aqui para ver as próximas entradas](README164.md)
