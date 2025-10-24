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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 153517a9-0dee-3b83-b3bd-578a7ea72de5 | -9.13021 | -50.77482 | 2025-10-24 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b59cfa9f-5fd1-35ba-b0ce-135d3a33ae7e | -11.0576 | -45.39934 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6a70e7bc-d485-30ca-a43f-f3a7a88f5576 | -4.27695 | -40.70353 | 2025-10-24 04:38:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4ef4194c-b575-365e-a512-c46634011561 | -5.45331 | -45.41083 | 2025-10-24 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| e59e07f6-5d62-310f-978f-9b9ea4570ad7 | -5.81728 | -46.21795 | 2025-10-24 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bacdbf3f-be54-3e91-b96d-f04aeba7eabb | -8.17149 | -47.76236 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8111ff11-9a1b-3f7b-9616-8c13e517cb66 | -5.62576 | -50.01176 | 2025-10-24 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67cf6d2a-a35f-3a19-bfbf-acd09eb2b4bb | -7.07523 | -44.49427 | 2025-10-24 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ed1574a-52ff-36d3-87b2-7cfed49cde4d | -6.29748 | -40.87453 | 2025-10-24 04:38:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c3b18291-e671-35d7-856d-d17ef6623357 | -3.8495 | -48.15865 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc0a2925-2fd1-3031-b90d-4701c769e17d | -7.97513 | -47.24029 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 851bff75-556a-33d9-86b6-f5bfa98bfb0f | -8.32862 | -46.24599 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 35af5979-ecfc-3230-ae4a-d869867126c6 | -2.80038 | -49.14416 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d41c4872-f8f5-3927-ae73-dbd8e2d1ba5f | -9.87034 | -47.72527 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb0b5a25-c4a8-3c2c-bf2e-186bd4e2ae6f | -10.01837 | -47.06779 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c008c49b-15c4-3350-b28b-de1b0da9503f | -9.24515 | -45.58972 | 2025-10-24 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09642693-af4f-3c08-a794-86e9ab83b6f8 | -7.99255 | -47.39558 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a66f3432-bed1-3a77-9ff1-94259732f90c | -9.23197 | -51.84121 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81d670da-4592-3ed0-8ce1-75c3b10fc4d8 | -6.8028 | -42.39437 | 2025-10-24 04:38:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8f1ca6a0-84dd-3054-9ae1-f52eb51cc8e7 | -2.85782 | -50.73693 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a259ca96-e095-3186-9fd0-552550c9dc71 | -6.30191 | -41.88993 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eeb80956-1f1b-33a0-bfb9-9613fc5982a0 | -9.36603 | -50.80967 | 2025-10-24 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0af4a4b6-a60e-3090-94cb-b110089697f9 | -2.87178 | -50.71584 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c493d5b1-dac3-30ff-872c-bbe25711434c | -3.76604 | -48.92505 | 2025-10-24 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ecbfa83-6294-3eef-94ef-1c9b838ccc46 | -9.55331 | -46.70041 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c580ab4-b0b1-3f82-bf30-b7479d12f9d4 | -7.62663 | -41.85257 | 2025-10-24 04:38:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a3c6d864-8f75-3b5e-a642-36b4f8a8994a | -3.21475 | -46.80962 | 2025-10-24 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac28811f-5a66-342b-b93d-41c46dd6dace | -3.98624 | -50.51833 | 2025-10-24 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e2d4152-7e8d-3d04-b875-3517c86dc319 | -6.42692 | -45.67225 | 2025-10-24 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 329e68df-af9a-35c8-885a-e924fa80a187 | -5.45703 | -45.41134 | 2025-10-24 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b3a03943-fba1-3159-b2e7-515f7e071a5f | -6.11771 | -41.74854 | 2025-10-24 04:38:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b83cea35-ec45-3af5-9208-9305f1c8ceb4 | -8.24216 | -47.17855 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adbcf52e-080c-3275-a4d9-1d329159bfc5 | -7.3726 | -47.02519 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cfa0b37-6daf-3935-960c-44836a9b87e4 | -9.64107 | -46.88838 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 137c7793-2235-365d-a036-6cccde937806 | -5.74487 | -51.08059 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d79cf66-9d15-3132-81c9-a7f47b7d323b | -7.07349 | -41.66191 | 2025-10-24 04:38:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ab89048-2214-3068-bca9-2b4830de2c60 | -10.42221 | -49.36734 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5fa36b6-f835-3c83-8e39-1437bded60db | -5.6019 | -48.66004 | 2025-10-24 04:38:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dab41539-56d6-323f-ad2c-c4b730a1f1a8 | -6.94563 | -44.02538 | 2025-10-24 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 323b1e7f-e8e5-35f5-b52c-27a7699c44f9 | -5.28941 | -50.57022 | 2025-10-24 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37d420ae-7c87-3669-9e40-53851c79e0bc | -9.27807 | -46.96906 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7de513e-9e8e-3ddb-b140-c7308a333364 | -4.14127 | -47.66037 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee593705-1435-3131-a824-99b518b78bed | -8.41546 | -45.66577 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51622d57-d90a-3abd-a85e-3271eb869259 | -9.51226 | -46.80205 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b154bbbc-1a5e-3b5e-93a5-ddb305003b72 | -6.88493 | -43.62211 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09abf317-047a-3282-83b6-900e34e447e2 | -9.97646 | -47.73993 | 2025-10-24 04:38:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0fee1c9-ceec-3c2f-9223-cbdafbf5fa0f | -3.14221 | -50.6222 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 27f3575d-69c7-3429-b9ef-101f9a8f1727 | -2.81252 | -49.13129 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c739dc9-63dd-3cc0-bfdd-0941cdc7c303 | -9.23382 | -51.82999 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94d12d2d-74a8-3d32-8aee-65747e3e6130 | -11.16723 | -44.69004 | 2025-10-24 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 507823e9-f790-33a3-ae60-2713d6606157 | -8.08964 | -46.9183 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ad31196-6104-3686-bcaf-f4e9ccce4855 | -6.09952 | -47.00072 | 2025-10-24 04:38:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cbbfe47-7602-3a3d-b689-05736d4f9ab6 | -4.54158 | -46.86222 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ddb884d-d361-3ebb-b933-ed4d45443fe7 | -3.84895 | -48.16211 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fb52c81-d5dc-3d62-809f-19c841013976 | -8.20497 | -46.99173 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1723dbae-d2cc-357c-900e-b794a021b9e6 | -3.02648 | -49.49678 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 170c0d73-4ce3-3de5-8979-05e43014c4ef | -4.2428 | -48.55249 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b10f9859-6a11-3975-a229-f204bc98d83b | -4.28659 | -40.70716 | 2025-10-24 04:38:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c70a0a0f-e3c7-3e9e-85e2-c1da41923857 | -2.57461 | -54.01274 | 2025-10-24 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02f3f1da-5b0e-32d7-b693-65c21c9b1dd3 | -9.24131 | -45.58906 | 2025-10-24 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7703d076-3183-3f64-ba98-f854702f9e26 | -6.22149 | -48.84627 | 2025-10-24 04:38:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 447dfa10-1ef3-34b2-bfd3-e4355fd0fed4 | -7.32352 | -45.28337 | 2025-10-24 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf86980e-4760-3034-99e3-c4eb018f58f9 | -4.46216 | -43.23569 | 2025-10-24 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7e7347ef-05ef-34ac-81e8-7e1ae891b398 | -10.03928 | -47.07513 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17d0e73c-a558-398f-b053-a9ae375e689b | -3.47013 | -52.98742 | 2025-10-24 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b415a84c-02cb-3946-92c2-03d77f0bd5ba | -7.78464 | -45.40946 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62773f84-d745-32ae-b5cb-e0eb9e020abc | -2.634 | -51.89146 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4286e06-c447-3bd5-b7f1-f7b5cf499f85 | -11.09628 | -41.61863 | 2025-10-24 04:38:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5421aa20-00e0-3820-9480-54e6ebd13189 | -10.27478 | -47.88341 | 2025-10-24 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4397a6d-9f20-3732-869f-050f241991ff | -7.44069 | -46.88289 | 2025-10-24 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb6f05b1-4298-3276-b7b0-381bed0b1b35 | -10.42554 | -49.36787 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de396d6c-e65c-3a46-a216-dfd3518d381b | -5.02237 | -47.15083 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef994270-24bf-3e9b-a983-2b27d3900657 | -5.12459 | -50.61824 | 2025-10-24 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b63fc224-9787-3e2f-9941-891062b397ec | -10.88984 | -46.04435 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c903a3b-9f55-34ae-8f52-c8b6a8af1e2c | -5.88679 | -46.2814 | 2025-10-24 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52c65df9-0f1b-39a9-abb0-b40b867528f4 | -3.82431 | -47.47754 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5655cbb7-7228-39e4-9cdb-a429a21f9bed | -3.70417 | -47.65409 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b974869-aa58-3caf-aaed-593f4e871411 | -2.80811 | -49.13768 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd53abaa-2521-35e8-a1cb-f08a3a126f5d | -4.79746 | -42.75361 | 2025-10-24 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 490ea39b-7ee6-3850-91a7-29fd0ed20ae0 | -7.85119 | -49.65081 | 2025-10-24 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1a1ee67-adb6-3e1b-9f8b-da51f1cb6721 | -8.35001 | -46.17886 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef115d43-5616-3b5b-96f0-5e60ec9426ea | -8.32797 | -46.25032 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9a40bde4-ca71-33ac-b572-cdf0c727f359 | -7.5519 | -47.36965 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 68752661-f9a6-3c6e-905a-35d7a49bf208 | -7.82852 | -45.37764 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 504addf0-0e66-3484-97af-9e85174e082a | -8.12001 | -47.38677 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b6e7ad5-1954-381d-8461-a8a2a8e3018f | -9.63258 | -46.89586 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4d00805f-98f0-32d2-8a8f-87e7a3d5980f | -3.98284 | -50.51779 | 2025-10-24 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52b935ea-f807-33b1-afaa-b7fe019b930b | -5.62191 | -46.43116 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb3e08af-6741-3215-8045-529a6df8dd38 | -10.11682 | -47.74113 | 2025-10-24 04:38:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abd08252-f928-3484-b209-27c0a0596126 | -8.11705 | -55.08629 | 2025-10-24 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb926ebd-6dfc-3c0b-bf9c-776f6bbcceb9 | -3.15119 | -50.16849 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e90f798-83ca-3929-98a1-e617770a5b94 | -8.16807 | -47.76183 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ad94742-1443-38a3-ace8-79674374d70a | -3.76549 | -48.92849 | 2025-10-24 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bcfcefc-23b8-3286-af08-9fc2e2c9563d | -7.07472 | -44.49771 | 2025-10-24 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fdec9f4-0ffa-3e44-acf8-d8b21b963c2f | -10.0117 | -47.08806 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e6274f40-928d-31fe-9954-a70abf6566a4 | -6.31246 | -41.85732 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c39ad012-c1f4-3fc3-8912-139a2a02c39c | -4.91776 | -47.32545 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bf8a384-0478-3ee6-9123-10326d86e3ac | -8.82556 | -45.41847 | 2025-10-24 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 648accc6-9ac3-357e-929e-dd0f3b945959 | -3.55143 | -49.44374 | 2025-10-24 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 656f74d4-ccbd-3f1d-9cfd-369bab9262f6 | -9.85788 | -48.27475 | 2025-10-24 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README40.md)
