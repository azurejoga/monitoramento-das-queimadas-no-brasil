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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d7f05d8-1c99-3fb4-8bf6-f76adeda8b68 | -6.6725 | -56.4029 | 2025-07-31 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 191.6 |
| a9970dc2-fdb8-3888-914f-5a4d10241f2f | -10.3065 | -54.1592 | 2025-07-31 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 89c2f7f9-e5b8-3fda-bc0a-ee605394bbb7 | -18.5536 | -46.6694 | 2025-07-31 00:00:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f3abb5f4-0e1e-3097-bf39-6682c9f07e84 | -5.5011 | -44.3956 | 2025-07-31 00:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| d6da8c72-562f-39b7-b884-6cfdbd5fb706 | -7.8705 | -45.5408 | 2025-07-31 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2520cebf-aa46-3483-beac-14c68f16db21 | -8.6053 | -45.5121 | 2025-07-31 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 3d95a7ab-67c1-3981-aa8a-bb211613f271 | -11.7508 | -48.1825 | 2025-07-31 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 49463c43-1ed5-3fda-a6eb-9d704e5ba843 | -5.4824 | -44.3969 | 2025-07-31 00:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d05cddff-79cf-3d69-9da0-3b30dcbf025f | -18.553 | -46.6929 | 2025-07-31 00:00:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 79.7 |
| b51482b0-fc3e-3148-857f-d4bd84a627ad | -13.5238 | -45.6693 | 2025-07-31 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| cf1d0fe2-31ec-3f86-8384-87033a10e1b2 | -16.3789 | -52.6551 | 2025-07-31 00:00:00 | GOES-19 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c1beae6d-6ca3-38ba-bfb3-2cde89584464 | -8.5864 | -45.5141 | 2025-07-31 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a47e85d2-df9b-3751-860f-74cba63a28fb | -16.3593 | -52.658 | 2025-07-31 00:00:00 | GOES-19 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 1f83d74e-5a56-3aae-a00e-80f2ade9f3b1 | -6.6541 | -56.384 | 2025-07-31 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 546996a1-9531-3a2f-b8a5-df19c163f819 | -6.6726 | -56.3831 | 2025-07-31 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| e63d6ea7-ddd3-38e8-b77c-f1257a8225e5 | -6.654 | -56.4038 | 2025-07-31 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 58f717a2-fa0f-335d-a270-d607bd7c9a79 | -5.5013 | -44.3726 | 2025-07-31 00:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 80455783-d35f-3de0-9ec9-3156571f88a5 | -10.0843 | -53.8712 | 2025-07-31 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 390e231a-b8b2-3c03-b143-ee3e457d6b37 | -18.5328 | -46.6973 | 2025-07-31 00:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 46.7 |
| ee8d9fd7-1789-30f8-8ac6-d2e71d768445 | -6.5258 | -56.2121 | 2025-07-31 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 24f38f04-9e64-3933-813b-409094decc98 | -6.6726 | -56.3831 | 2025-07-31 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| a1b41456-34b4-3c56-b1b1-6c29909f9563 | -6.5445 | -56.1915 | 2025-07-31 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 6280bdd6-9365-3d5d-8006-e17733bfc938 | -11.7508 | -48.1825 | 2025-07-31 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 63dcbbd7-2fa0-30e0-80e2-009fdb820d0f | -18.5536 | -46.6694 | 2025-07-31 00:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 5263ea42-3097-3c04-aa28-bd91a5f7aeab | -5.4824 | -44.3969 | 2025-07-31 00:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| eaca6bb0-d5a5-3606-8b88-fd71c7c92a57 | -6.654 | -56.4038 | 2025-07-31 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| a4450815-4119-39e8-9c9a-283ea7b65041 | -13.5243 | -45.6462 | 2025-07-31 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 9d52f94c-d1d8-3785-a2f3-68e83d43e6f0 | -13.5238 | -45.6693 | 2025-07-31 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 1147fe9c-ce2f-3380-b728-c30ff6207936 | -10.0843 | -53.8712 | 2025-07-31 00:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| a5deb3fa-74e6-3ca0-adfe-fd3e4da3438e | -16.3789 | -52.6551 | 2025-07-31 00:10:00 | GOES-19 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 8af0f1e3-2c1c-3ad9-a9c0-6446b518dfeb | -8.6053 | -45.5121 | 2025-07-31 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 5b9f209a-a94f-3b66-8b19-50b4871aa4b3 | -13.5233 | -45.6925 | 2025-07-31 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| bbc6c8fe-4fbe-3ca4-82be-451bbcb19e19 | -10.0655 | -53.8727 | 2025-07-31 00:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| f2f9e6e4-a70f-3e99-8cf6-4ed68da6113f | -5.5011 | -44.3956 | 2025-07-31 00:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 40f66526-cecc-3814-99d5-9ee36bc42a9a | -6.5075 | -56.1932 | 2025-07-31 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| c7ffd659-34b5-32f8-b301-ddfaa6d970cb | -11.1348 | -48.6321 | 2025-07-31 00:10:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 4d49e63d-e194-3ba3-9aaf-c33724af4f52 | -6.5629 | -56.1906 | 2025-07-31 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 88ce1a55-b127-38cf-b632-719d418b7425 | -6.6541 | -56.384 | 2025-07-31 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 1aa9a578-a5c2-3db4-b26f-6a086a8d65af | -6.526 | -56.1923 | 2025-07-31 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 8678aa50-e5f9-3ef1-828e-52266b5dba79 | -18.4473 | -46.9023 | 2025-07-31 00:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 8ab92406-f585-393a-b82a-2fa3536295b8 | -6.5074 | -56.213 | 2025-07-31 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 0eaacba3-582b-3d23-82b2-82a4edf9571f | -18.553 | -46.6929 | 2025-07-31 00:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 6da787ce-df6e-3c9d-8375-991fa54aa364 | -6.6725 | -56.4029 | 2025-07-31 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 3f24038b-2c39-32dc-90eb-5b05dbb62b02 | -13.5044 | -45.6726 | 2025-07-31 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| d9a4dd7f-e4ab-3efb-b290-8f82751818a6 | -6.654 | -56.4038 | 2025-07-31 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a25a37bf-859d-39f5-bfff-66f14ae1e878 | -5.4824 | -44.3969 | 2025-07-31 00:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 02c6fd4c-7482-38df-908d-5d469f916631 | -6.5075 | -56.1932 | 2025-07-31 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 038486c9-a41f-3314-a557-cfbfd160ccde | -6.5629 | -56.1906 | 2025-07-31 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| c767671a-e238-3134-ad1d-dda267df3830 | -11.7508 | -48.1825 | 2025-07-31 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 63b7329e-59c9-3120-93d0-cf984fd38c17 | -13.5238 | -45.6693 | 2025-07-31 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 30fe969a-9cbd-37ae-8a05-87a8f9dc755e | -11.5503 | -44.2407 | 2025-07-31 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 5c081fd7-4c4c-3703-bb21-37696614fc45 | -6.5258 | -56.2121 | 2025-07-31 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 13b0c7b3-7aeb-3c22-9d4d-9ab722deaa8a | -6.526 | -56.1923 | 2025-07-31 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 690a0e41-0172-3166-89f2-bf13420f3290 | -8.6053 | -45.5121 | 2025-07-31 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| f2937241-7312-3502-ac34-2a0e8b7aeab4 | -6.6726 | -56.3831 | 2025-07-31 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 05892d4d-f861-377a-a06e-d6412a661348 | -5.5011 | -44.3956 | 2025-07-31 00:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| bb1aac5b-575e-3467-a81d-6ac9ea81edbf | -10.6108 | -43.2969 | 2025-07-31 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 52.0 |
| 850242fa-0fb8-3b21-86a7-5ecb883310c7 | -10.0843 | -53.8712 | 2025-07-31 00:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 71e6b7f6-e60c-3a9f-ac7b-7bedffe3ed65 | -18.5536 | -46.6694 | 2025-07-31 00:20:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e92f1688-13f0-3f98-9aac-c1e3bed6a7a6 | -18.553 | -46.6929 | 2025-07-31 00:20:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 65b9545e-4dbf-3e94-bc2f-4020b1bac9d1 | -6.6725 | -56.4029 | 2025-07-31 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 150.9 |
| a1c0e91a-c023-31ab-8d82-b78d31178d0d | -6.5445 | -56.1915 | 2025-07-31 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1bb0ba29-4ecd-3216-97b4-27ee587e4110 | -6.5074 | -56.213 | 2025-07-31 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 30965c16-9627-3f6c-9f49-3dd50d398fe4 | -11.5311 | -44.2436 | 2025-07-31 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 31c4ddee-1994-3507-988b-71efa7ab9571 | -6.6726 | -56.3831 | 2025-07-31 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e28865a9-673a-33a5-a87a-337eeaaa3ac4 | -6.526 | -56.1923 | 2025-07-31 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| d4012c74-5a96-3acc-a220-dd68ac32efa3 | -13.5238 | -45.6693 | 2025-07-31 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 88310536-d891-39b0-a9f3-6cb492346607 | -13.5243 | -45.6462 | 2025-07-31 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| c6eb2ec0-750e-36cc-a3bf-e33d35ee333e | -18.553 | -46.6929 | 2025-07-31 00:30:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 20693bd7-1e5e-3495-ab36-50b44ae1aef5 | -6.654 | -56.4038 | 2025-07-31 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 97e7e572-0f57-3ac1-ab84-099d96acfdf9 | -6.5629 | -56.1906 | 2025-07-31 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 13e1c3da-c236-3896-8b15-af51dd13bc7c | -10.0843 | -53.8712 | 2025-07-31 00:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 109.0 |
| c133c475-bc68-3d92-be8a-a29c8e0e2cb2 | -7.8894 | -45.539 | 2025-07-31 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 83e71f00-5f11-3e04-963a-4efd399a6eb1 | -6.6725 | -56.4029 | 2025-07-31 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 70e4e914-9c06-3507-b606-12587a7a45cd | -6.5258 | -56.2121 | 2025-07-31 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 2cd1ab0c-754a-3da8-ad56-c9060a695027 | -11.7508 | -48.1825 | 2025-07-31 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| f5f4251a-1a1c-3604-be95-68f541590699 | -6.5074 | -56.213 | 2025-07-31 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 3c2a0cab-66d4-3eef-8fd8-26f512c63df9 | -5.5011 | -44.3956 | 2025-07-31 00:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 39fe439b-cf5e-3e8f-b9e5-b704087ec75c | -6.5075 | -56.1932 | 2025-07-31 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 8c74fb79-8354-316c-b9ec-3d0425d04d65 | -6.5445 | -56.1915 | 2025-07-31 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d9eeafcf-e525-33c4-a3d5-a551e832a472 | -11.8841 | -44.553398 | 2025-07-31 00:31:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1eb11b7-c61f-3813-bb2c-b22533f522c1 | -7.8412 | -45.547501 | 2025-07-31 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c05d7c3d-c7ee-386d-ac7f-e3a92174ac63 | -5.4497 | -44.391701 | 2025-07-31 00:31:00 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 081bfc3a-9042-3910-bd20-f1d746a64ca9 | -6.4616 | -56.190601 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbfccb70-fd8e-37f6-a146-35ec4b34c549 | -10.5952 | -45.235298 | 2025-07-31 00:31:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 732ef273-5201-3018-9d9c-aede188fe971 | -3.799 | -49.260101 | 2025-07-31 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d72a33b0-fa2d-351e-9b02-e50a1fa71f6c | -6.51 | -56.180599 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ddf69cb-39d7-354f-aab5-0c1ebd409ee6 | -11.4949 | -44.248001 | 2025-07-31 00:31:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 555fb722-46f0-3dcc-9e4e-39c553f9ed43 | -13.4741 | -45.679298 | 2025-07-31 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5002a4bb-065e-34b3-a377-6543d6d79397 | -6.6296 | -56.365101 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d4331a7-bf08-3d68-b74d-e8eb65e191ae | -9.5361 | -43.896599 | 2025-07-31 00:31:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c41165eb-bf60-3c17-a577-1fc0ef392357 | -18.506001 | -46.684799 | 2025-07-31 00:31:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f6560ed5-169b-34cf-9965-fab414ba81df | -6.635 | -56.390701 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f155723b-83a9-3356-ac17-517bba517d96 | -14.8188 | -49.290798 | 2025-07-31 00:31:00 | METOP-C | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bce3b4e8-2240-3e13-9f5e-dba284fc7558 | -13.6356 | -44.2295 | 2025-07-31 00:31:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77f95193-b6c0-32e1-a606-ba108940e91f | -6.4194 | -43.193401 | 2025-07-31 00:31:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e07bd4e-2fe2-3501-8c9f-3658eb4744ff | -13.4791 | -45.655201 | 2025-07-31 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52587f54-6c1e-32b0-841b-6b2451946def | -10.5771 | -45.2467 | 2025-07-31 00:31:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| acef5208-3845-36de-a5ed-f2ccfb56ac4d | -10.0474 | -53.880501 | 2025-07-31 00:31:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45336f27-de6a-37ff-a0dd-153d26e6cdca | -10.4843 | -42.559399 | 2025-07-31 00:31:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
