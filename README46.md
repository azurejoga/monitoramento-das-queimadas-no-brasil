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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03d94559-ddc0-3f5a-a685-6e5614f7fe59 | -9.1626 | -46.65115 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b564463-73bc-3ae7-b35e-67d5e0d4bb7b | -8.65394 | -43.99137 | 2025-09-27 04:44:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c17b0b7-42bd-33a1-a9e4-24d0f5b891f5 | -6.06486 | -44.07716 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9c1345c-1540-3e38-a445-660e42d9858d | -3.40064 | -46.90153 | 2025-09-27 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 045b9f54-0802-30f2-a2ab-4838b964cd00 | -9.87032 | -45.90587 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70e76499-16f0-35bf-822a-cac2c087ce3b | -6.49346 | -43.28219 | 2025-09-27 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c722becf-c0d1-3e4d-bbf4-2a980687b32a | -6.4252 | -43.07772 | 2025-09-27 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9bbd8043-8a87-330d-9779-375ef8577a5f | -6.26889 | -42.49088 | 2025-09-27 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99c6c0e1-7be6-3aee-8c76-ecdfe43cac91 | -3.58354 | -49.4276 | 2025-09-27 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74fff648-992a-300c-849f-55d5b8ba52a7 | -8.83113 | -46.21632 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b2db1ca-732a-379c-b105-9736645d7b7a | -9.04245 | -45.53814 | 2025-09-27 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| edd806e9-9ce2-32ba-a4e7-8944fec00924 | -8.47583 | -47.82899 | 2025-09-27 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 630ab3c0-0309-3d08-8d64-17ad17d186cf | -6.31696 | -43.38731 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c28812e-6dcc-32e7-8e5b-c790578f4b79 | -8.26417 | -44.94259 | 2025-09-27 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78775f1b-b9c7-3c90-9193-90754f0533de | -4.62228 | -47.41616 | 2025-09-27 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 598bad33-3b27-373b-8a77-a5e75bf0f2ef | -6.70358 | -42.74113 | 2025-09-27 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 027f31af-938a-3558-b145-1dc989f9cecc | -5.73721 | -44.98225 | 2025-09-27 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3107719c-00c8-39d0-815f-7c5fcf6e558b | -6.26617 | -44.07798 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1460751f-0d72-3144-89a4-999c8fb7aaa5 | -3.82949 | -40.34222 | 2025-09-27 04:44:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c9567ad8-cb8a-32b8-9c1a-3f352a84818b | -2.55126 | -48.40542 | 2025-09-27 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af7b49e9-da1d-3794-9437-254ccdf6c181 | -5.80081 | -42.83421 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e3ac012f-9753-3b25-9692-a22c66c68a22 | -5.80242 | -42.82305 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3ad90b79-4d01-3a12-8590-f9914ea5a847 | -5.73489 | -42.65376 | 2025-09-27 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 35140124-2cd6-314f-8e1f-2f9e29959dfd | -8.65424 | -49.41167 | 2025-09-27 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aae661a3-190b-3957-8b31-2c4b36b79453 | -5.7967 | -42.82775 | 2025-09-27 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d86f0dc4-efb4-304e-8677-a207e10a89fb | -8.911 | -46.09835 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90f8281a-f476-3df8-9829-da1ad6e40a53 | -3.69277 | -49.18914 | 2025-09-27 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0ebae88-294c-3efd-a35d-77c0e5b4140a | -4.64824 | -50.97176 | 2025-09-27 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f80affed-9ead-3518-a061-af9c52ec9a29 | -5.72996 | -42.65262 | 2025-09-27 04:44:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 26d1f1e2-7cba-3e5d-957d-7a696ecedc02 | -10.03237 | -45.41768 | 2025-09-27 04:44:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2b70484-cc83-3f11-9338-18d9a5b10eb4 | -5.86374 | -47.26748 | 2025-09-27 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1c9bb9b-a123-351e-a91e-86f8a8ca9c15 | -3.23964 | -46.80555 | 2025-09-27 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ee78521-dfba-32a2-8f3c-68460b2cef8a | -5.67268 | -44.8579 | 2025-09-27 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c2ff271-ba75-3c1b-ac3c-ac2ee146c12d | -4.60743 | -43.10912 | 2025-09-27 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dcbb5b0-1c87-3ba9-b0bc-06946a0d7d40 | -9.97864 | -43.56785 | 2025-09-27 04:44:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bf6c982-72d5-3c3f-a905-8dc1acb4087e | -2.44716 | -49.0287 | 2025-09-27 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c6c8f7c-256b-3b3b-842f-124090f48926 | -3.45213 | -44.11997 | 2025-09-27 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 520f8894-e0bd-3221-996b-ce8259083604 | -6.2558 | -42.47318 | 2025-09-27 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 523ee2c3-b660-372e-84c3-5de98dbc0c84 | -3.69941 | -49.01572 | 2025-09-27 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df0d8d3c-dbf8-38fa-8b20-3c4d55f818a5 | -8.65366 | -49.41544 | 2025-09-27 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad2ab345-6361-3d9b-9f5f-a6de070c444a | -2.44935 | -49.01465 | 2025-09-27 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f87e3c5-a2e2-35b4-9b78-af2c61679809 | -6.99844 | -46.99319 | 2025-09-27 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c609840-9e0c-3dbe-b1ed-093c3b8b3b88 | -7.65108 | -43.82623 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ac22c95-64ed-3855-8811-f7cfa49d8202 | -8.72121 | -46.68568 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e29fb01f-2ba7-3cac-bc3f-30549330ab85 | -7.18857 | -41.70851 | 2025-09-27 04:44:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 29346b7d-f86a-36b9-be59-12758a9b90f3 | -6.94712 | -43.25389 | 2025-09-27 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 87e7d9a7-770c-3e21-8d16-f55b040a2d75 | -8.2635 | -44.9474 | 2025-09-27 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7c27717-6eb2-3e7d-86fc-6c44afe0ac45 | -7.71361 | -47.3051 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b6ba991-3c4a-31cc-bd9b-511bb7d00f03 | -8.66347 | -43.99257 | 2025-09-27 04:44:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d5d8997-48c3-3d97-bea9-658d7f08c849 | -9.04188 | -45.54224 | 2025-09-27 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87efed05-eccb-3602-8913-94a991fdc1b0 | -7.75957 | -46.88372 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9f46c8a-5aba-3e49-b60e-71d8ca80fd77 | -4.40124 | -44.08683 | 2025-09-27 04:44:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8738cdec-6979-3318-8424-544ef3fcf0d1 | -7.12066 | -42.18292 | 2025-09-27 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ae035bd6-d1fd-3a30-83db-f9150e4bbffb | -4.53462 | -48.64871 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a116e9ec-f593-362e-a8c0-3643180d24fc | -3.38556 | -50.40514 | 2025-09-27 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ad9e935-a09b-3663-9d08-94e459203ceb | -6.54085 | -43.83139 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5f0b0ee-b95a-394f-bce0-4b7ca61b1120 | -6.98911 | -42.39231 | 2025-09-27 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5941ca9f-e78b-395c-a60c-ab8a90a27662 | -6.5535 | -43.84248 | 2025-09-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be6e6ff4-300a-3e3f-8002-4c144b0d1422 | -5.7353 | -42.65095 | 2025-09-27 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50d15446-06d8-3618-adf1-31c4ae11dda9 | -5.4782 | -43.07529 | 2025-09-27 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e4641ff-1b02-30aa-bc62-b5ea1890624d | -5.74146 | -44.98282 | 2025-09-27 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9341032-de4a-3779-8a3f-df23ddc584ca | -6.24994 | -42.47786 | 2025-09-27 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f56cfa31-b1d7-3dd0-88d3-c08df265b52f | -4.38337 | -48.06735 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c2f62851-4281-3380-a02c-3ab58d70de1d | -1.16358 | -54.20876 | 2025-09-27 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5385713-8b2e-30b6-91f8-7f33a757c525 | -6.94792 | -43.24837 | 2025-09-27 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c490416c-8244-3638-96e8-745e53368c90 | -5.52066 | -43.86169 | 2025-09-27 04:44:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c36c6ebe-eae6-32c9-96a2-0e6eca534f20 | -8.05669 | -48.16232 | 2025-09-27 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf65112a-c396-3ff4-b9d5-16d29cd6d28a | -7.65448 | -48.21149 | 2025-09-27 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84dd59db-af6d-3814-a81c-a2052dd4e0ab | -4.99064 | -47.35962 | 2025-09-27 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 575cca83-b3a6-39dc-8481-7df5048b591b | -5.67325 | -44.85397 | 2025-09-27 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6662d756-b990-3ef4-a150-5d5877f81553 | -9.11277 | -45.8684 | 2025-09-27 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 734b35a7-df88-3ac0-b994-64c24ec6eddd | -7.67371 | -47.42015 | 2025-09-27 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27b23ef6-49b8-3694-bf43-8f18bb73334c | -6.31698 | -43.45657 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82216ae9-6664-3456-93de-d4a282de8cd0 | -3.83007 | -40.33838 | 2025-09-27 04:44:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a09e8cb8-1c9e-3ac8-94c0-505529073fc4 | -5.97662 | -43.24099 | 2025-09-27 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| adf96732-1549-3249-be10-736b0d6e5d06 | -7.71805 | -47.30107 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ae25437-5f42-30d9-ac0f-21b7ffcb8ccf | -2.96218 | -48.6014 | 2025-09-27 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b088d268-ea37-394b-b7b1-785eeff39a6c | -4.53121 | -48.64818 | 2025-09-27 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24c5761a-efb4-3456-9528-6c3d4bb16df6 | -9.05443 | -45.51522 | 2025-09-27 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e9711315-6c2c-3fb9-ba82-58885996db8d | -8.8244 | -46.26396 | 2025-09-27 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec639bae-ccbf-3b38-bc59-51d446b7bf44 | -6.31217 | -43.38664 | 2025-09-27 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d0e59ff-5e72-3ce7-99de-1a195caf128a | -7.62612 | -43.84153 | 2025-09-27 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1c6f3566-fd73-381d-9cb7-d9a7ec927b06 | -5.07873 | -44.84984 | 2025-09-27 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b7e0f48e-178b-36b5-8ba1-b460c9d5f43c | -5.73957 | -44.96652 | 2025-09-27 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aff27920-6d76-3b67-9bf4-3775c85287ac | -8.86214 | -46.61445 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcdb85bf-71af-3e93-a7eb-bff804a4daf0 | -3.80157 | -41.57019 | 2025-09-27 04:44:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 14e9d5e9-2116-3fdb-b715-30f8060b11f1 | -3.44714 | -44.12351 | 2025-09-27 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1d53fd6-4850-34f4-8694-1747ea68c491 | -5.0733 | -44.85718 | 2025-09-27 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 74ff22ca-792f-3f48-acab-e9c629b68f55 | -5.07389 | -44.85319 | 2025-09-27 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 56d0ebcb-07f2-3eab-8306-518765f5a23e | -4.48422 | -47.67111 | 2025-09-27 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78a525d0-fde0-3b7c-a977-c5e008326cc1 | -6.99656 | -42.3885 | 2025-09-27 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0aa57039-d52e-32f7-b877-13784598d329 | -7.37563 | -47.03172 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bac2a4b0-93cd-317d-b465-a05c7fbbfa74 | -3.52378 | -49.26731 | 2025-09-27 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 934df947-4b1d-3173-b189-2b6d95c29548 | -5.86005 | -47.26691 | 2025-09-27 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78a881a7-ac52-39d8-8403-1aceaef11259 | -6.4927 | -43.28747 | 2025-09-27 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dcd1a33-db02-31a7-a7ed-085005070214 | -7.18447 | -41.70792 | 2025-09-27 04:44:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4461a809-9523-35a7-baf1-a01d50114376 | -9.11589 | -45.87673 | 2025-09-27 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15d644c6-80c8-32d5-9f7f-3574a0b7fbd9 | -7.67305 | -47.42468 | 2025-09-27 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f203646-e13e-3a86-8d10-107aa6c66583 | -9.00393 | -47.83957 | 2025-09-27 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c1aaa35-27be-31a3-bfac-9e9643609f29 | -3.33229 | -50.24883 | 2025-09-27 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README47.md)
