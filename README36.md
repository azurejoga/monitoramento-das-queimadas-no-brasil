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
| 9fed5272-be39-3bae-b27d-f01612bf5bdd | -7.86128 | -44.48174 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 742ae902-c69d-37de-a671-53440d60b6ce | -7.53237 | -44.29598 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66e9cfa1-4254-387a-a506-99f15e125483 | -12.90457 | -47.05378 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4adb787a-5b42-394c-8b4b-a8aceeadab29 | -7.55186 | -44.28873 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71267d66-0534-383c-b719-069fcaf33abe | -13.31249 | -48.49804 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0fd6ff4-5867-3adb-9a4d-4d8a97c83736 | -9.66364 | -57.76753 | 2025-10-11 05:01:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9875e66e-705d-31c7-84fb-2183b0f885bf | -13.31778 | -47.12284 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a98428e-ec7d-3e73-a2c5-990858ada2ac | -9.17963 | -68.18457 | 2025-10-11 05:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb289260-2707-30e1-9cef-81e4045ecd3d | -10.19937 | -44.61481 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb2f969a-afb0-3bee-98f6-655cb8decebd | -12.24253 | -51.1414 | 2025-10-11 05:01:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d21a3fb-7fa2-3696-ba28-4a9457429239 | -13.20957 | -42.34726 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 0a0754ed-4389-39e6-86c9-02e1c220bdf9 | -7.39888 | -45.91914 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01386db8-403c-338e-a997-a8cb11f4f4d3 | -13.28544 | -47.99712 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e79f93ca-803a-327c-bf81-12a642263fee | -10.52127 | -47.35199 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 09649b57-bf5d-3939-b568-b81b68c954e9 | -8.93109 | -47.20687 | 2025-10-11 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00e6ced3-7b85-3cfe-b366-b3a79671527b | -7.67528 | -43.99216 | 2025-10-11 05:01:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61870a07-278a-3d83-b112-7af3b5144803 | -13.28881 | -47.13076 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de4a7550-4330-3be4-9f8d-869a6b01b2cc | -10.51985 | -47.36296 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4904d0cf-056c-3c6f-be33-24773844a2d3 | -7.8618 | -44.47782 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43701d7d-17f1-3be8-ac76-c151fcaaa1e8 | -10.42852 | -44.9944 | 2025-10-11 05:01:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7077ec34-66fb-3dfd-8f49-2ca207e78fe9 | -6.75615 | -42.82131 | 2025-10-11 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| ba0bc94d-2952-352b-a36c-717ef8d229da | -13.46111 | -48.09795 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb8809bf-0e59-3cc8-b827-fb97ceb076a5 | -7.79116 | -46.01463 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b5dd8b8-8b3d-31cb-91b4-106d0881d23d | -6.43462 | -45.82701 | 2025-10-11 05:01:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21e7b9d7-7ce5-36ac-b9c9-01d3f8f25b5f | -6.75556 | -42.82582 | 2025-10-11 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 1c26c6e0-fe98-39b9-a238-751871cb05e4 | -13.26321 | -48.01616 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| abd5aa1f-9e0a-3008-ad72-776fe495b03d | -11.44729 | -43.48173 | 2025-10-11 05:01:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2191c35d-b6f0-3a38-9a8d-dd05e58f0c78 | -8.04643 | -44.11654 | 2025-10-11 05:01:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea46e46f-003b-3276-b55f-07f6353a6d1a | -12.6896 | -51.18935 | 2025-10-11 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e024affb-1531-3081-87fc-7f9d2b58db29 | -13.41657 | -47.26897 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09009719-7d83-3058-aca8-ada6c7ae88b2 | -7.53402 | -44.29044 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 913cdcd9-a275-34af-a47c-772e0bab9f59 | -7.85561 | -44.48057 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8beb3bce-ae93-34be-89b5-70a742d0c4f2 | -11.76332 | -46.36961 | 2025-10-11 05:01:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 435d92e4-dc70-3fca-81ae-4082af37f853 | -13.41146 | -47.26818 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60e34170-fc10-31e0-a668-4449558d1d70 | -7.25899 | -44.09499 | 2025-10-11 05:01:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b55f8e4-b1a4-32dd-934d-091605fef74b | -13.53483 | -48.11991 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 089425a0-f769-3f95-907c-752f3c953e40 | -12.90311 | -47.03688 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8d4a7519-fa71-35b1-885a-05f40859eb73 | -13.48596 | -48.09634 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8df98736-9509-3d74-aa58-b43ea3d935fe | -12.90633 | -47.04005 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abc9be27-ac32-3b99-9570-114af7dc29ff | -12.81564 | -50.51242 | 2025-10-11 05:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f345843-1a74-3a9d-88f7-604df32156af | -7.34469 | -43.85968 | 2025-10-11 05:01:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 208b63e6-f679-33a4-849f-c58b489acc63 | -8.08359 | -43.9045 | 2025-10-11 05:01:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3007cb9d-3fb4-3f86-b921-a6272578d137 | -11.7568 | -43.3202 | 2025-10-11 05:01:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f38479b2-1275-3d74-ae68-2a22c17ce7df | -10.1784 | -44.54508 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba497ddc-30a3-305b-9a79-0e3caf80a2e3 | -10.62494 | -54.95319 | 2025-10-11 05:01:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99d3340d-5374-3641-ab7f-4f6614a82d30 | -10.52538 | -47.34026 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b74a30ad-83e0-36ac-9ccd-bccce3ac1345 | -6.74433 | -42.81419 | 2025-10-11 05:01:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a3b333f5-43bd-3c1a-82c0-7a6ca81a6d6b | -13.21726 | -42.34137 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 9e9179e2-23ad-3093-9a76-89640dc935ff | -13.31312 | -48.49319 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d372c31-7eb0-3e82-b415-9531295b8de6 | -13.3395 | -48.47475 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ce57685-1bd5-3029-b509-112258f8b900 | -8.00736 | -44.44858 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2db42f31-2ea8-3755-9a31-145338e5c66f | -7.34411 | -43.86385 | 2025-10-11 05:01:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fc2f85c-71b5-32aa-a551-eed272d95858 | -8.19422 | -43.32947 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| af9dcd00-85b0-385e-abd6-958dec57536c | -7.7286 | -40.99291 | 2025-10-11 05:01:00 | NPP-375D | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bdf34ec4-e5c9-38a7-b394-c5c183a9d305 | -9.25022 | -56.30038 | 2025-10-11 05:01:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23b520eb-07a4-3db1-b722-cdc41f13cf19 | -6.73744 | -42.86692 | 2025-10-11 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f3226726-aa9b-3a2c-8613-102b36310a80 | -11.19153 | -50.51678 | 2025-10-11 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91b9edbb-251f-334c-8d13-cd9edfe3af37 | -9.93288 | -59.92264 | 2025-10-11 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb5861f4-a5d7-37ca-8455-8c3f28d79427 | -7.65715 | -42.58402 | 2025-10-11 05:01:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7f7aa9b5-612b-318e-8a03-52875a221450 | -13.30918 | -48.48662 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b2454ee-38d6-30b0-b761-de1a01475bce | -10.51823 | -47.35602 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 71dc6606-b14d-32e2-947c-e2dfe8e6a1f5 | -10.62161 | -54.95266 | 2025-10-11 05:01:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27fce116-f68c-304d-b651-bfa66b3a7536 | -8.40571 | -45.0913 | 2025-10-11 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b64ae43-fd6c-3839-ad87-0dc20b26b478 | -7.79073 | -46.01771 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d9d14ce-6ccc-35c5-87aa-ab4b229a84c7 | -13.33816 | -48.48497 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 510f30a5-3ec8-3685-8005-902114e22fc9 | -9.40261 | -42.67323 | 2025-10-11 05:01:00 | NPP-375D | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9a8be8a4-3512-3bde-b1f1-40180b504c5e | -8.40017 | -45.09056 | 2025-10-11 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77aa1100-672f-362a-adbc-c01564da1b4e | -8.19035 | -43.32341 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 69a4fb68-9ce4-3d09-9a76-2e97ddb98b91 | -13.45855 | -47.71245 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 274aa84b-6868-303f-ab5e-8d5854da9f20 | -7.06287 | -45.21702 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abe3b6a1-198f-3171-bb6e-339c11aadf42 | -13.31574 | -47.1253 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f00435e3-ebce-3432-800b-aaf28c624d28 | -7.85402 | -44.49249 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bcc88523-f640-37b1-9db2-79ec79bf9ae8 | -10.54648 | -47.31161 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c4bdf5d0-5404-352e-94b5-3f3dd334587a | -10.51146 | -47.35083 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e4a3fbb5-59b9-32c8-a37e-ae0a7b2d3242 | -7.86513 | -44.45302 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06b747fe-a0f7-33f7-ac33-73e080b3b9a0 | -13.2583 | -48.0159 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d62b48ba-a7ba-3663-9c7f-edd7167134c6 | -12.90598 | -47.04279 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68b0307d-54a8-3241-a3ed-11b0ee112ef5 | -12.72873 | -45.84409 | 2025-10-11 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 758c9eb3-62cd-3c45-a722-8d31e514a002 | -6.91557 | -43.58668 | 2025-10-11 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2f939514-ff97-37c7-a9f8-5fe3f8402d4f | -13.28616 | -47.99152 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4eb84611-dc8c-351a-a061-0e89234d6add | -8.08067 | -43.90721 | 2025-10-11 05:01:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5bd59213-3b7b-3786-b462-30744237d574 | -13.46099 | -47.69749 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e12b0607-a9bf-3e62-ba65-650760ab66a0 | -12.6935 | -51.18995 | 2025-10-11 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63c7dcf7-0c3d-33ed-8b26-91d1b4afed00 | -12.6889 | -51.19436 | 2025-10-11 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db8a391b-b8b3-3782-9219-e39dca94e07a | -10.17193 | -44.54906 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c1157b0-036e-3fe6-865d-4ea9d53950f4 | -13.46049 | -48.10279 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1b41648-4095-35f0-8acd-5c7dd9bfff83 | -13.49008 | -48.10263 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04ac3447-98b1-3aa0-b289-e9c80a81a9d6 | -7.53271 | -44.60303 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 312a1e13-87b7-316d-84fc-9b9e6a063801 | -10.52269 | -47.34106 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38a386fc-fac0-34ba-a7d3-baffb4aeb900 | -8.88969 | -66.86362 | 2025-10-11 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19c6343f-1ada-3fc6-a9fb-64782dced83e | -13.4597 | -47.708 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0cef8694-5dc5-392e-89d8-a29356527158 | -10.5606 | -57.51614 | 2025-10-11 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a03ce9b-4d2f-3441-8b74-e6975974ad6e | -7.65704 | -42.58145 | 2025-10-11 05:01:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 828068b2-bcd8-37f1-9f91-224b0e1a4dec | -10.20042 | -44.60657 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 033b72ab-2732-3ead-ae14-0dfac647a63c | -10.1999 | -44.61064 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3cfb31e3-795d-35f1-af50-204cc59c10d5 | -7.38088 | -45.17487 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66bdb44a-42a2-366d-b5a9-adfd344aff91 | -10.53043 | -47.31984 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 785aea16-8f52-3fa9-b557-1c21f3b76bb8 | -9.40479 | -66.76305 | 2025-10-11 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9abe1913-efda-3ebb-a325-f50228ebaf53 | -7.65776 | -42.57616 | 2025-10-11 05:01:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 533925fe-a05f-383b-afe6-60a852393fb7 | -10.42231 | -44.99762 | 2025-10-11 05:01:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README37.md)
