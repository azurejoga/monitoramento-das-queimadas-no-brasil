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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb6f7497-c1e2-3fa4-8226-8193d7abd2b4 | -10.6649 | -46.159199 | 2024-09-30 00:26:39 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6b39493-d501-3349-8ff6-aa96a99b0a5a | -9.9411 | -44.023998 | 2024-09-30 00:26:43 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a8e58d28-b0e4-39b2-a8aa-6cfc2f8809bd | -9.9329 | -44.033501 | 2024-09-30 00:26:43 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 836b888f-17e2-3096-ae5d-a98b958bc482 | -10.7114 | -47.9692 | 2024-09-30 00:26:44 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a273f104-e285-38a2-88c6-31d10f9b37a0 | -9.0154 | -40.558201 | 2024-09-30 00:26:45 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| ad3415d1-155d-3e75-899d-2afa4e55f95d | -9.0171 | -40.565701 | 2024-09-30 00:26:45 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 065188fd-2b83-33f9-b3e2-97a44b59e5b7 | -10.756 | -48.7215 | 2024-09-30 00:26:46 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0af09366-5e20-33da-9094-cb162dc5dfa7 | -10.7587 | -48.7346 | 2024-09-30 00:26:46 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3bf46e5-ef34-3287-88c5-b8b14d92b086 | -8.714 | -40.461102 | 2024-09-30 00:26:49 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| ac2f69ce-e9f0-3b44-8aec-aada0573edb9 | -10.1934 | -46.8727 | 2024-09-30 00:26:49 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e476a45d-9272-3c9a-90f3-2a6467e7a575 | -10.4261 | -48.164299 | 2024-09-30 00:26:49 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3ba78ca-6202-3702-ad7d-730bf1491c8c | -10.4311 | -48.188099 | 2024-09-30 00:26:49 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5ced729-8214-3f54-ae57-29006255b442 | -10.4336 | -48.2001 | 2024-09-30 00:26:49 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a01ff2f6-f526-32a9-b779-50c0f7bc78a6 | -9.4855 | -44.056999 | 2024-09-30 00:26:50 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 07a1f25d-c71b-3afa-8503-7787e35d8bc8 | -10.4163 | -48.166401 | 2024-09-30 00:26:50 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4b93a7c-617c-34af-9496-f2531bfdfea2 | -11.061 | -52.401901 | 2024-09-30 00:26:53 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4e09652-4d2f-3456-8896-293a5fa4b661 | -11.0657 | -52.425701 | 2024-09-30 00:26:53 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dae20e41-93e1-3f28-b6a6-10df18a6c9be | -11.0704 | -52.449501 | 2024-09-30 00:26:53 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0dea503e-bbfb-3a9f-ae13-2d302c212209 | -11.0513 | -52.403702 | 2024-09-30 00:26:53 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47ffe5f5-ceb4-3877-87c2-53e319c0c3d1 | -11.056 | -52.427502 | 2024-09-30 00:26:53 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a40920ed-e574-35b3-acfb-a64826a2de6f | -11.0607 | -52.451302 | 2024-09-30 00:26:53 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da9d4a68-92b5-3013-bd50-ae9fb9e54dae | -11.0417 | -52.405602 | 2024-09-30 00:26:53 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0379d1c9-5107-358f-9106-6076a8fb9a38 | -11.0464 | -52.429401 | 2024-09-30 00:26:53 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6265eb47-9a7d-34d4-963b-083bf29e8074 | -11.051 | -52.453201 | 2024-09-30 00:26:53 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab9edc19-f767-37c1-b82c-17bd5357e0e6 | -11.0367 | -52.431198 | 2024-09-30 00:26:54 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1db8ec20-29fa-39b2-8a77-d16ac518b241 | -11.0414 | -52.455101 | 2024-09-30 00:26:54 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 281ad371-e4b3-3550-a961-8c65465080aa | -8.4064 | -41.2659 | 2024-09-30 00:26:57 | METOP-C | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f92fbd5-a7e2-3b7f-b7e7-b1c8a86b18da | -8.3305 | -41.161301 | 2024-09-30 00:26:58 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 03f2ac65-b3a9-3be8-b622-cefc36b5ba7e | -7.8834 | -39.3041 | 2024-09-30 00:26:58 | METOP-C | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| aa417f0d-6a1b-3fd5-bb1c-3c6cef6602ce | -7.8855 | -39.312801 | 2024-09-30 00:26:58 | METOP-C | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 511715ac-67c0-3e40-8e92-f3b4e0529c4b | -7.8876 | -39.321499 | 2024-09-30 00:26:58 | METOP-C | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f34b10c3-eaab-365e-90d5-ae0f11f09b44 | -7.8896 | -39.3302 | 2024-09-30 00:26:58 | METOP-C | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 7159c4cd-8b78-3a9f-98bc-c3385db7c213 | -9.5495 | -46.591301 | 2024-09-30 00:26:58 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac1f669e-4f8b-3d5d-aeee-4c00523d7b3d | -8.4333 | -41.917198 | 2024-09-30 00:26:59 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72824981-3cf9-33db-9f0f-992fa73c1e03 | -8.4349 | -41.924198 | 2024-09-30 00:26:59 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0df50565-4ff4-3d03-bc9e-46d521886b28 | -6.7459 | -35.2169 | 2024-09-30 00:27:01 | METOP-C | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a35bdb6b-1f57-3bb5-8aa4-f1897b3b0786 | -6.75 | -35.233299 | 2024-09-30 00:27:01 | METOP-C | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 2077e285-256a-3fd0-9359-cdbf5fa0e7f6 | -6.7363 | -35.219299 | 2024-09-30 00:27:01 | METOP-C | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| aee77358-1ec4-3017-966d-c0ef6b7912db | -8.64 | -44.0494 | 2024-09-30 00:27:04 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4286b5b5-adc0-3584-957d-d49b66fbfc76 | -8.9247 | -45.654301 | 2024-09-30 00:27:05 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4dddcc57-a39a-3193-9276-79fec44b3246 | -8.9265 | -45.662399 | 2024-09-30 00:27:05 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e2fce91f-958f-3070-a488-4af759c1ec9e | -8.7618 | -45.148899 | 2024-09-30 00:27:06 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d818985-b896-3b9b-a7a1-17b95ba71916 | -8.7542 | -45.2075 | 2024-09-30 00:27:06 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4a8bf0c-253b-341f-9676-8e7d849dc2cf | -8.5169 | -44.694599 | 2024-09-30 00:27:08 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| feb1288a-d2f7-3e48-adc4-65b81e7368e5 | -8.5186 | -44.702 | 2024-09-30 00:27:08 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 51c0c2b5-185a-3b82-84a8-d3b7eeb3cd97 | -8.5203 | -44.709499 | 2024-09-30 00:27:08 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e18a7b0d-821b-375e-a3f7-1b997df400b8 | -8.5219 | -44.7169 | 2024-09-30 00:27:08 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 384436bd-2977-3ff6-b685-36cca034f044 | -8.5236 | -44.7243 | 2024-09-30 00:27:08 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4e49386-e12e-3153-a416-f253fdb7cdf7 | -8.5252 | -44.7318 | 2024-09-30 00:27:08 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 25ff412a-f894-300c-b70b-dba0621933bd | -10.2131 | -52.691101 | 2024-09-30 00:27:08 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 593f51df-f11e-3a78-bdf7-37dbf847d998 | -9.5731 | -50.177601 | 2024-09-30 00:27:10 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f068def8-5a09-3423-9ad5-1121774db6fc | -7.9243 | -42.754902 | 2024-09-30 00:27:11 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 39c29140-5d4e-3435-9148-4744c693089d | -7.9259 | -42.761799 | 2024-09-30 00:27:11 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf008198-c31d-359d-b4cd-ebff0ee03766 | -7.9114 | -42.743301 | 2024-09-30 00:27:11 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1483da79-cee1-3bba-84a7-332beee7a894 | -7.913 | -42.750198 | 2024-09-30 00:27:11 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a130e372-881b-39e1-93e5-622cf57ea3e9 | -7.9145 | -42.757099 | 2024-09-30 00:27:11 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 31c7e2a4-7a43-353f-b4de-93d32f7d5ba8 | -7.9161 | -42.764 | 2024-09-30 00:27:11 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5a3dd821-b18b-3369-8894-c7376f4036f8 | -7.9177 | -42.770802 | 2024-09-30 00:27:11 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 98f155a2-5b70-3bc6-9103-1488bf090583 | -7.9032 | -42.752399 | 2024-09-30 00:27:11 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 70013c37-1274-39a5-ac95-e2a80e1b9f67 | -7.9047 | -42.7593 | 2024-09-30 00:27:11 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b20d10e4-c82c-3791-a447-1508f5e87fa6 | -7.9063 | -42.766201 | 2024-09-30 00:27:11 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 83906d2d-d5e0-3851-a84a-3d31a8ce77c0 | -8.4278 | -46.335499 | 2024-09-30 00:27:16 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67411254-4fae-3a53-ad7a-bd06be583729 | -8.4161 | -46.328999 | 2024-09-30 00:27:16 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a21523e0-2538-3586-a89c-1f1342a6faff | -8.418 | -46.337601 | 2024-09-30 00:27:16 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03f443df-1fbe-31f2-ae38-4cb27270bd81 | -8.4199 | -46.346298 | 2024-09-30 00:27:16 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29ff9704-5dae-3e53-9ec2-64c22c4cc187 | -8.4218 | -46.355 | 2024-09-30 00:27:16 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae10315e-0b04-3942-8b49-c7903c2b90b2 | -8.406 | -46.376701 | 2024-09-30 00:27:16 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 943a80fb-db60-3229-9952-ba4dd879bdd5 | -6.7869 | -40.122398 | 2024-09-30 00:27:19 | METOP-C | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 409440a5-d3dd-327c-8ba6-39b1427601eb | -6.7888 | -40.1306 | 2024-09-30 00:27:19 | METOP-C | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c2248a67-ccce-3ca1-bf10-71c02f0f28c3 | -7.2801 | -42.239498 | 2024-09-30 00:27:19 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4cc90cd5-3a3e-3aae-b4e4-6542a3125a3d | -7.2817 | -42.246498 | 2024-09-30 00:27:19 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3be603c3-7b47-3780-a2e9-cbffaa80bba2 | -7.2833 | -42.253399 | 2024-09-30 00:27:19 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bac5f6f9-1dc9-388d-a4ea-42265b0a1a95 | -7.5644 | -43.8452 | 2024-09-30 00:27:21 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a233570a-4a35-36e2-b640-82ef6992ab8a | -7.566 | -43.8522 | 2024-09-30 00:27:21 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 608fb6eb-2add-30d2-b4de-bcc8228d443b | -8.1733 | -47.6605 | 2024-09-30 00:27:24 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47e8139d-2ea6-3145-852d-e1588e8c5708 | -8.1755 | -47.670799 | 2024-09-30 00:27:24 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 803f396c-b5cc-3de7-a671-037d11ff0711 | -7.0515 | -43.945301 | 2024-09-30 00:27:29 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d72fbfd4-69e5-3fac-a135-e9fe217e546f | -7.0531 | -43.952301 | 2024-09-30 00:27:29 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b75c0500-1db2-3998-8875-aba9de60673a | -7.2427 | -44.929901 | 2024-09-30 00:27:30 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f165adfd-4432-36a3-b729-e6531b37b77b | -7.2443 | -44.937302 | 2024-09-30 00:27:30 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55101c94-a3ac-3b9c-a2c2-117c4f56ad44 | -7.2461 | -44.991199 | 2024-09-30 00:27:30 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4eb08de4-30a2-3834-aadd-2482d047d643 | -7.2478 | -44.9986 | 2024-09-30 00:27:30 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a42352a1-a47e-33ec-8f9f-f0964c6c8822 | -7.238 | -45.000702 | 2024-09-30 00:27:30 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 135e4ba2-e9de-30b1-8bcd-6f1ccf8b2fae | -7.2396 | -45.008099 | 2024-09-30 00:27:30 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86ae0402-ff9e-3750-b183-779ddfae8986 | -7.2413 | -45.015499 | 2024-09-30 00:27:30 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96149d2e-2067-3be3-91ab-58398b8a3f94 | -7.243 | -45.0229 | 2024-09-30 00:27:30 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edf62881-5b3f-326a-bfda-179cba45e7d7 | -7.2348 | -45.032501 | 2024-09-30 00:27:30 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d80acaa9-9717-30c6-ab12-a15d7d61e779 | -7.2365 | -45.040001 | 2024-09-30 00:27:30 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 323131c4-c9ad-3d54-8903-2e4d67a82ed4 | -6.5403 | -42.6991 | 2024-09-30 00:27:33 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9d8b12c7-9ff7-3bba-93e7-7321eebcf4e0 | -6.4277 | -42.927299 | 2024-09-30 00:27:36 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| ae907c88-f5d1-3d60-9567-3964901a656d | -6.41 | -42.8951 | 2024-09-30 00:27:36 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| d92d9a5c-7048-30a1-9ec1-55d87d6c939d | -6.4116 | -42.902 | 2024-09-30 00:27:36 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 281e5af0-a086-342a-9c08-e5351153b277 | -6.2754 | -42.533699 | 2024-09-30 00:27:37 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 957bc9b1-4598-3e6f-baf2-2eefed00cbdd | -6.2656 | -42.5359 | 2024-09-30 00:27:37 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 423f63f2-aed2-39d7-9d3b-b78e771f2ea9 | -6.2672 | -42.5429 | 2024-09-30 00:27:37 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4e4e42fc-71f5-3d60-98e1-5d3332b45277 | -6.5046 | -43.624298 | 2024-09-30 00:27:37 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 053c756f-e596-3182-803b-1b86287b1b96 | -6.2728 | -42.701698 | 2024-09-30 00:27:37 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 861ac6a3-9a38-3af6-b472-cd880812a663 | -6.2744 | -42.708599 | 2024-09-30 00:27:37 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61b0d2fb-9b7a-3d81-9fae-db1bc5dbfd46 | -7.055 | -46.208599 | 2024-09-30 00:27:37 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d5ff223-23e8-3557-ad20-489bf8213c07 | -7.0569 | -46.216801 | 2024-09-30 00:27:37 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
