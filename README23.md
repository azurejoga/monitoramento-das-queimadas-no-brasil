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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b40b96e-3f47-3a37-a1ff-2c00b35e0a7f | -3.01208 | -51.34309 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd18c162-e8ee-3d8d-9f15-3c42b7ed7b8a | -3.81259 | -47.4959 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff589c4e-87a3-314e-ba4f-4d4e872d8867 | -6.92664 | -45.34917 | 2025-11-18 04:21:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 944483ec-ea8e-3aa9-9730-e22820ed9358 | -3.14828 | -51.32073 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2680777-5551-349f-bc15-9899b1c08c57 | -8.29332 | -44.00169 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e176b7c-ecca-3ce2-99f4-c5b974e03493 | -4.18837 | -44.24125 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74044d91-0209-3e8c-aeda-535430e049d8 | -5.39901 | -44.4645 | 2025-11-18 04:21:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56976ed4-ce69-35aa-a7d8-fcbf6293cca1 | -4.91665 | -44.04665 | 2025-11-18 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 717c6692-93b1-3d28-9ece-03e4b649cf56 | -4.97638 | -41.85668 | 2025-11-18 04:21:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dc36f7d3-7c0b-37bb-b1bc-fec17b0f39cb | -3.84994 | -51.06005 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73a3c84f-9dd9-3ea6-982c-241889262e59 | -7.70777 | -42.93684 | 2025-11-18 04:21:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d2a8292a-f736-36af-9a75-59569431a38d | -11.06064 | -45.23445 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b0ea1ff-55dd-3403-b5d4-bc8f2e39d90c | -4.71065 | -48.3195 | 2025-11-18 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f041d70-c2a5-31b6-9a95-32f7aa51c73e | -6.40542 | -42.32397 | 2025-11-18 04:21:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b157d08c-c325-36d4-ab53-a8e69637e812 | -9.00134 | -48.42955 | 2025-11-18 04:21:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a52f16b-8718-3fe1-9702-703a4f6a35cd | -6.20322 | -46.883 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad37a0da-5262-3675-943a-8b2373db1d0f | -9.5152 | -45.11239 | 2025-11-18 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26edb998-4c8c-314a-bfe4-52169138a8e3 | -6.80757 | -39.20365 | 2025-11-18 04:21:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6990d6a8-670e-3ee8-8014-d60edfaf360d | -4.18945 | -44.23437 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18fb72b2-440a-34de-86ab-1a5467026d26 | -8.66919 | -45.45359 | 2025-11-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bef621b2-22c6-3acf-98fe-ab3a3025e8da | -9.39112 | -48.45233 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 789d0cc6-011a-3d96-8521-1ec6df6c35de | -3.46905 | -50.24192 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79ab84a9-ec6f-360d-8af0-4574f33099e0 | -3.15048 | -51.48686 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4aaab14c-594c-33b1-8853-0e95f0c4676f | -5.69867 | -45.98463 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8d69da4-2349-368b-9b8a-9cd451d3b6de | -4.04298 | -50.48742 | 2025-11-18 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cf792d2-f0cb-3e67-8c9d-d7325ef1869b | -10.58817 | -45.10123 | 2025-11-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1408cedc-d9c9-3115-9e12-a0128fb0c74b | -8.40785 | -44.03045 | 2025-11-18 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ad0ea4f-8080-319e-8a63-716401d3f7ce | -4.19275 | -44.23488 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f33a2e69-93cb-3b2e-a819-3866d4e3491a | -7.87848 | -42.87493 | 2025-11-18 04:21:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4c08b04f-af08-3f69-8893-a6ab2b72f89a | -4.77507 | -44.92543 | 2025-11-18 04:21:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e9351c0-7962-348f-9827-cd595714454d | -8.29999 | -44.00279 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36924ed3-11d2-3fa9-8871-33dd5719dd5c | -4.60392 | -45.95419 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4fc7584-21f5-3035-913f-e2e0d3a6dbb3 | -10.59089 | -49.00734 | 2025-11-18 04:21:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 516b8ca5-f96d-30e4-978f-35b1b86d3810 | -3.26017 | -49.56985 | 2025-11-18 04:21:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a75bb899-c621-3ac3-99e4-878c64d03c7b | -8.60973 | -50.07372 | 2025-11-18 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5adbb0c2-3180-3af0-9db1-acec64f2ce51 | -10.52116 | -43.96593 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| da15fdd7-e6e4-3856-84b2-ad94ec59a3c6 | -5.40365 | -44.06306 | 2025-11-18 04:21:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8be3803f-63d0-3b04-adba-0d7360a6b735 | -6.02474 | -44.22472 | 2025-11-18 04:21:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cd99c93-03d9-31f9-8769-34052f30392a | -6.74305 | -43.76041 | 2025-11-18 04:21:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e45ac37c-257b-3d0a-80f8-25ba3e3977e6 | -3.23715 | -50.49436 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9245126c-c957-3331-b09e-362f063dc0b2 | -6.72441 | -46.31417 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da238883-8fac-36aa-b84b-8726f0a425e4 | -10.84973 | -44.88376 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e9128904-fd28-3190-b87d-04f46fec460a | -9.97161 | -44.78049 | 2025-11-18 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 359f1145-42f0-3fc9-9d40-60a8291b249c | -10.05288 | -54.32344 | 2025-11-18 04:21:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c9bdd8d-518f-3595-8da9-88ab71b580e6 | -9.06128 | -45.42806 | 2025-11-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 635534cc-f95d-3ed0-8b45-107aeff6ff26 | -6.3794 | -39.51426 | 2025-11-18 04:21:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0a922809-7959-373f-a715-018c5917e9d7 | -6.72382 | -46.31781 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0b2cf75-24cc-3b71-98fb-16aadb38b2a9 | -3.18164 | -50.65295 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9579d5a2-1a6d-3280-862b-79b6bbc227c3 | -4.01215 | -46.13913 | 2025-11-18 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bf7e8be-d3fa-3387-b96e-4ee9321356db | -7.8607 | -46.86944 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b6d8c84-878f-3911-b272-be32996a57b9 | -7.33366 | -46.17074 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8c3ecf7a-9722-342f-a421-4e458b089032 | -7.45733 | -46.84328 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2233e3cc-4a14-31bb-be92-6bb6d6605e04 | -8.22579 | -48.30106 | 2025-11-18 04:21:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1495cd2f-fc58-3f38-8683-6e30826f163f | -3.04938 | -51.14626 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5981e7f-cb95-3181-8516-8c46693619e5 | -7.62825 | -42.58569 | 2025-11-18 04:21:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a413110d-43b9-32f3-a7d6-c476095a83f6 | -4.46613 | -41.80149 | 2025-11-18 04:21:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 740747f7-a896-3a94-8d4f-a152ec13f68c | -4.19006 | -45.61403 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2cb7f0ad-9bd8-377f-a044-fe0a0a1de718 | -3.18689 | -50.6492 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9268e4b7-49b9-31c5-8264-dfe2c6d11430 | -4.9758 | -41.86051 | 2025-11-18 04:21:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a8ae145f-a743-3a1e-a076-15c9bbea3282 | -5.14928 | -47.24929 | 2025-11-18 04:21:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12b5cfb3-e450-3359-b1f0-498d3ee20562 | -3.51679 | -50.28011 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 657c50fe-be94-3537-b8d9-9f01ca3227b7 | -10.87685 | -49.54694 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03394da0-8769-3ad9-9387-d063c35febb9 | -6.19578 | -49.5407 | 2025-11-18 04:21:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d5595cc-ea33-3d81-941b-3bc8574b488b | -10.85792 | -44.09972 | 2025-11-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 02b92427-ac78-37a4-b367-8101e615f016 | -5.8727 | -35.42141 | 2025-11-18 04:21:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 395c692d-c126-32c2-9868-fb6ab201008c | -6.30336 | -43.78914 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| be601960-73ce-3ece-85c7-d31ad18a0392 | -9.57814 | -47.3721 | 2025-11-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfd3f70b-3c84-38e5-ab6d-9f069d6bda0e | -6.84413 | -46.26938 | 2025-11-18 04:21:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c7078a6-0073-3625-8ddd-97b50238ef56 | -6.43683 | -47.04922 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99df2fa0-1a5e-30f7-9da7-224e062ebfe3 | -3.21349 | -50.92154 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f25c82a-b591-3f36-969b-0a33de9974af | -7.57158 | -45.61707 | 2025-11-18 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66c78303-cf80-3993-8151-008ad47badcf | -3.23643 | -50.49872 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5666ec64-a27d-364b-9825-39324682272b | -7.43302 | -48.94033 | 2025-11-18 04:21:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c502a3fd-58e1-370e-a78a-0c99d2b66688 | -4.19167 | -44.24176 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7353f99-56b0-3185-bb0e-e40d63d57a8a | -5.7431 | -46.29456 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 221f6ba0-1a55-3210-8bf4-96e813161f0f | -5.03632 | -46.82423 | 2025-11-18 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0f1f709f-010f-3fb3-bd72-18fb6afffbc9 | -5.65665 | -45.97802 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d535a6fb-9a3a-3007-9fc0-806a13f8989d | -11.2129 | -47.92693 | 2025-11-18 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dc56bb8-14a6-312f-a31d-42cc3d4246d9 | -5.08942 | -41.4707 | 2025-11-18 04:21:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 445b1782-84a1-3f19-9ef9-395ac36d219f | -10.51945 | -43.95443 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29bdcbb6-bbd6-3545-b02f-422e1adfd075 | -10.73665 | -41.36514 | 2025-11-18 04:21:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4550afd8-805e-325d-9232-cfe1e1959464 | -8.46938 | -47.98573 | 2025-11-18 04:21:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7ac8c85-8c80-3b9f-9b4e-5d97b2945c34 | -3.24814 | -51.03083 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e9995f5-0561-3c1e-9450-f2d16aab257f | -4.18338 | -44.22991 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d9bb4dc3-d347-36ad-88eb-1609cd510afa | -11.42669 | -43.32953 | 2025-11-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc70327b-f023-3054-be2a-809a42a3d229 | -6.55008 | -46.63043 | 2025-11-18 04:21:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34183e25-9e2e-312a-819d-ba3c3db7ca51 | -8.66864 | -45.45707 | 2025-11-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0c4cd09-37d7-38d8-9c80-b673c8e14be9 | -7.30705 | -45.76163 | 2025-11-18 04:21:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de4c12c8-ff75-3787-892b-8ab7d78eb7ec | -4.60319 | -45.95361 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e936b957-85ba-3cc9-a91a-13125b6ddcdd | -6.67858 | -40.90358 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6f0a4a73-cb68-369c-85f1-f8ed1510e07a | -6.71491 | -40.79732 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 00235356-21ef-3420-be8c-c142b3efb967 | -7.69559 | -46.84696 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39c58494-16d2-39ed-b351-a887aff4a6cd | -3.23944 | -50.50827 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f34588e9-ada6-38c1-8f71-fd9626a0bbc0 | -4.44462 | -47.99613 | 2025-11-18 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92809c48-3f44-36f5-b439-70f3788ac71e | -3.66778 | -50.21236 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e5327280-5f10-320a-bf85-8f4676b4d9aa | -7.42953 | -45.20144 | 2025-11-18 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d0fcad4-2a2b-3885-88a1-dd3177d86ed0 | -6.359 | -41.79079 | 2025-11-18 04:21:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 11a42af3-bb46-3662-9c9c-f4f115750f18 | -3.32822 | -51.51315 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea6e307b-6f69-3580-a2bf-fcdfe1da6823 | -3.81191 | -47.50015 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70a449bb-6798-375b-b588-3756f638247f | -4.64345 | -47.94672 | 2025-11-18 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |


[Clique aqui para ver as próximas entradas](README24.md)
