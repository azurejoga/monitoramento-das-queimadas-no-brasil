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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6e83eef-8546-3c5c-b53c-397b3329216e | -8.8296 | -50.67034 | 2025-09-30 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98a48f77-f339-3e9f-9c5d-4bc7fc90a6f7 | -12.02712 | -47.8921 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3378ba68-e4c2-35b5-b869-1101334a5b56 | -11.26061 | -47.23289 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1f6a3387-164f-3535-aea5-3badda1191ec | -10.75352 | -45.38793 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6b4bd8f-050b-3ea8-9f29-8442d51a334e | -11.20729 | -53.29856 | 2025-09-30 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c90bc85-c094-3657-a8d7-c652d1f00b84 | -11.16531 | -54.11781 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| dfee6f9d-fb9e-34b0-8118-8de8ae486b23 | -10.96092 | -46.49795 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3e4cad72-f729-3bd3-9c2a-29f6c13b9f5b | -13.06537 | -47.07714 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89f26756-f7fe-3cfa-8a1f-6fd1b0d57289 | -10.40013 | -47.80537 | 2025-09-30 05:08:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f67c1f03-442d-3a2b-842b-ede42c04c0b5 | -12.22392 | -43.75707 | 2025-09-30 05:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46cbe78a-da06-387c-9eda-a46a64adfd2a | -7.7666 | -45.75946 | 2025-09-30 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cd5d19a-f72d-371c-bf91-ef994e7fe158 | -12.16088 | -47.7748 | 2025-09-30 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d124bdf-9ac9-37d5-a061-62690cadf239 | -8.50305 | -47.25479 | 2025-09-30 05:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f5ee76d-52d9-3983-842d-a36c97f8e45b | -11.20188 | -47.7397 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d653da67-f01f-3422-86af-d52ba3de96d9 | -6.32737 | -53.17325 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f1de92a-157e-392a-be9b-5f018f6e5db7 | -10.88544 | -53.74968 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b48058a1-7c62-309f-831d-2fc48a3ce6d6 | -10.83549 | -47.97483 | 2025-09-30 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59f33d47-2272-3746-9173-9926842d9fec | -12.95472 | -48.41299 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df403f31-0ad2-3467-9d85-e70b1bbf6c65 | -8.14428 | -46.37273 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e114d558-2a8b-351b-8b17-1b166d02f695 | -10.83203 | -47.96048 | 2025-09-30 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a9a28a3-1d96-396e-a293-3397801c0531 | -8.00596 | -47.05291 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c346f3d-3d93-3cdf-a53e-b7bbcb8a6d72 | -11.25164 | -47.22556 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b42ffa35-8914-3eeb-9c5c-4bac201bc770 | -6.36849 | -45.63507 | 2025-09-30 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0dfcb1b2-1f36-3f21-b99c-f75cffee46a5 | -9.06106 | -46.70754 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 041694e9-4edc-36d6-aca9-8b0f3e4a515c | -8.24846 | -45.54229 | 2025-09-30 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54f6262f-be21-3fc1-83a9-fa7449c47474 | -11.75291 | -46.84455 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b64007ce-0ad5-3381-a357-0ea465e0eea6 | -13.3657 | -47.9152 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b194c754-7680-3e90-a018-e0155b049940 | -9.51552 | -47.69272 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb65a411-c61f-3e07-94c1-7fd04ab3e2f4 | -10.83631 | -47.96853 | 2025-09-30 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d6390e7-6826-3fa8-84ca-6830e773ef14 | -13.39153 | -48.06416 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffdaf224-2e52-3785-940b-9f74123d32f1 | -10.19688 | -44.89312 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6c0e0271-9717-3956-b3a0-87934957839b | -10.18856 | -44.90797 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 0c9a4817-b58b-3600-8740-bd87eb685573 | -7.11075 | -45.5516 | 2025-09-30 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5850f218-d33f-30b8-b284-8d7aeb8672b0 | -11.20111 | -47.74561 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91abc829-7124-3390-a23c-2db32b801a7b | -7.91193 | -44.60912 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1804d97d-afe3-35e9-a5fd-8165264b0a1d | -9.30114 | -54.50636 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 044edecb-91e2-3652-9326-b0e1e3a7d3f0 | -10.02992 | -52.10381 | 2025-09-30 05:08:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1a97d71-a7a5-346c-8b48-635e43b41898 | -7.76888 | -45.74298 | 2025-09-30 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7815718-e901-3322-a3ce-ca8b61c1bf8b | -7.86949 | -47.25859 | 2025-09-30 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5451fb34-2a7f-3a8e-8f16-5b5ce87efe4e | -9.41589 | -54.71553 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c009296-9bea-3d4e-9cb0-0b3879aaccef | -9.29481 | -54.5015 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8816c464-9d9d-3638-9c4c-312978191f11 | -12.21661 | -43.75322 | 2025-09-30 05:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e151c73-b64c-3794-9cfc-af0837a9c6ef | -10.19051 | -44.89252 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8274a8a4-a5e7-3780-9023-9dc7a6c4bade | -12.23003 | -47.79357 | 2025-09-30 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 082f23b5-332d-384e-a9af-ba32556be271 | -10.75679 | -45.37113 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8fb5c903-7fa6-3691-874f-a1402b9d3ec6 | -13.36611 | -47.9118 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b9a191a-7645-3a61-9609-a45eecafe154 | -9.75755 | -47.19638 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5625577d-4b58-3007-b21b-2e9f3834669a | -12.75594 | -46.86792 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fad83a19-df7a-34e3-a586-57b33cc51d38 | -7.8268 | -46.9878 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec2e4bda-ca99-3e57-8ff9-fc87f7eafd34 | -12.2172 | -43.75418 | 2025-09-30 05:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d1aebbc-ae25-32f6-83b4-3e91267fb18e | -8.16743 | -55.16947 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 286f6a6d-4cd8-3d4f-8c3a-e4c068de67d4 | -8.87578 | -46.63068 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4d323c0-466c-394e-bad2-bc5a32d36f01 | -10.07765 | -50.21287 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 82692954-2ff4-39ba-b492-0e02f6a8e6d9 | -10.63798 | -53.6643 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fb88b62-cbbe-3c58-9768-09dc529f2754 | -8.87382 | -46.64544 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32b442e9-809c-3b4a-8385-5a0be58595ec | -6.72093 | -47.20589 | 2025-09-30 05:08:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 774eec55-53fa-3289-8bae-3152b79dd1ac | -10.60276 | -49.63982 | 2025-09-30 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c664375-fd0a-3402-9d9c-c5e1fa649c8e | -9.4119 | -54.71871 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e00b022f-b06e-39da-bdb6-ed3548c73e45 | -12.87174 | -46.77985 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acda4ac2-6db7-3fd6-8a78-c1caefc2e196 | -12.69081 | -45.28587 | 2025-09-30 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de38e593-f1fd-3c57-bea8-690761cb27cf | -8.52506 | -44.66669 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4d68737-6b08-340d-ac7c-5e148437504b | -7.83172 | -46.99184 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff0aec7f-f3d2-33b2-97ae-ed0e03cd8fcb | -11.14749 | -54.11512 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc452e72-b868-37a2-9334-0f3c47e01d36 | -8.87772 | -46.6162 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b6679048-e300-38f2-828d-4b8e08816cbc | -9.41244 | -54.69212 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7ef4f3d-c50b-31bd-a5f9-fc6d4df19823 | -11.45998 | -45.01759 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 57135b13-cae4-3859-b1d9-eb4a4bbf74f9 | -13.59489 | -48.04684 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaccca57-b21b-338c-80ef-3e6b08de3d9b | -7.90975 | -44.62519 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffd12779-bfc2-3d2d-973f-f9680cfc80e7 | -11.6682 | -44.28804 | 2025-09-30 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d87afea8-17de-3526-87d8-6fdbba20dccb | -9.75801 | -47.19289 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24bb44f3-bc08-3d19-a6f7-61fa1054a7a1 | -11.97865 | -46.58091 | 2025-09-30 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b27acca-9f69-32e1-a78f-5953f5dad2f6 | -10.64213 | -53.68642 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69757157-5eab-30ad-8fe9-8893e09bbd2d | -7.91354 | -44.62701 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b0002e4e-bf51-39b4-ba9c-8950ae428a73 | -13.35236 | -47.84147 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2651e7f6-7013-3bbd-ac15-5cf08ff8883b | -7.86556 | -47.25783 | 2025-09-30 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfd4702e-5dcd-32d6-b365-f580e89cbd88 | -10.41045 | -48.16735 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef1062b6-9979-3dc0-90c1-c6a365e00eac | -10.8837 | -53.73649 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a7766cf-a916-30cf-9b43-255c6e64a3cd | -9.29519 | -54.5062 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12f92c4a-3e75-3c0f-9590-764da5692e40 | -11.88423 | -48.04863 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2d030a92-dfdd-31c3-99d2-b7cff4697800 | -7.05438 | -45.19361 | 2025-09-30 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0f98d95b-e388-399b-ac8d-d1a086968eff | -7.37086 | -47.04926 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdce3eb5-a1c2-3f62-873e-60f29f5184a5 | -13.58914 | -48.04887 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97ff4f65-d909-3501-a153-988f5560bc62 | -13.58339 | -48.05093 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 471cd24a-7dc3-3ddb-9788-6a22fbb8051d | -10.0821 | -50.2135 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 48519327-15e7-323d-8bed-058d1339c520 | -10.99776 | -57.06142 | 2025-09-30 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8037bf1c-318f-38d8-b1bd-ee1d05651849 | -10.19871 | -44.89961 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 764b0a91-f976-3d21-af96-899709927edf | -8.01732 | -55.41503 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1b841bc-959f-346f-a949-437cadd9eca8 | -11.20178 | -47.21886 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9081a2ee-451e-36cc-ba90-89296c4f6463 | -11.8834 | -48.05512 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ecc2a128-d7c2-3d9e-871f-f40a6e00a651 | -8.72093 | -47.99121 | 2025-09-30 05:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c81c0cb-cdc2-3d87-b0fa-baf1546094fa | -10.19117 | -44.88729 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 30b3533e-d0cf-354a-aaf7-41ecb683d2dd | -13.23684 | -48.44832 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37cef266-cd01-3a40-bd5c-171b11de0c67 | -13.37234 | -47.31192 | 2025-09-30 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb81451e-8126-3cdb-88fd-1f6f42dc52f3 | -10.96242 | -46.4856 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8125d27b-20ae-37a0-b290-2b58aba050bb | -13.59592 | -48.03847 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41f17ca0-667f-3135-81cd-f927d37b590e | -13.2185 | -47.32531 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d357719c-46e9-30ea-b924-4e971fc15034 | -10.0726 | -50.21662 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c0a6eabf-d8c6-3ed4-88a1-d61340796edc | -11.7096 | -44.43573 | 2025-09-30 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d95732b5-3853-3fbf-ae5b-9c3981c3dbfb | -13.65315 | -47.32743 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c988f1a-96c2-39dc-86a4-0e0ddabd950d | -13.40457 | -47.54336 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README92.md)
