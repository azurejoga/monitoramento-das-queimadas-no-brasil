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

## Dados Diários - Página 213

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e91378dd-dbf6-3af9-b0db-47c931563f65 | -9.9018 | -44.7917 | 2026-10-08 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 885765ab-a1c6-3c5f-8623-4ba364ed7d18 | -11.3937 | -46.6922 | 2026-10-08 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 27f6a79c-75a6-3fb1-9043-42df36fae64c | -11.2486 | -46.2377 | 2026-10-08 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 0612ba01-f699-3986-9142-720e6d5ca44d | -11.9832 | -57.5867 | 2026-10-08 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| b853f678-d346-3fa3-8717-2e0e5e83e0d9 | -13.1639 | -54.3385 | 2026-10-08 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| cd013001-639c-38c4-8b9a-a22986e92336 | -12.0448 | -43.434 | 2026-10-08 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| a08b0425-6286-323f-b50a-93587f660143 | -13.3865 | -43.8708 | 2026-10-08 14:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| c72ba32e-7f89-3c85-a42c-0148def70985 | -15.5216 | -42.6588 | 2026-10-08 14:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 456.0 |
| 8b47e1b2-46eb-37cf-a6ea-4feb6078e959 | -11.3347 | -51.8884 | 2026-10-08 14:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b45507c9-4218-33ff-968c-6e580e808e34 | -7.7784 | -43.8073 | 2026-10-08 14:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 45f3ebaf-945b-35e0-bfe3-75522292e6e8 | -11.2661 | -45.1859 | 2026-10-08 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| c334883f-b1c5-3b18-925b-41433da3149f | -9.475 | -64.3525 | 2026-10-08 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| dce418aa-153b-39cd-8419-0cb9bfa42e0b | -8.6107 | -67.0116 | 2026-10-08 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 5ec3650e-5af2-3969-a336-a8c512b3e2a8 | -11.6177 | -43.6906 | 2026-10-08 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| b540edfd-b5db-3e2a-a116-8de02677936f | -6.7366 | -55.1274 | 2026-10-08 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 891eb7a0-d343-3e08-b510-327134311349 | -12.2316 | -44.7427 | 2026-10-08 14:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 564e18ea-a17f-34a0-a580-133eae22dd8b | -15.5222 | -42.6342 | 2026-10-08 14:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 512.4 |
| 976357c1-4e47-3399-9012-64b1487382c4 | -7.8876 | -55.0023 | 2026-10-08 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 2e734ba0-3cb7-325e-8fb9-8fd4bf5fbdee | -11.6369 | -43.6876 | 2026-10-08 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 347.4 |
| 5b2a40ba-3509-3c69-ba68-d526c3165f6a | -11.3536 | -51.8864 | 2026-10-08 14:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| d0f266ac-cc35-34d4-864f-43d372e72e15 | -8.1876 | -54.7219 | 2026-10-08 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 54d8093a-b3cb-3926-a275-657ab35ba54b | -10.4337 | -47.2824 | 2026-10-08 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 205.0 |
| e86de421-fe1a-3f17-8200-eff0a2c125d3 | -7.5284 | -45.8885 | 2026-10-08 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 33c81daf-93ce-32d1-95f6-afe1252d28f8 | -1.0993 | -48.0561 | 2026-10-08 14:00:00 | GOES-19 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 4e35ede3-25e4-36a7-af4c-b5d3be10b3e5 | -6.4568 | -55.4609 | 2026-10-08 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 37e926cb-96d4-3638-bfc4-40be1d5ec199 | -9.4936 | -64.3518 | 2026-10-08 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 5ca520ab-31e4-3254-8697-8622608cc0c3 | -13.1833 | -54.3158 | 2026-10-08 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 295.4 |
| 54664f3f-042c-39de-a6ef-3d4e7f1f9fc1 | -12.1545 | -44.7547 | 2026-10-08 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 229.9 |
| 9565e43a-5cfd-319a-aa01-06017030a2a7 | -11.6374 | -43.664 | 2026-10-08 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| ed90dd4f-2910-3fc2-bcb4-8917a0e517e1 | -6.3283 | -55.3276 | 2026-10-08 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e5a28c01-45e8-3254-8696-fb9a21dd77f1 | 3.0733 | -60.557 | 2026-10-08 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 79.7 |
| bc0b81a7-ff3b-3de5-9f24-7239a85ede1d | -7.4697 | -42.8315 | 2026-10-08 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 18baee2c-55c6-33cf-9d5f-fe01e627380c | -15.5743 | -44.5235 | 2026-10-08 14:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 341.5 |
| 2b4a5249-e00e-3d3c-bd74-1c266389dac1 | -8.9501 | -45.1334 | 2026-10-08 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 772.3 |
| c9982003-b37a-368b-9957-21c64938f3d6 | -6.7368 | -55.1074 | 2026-10-08 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 571b6e2f-ff12-3939-b0c6-ad2605b0e3ab | -11.8404 | -47.372 | 2026-10-08 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 05fddb14-5a85-3a70-b21e-fb481aee9958 | -13.3671 | -43.8742 | 2026-10-08 14:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 27d2daa0-8c69-379e-834f-2d84c1594e08 | 3.1463 | -60.5937 | 2026-10-08 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| fcb86d0d-e3c4-3189-96ef-ff25652624d4 | -12.1738 | -44.7517 | 2026-10-08 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 214.2 |
| 0501d56a-19c6-3aa7-84be-0ee91c47a35c | -8.0578 | -45.6131 | 2026-10-08 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 3d23937c-b561-3f33-b594-f6a4474d6dec | -7.2371 | -55.1005 | 2026-10-08 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 4edaa408-4467-385a-b9d4-d699be664526 | -6.8289 | -39.5722 | 2026-10-08 14:10:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 67.4 |
| c1bf2a0a-06e1-3dfa-bb03-d1e3b009921a | -15.5222 | -42.6342 | 2026-10-08 14:10:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 599.6 |
| b6d2704c-080c-3a06-8db6-2f6aa5490fb7 | -6.8762 | -43.7083 | 2026-10-08 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 2c24ef92-8fe6-3083-a35b-720cd0ff54dc | 1.6937 | -55.6461 | 2026-10-08 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| c664e1e0-3abf-33f3-a064-e1c874897974 | 2.7641 | -60.0106 | 2026-10-08 14:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 03241231-0a58-38ad-9f4a-fe92d45d7cde | -8.5426 | -54.5975 | 2026-10-08 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0d777e93-86bf-35a3-9fd8-bbf66089e84d | -10.6912 | -47.8278 | 2026-10-08 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 213.2 |
| 2a0ecf33-c07b-34f7-978d-9c004df1aa2f | 2.7458 | -60.0109 | 2026-10-08 14:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 1ed460b3-29a2-3eb5-8f86-528d8ede18a2 | -8.5841 | -45.6955 | 2026-10-08 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 8a217e8d-21e3-311b-a0ef-40f2ef4a54ab | -6.9331 | -43.6566 | 2026-10-08 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| c4f57962-65ba-3939-8e1c-a9c5bba4358f | -8.2181 | -46.362 | 2026-10-08 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b6ad13e4-c820-3db2-9e5a-d27eceb66ed7 | -6.7366 | -55.1274 | 2026-10-08 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 3d7eb9f2-5cf6-329f-bd9a-23e52288ed75 | -8.9082 | -49.986 | 2026-10-08 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b9993c6e-d97a-38b8-b006-5d84614df45c | -10.4334 | -47.3046 | 2026-10-08 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| ee1d848b-ede4-351d-bac0-048f1456a68f | -10.6722 | -47.83 | 2026-10-08 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| e9a3997c-226e-3724-a841-147451f6a781 | -9.0591 | -65.9396 | 2026-10-08 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0e59c666-e5ca-3e13-a098-a4c5e00cf11d | -9.9018 | -44.7917 | 2026-10-08 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| d47145f1-0142-3b2e-b967-c401d5a5fb3a | 3.0733 | -60.576 | 2026-10-08 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ce34650c-c4d9-3fe7-bbf9-046162da3945 | -15.5743 | -44.5235 | 2026-10-08 14:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 281.4 |
| 5711cdc2-6f96-3a59-a450-01167866565d | -7.2184 | -55.1216 | 2026-10-08 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| ab0e628b-ab6a-3a23-8e23-c44275cb3a31 | -7.3472 | -50.8301 | 2026-10-08 14:10:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4cbe9c93-d040-357d-a5e2-2d9879b7efe1 | -11.983 | -57.6066 | 2026-10-08 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 75fc262b-9150-32a0-b071-9be8feeafb3b | -11.2482 | -46.2604 | 2026-10-08 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| dea4d5f9-3cca-3262-97bd-460a8cede6f9 | -9.9398 | -43.5542 | 2026-10-08 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 2c78aede-23a3-3c5d-bd0d-94d3af3b6ccb | -8.9501 | -45.1334 | 2026-10-08 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 443.3 |
| e2c3f007-fda5-3245-8697-9c8bdd0944c5 | -9.475 | -64.3525 | 2026-10-08 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 4219badc-2571-32e9-a5b6-030879209ad8 | -9.0592 | -65.9209 | 2026-10-08 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.1 |
| a73f737e-f220-3a11-b91c-b78a95f080e1 | -13.1641 | -54.3178 | 2026-10-08 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 167.3 |
| 255a491c-495a-3699-95ec-a7eba3cd8661 | -6.8602 | -41.7494 | 2026-10-08 14:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 156.9 |
| 598a7e3a-63be-3527-91fd-7e3ed9a47d99 | -7.3286 | -50.8314 | 2026-10-08 14:10:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 16f0c1de-b174-3201-866a-13b5d7a0164f | -8.9054 | -63.3378 | 2026-10-08 14:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| f22aeb94-7024-3e94-bc55-3613780fbbcf | -6.3283 | -55.3276 | 2026-10-08 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| fe2fa1a6-dd9b-3d40-b23d-9b351e6164a8 | -13.1639 | -54.3385 | 2026-10-08 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 4da3d334-0885-324b-9ef9-ac2edf198944 | -12.1549 | -44.7314 | 2026-10-08 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 78be9352-d162-3d33-9725-02cf6f4ce2bb | -8.5313 | -46.911 | 2026-10-08 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| c4c6e5bd-607d-32ff-ba6c-5bffd648ea09 | -11.2486 | -46.2377 | 2026-10-08 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 89f34d46-8692-3c6f-a8fa-9c9bc36a4239 | -10.9384 | -45.3916 | 2026-10-08 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 409.4 |
| 0717bf7c-41ba-3560-943f-69d7cff0044e | -9.1543 | -49.8142 | 2026-10-08 14:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 12576013-d629-3066-af01-e7dc040785f4 | -10.9575 | -45.389 | 2026-10-08 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 52ca93fe-c3da-347a-8d18-f7050c07c204 | -3.1951 | -42.9538 | 2026-10-08 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| f9189588-9ef3-389c-ae88-7005efd68cef | -7.3054 | -43.9931 | 2026-10-08 14:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 71acf2dd-d31c-3f43-9e58-0a93635a38ed | -11.9832 | -57.5867 | 2026-10-08 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 94862a8f-c02d-3c2e-90be-864f5fa3e2b4 | -7.2371 | -55.1005 | 2026-10-08 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 384dcd64-0a76-3646-b51f-169422e38d92 | -1.0993 | -48.0561 | 2026-10-08 14:10:00 | GOES-19 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5016e083-9fc3-3d11-bbe1-c4f05bddf503 | 3.0733 | -60.557 | 2026-10-08 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.9 |
| fbcde260-3555-3b0b-96e3-2f65b25d9e72 | -7.5284 | -45.8885 | 2026-10-08 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5de4ada3-b043-3ef4-9795-f7285a75f3e9 | 3.0915 | -60.5946 | 2026-10-08 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ef572f6b-4935-3b9b-9e5d-8e447c5397cc | -7.2369 | -55.1206 | 2026-10-08 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 07ffdfd0-fd86-3612-84b1-544f81d954b6 | -10.4527 | -47.2801 | 2026-10-08 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 1b8c308b-964b-3de2-866e-4464073aad4d | -11.3937 | -46.6922 | 2026-10-08 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 4ce699ea-3485-3589-92c2-f8216418dc34 | -13.1833 | -54.3158 | 2026-10-08 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 258.0 |
| 0574ab79-2b65-33d1-a496-f4e8c2a7d080 | 1.6568 | -55.7847 | 2026-10-08 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c95a690a-28be-3d79-b20d-19985ebd84f5 | -15.5546 | -44.5275 | 2026-10-08 14:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 183.5 |
| f51527be-3a68-389a-8176-54f9fb0c4087 | -7.0065 | -59.1223 | 2026-10-08 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 211.5 |
| 07b1b997-06be-315e-9de7-7efdada26282 | -10.4337 | -47.2824 | 2026-10-08 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 206.6 |
| d31891d1-a6dd-3f51-85ec-dcf63d1245c2 | -6.9328 | -43.6799 | 2026-10-08 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 2f665573-427b-3d62-8021-60b10a034f8e | -6.8292 | -39.5472 | 2026-10-08 14:10:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 132.6 |
| a66fbb4c-64c8-328f-becb-1a9c188671e3 | 3.7462 | -51.6224 | 2026-10-08 14:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d02e051e-8eb3-37e9-8541-4d07e069f322 | -8.1996 | -46.3415 | 2026-10-08 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |


[Clique aqui para ver as próximas entradas](README214.md)
