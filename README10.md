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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce17fd10-ee23-3f62-8b72-40f2878aa391 | -11.6789 | -50.3651 | 2026-07-23 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 6c8397ef-65b5-34ee-aec3-c82aef5faca7 | -11.6792 | -50.3437 | 2026-07-23 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| e8dd57ae-dccf-375d-b668-5272a290b11a | -7.01318 | -45.85013 | 2026-07-23 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cad9cde5-9bc3-3697-956f-29e17ea1e6a6 | -6.41673 | -43.06591 | 2026-07-23 04:23:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aaea0170-c3d3-39dc-a144-ccab86ca29aa | -4.03412 | -43.23453 | 2026-07-23 04:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3eccf623-5034-3dac-8e5b-abc5f5045d04 | -4.47772 | -40.86727 | 2026-07-23 04:23:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d10562fc-1f47-365d-9c19-67179a6b2de9 | -3.5238 | -42.69707 | 2026-07-23 04:23:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9032708-4162-3152-a84b-d2aaca01ba14 | -6.04856 | -43.86775 | 2026-07-23 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7845dca-9ebd-3c64-85fb-7d8f344a49b3 | -7.02001 | -42.78313 | 2026-07-23 04:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6ab8404b-be7d-303d-9b1f-fd3230f66d96 | -7.01002 | -45.42743 | 2026-07-23 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 363dda88-8779-3b52-a928-63a0b5ac4b15 | -6.5426 | -43.10711 | 2026-07-23 04:23:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb9feede-adaa-398a-802d-f04b1d3704cd | -5.67552 | -43.57629 | 2026-07-23 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64cf0e90-e27c-3d08-a866-babed1b48b24 | -6.49395 | -42.22506 | 2026-07-23 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 542da00e-7db5-36c9-82ed-b45cdf27ffcf | -7.68598 | -41.23979 | 2026-07-23 04:23:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 169bcab4-e2bf-3721-855a-33cb3b04326e | -1.59099 | -50.43676 | 2026-07-23 04:23:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f2a4c9f-350f-37d3-8493-ac4e4470dce8 | -4.83482 | -44.07188 | 2026-07-23 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0283f1c6-efd6-3f66-843b-14587327f44c | -6.23247 | -48.99182 | 2026-07-23 04:23:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9377af8c-ca36-3101-9d94-a20d83d570bc | -5.82937 | -43.48396 | 2026-07-23 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8223edb3-c15e-3634-b299-ecc61b4f6cfa | -6.21238 | -49.43428 | 2026-07-23 04:23:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1bcbb075-5eee-329d-a47d-cc2b2884308e | -5.11838 | -43.22873 | 2026-07-23 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04ba2768-43b8-360e-a7b4-850ff48fd74f | -5.6369 | -47.10107 | 2026-07-23 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19326ea1-dfcb-3761-b97e-782a39c0fb97 | -5.80509 | -43.63666 | 2026-07-23 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6126d0f4-0a16-3234-a1af-a5f1ad630e56 | -4.0308 | -43.234 | 2026-07-23 04:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2bfdd588-af3a-3278-a453-125f7b3efacd | -7.04057 | -45.54477 | 2026-07-23 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cba93225-231e-3612-8980-9bfd9c6e6363 | -6.15635 | -47.11647 | 2026-07-23 04:23:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36c0d333-fd3c-35de-99ae-bdd3ff2c2cf4 | -3.27284 | -48.8325 | 2026-07-23 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a116e797-499b-38f4-9ce9-f011d8eea893 | -5.06191 | -38.02066 | 2026-07-23 04:23:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 57153aea-c50e-3b8d-a1be-96ba5ccf23b4 | -5.11892 | -43.22527 | 2026-07-23 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90308e2d-0e88-3dc1-9a94-d7c0997af5a0 | -5.35929 | -43.13966 | 2026-07-23 04:23:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3518d37-0dcc-3c36-a4f3-bacb2b80e1ec | -5.63857 | -44.1299 | 2026-07-23 04:23:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b885058-95d2-34fe-96bb-027ac2a8c726 | -6.20802 | -49.43353 | 2026-07-23 04:23:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 897c52e6-2cbc-3bc3-b34f-237c5b7dab0f | -6.48501 | -42.22765 | 2026-07-23 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 420d35d0-974a-3391-9a80-7249161dd17e | -3.19439 | -48.76522 | 2026-07-23 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0034a4a8-8fce-361a-91e9-67255dcedfa5 | -6.42005 | -43.06643 | 2026-07-23 04:23:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 980687fa-7c90-3051-a626-17d3bf80f3c9 | -6.04801 | -43.87124 | 2026-07-23 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4cd7c89-0aa4-3fb4-b48a-3687ed9b0929 | -2.7673 | -48.57598 | 2026-07-23 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e07f40a2-6622-37f7-84ef-818ed27d895a | -7.0078 | -45.41936 | 2026-07-23 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 110f0a7b-323f-3c54-ad87-8529a944c2cf | -4.90623 | -43.47586 | 2026-07-23 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a9a5f7f-a57a-3b53-b8ae-0e4491533fbb | -5.82343 | -44.13437 | 2026-07-23 04:23:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 25bd74ac-d5d9-3afc-b592-af2c94e3cb3d | -5.09562 | -41.71756 | 2026-07-23 04:23:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 852d370e-0e27-32f4-96db-2b21477756ee | -3.42197 | -43.16614 | 2026-07-23 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d97df59b-e57f-3d2e-b8f2-1d98204fc454 | -5.75816 | -49.08805 | 2026-07-23 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1dfb5e1d-a0c6-3dac-aa41-134779904828 | -7.01253 | -45.85403 | 2026-07-23 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cecfeaa8-1432-301a-82a4-6815da7aec1f | -6.31633 | -47.33664 | 2026-07-23 04:23:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7fe83a2-ef67-3b2d-aaec-cab5099179a2 | -5.80841 | -43.6372 | 2026-07-23 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31d67572-e80c-3896-ba16-f03c0c750fcb | -4.4141 | -42.13838 | 2026-07-23 04:23:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc6c8353-d790-33ba-a70c-fd3661c10753 | -5.48785 | -45.11843 | 2026-07-23 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 512377bc-108e-3eb8-8149-58650da23c2d | -4.83818 | -44.07241 | 2026-07-23 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c334826-a9d8-3863-8e02-0e1894c18cc3 | -6.30892 | -43.65963 | 2026-07-23 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a06a3082-70a1-3a73-bf22-116b87a461bc | -5.79789 | -43.63908 | 2026-07-23 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a85eab6-703a-3f79-834a-51514f17f4af | -6.49785 | -42.22205 | 2026-07-23 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d90260cc-e5f4-38ad-b7c2-aedaecf176c9 | -5.55042 | -45.38841 | 2026-07-23 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e61d5c7d-637d-3907-be06-4ab3be4cd7be | -6.30616 | -43.65562 | 2026-07-23 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e6c1270-e17d-3543-82a1-d5ab9a15320a | -6.05189 | -43.86828 | 2026-07-23 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b7842c3-346d-3ef6-8693-bf9d68891e8f | -5.82605 | -43.48344 | 2026-07-23 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1ac3656-e6cb-34aa-8342-e8f3ac4002b8 | -6.04079 | -43.87367 | 2026-07-23 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58554b75-606d-37a2-9e0a-6e04c543f3c4 | -6.3056 | -43.6591 | 2026-07-23 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8859e73-5865-3a6f-8caa-fd2866b423af | -1.59046 | -50.4348 | 2026-07-23 04:23:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 739b36d6-64b4-36dc-8627-d785f02d6a5e | -1.58595 | -50.43591 | 2026-07-23 04:23:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00a34c7f-a31a-3bc9-a71a-105b2f81613d | -3.14382 | -48.15665 | 2026-07-23 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb910077-2043-3c27-a2d5-135184d45861 | -5.14907 | -47.60229 | 2026-07-23 04:23:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b040b9e0-d7a9-3309-abbd-ec61d4b39aa5 | -5.54946 | -45.38918 | 2026-07-23 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd73ed85-75f9-3209-8a8e-09ec65cacc0d | -5.09899 | -41.71808 | 2026-07-23 04:23:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89589c91-1d1e-3430-84f4-fb8c95d2b3e6 | -5.76245 | -49.08878 | 2026-07-23 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a3a6afcc-2dd7-3496-b3a6-f1c18e95210c | -4.47251 | -45.9156 | 2026-07-23 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b48b87fb-cb0e-3952-8f0e-7478b4a09a60 | -7.01123 | -45.41994 | 2026-07-23 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b32203a5-5b46-336e-a91d-fd6e084264da | -6.49675 | -42.22912 | 2026-07-23 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f80f1eba-db5c-3c3f-9151-5bf2e89db044 | -6.4934 | -42.22859 | 2026-07-23 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 30592650-2b2b-354c-b474-5bac8aea558a | -4.58916 | -43.17333 | 2026-07-23 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3da27658-992e-36a2-bbc6-7043ad4e06e2 | -5.55007 | -45.38534 | 2026-07-23 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67b66994-fd21-308b-ac15-c08139726a08 | -6.4945 | -42.22152 | 2026-07-23 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 8f109593-d33b-3548-ae95-b48a54c5a4b5 | -4.15917 | -43.08754 | 2026-07-23 04:23:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a9aa781-9b96-3985-b6c5-16783d79ca6a | -6.4973 | -42.22559 | 2026-07-23 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c8119d7d-0378-3215-acb9-b361cbf0a6b2 | -5.72314 | -44.50122 | 2026-07-23 04:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f2aa390-2405-38e0-b347-41f1dd814a47 | -5.84861 | -49.06056 | 2026-07-23 04:23:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 048d0aab-211e-302d-8dc7-0cbef1e9bb3a | -7.01062 | -45.42368 | 2026-07-23 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbfe2f28-4bed-3104-9587-a2873bff6680 | -5.80176 | -43.63613 | 2026-07-23 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e7c36a5-815c-36bd-9809-5cffa0b877c4 | -6.30948 | -43.65616 | 2026-07-23 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51cadc97-97c6-3aec-b18c-ceb3e8f0f830 | -7.00841 | -45.41562 | 2026-07-23 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25b30e40-9125-321f-a784-75d61343bacd | -6.05133 | -43.87177 | 2026-07-23 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acfcbcec-855c-328b-9b7c-cdd549e4a830 | -6.31732 | -47.33945 | 2026-07-23 04:23:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fab40e2-9acc-3521-b817-102cf9ef8a84 | -7.01184 | -45.41619 | 2026-07-23 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8f53e238-76ae-3080-af08-213dbe19ea07 | -6.20874 | -49.42934 | 2026-07-23 04:23:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d077c0bd-26d1-31bb-9258-c29194599865 | -5.49021 | -45.11891 | 2026-07-23 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3efd4443-2d26-322f-a6b9-fdbb4c935945 | -1.58998 | -50.43766 | 2026-07-23 04:23:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc6d09ed-3147-3f85-a687-01ac6da0faac | -6.49285 | -42.23211 | 2026-07-23 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 89a3f497-8bed-30d9-8381-7d67b98c6c7b | -8.83383 | -47.0768 | 2026-07-23 04:25:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3c5dff7-5bd9-3b6a-a96c-08702f863d18 | -7.60611 | -44.46289 | 2026-07-23 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25741c52-408a-39d0-980f-a3c5558585d4 | -10.6342 | -47.48456 | 2026-07-23 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73862004-a1b2-3198-b2e5-41703490e070 | -12.66576 | -48.21767 | 2026-07-23 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20eb1956-ca2f-348c-a225-2c4bddf8d0a4 | -11.67113 | -50.35638 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 094b07d7-baf0-35be-99f0-953a604e1db2 | -12.40986 | -50.395 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9b4af793-12e4-378f-b963-dd6962451b69 | -11.91291 | -43.84915 | 2026-07-23 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 35b8e547-d51d-3228-acef-234fbf6a5522 | -11.79705 | -47.10862 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8da5acb8-2aa6-3016-a277-c888963bd3a2 | -11.78787 | -47.0988 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3440898d-778e-324f-91a5-e325db4522bf | -11.78017 | -47.10155 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de289228-12b5-3ae9-ae48-dc3cb3fbe717 | -11.91768 | -50.38443 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e32c4ac1-c4b9-30a8-bf23-66a426fe9790 | -11.94511 | -50.37726 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 81bd9a30-befb-32e5-b6ec-bd882220f2dc | -11.95773 | -50.35507 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d1a7b280-6770-3922-b6cc-ad31951d0e88 | -13.37546 | -54.30426 | 2026-07-23 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
