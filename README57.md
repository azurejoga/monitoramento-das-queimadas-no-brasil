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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6b0956f-364d-3671-abe6-ca67c435f195 | -9.47646 | -60.46579 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e389471-3287-3734-88a2-93bda9abd35c | -8.74896 | -62.57911 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 54f17dce-1e2d-3f39-bf6d-f5730abd1892 | -13.97765 | -58.68404 | 2026-09-02 05:18:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dff4fefd-7764-3a8b-b8b2-a824d990da5e | -11.6616 | -50.18816 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb445099-fcff-33e0-a506-dda170f6931c | -11.35414 | -50.62375 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c35b8108-d160-3524-8445-fae783ffc122 | -9.00233 | -65.41847 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9178ae64-dc79-30a2-be72-aa634e1d4df0 | -10.30981 | -50.03647 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc67aa3a-cf28-3c8d-a988-7269b1a79fdb | -7.76786 | -61.19606 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1949898-5946-35e6-b48e-fc67a94c6a23 | -12.12822 | -47.08804 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99cca1c4-a0af-308d-9535-0c96081de75f | -7.68737 | -67.12621 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cad2bff-28c2-38cd-ba5b-8176fa7d1d4d | -12.14675 | -47.06974 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 412d174e-2282-3eca-9aa2-9235b14fa0af | -10.41542 | -50.00571 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a35073b-8781-3c7c-945b-0ba3395f18a2 | -9.95183 | -53.9953 | 2026-09-02 05:18:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 605b484e-310c-33a5-8bd7-6045e120df08 | -14.96358 | -48.11843 | 2026-09-02 05:18:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a43d067-5292-3610-afac-f73b9f03fba0 | -10.77987 | -44.76383 | 2026-09-02 05:18:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 9f826e9a-3625-3d8a-92d8-a611bdc25d62 | -11.03008 | -49.66856 | 2026-09-02 05:18:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bad1af8-b79b-371e-a577-261851928cb2 | -11.30009 | -54.05748 | 2026-09-02 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85e497dd-6991-3b66-a6c8-894dfcb49771 | -10.3838 | -49.98543 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fdc6c855-bb08-390b-b2a1-cdac4a3fca06 | -7.69635 | -67.12428 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d05aba0-1945-33a0-8c94-df45cb736341 | -10.77512 | -44.74243 | 2026-09-02 05:18:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 69306479-d203-350c-9d0b-8f9236b3341a | -10.50373 | -59.62254 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27d7c2af-4307-300a-aba5-940384a506de | -10.96418 | -50.49266 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17d3a557-f190-3337-bea4-b67a133c8fc0 | -12.14107 | -47.12003 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e284fa89-33a3-356c-80a8-b9cc9fcc9fc0 | -11.662 | -50.18512 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b587a27d-2bf1-3612-8526-0ace85ab3f5c | -11.30317 | -45.19674 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14a2ed36-bdc4-37db-bca4-9180cd99404a | -9.72173 | -47.77063 | 2026-09-02 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 516401c6-6ff7-3c3f-9171-ae4a9d2af7e7 | -8.75591 | -62.58512 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dc2333e8-3951-33c5-a9f3-dd24b3aee94d | -8.99658 | -67.80453 | 2026-09-02 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30208b29-c706-3b88-980e-4c637f45b962 | -11.29409 | -45.16105 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7744edb-9223-3ac8-90f4-db2939d2cae9 | -9.94024 | -53.99354 | 2026-09-02 05:18:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6397772b-6977-3056-a2c4-3609ef2374fd | -7.72565 | -60.97446 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6b477f4-9978-3a68-9edf-b69c154c2dc3 | -10.78086 | -50.48103 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c44b754-3630-3cad-bd6e-3a25eac17b31 | -11.05512 | -51.52758 | 2026-09-02 05:18:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47d6c50b-af09-351c-845d-30357748d06e | -8.77404 | -62.8352 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c6e6b55-051a-368b-b12a-f32a1f57a2b9 | -10.90208 | -45.34166 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8ebe0ae2-0f37-3b99-b2b0-346e236958ef | -10.98048 | -60.78801 | 2026-09-02 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98d5a5f7-59bb-350f-b0c5-611bb3925612 | -10.49934 | -59.60709 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40d85709-5fca-3e11-ac6c-5732f530af90 | -9.41442 | -56.98857 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40ba5d62-47ec-33a0-924f-fda68a29a236 | -11.12121 | -51.52698 | 2026-09-02 05:18:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af328a90-4e2e-31c3-b4a9-41f5e900a1d0 | -9.45947 | -56.7397 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 221e2faa-d64d-3695-a425-627e9f618301 | -11.47689 | -45.08696 | 2026-09-02 05:18:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9b3d42ba-d4a4-3693-8492-cd8f781d8661 | -12.13074 | -47.09855 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f208dcd1-7c93-36da-a67d-18dead7a14bc | -9.87611 | -64.98753 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5da63f9-31a2-3d2b-b011-835254c19870 | -11.34277 | -50.63369 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e4d7b76-78b2-3fd2-9144-72a9b135c09c | -8.92898 | -62.36895 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14fd925b-66ac-30aa-8d7c-03fe27625330 | -8.9107 | -62.36092 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90e86ffe-a3be-3071-b5cd-990dcdcee462 | -9.46285 | -56.74023 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e855d6e8-da56-311d-a566-0757f63a64df | -9.87403 | -64.97334 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13e5df05-7abd-3163-afa3-197b36c5d913 | -8.56841 | -63.1923 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b8217a4-31fd-3d73-853e-048d2b700d10 | -7.69102 | -67.12329 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1513b9cf-7901-3172-9ec3-a332920ba115 | -14.96406 | -48.1141 | 2026-09-02 05:18:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d243e78e-4ac3-3b4d-bda0-2cc6b6e02cae | -9.47325 | -57.03087 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f92808f0-d550-3f3b-a57c-dbbb76d6360f | -10.88764 | -45.34584 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6a6d5787-0174-3faf-a2b3-287c2bea4637 | -9.4699 | -57.03034 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cb0a4da-7acc-3e6f-8c86-c4a0ed030cf3 | -7.49943 | -63.75997 | 2026-09-02 05:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72240726-b73f-33dd-bbd2-78c8c1bb0449 | -12.12501 | -47.09278 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 959d60d6-d4c9-3a45-adbd-288a073d2dcb | -9.46598 | -57.03341 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a43377a7-8db5-362c-a3ca-eef8fa70e095 | -15.6791 | -45.89025 | 2026-09-02 05:18:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b6983f4-2c7b-3cdf-9f86-0bead8cf03f0 | -9.02584 | -65.44818 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6abbeb19-479e-3ec0-aa42-d7837ab8508b | -9.68883 | -47.17347 | 2026-09-02 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c3c004d-d518-32d9-8367-69a1d7af9a66 | -12.12554 | -47.05673 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34f7afb9-1602-3780-99ce-14604e978f70 | -10.75879 | -54.06532 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26e60fbf-e696-38ab-a378-588556a67c4f | -8.91547 | -63.28937 | 2026-09-02 05:18:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 82218df8-9547-376b-aea3-d5eb1a59d99b | -10.7595 | -54.06039 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75a49552-495d-367a-8f5a-16fb279dcbf1 | -10.88651 | -45.35019 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5964833-8150-3557-bc5a-6afa3d6c881a | -8.74592 | -62.57355 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 96608adb-e37a-3ab6-bc53-63edb506abeb | -11.34994 | -50.61743 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b4b7f0e-8422-3089-9b28-7d734aaf6d2b | -10.9097 | -45.33615 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 5fa8e0be-4bd4-369b-bde1-758e76cf584f | -15.35573 | -47.04267 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49b522ac-371a-30b4-a149-6a2ab0e416cd | -10.99542 | -45.08376 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 96fd4413-fa5d-35dc-9f97-a853a4457927 | -12.13214 | -47.10874 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2aaff938-363b-3afe-b42c-3a6426c32975 | -11.30025 | -45.16904 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d1b09ae-a8f1-3979-8dee-db80eb33ac30 | -14.97525 | -48.12479 | 2026-09-02 05:18:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84a66f06-4386-3c0c-9ac8-9a7fd8142bf0 | -9.03372 | -65.40395 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c5b1732c-d14d-332d-9377-1cab8e0eef3c | -12.08867 | -47.09877 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba5faf43-a817-38d8-8ce4-23d31ea25bdf | -7.69164 | -67.11996 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c246d0a6-468b-3487-b94d-569785846524 | -11.76093 | -50.55479 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5059d5b-eb58-3d89-a752-cff66511d065 | -10.32621 | -49.95004 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 674d5043-810e-33d9-b922-cc7475a6d19b | -9.45553 | -56.74283 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d76a739-ebc4-3fd4-93ed-ebdd30700a03 | -7.50369 | -63.76074 | 2026-09-02 05:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c817f6a-5beb-30c5-9c05-59dde9a13b3b | -9.72763 | -47.77102 | 2026-09-02 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a1ad17e-7d95-3301-9ba8-6615bbf65194 | -8.26319 | -62.75895 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dc3ddb1-ea0a-33e8-8952-25b9c9ce9724 | -10.6775 | -52.50559 | 2026-09-02 05:18:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 246d3ad2-2d14-309e-b821-908622cd847b | -9.82962 | -59.47989 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9c78d4f-a6a2-3d23-aa45-8fcf5ab75229 | -7.68796 | -67.12288 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcdbeaac-0f26-3d55-95c9-328869d19fe5 | -9.00433 | -65.43407 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7041cb03-4fda-3d22-a60e-a49fca6c6bcb | -11.32962 | -50.5801 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3f50bc1a-2f59-32b1-a084-99746b0f5396 | -8.4051 | -62.70748 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 847d9067-314e-3e00-82f7-58580b7859de | -9.01941 | -65.45724 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b350b26-15cb-3601-9537-869edb0d0c83 | -11.31646 | -45.15161 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bad26db3-0a71-393a-aa2c-573d22133fda | -12.13332 | -47.0988 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d99e1f38-325a-39b0-a6a9-59f439f15806 | -12.07325 | -47.12189 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ab90bd5-b454-352e-ad8a-be6a9f6dc748 | -11.47611 | -45.09385 | 2026-09-02 05:18:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e56fd1b1-5429-3890-9ee4-40d35def7d3d | -11.66773 | -50.20213 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3efb983f-6cf7-37a1-9050-e4fcdc2f3860 | -10.04442 | -48.68864 | 2026-09-02 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db9effab-02f6-396b-ad90-f405cfd51e70 | -10.73897 | -54.03697 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 211f90aa-a748-33b5-84e1-f52906318f06 | -10.29998 | -49.99257 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8f4c9b9-fb05-3bac-b429-7f2ee97b2a5b | -10.96349 | -50.49144 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aff3a9b-9ada-3794-9893-c3bf30e91320 | -7.47454 | -63.75145 | 2026-09-02 05:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6d11a5c-69e1-31c0-a36e-5235e2f3889b | -9.68759 | -47.17574 | 2026-09-02 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README58.md)
