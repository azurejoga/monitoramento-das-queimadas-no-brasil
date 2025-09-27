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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1a27943-1830-3907-bbe5-bae0465e6d56 | -12.30117 | -47.2211 | 2025-09-27 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a726db0-f90a-35c5-85fe-5aa0e9af4a10 | -7.67561 | -47.42625 | 2025-09-27 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1573faa-aba9-3395-a486-4c6aacecf976 | -8.49682 | -47.85384 | 2025-09-27 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 797925d8-4b97-3180-9935-86f0d1a03e5d | -12.27997 | -44.05772 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e39b3226-f38f-320a-8cba-1a86f5985e28 | -13.32443 | -47.30526 | 2025-09-27 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3200105c-e652-3c1f-8e32-5c9b8bef970e | -13.16171 | -44.65252 | 2025-09-27 04:23:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bef62fc-d26a-3907-95f2-71cc8ddc146f | -9.97688 | -43.59752 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf1b1269-0b78-3820-9664-536dd6e96fc5 | -8.47538 | -47.82972 | 2025-09-27 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7f1ef5b-364f-3dc0-86dc-75484e42ab0f | -11.61441 | -45.41833 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1bf97e1-e761-3ec9-a47a-e31deae79ce3 | -11.99399 | -46.6111 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9c293c4-7a48-3f5d-89b1-381ccae5ad2c | -11.40902 | -44.91578 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7312a725-23ea-3fe5-900f-643c69e2934a | -12.02769 | -46.50728 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b1a0927-547c-31f4-9190-dc680993fe7b | -11.68065 | -44.42207 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ec19878-ce14-3dd9-9bcd-6a860496217a | -8.30361 | -47.03518 | 2025-09-27 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baa3ba6b-0049-35cd-9e44-389a5cb55481 | -11.38445 | -44.94123 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1df6c752-c8f3-366d-85e2-7bc25499a310 | -11.61371 | -44.40469 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69698b3b-e80a-3d6f-9ebb-40277dc09d95 | -10.59538 | -48.50128 | 2025-09-27 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8fac6cf-ef7a-3f25-b8dd-6eeaed17c7d9 | -7.67589 | -47.42525 | 2025-09-27 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc0095f1-1bc1-30e0-a977-3df8546e0f86 | -11.36104 | -45.00364 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7960cc72-b344-3ec6-9225-fb836498e453 | -11.97641 | -47.88147 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7503a8f4-9b99-313c-bd68-f9b4de8ecaa8 | -10.18184 | -49.51393 | 2025-09-27 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db1953df-1005-3b4e-b88c-56d05db1b5fb | -9.89767 | -47.69538 | 2025-09-27 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6168dc8e-6b85-3572-9124-812ad315b8dc | -12.55559 | -45.84153 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 07970eda-e528-3b07-8117-74e971d2570f | -9.97631 | -43.60129 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b76286a-5684-36d8-8d09-9a6c43e259a6 | -10.17847 | -46.93317 | 2025-09-27 04:23:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4ca51ce-f00c-35d9-ad69-ba2848601abd | -8.32079 | -47.03796 | 2025-09-27 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e181fc4-0e1e-3456-b040-4abf5e2306ef | -8.20253 | -44.40594 | 2025-09-27 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd724ce8-ad70-3e47-add4-af07e3195a6a | -11.705 | -44.46735 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4502c03-817e-36af-8ab4-b76421c8d0ad | -12.85393 | -47.6247 | 2025-09-27 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aee84498-26aa-3943-8da7-a56b32979153 | -8.82933 | -46.22053 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 309498ce-c59e-3cab-8096-c925ec48e124 | -12.28922 | -45.64664 | 2025-09-27 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c901647f-f7e6-3de1-813f-762dc1ba95fe | -8.4768 | -47.82699 | 2025-09-27 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cee7cb6b-3824-329c-84a0-561d2ff8365b | -9.97287 | -43.60075 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 402f8442-bfae-3311-86d3-03e67e0353f8 | -8.47745 | -47.82299 | 2025-09-27 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9b91b50-b79c-36ca-8960-9ba7c7873ad7 | -7.37864 | -47.03175 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 87a54521-4e38-306c-83d7-4e304e50536c | -11.29014 | -47.81148 | 2025-09-27 04:23:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71ed430f-5157-3011-9d2f-2ab02e5acd8b | -8.71958 | -47.99177 | 2025-09-27 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd634562-8538-3623-83f0-f70a310fc3b6 | -10.23474 | -50.25286 | 2025-09-27 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1e7c5b8d-7cd1-325d-9764-145c92552bdb | -11.61721 | -44.40456 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 691e4bfa-ab42-348b-883c-0d9aacbc8a35 | -11.43051 | -44.98873 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c24b09f-0879-3e90-9cbb-3ee0271ccc9f | -10.97296 | -49.57074 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a0ff952-6b24-33b5-9927-f142ad6f3464 | -11.68349 | -44.44891 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89b59e36-245d-3662-9975-1ca086c211c2 | -12.30484 | -44.3508 | 2025-09-27 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4137b962-76bc-367d-99ff-cee3bd9e72ae | -9.94238 | -48.49842 | 2025-09-27 04:23:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4384400c-2885-3c9a-8b60-6c677d21524e | -11.68406 | -44.44522 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd1cdad7-430e-32d8-a0f8-4bfe13f0cd78 | -8.82876 | -46.22408 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a19a5c-fa4b-3bd5-bc8e-5983b67f5dfd | -7.52872 | -47.28731 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 538ca036-b451-3147-b897-17faadfee3dd | -10.90211 | -43.62555 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed40aa0f-d1cc-3b5c-a216-ce9f8c97f482 | -11.97609 | -47.90483 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7795fa3-7774-3809-ae52-40de6d43e8ff | -11.43608 | -44.97482 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d583a156-a975-3eb5-aa6f-281867cf66b3 | -8.72025 | -47.98773 | 2025-09-27 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 243abea5-77e7-3e97-abda-6554dcc6495f | -11.79156 | -44.92798 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e3ea552-e41f-3032-9097-5218b5eb7632 | -11.7778 | -43.75872 | 2025-09-27 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 229da1da-8500-319a-9ef5-7c96187773b2 | -7.80565 | -46.96019 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03e493c5-d8b5-3901-8e92-7a9b7356205e | -10.11009 | -45.30847 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aba52041-c8f0-3279-a20b-eaa952589001 | -11.36162 | -45.02201 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3298605-8109-3935-b37a-faa9ce8e26f8 | -12.05595 | -48.77018 | 2025-09-27 04:23:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd6dca9d-a167-3c51-a860-e45726eddff1 | -11.42859 | -44.92257 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eec82f15-0d81-3ef8-bdc6-caf3ff2c3b83 | -8.90962 | -46.09526 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77f321e6-e7a4-374a-a836-e20f422ea927 | -11.69651 | -44.45472 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6c96b15-8be1-38c9-a9fd-a216ab8edac4 | -10.11677 | -45.3311 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d762201f-170e-38ed-918e-d6215f341044 | -10.04909 | -49.20081 | 2025-09-27 04:23:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39fa5e89-9897-3213-90b3-7d1c592ccb38 | -11.6931 | -44.40894 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a7aa439-0ad6-319b-b33e-98b426058410 | -9.03534 | -45.52081 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d23e28a-aa1f-30de-9fee-a381ba6fe271 | -11.37109 | -45.00523 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55258141-bf8f-3f9e-b3ce-c10bb64e96f9 | -11.66519 | -44.29473 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54667223-1d73-35c3-8e74-1e317ea5d688 | -11.43384 | -44.96711 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64c5ded0-f56f-3c01-879d-52b0cf3bbf41 | -11.78127 | -43.75926 | 2025-09-27 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a675b44f-8c1f-3c84-b096-c80670ac20cd | -7.85504 | -49.64121 | 2025-09-27 04:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90e96e65-885a-313d-88cb-84375f7971b6 | -12.0114 | -47.88332 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 560c6b58-bdcc-3bbb-9859-0e1d536a7b23 | -11.99619 | -46.61878 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2355c401-fd75-32cb-8a1c-c8930a6978ef | -11.68859 | -44.461 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee24fec7-f601-36f1-a9d4-09cf0b6e56d9 | -11.97453 | -47.89288 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 796cb7be-6fc5-3aa4-9170-b3225337fcd1 | -7.78057 | -46.94078 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09150361-c3b1-3b2c-bb75-c6847b6458aa | -10.25707 | -50.24118 | 2025-09-27 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 747fb5ba-67bd-369a-aaff-90fbb0627536 | -12.10171 | -44.31219 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88365a7f-c932-3a26-b83c-c2629543e88f | -11.68629 | -44.3852 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18bcce21-6584-30d3-8694-cd4562c1dac7 | -11.97797 | -47.89346 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bb4c6db-f7a4-3b88-949e-ad629c3822df | -10.94217 | -44.30581 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5af8419e-bf8c-3bd8-9419-b6af2dea40dd | -8.0503 | -47.17274 | 2025-09-27 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a13c4416-31dc-3e00-b8ed-66c07a682c6a | -7.8783 | -44.01833 | 2025-09-27 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eff0196e-b0da-34cc-b9f4-effae5227010 | -10.00275 | -44.17657 | 2025-09-27 04:23:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caf67c24-4432-3d8d-8da6-d36fa4ca0640 | -10.12287 | -45.33567 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b1ebe266-d283-3443-a960-a4ae4f05e760 | -7.87494 | -44.01781 | 2025-09-27 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee4c7dcf-f4b8-3b0e-980b-bdcdc5d70671 | -11.66993 | -44.46936 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34e40f00-c6e2-3029-a9e4-0cef32336708 | -9.55852 | -47.69678 | 2025-09-27 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32b6f46e-4493-3a43-a70e-2287d4e184c9 | -7.63986 | -46.77745 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fad59a8-c86a-3e03-992a-942046ffcc76 | -8.81357 | -46.25448 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90bb3eb0-7648-3387-afb0-f8499536e975 | -9.11337 | -45.88195 | 2025-09-27 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 781cbf09-b925-3bd0-afab-5d44dc2ba97d | -10.59541 | -44.06448 | 2025-09-27 04:23:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fbeec2f-6e9b-3385-aa9c-16f3d30bbd09 | -11.50616 | -47.75028 | 2025-09-27 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ac6cab5-df11-36fc-8a03-3ffda8031309 | -10.23649 | -43.9495 | 2025-09-27 04:23:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89326713-4f3c-36eb-bdd3-352c8e8f077a | -9.04255 | -45.53989 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91f5c54f-4cad-3c72-971e-5209421695c3 | -11.96899 | -46.59605 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dc83489-cb86-37ee-8ef5-de9d27c9bc05 | -11.78366 | -44.8674 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16fdba64-76c2-3c26-8ea7-dd978c75b0ee | -12.29065 | -45.65018 | 2025-09-27 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 660410b1-e651-397e-8ecd-31aee49d402c | -8.30582 | -47.04322 | 2025-09-27 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5db7848f-f874-3dea-a573-7993ab595419 | -9.04809 | -45.50491 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bafbf75c-b16e-3743-9bf4-9181b0aed47d | -11.9714 | -47.91183 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 727a22e4-d18e-3cd8-ab66-c247e559d0b6 | -8.86111 | -46.61198 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README38.md)
