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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2985d5e7-c11b-3fbf-96ef-2b6557bbf4d6 | -2.73852 | -51.54829 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7068b02-3b55-3b64-bb2b-206dd52624ca | -3.50437 | -53.20113 | 2026-09-23 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7f6b441c-c19c-3172-9cb7-b8e482e2c8a7 | -1.744 | -47.05229 | 2026-09-23 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0a14303-6142-3aaa-bac0-fce3ceeba0be | -4.06672 | -56.22342 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c0e5d0c5-8c0c-3d18-a60f-d739c94dc6b8 | -3.23093 | -46.93951 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0fbcded5-1e53-342d-8ef1-02c35141837c | -7.13404 | -42.06196 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 71e99d27-a3df-31fc-b08d-0c899f8b1fcc | -3.87361 | -52.25888 | 2026-09-23 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cbcbfd5-1f78-3392-ab2e-a5a56a424b19 | -5.24348 | -48.19611 | 2026-09-23 04:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5cdb19e3-1581-337e-aef3-6b3aba369899 | -6.18897 | -45.31748 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac2be90b-b6bd-3447-a359-d01c43a72fb9 | -2.95477 | -54.08616 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43cbfe2a-ad04-3fdc-890c-364a3e54ebb0 | -5.76548 | -52.35639 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbdadd01-645b-33f4-914b-cce78211ca4e | -4.57613 | -45.65134 | 2026-09-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1aa97bc-282e-314b-b4a8-137fc79a4659 | -3.8692 | -52.25821 | 2026-09-23 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a4a2435-4ff1-38ee-9ecc-632f2514ab0a | -6.74275 | -45.45012 | 2026-09-23 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62f82893-c5bd-3499-a44b-0fe724317b74 | -5.17905 | -56.18044 | 2026-09-23 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dd0acfd-cb03-3197-82dc-fe867607fb56 | -4.64593 | -46.31784 | 2026-09-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c93844f-3c7e-3bb2-8565-fb42c6a629d6 | -6.60403 | -45.86626 | 2026-09-23 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa436f12-d3c8-3f91-8dc0-b75211d562e4 | -4.929 | -45.80877 | 2026-09-23 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6105c717-7368-3fbf-882b-a0a4c83bd181 | -2.55023 | -49.10048 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 389b25e4-9b04-3e0d-a66a-3e365605a392 | -3.22398 | -46.94553 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7e7d4841-2e49-3bef-9ab5-f2a84d8a0579 | -3.86745 | -48.97335 | 2026-09-23 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59c1a85c-f159-348f-9dc4-56d76ab51a39 | -5.87777 | -52.07403 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5a0f953-8a2a-347b-bdfe-ce5d079dc0fc | -5.87809 | -52.07449 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb0a9380-d929-3b0f-a4e5-e79d4b8f6487 | 1.44041 | -50.81738 | 2026-09-23 04:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab9f18cf-233a-3c34-a3c7-a49da2c9a40c | -5.83478 | -52.17735 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a12bc2de-88db-3398-be2b-b76ad984af1e | -5.86217 | -46.1072 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cf366df-d65d-3826-85f5-5e27efad5b73 | -3.39406 | -50.43895 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a386a0e5-f2d8-3e42-bcf5-119fd1a2e048 | -3.72528 | -49.04496 | 2026-09-23 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a519fce5-446e-3e40-b9a9-c859fbd76294 | -1.42106 | -50.61275 | 2026-09-23 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8297a49-0b05-36b9-9413-ed29f03c487d | -5.12915 | -46.05555 | 2026-09-23 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f57cbfa1-7582-3c01-b45a-53ea30a71d12 | -5.61939 | -45.23999 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3d44687-80ea-3ec1-9d19-cc9760d61866 | -4.06605 | -56.22737 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8236c634-2d53-3cc4-bdef-e44ddfabf442 | -6.98451 | -42.59528 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f9b44cdb-e8ab-38d9-b55d-ab3cc70fe209 | -5.34541 | -45.16536 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 573ce967-4d6f-3cec-82fb-b389a9508f63 | -4.93381 | -45.80312 | 2026-09-23 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab01cb63-052d-3acb-9f74-d9c1325b9259 | -4.2066 | -56.35121 | 2026-09-23 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2cf230cd-978d-37e0-ba7d-57d7bfeb38f1 | -4.17626 | -53.66189 | 2026-09-23 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 030594fc-2bef-3a84-925e-ec6bab28738e | -7.14329 | -42.08593 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9568a96d-95b0-3deb-aad4-e3b012b16840 | -6.42611 | -43.48618 | 2026-09-23 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16580c08-e7e6-347d-8ebd-d5507b29d6b5 | -5.80132 | -43.91064 | 2026-09-23 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3aabf34e-bbcf-3348-adb0-3412606de6d4 | -5.16755 | -45.43523 | 2026-09-23 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b7510d9-85a8-371f-b161-a9f2275224cd | -3.04335 | -50.26914 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aaf9c536-6af7-354e-998f-67072bac2a67 | -5.79998 | -46.09402 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 40cb3ddf-1a98-39a5-aa7e-56d67ddafca8 | -4.17539 | -53.66717 | 2026-09-23 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d3c687c-7d3a-3803-a517-d894f4fa8941 | -2.25845 | -48.76271 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e79afa96-49ea-3025-8d2c-e8d2d4576121 | -7.03173 | -44.65351 | 2026-09-23 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3ae125f1-cdeb-3b2c-8a2c-4017ca2da926 | -2.95041 | -51.04461 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd9270ab-5c1c-3130-89d5-409e288d613e | -6.88318 | -43.96389 | 2026-09-23 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fce9fba1-1639-333b-9c0d-f1bbcecf0cbf | -2.45282 | -49.21455 | 2026-09-23 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b74edaef-4240-3eb7-9d36-df9dcfc51a5e | -2.86718 | -49.62998 | 2026-09-23 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 039f65f4-640a-3312-a716-720b649e82f8 | -4.33831 | -55.65546 | 2026-09-23 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d99b090e-e77f-3d9e-8b9c-cc12c39300a9 | -5.34874 | -45.16587 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b604bb4a-08e3-3dbf-b57d-00babd3d43f0 | -6.57532 | -44.15075 | 2026-09-23 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 556e6a08-7d83-3038-a4b9-f86c8e204da2 | -5.87721 | -52.13067 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 743bf564-9b62-31c5-81cd-2edf799031c3 | -2.76297 | -57.02994 | 2026-09-23 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c604653-d4ff-3a8f-9042-b5b8fb45c9d3 | -6.27968 | -47.65172 | 2026-09-23 04:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7a7d96d-a35a-3c03-a4fc-a119c9408e74 | -6.74609 | -45.45063 | 2026-09-23 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f8ccbad-fae5-3e66-af05-7315c324a333 | -6.27215 | -47.57375 | 2026-09-23 04:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d81caf93-d555-3fc3-b9ca-f012bcf42c55 | -2.87095 | -49.63055 | 2026-09-23 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e93e9af-2d83-3115-92a9-253df3a66578 | -6.9229 | -42.88579 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3a7e00f5-5ac0-3b89-9bca-e150c029859b | -2.59899 | -47.35173 | 2026-09-23 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0d52158c-aaa3-367a-b711-6d699cad9df2 | -3.44683 | -50.61002 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ecf8c55-de9d-3e96-addd-87eacdbf03d7 | -1.3885 | -49.04613 | 2026-09-23 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f6e1315-c15b-3bf0-a514-28d1fcaad920 | -5.93188 | -46.35859 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 250949dd-8e16-3ee7-b75a-ff89a56afd41 | -3.24323 | -53.9534 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0863b06c-7fc3-38ec-8090-f9a85a2b5f92 | -6.55987 | -44.89493 | 2026-09-23 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96a5884b-0faf-3d81-a5bf-694bac6fc003 | -10.3081 | -50.5095 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bbfc97c3-8494-355e-a95d-08b9714f37f3 | -10.7043 | -48.71785 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6918e2ce-58f7-31eb-8c7b-2615dd00c7c4 | -12.05602 | -50.35505 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 113e7352-4b53-33cb-b7cf-08a1bab64e29 | -12.36846 | -50.15234 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 468ffeb2-cd1d-32b8-97a0-7f2e7b2ef7a6 | -14.63815 | -45.64297 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd30b419-6f28-39c0-8c66-1ddd288a275f | -13.72341 | -48.78206 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 488278f2-d335-3162-821e-96dfaf1b849b | -9.86421 | -48.39433 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3fe5fe9-b17c-3be5-abe5-ffb54e54afcb | -11.6608 | -47.79321 | 2026-09-23 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59f05ecb-0b35-3e73-b17a-73c3f8fc12f5 | -12.53631 | -50.06868 | 2026-09-23 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d0bee9f-321a-3904-88fc-fa7bb9cf69df | -12.71917 | -50.88322 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d50709ae-18ad-34f0-a87a-53481bdd1478 | -13.45371 | -46.25957 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32fc14bd-37cb-3592-b1ca-75bbbd0021ba | -6.89407 | -55.33369 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35060d47-2c90-3ad8-85d3-7708a458c40a | -11.30151 | -51.35099 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9f58488a-e1a3-3033-84c2-c3a4cbe3b3c3 | -14.62741 | -45.63814 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6ace2af5-f704-3a53-afaa-778251b37f2c | -6.30419 | -57.75279 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d5dff29a-8efd-3e81-bafa-34fdcb380033 | -7.59059 | -57.66772 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 104612b8-e2d6-3f8c-a127-adeb356d0646 | -6.68387 | -55.0597 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98681919-2cb5-3074-a63e-da5f0d256479 | -6.04375 | -52.77063 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bf62b73-dbad-3430-849c-b60ba891b62b | -10.53973 | -43.98023 | 2026-09-23 04:27:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1097d997-e47f-38fc-b8f9-16d8f8cb6fde | -13.4296 | -46.2758 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64b5fed9-b5f6-3f09-91f0-fcde013b14e3 | -9.86698 | -48.39845 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23b578a5-bd11-3381-a04e-3487ae88a9be | -11.13083 | -42.78813 | 2026-09-23 04:27:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 06330069-9676-3fce-a1ec-715cf0d82cbc | -8.09553 | -44.42898 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 392d25e1-fcbe-3908-b40d-d7f8958354f1 | -9.97007 | -50.25251 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 385f41a8-a4e4-3227-8b90-cd9b29ebd6c7 | -7.32829 | -55.60083 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63889b36-30d6-3c34-ab2e-5a867507a117 | -8.91014 | -45.94761 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12060cd6-e590-3835-9346-63ff686bdde0 | -10.70982 | -48.72626 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a6b7e0b-6f52-389a-a2e9-6858af7026c1 | -6.67772 | -58.56592 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 46189013-4389-3a81-9a10-f126bc704d66 | -11.52641 | -45.34446 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5390864-8f79-3c0a-8108-23156855f4d6 | -12.02268 | -47.8087 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49c37704-6e2a-3156-8e13-37f436c59448 | -10.25648 | -49.98701 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 569c13f6-539b-38fc-81ab-2bb8bfaec659 | -10.0583 | -52.07486 | 2026-09-23 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f56592f-c617-3135-924f-4eb83c71e502 | -11.35437 | -43.3849 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 41c71ade-3aa1-3d88-9cf7-24668a852b5b | -11.45917 | -46.70174 | 2026-09-23 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README56.md)
