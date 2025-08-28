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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72767ece-353a-33b7-aa68-8f1ff6e13b2d | -6.76505 | -44.82222 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b8fb8b7-75e6-38fe-abe7-87205b812ed0 | -6.43981 | -44.56526 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| caf5446a-dc74-3e1d-bbf6-b8dec03a0ef0 | -7.35324 | -57.62659 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0554a94d-2a2a-3307-9638-d89917ad676b | -9.45229 | -51.95918 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37ac1a71-6cd2-30b0-8e56-d42acab051dd | -3.40491 | -52.72825 | 2025-08-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0ef35cf-9f59-3e0a-bfa3-bff7d2a6e289 | -9.07514 | -49.56979 | 2025-08-28 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68b0dfa0-e9cb-3794-a4b5-3162031d88cb | -6.01189 | -57.84902 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9286039c-270a-3552-b98e-3f257dd48b09 | -3.23473 | -43.44106 | 2025-08-28 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2a0eeed3-8215-3d62-8c20-53f1a9be4eb2 | -6.44535 | -44.56631 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6b60beec-a0ef-38ad-8fb3-fb2bca0609a5 | -3.24034 | -50.11384 | 2025-08-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b2ae406-d6d8-3420-b416-3db0a02159ee | -6.76459 | -44.82553 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bd9384e-a3d9-3ac6-b378-c6097dcf1a08 | -5.53007 | -51.44437 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6421b90-a2c9-3a8a-ba21-0d929552eede | -3.75857 | -54.81701 | 2025-08-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 84bad6af-d1d2-3886-b5ad-cd3424f9f73d | -4.24908 | -54.91959 | 2025-08-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65ce2387-a9b6-3068-8b4b-30a5b6a9ca1f | -7.44705 | -57.62891 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64a0975a-e442-3725-9599-01c629457946 | -7.27833 | -60.2921 | 2025-08-28 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 821de421-f5a7-36dd-8c3f-f1da8dd39a0b | -7.74556 | -50.27549 | 2025-08-28 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 490eb127-8197-339a-9dc8-6f28d74a155a | -7.5414 | -63.84545 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32b2c87a-b408-3623-b796-7e699bad2ef7 | -4.7621 | -46.80664 | 2025-08-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d19b5bd-3472-329a-9559-00f01f15282f | -9.96363 | -46.50842 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9efc28d6-b13f-30e8-bd4a-1f00adac7e9c | -7.47425 | -59.90557 | 2025-08-28 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffc26ec3-0706-3e01-b956-4ccf9ac1da1c | -6.91517 | -62.93454 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bee3900f-32c6-3fdb-96e0-259c10aa268f | -8.70777 | -50.38526 | 2025-08-28 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1499c4e-ac61-3de1-b93d-72784cc6ed6b | -4.08165 | -47.94915 | 2025-08-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5147f67-561e-3be3-97d4-6bf0e59d55fb | -4.96125 | -55.80984 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9aa7617-d631-314a-a8ea-8ada3aa2cf0e | -8.28028 | -45.18837 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bf530a6d-2bbf-3c4a-98e3-4a24adccdc48 | -7.55323 | -63.84064 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9464055c-b699-34f5-9c2b-f989e76094ce | -8.2827 | -45.16988 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 5ed20488-689c-3052-b570-f77e4d0886f7 | -9.44535 | -49.45101 | 2025-08-28 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09d0549e-bc6d-3770-a53e-6f10cc7443e7 | -3.75801 | -54.82054 | 2025-08-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9f61b8ea-d90b-3d7a-b277-8f3c75adfcaa | -6.90905 | -62.9396 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74d95d73-cbcc-3712-a0db-9aeaca08b3c9 | -4.08485 | -48.04685 | 2025-08-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f03f0aee-a71c-39f1-a5cc-ea8817e75cd4 | -3.76246 | -54.81399 | 2025-08-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 39fc9eca-a297-31af-b9e1-cf642f55ae4f | -5.19885 | -46.06383 | 2025-08-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 088c86bd-ab2c-383f-aaa6-61aaef0c25fc | -5.77556 | -44.92619 | 2025-08-28 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebe052b6-d5c3-36b0-b2ce-e931728a0113 | -6.28344 | -44.4795 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23edc30f-25fd-37a0-8964-97378fd95d98 | -7.19533 | -44.06366 | 2025-08-28 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44fb26be-873b-3a25-9317-33a352c2889f | -3.59583 | -49.45272 | 2025-08-28 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76d19e58-f7d9-327f-99a4-e474f0535b60 | -6.59432 | -45.97001 | 2025-08-28 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11d76687-d090-3cd9-ab2f-6c42bece0cec | -8.2994 | -45.1282 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 607e4d73-5e3b-366b-9251-2a544ee1c472 | -7.55858 | -47.49374 | 2025-08-28 04:57:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4bf04ed7-41bd-3ae7-9f06-b900ac7f9262 | -6.13346 | -44.41943 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26412ab8-d039-3b03-af50-f6debff64e60 | -5.94525 | -51.83389 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 160c7c3f-008a-338a-9c07-325b8e2b8fa6 | -8.29016 | -45.15572 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7b55bfc-0ed4-3da4-82cc-81d5cb8aeeee | -4.7876 | -47.27071 | 2025-08-28 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b43f95fd-bae3-3365-a6d5-3c04f0b018c9 | -9.0527 | -54.94222 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 54419fac-991e-394b-8758-5a6893608c29 | -5.83101 | -44.10118 | 2025-08-28 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2bd86713-a691-3a69-9acf-77690fd3e7a7 | -2.92837 | -53.68976 | 2025-08-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a56b38e-84df-3436-9f59-3fb0ecfb5617 | -5.20299 | -46.07014 | 2025-08-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 11e97bb8-fea1-3b9d-92f8-b6d278d37d95 | -6.228 | -43.35976 | 2025-08-28 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c457ee0-9a9d-3590-be03-8ceebfd993c1 | -8.28222 | -45.1736 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 7c122db4-7690-3896-adc7-9f88dc6ef4d9 | -8.44217 | -43.68676 | 2025-08-28 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4ba5564-780b-3718-990f-7aa9576539c8 | -9.28623 | -48.82421 | 2025-08-28 04:57:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a76d344-d01f-3f4d-a49c-75958b37869b | -7.7435 | -50.27861 | 2025-08-28 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e5040f4-5485-387f-87b4-c9bfb08c86c4 | -3.23412 | -43.44509 | 2025-08-28 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f2e3ab1d-9fc4-3228-b7e9-9eb2efe16e71 | -8.29568 | -45.15641 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3d644215-89f8-3fa8-85a2-305c82605be2 | -9.63836 | -49.76286 | 2025-08-28 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97d43b33-fbd0-3dd4-a0c0-b3c6b0c1244d | -6.71919 | -43.09414 | 2025-08-28 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 529dd7ce-ad36-34df-ab38-535147399462 | -6.19253 | -44.15702 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3108b211-9e58-3c9f-9193-0b74940daa01 | -6.881 | -43.62143 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ae68df3c-7076-3b36-b21f-4733b4c00fb2 | -5.99644 | -57.8511 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81acdd94-ecf8-3001-8248-e22c502fa40f | -4.79799 | -47.26287 | 2025-08-28 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 0a992fb4-5e3d-31b6-9841-40d9d82905c4 | -8.86109 | -47.15848 | 2025-08-28 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e235109-6021-312b-89ae-b4a58a2e2e6a | -6.15332 | -55.80362 | 2025-08-28 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08ed7d66-5513-314d-aa63-03f20300839d | -6.86967 | -43.61512 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f2a27c7-f95a-3ca0-b330-cae4d46c1895 | -9.45166 | -51.96342 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c22b90f7-ac61-3509-bd4a-c493b1155e73 | -9.63783 | -49.76657 | 2025-08-28 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e67285dd-2225-3894-82e7-a7e4ca87412a | -6.91411 | -62.94046 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7662336c-7d9c-332b-96db-c99d0f232b0a | -6.00013 | -57.85167 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c01f939-3eb9-304c-a72a-dc9410a06b1d | -4.96406 | -55.81403 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c3bb861-9ca8-3047-8753-22d7fba79cc0 | -3.2307 | -43.43956 | 2025-08-28 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8fcf322-0c99-3c26-b553-eda0480939dc | -2.91891 | -48.30972 | 2025-08-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df83f100-81b6-3bf3-adbb-8079fb39823d | -5.33264 | -48.98999 | 2025-08-28 04:57:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d8a40b8-a09c-3a18-baf5-a02dbc2213c0 | -5.19805 | -46.06937 | 2025-08-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2ab71dcb-0714-3c14-8e60-3127c6fd2e34 | -5.5318 | -51.99548 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3971204c-1ccf-3b24-84ba-bfb53a5fa842 | -8.44691 | -43.65841 | 2025-08-28 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d592f9a-8c19-3e83-b20e-4437c9b71b70 | -3.76469 | -54.82156 | 2025-08-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0eb7ebe4-8a3b-376a-af65-b7d64a109639 | -6.87198 | -43.59756 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 452ec2e3-31bd-3eb2-8837-f1893d5a4fbe | -5.23032 | -46.09022 | 2025-08-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18e51cf2-5332-3bec-a128-82ff8990bcba | -4.79281 | -47.2667 | 2025-08-28 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f94ec1c9-4a97-3174-babe-42cc8a9c2935 | -6.94325 | -44.08745 | 2025-08-28 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a79cc7c0-bbc9-31e6-9212-47febdc586ea | -9.66928 | -48.31641 | 2025-08-28 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 246959e8-0bbe-3d6c-a08a-39b5804246e0 | -6.222 | -43.35875 | 2025-08-28 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74f3e954-cf03-32f9-ae95-e6fb9d562fdf | -8.09012 | -45.00951 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0428d597-c302-3cac-be6f-34b1c76a6444 | -7.35748 | -57.62308 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d85bcafe-bc45-38a1-9acb-a67b1b16f606 | -6.9197 | -62.93838 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd20c886-6d3a-34b5-896f-8fd8fc191dbd | -3.85693 | -54.08233 | 2025-08-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57deb6f3-5a56-35f8-9330-5555712fa258 | -8.90205 | -47.32782 | 2025-08-28 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f1097a1-d5c1-3ead-827f-b17b4c0bcd4a | -7.06437 | -44.36972 | 2025-08-28 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17a411a6-88cd-36b1-b671-36179a8fde45 | -5.90008 | -45.56292 | 2025-08-28 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca92c97f-5b5a-3e80-af9e-3a1ab923ba57 | -6.59474 | -45.967 | 2025-08-28 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d508ba0d-695e-3003-a7f0-2fb6e1ffd4dd | -3.09876 | -54.59843 | 2025-08-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80151aca-8a0a-36e6-969e-42573968beeb | -8.29893 | -45.13179 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07642cb3-73f0-3d04-8eeb-95048ab95420 | -8.09062 | -45.00577 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74d56e9e-d0b1-3f8a-842d-f1b9eba213a3 | -4.48527 | -55.55564 | 2025-08-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18444c3e-3afe-3c5d-a136-fbf0d5fb0194 | -5.64766 | -45.26081 | 2025-08-28 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2acd618-a67a-346f-a2af-9990a1bd7175 | -7.20167 | -44.0605 | 2025-08-28 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41979c32-0a45-3dcd-8d76-97c2a422f000 | -8.29183 | -47.21467 | 2025-08-28 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbe21866-3eec-39e0-9698-18cf0ffd1c0a | -8.38715 | -44.97133 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be7667c8-73eb-36a5-a113-4d7a4c4fb93a | -9.67436 | -48.31298 | 2025-08-28 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README52.md)
