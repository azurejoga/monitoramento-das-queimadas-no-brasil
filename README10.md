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
| e08654d6-5ed7-3076-a4cb-466189af5dc0 | -9.28522 | -50.33205 | 2025-07-07 04:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbaff5e6-40c4-3004-b028-a41d588ae746 | -6.64036 | -43.17449 | 2025-07-07 04:59:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4f3fd22-38d8-3302-89d3-19b820c6854d | -7.71554 | -44.57323 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0768b92f-dfad-3064-81e8-19cfe1d737d8 | -10.63951 | -46.37975 | 2025-07-07 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96dbe1a7-eda2-37c2-8026-a65e85ee037f | -6.30096 | -45.7325 | 2025-07-07 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 56500b3b-9b4a-38bf-902c-341ed66984c8 | -6.6933 | -43.14909 | 2025-07-07 04:59:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e6ecd02-abd3-3e86-b432-60c02fc2e184 | -6.1692 | -48.05817 | 2025-07-07 04:59:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 52bd677b-e218-3ac8-bfde-a4492eb265cf | -9.79886 | -53.23463 | 2025-07-07 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78c5ccbd-9e72-3daa-93a6-90ff60743662 | -9.33371 | -58.8495 | 2025-07-07 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aad2afcc-a095-33a3-8af4-25108f19f46d | -8.14191 | -47.16883 | 2025-07-07 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3061cdd1-079a-31ea-ae62-66c69da7e035 | -7.69757 | -44.57851 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 766f0a44-289a-3bc1-863f-4b26cee99391 | -10.58121 | -49.11877 | 2025-07-07 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c93dc299-7055-3489-9b68-cd2792113513 | -7.27341 | -44.6554 | 2025-07-07 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce3f6bdc-8276-3c52-8079-8503a6733308 | -7.69243 | -44.57397 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53d17e15-448f-31e8-a51c-1b14bbdcbc95 | -6.70749 | -47.80136 | 2025-07-07 04:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 044000df-6eed-331d-98f4-088cddfb3323 | -8.05986 | -43.1146 | 2025-07-07 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| fecdc28d-b171-3c06-aa5c-f84cfe8ddb4a | -10.12895 | -57.7796 | 2025-07-07 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0a1617c-ea0d-3baa-863a-fee5ab4d9d9a | -6.16548 | -48.05333 | 2025-07-07 04:59:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9f507649-57b8-3059-bab9-f018b2960bcc | -8.06108 | -43.11852 | 2025-07-07 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 49b74cae-f154-30c7-86e3-e0f0810ffcae | -9.35491 | -58.83884 | 2025-07-07 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85ea604e-b27d-3113-ad6f-1855311b5302 | -11.88051 | -44.88836 | 2025-07-07 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a6be938-f279-3fb6-9d0c-75574d12a0e1 | -7.64228 | -45.36391 | 2025-07-07 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ef8070b-a10f-3305-bccb-ab51ba0195e0 | -10.12541 | -57.779 | 2025-07-07 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf3ac364-3972-3e26-b6f8-b825c00ee1fd | -10.95043 | -49.2539 | 2025-07-07 04:59:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dac8bbd-6b70-38f4-b072-842c78505091 | -8.58663 | -54.98322 | 2025-07-07 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1af44b4d-711b-3b12-a274-04905a454354 | -7.69192 | -44.57774 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5561917c-9282-3dcc-9a74-23b507e10492 | -10.63392 | -46.382 | 2025-07-07 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d8174dc-400e-3754-bc23-7c028228fa23 | -6.71131 | -47.80648 | 2025-07-07 04:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| da300894-a644-337e-940b-c0a510927cba | -6.69391 | -43.14454 | 2025-07-07 04:59:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cc14674-2cec-3b05-99c6-4e37df7a680e | -9.35869 | -58.83947 | 2025-07-07 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff046a85-62a9-3bec-b16d-09da7c0171b3 | -7.70372 | -44.57555 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb4ad47b-1c53-34ed-91c6-3199109d8955 | -7.64767 | -45.3644 | 2025-07-07 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59ede394-f240-31d7-b9ee-eb0fa8ba6902 | -10.50595 | -51.87844 | 2025-07-07 04:59:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41b30f1b-2891-3666-969d-7f23d4111753 | -6.30245 | -45.73602 | 2025-07-07 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2d528308-0383-3182-b90b-5c6bde61c2ac | -8.06609 | -43.11545 | 2025-07-07 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 599040f0-047e-30d5-9ffe-56ae654af6a3 | -10.57523 | -49.13028 | 2025-07-07 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9bf5bdb4-b6ef-35c8-bc18-b3f582ca446b | -10.57468 | -49.13436 | 2025-07-07 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55c6fac0-5a76-3f49-8137-72bbec3bc306 | -9.33749 | -58.85012 | 2025-07-07 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a503674a-6963-3083-9176-e69216fdac77 | -6.29628 | -45.72874 | 2025-07-07 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 446c491e-694b-3077-804b-09828412b5c9 | -10.95217 | -49.25329 | 2025-07-07 04:59:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 193e5226-a594-3bdd-b636-917970ae0698 | -6.16487 | -48.05745 | 2025-07-07 04:59:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 08a69436-9670-3b8f-9da4-dd1d9e868793 | -7.69707 | -44.58222 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be93f2bf-5b4c-33fa-9bc3-ae1701518be2 | -6.30053 | -45.73551 | 2025-07-07 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 47713930-babc-3b8d-a257-a8d279d53ae1 | -10.64847 | -44.48493 | 2025-07-07 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aebbe80f-8dec-355d-a828-e774d05664af | -9.70673 | -56.18215 | 2025-07-07 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71edbf6c-fffd-31fa-a9e6-499f9eaaafe0 | -7.68577 | -44.58071 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40835553-5a35-3f3f-8352-a7f45dcda3e5 | -9.58174 | -57.39877 | 2025-07-07 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 958e3a69-3daf-3ef2-bf75-067405576e26 | -8.85897 | -47.94979 | 2025-07-07 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ead7c611-3a73-3b2d-9f17-c5b1fb06a9b6 | -7.68527 | -44.58447 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d1b639f-d743-37d9-bf0e-ad6bb9826414 | -7.70989 | -44.57253 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d594ced-7442-38ba-b972-bc5f5c5d75c7 | -10.57037 | -49.13367 | 2025-07-07 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e811c704-3cb8-3c54-8a87-ab0aa7670948 | -8.06174 | -43.11364 | 2025-07-07 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| aafb7a9b-853a-3cc9-986c-f71bb252638f | -7.27392 | -44.65173 | 2025-07-07 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94261718-867f-39aa-bf55-7a87ceb9af64 | -9.79988 | -47.73991 | 2025-07-07 04:59:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eea78263-8a0c-34c6-8f83-74d8ea1c6224 | -6.1779 | -48.05945 | 2025-07-07 04:59:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| e8b51803-fb59-3105-86a8-9f3f93c09764 | -10.65437 | -44.48575 | 2025-07-07 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d6bf5d8-075a-3074-a296-bcceef0f6277 | -6.1606 | -48.0507 | 2025-07-07 05:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 6c398100-08d2-34f8-b9e1-4a3495ffe5ba | -6.1792 | -48.0494 | 2025-07-07 05:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 780807c9-5316-3ae3-b418-1e5049d0d94f | -14.1324 | -51.3017 | 2025-07-07 05:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 4009d2fe-49e1-3996-8ff8-63560f99e7e8 | -10.36946 | -57.50791 | 2025-07-07 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c27e5ee-7468-32d7-91e0-0cb3b460be4f | -14.62971 | -48.14625 | 2025-07-07 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6bd5daa-541e-3788-a17c-d29f1f68fa9c | -15.80011 | -47.65047 | 2025-07-07 05:01:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0152c351-62d9-3b71-bd4d-cb78ad54be57 | -12.57672 | -56.97288 | 2025-07-07 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9c2eeb9-650f-32b7-9736-c19909480eca | -12.03072 | -57.08286 | 2025-07-07 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d7d379a-7ca6-3029-88e8-296098ad677a | -11.88159 | -58.73573 | 2025-07-07 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 590eea32-8411-3469-84eb-4702b02ac658 | -11.88157 | -58.73696 | 2025-07-07 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 535217c5-de54-3be6-9eef-1a24aee1371d | -12.02852 | -57.0749 | 2025-07-07 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 93fb2411-85a7-3aae-8452-0121f571311f | -10.67129 | -56.54708 | 2025-07-07 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6bdad39b-e695-321f-8266-aa6c83ee60fa | -11.20986 | -55.91485 | 2025-07-07 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03be1721-c031-3440-8b1d-735077a623f2 | -14.13094 | -51.30361 | 2025-07-07 05:01:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 24bd5077-3749-3501-8e01-0e0bdbb76a91 | -12.95476 | -47.1362 | 2025-07-07 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f6207f80-d21e-3c16-a937-dd9c5a5e1efd | -11.8787 | -58.73083 | 2025-07-07 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf9ef919-9f4c-38e7-99d7-5b9aed17c47c | -12.48423 | -49.08588 | 2025-07-07 05:01:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b5a37da-69fa-397b-b6cc-24ccb7c41f47 | -16.67705 | -43.88484 | 2025-07-07 05:01:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70e77310-667e-3945-8172-5d0c5f5a5485 | -10.88886 | -56.45627 | 2025-07-07 05:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74e1b0e3-81b7-36a8-9a10-cc4ebb96aaa2 | -11.87721 | -58.74067 | 2025-07-07 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f97e211-befb-3ab0-a905-e302a021b899 | -12.95446 | -47.13866 | 2025-07-07 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 40454284-5b5f-3762-bdc6-e5d4c8f038a0 | -15.5687 | -47.85376 | 2025-07-07 05:01:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f99c196-3e90-3d6e-88ee-9804f2c27f88 | -12.7502 | -44.41124 | 2025-07-07 05:01:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2f76403-077e-3471-91b4-4fa08fe56f92 | -13.02019 | -46.77089 | 2025-07-07 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 066eeb9e-7903-3c9f-89d1-fde5cbba820d | -12.02393 | -57.08171 | 2025-07-07 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad6e43fc-a095-398f-a47f-01b69b5fd239 | -14.12306 | -51.30246 | 2025-07-07 05:01:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7b078124-84cf-303b-a235-1fc0aec328d8 | -15.68332 | -53.6771 | 2025-07-07 05:01:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c81014d-ed4b-3138-9b86-26e9e90c013b | -13.01601 | -46.76137 | 2025-07-07 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f0adb5a-beac-36aa-b985-f1c45802b270 | -11.87722 | -58.73943 | 2025-07-07 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07b96d73-35ba-3177-8eaa-b2894a3dbab1 | -15.80528 | -47.65086 | 2025-07-07 05:01:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58c22ee8-a191-3778-a5f7-39e1ca9aff0d | -12.57891 | -56.98077 | 2025-07-07 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 928547d7-b0fe-3eeb-930d-e31cb9bd8fa0 | -15.7436 | -47.78017 | 2025-07-07 05:01:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 559ca4de-6e0e-3ef9-8607-9bca64ad517a | -15.7487 | -47.78079 | 2025-07-07 05:01:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 677f16a2-5679-357b-961c-e4fd0cebd88b | -13.51493 | -56.57198 | 2025-07-07 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e68bdf58-7b15-31fd-936b-b156316af0b3 | -16.6836 | -43.88588 | 2025-07-07 05:01:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c0ff7db-4a18-3851-9649-b9389f775de8 | -12.02672 | -57.08598 | 2025-07-07 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ed97903-f0bb-3915-ab66-70ba637f4e65 | -13.02136 | -46.76124 | 2025-07-07 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aed76e0-b2bd-3b3d-8782-04f28045f8fe | -14.9308 | -55.83636 | 2025-07-07 05:01:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce03e622-9a1c-3a27-bce7-0dbf6e5ed692 | -12.5801 | -56.97346 | 2025-07-07 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30e898e7-b44c-3d42-ad8d-09e3f2315ad7 | -15.74539 | -47.78017 | 2025-07-07 05:01:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25a928df-228b-3b37-95ab-0040a7b2d8dc | -12.58069 | -56.96981 | 2025-07-07 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ccfa75a-c947-3cdd-8a35-acf00b810456 | -12.74912 | -44.4144 | 2025-07-07 05:01:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddb44624-ea5b-3991-93be-ff798c49ffee | -14.8919 | -59.54232 | 2025-07-07 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1ff7011-e283-3bd9-9456-92bf1cdd8487 | -14.63273 | -48.14218 | 2025-07-07 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README11.md)
