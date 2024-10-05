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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca977ba6-1ada-3249-88a0-72038d95216f | -8.7844 | -44.8085 | 2024-10-05 02:35:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 208.5 |
| 2372be9c-3da3-3e50-a9ed-bd651290adc6 | -8.7769 | -49.9763 | 2024-10-05 02:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 7641d88d-9be8-3a85-88dd-848e3583cc37 | -8.7772 | -49.955 | 2024-10-05 02:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| f85fdac4-e23d-36d3-957a-350100c361b2 | -8.7957 | -49.9747 | 2024-10-05 02:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 87f81c4a-0ff2-3c20-9f8f-201e806c8c84 | -8.7959 | -49.9533 | 2024-10-05 02:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 9be75a00-08c3-38d4-8a47-a66c1c9505c0 | -8.9851 | -49.8297 | 2024-10-05 02:35:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 1be83c01-a6b7-3e3c-9342-d7eb846af3aa | -8.9853 | -49.8083 | 2024-10-05 02:35:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| cd3c5414-ccd8-3e9d-9585-f4a6f5248f5c | -9.3645 | -51.1109 | 2024-10-05 02:35:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 277d9736-a487-38bc-9384-6007cb59e77f | -9.2839 | -65.4283 | 2024-10-05 02:35:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 978ce13b-90a0-3bad-ac2b-ea2a4c22b21c | -9.3647 | -51.0898 | 2024-10-05 02:35:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c0d8d27b-d634-3ac7-beab-bf12d04cbf37 | -9.284 | -65.4096 | 2024-10-05 02:35:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 9b3ad993-cc70-3d09-ba8a-bc818a9b892b | -9.3457 | -51.1125 | 2024-10-05 02:35:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 822e34dd-6e10-3140-9e9a-7ee64557ee0e | -10.3318 | -50.5322 | 2024-10-05 02:36:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 176ddbf0-fbad-38d7-bacd-fea194ea693f | -10.3315 | -50.5535 | 2024-10-05 02:36:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| ff66d631-1ae4-32e9-9bef-8e0f44dee209 | -10.3129 | -50.5341 | 2024-10-05 02:36:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 6af7f1ef-3038-3878-89f2-74ddcd6d0bd0 | -10.3126 | -50.5554 | 2024-10-05 02:36:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e87ebd31-180d-33a8-842e-364c37221ba1 | -10.4424 | -50.7336 | 2024-10-05 02:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| be3ef3f6-950c-3ac0-90ee-0d0d2531c339 | -11.1155 | -54.2319 | 2024-10-05 02:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| bd6706c6-bcc2-38cf-ad34-3f719000418e | -11.7187 | -47.8107 | 2024-10-05 02:36:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 7c9ce208-9478-3cf6-912a-befeeb5b585c | -13.1362 | -51.1313 | 2024-10-05 02:36:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 16d06b05-5867-344d-8874-6d6684f016cf | -13.1358 | -51.1527 | 2024-10-05 02:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 0467a630-d1dc-320c-9ebf-446aa597f532 | -13.117 | -51.1337 | 2024-10-05 02:36:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 260dfaab-1660-3322-8307-fda2ee035999 | -13.1166 | -51.1551 | 2024-10-05 02:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 680990f8-d97f-37f8-8c6f-493a41a0e48a | -13.995 | -47.2572 | 2024-10-05 02:36:24 | GOES-16 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 3878ae28-b02c-320d-a63e-29ef222fd341 | -14.014 | -47.2767 | 2024-10-05 02:36:25 | GOES-16 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 592830c4-24be-3f9b-9f71-39bb9ebb7df2 | -14.0144 | -47.2541 | 2024-10-05 02:36:25 | GOES-16 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 2867e44f-ca32-36a6-851c-0e701e0d5abf | -15.5594 | -57.4756 | 2024-10-05 02:36:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 8b92a604-74db-3260-98f1-e5df866e52eb | -15.5788 | -57.4735 | 2024-10-05 02:36:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| bb7e3e21-691b-3a43-8820-886e7e2a227a | -15.5791 | -57.4532 | 2024-10-05 02:36:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 130.9 |
| b7a3feed-7c72-3f64-9a7b-6551e75a7026 | -15.5597 | -57.4553 | 2024-10-05 02:36:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 29732bf8-feab-389d-897a-24cff415d0a3 | -16.0942 | -50.2323 | 2024-10-05 02:36:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 918deffb-c35c-3807-8bbb-99421faf2cbd | -16.5745 | -57.16 | 2024-10-05 02:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 6f2c95d8-1d23-346e-83d4-ea1d2e160f6e | -16.5742 | -57.1805 | 2024-10-05 02:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| ba3f3369-279d-34be-93cc-cb9d714b9015 | -16.554 | -57.2237 | 2024-10-05 02:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 035a9358-c2c5-325d-bc54-37a270e37063 | -16.4155 | -57.3619 | 2024-10-05 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 7cf47e78-cbf0-390e-bf87-a96aecd13a08 | -16.7647 | -57.4856 | 2024-10-05 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.5 |
| fca6f20a-5aa5-3207-9171-47699ed6bc79 | -16.6871 | -57.4536 | 2024-10-05 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| b0811776-5295-317c-97f9-19e22be8da21 | -16.7843 | -57.4834 | 2024-10-05 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 5148f928-b76d-397b-97c4-eb0380fc6a66 | -17.1085 | -56.7892 | 2024-10-05 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 2f04364d-7b0e-3922-84e6-c5ab50f2f815 | -17.0892 | -56.7709 | 2024-10-05 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 2b19644b-414b-3c9f-98ef-b682e91d9869 | -17.1235 | -51.7238 | 2024-10-05 02:36:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| eefd4b9d-896c-389c-b946-82188a77ab35 | -18.6525 | -43.1453 | 2024-10-05 02:36:49 | GOES-16 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.7 |
| 50b45454-dd26-3459-b287-aee1da8ec0af | -18.8809 | -43.6032 | 2024-10-05 02:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.4 |
| 6bcaa3ac-6c94-32b0-a637-fd40e1a6fda7 | -18.6582 | -57.2967 | 2024-10-05 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| a8bfc154-e007-3e1c-9bcc-df88540bdd2a | -18.6586 | -57.2759 | 2024-10-05 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| efa40644-cc20-31ef-9fcd-320ebceb3fb8 | -18.6782 | -57.2941 | 2024-10-05 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.3 |
| 8dc8bc4e-35fb-3a51-a82a-055520743557 | -18.6785 | -57.2734 | 2024-10-05 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 178.1 |
| 25664878-eed7-3b12-b93e-3642bb27aab1 | -18.6981 | -57.2915 | 2024-10-05 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| b96397e9-e0ba-3bdd-9514-8a954cca352d | -19.0944 | -48.2415 | 2024-10-05 02:36:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 105.0 |
| b3e8821b-81bc-3d94-8540-236fa955dbe4 | -2.9014 | -50.7142 | 2024-10-05 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 49ee11fa-f881-344f-a6f4-16e5992f14f6 | -3.3083 | -50.4719 | 2024-10-05 02:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| f3a362a5-1110-3661-9563-983c90db582a | -3.3084 | -50.451 | 2024-10-05 02:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 773d78ce-9bb3-3b96-bf10-8c6414cd6959 | -3.618 | -47.5352 | 2024-10-05 02:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| c99e8218-4bf7-399c-92e9-83cd025f3f13 | -3.6181 | -47.5134 | 2024-10-05 02:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ed7b9c6a-d050-359c-b3bc-528c952fdcb6 | -4.0794 | -47.9502 | 2024-10-05 02:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 71e72245-162d-3a52-9788-2c2e79569ae8 | -4.9451 | -43.7888 | 2024-10-05 02:45:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| b3524070-f1f7-30c3-9ff5-c0cdc22b649a | -5.8214 | -44.1426 | 2024-10-05 02:45:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 5f296d4a-e7ae-3076-b810-3853f4d59a8e | -5.8216 | -44.1196 | 2024-10-05 02:45:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b53d0d88-e81f-37a7-8874-81ae898c92c4 | -6.9514 | -59.0666 | 2024-10-05 02:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| ff15b14b-39c1-383d-8fd5-a512f597a6f3 | -7.5193 | -63.2558 | 2024-10-05 02:45:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e534546b-e901-3778-92b5-f6aff01f06f2 | -8.7652 | -44.8335 | 2024-10-05 02:45:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 175c2043-5322-3153-bd58-ee02c5dfda21 | -8.7655 | -44.8106 | 2024-10-05 02:45:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 220.7 |
| 39c5a69b-7adf-3dc1-b031-225c2ecb48e0 | -8.7841 | -44.8315 | 2024-10-05 02:45:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| eb4a9613-1948-3dcd-9220-460f7d1f8887 | -8.7844 | -44.8085 | 2024-10-05 02:45:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 34376f7c-7ffb-3e98-8503-be010bce91e7 | -8.7769 | -49.9763 | 2024-10-05 02:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 15cf335f-3760-3d93-81f5-1595ec2bb3f3 | -8.7772 | -49.955 | 2024-10-05 02:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 402a17bb-8585-3063-8f46-cda3b091c292 | -8.7957 | -49.9747 | 2024-10-05 02:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5e482d45-148e-3753-88e6-759545091316 | -8.7959 | -49.9533 | 2024-10-05 02:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 25b52288-5fc1-3722-91c3-c4d7f11bac89 | -8.9853 | -49.8083 | 2024-10-05 02:45:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 6be9ebf7-13db-379c-870e-ff6f3b45d31b | -9.3457 | -51.1125 | 2024-10-05 02:45:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 8de3d0cc-1332-3562-a8e0-61def08e79ba | -9.3645 | -51.1109 | 2024-10-05 02:45:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f20598bd-d014-33b5-9636-24410c48cf82 | -9.3647 | -51.0898 | 2024-10-05 02:45:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ef2d324c-4365-3068-aa5a-dc29d9bbac98 | -9.2839 | -65.4283 | 2024-10-05 02:45:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a719528a-9d85-3ebe-a06b-885e86c44e5e | -9.284 | -65.4096 | 2024-10-05 02:45:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 0fa34a05-a40f-3fa5-908d-6eaf47c7af33 | -10.3126 | -50.5554 | 2024-10-05 02:46:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d3091df5-82a6-34f1-97b3-9646bdb96442 | -10.3129 | -50.5341 | 2024-10-05 02:46:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 143.1 |
| b04218f9-c333-3bfa-b9e0-c2acb1df37ae | -10.3131 | -50.5128 | 2024-10-05 02:46:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d9898166-06e8-3983-a03d-34e0b15b77e1 | -10.3315 | -50.5535 | 2024-10-05 02:46:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d035b614-b705-3aa9-a34b-36739ba030a5 | -10.3318 | -50.5322 | 2024-10-05 02:46:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| bcf705ed-a487-3feb-aea5-b560cdb47197 | -10.4424 | -50.7336 | 2024-10-05 02:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 4ca59e1b-5830-3a59-8393-068c46da8819 | -11.0966 | -54.2336 | 2024-10-05 02:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e2c2bac8-4b71-3f67-a5ea-77e031c74bd9 | -11.1155 | -54.2319 | 2024-10-05 02:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 4c862579-714e-3cc6-80ec-8fd64644b49b | -11.896 | -56.9354 | 2024-10-05 02:46:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 84dcea2c-d81c-34b1-8fbe-ddd29edd945f | -13.1362 | -51.1313 | 2024-10-05 02:46:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 8f0bb96c-eac6-3514-9c27-fe6fe7abaadf | -13.3976 | -61.957 | 2024-10-05 02:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 709f6ca5-8eb9-3df4-b3ae-0a2ac54bba64 | -13.3978 | -61.9376 | 2024-10-05 02:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 5f2238da-cc88-38fd-b05c-9c0ef9d15703 | -13.995 | -47.2572 | 2024-10-05 02:46:24 | GOES-16 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 12384ede-79b7-359b-9377-84757a13ce3d | -15.5597 | -57.4553 | 2024-10-05 02:46:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| fec8ec05-5c49-30c6-b30b-d27441a24410 | -15.5791 | -57.4532 | 2024-10-05 02:46:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 80871365-a60f-3b38-98f1-ea71999b5174 | -16.5544 | -57.2032 | 2024-10-05 02:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| fddcb2e3-b4bd-39d2-b100-31883d4edc18 | -16.5742 | -57.1805 | 2024-10-05 02:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 9e8eb474-b630-359a-9dc8-56f81d6aefed | -16.5745 | -57.16 | 2024-10-05 02:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| e5970ee9-2e71-3e5a-b4ce-1ae5fa1679bf | -16.4155 | -57.3619 | 2024-10-05 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| cacdd169-b82a-3af6-a26d-8bf25fccd771 | -16.5345 | -57.2259 | 2024-10-05 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| e257ef43-e7dc-30c4-8ec7-54acc2e2fb9a | -16.5537 | -57.2442 | 2024-10-05 02:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 4841cd6e-ab80-3b39-b598-977136355c2e | -16.554 | -57.2237 | 2024-10-05 02:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 214.7 |
| 2ce20103-dbfe-375b-899e-ce6ba010b72b | -16.6402 | -55.5243 | 2024-10-05 02:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 2ea02048-5943-3ecf-964c-c4610345eb95 | -16.679 | -55.5402 | 2024-10-05 02:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.0 |
| b5a1551f-4574-31aa-863b-4b8214e6c5cd | -16.6405 | -55.5035 | 2024-10-05 02:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| d30c090e-a0c2-394b-bcb8-0c5610dfe932 | -16.6601 | -55.501 | 2024-10-05 02:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |


[Clique aqui para ver as próximas entradas](README35.md)
