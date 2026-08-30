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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1635a271-ef9a-3c6c-a9f8-b7f819ce729b | -9.7123 | -60.733101 | 2026-08-30 00:55:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1bb6c7e-26bd-31c7-914b-367322a9ca26 | -11.3364 | -45.148399 | 2026-08-30 00:55:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8ff17a1-9e5f-38f2-9c3b-1796184a83b7 | -19.4793 | -57.565899 | 2026-08-30 00:55:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ac5b393c-d3b1-330d-9f35-e92de059618f | -3.4903 | -54.6488 | 2026-08-30 00:55:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3d47d79-0f81-3fea-a187-e5898384c672 | -5.9818 | -57.790798 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adb38281-bc26-33dd-8de3-cea8807e43e0 | -6.763 | -55.6549 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07454068-1f88-3021-9ac9-7747594e4f8d | -9.1963 | -51.545101 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76c651f1-54cc-3d58-b6b4-d4f8772f0bed | -10.4783 | -59.614101 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ca8953e-9fea-328d-b4ee-bfce4c80c1fd | -16.1423 | -43.050701 | 2026-08-30 00:55:00 | METOP-C | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ed293a1c-a54f-36b1-986e-b0d41130a07e | -10.7714 | -44.8736 | 2026-08-30 00:55:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 56ff5391-0f21-345d-b9df-fc324d2bbd58 | -11.3461 | -45.145901 | 2026-08-30 00:55:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4038244d-43c3-3829-a2dc-9122ab537f66 | -6.0753 | -57.890301 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e461179-7090-39a9-9fc5-1171a2cddab6 | -7.3393 | -55.1479 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc4746d7-dcd7-3574-91cb-a64868fa8a13 | -9.12 | -50.585499 | 2026-08-30 00:55:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6462bea0-cb05-305b-a2dd-4fa36f0bf8b9 | -6.6779 | -52.846001 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75bb600b-732d-3539-b3dd-487718f4ebdd | -6.9279 | -55.7038 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fbe64e5-eba4-32c3-aaf5-5e5fa7951881 | -3.6194 | -60.537701 | 2026-08-30 00:55:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdb3dd09-db70-365e-8f57-20a9230c2d12 | -10.7501 | -54.022099 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14b94a1e-bef1-3bb3-a50f-bf78e8e44804 | -10.8731 | -50.490101 | 2026-08-30 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 081aa867-869a-3bf1-96ce-449c4b9121fb | -3.2232 | -49.2337 | 2026-08-30 00:55:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0fad9a3-9171-38af-b105-417560c1df81 | -10.9615 | -43.026501 | 2026-08-30 00:55:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a92fa611-c09c-36c9-a798-6079e0d4c80b | -9.1673 | -59.511002 | 2026-08-30 00:55:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6577ae5e-b387-3cd3-9552-9bb584dd7078 | -7.5235 | -55.329899 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4ab81e1-b550-3da1-92fd-93aa677c5a4a | -16.3435 | -50.971001 | 2026-08-30 00:55:00 | METOP-C | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dff59dbb-a8d0-3fda-85a2-90d5c1d8b6d4 | -10.7486 | -54.062302 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 810715f2-5abf-3290-b514-d03e419eb734 | -9.8878 | -60.251099 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1250ceb-2b03-392c-896e-7e6fa26766e5 | -6.6287 | -53.173901 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d07b8c-f78a-32d6-8000-bd549d109bc5 | -10.3623 | -49.978199 | 2026-08-30 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f01d85ca-4947-3f8b-b0f2-4027190b8c71 | -11.1897 | -55.102798 | 2026-08-30 00:55:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1051b982-e7d4-3ab5-877a-f7ba95908c44 | -7.4176 | -49.747601 | 2026-08-30 00:55:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49e6eab5-82b5-3bfa-a04e-096357a5ba00 | -7.2372 | -60.632801 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95236111-7f85-368e-9f77-a74422a6d20a | -6.6795 | -58.738998 | 2026-08-30 00:55:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee04256-e66d-31dd-895c-0f1ccbbf6739 | -11.7138 | -54.5354 | 2026-08-30 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79af8af4-2b21-3b49-8b5d-bcbe9f73c3fa | -11.8286 | -51.057598 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aaa47809-8db5-340c-8cca-ba59e2e365a9 | -10.5692 | -59.6124 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30866795-495c-33b6-a6a8-7abe5b0839e6 | -5.48 | -57.142601 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67aa98fb-a599-3429-99a7-5440fbd8ccb6 | -15.4585 | -52.811199 | 2026-08-30 00:55:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c6eef510-91cf-34fb-b97b-92dc599d5f8b | -7.5252 | -55.337799 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 644c807f-e0b1-3a06-84c0-c99c91cb12c2 | -14.1557 | -52.8176 | 2026-08-30 00:55:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe85f941-5061-3716-ae5c-36b05802bad6 | -5.9789 | -57.684399 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2223f473-ac18-3bfb-b7e1-75d102d62983 | -10.7419 | -54.031799 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca2919c9-f411-3c5d-acda-c7f648278724 | -7.5474 | -61.287998 | 2026-08-30 00:55:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 962b8a79-8c1a-3d18-aea3-eaabbded1a6a | -2.9398 | -51.477402 | 2026-08-30 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c650fb1-6189-343d-8568-362a4484a79d | -10.746 | -50.834599 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c943821-135e-33bd-a823-a861ceaa10c8 | -10.7428 | -50.685902 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 148c0899-07b1-34b2-8968-99d432d7bf9b | -10.7321 | -54.034 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52fab130-c567-320d-97ab-ff8f50ba5de1 | -6.8733 | -56.573898 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09952a23-0089-370a-ad1d-2be2f5936221 | -7.513 | -55.282398 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d2b9c2e-dd13-3e44-a63a-fe2e0a0e1a3c | -9.1576 | -59.513 | 2026-08-30 00:55:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2368b99f-de89-375f-b4a5-d64375beb3a2 | -7.2433 | -60.614101 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba85840e-4060-30da-a5a8-d386b107ed7a | -10.9518 | -43.028999 | 2026-08-30 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c3223d41-9f79-3560-be51-4ee6b1fee2ad | -6.3399 | -44.087502 | 2026-08-30 00:55:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca2e1426-fa23-3b22-a299-c498ece9dced | -9.2046 | -51.535801 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5831b4cb-5def-3074-a3cb-72eef5f64aa8 | -15.3671 | -52.6721 | 2026-08-30 00:55:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 37e1c81c-585e-3cd9-8262-d3b771d2a671 | -20.013201 | -47.894699 | 2026-08-30 00:55:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4ca8b8f2-ed87-3f4b-bf4f-aeb549d45b88 | -9.1447 | -59.500099 | 2026-08-30 00:55:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0732d3be-f9bf-3671-9c78-63e17d2bf5a1 | -13.8389 | -54.115501 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cc37276a-45d9-370e-8339-e725bc0db924 | -23.160601 | -48.671001 | 2026-08-30 00:55:00 | METOP-C | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 30160112-7295-37ce-ad32-c3f954385629 | -12.0873 | -47.1884 | 2026-08-30 00:55:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d04c5fb-c5ee-3a8b-9169-1dca8d6eb8f1 | -18.826099 | -47.459999 | 2026-08-30 00:55:00 | METOP-C | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8a9215be-02d5-3bdc-9f0f-a5ed6931ad0c | -7.3427 | -55.163399 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7bcde45-c403-316a-9fc1-371ef4712eb9 | -6.1669 | -57.7943 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2485ceda-2ea5-32d9-ae7f-0fcdcb55d427 | -4.1558 | -60.700699 | 2026-08-30 00:55:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32c558e6-17fd-3239-99ce-883efc131521 | -10.7355 | -54.049198 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd27195-55d9-390d-b6f1-6be5685eab32 | -6.7452 | -55.667301 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee4ab6be-3630-34ad-9dc1-e3068ee7d4e3 | -9.1979 | -51.551998 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ec19167-e767-3f27-b091-a12355214652 | -7.5572 | -61.286098 | 2026-08-30 00:55:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6077bdf0-b89d-3da8-80d7-8e1305d77aae | -5.8824 | -57.7584 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3ba6efb-0875-3068-abff-16eb0764326f | -10.4751 | -59.598202 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 418a9367-4332-3003-9ae0-e353e77a4a23 | -10.7657 | -50.6507 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e6c9d68-1149-382e-9311-94d76f028cbe | -4.0814 | -45.946301 | 2026-08-30 00:55:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6bab3d86-236e-3491-8dca-336835de8084 | -10.566 | -59.5965 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41accb44-8932-372d-8f59-554c7943f1b6 | -14.154 | -52.8102 | 2026-08-30 00:55:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba6aa25f-5f92-328d-96ae-8b685631f800 | -13.8372 | -54.107201 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 61447f12-3922-3378-be39-c3631fff2b07 | -10.3508 | -49.973099 | 2026-08-30 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52b946e9-65fa-3677-bfb9-6d5d62fc0e12 | -11.2882 | -54.040001 | 2026-08-30 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9698e7e3-0879-3ccf-97e4-db6f29135792 | -7.0906 | -51.584202 | 2026-08-30 00:55:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 492d1edf-2710-359c-a151-ba25781f870b | -3.9336 | -59.3256 | 2026-08-30 00:55:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a31c5289-ff43-3372-9cf9-f80ef40af3e6 | -9.6137 | -55.120201 | 2026-08-30 00:55:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb9d66ee-a4cb-362e-b6cd-0f1e0cbb1359 | -13.8522 | -54.129902 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0844e27f-7807-3163-9945-1583edcd5610 | -9.1795 | -59.618698 | 2026-08-30 00:55:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f38834da-0a1e-3f6f-b099-0be1c897ecd4 | -15.1192 | -53.5784 | 2026-08-30 00:55:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56f3ebe8-cf06-3d0a-8c09-2eb434589a57 | -7.0631 | -59.717701 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a092275a-b20f-39c0-ab9d-c2f91c339891 | -11.5013 | -46.947201 | 2026-08-30 00:55:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76319866-ec62-3799-8118-6d780c3c55ba | -5.9571 | -57.678501 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87c9346e-6ce9-3685-8ecf-8146fba0faab | -8.9445 | -62.380199 | 2026-08-30 00:55:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 94ab761f-c51c-336c-b304-f396eb37314a | -5.4841 | -57.161098 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f6adf0a-e143-3945-a881-cd24f62b4c46 | -5.9868 | -55.723499 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bbfe249-4e90-3ed8-906d-9528a037705b | 2.174 | -50.690601 | 2026-08-30 00:55:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7d743fa6-84a7-3a38-a04d-0d787acf3383 | -10.7673 | -50.657799 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5213ee86-8107-3c70-b4fc-4f89d437cc1f | -7.341 | -55.155701 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f5d38dc-a30a-3927-af04-1ebfe0a18ad6 | -6.2595 | -55.424702 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 976cb0f7-123d-3a8d-8a6e-819f0ff77823 | -14.4012 | -52.575802 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f6f02b1c-7523-369d-9c92-782812c5d180 | -10.3542 | -49.987999 | 2026-08-30 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 869d1c04-ddff-3a0d-9e9b-cb45dfa0685a | -10.816 | -50.510899 | 2026-08-30 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bdd8964c-0b79-3e7c-822a-5cb3e39cf462 | -8.4999 | -55.285301 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcf38cdd-2b1f-3790-9240-a796228d626e | -6.8649 | -41.6548 | 2026-08-30 00:55:00 | METOP-C | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ee6ea29b-b580-3d62-b278-3de2d638f23e | -8.5882 | -54.752899 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56091eac-e4d6-3668-a61a-d133a308f6dc | -8.6156 | -54.690601 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42288e44-c776-32ab-acfe-d9fe75f211f6 | -6.3786 | -55.2206 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
