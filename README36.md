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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ab7b96f-a5a7-3002-9d08-c6d13ee85066 | -15.2499 | -49.821301 | 2026-10-08 00:48:00 | METOP-C | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a7874f3a-0f49-35db-ab8d-a16b0bb25bbb | -3.2214 | -54.292 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8951f966-7f3f-38ae-aeac-a4d3e12b8fa8 | -3.1047 | -54.277401 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94773e8d-33b8-338c-ba40-f760508e87be | -3.3099 | -53.866299 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 438a791b-742d-384d-ad06-9057b20fab4e | -22.423 | -47.659901 | 2026-10-08 00:48:00 | METOP-C | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 80c2e35b-ef1d-37d5-a3a5-808420ef7384 | -1.4694 | -54.648201 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 907bb148-8d1d-323d-9a23-12e463e723cc | 1.7482 | -55.579399 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb4cafd0-fcf3-3fbf-af23-5b90a523775d | -3.0372 | -54.252102 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 217fba28-806f-3914-a5bb-56c5aef8f9b3 | -4.4562 | -47.930698 | 2026-10-08 00:48:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e19b509b-9f71-38d5-a280-4b3266f6bd83 | -2.6865 | -49.0508 | 2026-10-08 00:48:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c26cb83c-8dd8-3346-b32c-bdc065cb7786 | -3.8764 | -55.8246 | 2026-10-08 00:48:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10defd50-dfd0-37f2-9a70-185ee2fa0158 | -3.7338 | -59.447201 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78a1bd24-2f85-34b1-8e67-8a1c70504077 | -2.3863 | -56.1422 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc7999e-c847-3a0a-9f29-8e5784711736 | -7.4744 | -42.849602 | 2026-10-08 00:48:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5ac86af9-2e10-3c33-89b7-22024061efb1 | -2.7829 | -54.0853 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cc3c355-e192-3155-9e96-8600740472c9 | -3.0556 | -51.2248 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78124440-108e-3493-baf3-790792f7f7e7 | -9.1255 | -48.5187 | 2026-10-08 00:48:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b095d559-080e-3296-a4a1-194b448ca910 | -3.0752 | -54.147499 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90df1448-f0fb-3007-8626-16377d951595 | -3.5147 | -54.6325 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed9d00bf-3ca9-35a1-88c2-6894b091b4fc | -3.0666 | -54.245499 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 040e232e-92dc-334a-b07d-ecc6075ca764 | -3.5144 | -54.540199 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0f4b947-2484-3b9b-b447-f8918934b9c3 | -2.8026 | -54.081001 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0bfbb8b-649a-34c9-87ba-cb7f0cf88f48 | -3.1035 | -54.181198 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a59ec9b1-944f-396c-8d64-ac22407c434b | -3.5863 | -54.676102 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 072bb900-8914-301a-9bcf-23ccaf0825e5 | -2.4992 | -56.186401 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f76fa33b-835f-3b5c-b901-6c3f76aabdaf | -6.843 | -55.786701 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 391d9a67-d439-34ce-b32d-7cd65bfcef1c | -2.1252 | -54.814098 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dee855dd-7b9a-3169-820e-235d941274cc | -5.7034 | -53.478901 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 414150a9-e64e-379f-89d1-854604f4da87 | -3.0781 | -54.251099 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3b654e-b270-32cb-beb7-7eae6154f90c | -3.0932 | -53.7743 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac58527e-f138-34dc-9761-9daa37f33d87 | -6.3375 | -43.369598 | 2026-10-08 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45d8839a-111d-303d-b67a-02d57f8f8bbd | -6.1143 | -51.746799 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55c0b557-fe18-3d6f-bc81-b10ed18ce518 | -3.0596 | -54.214901 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d0c428d-473c-3c1b-a6b9-2173f3b09637 | -4.284 | -49.089901 | 2026-10-08 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27703a7f-33dd-313e-aa7f-96d37b225f52 | -2.5655 | -56.1618 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb4459e6-1b52-36ae-9fdc-54420921e73e | -3.0227 | -54.1432 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a348660-de57-3bbf-a5ae-9c4e5b324e8c | -1.4676 | -54.640499 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15948908-2b68-3c2b-97aa-3b026af92147 | -2.9339 | -54.1152 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f36fc624-51fe-316f-aba2-cd40deb5a3cc | -5.1191 | -47.112202 | 2026-10-08 00:48:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac8d2d70-6de3-3fa7-99bf-d48547cab054 | -3.2384 | -46.960899 | 2026-10-08 00:48:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bbb8194-aca5-3d39-835b-f55e6f5419f1 | -2.7702 | -54.119701 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 782c5b1d-62a1-3b32-99e5-923f06b0bda6 | -1.7956 | -57.1143 | 2026-10-08 00:48:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f5f9bc3-1efd-3231-94f2-e07a6eb0aa87 | -2.8418 | -54.0723 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 166ee354-6cce-31e4-86f9-7ffa51dfd2cd | -6.2141 | -53.278999 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5451204-3983-32dd-bbc5-b2ec7876608e | -9.8423 | -47.482498 | 2026-10-08 00:48:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8eb25002-ec2d-3141-b9ac-c660ac7a5327 | -11.0167 | -45.443199 | 2026-10-08 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c3fbb9a-b6d2-348b-8b3c-d59992f30a34 | -12.2014 | -48.4263 | 2026-10-08 00:48:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65adb25c-1477-3599-93bd-e321982a28e0 | -3.5392 | -59.4893 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d164b9e7-5bc8-3be4-a71a-9cc01fdb20aa | 1.6944 | -55.633499 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88900d4f-1453-3c0e-af1a-d60ba8f8e3a0 | -6.7283 | -55.125198 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc61415f-151a-3868-a0ce-fd0596b45db0 | -6.1578 | -39.438599 | 2026-10-08 00:48:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1f255cbd-df5c-39d8-a121-09c1d790591d | -6.245 | -52.867901 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9206e3ab-ab38-3e50-841d-1d0b08ba2689 | -6.8997 | -48.7131 | 2026-10-08 00:48:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 78902180-d4a3-361b-9e21-445c43ec272e | -3.0452 | -53.924999 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e55f2611-8a5d-3481-9f0a-78fcd50797ee | -6.1992 | -52.847401 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89b586eb-8a2e-35a8-bdde-197904f2753e | -3.0481 | -54.209499 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 663912fa-2867-3073-b4cf-4185a93cc656 | -5.6987 | -53.503799 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9360db8d-1464-3f71-99a2-bfcd463fc7f0 | -14.9261 | -48.111301 | 2026-10-08 00:48:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca514c8-2e76-313a-bf84-b8bcfaaa8a8a | -16.908199 | -40.8979 | 2026-10-08 00:48:00 | METOP-C | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03b6ab62-6aab-3d71-b8ff-be7ce0ea2dee | -3.3331 | -50.1926 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4871b824-1a96-372e-b52e-752def98d37f | -6.5774 | -53.018299 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d9ba531-ce38-302f-b5e9-adb9b51e6de5 | -13.799 | -52.7966 | 2026-10-08 00:48:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 28e79bd6-3932-31c4-a07a-82fcc73488e9 | -3.1111 | -53.7626 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e13455d-2602-3d3c-988f-0a2787cff6ae | -3.7003 | -50.665699 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a866b67d-d577-3781-9211-6881841a0fff | -9.2938 | -50.319302 | 2026-10-08 00:48:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3e24db1-927c-3f16-b392-e99233dec0c0 | -6.3278 | -43.372002 | 2026-10-08 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06ea6c8f-ef91-3c85-b86b-4a4698a64643 | -6.0311 | -51.743698 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7178ea48-207e-3be9-8691-e52f44ffbfd2 | -2.9974 | -54.077301 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c405b1cc-047f-30d7-b77d-4fbc0fcab961 | -4.3457 | -43.801201 | 2026-10-08 00:48:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 450db87c-719c-358d-ae84-de97f716bdfb | -5.6757 | -53.493 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c30f75ab-3f3a-3b97-a131-546dfe9cfb07 | -4.2452 | -50.747002 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9616547a-5217-35de-a2e9-7a1bf91946d2 | -6.5099 | -55.3908 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83ac4a7b-fa4c-37ab-9437-3fed9c485995 | -4.1191 | -54.0289 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbc6e1f6-2401-34f3-a396-aaec7800922a | -2.7586 | -54.114399 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6385a28c-4b74-3783-ab57-361b049f8ea6 | -1.3991 | -48.923 | 2026-10-08 00:48:00 | METOP-C | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa677ebe-3444-3d2d-9f65-18194ac8b748 | -18.379101 | -41.9524 | 2026-10-08 00:48:00 | METOP-C | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 891b08af-b085-3c7a-ba8b-27bf16ab9125 | -5.1801 | -45.338699 | 2026-10-08 00:48:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3fb2b32c-3e4d-3999-ae7c-7c4c9e2cfed2 | -3.2933 | -54.0196 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 758e0978-591c-32ae-9d28-4d53dca776f6 | -2.9558 | -54.166 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9095f68-5f70-3e4e-a9cb-281471759b53 | -3.2092 | -53.967201 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2deb6294-d305-35ac-b8f1-8d04de8e41c1 | -11.864 | -43.558998 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf6f8622-ac65-3076-a1fe-18afe2027d84 | -5.841 | -50.151798 | 2026-10-08 00:48:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dddca9a8-33ae-3efa-8984-f9a82aebd708 | -5.8555 | -53.4692 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a5a1ee5-e510-313c-ae50-765d6749b2cc | -3.2688 | -51.075699 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56b86f3f-b339-3b1e-9051-edc3beda12c0 | -2.8457 | -54.134701 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3482e494-e4a0-365a-baba-fbc30d416a83 | -3.5282 | -54.6465 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 439e6b6f-555f-3aa0-9734-3a267cb584f8 | -3.3236 | -58.158901 | 2026-10-08 00:48:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bfe31557-bd8b-3450-b94c-3f818c5b1286 | -3.5587 | -59.4851 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51a3479e-e1e9-3891-8717-112d1a3ae7f1 | -18.107 | -42.550598 | 2026-10-08 00:48:00 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 23399829-3d0c-3524-ab46-bc45b62cb5cf | -2.9807 | -54.049301 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c35565b-9d20-3fd2-9124-4a4099c648ee | -9.3072 | -46.451801 | 2026-10-08 00:48:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3e0c31e-6197-3d62-b546-1659458a5db8 | -2.4766 | -56.132099 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41bcab90-2da1-3805-8b25-ad18d8c4aea8 | -5.9575 | -55.3512 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a38d946-9635-38e9-8969-8ef350c4b7dc | -3.0996 | -53.757401 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 601dd0e9-a4e1-35a4-93e7-b87836b7eb5e | 0.7704 | -51.360401 | 2026-10-08 00:48:00 | METOP-C | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 28e92422-c58e-30f9-bc29-d6edef117651 | 1.758 | -55.5816 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41234af5-3024-3580-9940-b7cd6d9f7797 | -11.106 | -44.001301 | 2026-10-08 00:48:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f15f9f11-ffd6-3024-90cb-33288ba2b4e3 | -3.5398 | -54.652401 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac4da436-165d-30e4-8bb6-8b296b74a922 | -7.2174 | -55.1577 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4cc6fcb-a771-3562-9a86-3b06cedca45d | -3.4697 | -59.5895 | 2026-10-08 00:48:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README37.md)
