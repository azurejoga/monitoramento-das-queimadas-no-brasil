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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 362b5839-084c-3554-aa54-81f2ad42452d | -6.00884 | -42.88557 | 2025-10-11 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e23bbdd6-5367-35ee-af2c-26574ece80ae | -4.83034 | -49.94699 | 2025-10-11 04:59:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f09bdda8-5bf3-373f-ae41-9ac1bbba4071 | -6.73893 | -42.87629 | 2025-10-11 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e6cdbb2a-ba22-3606-8eab-9eecc97e74c8 | -2.55011 | -48.39624 | 2025-10-11 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f3902c2-3b31-3ff2-a7cf-c75a25f3fd17 | -5.84096 | -43.40881 | 2025-10-11 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7d8a99e-f19c-38ad-8fd7-68f5bbfe1dd9 | -4.14321 | -47.66301 | 2025-10-11 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 696e2729-11ff-3dcc-a3e0-a4c3f1722896 | -6.28801 | -43.90997 | 2025-10-11 04:59:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfadb36c-5250-3992-9b64-68cffed506af | -5.85743 | -42.85403 | 2025-10-11 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 09d1e443-e1cb-349c-bab0-d3ec1c1bfea3 | -3.39008 | -50.13911 | 2025-10-11 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 105d8456-4b9f-3838-9734-863c5c7cf42d | -2.27036 | -47.85157 | 2025-10-11 04:59:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 90fb96a0-5005-36d9-80c0-edbc44880867 | -5.32554 | -43.08903 | 2025-10-11 04:59:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 202c9ecc-7a78-3646-83b1-f8b910235c0e | -2.55064 | -48.39273 | 2025-10-11 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac51f7b3-b862-3793-938a-698b3242ece8 | -4.41393 | -43.47506 | 2025-10-11 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab7bc037-e4ae-3f78-a25a-76614eb08e41 | -5.91021 | -45.43039 | 2025-10-11 04:59:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83a5e9bb-722d-3228-97e2-48b29e2a7ab6 | -6.75308 | -42.81993 | 2025-10-11 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8eecc188-f742-35e5-93d4-eed41ffc3cca | -3.55517 | -50.12543 | 2025-10-11 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3479dc7-921e-3975-a586-2d5a5eb4fbb1 | -5.85872 | -42.84474 | 2025-10-11 04:59:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 38.5 |
| a4dc9193-08b4-38cc-bd43-7b242c57550e | -4.75379 | -40.57267 | 2025-10-11 04:59:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 25c0c63b-74e2-325b-88f4-f3f1ed16d24a | -5.59127 | -41.11028 | 2025-10-11 04:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bcdab865-df5e-3859-ac66-af36672755a8 | -5.87631 | -45.29263 | 2025-10-11 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c118611b-5bb0-332a-b7e9-708f42d63c23 | -2.55117 | -48.38922 | 2025-10-11 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9dc33ac-fa65-3064-b2be-b6b6695069df | -4.75572 | -40.57425 | 2025-10-11 04:59:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e0b3c9a3-c449-3e06-a99c-34589bb4f850 | -3.06903 | -49.21271 | 2025-10-11 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f772461a-e3c6-3ef1-8473-8d6de11412e1 | -3.51937 | -49.69937 | 2025-10-11 04:59:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87d98e92-fd02-3e9a-9b68-99742e3bca9d | -4.25377 | -48.55159 | 2025-10-11 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 971c5393-f26d-3139-97b6-05468753a217 | -5.65819 | -46.41022 | 2025-10-11 04:59:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78e15f40-c50b-3789-9648-8d4491084f29 | -5.68344 | -47.90257 | 2025-10-11 04:59:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5aeada30-8ac2-3552-a3de-0b76d7e5a7f2 | -3.14547 | -49.89773 | 2025-10-11 04:59:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df97181d-c9d8-367b-9836-1f6a5c917037 | -2.51724 | -44.11922 | 2025-10-11 04:59:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fb1d087-5b93-30e8-b1d2-00bfd432ca6b | -4.47838 | -42.86349 | 2025-10-11 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4e2ad1f8-0b9b-3e10-9d25-7404fbc608f9 | -5.91065 | -45.42728 | 2025-10-11 04:59:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1da1a032-2ea0-37e7-929e-153d13df66d5 | -5.5921 | -41.10432 | 2025-10-11 04:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b0eeab17-57f8-340c-867b-491b84d3c650 | -1.90011 | -51.00951 | 2025-10-11 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5853bf1a-d3d0-30f4-aa56-d0f9f574cd0c | -4.42572 | -47.60163 | 2025-10-11 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0bf93b11-68e4-3584-a71a-107132f1825c | -2.29285 | -47.99217 | 2025-10-11 04:59:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b71c4d40-cadf-3c3b-b3cf-0238cd344009 | -3.39242 | -50.14835 | 2025-10-11 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ce88644-8e63-3ff1-bdcd-3a32c839c2d4 | -3.55674 | -50.12761 | 2025-10-11 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 784ac48c-2c65-3736-8fc9-ac356abcb59f | -3.38941 | -50.14346 | 2025-10-11 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2cde95d-7290-3a8e-b0ac-1e688577ee40 | -5.84752 | -43.40546 | 2025-10-11 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05489475-4263-3d7e-a3e0-24001c21492b | -2.26678 | -47.84715 | 2025-10-11 04:59:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c723f11c-e327-385c-9e63-70c81c2778ca | -2.26315 | -47.8155 | 2025-10-11 04:59:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30979a77-7525-30c5-b558-26466733e9ed | -2.59611 | -48.12011 | 2025-10-11 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66fdb244-b9d7-3a17-9e44-c3aaa5df5b77 | -3.97958 | -47.8831 | 2025-10-11 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cede5d6d-dce5-3b19-9c1b-896b7d6730e2 | -1.40776 | -46.70697 | 2025-10-11 04:59:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23436452-3f7f-3699-b9d5-7f3a86848d4f | -4.14386 | -47.65876 | 2025-10-11 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e222e69-bfd6-3055-83d4-e50e78a2260a | -3.44086 | -49.48935 | 2025-10-11 04:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb99e561-b95a-3bdc-97de-dfc42b6b64f0 | -5.8649 | -42.84553 | 2025-10-11 04:59:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 41.9 |
| 90a9be37-e659-3f91-8dc9-a1d43503bc57 | -4.42499 | -47.75501 | 2025-10-11 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2b5ac1f-9e09-3b03-9be2-322a6c1c4174 | -5.25297 | -50.9062 | 2025-10-11 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28ca548a-cb0f-3725-9e63-710b8ff4c7ea | -6.28745 | -43.9141 | 2025-10-11 04:59:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c738ad6-b6d9-3b69-bc49-ad38ecdf1f84 | -3.39309 | -50.14403 | 2025-10-11 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b9c1fcb-6af3-309e-8200-6ecb0fa7289f | -2.59556 | -48.12376 | 2025-10-11 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1668f183-4a85-37f5-8119-462cbf722745 | -2.59501 | -48.12742 | 2025-10-11 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2b0ece6-4112-3ee9-a388-f95ae80608db | -6.75927 | -42.82135 | 2025-10-11 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9b9acc3a-7a7a-3c4f-8646-1ba9b250613b | -5.86358 | -42.85504 | 2025-10-11 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| b5367f85-be92-385a-87ce-d72bbecdbc38 | -6.16147 | -43.76166 | 2025-10-11 04:59:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 425d4572-d0f5-3d0a-9068-aa916f433204 | -5.87584 | -45.29588 | 2025-10-11 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 775556b1-c5ae-3ee8-a79b-dd359cfa672e | -3.2632 | -50.0421 | 2025-10-11 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e9ce5a8-155e-3702-b211-d5684ac98741 | -3.41201 | -52.60357 | 2025-10-11 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ebf6ff7-2def-3b02-919e-f536fa2309ca | -2.26619 | -47.85095 | 2025-10-11 04:59:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1acdc96a-ef1b-3eb1-abd5-b6068b638deb | -3.77209 | -51.3958 | 2025-10-11 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5dadba2-5c39-3ca1-86a9-5cbd61f0a834 | -5.48133 | -51.40971 | 2025-10-11 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e6ca23c-f5fc-3c66-bfdd-fbda5bea43ce | -4.13519 | -47.65725 | 2025-10-11 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30e004d7-9879-3bd4-b336-104b2b870706 | -3.42288 | -52.7312 | 2025-10-11 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c1a2db9-a43a-3931-b880-91fd757928ff | -3.51919 | -49.70162 | 2025-10-11 04:59:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 238e199a-8224-3803-a819-ae9a088229fa | -4.67121 | -49.67926 | 2025-10-11 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a17dd4f-5b73-3a1d-8697-6eafb1899731 | -5.22245 | -45.65208 | 2025-10-11 04:59:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf13fdbb-71df-33d5-a212-f961994da803 | -5.84958 | -43.40745 | 2025-10-11 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 485ce55d-502a-3848-a127-8d31230b39fb | -3.43869 | -49.49103 | 2025-10-11 04:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5898744b-269f-3d29-9a5e-22de28072dbd | -1.8995 | -51.01331 | 2025-10-11 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c765eae-e00d-3574-8b1e-ce3e353c98be | -4.42036 | -43.47173 | 2025-10-11 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2981fc4b-e29a-3512-8a04-153f19bd40b6 | -5.25659 | -50.90673 | 2025-10-11 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e133b866-9320-391b-9467-4f4754c97af7 | -4.25163 | -48.56596 | 2025-10-11 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f14be572-02dd-36ab-ba50-c8c01537daf2 | -2.29228 | -47.9959 | 2025-10-11 04:59:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e41fb08-b714-3010-bc39-bfa64695214d | -3.26254 | -50.04643 | 2025-10-11 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6beafb9-ae74-3cf5-9de9-1295697b3278 | -4.40811 | -43.47429 | 2025-10-11 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48a38801-0aa7-35be-bc85-3068a7779b69 | -5.75814 | -46.49647 | 2025-10-11 04:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1195c719-0074-3305-b6a3-b7832fbaed6d | -3.39904 | -42.39619 | 2025-10-11 04:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 779dd305-ebbd-3ab7-8896-67e82feea656 | -5.32618 | -43.08459 | 2025-10-11 04:59:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b24c09b-6109-3e99-81ad-ce63787efd1a | -5.83565 | -49.02324 | 2025-10-11 04:59:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88911769-3ac9-39e5-89fb-876b1625ed21 | -3.98386 | -47.88367 | 2025-10-11 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2229bdc-6fc3-30d3-bfbe-6226cc73f914 | -2.55414 | -48.3969 | 2025-10-11 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ae0e2e7-d0f3-32b0-8340-67be69d55e2f | -3.98017 | -47.8792 | 2025-10-11 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cfe97ef-5a77-3b85-89f9-d8417307262f | -0.7539 | -47.76166 | 2025-10-11 04:59:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e031e87d-ca80-3da6-90fa-ec063a34825a | -4.25217 | -48.56237 | 2025-10-11 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58ec3603-8081-3dc2-8641-7e20ee2c2e9c | -5.22203 | -45.65502 | 2025-10-11 04:59:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a2a36e1-95d9-381a-996c-32e7eec2c21d | -5.76417 | -47.90356 | 2025-10-11 04:59:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ba59da8-e6b6-30d2-aabf-d3ae9245efeb | -4.42634 | -47.59743 | 2025-10-11 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c7565e06-9e57-30a2-80e5-979a3bb3b438 | -3.42623 | -52.73172 | 2025-10-11 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee4f5fa4-4751-37ae-8d09-56648d77e52d | -4.25628 | -48.56292 | 2025-10-11 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fdbe081-e39e-39f6-846c-d082bc7b354b | -5.32976 | -41.57156 | 2025-10-11 04:59:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 11244133-9ee5-38d2-92cd-9f993d887509 | -6.00783 | -42.88711 | 2025-10-11 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d7c87356-c81a-3335-92a9-890eb11b95d9 | -3.39291 | -42.39519 | 2025-10-11 04:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d8700116-8ac3-3824-b6a3-e0049af5c7eb | -3.50809 | -49.72311 | 2025-10-11 04:59:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d81e111c-006c-314f-bfd4-7d6d3a206e50 | -0.758 | -47.7623 | 2025-10-11 04:59:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b35248f9-5491-3d4f-94f4-04dd0db4f71c | -5.84692 | -43.40961 | 2025-10-11 04:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3bcc36b-52d2-3ff4-9adb-d08971af9eac | -5.48078 | -48.6586 | 2025-10-11 04:59:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62c84cd0-7a2b-3a1f-8b70-604fa4da4497 | -3.86273 | -50.76905 | 2025-10-11 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d20a5bb1-a1b6-3475-9771-e8c1c68ca363 | -3.78757 | -45.04784 | 2025-10-11 04:59:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e70dec48-6499-308e-9a19-9501df66981b | -6.73541 | -42.85567 | 2025-10-11 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |


[Clique aqui para ver as próximas entradas](README33.md)
