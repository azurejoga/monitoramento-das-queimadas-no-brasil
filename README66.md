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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6238d01-168e-35ad-b984-45731e8a0936 | -8.34527 | -44.84144 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 695edf70-b537-3a44-8afa-4060c780d33b | -6.69758 | -43.54078 | 2025-09-10 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39f8c7d1-0634-35ff-87da-7650cdd09c6c | -8.70755 | -47.87455 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f65bc99-e02a-3a13-8aae-58e112b11465 | -11.7249 | -46.7009 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 893b576c-58c1-33f8-9d0c-b16b171fc509 | -7.08542 | -45.20085 | 2025-09-10 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b7522aad-701c-35d2-9b99-8b206c5fbc43 | -6.34063 | -47.10215 | 2025-09-10 04:42:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ef7e1419-f022-3273-b095-0f657c149e1e | -11.66463 | -46.90361 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61c03f35-5d42-38f1-83f1-73c8a754f5e3 | -7.55231 | -44.6604 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e58411b-4b04-3e26-9824-2d1d43938c66 | -9.31826 | -46.72871 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc936f2f-9057-3ebf-b970-09761ce9d27c | -10.01607 | -51.67008 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c5b406b-0b47-3822-b88b-9ec7013d2f84 | -9.04819 | -50.492 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08ddae03-5a4f-30e0-8f63-5ec04174b056 | -9.66922 | -46.63729 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e58a611-849c-3ffc-979b-e98afa56851c | -8.98683 | -46.0654 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6346940-d975-336b-b75a-9e7a95c0d43b | -9.77183 | -48.34074 | 2025-09-10 04:42:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 432b96d6-25b2-3b41-a4ba-4f3a855d6a0c | -8.06757 | -48.65627 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abc662dd-01b8-3452-a5eb-da94a1984326 | -9.31159 | -46.72333 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c0fae5d2-d2aa-388e-80dd-5a2b0e7cb4ea | -11.16079 | -45.27295 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 885c65df-c205-3a95-8600-3270117f3967 | -7.38491 | -48.17223 | 2025-09-10 04:42:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9439b5b3-3b3f-388f-8f53-cde1af0577d4 | -8.06282 | -50.19742 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9556c57a-397e-3c64-aead-ab2c249339ee | -11.44077 | -49.26147 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe1d8b3e-d699-3ba5-9cb2-e2c736bc4b32 | -8.05472 | -48.67261 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 400e54cb-0315-30ef-a85e-77c04fe427d7 | -10.00813 | -51.67609 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab995448-5ef0-3de2-b757-e5598984bffd | -7.36987 | -47.43621 | 2025-09-10 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2b4eb1a-bda4-3fb5-b875-6fa68bd82931 | -6.19964 | -53.27419 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db4ac87d-a8ac-3c9b-bb8e-20b228889b5c | -6.89205 | -47.88549 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e9be2a59-ee55-3de5-ac9c-5dc2abd6d52c | -9.06022 | -46.98202 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2b8be6fd-5557-35ef-b3fb-7e2f7a5c46ff | -9.55603 | -48.29274 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3814651d-91e2-3757-9fd2-2e0818257e1e | -6.31165 | -45.668 | 2025-09-10 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a16fbf17-5602-3316-87c9-15ae983c9cf2 | -7.83952 | -45.41301 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57d686c7-be22-3411-8ef8-cb16933c3ffd | -10.65646 | -48.61868 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecb6e502-7a1f-34c6-980c-d1afd81f23fc | -10.72416 | -48.28506 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b24c4efb-d381-3427-b33e-1ed58ee9fca4 | -10.66043 | -48.61563 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f6f29f2-835d-3ebb-9e75-a0071cd4e9a6 | -11.14103 | -46.34924 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fac34ca8-e61c-3c2b-b273-b2e8002b1296 | -7.54828 | -44.65973 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 423ad754-e73b-3a31-b1d5-0415691251db | -8.04916 | -48.67577 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e547035-78f4-3e8f-8a12-75f9c77427f7 | -6.69068 | -46.41143 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c17b48af-03f4-39a3-8c5f-2f706dc81533 | -7.46565 | -44.9435 | 2025-09-10 04:42:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 751bc3bb-f1ad-3f52-ac4f-14ab313c6eae | -9.89204 | -46.47361 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8477aea0-99a3-3304-b0da-2fa3b52da10f | -10.16725 | -52.62152 | 2025-09-10 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 681d1615-4897-35cc-bf57-3fe6b2b188ee | -9.06742 | -46.98314 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fefda26a-4d89-3645-ac9c-bddc17b6c4ce | -6.41181 | -45.29015 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 111f73ef-b406-3ce8-ab1e-575fee0d22c9 | -11.109 | -48.37335 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3a62cf5-afac-398d-b486-4a514f59efcc | -6.56617 | -43.15032 | 2025-09-10 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb57ebdb-f7cc-3a44-88f4-53c7ed940281 | -9.07207 | -46.98225 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| deedb660-823d-33b3-86b6-92b16c5ef27d | -6.72203 | -51.97219 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0226c335-b081-36ae-9d6f-6de4a564901e | -6.67875 | -44.55023 | 2025-09-10 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb53cdbc-8073-3494-812b-64a2c71bffc9 | -8.2011 | -47.15812 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29b9b834-dffd-3a0a-81f6-e6e05917d673 | -9.95915 | -51.17968 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae9137c7-0efa-306f-847a-fc8528c9ac02 | -6.20712 | -45.62254 | 2025-09-10 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4720bdde-58c6-3e29-a1a1-8bc405550ee1 | -9.66986 | -46.63289 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fdd229a-541f-302c-a98b-a4e94b558c8e | -9.05974 | -49.82278 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e65d44b6-2bd0-303b-a1c0-9ea83d79944e | -9.04197 | -49.80561 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 463e78b4-7086-3a51-997f-dc0f825f2bb0 | -10.14754 | -46.17192 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b521286c-ff99-33ad-b848-6f17e6177adb | -5.79948 | -51.67321 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5038439f-888f-3e84-b332-feba1f8586ef | -8.02603 | -44.49989 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d347aa0e-bd9f-3049-a433-5bd971a5c0d5 | -9.88765 | -46.47744 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 095f255d-eecb-3f79-94dc-ce69d588dd79 | -6.68224 | -44.55437 | 2025-09-10 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08a23b96-7790-3675-b482-76db6f719138 | -7.56147 | -44.65439 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5b74c8c-1f95-3bdd-8437-e885045af36a | -10.30489 | -48.82233 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b30ef6b9-7b33-3610-9537-b86b303dbd00 | -7.27613 | -44.56881 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31dc68ec-38d0-3ce5-99b7-ccbc523542a4 | -7.30575 | -44.14793 | 2025-09-10 04:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3b4acf8-5a7a-32a3-917f-5810850fa172 | -8.75022 | -47.09594 | 2025-09-10 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf317fba-6687-3389-9c52-4f57e9327c91 | -9.3565 | -49.00232 | 2025-09-10 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3597736a-1abc-36bb-842d-8c78fa935f01 | -8.04861 | -48.67931 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 0ae6f83f-24a0-3bf9-8d57-a3384c96bff0 | -10.38279 | -50.54162 | 2025-09-10 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1489ff6-4393-3e6f-8aed-c707b64e79c4 | -11.11764 | -48.36311 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4f5a54f-4af2-3832-9c74-47de68f7c148 | -11.84951 | -46.77265 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c94dc55f-b897-39cf-9cb7-f1e798db5c66 | -10.00736 | -51.70229 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb6bbb27-bbd1-3648-bc5b-3bd643383c64 | -10.72936 | -48.2976 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a61f08ac-d573-346f-b76e-45d45de48c3d | -8.4781 | -47.3037 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba1bc828-b09d-39d0-8cb8-1ab7ee4a4e04 | -9.09743 | -46.98512 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1f36fd7-4985-34db-a206-052c1588026c | -8.39935 | -47.29945 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebaa803b-306a-3747-86ee-50001d4277b5 | -8.46092 | -48.9541 | 2025-09-10 04:42:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7edb6ff-ca35-354d-ba1b-dc80cfbeddea | -9.0061 | -46.06071 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| afa40e5b-773f-3329-ba1f-64f89775be87 | -8.04303 | -48.693 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8fbb7d6b-9a23-384c-8fd4-5aa62dd5852d | -8.49662 | -45.66061 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0269e3d-edbd-3099-ac8d-89bed00af16b | -8.48229 | -47.29965 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b6d96a43-de04-3394-86a3-97e7cddd4f87 | -6.43934 | -47.02553 | 2025-09-10 04:42:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a03309ba-36d3-3c44-b7c0-3d1e74424655 | -8.2808 | -47.4669 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8eaf271-b717-39cb-8541-f37b397b1055 | -7.57917 | -44.70697 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f779507-e1da-3d01-b478-eb68945e5f4a | -9.31761 | -46.73298 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a84efc6c-afda-3227-9564-62e8ac7e13ea | -6.21085 | -45.62319 | 2025-09-10 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0df9636c-4ffb-35bf-ae46-df2d1484b465 | -9.07981 | -47.05431 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11c9b1f5-d860-31a7-97c8-e1b1fe2b88c9 | -8.9824 | -46.06918 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcb5e650-8b9c-38be-bfcb-acd4fc403c48 | -11.55749 | -49.04346 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baa729e4-3678-37b6-ba96-1c456c5fb1cf | -8.07094 | -48.65674 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00106b55-f8a8-3be9-848d-ad0d827955f8 | -7.73643 | -50.75515 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c64376c3-ff1d-3504-981c-c7d91c77e740 | -7.24149 | -44.46928 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2fc0a29-8a4e-3720-8de8-b4dc1ff810d6 | -10.14617 | -46.18884 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c691db6-6de4-3526-9668-413f0e2da1c6 | -10.00456 | -51.69808 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a5c1343-c6c6-3680-af3d-c562f9953c26 | -8.05143 | -48.69389 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 79bca2d8-fb87-303a-9743-2b12be4ed5eb | -10.0121 | -51.6731 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc59d94c-7073-3c78-9f52-55b4e8e06d2b | -9.02088 | -49.78791 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84787cf3-463c-3f0f-8e0f-dcb6407646a2 | -6.42594 | -44.44104 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50dfa40f-e46a-3034-a392-3bde47613a09 | -8.98596 | -45.72945 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 893e6d9a-935c-3b4d-81e2-e525a1164387 | -8.28022 | -47.47079 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcd1d31f-de89-3ae9-a32c-7d7cfd5dc17f | -8.1658 | -46.07012 | 2025-09-10 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f11e538-586e-3711-90f6-c7bfc144df8b | -8.47816 | -47.30319 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2be1143-555f-3a9b-a666-71a48afdfc05 | -8.70467 | -47.87025 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 305d52c6-7f87-37e9-ab97-2756d7a02964 | -9.80394 | -47.79565 | 2025-09-10 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README67.md)
