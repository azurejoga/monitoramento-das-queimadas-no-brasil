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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03679654-238c-38b4-bc6c-7747a3e1e173 | -7.5668 | -61.2096 | 2026-08-28 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| fe878626-249e-3e42-99b0-a20aa044485a | -14.2302 | -45.2472 | 2026-08-28 16:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 2bf5fce9-edd9-3c62-a531-7fef6f3ad7f0 | 1.4917 | -55.964 | 2026-08-28 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 073bb12b-94f2-3799-a1a1-8f8d07484be9 | -6.7267 | -59.654 | 2026-08-28 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c688da93-bf79-3642-8950-f9746244c359 | -8.6694 | -49.5369 | 2026-08-28 16:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 47b93aa7-4a83-3e08-a7ba-6caf9e183923 | -6.7833 | -59.4208 | 2026-08-28 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 4828472f-5aa0-3e81-8b6d-e29fdfa3bcde | -8.6881 | -49.5353 | 2026-08-28 16:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| e7f4bf74-e961-3730-8197-abc161995238 | -9.2477 | -57.0697 | 2026-08-28 16:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 7cfda0ff-3ef7-3a45-a9b4-8050cf81bc4e | 1.4917 | -55.9837 | 2026-08-28 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 88baea31-7c59-33c1-8d4f-fda62f88119e | -6.8756 | -59.4171 | 2026-08-28 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 65cb2b65-1f39-3d25-86c6-aaad65382e03 | -9.0462 | -69.587 | 2026-08-28 16:20:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c81641d3-c4fe-3018-a683-df029abbc0c7 | -7.4735 | -61.3846 | 2026-08-28 16:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 7bf75e1a-19d4-3964-bac6-2ae1ff81eb65 | -6.9315 | -59.3184 | 2026-08-28 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 0c2f61b0-7e17-3850-96f8-4d1f491640ef | -13.2835 | -51.4968 | 2026-08-28 16:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c4d6e5c0-9cb0-3a19-9b3d-0eb950455dc1 | -11.1643 | -45.5668 | 2026-08-28 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 9a0e668d-4a67-3739-8383-97b42324a59f | -6.018 | -57.8242 | 2026-08-28 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 70dcb224-dcf8-3b45-bbe6-03b53da8db61 | -6.8017 | -59.4394 | 2026-08-28 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 77937809-3bb9-3d69-8b8b-fcb4d8fed067 | -6.7123 | -58.9412 | 2026-08-28 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 6ecd2845-f5f5-338d-b8f7-4a344e9ac7eb | -10.8993 | -50.4945 | 2026-08-28 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 4f1d359e-3046-32dc-91ae-a7e3afa1a7c0 | -6.0179 | -57.8437 | 2026-08-28 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 95ee0b3c-5968-37d7-8568-b4a0bcb36bad | -8.6919 | -70.9881 | 2026-08-28 16:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 49.2 |
| fa5b763f-5b2b-38ef-a5b0-8b993a8bda7d | -6.7647 | -59.4601 | 2026-08-28 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 9c6fce79-4c9c-38be-b5e2-e13cef0b5d20 | -6.8358 | -59.9379 | 2026-08-28 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 161.3 |
| f646ef4c-2cac-37be-81af-dedd2d8ca43a | -8.7767 | -49.9977 | 2026-08-28 16:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 600e2cd7-bfb8-3d3d-af47-225ede6c8caa | -7.5847 | -61.3042 | 2026-08-28 16:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 0d0d3fce-02ce-3ca3-b57a-8974770dbc6e | -7.0057 | -59.2575 | 2026-08-28 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 035322f0-b843-3118-ae30-a91a1b66cb68 | -4.9582 | -56.277 | 2026-08-28 16:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 1c5f2918-6146-306c-8288-7a16f092c6fb | -8.7764 | -50.019 | 2026-08-28 16:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 5e2cba28-ac5f-3f5b-a171-a4d31107619a | -6.598 | -45.201 | 2026-08-28 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| b03b0669-831c-33b3-b9ec-5a434186db16 | 1.51 | -55.9835 | 2026-08-28 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| c86bec44-3b58-3306-8372-dd5a1630b089 | -10.7598 | -54.0179 | 2026-08-28 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 21ebea1b-1c62-30dd-921e-5608e9eb19e0 | -10.7839 | -50.6346 | 2026-08-28 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| be826268-ffce-3f14-a6ab-be98bc3e7ee0 | -9.0278 | -69.569 | 2026-08-28 16:20:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 0142f24c-131c-3c48-825e-a30b1026ac28 | -9.0824 | -69.8992 | 2026-08-28 16:30:00 | GOES-19 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c63ebb36-df4a-3966-8829-c81da0e87d19 | -13.1906 | -51.3166 | 2026-08-28 16:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5d5737b2-baa3-3aca-b021-3d18b3ee98d2 | -11.1452 | -45.5694 | 2026-08-28 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| d20a314f-fe59-3e43-ad9e-4c6ce86e5574 | -5.9995 | -57.8444 | 2026-08-28 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 603a5c39-c31d-3306-adb3-ecbdd810bc18 | -8.3717 | -62.716 | 2026-08-28 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 88684496-7c8f-33e6-97f2-29e053056077 | -6.5865 | -55.4346 | 2026-08-28 16:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 9a167a12-cec3-348a-a6fb-035ad7092254 | -9.2477 | -57.0697 | 2026-08-28 16:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| b5193fa9-e63a-3f80-97bd-640137516002 | -11.1998 | -55.0805 | 2026-08-28 16:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f325e617-15e5-3e1a-b5ce-a7702e3c6459 | -14.5827 | -53.1744 | 2026-08-28 16:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 3a92a9c1-3a95-3ca0-a375-c57c131b7aab | -3.2901 | -61.5747 | 2026-08-28 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 48de9fef-b921-3766-a896-77ce42bdec9b | -10.937 | -50.5118 | 2026-08-28 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 0722fb8c-3904-3c1c-8344-2092c89542f2 | -6.3862 | -54.9651 | 2026-08-28 16:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 22440a4d-44a5-3ec1-8688-d920cbc33430 | -6.8384 | -59.4571 | 2026-08-28 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3952bd6f-e822-3045-aa03-73b21a5905f1 | -8.5585 | -54.8991 | 2026-08-28 16:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 7d61eb61-572a-32ca-98dc-dcfd6977a9cb | -7.6031 | -61.3225 | 2026-08-28 16:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6af44729-1f3b-38cc-b963-36cb9c38d38a | -6.9872 | -59.2582 | 2026-08-28 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b1c1f11a-c6a7-3b77-80a1-ccab05ade5f7 | -8.8372 | -49.6291 | 2026-08-28 16:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 3bcc8f06-742c-3a07-b13f-3a27fa00f979 | -10.7649 | -50.6366 | 2026-08-28 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 07f108f9-f1ec-37dc-9b4e-6fead12f7b24 | -6.8015 | -59.4586 | 2026-08-28 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 23e47002-b3ad-390d-bf4e-2d83750ddbc0 | -12.3999 | -48.2073 | 2026-08-28 16:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4325ad79-0288-3336-9808-9e95273c79dd | -8.5777 | -54.8373 | 2026-08-28 16:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 8a5cfc61-37f0-3c1a-97ec-9db979ad89b1 | -11.2111 | -51.2264 | 2026-08-28 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 426cd10c-3bac-3233-bc75-dc19e9fa59dd | -8.5971 | -54.7553 | 2026-08-28 16:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 30192a20-5252-3a8e-b8d4-82eb1e3ccc6d | -6.641 | -58.4987 | 2026-08-28 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 9ea3bc52-ffec-38a4-b2f7-1ab68b73a986 | -6.8357 | -59.9571 | 2026-08-28 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 9b407afc-33f3-3f6a-9418-2a70cbe17f46 | -8.795 | -50.0387 | 2026-08-28 16:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 2d00cfeb-ddab-398e-a0b8-a09c05e63345 | -10.8993 | -50.4945 | 2026-08-28 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| fb284056-8fd8-3e11-a1f5-6ab1b317d3ab | -6.8756 | -59.4171 | 2026-08-28 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 24a45ca7-837f-3742-9b64-b2c0500d6e4e | -3.2178 | -61.2362 | 2026-08-28 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 396f4c29-7ded-3e2c-a69a-97b86f80130e | -8.8187 | -49.6093 | 2026-08-28 16:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| dcb99b1e-727a-37cb-9f06-dd293c0ba584 | -6.7123 | -58.9412 | 2026-08-28 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 4d67b6bf-6701-3d43-ae4b-fdc2d854e51c | -12.2281 | -50.5578 | 2026-08-28 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| f9d64814-6edd-38a9-9782-e3aae9d25035 | -6.5829 | -58.9851 | 2026-08-28 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| b241ce18-75c0-34ad-8397-23a8c295ec34 | -10.5593 | -50.4663 | 2026-08-28 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| bd82ab21-8f42-382b-8705-268cf76f96d0 | -8.9873 | -65.4379 | 2026-08-28 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 65bb8d6d-9921-3fb8-81d7-b80817c85ab2 | -6.254 | -55.391 | 2026-08-28 16:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 38a7664c-ba8f-33cd-aff2-ecde38eb1957 | -10.8422 | -50.5219 | 2026-08-28 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 18eb3f2f-351f-3e3e-a597-00c2c3bf723b | -10.7649 | -50.6366 | 2026-08-28 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 8208ef60-61a6-385d-ae39-6e46d14a6cc7 | -8.5777 | -54.8373 | 2026-08-28 16:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 3558f31b-eabc-39ec-b04a-de8d6f69e49b | -6.8017 | -59.4394 | 2026-08-28 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 93ca5240-a7a6-308d-8fe6-59a914defbc0 | -10.7839 | -50.6346 | 2026-08-28 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| c7f786f3-aaac-34d8-afe5-564deb3e9233 | -6.8019 | -59.4008 | 2026-08-28 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| f4db849a-ff65-35b9-bbc2-cbf3e13906be | -8.5971 | -54.7553 | 2026-08-28 16:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 7e79ce8a-1f50-3f61-8278-d7332bb693a2 | -14.2302 | -45.2472 | 2026-08-28 16:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| eccf8551-0251-3719-9242-91c16ca3019d | -8.8372 | -49.6291 | 2026-08-28 16:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4e3641dd-5ec2-39ba-855e-0b8827c5a127 | -6.5608 | -56.5266 | 2026-08-28 16:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ff5666a3-9da9-34bd-9d9b-e8ba7bb304df | -6.1292 | -57.7223 | 2026-08-28 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2b5033ee-f549-301c-b79d-8f76e8917f27 | -6.598 | -45.201 | 2026-08-28 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 88176527-f61b-3d27-8d73-af5825c1edd2 | -9.2477 | -57.0697 | 2026-08-28 16:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 58c3c977-8dd8-3ae4-9672-ff2d1c8773ec | -10.7598 | -54.0179 | 2026-08-28 16:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 43a265b3-1c9d-3a5f-a061-b665f906c02b | -12.3999 | -48.2073 | 2026-08-28 16:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4f028bb1-02f8-349b-bce3-65277504dda1 | -10.2557 | -64.4915 | 2026-08-28 16:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 8fc30ea4-8d6c-377a-859c-bf65a639e923 | -6.641 | -58.4987 | 2026-08-28 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 66086fa8-5e75-3731-a397-0b7941e80592 | -3.8947 | -60.9399 | 2026-08-28 16:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c15e80e9-6e24-32ed-8f79-30ffe84b7310 | -10.7839 | -50.6346 | 2026-08-28 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 55f45a6c-e03a-3362-bee5-1c790456d3c8 | -6.9872 | -59.2582 | 2026-08-28 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 79345d4c-0a3f-32f4-99ae-c60243bcac11 | -8.2227 | -54.9613 | 2026-08-28 16:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 8a1fc41b-7967-310f-8710-2fccf27457a1 | -6.7123 | -58.9412 | 2026-08-28 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 1514732b-e579-370b-9224-12bdd4adfcf3 | 1.51 | -55.9638 | 2026-08-28 16:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 03a4cfaf-5963-3efc-9a57-394c81aa192e | -10.899 | -50.5159 | 2026-08-28 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| eca32fd4-fbd8-3a70-8282-edcb4847c54e | -5.9995 | -57.8444 | 2026-08-28 16:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 63b0c438-8944-333c-b88e-ef8904f1bb20 | -8.8187 | -49.6093 | 2026-08-28 16:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| a109df14-f9df-35b7-a834-fd53c0a4559d | -8.7767 | -49.9977 | 2026-08-28 16:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| c7518e96-414a-3660-bf97-07f292963cbf | -6.6169 | -45.1767 | 2026-08-28 16:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 265d020f-6343-3e22-b80d-e0171185d17e | -10.8801 | -50.5179 | 2026-08-28 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9fab0e98-d625-30d2-a181-2e9e039edbce | -10.8422 | -50.5219 | 2026-08-28 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| c09614d9-e34c-3aa5-9710-4dad145b2fd0 | -6.254 | -55.391 | 2026-08-28 16:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |


[Clique aqui para ver as próximas entradas](README102.md)
