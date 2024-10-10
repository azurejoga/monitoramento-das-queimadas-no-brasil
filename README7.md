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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0876bac-d199-3b13-97fd-000d4c7b0f19 | -9.8361 | -36.1745 | 2024-10-10 00:19:04 | METOP-C | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 749a82b1-7d46-341d-a548-4f6baf10e720 | -11.7202 | -44.507099 | 2024-10-10 00:19:04 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 948ad9e3-031c-3d54-bc77-17377714097e | -11.0132 | -41.5411 | 2024-10-10 00:19:05 | METOP-C | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d023d9fd-8e70-3712-ae30-adb4866d28a8 | -11.0148 | -41.548199 | 2024-10-10 00:19:05 | METOP-C | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ab9b947e-cd63-3d9b-8a26-b4137eefd1b9 | -11.0164 | -41.555302 | 2024-10-10 00:19:05 | METOP-C | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6e2dc69e-fab7-3e16-93be-d5507f7ae5f5 | -12.1308 | -46.729801 | 2024-10-10 00:19:05 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 115b44d4-3761-38c8-9b6f-3b1d9c265d32 | -11.701 | -44.561199 | 2024-10-10 00:19:05 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0a8055e4-75fd-3653-a0bf-ae9a0a836af0 | -11.703 | -44.570801 | 2024-10-10 00:19:05 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e6c9ebf-533b-32c8-ae7d-7e454eee7fba | -11.6912 | -44.563202 | 2024-10-10 00:19:05 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f9e21792-89dc-3099-9fdf-cdd34837d1e7 | -11.6932 | -44.572899 | 2024-10-10 00:19:05 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8660bcf-4982-3cdf-aa8d-d05f8239f469 | -12.8554 | -51.1245 | 2024-10-10 00:19:07 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0edd05ea-df16-3c85-bd48-073e7514f5b6 | -11.4578 | -43.996101 | 2024-10-10 00:19:07 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| facf3230-8fae-301d-966e-46980b89892b | -11.4597 | -44.005001 | 2024-10-10 00:19:07 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a52eb289-191b-395f-8d86-03436605a8e9 | -11.448 | -43.998199 | 2024-10-10 00:19:07 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c87437e-9866-3832-9f24-2011841c2809 | -11.4499 | -44.007099 | 2024-10-10 00:19:07 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 137581ae-49d1-3d15-a49a-a31b0da0b4c9 | -11.4537 | -44.024899 | 2024-10-10 00:19:07 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 543f9f2c-7d75-3552-b034-83125bc2d88b | -11.4557 | -44.033798 | 2024-10-10 00:19:07 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aeff8cff-bc42-3632-95a8-354f2dbc20b9 | -11.4576 | -44.042702 | 2024-10-10 00:19:07 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06987142-2acd-3b70-be1f-21d2d1ceda62 | -11.5968 | -44.890499 | 2024-10-10 00:19:08 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dba8190f-a0bc-326b-9092-610e37000734 | -12.8458 | -51.126301 | 2024-10-10 00:19:08 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 81f936ab-fa0b-3390-8885-6a426f825bef | -10.5376 | -40.210098 | 2024-10-10 00:19:08 | METOP-C | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f3a4425d-42ce-3450-b644-f07969fd2ca6 | -10.9537 | -42.899399 | 2024-10-10 00:19:11 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5df1c1d8-88e6-3a2e-a511-872098eb183f | -10.9554 | -42.9072 | 2024-10-10 00:19:11 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 819192b7-92b2-3ce5-9257-e4774ab6b0f1 | -10.7238 | -42.4618 | 2024-10-10 00:19:13 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6d6b9a3a-8170-35d8-bf2e-a38237208986 | -11.7267 | -47.3922 | 2024-10-10 00:19:14 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ad3b841-267b-35a4-a3d6-82222f2bc43a | -11.714 | -47.379501 | 2024-10-10 00:19:14 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 135d2390-8104-3f97-99ce-e11db53dc12e | -11.717 | -47.3941 | 2024-10-10 00:19:14 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6525885d-4c3d-3a49-838b-1e38873a40ec | -11.0579 | -44.952999 | 2024-10-10 00:19:17 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9af66fd9-a6a7-3da0-87b7-9e102d08d6c3 | -11.0659 | -45.377499 | 2024-10-10 00:19:18 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e2961956-e302-3f60-b4a5-e4a7ed455450 | -11.0681 | -45.388 | 2024-10-10 00:19:18 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e18ffa2-bcd8-3d7b-a90d-98e2c2dfc40f | -10.713 | -44.344101 | 2024-10-10 00:19:20 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5344d93-7f57-3275-ba8a-b26c37ef2949 | -10.7149 | -44.3531 | 2024-10-10 00:19:20 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| affd953c-bf36-3bcb-a294-4ca6216bf638 | -11.5105 | -48.433601 | 2024-10-10 00:19:21 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f8b8a1c-8e58-3f80-bdaf-cebfc228260c | -10.139 | -42.466702 | 2024-10-10 00:19:23 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| eb092ad7-0f89-3f2e-81f0-4313efd88669 | -10.5282 | -44.771801 | 2024-10-10 00:19:25 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 375c6b93-b85b-303d-a254-75dbb4e3e04b | -10.5303 | -44.7813 | 2024-10-10 00:19:25 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b108d48e-3fb7-352c-9bfa-282cb409b302 | -10.5323 | -44.790798 | 2024-10-10 00:19:25 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe8f96bc-abbf-3ee9-8836-9177a0f83065 | -9.5079 | -40.351299 | 2024-10-10 00:19:25 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cf6541af-9c57-3e5a-9260-ec43d4fd011b | -9.5095 | -40.358299 | 2024-10-10 00:19:25 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5bd7ebe4-f54a-34b8-85f3-e2da26032ebd | -10.2248 | -43.4161 | 2024-10-10 00:19:25 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b745ee26-a4ac-3290-bb84-e4cc0afcbe9b | -10.2265 | -43.424198 | 2024-10-10 00:19:25 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 568e10e5-64eb-371c-98cb-4866182abe7b | -9.3887 | -40.371399 | 2024-10-10 00:19:27 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 19ddf766-9745-3469-b49c-c3642df0f2b4 | -9.864 | -44.067402 | 2024-10-10 00:19:33 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b48b3484-66dd-37a3-add1-a0f3fcf26438 | -9.8659 | -44.076 | 2024-10-10 00:19:33 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b9a14757-b17e-3edd-b5a1-3f72524f4d55 | -10.5295 | -47.6968 | 2024-10-10 00:19:35 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bece3f65-af06-36b8-b284-f0bf6b9221d0 | -10.5325 | -47.711399 | 2024-10-10 00:19:35 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34da092d-f8b0-3078-8986-0042ddfa631e | -10.5033 | -48.014301 | 2024-10-10 00:19:36 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a90192ae-d132-3b82-bc06-0f5fc89ae5bf | -10.5064 | -48.029701 | 2024-10-10 00:19:36 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0eda5bf-9d66-3f11-a5f4-a43c4f013320 | -10.5096 | -48.045101 | 2024-10-10 00:19:36 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee25eb2e-e5eb-36e8-bf85-b401616db790 | -10.4936 | -48.0163 | 2024-10-10 00:19:36 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e5224f4-8843-3cea-9903-ba04543fbebc | -10.4967 | -48.0317 | 2024-10-10 00:19:36 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c250cd3a-a76a-3ea1-a258-2ea6479716aa | -10.4999 | -48.0471 | 2024-10-10 00:19:36 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ee0173f-822c-3729-b68a-04ef8f2e40fd | -10.6628 | -49.5541 | 2024-10-10 00:19:39 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 314db604-cfa0-3457-aa4e-1ad902b66b3f | -8.7346 | -41.028801 | 2024-10-10 00:19:40 | METOP-C | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f1044bf8-d2c5-3748-baf4-9499fccf402b | -9.4341 | -44.0718 | 2024-10-10 00:19:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 78f704a2-8427-3e49-ad05-bf90dc3ca90e | -9.4359 | -44.0802 | 2024-10-10 00:19:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e78c0f8-7d73-33c7-ac6e-a8a3eccf7163 | -9.472 | -44.433998 | 2024-10-10 00:19:41 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 97dd0bbd-977e-35d5-a0d8-cc9d51f2392b | -9.4622 | -44.4361 | 2024-10-10 00:19:41 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cdfe946f-d869-3bba-bf69-cd98749301dd | -8.5584 | -40.393398 | 2024-10-10 00:19:41 | METOP-C | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| c07306c3-34c1-3a47-830a-af2a217d7702 | -8.56 | -40.400299 | 2024-10-10 00:19:41 | METOP-C | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f7f471c6-5b55-3697-b925-42cb2b2c2f66 | -8.5486 | -40.395599 | 2024-10-10 00:19:41 | METOP-C | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 35b70b7d-1ced-3fff-9947-da8ee1b95a8c | -9.2348 | -43.3508 | 2024-10-10 00:19:41 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c38e639e-2791-36de-947d-734691ca330a | -9.2365 | -43.358601 | 2024-10-10 00:19:41 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c60f2ba6-24b6-3ca8-8eef-00ea2199305f | -9.2382 | -43.366402 | 2024-10-10 00:19:41 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5d5ec76f-0438-3927-a8cd-4f048f161e19 | -8.5044 | -40.427601 | 2024-10-10 00:19:42 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 1fb7d0bc-4b28-3c0f-8be1-3c7480e269c5 | -8.506 | -40.434502 | 2024-10-10 00:19:42 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| fc479087-7a1b-3a44-8c01-11268116f0b2 | -8.5076 | -40.441502 | 2024-10-10 00:19:42 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| db696ca5-23ac-3bf3-be99-527017d0596a | -8.5399 | -40.717701 | 2024-10-10 00:19:42 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 47479850-d923-327b-85b6-98dd215f33c4 | -9.1848 | -43.543301 | 2024-10-10 00:19:42 | METOP-C | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79f0160c-f780-3c25-831d-4bacc0849f3b | -8.4979 | -40.669201 | 2024-10-10 00:19:43 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 0c46031c-6b9a-3d8b-819d-2d7d56b3a31d | -8.4995 | -40.676201 | 2024-10-10 00:19:43 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| e650a332-4d75-3779-8310-c45357a6bb8c | -8.4305 | -40.510101 | 2024-10-10 00:19:43 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| e1595fbb-229c-3263-8617-5127d5d5abf2 | -7.1114 | -35.071999 | 2024-10-10 00:19:44 | METOP-C | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9466bb39-bed3-3c9b-8010-cc9e66c8281f | -7.1017 | -35.074402 | 2024-10-10 00:19:44 | METOP-C | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb7d4bed-2b53-3674-97d3-e9ea6b187ab8 | -9.9595 | -48.727798 | 2024-10-10 00:19:48 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dac7349f-61e7-36d5-8c7b-b7daa4fe1a02 | -9.9414 | -48.8377 | 2024-10-10 00:19:48 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9586c7c-97e2-3659-9c98-c248ccbe26a0 | -9.9316 | -48.839699 | 2024-10-10 00:19:48 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f8859d2-ef46-3fc5-85a5-020e69d1f6eb | -9.9351 | -48.856899 | 2024-10-10 00:19:48 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6eebfb38-dd40-3384-9930-313a1e6add6e | -8.3567 | -41.9519 | 2024-10-10 00:19:50 | METOP-C | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 84b674c4-df47-366b-a8e9-cbb89f3eddb3 | -8.3371 | -41.956299 | 2024-10-10 00:19:50 | METOP-C | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ce308828-4f7b-38ce-9aa5-3d6e4fdb6369 | -8.3387 | -41.963299 | 2024-10-10 00:19:50 | METOP-C | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 347b7a3c-e7b3-3274-b4b8-4e04aed2b82e | -7.975 | -40.8172 | 2024-10-10 00:19:52 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c8316bb5-9ddd-3324-8dd6-83368c5fcd94 | -8.1105 | -41.365501 | 2024-10-10 00:19:52 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7f6cf04c-f6d7-3285-8873-0cef785fadce | -8.1121 | -41.372398 | 2024-10-10 00:19:52 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b0cb8a9f-529d-3c41-931f-973d7a92d3fa | -7.9183 | -40.974899 | 2024-10-10 00:19:53 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c06195db-8cb4-3de3-ade7-7895332fa0d4 | -7.9199 | -40.9818 | 2024-10-10 00:19:53 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2d5f2133-d35f-34f8-8cc0-6247f2b38987 | -7.9215 | -40.988602 | 2024-10-10 00:19:53 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 113e3685-bb51-3ebb-8e8f-9f934a8838f1 | -8.0003 | -41.1082 | 2024-10-10 00:19:53 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b859a59-6be2-3ccd-abe7-a850a222ce79 | -8.0783 | -41.496101 | 2024-10-10 00:19:53 | METOP-C | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2fd375a2-1987-3f9c-ba51-f1e9dbf95a82 | -9.1671 | -46.443001 | 2024-10-10 00:19:53 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2939e43b-a060-35b2-83ad-2b08d08c5f61 | -7.5972 | -39.626099 | 2024-10-10 00:19:54 | METOP-C | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 0f96c761-bba4-35af-bc13-b1f55a4ddfcf | -7.5989 | -39.633301 | 2024-10-10 00:19:54 | METOP-C | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 0d8e59c6-52bc-3fa4-bb99-c0c014e02c89 | -7.6713 | -40.3032 | 2024-10-10 00:19:55 | METOP-C | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 2c676979-ffcc-367d-b22f-d24db5c4460c | -7.6729 | -40.3102 | 2024-10-10 00:19:55 | METOP-C | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 731f48bc-f5f2-3242-bae2-def0a22eb683 | -9.5565 | -48.9874 | 2024-10-10 00:19:55 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff290f18-db94-3aea-a0d1-1bbb86eee049 | -9.5468 | -48.989399 | 2024-10-10 00:19:55 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f68feae0-b147-3b5a-b87d-e8c8495c8021 | -8.0705 | -42.326698 | 2024-10-10 00:19:56 | METOP-C | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f31015e7-a058-3dfa-8197-c9ac2c8350fd | -8.0721 | -42.333801 | 2024-10-10 00:19:56 | METOP-C | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 97475e07-9eca-3583-9aa2-20227324dfe6 | -9.4973 | -48.945499 | 2024-10-10 00:19:56 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 802ea5c7-8886-30c0-97b0-6197e04a07db | -9.4876 | -48.947498 | 2024-10-10 00:19:56 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
