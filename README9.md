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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef56c9cb-184a-3eb3-8e52-81a011ab5657 | -3.2012 | -61.2346 | 2026-09-06 01:50:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad8d0e8c-03a2-3601-9cee-4e74aa5b8735 | -5.3869 | -56.027901 | 2026-09-06 01:50:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e80e042-e1a0-3e11-b2d3-0c9d0fd4031a | -5.361 | -56.005901 | 2026-09-06 01:50:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75c667e9-cc15-3b93-adfb-d054cbcffb9a | -3.1433 | -60.644798 | 2026-09-06 01:50:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d707ca0-88ce-36ac-a1a3-43bbd32bf6e1 | -5.3677 | -56.0327 | 2026-09-06 01:50:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14c2a9e6-a6b1-3241-982b-e3430af418cd | -9.1438 | -67.824997 | 2026-09-06 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6c55b86-c35c-3542-a6ae-525ce7ce36cd | -6.6664 | -59.938 | 2026-09-06 01:50:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 193541a4-c473-3be6-bba9-c1ef4f8b1cfb | -6.6567 | -59.9403 | 2026-09-06 01:50:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36006f7b-d9aa-308b-b8cc-97a31fee0bf0 | -13.7724 | -53.820599 | 2026-09-06 01:50:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1932494a-3f2d-37a8-990a-adf294ad0d56 | -20.459801 | -57.405998 | 2026-09-06 01:50:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4374368d-c5fa-3553-b2bf-79515bc5ddd2 | -3.1531 | -60.642601 | 2026-09-06 01:50:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 40eab8d8-1d32-3047-9e51-8e090ec85ff1 | -5.3744 | -56.059399 | 2026-09-06 01:50:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c93a0e62-53f4-3004-a45b-401c07876631 | -5.1511 | -55.943199 | 2026-09-06 01:50:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 930a2d83-d9c4-368c-861d-7de650e28346 | -9.1455 | -67.832298 | 2026-09-06 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33b8fb30-81c7-3ae4-a6e6-7019c64f5bc4 | -5.3773 | -56.0303 | 2026-09-06 01:50:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deef7bd1-b38a-39c0-bfb6-3d5ae90ece04 | -6.0668 | -57.799801 | 2026-09-06 01:50:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3430b337-5e5c-3980-b3c7-80747b520861 | -5.384 | -56.056999 | 2026-09-06 01:50:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da909175-655d-33d4-a61c-5260dd7bffa7 | -9.1372 | -67.841698 | 2026-09-06 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e2983fb-0b47-352a-bf82-45910c1695d3 | -5.1482 | -55.9729 | 2026-09-06 01:50:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c36b8b43-79fc-32b3-ae5b-f5759b185964 | -5.3706 | -56.003502 | 2026-09-06 01:50:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 387ccb68-e78c-3121-8a0e-4d89d2f93e12 | -20.456699 | -57.3937 | 2026-09-06 01:50:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ef2dd313-cf62-3681-87e2-6b22fd5dc54e | -9.1422 | -67.817802 | 2026-09-06 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0b17c8e-a8bb-3dd2-8911-0143ade684ec | -9.1258 | -67.836601 | 2026-09-06 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45816618-8dd6-386b-affe-37039854fc0c | -20.4438 | -57.384201 | 2026-09-06 01:50:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1c4985d1-1556-355b-9b12-66cbca7b509a | -9.1274 | -67.843903 | 2026-09-06 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad11ffb0-692e-35ec-9bfc-2ee5d71a4491 | -6.8993 | -62.962299 | 2026-09-06 01:50:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8ef702b-2d25-3232-808f-933420d295d8 | -6.6698 | -59.951698 | 2026-09-06 01:50:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b74986be-6dea-306f-9654-b3b8194d5d29 | -13.7799 | -53.847599 | 2026-09-06 01:50:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ee52c6cc-98c6-33f7-bd4e-a7b4010ad520 | -9.1242 | -67.829399 | 2026-09-06 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c2f8904-a776-35c2-a356-1c30f98a5054 | -9.547 | -60.8316 | 2026-09-06 01:50:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c2b835e-c0b3-3661-bbb4-bb71e0add894 | -10.7017 | -45.9016 | 2026-09-06 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f717b01c-2168-32f7-8107-27276d941322 | -6.6513 | -59.9642 | 2026-09-06 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d31fd1e8-cf3b-3dec-8c1c-04b163219f9d | -11.2955 | -45.7087 | 2026-09-06 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 765bc4e5-cb25-3d2f-b74b-91915db7a8ca | -6.6698 | -59.9443 | 2026-09-06 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| b41ea584-61f1-3a9a-9929-be9f43249de5 | -6.8813 | -55.619 | 2026-09-06 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 41478122-e2b6-3658-b52d-ce9aff86257a | -6.8944 | -62.956 | 2026-09-06 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 0441efc8-d9e0-3c44-82e2-fb160869d964 | -14.905 | -44.6782 | 2026-09-06 02:00:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 14627c0a-a416-3af4-b298-3f6fd6b58203 | -6.8944 | -62.9748 | 2026-09-06 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 5829fcef-44c2-34cc-aaf0-115c3bb5b781 | -5.1423 | -56.2703 | 2026-09-06 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 824a0ec9-ab35-366f-aac1-de50882a5cd2 | -10.7492 | -60.7097 | 2026-09-06 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| d7b216c5-0bd9-37c8-ac9b-d611b4c43210 | -5.383 | -56.0242 | 2026-09-06 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5f108660-d4ad-325d-a6ee-6574e798063a | -11.3255 | -45.0624 | 2026-09-06 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| ef153c33-8716-36f2-bb12-ffd28ac7e100 | -6.6514 | -59.945 | 2026-09-06 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 5cadc0c4-393c-3b12-86d8-21af4ececd6c | -5.3462 | -56.0256 | 2026-09-06 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d28cda42-dce7-316d-885f-1717f93fa48e | -11.2764 | -45.7113 | 2026-09-06 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 68446f30-46ea-3c7e-b0cd-3f3f6c446a2e | -5.1439 | -55.9543 | 2026-09-06 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 159db383-8714-3074-a00f-ac4adf710c25 | -5.3646 | -56.0249 | 2026-09-06 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 8fb776d5-8554-3fa8-8694-1a45a8748dd9 | -14.9246 | -44.6744 | 2026-09-06 02:00:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 90ba0cb7-50cc-39cc-b506-a1c837eb0ec3 | -5.1438 | -55.9741 | 2026-09-06 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 20f31f0e-d16d-3019-91da-313b3a03ab77 | -5.3645 | -56.0447 | 2026-09-06 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 63c5d02f-5fb4-3082-8344-e3e1a49b89d0 | -11.3447 | -45.0597 | 2026-09-06 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 16078b0a-a16f-3a16-af79-72d5bf976922 | -9.1442 | -67.8317 | 2026-09-06 02:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 891f0782-8f6f-3136-99d0-dad70ae7c3ff | -5.3462 | -56.0256 | 2026-09-06 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 57302251-a662-3c11-8d38-c0e562c5d5b9 | -6.8944 | -62.956 | 2026-09-06 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| dae48110-a85a-323b-aa4e-863413fdfbe6 | -6.8813 | -55.619 | 2026-09-06 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 35fb3882-1295-383c-9721-bc70b085bc60 | -14.9246 | -44.6744 | 2026-09-06 02:10:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 99.0 |
| bd82f479-effd-3257-8035-d564f70f6e69 | -14.905 | -44.6782 | 2026-09-06 02:10:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 9f408f91-c00a-3e67-8e58-b084666dad36 | -11.3255 | -45.0624 | 2026-09-06 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 7cda58bb-a17a-357d-8091-1eadd74cb7e2 | -9.1443 | -67.8132 | 2026-09-06 02:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 70d4db5c-5a71-3aa2-b0a9-abd27293b8a2 | -5.3645 | -56.0447 | 2026-09-06 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 52a53b50-ac35-3984-81c1-d36bc2a1e6f4 | -5.383 | -56.0242 | 2026-09-06 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| b2e91a76-b28d-3ac8-8168-c2f328a13d87 | -5.3646 | -56.0249 | 2026-09-06 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 166.3 |
| ba526f4e-6ac8-325c-ab17-e06d15a9129f | -5.3829 | -56.044 | 2026-09-06 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 671a826d-cb5a-31b6-ae3e-69fc27b9dc36 | -11.3447 | -45.0597 | 2026-09-06 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 9bb34f7e-529b-3f36-b8ae-68acab23061f | -11.3251 | -45.0855 | 2026-09-06 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 0d283f3a-964f-3086-adb7-901c92f76343 | -6.6698 | -59.9443 | 2026-09-06 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 69624352-b4b7-387d-9644-8d181671926f | -6.6513 | -59.9642 | 2026-09-06 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 9aa331e6-1bbc-3ba1-a161-4991aef936de | -6.6514 | -59.945 | 2026-09-06 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 30764a07-b4b6-3d54-9abc-0bea4353a811 | -11.3443 | -45.0828 | 2026-09-06 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 71e22783-6774-335d-abf5-86eba2dcd6ce | -10.7492 | -60.7097 | 2026-09-06 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 30a442f8-4f3a-312f-ab6b-531d3973acab | -13.4291 | -41.8882 | 2026-09-06 02:10:00 | GOES-19 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 190a0799-1710-34fc-840e-60bea6ac97d6 | -9.1257 | -67.8322 | 2026-09-06 02:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| c36c6526-be5c-3575-8b04-04f2bf6e0eda | -10.7208 | -45.8992 | 2026-09-06 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| a229656e-b72e-32a2-ac10-484de227c506 | -6.9128 | -62.9554 | 2026-09-06 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| de09a64b-0ffb-3041-94c6-746545f201e2 | -6.8944 | -62.9748 | 2026-09-06 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 3b005d76-932f-31c9-ad1a-9ccc3def06a5 | -10.7017 | -45.9016 | 2026-09-06 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| bc2a8da8-f435-311b-92d0-e0adf52d7dc1 | -6.8627 | -55.6199 | 2026-09-06 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| f9646be4-c29e-3d57-9771-178dae73fa5b | -13.7993 | -51.6445 | 2026-09-06 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 8ae7e4e9-ade8-3cbf-98b4-a361ff3c4ac5 | -13.8375 | -51.6609 | 2026-09-06 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| cb3960dc-79bc-3d8b-b761-4b71e98ee851 | -13.7997 | -51.6232 | 2026-09-06 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d740a4a4-4eb4-39ef-a746-922ad955f176 | -14.905 | -44.6782 | 2026-09-06 02:20:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 64e0bad1-892d-38fc-a237-a2dc8623107c | -11.3146 | -45.7061 | 2026-09-06 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0a38a423-bacd-3001-b395-18b2ecd75c10 | -6.1118 | -47.2237 | 2026-09-06 02:20:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 8c66c3db-14e5-3622-bff7-ec9c578aad34 | -5.3645 | -56.0447 | 2026-09-06 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 32010459-97d6-3ded-b2ad-67049c6968df | -11.315 | -45.6832 | 2026-09-06 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 87b643f9-9a95-3f28-ac2c-8b232d80a4e3 | -5.1423 | -56.2703 | 2026-09-06 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e3c7d288-e624-32f4-9716-0caa0f508195 | -5.3646 | -56.0249 | 2026-09-06 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 195.6 |
| 0af1fa19-03e3-3a4e-85fc-4810565e5538 | -13.8186 | -51.6421 | 2026-09-06 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 0a20ca7e-1b06-3e9d-881f-e65f789c946b | -13.8379 | -51.6396 | 2026-09-06 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| cda95739-4e1d-3725-9dae-c38dcae17e52 | -11.3255 | -45.0624 | 2026-09-06 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| fdebf9e1-761d-32d9-a69e-9f7a32e10e3a | -6.6513 | -59.9642 | 2026-09-06 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ab04b2c5-0feb-3961-af48-5a26e4894aaa | -5.1438 | -55.9741 | 2026-09-06 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| aa031bc7-7337-38fc-8b71-bfc5485ba2a2 | -6.6698 | -59.9443 | 2026-09-06 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 4753b384-072e-38bd-945d-2a6fc6e3a471 | -9.1257 | -67.8322 | 2026-09-06 02:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| d9715f65-1f6c-3cc1-b0d7-1e2190c9be64 | -9.1443 | -67.8132 | 2026-09-06 02:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| e978632d-9161-30a9-bd3a-7e938c8a8b69 | -11.2959 | -45.6858 | 2026-09-06 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ec48a96d-193b-3dbd-b39e-121ceb34e353 | -6.9128 | -62.9554 | 2026-09-06 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 4360c9a7-15df-3827-9963-25e5d12c611e | -6.6514 | -59.945 | 2026-09-06 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 4d0c366a-f91d-348a-856a-ce282db2191c | -9.1442 | -67.8317 | 2026-09-06 02:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 49d26a7c-7fd1-37ea-be40-8243e35ae2ee | -5.3462 | -56.0256 | 2026-09-06 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |


[Clique aqui para ver as próximas entradas](README10.md)
