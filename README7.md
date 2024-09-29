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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f06d55d8-189f-355e-8207-d261bb443242 | -6.5858 | -44.172699 | 2024-09-29 00:48:17 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e369cb6-0a8d-3758-a9e6-7027df2ab2a5 | -7.0499 | -46.1394 | 2024-09-29 00:48:17 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1628a0e1-e8a3-3c54-9eec-8b8e881b1716 | -7.0517 | -46.1469 | 2024-09-29 00:48:17 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbf87e00-8e7f-315a-9b90-9d11224f3e70 | -6.5738 | -44.1656 | 2024-09-29 00:48:18 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68d702b2-f20e-30dc-ba64-883ca437311d | -6.5761 | -44.174999 | 2024-09-29 00:48:18 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2e095c3-4bf2-33e8-9ffd-45f9be0d0ddb | -6.9391 | -45.8423 | 2024-09-29 00:48:18 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3523292-34ea-37a3-89b7-cb1307afbb6c | -6.9409 | -45.850101 | 2024-09-29 00:48:18 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc4c78b6-9394-379e-89c2-a77080e23259 | -6.8959 | -45.966301 | 2024-09-29 00:48:19 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2559742e-3491-31a7-963a-e582f9850c6d | -6.8977 | -45.973999 | 2024-09-29 00:48:19 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0bb564f-b65d-3cd0-9f07-98aed5af7cf1 | -7.5841 | -49.179699 | 2024-09-29 00:48:20 | METOP-C | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| bab6dfc1-70e4-36af-b10a-ae5612efa851 | -7.5857 | -49.186699 | 2024-09-29 00:48:20 | METOP-C | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| eefdb010-ed67-31e4-9ba4-89dce19de4de | -7.5872 | -49.193699 | 2024-09-29 00:48:20 | METOP-C | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 00ebe5c8-f36a-31db-9276-2cc796620358 | -7.8093 | -50.227299 | 2024-09-29 00:48:20 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0498be69-5db7-3194-a910-c90e59d62d7c | -7.7383 | -50.001999 | 2024-09-29 00:48:21 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbb2a1b0-5ba9-3fa6-8258-4938c52f5efb | -7.5647 | -49.4132 | 2024-09-29 00:48:21 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b622a506-237e-3964-a6a9-da6f6f73b065 | -6.158 | -43.504398 | 2024-09-29 00:48:22 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fece5aaa-b2e0-30d1-9a2a-17fa59d7abc2 | -6.3991 | -44.776299 | 2024-09-29 00:48:23 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3a83cbc-e4c4-3685-ba6f-7437ed3d582f | -6.3872 | -44.769798 | 2024-09-29 00:48:23 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f1e48a7-08f5-349e-8c1c-3b43c22d784f | -6.3893 | -44.778599 | 2024-09-29 00:48:23 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b522b3c-e444-352e-80c7-b111f0e7c4e7 | -6.3914 | -44.787399 | 2024-09-29 00:48:23 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a50fd916-078f-3c17-b226-cd83f46a25bf | -6.1703 | -44.2906 | 2024-09-29 00:48:25 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8afae6bd-ebd6-3e23-bce4-d04007d3020e | -6.1678 | -44.41 | 2024-09-29 00:48:25 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9025114-f8a3-309e-801f-ecff8812d56a | -7.0213 | -48.245998 | 2024-09-29 00:48:26 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9260745a-5172-361c-8bce-1c5b4e9eb16f | -6.3954 | -45.9436 | 2024-09-29 00:48:27 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40ceca86-2a14-3495-b478-052ab3c022d2 | -6.3972 | -45.951401 | 2024-09-29 00:48:27 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 220d11ef-2971-35f8-a8b9-34a802bc26a5 | -6.3856 | -45.9459 | 2024-09-29 00:48:27 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9b246c9-c93a-3e42-8e25-0c062c7944eb | -6.0334 | -44.539001 | 2024-09-29 00:48:28 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8419cfc3-c1f0-3a4f-9f90-81ac99d42c88 | -6.07 | -44.693501 | 2024-09-29 00:48:28 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5203b33b-5db7-37cd-a291-d0e387d4e4ce | -6.0721 | -44.7024 | 2024-09-29 00:48:28 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d7656cd-1d4b-33c7-ad08-60d819af2592 | -6.0743 | -44.711399 | 2024-09-29 00:48:28 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb2bd364-c78c-3fb2-b7b0-4fbb813e6783 | -6.1238 | -47.2589 | 2024-09-29 00:48:37 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfb5b4c8-bc39-343d-9607-3ce3fe19cc69 | -6.1525 | -47.6954 | 2024-09-29 00:48:38 | METOP-C | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca267e9-997f-3599-a7d0-b213913c057b | -6.1541 | -47.7024 | 2024-09-29 00:48:38 | METOP-C | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7a99d84-4734-3c4c-90fa-d3f841862133 | -6.1557 | -47.709301 | 2024-09-29 00:48:38 | METOP-C | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9443e6d1-65ff-3753-a9ee-f82571ea9318 | -6.1573 | -47.716301 | 2024-09-29 00:48:38 | METOP-C | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fb1d514-164d-3755-bfa1-e5b3d3779f62 | -5.0116 | -43.796902 | 2024-09-29 00:48:41 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44eee9ae-4486-3030-889f-79bbeaafdc61 | -5.0141 | -43.8074 | 2024-09-29 00:48:41 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a86654f0-0bcb-341a-9921-143b3f807d69 | -5.0166 | -43.817799 | 2024-09-29 00:48:41 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78d9d9f4-c88b-3c25-8af2-ac6768fb4f11 | -6.4289 | -49.718201 | 2024-09-29 00:48:41 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10e00723-4ea0-3bc2-b7bb-9b86de5386dc | -5.323 | -44.980598 | 2024-09-29 00:48:41 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 104584a5-7a0a-3869-b3bc-48e76e3cab1f | -5.3251 | -44.989399 | 2024-09-29 00:48:41 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63ed474c-20b6-3b86-819f-df21b13dd7e2 | -5.0018 | -43.799099 | 2024-09-29 00:48:42 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e525cf9b-90d8-3728-9029-014b998710c6 | -5.0043 | -43.809601 | 2024-09-29 00:48:42 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9409bb34-81ff-31a5-9738-d8061009bb9c | -5.0068 | -43.82 | 2024-09-29 00:48:42 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82914d8e-c1f0-3e97-8d0b-32a186ac9706 | -4.9946 | -43.811901 | 2024-09-29 00:48:42 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ced183c4-3833-30c8-9663-32343c4cc6b2 | -4.9971 | -43.8223 | 2024-09-29 00:48:42 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4c920ac-d037-30e2-aedd-d08dd8e2bd58 | -5.7629 | -47.437801 | 2024-09-29 00:48:43 | METOP-C | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87579511-7464-3628-aa6d-d58696d6bf31 | -6.0362 | -48.806801 | 2024-09-29 00:48:44 | METOP-C | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c0420db-eeb7-3ccb-aeae-911431291dec | -6.0378 | -48.813599 | 2024-09-29 00:48:44 | METOP-C | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d8c3fe1-1a19-396f-9a3b-1a4e568f9bcf | -5.396 | -46.567501 | 2024-09-29 00:48:46 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3fb58b37-af15-3948-9118-1ded41d26f66 | -5.3977 | -46.575001 | 2024-09-29 00:48:46 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8da7212-bbe2-35ff-ab91-94d9a52f9a70 | -5.3994 | -46.5825 | 2024-09-29 00:48:46 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2442884-f67a-342d-9f21-1f33fed58a82 | -6.0022 | -49.335602 | 2024-09-29 00:48:46 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e5eeacd-1090-3493-9be9-4fd5c8ba0548 | -5.9562 | -49.178799 | 2024-09-29 00:48:46 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f3badf3-2d1a-3eab-a465-116f9ff36014 | -5.2392 | -46.160801 | 2024-09-29 00:48:47 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c46db4b2-bde0-3919-a861-1c7399a3f312 | -5.241 | -46.168598 | 2024-09-29 00:48:47 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2be68ba-fca4-3854-9786-776e138d0a30 | -5.9413 | -49.203899 | 2024-09-29 00:48:47 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7ac8373-2d4b-3bb6-883e-b0236301c637 | -5.9284 | -49.192299 | 2024-09-29 00:48:47 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45bd8ff2-1e48-3020-84a6-37ca65967d65 | -5.93 | -49.1992 | 2024-09-29 00:48:47 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3f4cfd3-c160-380b-a88b-62e6f0ee81e1 | -4.9228 | -45.119999 | 2024-09-29 00:48:48 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94d30263-20a9-3c7e-9365-1c2178d9f4e1 | -4.9249 | -45.128799 | 2024-09-29 00:48:48 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80ac4b73-3656-390a-95d1-93b74e5dbd4e | -3.9606 | -41.471901 | 2024-09-29 00:48:49 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 957fa574-2473-3eb4-a333-14ce7a161097 | -3.9643 | -41.487301 | 2024-09-29 00:48:49 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2d031453-8b06-392b-9239-30b11df4819d | -5.085 | -46.163399 | 2024-09-29 00:48:49 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fda93a4-e007-318b-800f-6f64f9462cd7 | -5.0869 | -46.1712 | 2024-09-29 00:48:49 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0df77d41-25d3-3a49-85a0-7ebfb2d77ec4 | -5.0887 | -46.179001 | 2024-09-29 00:48:49 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 67e6abf0-3b01-32ae-97e9-4547bc360098 | -3.9509 | -41.474201 | 2024-09-29 00:48:50 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ff3b499-aa2d-399f-9571-f5b511e6ae21 | -3.9546 | -41.489601 | 2024-09-29 00:48:50 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ee8ec41-d914-3788-91dd-968f268fdffc | -3.9583 | -41.5051 | 2024-09-29 00:48:50 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a82a6f5b-ad55-3c90-8c2f-5be2e970f564 | -3.9449 | -41.491901 | 2024-09-29 00:48:50 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 084eced1-c221-3212-80f8-1511956ea0ae | -3.9486 | -41.507401 | 2024-09-29 00:48:50 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e1907fb2-875c-3c24-b3df-fd5fc31df924 | -3.9523 | -41.5228 | 2024-09-29 00:48:50 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e1ce04fa-ae11-3af2-85d9-631eabb9dca1 | -3.9389 | -41.509701 | 2024-09-29 00:48:50 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 659a2107-aa28-3c66-ac95-6e3702be7cc7 | -5.3249 | -47.684898 | 2024-09-29 00:48:51 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f4195ef-2a96-3dd2-91ab-281c98ce54e4 | -5.3266 | -47.691898 | 2024-09-29 00:48:51 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6348b3d-2ec1-3141-8404-19b8d30def7f | -5.2434 | -47.376999 | 2024-09-29 00:48:51 | METOP-C | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86802465-b5d1-30de-a1ef-ef56fc4c69e4 | -5.2451 | -47.384102 | 2024-09-29 00:48:51 | METOP-C | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 594e29f2-3e07-3a79-aabf-fc124d7959c7 | -3.8006 | -41.575001 | 2024-09-29 00:48:52 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9eee9e64-0632-33c2-ac2b-a1aa0fcf1cab | -3.8043 | -41.590302 | 2024-09-29 00:48:52 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab75b4c9-5beb-370f-a27a-3e58b24c0a9f | -5.5777 | -49.010601 | 2024-09-29 00:48:52 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3038aeb0-9067-34ca-a003-55ab22b077f3 | -5.5793 | -49.017399 | 2024-09-29 00:48:52 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb6f9e48-6248-3020-9cc5-a2f796957f0f | -5.5809 | -49.0243 | 2024-09-29 00:48:52 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1c38d0-0b80-3ddb-a470-4a808cb237e7 | -5.5664 | -49.005901 | 2024-09-29 00:48:52 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cf74630-f3f7-3f0f-852e-833d289cb03b | -5.5679 | -49.012798 | 2024-09-29 00:48:52 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64eb48b9-7f23-37f5-9f1b-cf3fa7def6a0 | -5.5695 | -49.0196 | 2024-09-29 00:48:52 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fc7f472-bc16-3755-b790-d0ac33469d3b | -5.5581 | -49.0149 | 2024-09-29 00:48:52 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f521280e-922c-3d3b-a0a8-f09174aad406 | -3.7909 | -41.577301 | 2024-09-29 00:48:53 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8868b3f1-f5f6-31bb-a0b9-fb59a84cfbcc | -3.7946 | -41.592602 | 2024-09-29 00:48:53 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 81048e52-6779-3310-af67-dd17ab675180 | -4.1382 | -43.7192 | 2024-09-29 00:48:55 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6cc1cd54-8d16-3aea-8d71-d89e98edea6d | -5.223 | -48.182301 | 2024-09-29 00:48:55 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| abf7eeb1-1bbf-3931-b825-dea0f5baf169 | -5.2246 | -48.189201 | 2024-09-29 00:48:55 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b645ee44-260f-30d9-94e3-098d57057a66 | -5.2132 | -48.184502 | 2024-09-29 00:48:55 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce445bb3-7186-3666-8dca-4240006ff532 | -5.2148 | -48.191399 | 2024-09-29 00:48:55 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4771ffa9-0909-3ce1-8fb6-9ab079315d11 | -5.2218 | -48.536201 | 2024-09-29 00:48:56 | METOP-C | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 630797b9-b5af-30f3-b0c4-f91bec588f1f | -5.2924 | -48.844101 | 2024-09-29 00:48:56 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c387798d-ab09-3afa-81a1-385db68c23e4 | -5.2939 | -48.851002 | 2024-09-29 00:48:56 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d231477d-c67d-302c-b713-be1472c6fe48 | -5.2677 | -48.871201 | 2024-09-29 00:48:56 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e5f5f62-9fa3-3365-ae92-8134f03a2e32 | -5.2692 | -48.878101 | 2024-09-29 00:48:56 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a9e1741-4490-3523-ac3d-ec8f1b36bd03 | -5.2708 | -48.884899 | 2024-09-29 00:48:56 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd0189e-c5f0-36ac-813f-e99253de99c2 | -5.2594 | -48.880299 | 2024-09-29 00:48:57 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
