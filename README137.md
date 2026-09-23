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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7aed034-af4d-3ca8-8d27-530215423828 | -6.6317 | -43.73 | 2026-09-23 13:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| c728fab8-c9c6-3413-be3c-c69ec20e3fd9 | -8.449 | -47.4938 | 2026-09-23 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 1a360610-9358-3d69-a183-7750d23e6d85 | -11.3551 | -43.3764 | 2026-09-23 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 07369519-5a15-3da4-8453-521204734880 | -6.166 | -52.05 | 2026-09-23 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6460d0ec-6ca0-32eb-9014-48d3d4d3bf3c | -6.9228 | -42.8852 | 2026-09-23 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| bbab449e-56ed-3d6e-ae71-dc1f980cca48 | -6.6129 | -43.7317 | 2026-09-23 13:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 344.4 |
| 03a3f8c7-b1ab-3f57-9395-2c98d3256521 | -6.2208 | -41.6651 | 2026-09-23 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 638c051e-4e0b-3f12-ada9-d49bea186a33 | -8.9013 | -45.9556 | 2026-09-23 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 948efb72-a4c7-3f41-a166-e3ee1c972e44 | -11.305 | -44.0432 | 2026-09-23 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 3bbe3bd2-61d1-3f47-999f-2b5d4df3b88f | -11.4782 | -47.3529 | 2026-09-23 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 7f04086b-2b43-3116-9258-716e1bb16be3 | -9.5731 | -47.9529 | 2026-09-23 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 3db39330-0811-3654-9879-a4aad03d1363 | -11.6605 | -43.4476 | 2026-09-23 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 41cf51fb-9240-3792-9afd-9947377d3e9c | -9.6108 | -43.9477 | 2026-09-23 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 1ffda272-1322-3654-aafe-09bb68bd4f4a | -7.0885 | -52.7575 | 2026-09-23 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| e45d3fa4-f512-363e-9c99-9f88de402db2 | -7.1033 | -43.571 | 2026-09-23 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 4d37da8c-8088-3bc5-8f25-f06dc637b791 | -6.9138 | -43.7049 | 2026-09-23 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 70b6aa26-0ec7-392c-9d97-974871c09b14 | -6.5763 | -45.4968 | 2026-09-23 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 091c29fa-c187-32e4-b765-938c302d7581 | -11.6601 | -43.4714 | 2026-09-23 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.6 |
| f970ee1a-4ff6-3e27-b44a-be347ca6a1b6 | -7.1392 | -42.0811 | 2026-09-23 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 111.2 |
| 66920d65-7b5a-3bf8-a556-3892720e9204 | -6.2399 | -41.6394 | 2026-09-23 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| eeb0fa79-8746-31bf-939b-9a4817c22b76 | -7.0352 | -44.6396 | 2026-09-23 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 6ea20696-9fb5-3d7b-ad86-07869dd2ec1a | -8.9205 | -45.931 | 2026-09-23 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 248.5 |
| 3acf4606-06cd-3d97-8047-4ac5105386b2 | -6.2396 | -41.6634 | 2026-09-23 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 9bc7cb1e-e078-352c-a467-fe0ae1aeb0bf | -6.9174 | -41.6957 | 2026-09-23 13:40:00 | GOES-19 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| f6834434-1b54-3aec-a5d3-87725926a23f | -8.0921 | -44.3538 | 2026-09-23 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 7dd4f7a2-a37b-3d01-8586-f920cd24f146 | -6.8985 | -41.6976 | 2026-09-23 13:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| aec352d3-e296-3243-99a4-3afdc83ab99f | -8.9202 | -45.9536 | 2026-09-23 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| dde7f0f5-a65c-3138-a815-aaeaf2b2b0aa | -11.1358 | -42.7914 | 2026-09-23 13:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 528dddbd-259e-38e0-9d2d-987a9951142b | -9.0242 | -48.1403 | 2026-09-23 13:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| fe31fb46-1a2c-3184-b10f-ccd8e54437a1 | -8.883 | -45.9124 | 2026-09-23 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 83eb4fce-e0d9-3280-8a27-fcb3b9b8916a | -10.9317 | -50.8955 | 2026-09-23 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 62037c6e-24a0-33af-99fc-1ae97f4420d5 | -11.1541 | -42.8364 | 2026-09-23 13:40:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 100.7 |
| e03213c1-c7a1-3aff-a64d-2075778650b4 | -6.6515 | -59.9258 | 2026-09-23 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 33eedcd3-0e44-3597-a0c5-961e0d2ae60f | -6.5953 | -45.4727 | 2026-09-23 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| d64f07ba-fbb9-34d7-a165-d465b3cb3227 | -7.1088 | -43.0792 | 2026-09-23 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 5a56e827-3eda-3e92-8ce6-9f256445cec0 | -11.4009 | -44.029 | 2026-09-23 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 9385a86c-5cb5-3f2e-900f-102f7536586c | -6.9416 | -42.8834 | 2026-09-23 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 1b9dcb63-fd2a-3908-bfd7-48c9d8b27a12 | -6.166 | -52.05 | 2026-09-23 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 6b490932-9c5e-3458-9b33-a8da1ae27afb | -6.7464 | -59.4223 | 2026-09-23 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 9fc0b563-45bd-35b7-86e9-1fce34f8d991 | -9.9163 | -45.0885 | 2026-09-23 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 8d9b40e4-adad-3050-9a52-b7331180f0fa | -8.0912 | -44.423 | 2026-09-23 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 5ff99c23-e8a4-3166-8949-6a6344dd76e1 | -11.0048 | -49.7325 | 2026-09-23 13:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 71c522b5-0d27-3782-9274-6d2cb7b8c4d3 | -9.8694 | -48.3814 | 2026-09-23 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 4fc1990c-8807-385b-8625-2617a2a40ae3 | -8.7924 | -45.6282 | 2026-09-23 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 18d019d8-72dc-3788-b3a2-5a71915d2e0b | -7.41 | -44.7198 | 2026-09-23 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| b0ef47cb-348c-32cb-bf04-b8776c8262e1 | -9.6111 | -43.9243 | 2026-09-23 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 129.2 |
| c57c9977-bb86-3021-b55e-7afc5d7b5ee9 | -11.4009 | -44.029 | 2026-09-23 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 85e077e4-617c-363f-abed-2be2d37785c9 | -8.4799 | -57.6085 | 2026-09-23 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 09d7fcdf-9e04-300a-b999-ec07f709f29a | -6.6148 | -59.908 | 2026-09-23 13:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 811f4fe0-f9e7-365d-b234-2a60d0899222 | -7.4286 | -44.7409 | 2026-09-23 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| ee8e0b1b-3eda-35e3-9a96-fb89bdd41092 | -7.1392 | -42.0811 | 2026-09-23 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 127.8 |
| ee3509cf-1384-36ed-a83a-481fe0a7fd72 | -4.2816 | -55.4297 | 2026-09-23 13:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 9d167314-ede6-3997-83f0-154bf83b5908 | -9.5857 | -48.433 | 2026-09-23 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 225.5 |
| 596f41c7-c806-332c-b79a-c61383d3eaa1 | -7.4288 | -44.718 | 2026-09-23 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 81feda1c-3b47-3cfb-b1ce-3d64f2313b20 | -6.9888 | -43.7213 | 2026-09-23 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 25a37b8d-3a0c-36b0-bfe3-57d1b9cc6813 | -6.2399 | -41.6394 | 2026-09-23 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 84f93023-d397-364b-a844-018092dd12dd | -10.9317 | -50.8955 | 2026-09-23 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| a83b141f-5d07-3f0a-b5b1-7b6aebdd775f | -9.5665 | -48.4568 | 2026-09-23 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| b8bd923f-4b3a-3686-9a4a-7792159bca65 | -8.4983 | -57.6271 | 2026-09-23 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 9fdd5cdd-6ecf-3ea9-961e-1137c59ca4bf | -10.7245 | -50.8321 | 2026-09-23 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 5a48c01e-7972-39c8-aef1-0dd302f9d1b6 | -11.6986 | -43.4654 | 2026-09-23 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| aecbc43d-765d-30ba-a15b-808351be928c | -6.8569 | -45.5415 | 2026-09-23 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 88afce1b-7c16-336d-8503-79a17f822891 | -8.378 | -45.6036 | 2026-09-23 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 5f21e211-b1c2-37e5-98c1-b2c6126118f1 | -11.305 | -44.0432 | 2026-09-23 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 161.5 |
| e669e1ab-7540-3932-97d6-8d20ea46ae9a | -11.8563 | -49.9574 | 2026-09-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 134b8bae-8a44-3be2-96be-6b95bf5a4f81 | -11.1541 | -42.8364 | 2026-09-23 13:50:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 8f4cc815-fde5-3221-9562-316a479ef1e2 | -7.1277 | -43.0774 | 2026-09-23 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| d3961a2c-6447-3592-ad72-21ed31cc4a6b | -8.754 | -44.2589 | 2026-09-23 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 76105e1f-a54b-32cd-bedf-c5b03a5dc249 | -8.7735 | -45.6303 | 2026-09-23 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 80bd75e1-eca0-3f0a-b699-cba06bbe2d33 | -6.6129 | -43.7317 | 2026-09-23 13:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 357.9 |
| 96c3a629-4ade-30d4-a7f8-b2c06ce493d2 | -9.5854 | -48.4549 | 2026-09-23 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 294.7 |
| be26d049-4c45-358e-9965-9484588d5c2b | -6.4301 | -59.9916 | 2026-09-23 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 23971b38-03ae-338b-bf0a-0e3522d94209 | -7.4153 | -42.6479 | 2026-09-23 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 9f7c0013-d91f-3103-a9ba-8c9c4f76e3ea | -11.3054 | -44.0198 | 2026-09-23 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| e29d8fcf-f795-3427-a4af-fc86379c18b6 | -9.5668 | -48.435 | 2026-09-23 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| cb2ed67f-4677-36ee-85da-d219c50ccbcb | -7.9904 | -44.9608 | 2026-09-23 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| bf55636d-cccc-3313-bbcc-d454ea3a7bbd | -11.7082 | -50.9598 | 2026-09-23 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 031f1813-afe2-3882-b7c1-e351b5eedd4c | -11.3058 | -43.9963 | 2026-09-23 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 16bff8f1-4507-35ce-871d-f063620dc855 | -6.6317 | -43.73 | 2026-09-23 13:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 8870807d-ed14-3c30-8ca1-668de3db8627 | -11.6798 | -43.4446 | 2026-09-23 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| b0d40fe0-5b63-3d3e-91dc-073ae2b529df | -9.5735 | -46.5337 | 2026-09-23 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 357.4 |
| dde27e4f-a44b-3d4b-b72d-327d47f4b045 | -3.7167 | -54.1896 | 2026-09-23 13:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 215.0 |
| 526e0e69-622a-30ae-83e6-9efb48ee06d9 | -8.4985 | -57.6075 | 2026-09-23 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 179.7 |
| ea60d882-90bb-32ec-ad77-3b3bdb07d3a2 | -7.0352 | -44.6396 | 2026-09-23 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 1d7253a8-bc2e-30ad-a9bd-924a26a485a5 | -8.0921 | -44.3538 | 2026-09-23 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| fe0da92a-8963-3f38-b0b4-7ea1e6231cb2 | -6.3014 | -59.9579 | 2026-09-23 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 1e62497e-ed40-3b0f-8acd-32cd688695d3 | -3.847 | -58.6675 | 2026-09-23 13:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| ac284bec-56d8-3f45-980c-51503da7a17b | -7.1049 | -43.4309 | 2026-09-23 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 68538378-7feb-3ec2-810b-461bcbd6f8bd | -9.6043 | -48.4529 | 2026-09-23 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 1315a720-a86e-3c06-860f-3cba7dbabcb1 | -6.6127 | -43.7549 | 2026-09-23 13:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 6e0bcecc-06c8-3f4c-9d93-39e39c72b478 | -11.7269 | -50.979 | 2026-09-23 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 5eb1a5e3-42c7-38d4-a49e-e9a73c1d7278 | -6.1178 | -59.8877 | 2026-09-23 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e0e79c92-4e65-3328-b0e7-69c030b8da5a | -6.9228 | -42.8852 | 2026-09-23 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 477b7efd-3888-3a21-bcbf-846afcbb7d47 | -5.1439 | -55.9543 | 2026-09-23 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 9099c712-853d-3af1-8db3-ae609ba9b313 | -6.9841 | -49.7777 | 2026-09-23 13:50:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| c15130a9-c6b4-30d7-a06a-02355513661d | -7.1033 | -43.571 | 2026-09-23 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 1728900f-7b64-3b9d-8956-510900409f24 | -11.2858 | -44.0461 | 2026-09-23 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 031f9532-6417-3aef-a823-62b31d4ee0b5 | -11.7079 | -50.9811 | 2026-09-23 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| dfe4762f-6470-336f-b756-e0805bb13675 | -7.0115 | -43.3696 | 2026-09-23 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 36e4b0db-a012-3d59-ab69-df60c9b8a57d | -6.8988 | -41.6735 | 2026-09-23 13:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |


[Clique aqui para ver as próximas entradas](README138.md)
