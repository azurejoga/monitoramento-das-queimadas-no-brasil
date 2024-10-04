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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 929efb96-1e43-338d-a0df-2ae9cbc1f2af | -11.04526 | -42.01839 | 2024-10-04 04:32:00 | NPP-375D | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| da105489-e9c1-3dee-ae90-43d0428292a8 | -11.04072 | -42.01767 | 2024-10-04 04:32:00 | NPP-375D | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3429fc34-98aa-3ca2-86a9-b9798660231e | -11.28439 | -43.39396 | 2024-10-04 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36b5dc47-11d4-338d-bff8-1d61cc8d0342 | -8.16372 | -44.40399 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4c7256f-a0b2-3d22-8974-bfaaa2051dc8 | -4.46418 | -42.88522 | 2024-10-04 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 384544ed-0072-3587-ab94-6155be6ff726 | -4.45954 | -42.88955 | 2024-10-04 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4cc8cb8-4536-3fd3-b033-eb9796a17872 | -4.45564 | -42.88892 | 2024-10-04 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d50fa5ea-0a6d-3c19-a5c7-59b3fbdbe57a | -4.45173 | -42.88832 | 2024-10-04 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d354b3c9-82c9-3d07-8425-c055dd2ac6a7 | -4.44783 | -42.88774 | 2024-10-04 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4db76914-dfe6-3719-920a-2883eac743e2 | -4.82268 | -42.76185 | 2024-10-04 04:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a5eaa11-659e-35a0-93a0-18a21b83c457 | -4.81873 | -42.76123 | 2024-10-04 04:32:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f0948973-13c6-3050-9311-0d1d44f7736a | -4.81477 | -42.76061 | 2024-10-04 04:32:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e341deae-d963-371f-af0d-b9bb7c684a97 | -4.81401 | -42.76565 | 2024-10-04 04:32:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 00b4b6fc-62b7-3b32-945b-48ee2bf9b48e | -4.81006 | -42.76503 | 2024-10-04 04:32:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9df51967-3742-30e4-b32c-4c2edd897ffb | -4.8093 | -42.77008 | 2024-10-04 04:32:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e28d007c-8e5e-3507-b8d7-7f65fd9f6626 | -4.80611 | -42.76442 | 2024-10-04 04:32:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9655074d-901c-381b-bd6a-a92ddcdb1f45 | -4.80535 | -42.76945 | 2024-10-04 04:32:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6a99b4c-a215-31b2-8ec0-a4b0f25641fb | -6.17604 | -43.20672 | 2024-10-04 04:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 15b17316-9c7f-3781-aacb-05882887f841 | -6.17576 | -43.20916 | 2024-10-04 04:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1de0faca-7e59-35e4-89e4-6ac4046962bb | -6.17185 | -43.20853 | 2024-10-04 04:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 762cdb6c-e096-31d4-a17f-d5796cfa46bc | -6.17111 | -43.21341 | 2024-10-04 04:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 82565de3-c30b-3213-9f99-ebffc7fe6f1a | -6.01707 | -43.20414 | 2024-10-04 04:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 487a3bf6-f8c5-39ad-90d4-246aa8ac3c03 | -6.40973 | -43.43558 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08085329-1fc2-308d-a5f1-d2e9c6b44063 | -6.31524 | -43.42462 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98ba00e6-cdb7-3a5f-8f6a-be0728aaed1f | -6.3121 | -43.41912 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 315703e1-05ec-3732-8687-f4f989233f60 | -6.31137 | -43.42402 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 653fdb6b-de02-3452-99e4-80ab9667228f | -6.29759 | -43.43685 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ff072de-9c02-3cc3-929b-b0593fa4cba0 | -6.29688 | -43.44164 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ae68b34-895d-32b2-a270-3fa6c2a79796 | -6.29373 | -43.43624 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4eb87121-8e65-3b0b-b37a-1abdf63d6598 | -6.29302 | -43.44102 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33d1f174-5490-3e93-9b80-f903723c2837 | -6.2891 | -43.2542 | 2024-10-04 04:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a17d085d-9a4e-35e2-889d-a3f661d00c8b | -6.20582 | -43.2766 | 2024-10-04 04:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9409d017-677e-3bd4-8b1f-a4a1ca1916f9 | -5.59763 | -42.93497 | 2024-10-04 04:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 496f0e7b-855a-33a6-a0cc-a06ab1cfc2fb | -5.40819 | -42.9233 | 2024-10-04 04:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3e963697-860e-373e-9d47-6432e919c5c0 | -5.40744 | -42.92831 | 2024-10-04 04:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 487a759c-7e3d-31c6-9f39-620ea01e5827 | -5.40424 | -42.92271 | 2024-10-04 04:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e89aba44-8aa1-374a-a65f-64bea3f5279c | -5.4035 | -42.92773 | 2024-10-04 04:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e9394c3f-28c1-3383-ba1e-ecc3874c555b | -5.32134 | -42.97059 | 2024-10-04 04:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8d7b3a98-5eb1-317d-8843-98c3d1cc1fae | -5.32059 | -42.97558 | 2024-10-04 04:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5a78e792-3c29-3acb-8f34-b0362e47702e | -5.31741 | -42.97 | 2024-10-04 04:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 69ad8a28-9501-3462-8bf6-6b1d8945077d | -5.31666 | -42.97501 | 2024-10-04 04:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 72d4a165-d6e8-3f22-aded-099dda44200b | -5.31273 | -42.97444 | 2024-10-04 04:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 329d53d1-aba2-37d9-a4c6-732786f231b1 | -5.31031 | -41.78408 | 2024-10-04 04:32:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bf3bfde2-052d-3453-a0bc-473c40feaa43 | -5.30606 | -41.78349 | 2024-10-04 04:32:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 49b81312-d819-37f7-90b0-e5ca6ce33b76 | -5.39319 | -43.1043 | 2024-10-04 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 647d620f-de27-3b5c-aced-16cbf7174512 | -7.86523 | -43.07975 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ad24d288-ca85-3663-9c35-0cc1db8c8d00 | -7.86117 | -43.07925 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| eeb84b40-e60f-3824-845f-52fba61c2d84 | -7.79584 | -43.10225 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6c56ac46-e76f-37d3-a291-bc254548ece8 | -7.79181 | -43.10162 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 775315e1-285c-3ccf-9773-ada2327ed923 | -7.76408 | -43.06556 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4bf25f4b-9f3e-3581-9ada-2ebc6ad7ed53 | -7.75548 | -43.06789 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9c02afe8-61c0-3905-804d-620136f1affe | -7.75498 | -43.07135 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 67457f51-b8d8-3e71-aaf8-0212527c2bb3 | -7.75094 | -43.07076 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| b57a4721-6eae-34b1-9a80-776ce0d30420 | -7.74942 | -43.05265 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b21350fb-046a-39b9-b801-c471b9e667d7 | -7.74891 | -43.05618 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4094eeba-3d14-334a-ab8e-a3480ee7d090 | -7.7484 | -43.05971 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 26f0799e-c5e5-3210-a768-c0cba3e8e730 | -7.7479 | -43.06322 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6631dfdd-6ce0-3908-a91a-6b0215fb0ef3 | -7.7474 | -43.06671 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ab2f1a9c-4392-3da9-bc8a-e6e04727c72f | -7.7469 | -43.07016 | 2024-10-04 04:32:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f77b050c-20e5-31be-8fec-943ea2441fa7 | -7.692 | -42.98996 | 2024-10-04 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 15bb6fee-238b-31c2-90a7-2ebb2538a862 | -7.68846 | -42.98584 | 2024-10-04 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4f34dc93-0b60-3a72-adca-cae1141717f7 | -7.65831 | -42.4576 | 2024-10-04 04:32:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5d2df270-112f-3fe9-8126-d8aeeda9b9c2 | -7.29596 | -42.25355 | 2024-10-04 04:32:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c482352c-7fd9-351b-b4b1-29f59ec521b4 | -6.66529 | -42.10447 | 2024-10-04 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 54f84497-7537-33c0-ba6e-e4bb893465b5 | -6.64231 | -42.11339 | 2024-10-04 04:32:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6a259754-e4ae-3d77-aec3-1f9828a8ba20 | -7.99544 | -43.80091 | 2024-10-04 04:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf7059dd-da25-3851-b13a-5b6aa1105a7b | -9.25126 | -43.50629 | 2024-10-04 04:32:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 71745d1a-cb7a-386a-b50c-ad67173211d5 | -9.2484 | -43.49785 | 2024-10-04 04:32:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| acf873e6-3ddf-3939-a1fc-c823af407564 | -9.24789 | -43.50131 | 2024-10-04 04:32:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6c673759-71fc-3405-aba9-e12ca09b1964 | -9.15654 | -43.15829 | 2024-10-04 04:32:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 16e5a837-c094-3805-9c12-fe6111e3ff09 | -9.15603 | -43.1619 | 2024-10-04 04:32:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 336e7674-92c5-3313-8acc-23592d7098a0 | -9.15243 | -43.15776 | 2024-10-04 04:32:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a7ee84f0-be6d-3402-910d-a0478e80d9cf | -9.15192 | -43.16135 | 2024-10-04 04:32:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0e426780-a571-3aa8-bdcc-d5cbd98eb15a | -9.1514 | -43.16504 | 2024-10-04 04:32:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 21bb6f87-8669-3b1f-8fed-13ca557b85b7 | -9.14833 | -43.15723 | 2024-10-04 04:32:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5dabb1bc-f214-392d-9a99-17e17059030e | -9.14781 | -43.16085 | 2024-10-04 04:32:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 67af4985-d83f-3b8c-9e99-c3c85ad9a476 | -9.94855 | -44.02557 | 2024-10-04 04:32:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ba6ace3-4c46-39a8-a9e3-d56fdab1b562 | -9.47345 | -44.05564 | 2024-10-04 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec2cc856-248c-3abf-9c28-685c21011976 | -11.21708 | -43.32695 | 2024-10-04 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 41b6221e-6020-35fd-8abd-f54843e243cf | -11.21635 | -43.32821 | 2024-10-04 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| aeb8cc58-79a9-3dbf-a1b4-21b58c9d7f15 | -11.11173 | -43.33637 | 2024-10-04 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d71c9308-ed7e-3bc6-9ea1-13979132e7d3 | -11.10908 | -43.33497 | 2024-10-04 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c65b7319-3594-3f2a-b336-c7a58b06d416 | -11.10856 | -43.33883 | 2024-10-04 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 20263ddc-72c1-35f4-830a-449408eef863 | -4.54061 | -43.29902 | 2024-10-04 04:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0073660-9c7c-38ab-ace3-90ac29f58e76 | -4.53989 | -43.30366 | 2024-10-04 04:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34819079-1956-3ce1-a5bc-24972d43fc85 | -4.53679 | -43.29845 | 2024-10-04 04:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ad5cb030-94c0-3892-8725-2032dd7a3586 | -4.53608 | -43.30309 | 2024-10-04 04:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3efedfe6-22fa-3e4a-a213-8b598424846b | -4.53537 | -43.30771 | 2024-10-04 04:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 4fb40fae-144d-3139-b2f2-76a0d7145c2f | -4.53298 | -43.29787 | 2024-10-04 04:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6b59563d-2c0a-382a-a302-4003c2d375af | -4.53227 | -43.30251 | 2024-10-04 04:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c9c27003-43d2-39b1-a70b-6966487bb72f | -4.53156 | -43.30713 | 2024-10-04 04:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 3d0991aa-9eaf-3c97-a65b-6f6cc1e150bc | -4.52917 | -43.29729 | 2024-10-04 04:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7dca7d76-e737-3746-a22e-e34c37e8b670 | -4.50164 | -43.6297 | 2024-10-04 04:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68fb18a9-02f4-3aca-a6cb-e3c394261caa | -4.50071 | -43.63197 | 2024-10-04 04:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd03f92a-b9cd-3163-90a9-816128c1ed2a | -4.74093 | -44.09816 | 2024-10-04 04:32:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dace44c1-e090-38c5-b047-1234441815d8 | -4.93061 | -43.77342 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9800e21-a237-3189-b15d-e1242a2019e4 | -4.92995 | -43.77782 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d566ee28-8072-3cec-878f-47f728f71098 | -4.92688 | -43.77285 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a359433-340d-3160-a663-bfa6db8c2961 | -4.92623 | -43.77725 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b40a59b6-01e9-3c69-9936-8a7e3add7754 | -4.79882 | -43.78262 | 2024-10-04 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README96.md)
