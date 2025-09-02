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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4db6160f-bed8-30e6-8642-39ff1dcf47c7 | -10.2792 | -47.478 | 2025-09-02 13:20:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 598c953d-d55d-34d2-8e74-c2496b243f33 | -8.8638 | -50.5847 | 2025-09-02 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 324.2 |
| 5e6f286c-25e1-34cd-82c6-5413aaa78eac | -11.8521 | -51.5166 | 2025-09-02 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 2e55f8dd-66bd-3169-8fff-f02c8ed22038 | -14.0502 | -44.5779 | 2025-09-02 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| d515ab57-d02f-3be3-9b6b-0523dedc0e2d | -4.9122 | -43.2103 | 2025-09-02 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 136.7 |
| bad73ad6-0328-3b32-affb-4600bcdce447 | -9.7294 | -48.9834 | 2025-09-02 13:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 30ca5312-8731-3f6e-b3b2-333687e15f2d | -7.5477 | -61.3247 | 2025-09-02 13:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| e2cebf60-87d2-3a99-9032-6f56c60c0ec3 | -11.672 | -52.168 | 2025-09-02 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 20bea3d4-a027-3892-99ce-3ed322fb12d0 | -6.8911 | -45.8538 | 2025-09-02 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 214.9 |
| ba0c4863-4160-3c3e-9b93-5b65fb3ec1f1 | -7.5489 | -45.729 | 2025-09-02 13:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3e8f04fc-b645-3cb4-b37d-fcc544989fa3 | -5.8882 | -42.9988 | 2025-09-02 13:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 7e767f44-d247-377c-a6c2-e7f3715b3b07 | -6.9754 | -43.2326 | 2025-09-02 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.6 |
| 12735fb0-c38d-37e6-ab47-5262b1307017 | -9.4794 | -46.4994 | 2025-09-02 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 689f2574-dfe2-316a-9f0f-9aec4ea3651f | -11.4297 | -46.8223 | 2025-09-02 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 910eb3fa-ec8f-3df8-9619-00cb632481cc | -5.9513 | -44.2707 | 2025-09-02 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 3cbeded1-eef7-37e2-8b5d-104970cebbd6 | -9.7485 | -48.9598 | 2025-09-02 13:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5e9f5c21-3bf4-3f67-8ea2-5b4089c58b60 | -9.5025 | -57.8032 | 2025-09-02 13:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 4c45768f-7747-3c48-ae12-bcc004cc65a9 | -11.8653 | -50.6219 | 2025-09-02 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 0d0efb70-16b4-3f88-bc11-1383bcec0f6e | -7.1089 | -44.7703 | 2025-09-02 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e0b7bb2f-d28e-3e85-956c-8d7365ceb8d1 | -11.672 | -52.168 | 2025-09-02 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 9d6577d2-cc64-340b-9dbf-918624082c24 | -8.8281 | -45.7828 | 2025-09-02 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| a79f8c72-e444-3eb7-820f-1bc79dd949d7 | -11.8521 | -51.5166 | 2025-09-02 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 3e7b2585-6343-3405-afb2-54c2380f2e44 | -8.8659 | -45.7788 | 2025-09-02 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 541d985e-92df-3c2a-9d94-24271c0fae38 | -7.5476 | -61.3437 | 2025-09-02 13:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 2677bfed-f584-319b-a986-412be56cd707 | -11.8518 | -51.5378 | 2025-09-02 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 109fb38f-8450-3b58-80ab-6e2a796a9cd6 | -11.6715 | -52.21 | 2025-09-02 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 4e3bc11c-ec90-348d-a95c-a9bba738b787 | -8.8451 | -50.5864 | 2025-09-02 13:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 155.2 |
| f040935b-2f26-358e-9b0f-842fcd6fe296 | -6.7909 | -52.8165 | 2025-09-02 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| fabd5948-568b-3f89-9043-4dd4e3396d8d | -8.6883 | -62.4002 | 2025-09-02 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 6861f88d-c329-37f5-91ae-6b41e03832bf | -6.8466 | -52.8132 | 2025-09-02 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c1ce4538-d2f8-3750-bc45-0c773dfdc722 | -11.1033 | -44.6548 | 2025-09-02 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 309.3 |
| a2bc64f9-fd10-3fae-8e9f-fd278f9bcdf9 | -11.6527 | -52.191 | 2025-09-02 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 0b5f3285-090d-33c9-8fe9-8420c805d982 | -8.847 | -45.7808 | 2025-09-02 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 0caa8f1a-11c1-3907-93c0-ba9967e151c0 | -5.97 | -44.2693 | 2025-09-02 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b4dfbd43-e3fe-39aa-b3d2-d9565cb8f138 | -13.3082 | -46.8229 | 2025-09-02 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5eab98fe-e10f-3af8-a83a-633555b8979a | -9.7294 | -48.9834 | 2025-09-02 13:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e194aad8-e782-3038-b123-64a83d8c0d52 | -11.6647 | -57.3533 | 2025-09-02 13:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 913e6fc5-ad08-3211-b5f7-cb2de9b9fa02 | -11.1252 | -50.5982 | 2025-09-02 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| cf7b185f-c164-30ac-8a46-81d7779f6e77 | -7.5477 | -61.3247 | 2025-09-02 13:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 8cd56b69-8356-3d5f-a8d9-045e89e0e868 | -11.3907 | -46.8724 | 2025-09-02 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 40874d73-700d-3a42-b1e7-167b2205d91a | -11.8138 | -51.542 | 2025-09-02 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 4d2d1bb3-61cb-3b1b-a212-6861ecb64fa2 | -11.6717 | -52.189 | 2025-09-02 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| e204e84a-ab1f-3913-92de-6fb24c22d0c6 | -8.02 | -44.084 | 2025-09-02 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 19414dd8-6141-398e-9e1e-08cf3b0b67cb | -7.9351 | -46.4559 | 2025-09-02 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| fada8067-15fe-35a5-bf71-b25328a087f1 | -6.9629 | -44.3707 | 2025-09-02 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6747a782-1d9b-3474-8525-6f60acc63d80 | -7.5489 | -45.729 | 2025-09-02 13:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ecdd9853-de96-3ac8-93c4-386b339aa1f0 | -6.9632 | -44.3477 | 2025-09-02 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 306fbf30-be0a-36c5-84a5-a601ee096b97 | -7.1091 | -44.7474 | 2025-09-02 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c9cba3b5-08b5-3c2a-9b41-cd7d00118b85 | -9.7483 | -48.9814 | 2025-09-02 13:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 044a9cb9-3277-3d0b-a989-a5b15c5e6fb8 | -8.8656 | -45.8014 | 2025-09-02 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a5f5c602-fce5-331a-8efa-7a5728089388 | -11.8656 | -50.6005 | 2025-09-02 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 99afc986-e8fe-35ce-ab55-22f0fe7b6fe0 | -11.1037 | -44.6315 | 2025-09-02 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 8a991dcf-d281-311f-a75f-2bc1b56e7f0f | -6.9942 | -43.2308 | 2025-09-02 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 144.2 |
| 676a4941-91a5-3aa4-abfd-0a4522625002 | -8.8638 | -50.5847 | 2025-09-02 13:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 157.3 |
| f93a4ba2-0fa2-3a36-90a0-68c5b1a31b0a | -4.9124 | -43.187 | 2025-09-02 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 81b8f6ef-bbd2-35ac-be7b-2a43b2d3ef1e | -11.1029 | -44.678 | 2025-09-02 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| e9f82760-d1e7-388c-840a-23cab3eec63a | -11.0841 | -44.6575 | 2025-09-02 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 39e377b2-6bcc-3b55-b058-89bf2fac569e | -4.8936 | -43.1882 | 2025-09-02 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 509b1f7c-1704-3edc-b2fa-a7a1251ae8cb | -11.8328 | -51.5399 | 2025-09-02 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 1cd5fed5-a02d-3921-b3d8-0a57fa68668f | -6.2038 | -43.3475 | 2025-09-02 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d5c866fb-2bca-3c88-827d-223f110d2a67 | -8.8467 | -45.8034 | 2025-09-02 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 921fc968-68fb-336c-a8ee-90f5bb06df05 | -9.5025 | -57.8032 | 2025-09-02 13:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 4d2f1d28-f3f0-3d39-a79d-df44c681ccd2 | -4.9122 | -43.2103 | 2025-09-02 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 48e7c0fd-c5c5-3214-8195-d9bbf160fd49 | -11.5694 | -47.6081 | 2025-09-02 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 62c19ea3-bb38-3812-942b-49ecfa3735a3 | -11.653 | -52.17 | 2025-09-02 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 72b7a05e-6099-3184-a4e2-dc44d1bcd048 | -12.9192 | -56.9873 | 2025-09-02 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a4e6990c-9b2e-36e1-bb7c-4493beba401a | -12.5769 | -44.7814 | 2025-09-02 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 4fea8e1b-c4dc-34ba-a5ae-4649765ce13b | -5.9511 | -44.2937 | 2025-09-02 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 5048ef66-1e69-3a4f-9e9f-1cef7c40c33d | -6.5305 | -44.454 | 2025-09-02 13:30:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 69885219-6fbc-3f9c-8952-a73c8f4235ac | -10.0623 | -48.0978 | 2025-09-02 13:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 408d4941-6e36-33fd-af44-c00e2988fbe6 | -5.9698 | -44.2923 | 2025-09-02 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 4040d838-bcba-35e0-b5d1-0d791501ee09 | -7.9165 | -46.4354 | 2025-09-02 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 0c47f915-8f81-36a8-b00c-b08ac42968ce | -7.9163 | -46.4577 | 2025-09-02 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 74ddbc05-b672-35d1-a1be-971e14dab1a9 | -5.3974 | -43.3867 | 2025-09-02 13:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d7621bcf-030c-36ab-a7a3-3187112b5d79 | -5.9513 | -44.2707 | 2025-09-02 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 4a890190-c3fb-3c5a-b360-ce70427f7c0f | -6.9754 | -43.2326 | 2025-09-02 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| 9da5c654-757b-3cd8-8663-e08db147c8cf | -8.0203 | -44.0608 | 2025-09-02 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 409a2100-6b34-3a8e-ab40-5713d70720ef | -6.185 | -43.3491 | 2025-09-02 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 73298585-c0da-3e4a-922a-bde29f6de7de | -8.65 | -62.6103 | 2025-09-02 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.3 |
| cbeeca87-dba9-3635-a352-55055a13e835 | -11.1249 | -50.6195 | 2025-09-02 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a8ff19a2-fbe1-3ab9-8951-8fbd8cbf2f0b | -11.9415 | -50.6131 | 2025-09-02 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c526de04-6971-3552-a261-940cb80fcd96 | -8.8659 | -45.7788 | 2025-09-02 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| fcc31f10-8591-3c9d-8af3-d2f2cae6ec43 | -11.1029 | -44.678 | 2025-09-02 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 4a79c78b-cf6e-3625-a140-ba3a8cb6ef9a | -11.672 | -52.168 | 2025-09-02 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6d3a5d07-a322-33a5-b068-a107614b5e21 | -6.9754 | -43.2326 | 2025-09-02 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| fdba3c59-cf0d-3a3d-84a8-3eaa05a87c62 | -5.717 | -45.3809 | 2025-09-02 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 77a702b2-b6c5-3bc9-a001-c655f9bb5c1c | -11.1037 | -44.6315 | 2025-09-02 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.6 |
| a89a20cd-5180-3ef3-8b2c-82a1463e6c39 | -11.1252 | -50.5982 | 2025-09-02 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 9e6b4425-f910-391d-bf51-7a9a49422975 | -11.6527 | -52.191 | 2025-09-02 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 1cca25f1-80cb-331d-81a0-aa8db345061e | -7.9351 | -46.4559 | 2025-09-02 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| f187ad7c-2f17-3e94-8f1e-55690bdcd869 | -11.6647 | -57.3533 | 2025-09-02 13:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 533b110c-ead4-30c0-b334-9892bb21b3d4 | -6.2676 | -44.4984 | 2025-09-02 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d379de98-6ead-35ce-acf8-f1dd45b18b8f | -11.834 | -51.4551 | 2025-09-02 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 641cf56f-6e13-3509-baa7-e5464e220cf3 | -7.5476 | -61.3437 | 2025-09-02 13:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 127.8 |
| cc6351ac-1b94-38f8-9c50-c74645c3eed9 | -6.185 | -43.3491 | 2025-09-02 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| f58a695a-6296-31a1-8501-e93536865c8f | -11.3692 | -43.6577 | 2025-09-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| ba91711a-374e-3aae-a8b0-774e8727f4b6 | -7.1091 | -44.7474 | 2025-09-02 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 7a3095dc-ecd9-3952-97c6-b01e9a225938 | -14.0508 | -44.5543 | 2025-09-02 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| d16315e6-fa8c-389a-8a46-49767e2c7004 | -5.9698 | -44.2923 | 2025-09-02 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 10be0903-dfa8-363d-bcc3-c760a8b9d0aa | -11.5694 | -47.6081 | 2025-09-02 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |


[Clique aqui para ver as próximas entradas](README97.md)
