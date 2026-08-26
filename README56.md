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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f5b0579-1eb4-30bb-bf4f-18cb4921701e | -3.78152 | -59.27895 | 2026-08-26 05:27:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e215e3e-354a-3b19-b6d8-171689ca71c1 | -8.60915 | -54.7347 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0540c932-8b5f-3146-824e-e2cdab5397ba | -6.69971 | -56.34711 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc826e2a-85bc-3815-8ddf-1552bc25032d | -6.83625 | -52.49951 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1045ba80-c4c1-3ddd-9a98-fb776c088ad9 | -6.98008 | -59.25584 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cff641be-0ea0-39ba-a265-13d9c1b8299d | -6.68487 | -56.34898 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e97b987-c5f8-342e-9f77-ecc029b298f1 | -5.3495 | -45.16097 | 2026-08-26 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6415ac73-6004-311d-8408-1e6211e7588b | -6.93865 | -59.09299 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbff3ede-de9b-35c3-a82a-2332b415cd93 | -6.62568 | -58.48359 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 952a5588-5217-30e0-8bc8-4f69a3c93585 | -6.502 | -53.26034 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 209de9c4-3c13-3a7d-99fd-cbe2a459d401 | -6.50684 | -53.25706 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac50b6ce-44e3-39a8-847a-f41a9c2a20ac | -6.81933 | -59.58659 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17b24e4b-c7cc-3b02-be16-febed8524a4f | -6.63237 | -58.5061 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b2d279b6-f77b-385c-be4e-9dd5172a02e5 | -7.47211 | -61.36905 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41df968d-a977-3c3a-b426-f114ae28e30c | -6.8592 | -59.40053 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a92b77dd-99a3-3105-8a2d-7b25552462c4 | -6.25928 | -55.41536 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ce9046f-7e02-31a0-8c4f-bfe1167cbb4e | -6.79324 | -59.64316 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c7a2bc9-5651-328a-a6bb-61e1bbeaf9e0 | -6.54088 | -56.25863 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f101be54-4f6e-39af-ae20-a586d1255e78 | -7.04507 | -56.60818 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4863f9fe-ffd9-3fac-9348-b8d5d17c907b | -6.82209 | -58.65437 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae7b99d4-a09a-3a6d-9859-9c1bb2c20355 | -6.77608 | -59.43352 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbc5de77-3006-3f13-8c85-6185ff1e6077 | -6.76391 | -59.44576 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d9f845d-3d4a-3e58-bb4a-a04cf30c2abd | -7.37429 | -55.19414 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e25761a5-eb8d-38c1-9374-ac4ec0157880 | -6.24641 | -55.47626 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8357525-72ae-3fe9-9620-3b444a34f1dc | -7.56043 | -61.42551 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fa1de89-f11f-33fd-918e-dd75c29a04e0 | -7.06919 | -59.22796 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8d2482f0-2096-3ef2-978e-d3762ae4b165 | -8.56681 | -55.27916 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80b9aa47-f278-3188-97e0-5548f1f10393 | -6.12348 | -53.75301 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8481f5fb-be9e-35e0-87f3-197d983cd25b | -6.17904 | -57.70464 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45a5cb61-6912-3ecf-9e37-6dd47b7e7c90 | -7.06477 | -59.23438 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aafed46e-237c-3bb9-ba05-913ffc4b862e | -6.62125 | -58.49004 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b40322ee-8bf6-3e3b-ac58-6be9362472ba | -7.3035 | -49.54469 | 2026-08-26 05:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a38a9d6d-e5bb-3bd6-a09e-22356b6f1ff8 | -6.18192 | -55.44104 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f9902f4-6130-3419-8101-75e7ee9855bb | -7.56327 | -61.42987 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9580a49-654f-3565-aa08-9854159cfaf7 | -6.81987 | -59.60454 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11b2c137-e239-3fa0-8b81-28f7e541a6bf | -6.70075 | -56.14754 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79b47631-6b39-3906-ac7d-cbd83ef5ddcc | -6.07632 | -59.97456 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab416604-9268-3df4-aefe-8d8f2847e973 | -7.06642 | -59.22396 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1fc7cd01-9038-3719-91ab-29badc5ccaef | -7.0282 | -59.23148 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19efab56-8247-30d0-9b5f-d516c57747a7 | -9.18861 | -49.99606 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0c40305-204f-3d47-a4f2-ca526c191d9f | -3.54296 | -58.65058 | 2026-08-26 05:27:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63464e6c-c8c4-3abe-a924-396bcb6be455 | -6.88854 | -59.40877 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b58bfc27-5fb9-3636-8750-726a22db8827 | -6.87987 | -56.51119 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31ce7a43-c5c8-3097-a9c2-1d1b57d9161d | -3.5335 | -48.17918 | 2026-08-26 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98fc67b0-ae83-31fc-bd0c-7d601f4547aa | -6.63899 | -58.49987 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f0d7aa5-ea69-3d75-b698-8a93ede94f12 | -7.47746 | -61.36917 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b13aa41e-fac1-3d9a-8ce9-d89262af2712 | -6.71967 | -59.12949 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27c9be27-8645-3df9-9ecf-27e09d6bbaeb | -8.17464 | -54.95947 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d4fa2d0f-0742-3886-bac6-bacee12f0c23 | -6.78436 | -59.65602 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79572414-55a2-371b-b079-09eae2d2d5bb | -6.28115 | -53.35904 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 475e954b-3a34-37a9-a478-614d66f71793 | -6.8115 | -58.6134 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fa3511e-36f4-36c5-b6fa-844c9ad47595 | -6.79494 | -59.58986 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55a1b8bb-84b9-3cf9-8b88-8cef8a0468b6 | -6.86087 | -59.41148 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29667606-9148-30a7-85ab-7149a0609ef0 | -7.2758 | -45.35178 | 2026-08-26 05:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96775faa-6305-3d8f-ad05-aef6aa7d29d7 | -6.6462 | -58.49742 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 528a22b0-8599-3f2a-ba2f-5b9a41164622 | -9.0273 | -50.78337 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f04a3f40-42ac-395e-b59b-859581a87269 | -6.15998 | -57.80432 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 77a8d653-97ec-3a1a-bd64-d3382e53c13c | -6.27522 | -53.36999 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15e854e8-848b-32ab-a762-e7b90c9fb22b | -7.25983 | -49.85728 | 2026-08-26 05:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f635ec3-04ca-381f-81e9-8a5b8aa868ba | -6.14867 | -57.69994 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81002083-0a00-3b43-ad63-9f46433f234a | -8.16335 | -54.98221 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef69cd1f-b197-3683-b667-1c77ce9b4a62 | -6.14622 | -59.92418 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd27f293-642b-3676-a48f-a2c7760500df | -6.31049 | -53.56995 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6b0d318-70aa-3c09-bb81-ebe39109ef0b | -6.81095 | -58.61689 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1644a68-598a-351b-ad72-066095f85274 | -6.97515 | -59.07743 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ceebc94-bc99-32ea-b6d2-eef26d25484d | -7.02046 | -59.23736 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a496c8c-baf7-35e9-b114-03b93cc0b091 | -5.78169 | -59.17206 | 2026-08-26 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c95b9b5a-b32a-3765-8b88-d6b91d73e460 | -6.62901 | -58.4841 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c9e0842-a2d9-3325-9ba8-019b5b309da7 | -8.59647 | -54.75267 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23940281-d427-3279-bf25-c43e2ca62745 | -3.26755 | -49.52422 | 2026-08-26 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b87c04f3-cf1e-33fa-ab92-b06f688156e4 | -6.65341 | -58.49498 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a36b11f9-3975-3b3c-9d4a-fefface32814 | -6.79363 | -59.81144 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 256f1fda-e82f-3007-a0cc-dd0590033476 | -7.06697 | -59.22049 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 14a4edaf-f19b-3fce-aad0-b7abdef1c4c3 | -8.09121 | -51.67637 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5784faed-8f03-3bda-95f2-6a4d40feddf8 | -6.83294 | -59.95078 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dbb5306-76b2-3d90-8da3-b861447ef94e | -5.90588 | -57.71403 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7598c298-07b1-3d03-8ba1-378cc42ff8f4 | -7.00225 | -59.30918 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad7de9d6-794a-3770-958c-6ef1f42ca385 | -7.20969 | -60.61238 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08aa326e-a44a-3739-9874-7da94e306090 | -7.25928 | -49.858 | 2026-08-26 05:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5aab9ef-bfc6-389e-8ab9-02afcd2a0ae9 | -8.57552 | -54.83903 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 677dd345-d468-36e4-ab8f-84c6fd60ee63 | -8.17073 | -54.9589 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a448e5ff-50fc-3b44-9433-b57af2aef380 | -5.77706 | -57.55093 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6dadcd7-823f-3891-855f-5e57bc2a3dce | -6.7313 | -59.142 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8b8ec08-780d-3710-82ef-f633de9e76c5 | -7.30732 | -49.54393 | 2026-08-26 05:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fd86e27-6418-316b-9091-90f0a6726651 | -6.42412 | -54.93705 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d91f5940-7e6d-3fbd-abe9-e15d3c5b77e7 | -6.12846 | -57.71886 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd4b8a94-197a-3d5a-82f2-884b4afbe17f | -6.62425 | -53.18712 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96fc22be-02ce-3d4c-b6fd-1ab5c6d9f4c9 | -7.03429 | -59.236 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f467662-a506-36e1-a231-0d7534aea5b0 | -3.21625 | -61.23865 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e65ffbba-3c77-395a-9367-774c143d55ba | -3.54501 | -48.18116 | 2026-08-26 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2d08eeb-6de7-34be-92f2-ddb18dc094bb | -6.57951 | -59.00722 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68c0de5f-2d04-3d64-9878-b3f70c3f21fc | -6.83406 | -59.94377 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e567b81-e57d-3fb1-8568-4e869d05be3a | -6.63844 | -58.50337 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f47a9de-aefa-3f2e-98d5-3c530b73550c | -6.82044 | -59.57963 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd28679a-3a0d-3724-903e-11988c81b807 | -8.17543 | -54.95402 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8435f12d-2bf0-358e-ad71-87b53d70ba22 | -8.70887 | -49.60689 | 2026-08-26 05:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29fc5ee5-a530-3a55-b32e-b78da0aff89f | -7.51639 | -61.39106 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 566441ac-53df-3616-b5ef-6027ba599e0e | -3.5329 | -48.1832 | 2026-08-26 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a9c46ac-a6aa-3a8b-99a0-dfeec2bbc456 | -6.25719 | -53.37531 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2b45bac8-0018-3638-ae3a-8e4b0128f264 | -6.94252 | -59.09005 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README57.md)
