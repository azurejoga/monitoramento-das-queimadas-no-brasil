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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdb25ed0-4b8e-3e00-aed6-629488b7f64a | -4.33716 | -44.34193 | 2025-11-25 03:46:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4eaac4ce-0788-3396-be04-26fc055dd42f | -4.369 | -46.11031 | 2025-11-25 03:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fdd542c-43e3-3366-b767-627d78c0c94c | -6.81323 | -38.57345 | 2025-11-25 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ebaaaa87-befd-314d-abb2-bcd7c6dc625d | -6.90371 | -39.05987 | 2025-11-25 03:46:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bac68383-015b-3c88-96bd-52f5202e3930 | -6.73154 | -42.93771 | 2025-11-25 03:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6eccaebf-31b4-3671-a899-ec91c1d29c65 | -8.06384 | -43.131 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 68d30849-793a-37a4-a12a-ac48322574b8 | -8.46618 | -40.70118 | 2025-11-25 03:46:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a559d83d-b483-3f61-a46b-c8ac20bd2ee7 | -7.30664 | -45.28157 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5a69730-41dd-3178-9e05-32d9ecb03f42 | -4.67623 | -45.0121 | 2025-11-25 03:46:00 | NOAA-21 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dec6983-dea0-3c2a-bdce-fa613b06b027 | -5.56832 | -44.9724 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| abb626d0-7b37-379e-ae6e-c743f045074c | -5.58047 | -45.16212 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d8c3f66-46ea-3c99-a9c2-d0e60bfa776a | -6.07896 | -39.54546 | 2025-11-25 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a29a030-608a-360b-bb2c-bb2b8793a9b1 | -4.9683 | -43.95668 | 2025-11-25 03:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22a3d669-cd5c-3e09-a7f2-5db6626c488c | -5.63299 | -43.92516 | 2025-11-25 03:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a8fc310-1680-3888-ab8b-2906276c1128 | -6.14442 | -39.77041 | 2025-11-25 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 631d3d45-71d8-3685-90af-adbcf174c65b | -8.06743 | -43.13588 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| abb17cf1-96e3-3127-82e8-d34b727f435f | -8.16181 | -43.19322 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7a1e7058-fa7a-3cca-948f-20a4e73630e7 | -8.05457 | -43.13361 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| e5626aa5-4aad-3f06-b251-16635023f576 | -5.83725 | -42.92606 | 2025-11-25 03:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab56ea8d-7a48-39d6-b61b-664060669356 | -5.58292 | -45.17831 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 824f4cd8-bb43-3093-8e49-0ea0446283b8 | -6.49352 | -38.83577 | 2025-11-25 03:46:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9bd78088-340c-3803-9970-7b5a80385cd4 | -4.93955 | -41.15372 | 2025-11-25 03:46:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3174cbb0-9956-39f0-b847-02651823219b | -9.35455 | -35.54214 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ed0fc37-22c5-3a83-b503-484f25ef754b | -6.46377 | -43.55507 | 2025-11-25 03:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45e709a6-4e7e-3653-ba69-9071a95171ee | -8.33291 | -37.0407 | 2025-11-25 03:46:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4b7774f9-3d19-3c40-a85c-31e3b8db53e1 | -7.6335 | -39.28333 | 2025-11-25 03:46:00 | NOAA-21 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a2464271-04f1-3971-b449-8db3a059d73b | -6.5091 | -38.82652 | 2025-11-25 03:46:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 03a8fca7-df3e-3f9a-8d30-2651aa412222 | -7.56315 | -45.87193 | 2025-11-25 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79375f3a-27e6-3a2d-b26c-2e0af8356e4c | -8.06095 | -43.12207 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 275ca327-cb4f-3da0-99dc-d8752a1a9cec | -5.89693 | -44.52031 | 2025-11-25 03:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e80d8b4-062d-31f6-a4b6-03bf8be3f6ff | -5.31162 | -40.87219 | 2025-11-25 03:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 15b5d60d-0817-3c70-8b01-8159e9ba9c78 | -5.41877 | -43.65636 | 2025-11-25 03:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cbac630f-3f29-3282-95d0-f58666b08045 | -5.31626 | -40.86804 | 2025-11-25 03:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b18d74ca-a8b9-3bc9-8917-b85065678459 | -8.05246 | -43.14597 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2ae894d4-3f82-34ca-ac2f-dc63cc142ac3 | -4.092 | -48.82334 | 2025-11-25 03:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abbda690-1fe3-3b38-977a-0711de0456c0 | -4.5923 | -44.0552 | 2025-11-25 03:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1a38f366-420f-3dc4-b69d-e8aaa8175ba3 | -7.28437 | -45.11577 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f30c8866-bff0-3578-bf27-8a777001f789 | -8.04739 | -43.12396 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7387942e-9e8a-3167-b3b8-92077014ead1 | -8.05666 | -43.12133 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9f02857a-566d-3b17-8b5b-32647753b637 | -4.34995 | -44.32662 | 2025-11-25 03:46:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f380cac0-8e8a-3a6b-a89f-e8b2f4e7f1c8 | -6.68403 | -42.47999 | 2025-11-25 03:46:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 94431765-e2c5-3c65-aa2f-30857650e63d | -5.03876 | -43.25974 | 2025-11-25 03:46:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bda9ab22-3f96-38d7-af3b-49841202de74 | -5.85442 | -42.93309 | 2025-11-25 03:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a36b5a7e-ea98-3762-9173-49b91f717ace | -6.85784 | -39.3689 | 2025-11-25 03:46:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 548f877b-a090-3a88-8fe0-60c00b7de45b | -6.50101 | -38.83302 | 2025-11-25 03:46:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 641aeafa-8be1-3989-8e78-dc97b1cec380 | -8.04459 | -43.14033 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5a7d1e83-4d45-35fe-87f2-e8c89a0f7954 | -8.54227 | -40.21519 | 2025-11-25 03:46:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 132c9386-d0d4-3c59-9cb5-b287d347958f | -8.05745 | -43.14263 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bd411838-e812-37a3-8d31-1bdbeaa2cac5 | -4.59606 | -44.87889 | 2025-11-25 03:46:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2e42bbc-b329-38b0-ae6f-1b8be38f4ff4 | -4.95138 | -42.71057 | 2025-11-25 03:46:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d1962124-5529-3f59-9b54-2581e888bfc7 | -4.81657 | -43.83297 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e8cad7d1-f492-3fed-9783-3500f4823bae | -8.05028 | -43.13287 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 5caf43de-fa44-3fb6-a4ec-373b6e78fb7a | -4.75222 | -45.1055 | 2025-11-25 03:46:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9c233c6-6969-33c4-b1dd-ff473281214d | -7.26697 | -39.66917 | 2025-11-25 03:46:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 105098c5-af8e-3e7a-a9b1-07040749dfd8 | -6.67992 | -42.47877 | 2025-11-25 03:46:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bcd69589-eed8-391c-9a2f-dc5e3aae8cfd | -4.81328 | -43.82927 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 19c86b0c-fb5c-341f-9bfe-d242f18ba27f | -4.74702 | -44.44555 | 2025-11-25 03:46:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ba69c1f-eb9b-3e96-89b8-d816aac53d58 | -5.41411 | -43.65565 | 2025-11-25 03:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31cf20cf-7859-3f0d-8248-65e1f2555d0d | -7.39353 | -39.69361 | 2025-11-25 03:46:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 47831ca4-ba04-3188-9e2f-04da4049828b | -5.31364 | -40.86987 | 2025-11-25 03:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f4b00a79-cb88-3b08-8cbb-9d75f05f3560 | -5.00482 | -41.96959 | 2025-11-25 03:46:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b51c23e8-c29c-3b80-ac48-cdf87f7d7f82 | -5.78692 | -43.03823 | 2025-11-25 03:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 99806288-b2ce-3c1a-a2cf-c79bb98c0c6e | -5.04028 | -42.55157 | 2025-11-25 03:46:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 36e48795-6969-31ac-be97-d30dcd000e8b | -6.07829 | -39.54506 | 2025-11-25 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 312a7e96-0916-3d56-a9dc-c8360062ac00 | -4.82367 | -43.82568 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ffd62a77-efca-3a01-af50-aecf73f99d5a | -6.2811 | -39.6804 | 2025-11-25 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 25b93be6-8fe7-3d0d-a0b8-3a5b7a3b76e9 | -6.68961 | -43.94332 | 2025-11-25 03:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 00177f6d-663f-3526-b1cd-fe6ecb2711e5 | -8.29811 | -40.39933 | 2025-11-25 03:46:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 419d8aa3-7d7a-30ee-b401-36bcd094e524 | -8.04669 | -43.12804 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5a458222-74f9-3c74-b262-ca0e6364afeb | -5.89973 | -44.51869 | 2025-11-25 03:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c7411b5-4e2f-340b-9c8a-33f16c2d5d8d | -6.6601 | -38.9125 | 2025-11-25 03:46:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 919ad8d0-29f8-3a6a-872b-df0e1c17c0a4 | -5.0342 | -43.2591 | 2025-11-25 03:46:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3d9624d3-2586-354b-800a-660f993ffc9f | -6.09405 | -39.44929 | 2025-11-25 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a653a3b1-7e8b-392d-bc5b-43276862d2da | -6.50042 | -38.8367 | 2025-11-25 03:46:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 61f11e16-4cbc-3c58-93a5-e22fbd9c7bf9 | -5.78997 | -35.57055 | 2025-11-25 03:46:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3418c52e-9ffb-37ba-946f-86ef77bf4b88 | -6.75156 | -38.97698 | 2025-11-25 03:46:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6fb13286-12c4-3cba-8cee-235a088edba6 | -8.16612 | -43.19394 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 2ccd0e19-62a6-305f-92cb-2738f55f26de | -5.86675 | -45.27685 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d70dfa4c-5acf-32b9-967a-728aaee035f6 | -4.82455 | -43.82057 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 60fbdeab-0c1f-38ed-ba41-0a41334ea1e0 | -6.07187 | -39.54416 | 2025-11-25 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28aadf53-b2e3-363f-8df3-331d072f0265 | -6.12287 | -42.94901 | 2025-11-25 03:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| c2242eaf-702b-3778-b6a3-7cd36b1e4bd3 | -7.46686 | -45.19294 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e5f6138-6f6c-3516-b117-352a1a7b9ba4 | -6.68399 | -42.47638 | 2025-11-25 03:46:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2ae82976-f6ff-372e-8c9c-6166af203147 | -7.56779 | -45.87604 | 2025-11-25 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f81be4a3-2999-3708-9c1d-617d66c960b5 | -8.04103 | -40.94987 | 2025-11-25 03:46:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 116d86d7-14f2-30e3-bd63-1e7f41f33cf0 | -8.04958 | -43.13697 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 7b5eb8ee-1a4a-3d31-8ba9-7f6a0cfebdf4 | -4.82217 | -43.82863 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4511f6f1-b287-3cc3-bd90-442658ab5784 | -8.04888 | -43.14108 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f56e2526-c22e-3dcc-afdd-c98bd89a89be | -5.11942 | -40.73005 | 2025-11-25 03:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b93e79db-ed87-3714-bac1-006b976813c5 | -5.03797 | -43.2644 | 2025-11-25 03:46:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42ebddea-5a3e-3d5a-ab71-92e8548d9955 | -7.40869 | -39.04145 | 2025-11-25 03:46:00 | NOAA-21 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fd7e2db6-65c9-3281-9779-c117f366ac79 | -5.58238 | -45.18138 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5098a739-6891-3025-89a8-45ba42559796 | -8.06244 | -43.13927 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| c4298bab-8ad6-39e8-a006-28567a8c2e43 | -6.55977 | -39.50907 | 2025-11-25 03:46:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7a1ad11f-e0c9-35e1-b52b-cddc3ddd852c | -6.8078 | -38.2081 | 2025-11-25 03:46:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d2405af5-1a62-3e6a-bafc-da0a85934568 | -8.05387 | -43.13771 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 2f2280de-e21f-3628-bcd5-be6f087a2a90 | -4.82776 | -43.82426 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f55f9623-496a-3cdb-bf88-d283aed9d2ad | -8.06314 | -43.13512 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 9efb8c82-0a63-38e8-b648-155156ba9e60 | -9.354 | -35.54586 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 75266e5a-6789-31e4-bbfe-5ef930b043fa | -8.31564 | -36.42855 | 2025-11-25 03:46:00 | NOAA-21 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
