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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff2aeef9-1bed-389b-8dd7-a8f111f464e2 | -16.90762 | -55.79033 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 5e68bbde-73b7-3b2b-bd35-5dee7b513526 | -16.90717 | -55.81478 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3d4b5018-4495-313f-b33e-d7e22ea849dc | -16.90678 | -55.79505 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 836a1755-53af-31a4-9c1a-22e171ad6fa5 | -16.90594 | -55.79978 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 43758769-a4e6-33a2-9f4c-b2d3e45c3fb2 | -16.9051 | -55.80452 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 3f4d25ee-2b62-35df-81c1-1126e4556834 | -16.9047 | -55.78487 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 6d9b00c0-a539-3a33-9d44-ad716a58c68f | -16.90425 | -55.8093 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| e1a6a93c-c479-3775-9807-da513d32c7cd | -16.90385 | -55.7896 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 9c8637e8-5476-3edb-933e-69d055504857 | -16.9034 | -55.81406 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 949031ab-83ef-3bbc-b785-5e6d69bd3b45 | -16.90301 | -55.79432 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| d6f9eb9c-f4ab-369d-b606-e74df1b032a6 | -16.90217 | -55.79905 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| d5b02866-47ac-39a4-a9b1-2eba24b1c177 | -16.90177 | -55.77942 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 50517979-005c-3ab7-b14e-02919b28310f | -16.90132 | -55.8038 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 9b423dc2-1534-38a1-9c14-628ea0a66e4e | -16.90093 | -55.78415 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 8ca93370-9717-39ad-9cf1-93115c4726cf | -16.90047 | -55.80857 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 86b787e2-7541-3ad1-bb9f-4e631d705711 | -16.90009 | -55.78887 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| d2e80d5e-e673-344a-a4ea-2ca083b9fc2d | -16.89962 | -55.81334 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 14baee79-a326-3486-9096-40bd303f6ffe | -16.89924 | -55.79359 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 0bff8526-e118-395d-940e-77e954cd77ea | -16.8984 | -55.79833 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 36497798-0278-3761-b076-5a3e76964422 | -16.89801 | -55.77869 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d47fe096-0fe3-3726-b50b-a410cdb59e15 | -16.89755 | -55.80308 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 9591a810-da08-33c0-8935-abc61ab32ac4 | -16.89716 | -55.78342 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| c28f6d19-7bec-3ffe-a745-9816445290aa | -16.89699 | -55.87201 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 51d132af-21ba-3506-825e-3829d42e4b53 | -16.8967 | -55.80784 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 90d680d8-0159-3596-8a49-ef3c6c0a23e2 | -16.89632 | -55.78814 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| f42570e7-7dce-376b-9de5-3f6a9bd13469 | -16.89613 | -55.8768 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 734a62b9-b1e3-3dee-a813-e45024d61b9b | -16.89585 | -55.8126 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 05fd28ea-ac9c-389f-a26d-c8fc44d2ec20 | -16.89547 | -55.79287 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| aa535cef-7e4f-3f90-a1f4-afeb86d75ffa | -16.89463 | -55.79761 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| f3ed258f-e774-3693-a5b1-b07ab7f36a13 | -16.89424 | -55.77797 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1305ad9e-494f-3f99-b49c-4a9385826b4b | -16.89378 | -55.80236 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 780b819c-ecd6-38d7-947d-d31ea2054e4e | -16.8934 | -55.78269 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e36ab95a-93b8-354d-ba58-1eadbf664b28 | -16.89293 | -55.80712 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 42d139c1-34b4-341e-ba8f-227785304fcd | -16.89255 | -55.78742 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4899d910-db9f-3552-b810-198abf97de10 | -16.89208 | -55.81187 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 318449a6-fabc-3115-9ea1-5b6015031a5d | -16.8917 | -55.79216 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c4638df2-d669-3ca2-bc8a-7cda9d9dbfee | -16.89085 | -55.79689 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c3e9e1e5-cbee-38d2-8cff-8b1b79d6312b | -16.89012 | -56.71879 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a2924f91-2154-382e-a6f2-063639e45f06 | -16.88963 | -55.78197 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 6433152c-4d52-360e-97f4-51b0faebc7c1 | -16.88916 | -56.72412 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6a11d204-616a-3777-9a3f-ff552d991b67 | -16.88916 | -55.8064 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c23d26a6-25d6-3ff0-af36-744794e99223 | -16.88878 | -55.7867 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4d45785f-1a67-3be7-a620-a44caa68881d | -16.88831 | -55.81115 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cd40bcf4-ed40-34f4-ba43-7f951505d3bd | -16.8882 | -56.72946 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 81a9550c-61dd-300d-8b2a-888473916370 | -16.88793 | -55.79144 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 471bd06b-070f-3ee9-8e4c-f9ffaf31584c | -16.88745 | -55.8159 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 36e4f565-602f-3d08-80e8-7e455d6699b8 | -16.88724 | -56.73478 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 4f71ca14-92a3-34c9-9401-4855959726cb | -16.88708 | -55.79618 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9352a787-76a2-3c81-945e-5c9a47463f8b | -16.88671 | -55.77652 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5b3b67c0-b27b-30f5-8206-c36b64c265e8 | -16.88623 | -55.80093 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b8c1884a-5cbb-3966-aaaf-2c4a9d134447 | -16.88586 | -55.78125 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4b7cd552-9f8c-3a4f-933d-ca9bcc37e565 | -16.88519 | -56.72333 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e2e49f5c-4a7d-3c24-a7f3-a2907365a9e2 | -16.88501 | -55.78598 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e3826621-1136-396c-bfd6-7a81b6082010 | -16.88453 | -55.81042 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 64ce9c31-84e2-349a-9c2a-f65272a20533 | -16.88423 | -56.72866 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 536e0623-09b7-363f-b17f-afd242736864 | -16.88416 | -55.79072 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 384eb35c-6f8b-38ed-b13a-2a0c2c791174 | -16.88368 | -55.81517 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ed8acfcc-25f8-3ad8-835d-24ed1dcdf30a | -16.88326 | -56.73399 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| b7bc4f86-640d-362c-847e-eae7c3e8dccc | -16.88121 | -56.72252 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 590d792d-e617-3def-9007-a27a95375638 | -16.88048 | -55.89858 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e7625632-25a0-3423-b80b-7af276a80176 | -16.88025 | -56.72785 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fcbb0d13-5cfa-3312-bedd-9a41fff9e2ca | -16.87954 | -55.79473 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3e732903-b516-3249-80b7-efba87895e2a | -16.87928 | -56.7332 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 598ae6f6-8573-3f73-b490-e1db36b0d4b9 | -16.87869 | -55.79947 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a424dc57-99e7-306c-8002-34fcd60ec8d2 | -16.87832 | -56.73855 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 68b6696a-1888-3916-b8f6-b77a29e21324 | -16.8782 | -56.7164 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3548068c-039b-3815-848a-c57a0991f019 | -16.87729 | -57.80719 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dc2daa90-0da8-303a-98c8-98368b026be0 | -16.87724 | -56.72173 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ce0dd06a-98c3-34f0-8c28-3c0b665ae152 | -16.87711 | -56.69965 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5e6d67e8-ce04-32ee-8756-fcf77f4e44dd | -16.87627 | -56.72706 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e59ed423-76c5-3286-8a63-cce1e7e63af6 | -16.87615 | -56.70496 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5b3eb36b-a8a6-3575-9572-38d04535ea3b | -16.8753 | -56.73241 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8ef18634-a47a-3477-9728-5459455821a5 | -16.87519 | -56.71028 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bdf0d8bb-1cc0-3669-84c7-bf8bdfc05fb9 | -16.87434 | -56.73776 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6957647c-ac94-3b65-9b1d-1330a960c59c | -16.87423 | -56.71561 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 74bc6b1c-b527-3225-8584-2aa408706d84 | -16.87314 | -56.69886 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 47ec0e83-f603-30dd-a615-010b2da8e7ab | -16.8729 | -55.89711 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 23872312-1a2e-3192-b8a6-74491d9b05f2 | -16.87229 | -56.72628 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 16c3cab1-c5ca-37ef-8bbe-00c5e76f19d1 | -16.87132 | -56.73162 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 14b4a99d-7e9a-32af-9261-3aa791df80d7 | -16.87122 | -56.70949 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 80a944f8-9b01-3f8e-b1f1-bd3a196baf00 | -16.87012 | -55.95643 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e97bb5e0-8730-3db2-a4ed-b40dd9739228 | -16.86926 | -55.96127 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d88d4369-7e58-3eba-a60e-9403e034bb2e | -16.86841 | -56.74769 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a3e76a1b-2f1d-3720-ace2-eb0225573bba | -16.86735 | -56.73083 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 06dac9c1-ced9-396b-aaf6-00d3f3718a29 | -16.86632 | -55.95569 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c1efc567-6a63-3a74-8606-a0b109b7e298 | -16.8654 | -56.74154 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8a1865e2-8efc-3dd0-ad4e-23dfe4f97289 | -16.86443 | -56.74689 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 68d4e5bf-f6de-3492-926b-cd6a46086140 | -16.86292 | -55.86542 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6beafff4-0f09-3c5a-98d9-742557988041 | -16.86142 | -56.74074 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 46a3c22d-a722-3bb7-9b23-1c2c0d8df078 | -16.86045 | -56.7461 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3b4d7d99-6195-3342-9355-ef83f119f59b | -16.86032 | -55.8798 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b7cd3a5a-94d5-3a7b-95e0-c43309a4ea5f | -16.85999 | -55.85991 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1287a1d2-48d0-37f3-8551-a09c17f87be9 | -16.85946 | -55.88459 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f8cdd62b-a540-33ba-ab8e-afce0027c955 | -16.85913 | -55.86469 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e7ba2e28-6006-376b-93ff-64d988b16811 | -16.85696 | -57.44886 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c59957bd-3049-3404-83cd-14b8389c6de5 | -16.85647 | -56.74531 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 38adae71-0b29-3a8e-a0c7-13a4b2051f7c | -16.85623 | -57.4528 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f533b99a-16c8-31bf-9ac5-6f79999822ae | -16.85551 | -57.45674 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d2145bec-00f9-3a55-9426-41d2fdb7f812 | -16.85369 | -57.81522 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a90979f0-a015-3816-99e4-ffacdd08eb29 | -16.8528 | -57.44802 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README138.md)
