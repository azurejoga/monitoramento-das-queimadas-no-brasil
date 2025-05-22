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
| fea84b24-6c3a-3f46-bac0-e56accf275fa | -11.70934 | -47.78455 | 2025-05-22 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 983e131d-74e1-3cc8-9194-81224b1559a6 | -7.96993 | -49.68892 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d56821cf-b2e5-326e-91d6-17ae8a6b0619 | -9.71105 | -48.6138 | 2025-05-22 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89ebddea-fdaf-3544-b947-c94df294fa88 | -10.5526 | -42.43203 | 2025-05-22 04:44:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b8cc499d-4f40-3fec-b2a3-ea898d9d4673 | -9.95884 | -49.8198 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a03f9c8f-7c86-37cb-bf2b-23c090ac4f6a | -7.94804 | -49.76413 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 725a9d8d-2438-3d61-b276-a07721ea4d87 | -8.59856 | -49.51389 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 852c556f-e001-3eaa-9ba8-7e956c09c25d | -9.37168 | -48.41204 | 2025-05-22 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b897d5bb-670f-3847-8ace-fd7033e64ee5 | -9.04501 | -47.02536 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 044a43d0-b45b-3e99-882a-75b92b00afa7 | -9.2793 | -50.68552 | 2025-05-22 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92c97dae-b9de-3016-a278-ac88d1120945 | -11.24817 | -49.49382 | 2025-05-22 04:44:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef2a3941-1600-3a49-861d-049e174b63a5 | -10.36335 | -47.96925 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f0c6fd77-00ef-38c4-8d4f-d11f5f4c93e1 | -11.55581 | -47.45189 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 08844929-ea3d-34f6-8193-408a14f52180 | -11.60418 | -47.61882 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55b25819-03db-3a61-a677-2b2a821c1a47 | -10.37799 | -47.97889 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48a13a45-8b0b-34f8-bf9b-e55586cc8116 | -10.35049 | -47.82018 | 2025-05-22 04:44:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dea01839-bab3-393f-a58d-07815524b268 | -8.60257 | -49.51065 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b82986a-000a-3473-9651-bc023b598211 | -9.41809 | -58.31657 | 2025-05-22 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 701eaef6-6c32-30f1-98a0-995ab0ce761d | -8.90898 | -50.02538 | 2025-05-22 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7954d9e-5803-3349-a0b0-6a0bcb4f7bd3 | -8.16188 | -61.47749 | 2025-05-22 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 130b2268-de99-3d6b-954f-9bfae1fa3fb5 | -7.9486 | -49.76048 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0db637cd-3743-332a-8e0b-b1dc67fcba62 | -8.7894 | -49.06925 | 2025-05-22 04:44:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 801b0a6a-762d-3aff-a1ab-0e0aa3f5c7ee | -11.56442 | -47.4479 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 35a52140-b077-3330-88b6-43550bbe91d8 | -10.36768 | -57.50021 | 2025-05-22 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ecc77f44-f5e5-3c58-904f-718f1dd4c4f8 | -11.55188 | -47.45128 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b27c861-71cc-31aa-b87a-cf6365e28572 | -10.0984 | -47.09896 | 2025-05-22 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 393bad7b-5ab6-384f-8433-b9a741ff9931 | -8.74798 | -49.74971 | 2025-05-22 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 230afacd-3c2c-39d3-9a68-1ce437a7dc23 | -10.37396 | -47.9755 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23031cfc-d581-3c63-919f-e6b879cc53a0 | -7.83702 | -46.88321 | 2025-05-22 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d288736-b0b6-3bf5-81ef-d1f262b7f6c2 | -8.74854 | -49.74601 | 2025-05-22 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7a7f5657-1a43-36db-ac6b-95f438f21590 | -10.52549 | -47.58804 | 2025-05-22 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0120a30d-17cc-30ef-a554-60b90fae62a2 | -11.57945 | -47.87045 | 2025-05-22 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 924ca77c-49e8-32c2-a65e-4ec66e471977 | -10.03156 | -48.69233 | 2025-05-22 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 75e352c9-3b8a-317f-81e8-cd28972c994e | -7.58044 | -45.86369 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9f143ef-995e-3037-a328-dc3b3afa2bf7 | -11.56692 | -47.45876 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0ad16cf3-e5cb-3c38-88b8-cc5edc7043af | -11.56047 | -47.44735 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 6a35f47a-b76e-38d1-a910-902ebd7dfb64 | -6.63354 | -55.01517 | 2025-05-22 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0e2e446-c17e-317d-8630-d388eded068a | -10.35117 | -47.81553 | 2025-05-22 04:44:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1233953-a62f-352b-8e4e-5094edc6246a | -7.8039 | -46.21266 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dc628f1-6f4c-3d25-8413-529214666ba6 | -11.57723 | -47.87231 | 2025-05-22 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c8343c2-4833-35ad-a423-3bafd18cf7e7 | -11.64213 | -48.09834 | 2025-05-22 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 64165bdc-66df-36cd-88df-af500a80fdb8 | -7.3956 | -45.93879 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb4e9c4e-8260-3f7d-971b-ebb61d0e8e13 | -12.08109 | -47.34667 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1e0a4ca-3fd8-3d0c-8870-0affca086422 | -10.65954 | -49.44234 | 2025-05-22 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ef64024-a7f3-301c-99a8-7907b8de3180 | -9.41888 | -58.3121 | 2025-05-22 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df09129e-fa5a-308f-bad3-7bd889da10b6 | -10.65662 | -49.43788 | 2025-05-22 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4102003-3f21-3f9c-bb1d-c6b8c4d768a2 | -10.37112 | -47.97321 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f404278-ccb2-32d3-a924-5e5ff3dc040f | -9.3357 | -49.91314 | 2025-05-22 04:44:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e79bb0a1-3579-334a-8d47-7cabae0ebe43 | -10.09445 | -47.09837 | 2025-05-22 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd53226e-dcd7-35c6-8d84-ea8a8bb8b2f8 | -10.36268 | -47.97381 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4a27a8e2-c89b-353d-9267-b4a7e886ab30 | -11.79797 | -49.33619 | 2025-05-22 04:44:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed66a8e8-7968-352e-8cf5-9bcbe7d2b6de | -12.07805 | -47.33902 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b728dbb-6e9f-38e4-bb3e-3cdc3f314a25 | -9.96342 | -49.81281 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f02655c4-a755-3775-9124-a7188d570ad3 | -9.29044 | -57.55389 | 2025-05-22 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5bd132e3-8448-3f09-9d94-6bcbbcadcdd8 | -8.91009 | -50.0181 | 2025-05-22 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4dd29c5-3349-3481-8878-d787dfa1e010 | -9.67534 | -50.95445 | 2025-05-22 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16de5fbb-d179-3063-b3d6-5f1dead064b1 | -4.29377 | -48.27551 | 2025-05-22 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ad0084d-11c7-36e8-867c-1352a02f8662 | -10.12158 | -58.22294 | 2025-05-22 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35dcf135-e3a2-3742-8fb5-fe8f9ad5223f | -8.73705 | -47.98595 | 2025-05-22 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93b94859-e462-3ff3-8a91-0bc6fd0735dd | -9.95941 | -49.81604 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 440542ab-d097-3667-83cd-c7fd3d687d53 | -11.55904 | -47.45758 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| dd876b28-81d2-3cee-a2cd-5e3448638149 | -10.3636 | -47.97207 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 456c9149-0367-328f-a0fe-8341cd0a4095 | -10.54715 | -42.43129 | 2025-05-22 04:44:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1b8dd782-55cc-3f16-b5c1-5d58640310b0 | -11.79586 | -49.33301 | 2025-05-22 04:44:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffa0b916-9519-3b45-827c-2f17fce2f5b1 | -9.03337 | -48.93915 | 2025-05-22 04:44:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af19514c-665d-3975-a56f-bc049302fa84 | -7.80443 | -46.20909 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38bc975d-0c3a-3f4e-82e2-0e37e280efc0 | -8.16822 | -61.47467 | 2025-05-22 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b55fa0a-dc8b-33a5-8dbd-d4f9ebbde4b2 | -10.36425 | -47.96746 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 48bd6869-60c4-3b04-9d1c-5ed4da578e2b | -10.34137 | -51.68922 | 2025-05-22 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1cb8b0c-0b0d-32ae-95dd-7abb020fabdf | -11.79856 | -49.33212 | 2025-05-22 04:44:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 612ac85d-8686-3c82-b945-d34fc6b201db | -8.26357 | -54.96475 | 2025-05-22 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7a1c2ef-8a63-339e-a449-8b45b107a4c9 | -11.56586 | -47.4376 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c1ff42a7-30f3-3b27-8e06-710a8dffe104 | -11.79441 | -49.33564 | 2025-05-22 04:44:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aac676ca-d669-368d-b666-a46a41bedd2b | -11.79525 | -49.33707 | 2025-05-22 04:44:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87142eb7-79e0-34a2-bb7f-0ee506fa08f3 | -7.95143 | -49.76466 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f12edbb-e428-32e2-a30f-0002755c401c | -9.85931 | -60.32096 | 2025-05-22 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5638c8e-0a3e-37be-885a-fd4346b28d15 | -11.56765 | -47.45356 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bdcd0ffc-4998-3320-b540-0ae5a7bdb11d | -9.04429 | -47.03034 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2db9c121-4b21-3336-9105-283e18e070e8 | -9.29114 | -57.54992 | 2025-05-22 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f4f3e5a-ef2a-3828-b5aa-c19fc68fd59d | -10.36711 | -47.96983 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d6ce4126-55f5-39b2-8fb1-6b83bd4deb76 | -10.65603 | -49.44182 | 2025-05-22 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bca4cbca-42d8-33eb-b4ad-e75035cc8019 | -7.58097 | -45.85999 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0962235-3e50-3f86-a5c4-983bbe46358e | -10.36736 | -47.97265 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 220fffae-6497-3cd0-9b53-ac40552eb1b4 | -10.12109 | -58.22585 | 2025-05-22 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37e83c73-77b2-392d-8039-04f35538681b | -11.79499 | -49.33157 | 2025-05-22 04:44:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b5255cb1-f844-33cb-9b26-2f516e3a6556 | -11.60345 | -47.62599 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f55cef25-92f1-3bc1-8ef2-86e8bdff429e | -10.34082 | -51.69271 | 2025-05-22 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aabc222-8e59-3188-a986-2cc042ce04d7 | -12.08205 | -47.33962 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 302d0f93-1f67-3e39-ad96-4ad401fef7e6 | -10.36921 | -57.50021 | 2025-05-22 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1ff2ada-0686-3b65-8d3d-9b917cb93c4a | -11.57486 | -48.37776 | 2025-05-22 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1bd51b6-0536-31fe-a1db-3c79e69cfbae | -10.36577 | -47.97891 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 612f5d16-4ee9-3650-8828-9817f35bf70d | -11.58072 | -47.61563 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff326e03-5160-32d3-9662-7c79667c2c29 | -11.56192 | -47.43699 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6641527b-4b13-31e9-a0ff-ba0c8b6a81d4 | -11.5551 | -47.45702 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 7141bff0-f8fa-3d0a-9637-f9280e6a6e83 | -9.60306 | -49.01944 | 2025-05-22 04:44:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7b4c206-b7fc-3d7e-b08e-9c89d23cf43c | -11.5716 | -47.45412 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4fd76ca8-2cb0-396b-b226-089325370977 | -10.71389 | -48.80585 | 2025-05-22 04:44:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc9857c3-521b-3bb9-8d53-976890741b63 | -10.46485 | -49.15016 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fda3d05d-6631-3c1f-b2a1-baf38dab0bb0 | -7.24189 | -44.71633 | 2025-05-22 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75fca353-688b-37c4-91a8-82d125d62f8c | -8.47988 | -49.60336 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README16.md)
