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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99f52ce5-40b4-3f69-8761-d851fc405516 | -6.98984 | -43.27765 | 2025-01-04 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dc0ed546-0f6f-3a94-b9d9-a82ad204b1e9 | -6.98366 | -40.00969 | 2025-01-04 04:08:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0e9ee6e2-23ad-3303-95e6-1cd3f3f08bf7 | -10.28663 | -36.36691 | 2025-01-04 04:08:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5d5f8a8b-c308-3255-a44b-82f4b1a03a84 | -10.56269 | -37.03655 | 2025-01-04 04:08:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9bbcf7e1-f511-3d9e-ac22-2c670fce1ed6 | -8.30906 | -38.76073 | 2025-01-04 04:08:00 | NPP-375D | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a9d73e2a-112f-3aac-a244-7f373b369776 | -9.92171 | -36.00188 | 2025-01-04 04:08:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9c2826ba-62c3-3c75-807d-070a83e42b54 | -10.76702 | -44.39217 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cc8695a-36e5-3d45-863c-db3f1a587f79 | -5.50397 | -44.29502 | 2025-01-04 04:08:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1621fe5-95d9-348a-b1ad-6cf289d1e1b6 | -10.21715 | -44.76215 | 2025-01-04 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7fb4452-96a2-33cd-bd6b-0a27d34e052a | -7.56179 | -39.00814 | 2025-01-04 04:08:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5c908958-15e8-3426-9096-9e66ccc30add | -7.69566 | -41.66749 | 2025-01-04 04:08:00 | NPP-375D | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6dd78154-a19d-34ec-9539-728e5f6fa6f9 | -9.85146 | -37.12128 | 2025-01-04 04:08:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 8fc3c237-9afc-3588-865b-d4364b014669 | -6.79793 | -35.18441 | 2025-01-04 04:08:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b383accf-8d16-3309-899d-57909175dd37 | -10.42608 | -40.37293 | 2025-01-04 04:08:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6c017010-e82d-3d39-b889-7cccc1cfcc14 | -9.90713 | -38.10823 | 2025-01-04 04:08:00 | NPP-375D | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7f71d696-d1d8-3c4a-b911-3f67e407536d | -9.84733 | -37.12073 | 2025-01-04 04:08:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4cb1c394-d6ce-362e-a210-63ad06e4b1a9 | -8.98301 | -35.61594 | 2025-01-04 04:08:00 | NPP-375D | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 35934c05-d6c5-3b29-b072-b809d7759e63 | -5.16683 | -40.76119 | 2025-01-04 04:08:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e922cc71-8aa7-344c-90a5-be8d0214b6a3 | -6.18254 | -36.55984 | 2025-01-04 04:08:00 | NPP-375D | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b8fb896c-6e80-3802-93fd-06f61d9583de | -10.54513 | -44.68079 | 2025-01-04 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 693a8473-e311-3959-a897-f1c512cdc51f | -6.70512 | -39.14999 | 2025-01-04 04:08:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 375b621e-918b-365a-b55f-14bfd8b0b8a5 | -7.85081 | -37.71481 | 2025-01-04 04:08:00 | NPP-375D | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c2519c2b-2480-3fea-8564-faa6d925a2ed | -10.42489 | -40.37387 | 2025-01-04 04:08:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4cbacf0c-349a-30eb-bdb4-9031d339d11a | -10.60475 | -44.33859 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8ad190d-8c1b-3301-8045-4d088acf9a85 | -10.61157 | -44.33973 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 9ec78fb0-1853-3580-bc14-79d17271cf57 | -3.75641 | -42.31535 | 2025-01-04 04:08:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dc31149d-74d8-318f-b305-db719fc643a4 | -10.60877 | -44.33544 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| a04d6282-1511-3424-a74b-1965f189bb49 | -4.00639 | -40.9323 | 2025-01-04 04:08:00 | NPP-375D | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ca30523e-e78d-3a5c-b3ae-881007371d6e | -6.44035 | -40.00341 | 2025-01-04 04:08:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 08495ef0-7e60-33ed-a7b6-49831701b59e | -6.66303 | -47.60262 | 2025-01-04 04:08:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b839a741-80c3-322d-b7d9-d842bcc496d0 | -7.99743 | -35.23351 | 2025-01-04 04:08:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7e73e372-f8ea-3aa1-8b13-242839cd8b16 | -10.60998 | -44.328 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9adfe170-8f0e-35cf-aa65-c91e97be07c8 | -5.49974 | -44.29844 | 2025-01-04 04:08:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcf602a1-ef25-326a-aa71-61aad250a8b1 | -10.5937 | -44.331 | 2025-01-04 04:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 86e89e71-f054-35f0-a4f9-c8e1a9f15680 | -10.6124 | -44.3517 | 2025-01-04 04:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 394c4a1d-486e-393e-9322-15edb85893d0 | -10.6319 | -44.3257 | 2025-01-04 04:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 359fc2f9-a743-3ffb-b63b-3c53949564db | -10.6128 | -44.3284 | 2025-01-04 04:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 47be1244-a8d9-3328-82ac-295ca634307d | -13.98662 | -39.99011 | 2025-01-04 04:10:00 | NPP-375D | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c208a96f-cdd2-3d43-9d33-8ce94d751694 | -13.46274 | -41.33581 | 2025-01-04 04:10:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 05242077-0ea1-384b-bbe1-9208b0534859 | -12.48466 | -43.78976 | 2025-01-04 04:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdf7f536-a19d-385d-a747-83014c681b07 | -12.27051 | -44.98589 | 2025-01-04 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c2ab7d3-4274-30b3-9807-0257a7b9ed90 | -12.46706 | -46.93771 | 2025-01-04 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 164862bc-9a95-3e5c-82bd-4d429124d20c | -13.4593 | -41.33525 | 2025-01-04 04:10:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 03754cb1-a63d-31f9-b9d5-44aeee17f36f | -11.8003 | -49.32517 | 2025-01-04 04:10:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 14780056-9599-3fc1-bd86-edda7b127ed2 | -11.82602 | -44.21824 | 2025-01-04 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b50bc6c6-77b9-3cf8-8d82-a5635c31f028 | -12.4716 | -46.93378 | 2025-01-04 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c26dc55-735b-3674-be36-04912d33a0ba | -11.8294 | -44.2188 | 2025-01-04 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cbfc11f8-431f-363c-ae8c-b90b5d1ce594 | -11.80469 | -49.32603 | 2025-01-04 04:10:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3ea0ff15-d5e5-3aa3-8763-4d1272b7c4f1 | -12.21562 | -42.44881 | 2025-01-04 04:10:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f314907b-aad9-35e1-b58a-64d7396c0f89 | -13.64003 | -41.35825 | 2025-01-04 04:10:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4face14-7ffd-35e2-ba77-f5faa784c582 | -11.11151 | -45.29575 | 2025-01-04 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7da05ee-1d1c-3518-b7c3-b9ae8ca1133c | -13.90135 | -39.18354 | 2025-01-04 04:10:00 | NPP-375D | IGRAPIÚNA | BAHIA | Brasil | 2913457 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 35996512-8ae5-37fa-9eaa-d92a180507a6 | -12.23052 | -44.75788 | 2025-01-04 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d6a75c8d-3112-33c6-b2b9-95471b7e0cfb | -12.46785 | -46.93312 | 2025-01-04 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed882e5d-9a15-3e3f-9994-474e5dc8ae38 | -12.05842 | -40.01363 | 2025-01-04 04:10:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 82efc96c-e12b-3785-9e3b-af478e6fc40a | -12.106 | -44.75366 | 2025-01-04 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 465fe185-bd34-3a5a-9a09-9ac6a67ae2c1 | -12.47082 | -46.93837 | 2025-01-04 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 780504ab-4086-3d09-91dd-08c170eecf94 | -13.99029 | -39.99065 | 2025-01-04 04:10:00 | NPP-375D | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e9d000ce-086c-36b1-9732-2d5dfc64f677 | -12.16905 | -44.62155 | 2025-01-04 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3250206-4226-3a97-ac5f-a4cf97d5bd3a | -11.37363 | -43.8395 | 2025-01-04 04:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fed0c8d4-e01f-3842-ad38-91c9b4396570 | -12.90114 | -43.65729 | 2025-01-04 04:10:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74f20356-c8ae-30ef-86d1-23e7008bd50f | -10.50322 | -49.12949 | 2025-01-04 04:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2deaccf-f9ff-3339-89c2-a98265919537 | -12.71715 | -47.62754 | 2025-01-04 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0165f05c-f6aa-3267-a6bf-4a3a876198a1 | -12.17027 | -44.61411 | 2025-01-04 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1b7e020-4928-36f4-8a8a-9bdf561b8d6a | -12.08837 | -40.27229 | 2025-01-04 04:10:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 117e0056-e65b-3778-8f4d-7e4b1a1f8f72 | -22.9205 | -45.41374 | 2025-01-04 04:12:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a910da45-2edf-30f1-9f42-2c349fb6fe6f | -22.67649 | -42.85393 | 2025-01-04 04:12:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 38ac610e-96dc-3dde-abec-9a5980571c2b | -22.67589 | -42.85815 | 2025-01-04 04:12:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 10323f7b-92d0-3d07-8544-3fea33d02e25 | -22.67578 | -42.85648 | 2025-01-04 04:12:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1e93f6a3-37b0-36f6-a13a-45a991235577 | -22.78521 | -43.75527 | 2025-01-04 04:12:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4cb31345-6c40-35a9-9375-6fc1117f48e6 | -22.67637 | -42.85225 | 2025-01-04 04:12:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5fed230d-fc81-3d34-a25d-9aacca87cecc | -30.72707 | -53.33233 | 2025-01-04 04:14:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| af78bdf4-196f-31ed-acc8-12bd256dcfc3 | -27.62633 | -50.21117 | 2025-01-04 04:14:00 | NPP-375D | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce47860d-1879-3958-9648-40db2ec9d5ee | -25.19107 | -49.327 | 2025-01-04 04:14:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 59b3b760-94fb-3d93-8a92-9a7ba4a2d0e9 | -27.62717 | -50.20657 | 2025-01-04 04:14:00 | NPP-375D | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 07ca46f9-c723-36ca-8270-09ff72eac992 | -24.24349 | -50.74176 | 2025-01-04 04:14:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b6c0c1df-e165-32cd-966a-355d976e5d90 | -10.6128 | -44.3284 | 2025-01-04 04:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| a57c5011-c3bc-3dbe-81a5-79b0ae6a4f41 | -10.6124 | -44.3517 | 2025-01-04 04:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| e159e5c7-9574-3983-b893-36290e3b68e8 | -10.6319 | -44.3257 | 2025-01-04 04:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 367df935-c2cc-3a65-bc4b-ec7753d8909a | -1.26875 | -46.3299 | 2025-01-04 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e1e91be-d49e-309a-a238-5e2f573666d8 | -6.66212 | -47.60314 | 2025-01-04 04:29:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22687cc7-6ffa-3086-b2b3-e484ba8c254b | -4.39107 | -37.84349 | 2025-01-04 04:29:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 01fc4568-56f3-3612-8ffe-d10eb6fd7f3c | -6.21063 | -46.22157 | 2025-01-04 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7e8699d-221c-3dfa-9412-222e0ec43265 | -5.50158 | -44.30088 | 2025-01-04 04:29:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcc8bdd3-b7bd-3a1e-886d-fe0f99b811b1 | -8.30705 | -38.76011 | 2025-01-04 04:29:00 | NOAA-20 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9052b19d-3e22-3ee5-ada0-81f129a1e81f | -4.16253 | -42.02361 | 2025-01-04 04:29:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5ea7b238-bcad-30be-bcab-b26e350ddde0 | -5.76081 | -46.04552 | 2025-01-04 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d2191c4-9e32-3489-8783-1bb4bf8dfb9c | -5.71391 | -41.40749 | 2025-01-04 04:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 35c0fbb0-9733-32ec-80f1-9f9d8c1ebda3 | -7.21686 | -38.63871 | 2025-01-04 04:29:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 986e6746-c437-31cf-977e-d5dfb57f3095 | -6.70594 | -44.31908 | 2025-01-04 04:29:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7db01d8-4276-33ea-afd7-f63c2571e116 | -6.98259 | -40.01774 | 2025-01-04 04:29:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| bce8be51-68b5-3890-8259-f5ad25e9d7f8 | -1.37392 | -46.43793 | 2025-01-04 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f4d8b64-9ba2-310e-9b95-a8be029a76c1 | -2.96611 | -41.85502 | 2025-01-04 04:29:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 89fff654-9ba0-38fa-96bd-19405d28caa3 | -5.62873 | -44.83751 | 2025-01-04 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfef3756-03ad-36dc-b0eb-a11fa503ae28 | -3.22079 | -48.76228 | 2025-01-04 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1a39f65-4ba0-3ada-885f-59c40a7651a0 | -2.44263 | -53.82346 | 2025-01-04 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06ef7cab-832e-3e1a-838a-851366e85206 | -4.39657 | -37.84429 | 2025-01-04 04:29:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2602b166-d5ed-3e02-b562-5f5984cb121c | -1.27152 | -46.33386 | 2025-01-04 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17969ed1-3924-3fb9-88a9-aed161a5d672 | -5.38166 | -43.25305 | 2025-01-04 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 863a88c9-6c7a-33a8-a949-09bcacaa8013 | -6.16311 | -44.79241 | 2025-01-04 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README7.md)
