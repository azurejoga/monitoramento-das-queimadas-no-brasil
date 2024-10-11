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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ae512e0-201c-33cf-a64f-9d6d4e39f289 | -9.62182 | -48.99166 | 2024-10-11 05:18:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71da257e-d93a-317a-8d8e-caa35e548634 | -11.5288 | -49.8291 | 2024-10-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e19c8bad-2a50-30a8-9c64-9e3ff2d8ca7a | -6.33211 | -51.21767 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfa5fd3f-6c0a-348f-bccd-c3bc27f4f660 | -6.12686 | -51.1472 | 2024-10-11 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c95d210b-378d-3525-a341-dff413e0ad21 | -6.12619 | -51.15184 | 2024-10-11 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d697161-b0a4-3a1d-b578-61eea45fcbe4 | -6.10388 | -51.10009 | 2024-10-11 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a63d7d70-d324-39c8-9a84-1d08fa9485d8 | -6.09904 | -51.0993 | 2024-10-11 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 633a06f7-837b-364f-a6d4-9a535413b800 | -6.09487 | -51.09371 | 2024-10-11 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4479c927-bb82-3a49-877d-1d00874a7d7f | -6.09421 | -51.09839 | 2024-10-11 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0dd502b0-3872-32a6-a4ea-7d71856e9ccc | -6.32439 | -49.98846 | 2024-10-11 05:18:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d26ffda6-837f-317e-9845-ed668af920bb | -6.3243 | -49.98799 | 2024-10-11 05:18:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9027f29-09ec-3dd8-9e60-a3a0f4114779 | -6.31921 | -49.98717 | 2024-10-11 05:18:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e990bec-5424-35eb-b3b8-7112d1ff9fbb | -6.31911 | -49.98663 | 2024-10-11 05:18:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1cd5647-a5a1-3429-8595-ceb50d4b8b4d | -6.31287 | -49.99392 | 2024-10-11 05:18:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a39c19d5-3cb9-3c2c-993c-83cdb40c6bde | -6.3125 | -49.99656 | 2024-10-11 05:18:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a21052e8-fb4a-32b5-9017-ee36be31aade | -6.31245 | -49.99612 | 2024-10-11 05:18:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 55479922-e674-37d3-b35e-e1ba1b0d6541 | -6.20499 | -50.89554 | 2024-10-11 05:18:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45801e97-b53a-38d3-a9d1-3e0f62370052 | -6.20006 | -50.89475 | 2024-10-11 05:18:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7ef8d99-4803-37b6-aa58-0ab5d7313973 | -5.94195 | -51.00564 | 2024-10-11 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6eb83413-db67-30cb-a0fc-5276751fb040 | -7.84588 | -50.18674 | 2024-10-11 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b69f35ea-a456-3335-a1b9-540e0d447822 | -7.682 | -50.25111 | 2024-10-11 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85c34cc5-472a-3cd1-841b-f13ada37847d | -7.68169 | -50.25182 | 2024-10-11 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b3340b8-2846-3ff9-8207-704728f2e890 | -7.67675 | -50.25026 | 2024-10-11 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d5bc178-b75e-3c10-b2be-9516dfdc9977 | -7.67644 | -50.25095 | 2024-10-11 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 098f75d2-b612-3537-8329-d89d3456dea7 | -7.17987 | -50.76576 | 2024-10-11 05:18:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34af0d62-293f-3a2f-8675-9e865260e922 | -7.17916 | -50.76528 | 2024-10-11 05:18:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9e72b3b-bf11-3478-8cb3-e46e0f2ee985 | -7.1749 | -50.76448 | 2024-10-11 05:18:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70cbcd91-f3d5-32dd-954d-5280c14a420a | -7.17335 | -50.73907 | 2024-10-11 05:18:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4c4b458-c23b-31ad-bdd3-d8a30abd3c1a | -7.17298 | -50.7417 | 2024-10-11 05:18:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d59a39c-d8bf-325f-941b-659815503de0 | -7.17261 | -50.74429 | 2024-10-11 05:18:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27d176b4-8642-36bb-850c-fe740c99d279 | -7.17209 | -50.74122 | 2024-10-11 05:18:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 90bdfea3-262f-36d7-8be7-627469490741 | -7.17174 | -50.7438 | 2024-10-11 05:18:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0cc5c37-4cb8-3aab-bada-2e79670673dd | -9.38246 | -50.75363 | 2024-10-11 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05c1e07e-5793-339e-aa7f-40102a8dca5f | -9.1973 | -51.5267 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c5fa0bc7-001c-340b-a8c4-ad44cc563981 | -9.1821 | -51.49019 | 2024-10-11 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3442c02-633d-3ac0-b385-7ea8a3c60365 | -9.18136 | -51.49567 | 2024-10-11 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff0075ad-cd15-3fc2-8081-2017f46c6756 | -9.17642 | -51.49488 | 2024-10-11 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 14392b51-3f14-3112-88fe-e6b4310c60ab | -9.14051 | -51.30577 | 2024-10-11 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d1cbeb7-faee-38fe-937e-cc4481b61239 | -9.10647 | -51.29345 | 2024-10-11 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e28d1d98-3bcf-30fc-930a-40cf16ad2dc8 | -8.73692 | -50.77313 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e1072d2-e4b2-3ee4-8f5d-38d3b5b9308b | -8.57105 | -50.53122 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16ef0962-e32a-362a-abab-4de81183758c | -8.56625 | -50.52724 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 120d336a-ac6c-3999-b073-267b4d94c90c | -8.56581 | -50.53051 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 631c4565-cdf9-3cef-9c8e-d85739c3c258 | -8.49315 | -50.79715 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a98c120a-2d98-3709-ac9e-f7cbbbfa6fb0 | -8.49273 | -50.80031 | 2024-10-11 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b3e976e-9204-3102-a9e0-1c1a8de582f8 | -9.62734 | -51.76524 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3430a1a8-1bba-39b8-b0fe-f12bd887d27e | -9.62459 | -51.76453 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d07fe1d8-997e-34c5-9f99-434455c9b786 | -9.62383 | -51.77005 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83682a0a-8611-3a8c-95d3-a8e977a525c5 | -9.62245 | -51.76456 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e72dea79-7bca-3fd1-8ce9-f673920aab86 | -9.62174 | -51.77008 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94ce8c4b-ff64-3b98-8937-5dab10816808 | -10.85741 | -51.06045 | 2024-10-11 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fe15a46-c970-3467-9458-5082c51ed297 | -10.44828 | -51.88105 | 2024-10-11 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| adf52350-5d02-3494-9125-99975d9ce723 | -10.4456 | -51.88226 | 2024-10-11 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41141c77-1937-3949-aceb-6be40434b89e | -11.29014 | -51.31163 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13c5f329-ebd5-3e04-a7ec-6fcc52987219 | -11.28579 | -51.30466 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0be2ba26-0309-3c84-aebf-23b11961354b | -11.28275 | -51.30087 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4d1c470-8e6f-36b0-83e3-21e73998f96a | -11.28104 | -51.3008 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b83d880b-837d-336a-8131-ec4371534ffc | -11.27759 | -51.30013 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4209393e-ff27-3a24-9a68-f04454a21266 | -11.27668 | -51.29384 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f5863bc-1f52-315d-97d5-ce5bead315bb | -11.22538 | -51.0285 | 2024-10-11 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 277c0fc7-76b3-3faf-afa0-cf7844f5cd84 | -11.21887 | -51.03683 | 2024-10-11 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0338fa7-81f2-3152-9279-22bd3c6a6f30 | -6.45225 | -51.71445 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a32ad881-e103-3e74-9748-c4cf491959c9 | -6.4122 | -51.72768 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 18464c68-1916-363e-a4c5-52300b4f3cac | -6.40819 | -51.72219 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5c9ccaf8-bc34-3a9c-acdb-6420adbd4792 | -6.40555 | -51.72078 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 254ab7a1-d81c-3adf-8308-4defcbf3e546 | -6.39331 | -52.72305 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8996b0ec-5003-35de-9d45-178acf4f026d | -6.34021 | -51.71066 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b04375cc-225c-3268-aac7-23401eee5825 | -6.31629 | -52.78588 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f9695c2-b6d0-3d56-aedb-97e178074a40 | -6.31568 | -52.79005 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fc0f5e6-e38b-3c0a-adae-bdde039436c2 | -6.31507 | -52.79422 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e177574b-313d-3416-b2e0-ada32ab4f0cf | -6.1011 | -51.2237 | 2024-10-11 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 682fdec8-8789-35e0-8e43-79f9f67ee7a2 | -6.09631 | -51.22281 | 2024-10-11 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14f5200b-2287-3c03-9790-ad8c279a4859 | -6.04528 | -51.37595 | 2024-10-11 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef0b1515-9597-37cc-bb6c-8127a466a0b5 | -6.02781 | -52.4795 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cff271af-1b01-32d6-8e61-89cb63737a0b | -6.02718 | -52.48383 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6bfa8c6-9222-3e40-a17c-e35f7c9d4c52 | -5.97719 | -51.7908 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 016eea36-7bee-312c-af82-a811cbfae892 | -7.91846 | -52.3471 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e97c1335-a4ff-3dee-b550-fe3157dbfb19 | -7.76682 | -52.71275 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf2ff43f-eb77-30a1-9a9d-b4f2bf18d3e2 | -7.76624 | -52.71679 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22d31b91-3a53-3fc7-94c2-472e5de04294 | -7.76549 | -52.71411 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30d669ee-bf88-3f5f-9faa-b80df19709b8 | -7.76494 | -52.71808 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48edcc4c-a3d0-3510-b0fb-4dd5a0e2b0ea | -6.74725 | -51.49642 | 2024-10-11 05:18:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a26440d-9c6f-3c07-b246-862851636b13 | -9.04025 | -52.94818 | 2024-10-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| faebb652-e0e9-36f9-844d-2e9a931b6163 | -8.86391 | -53.05807 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b43b406c-b1e1-3d75-ab79-989c3a503bf6 | -8.86112 | -53.01343 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edc9061e-31f8-355d-bfac-fc131574fcfb | -8.86051 | -53.01782 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ed94b54-238e-3d52-9aab-9f2bb0cc1774 | -8.85813 | -53.03486 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 159c0f25-bde0-3e9a-aaf4-4714874b0731 | -8.85753 | -53.03912 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41129981-47f4-3508-984f-b0522463be21 | -8.85728 | -53.00849 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12bbb54a-a1ff-36fe-bdd1-5ef8e487b2da | -8.85694 | -53.0434 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b54ce849-df17-3f73-85ac-f108f89a47bf | -8.85665 | -53.01303 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 156f5e50-bbfa-39c8-a6ab-5ad1c566572d | -8.85603 | -53.01751 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afef4691-8080-3749-a655-6e208d881b05 | -8.85286 | -53.00772 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68078a46-f08c-3787-b0c1-a32f9a376778 | -8.6569 | -53.0599 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d038e01-a935-3f31-895e-64ed32b0bc8b | -8.65628 | -53.06428 | 2024-10-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d68e0e2-d858-3687-95dc-031aeacb9961 | -9.74556 | -53.14966 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 18108f42-347b-34f6-b5e6-af025361e001 | -9.74494 | -53.15406 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffefc9dc-d5e3-38e9-b260-176f5d90caac | -9.7447 | -53.14681 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0593df5-ba9a-38b3-b7d1-c7338d4b7f44 | -9.74411 | -53.15121 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f9ca4a99-89ce-3979-bd22-6e7638051d8f | -9.74111 | -53.14896 | 2024-10-11 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README90.md)
