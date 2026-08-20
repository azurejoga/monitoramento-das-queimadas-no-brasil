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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94bd4055-579f-3230-a470-a53e012f1527 | -9.38824 | -60.59572 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22640846-8ea5-3329-89f6-234e23b48153 | -11.18869 | -54.01009 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a16e7a3b-2dfd-3427-aec5-1211687b1cae | -11.2422 | -54.82787 | 2026-08-20 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff8c2ccb-e2c7-3919-abc0-03dae22258c9 | -12.48801 | -54.72503 | 2026-08-20 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8763461-4e19-3fa8-aa44-7f05a39da941 | -13.5487 | -52.22899 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0d4923de-93b0-3e05-8ca9-f93f07b62814 | -9.45217 | -51.63197 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f795b95-6961-3a0a-9af5-1c980911528f | -13.54512 | -52.22471 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7a0a71bd-3ead-3868-b3dc-18f1daa6fc30 | -9.21525 | -59.77617 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4736f31a-2e67-3d7e-b274-91bb6e44b93a | -11.82661 | -58.83559 | 2026-08-20 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 196e86cd-3f76-394a-ad15-a8fb2ee80e53 | -9.11903 | -61.59852 | 2026-08-20 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be8e2a05-c14e-3d60-a97c-690b74b8207b | -7.86327 | -63.76117 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2871b591-965a-3f3d-90e2-3f8c126dcb65 | -7.36386 | -55.51613 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d97ce8c-eaa9-33dd-b241-ebdae92fcf3c | -13.44942 | -51.81369 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0f712ce-cf49-396b-ad87-d0c1be720313 | -8.53172 | -54.86087 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47b1a757-bccd-3277-abec-cb60189c8f81 | -8.56749 | -54.67186 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 350ccbf2-7f4d-3078-8e32-d6d877279e28 | -12.16145 | -57.21967 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dee3b1a-1500-3736-bef3-5f4e397ee1ee | -10.92794 | -57.17155 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2cc1a53-fa83-3b63-aab4-c147552cc54c | -11.22299 | -55.05009 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1313e0a-15cb-3318-8f14-a001ef6ed074 | -7.8297 | -61.60252 | 2026-08-20 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a32860a8-f981-33a1-bfbc-5f0f650299fd | -11.18691 | -54.0225 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a6e80aa-82c2-3e5d-836c-44dab926e92a | -8.66859 | -54.65358 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 4083ff04-db4c-3b94-b655-f034ddfb9e6f | -9.39347 | -60.56664 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ea752b9-17b0-370f-ac90-9583e8ed2bdf | -12.80531 | -48.43404 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 476ddb15-0b7b-3148-998c-605de8b58777 | -7.10342 | -59.77077 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42bbf5f7-ef76-32cf-8209-9298c6c1aaf2 | -6.91661 | -59.35068 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e02618a1-cd25-34da-9ec3-7ebcc411b42e | -8.58413 | -54.77586 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89b41276-b82b-31c6-86c2-7272b4052c65 | -11.22302 | -55.07318 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cee28bf-0b31-39d2-b88f-9b3de5a54ff3 | -8.67652 | -54.64725 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 665b5d6e-65bd-369e-9533-6e2636acd14a | -11.68757 | -54.55891 | 2026-08-20 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6eb6ed59-ad3a-38c2-891b-40d2a1bc6a3c | -11.42727 | -54.33498 | 2026-08-20 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2916c793-5009-378a-8c06-273ff24ee98c | -10.8145 | -50.28925 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4426379-1225-3d74-b632-491ff8871c3c | -10.39551 | -61.21212 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88fd4471-a00a-3bfe-ab4d-918909dc4020 | -12.12614 | -57.20678 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d086688-b558-3c5a-8f0b-129d1a0a65e5 | -8.52779 | -54.86398 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00ba5977-2972-34e6-977e-254e07621f9a | -9.39808 | -60.55936 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bcedc6ae-1546-369f-b414-27a27d4a2dea | -11.99843 | -53.44049 | 2026-08-20 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 17303320-84a0-3acd-b111-4129fa13ac22 | -8.58358 | -54.77951 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 598e29c0-901f-374a-b004-d222d82c2c87 | -7.54047 | -55.5832 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0f75a3f-4485-38e2-83e5-46cf66b63809 | -7.3451 | -55.68061 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e007837-9557-3510-912d-a604e8b43062 | -8.64648 | -62.82296 | 2026-08-20 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e28f418-ef0e-383c-ba3e-ceaf7a0f32f0 | -12.00279 | -53.43657 | 2026-08-20 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91e34920-5775-370a-9c9e-7be367873ef1 | -9.80195 | -46.6368 | 2026-08-20 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ded8154-72cb-3c58-a5ef-94666a04275b | -8.68388 | -54.64462 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4663151f-f9be-3157-9cc0-4c0b8e5bd07f | -7.77083 | -61.14128 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53d98491-cce4-35d0-8c4f-73f5a5542e2c | -12.80005 | -48.43372 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 43bed869-084f-335f-aa2b-d80954078b49 | -6.84424 | -58.99295 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b7883ad-686b-35f6-a5a5-60961f58b6cc | -12.2541 | -43.16751 | 2026-08-20 05:06:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f71a9f89-e7c8-3065-b977-fa2d6b83c141 | -10.78473 | -50.30775 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 58329560-10e4-31a2-a28c-12f58da6fcb5 | -8.55786 | -54.66661 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3381f508-403c-312a-89e6-2c18947f5ed1 | -10.32512 | -57.56367 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3391bb9c-d76d-37c2-bc9b-ed2543bd8e9b | -12.81054 | -48.43452 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc8b04e5-8b00-37bb-ba5f-5ad4a70d9ef4 | -9.98908 | -53.93514 | 2026-08-20 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f183f7e1-aa13-34ce-afec-79a4e632aefe | -12.93951 | -56.6279 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 027aefd3-7245-3ca5-87f4-b358212bd30f | -9.39732 | -60.56398 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0644afd-4ecf-3bf7-a816-e5cc00b6206b | -8.55954 | -54.65555 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40f57747-f57d-3481-a76d-9381ddf0c5d8 | -11.21548 | -54.00145 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 464486f4-8efe-3e87-b7ca-dfb3c086ac1f | -11.83619 | -58.841 | 2026-08-20 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8a85ed2-41f3-377f-97e2-f8b4afeccc5e | -10.44718 | -51.80521 | 2026-08-20 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d374e29-78ec-356c-8f26-d8e21f1335ad | -6.92026 | -59.35125 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8ba60392-8e17-384b-a55b-90d93138a4f5 | -13.60688 | -51.79318 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 260534cc-2979-300d-ab8e-b35870d199df | -11.70151 | -47.81606 | 2026-08-20 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dc1f461-5899-34de-89e8-b53399905b25 | -10.52229 | -50.7848 | 2026-08-20 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6abddc0e-075d-3de0-9a74-9c2bfd638f8b | -8.59331 | -54.66835 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f3be722-099c-37db-bc0f-7bbd4cf9d05e | -6.85163 | -59.01512 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd6ab4f3-47a2-3937-a8d1-8162717b37d7 | -11.31573 | -45.20979 | 2026-08-20 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4dad75ae-d9e9-30e8-8bdb-9a01126d4b1a | -9.45617 | -51.6325 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 047154f0-eaad-3894-8786-57a67389a5a3 | -7.40224 | -55.53253 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd246a23-21cf-3d85-a30c-ed76234c96ac | -11.21216 | -55.05231 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a87ec468-40e1-3c06-b7a7-228ed47bc0f5 | -8.40899 | -62.70521 | 2026-08-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e5437e2-9802-3941-ae7f-44a077fdeceb | -12.0065 | -53.43712 | 2026-08-20 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2792b2e-4d38-3eca-8619-34478d3d5059 | -8.58514 | -54.74611 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1cc62392-f3db-3c67-ae1c-87d75be37535 | -6.75877 | -59.46665 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0649735-b2e7-344f-b042-c521afcc270b | -8.55183 | -54.77451 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5c91272-e7b3-3423-b307-408f8bff5e95 | -8.54228 | -54.79169 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ded2cae-7989-3ee3-bfb7-3f97e4b36386 | -8.51318 | -54.86915 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9fdcd65-aa9f-385b-9fdb-91b70d4434e1 | -8.58065 | -54.75289 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d61ee832-6eb3-3b49-9c68-41ef14a106b6 | -8.58743 | -54.75392 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4225949-5846-3653-982a-689666c0709c | -9.21595 | -59.77194 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7043620a-726e-353c-92ff-8ee064a26822 | -6.84357 | -58.99704 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a7d9d9e-d985-31cb-9570-7a2d6c6d939c | -12.2577 | -43.16411 | 2026-08-20 05:06:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 24a933b8-378f-33df-8135-0ca764d6babd | -8.55898 | -54.65924 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1e19530-bf1e-3345-95be-f1ccc254592a | -7.87279 | -63.76278 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bcfc4cca-0273-3b57-814a-c23eda5b608b | -9.38679 | -60.55741 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b56e3613-5e62-3e98-9e65-04b7547fbd09 | -8.10447 | -51.66789 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d994e2b9-90e4-3858-aa08-f7b2d2067b01 | -8.54001 | -54.78387 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a870b5d-f7a3-3362-a9d8-0d50db9c595e | -8.51263 | -54.87278 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62481d79-ae80-3d01-9305-b96a93a91087 | -8.53399 | -54.86868 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cd89e6d-d523-39ee-a092-aae724247fdd | -12.93619 | -56.62737 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f609d3de-ad17-320b-b607-d698be730e23 | -11.20817 | -55.05556 | 2026-08-20 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 132a87b9-4c8d-33a3-80a7-0e178106fa16 | -11.21272 | -55.04854 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ed86a210-ecd1-3399-adfb-6dff3952853b | -7.56693 | -55.56589 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01df1093-31f6-3c5b-8f50-47306a0e9b95 | -7.53107 | -55.57816 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0848585-4be6-37ff-81bb-5fd1aa68ce2d | -7.866 | -63.74939 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb244917-8ba6-32b5-948c-ea1f0fe80227 | -8.28473 | -62.89971 | 2026-08-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ca6f071-ac45-311a-9688-7db24ea4d040 | -8.53287 | -54.87596 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eff4a913-aa6a-39b8-ab3c-db4f9d179952 | -6.8438 | -59.01808 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f67ef266-acf4-337f-978e-b034b0489487 | -12.79972 | -48.43652 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 894307ac-70af-3044-b3d5-e635503c3cf5 | -8.57599 | -54.68446 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72391865-fbb5-3d0e-800c-f7340d14e48c | -7.53214 | -55.5712 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd062670-60c9-3a43-b7e9-d16ea7d9d744 | -6.80553 | -59.01332 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README52.md)
