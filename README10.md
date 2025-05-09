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
| 402907fc-3735-3a0d-9951-296316225299 | -18.71789 | -47.16998 | 2025-05-09 05:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dcffb3e-3b21-3253-9f07-06d2bbf8639e | -17.53048 | -52.11653 | 2025-05-09 05:08:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5018708d-ab86-3854-8578-1def3642969f | -13.80484 | -52.24174 | 2025-05-09 05:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b571d8bc-fc7a-3642-9737-0ddfb25a40e0 | -14.20504 | -45.46969 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e9088431-f0bf-3f0c-8c59-dbba83b90fb7 | -17.36023 | -52.01707 | 2025-05-09 05:08:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bae3211-0393-3238-9e36-c983d214f5ee | -14.19919 | -45.46354 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccdd45d8-ce4c-31fe-9123-e027a033d8ad | -20.06002 | -49.36548 | 2025-05-09 05:08:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8b138d91-2415-3396-b20b-8c95b7f0473e | -19.15682 | -47.82007 | 2025-05-09 05:08:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e9fed01-4419-3eff-9ae4-43aac764786b | -13.36529 | -54.25332 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02a9bcbd-b4df-3dcf-a48c-cec4d60581e6 | -14.21847 | -45.46593 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4c3be86-b3e4-3e93-ac3c-049a71bfe555 | -14.30943 | -54.65886 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8ae7787-325e-3977-b8da-76fc007f94c4 | -14.22634 | -45.46438 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ec486e8-90da-33ab-96b9-195bb9e33fc3 | -16.24717 | -60.02478 | 2025-05-09 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da345b6f-4cce-3a84-b1ff-dd4c4538c842 | -13.09141 | -52.29525 | 2025-05-09 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c3462c1-42d0-3166-83c7-ff1826399991 | -18.26192 | -53.00645 | 2025-05-09 05:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9c3dcceb-42b1-38ed-a066-a1584154b0d6 | -12.64568 | -54.06397 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61b76217-d6eb-334c-ac3f-7f396944d084 | -20.05879 | -49.36286 | 2025-05-09 05:08:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3b884fdb-d3c5-3d19-9faa-0352829ff298 | -15.35719 | -60.18069 | 2025-05-09 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9653013d-d208-3963-804b-953685b7b3d8 | -13.3683 | -54.25814 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10e970de-632d-3b48-b84a-1a3432bf1739 | -14.64192 | -45.12036 | 2025-05-09 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c521813-806f-3587-9afe-dfe9145abf43 | -15.369 | -60.08988 | 2025-05-09 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e014753f-1754-3dce-bfea-be3b2d68fbb9 | -17.52614 | -52.11587 | 2025-05-09 05:08:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 57114511-a580-3cb3-9a08-95c9bf5c8454 | -13.08754 | -52.29534 | 2025-05-09 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2f14942-0f32-3a09-a56c-29f6d951bbd3 | -13.37192 | -54.25871 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d20fc120-71de-3c54-bd2a-cc7c01ee913a | -12.27647 | -57.26721 | 2025-05-09 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b56cf34-6b38-3782-8364-26a108a0ab39 | -16.1077 | -59.77262 | 2025-05-09 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87a5be49-690f-304f-86b6-8d661a62979e | -12.17486 | -54.23803 | 2025-05-09 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ec857d9b-3c25-3566-b73c-d562e11f1d09 | -19.84569 | -54.2176 | 2025-05-09 05:08:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d73d532-d878-3b17-aff8-dd35ecb81946 | -12.72838 | -54.97376 | 2025-05-09 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97e834b2-1f4f-35b4-ae23-acf9cce43348 | -13.37917 | -54.25983 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 68b54638-b79b-3ebb-9783-d0760d64c715 | -11.6627 | -58.26487 | 2025-05-09 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41abbd7b-2ae4-371a-81ab-41096881a900 | -14.21204 | -45.46515 | 2025-05-09 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7f3862e-70f3-3f39-b60b-84916a3b7cf0 | -13.80201 | -53.30054 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b9c4d88-b741-33b6-a607-ccfaa5c59296 | -13.08805 | -52.29177 | 2025-05-09 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 933d9663-443b-3fec-a9bc-82faa9022ef3 | -13.37795 | -54.26827 | 2025-05-09 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99f03886-b3f9-3452-9a5c-b6d32003e551 | -13.08736 | -52.29465 | 2025-05-09 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75f4450e-8955-3157-8d4f-5bcecc01b883 | -17.23048 | -47.391 | 2025-05-09 05:08:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3168ee93-6b1e-391f-b19d-4d8702dd4b71 | -13.048 | -53.72239 | 2025-05-09 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8bdc1c6-fd7b-3a65-82d7-ce28fc8c2b8e | -13.05171 | -53.72291 | 2025-05-09 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 828370ce-bc39-386b-ba24-070d872e16fe | -18.87664 | -52.42442 | 2025-05-09 05:08:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8787df99-36f1-3a23-a407-bd7fd3ee5999 | -8.07 | -43.1216 | 2025-05-09 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 04b8d221-7fd7-3a05-8db1-f91406007de5 | -24.9341 | -51.91476 | 2025-05-09 05:10:00 | NPP-375D | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3e2425df-d220-3870-9594-3637aaeb9f52 | -25.19819 | -49.32225 | 2025-05-09 05:10:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5492ceee-b0d5-3364-805a-3f92ae110443 | -21.17938 | -48.67719 | 2025-05-09 05:10:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f3886d63-301d-3ba6-b5ce-2b6eceef3037 | -21.78696 | -52.74413 | 2025-05-09 05:10:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e97175a-8f3d-3405-93c6-8ccf79c94bc7 | -22.99864 | -52.44192 | 2025-05-09 05:10:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1b0a2e3b-c77c-343a-a736-ce661d7ed2a3 | -24.92923 | -51.91421 | 2025-05-09 05:10:00 | NPP-375D | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 30c9dd8c-acc6-38fa-a814-59f7d5454a51 | -21.35528 | -48.73698 | 2025-05-09 05:10:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c62e5d82-cd0c-3718-abe9-f0619ab1a697 | -25.19208 | -49.32612 | 2025-05-09 05:10:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bf6de458-e88c-36b0-9481-d6ea53e80f43 | -22.31535 | -55.16895 | 2025-05-09 05:10:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8c6fa74-ee6e-3d1e-a925-00bd527da286 | -21.0512 | -55.99888 | 2025-05-09 05:10:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 447b8771-2138-350b-acef-bf8d807ba19b | -21.78643 | -52.74859 | 2025-05-09 05:10:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72e479b0-f6c9-3036-aa23-ecd2a5b7a747 | -21.36098 | -48.73765 | 2025-05-09 05:10:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04d43bc1-0e40-3450-be8c-cc4a7a4e712c | -21.18018 | -48.67902 | 2025-05-09 05:10:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6f7e68c6-e223-3ee9-8a08-ef32a2614d37 | -24.24192 | -50.7396 | 2025-05-09 05:10:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| be544956-15de-36c9-b394-1737ad7b1d14 | -21.17898 | -48.68128 | 2025-05-09 05:10:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b509f578-c161-3f7c-948d-cc2d88000cfc | -21.05182 | -55.9944 | 2025-05-09 05:10:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d4f3160-2e23-3b6f-90c8-a7bf35d7f6a9 | -21.05545 | -55.99498 | 2025-05-09 05:10:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2fb713b-c622-3a8d-8b1a-f33e00b5ea46 | -21.782 | -52.74801 | 2025-05-09 05:10:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00d3317b-6165-3d4d-bf9c-62384671cd39 | -20.48032 | -55.83844 | 2025-05-09 05:10:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b9c71fe-33c9-3c19-b1c1-3c5b06dc3dea | -21.77839 | -55.31657 | 2025-05-09 05:10:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d14adf95-ce3d-3257-8ae6-5b397449bfb2 | -8.07 | -43.1216 | 2025-05-09 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| a7049fb1-6188-35d1-a1d2-8ed197d757cb | -2.95613 | -60.01548 | 2025-05-09 05:25:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f48798c6-3688-3b45-a25a-9a60f7fd0665 | -10.48431 | -59.15197 | 2025-05-09 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6d305731-ca79-3a33-a556-38b3a81b080d | -11.90994 | -54.39925 | 2025-05-09 05:27:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4de9e663-7fef-3a07-871a-d7fe31c51d8e | -11.62949 | -54.94221 | 2025-05-09 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c468fd5-7ce2-30c5-9aa9-eae83c0f0a74 | -7.88951 | -61.46545 | 2025-05-09 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97239498-35d0-3998-bae8-0e183fb3aec4 | -11.90918 | -54.40137 | 2025-05-09 05:27:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 966e0325-1df8-3720-b897-d1917c19c1d6 | -11.38364 | -55.1149 | 2025-05-09 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aaa24ce-fb11-397d-977f-bf4f96ce5409 | -11.6296 | -54.93951 | 2025-05-09 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7457131f-306f-3a67-8014-2def25db95a9 | -12.17562 | -54.23418 | 2025-05-09 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d435c65d-865b-3f1e-b344-ccb3d13fcd4e | -11.38248 | -55.11294 | 2025-05-09 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4751ada9-3142-3e44-868e-fbec4a4f01e5 | -9.42493 | -62.11313 | 2025-05-09 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f67680d8-0fcc-346b-bbd6-0b31575ab91e | -11.38172 | -55.11864 | 2025-05-09 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef3a08ee-a161-3131-a628-06b9e4b76734 | -10.48804 | -59.15257 | 2025-05-09 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 310b3724-5619-3369-a718-023722184710 | -12.17478 | -54.24104 | 2025-05-09 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83f89798-df9b-32da-95a0-60bea1894dcf | -10.23246 | -59.23796 | 2025-05-09 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af5651cd-3fba-34ca-af25-de58a0d25bf0 | -12.17031 | -54.23348 | 2025-05-09 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 867e1006-0561-339c-8813-f6fc44c37e49 | -11.39281 | -52.94313 | 2025-05-09 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b1c6f1d4-3e65-3c72-a613-b21f44a20b66 | -11.39231 | -52.94716 | 2025-05-09 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1d1ecefb-b7cd-3120-8bb7-35a9505f48ee | -11.40328 | -52.95248 | 2025-05-09 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6a028bd-531f-3eb6-b292-d3ab53a03c8e | -7.90134 | -61.5215 | 2025-05-09 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4805faa8-3e5c-3cd5-a782-6abc16c69c8f | -11.38758 | -52.93838 | 2025-05-09 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fb3ae3d2-d601-3fb2-aadf-6b9282bfd663 | -11.38708 | -52.94242 | 2025-05-09 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 98a63dde-482e-3aee-adc3-bfe34376c2ed | -11.90955 | -54.40246 | 2025-05-09 05:27:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f144f42c-18b9-3b45-b019-61b6ca8da993 | -11.62486 | -54.9386 | 2025-05-09 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb83256d-3bfc-3efb-b982-ee2819ed44bb | -10.23182 | -59.2424 | 2025-05-09 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ee0f785-4072-3a2b-890c-d57c65ec3675 | -12.35709 | -52.48828 | 2025-05-09 05:27:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a691030-e189-34ac-997f-b7f0cc866c4f | -12.16989 | -54.23692 | 2025-05-09 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fbe375d-6702-3e3f-84f0-4c344b79cb05 | -9.61962 | -62.06419 | 2025-05-09 05:27:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 418d4cbf-6a3c-3635-a9da-b0a2dc784da8 | -11.36043 | -55.12741 | 2025-05-09 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e1dee5d-3333-3b3d-89b6-ea2a135e6149 | -11.91441 | -54.40212 | 2025-05-09 05:27:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65ec6dcf-7b7f-3800-8526-28c2de4d7736 | -9.16155 | -61.95266 | 2025-05-09 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d61fba62-1a40-3cbe-8c06-3228748ad5fc | -11.62459 | -54.93877 | 2025-05-09 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09eeec57-c8ac-3cef-9fca-7954fff04b73 | -11.91517 | -54.40002 | 2025-05-09 05:27:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b387900-d7aa-30fa-a980-4f061ff8d80e | -7.90632 | -61.51145 | 2025-05-09 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 40632856-b9c2-3b9d-b128-4acf8af5cc3e | -12.35112 | -52.48756 | 2025-05-09 05:27:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f8757d9-821f-3fdc-9609-ddc699e39626 | -9.42161 | -62.1126 | 2025-05-09 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a79aca1a-3f74-3bde-a248-d026e40cdbf6 | -11.40377 | -52.9485 | 2025-05-09 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 39d1b9d4-f5fa-3578-bf15-03ef91581ef9 | -11.91477 | -54.40322 | 2025-05-09 05:27:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README11.md)
