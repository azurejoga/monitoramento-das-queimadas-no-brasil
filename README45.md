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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| babe323d-e1f0-3c71-992d-f40fa02df3ad | -15.4042 | -46.27874 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e69153f8-c671-38cc-900d-b9910d3e973d | -15.39548 | -48.04961 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50fe6d8d-25bc-3d6a-8ce5-b034e502e129 | -18.02386 | -57.56845 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8387cf68-c4d0-3021-9ac1-125d934aaa3f | -17.90103 | -57.65998 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 435a6a50-07b0-3ca4-bee3-a5fa7bc1ed4a | -17.58491 | -46.06691 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d3d7037-9c94-38f5-a6bc-9d23e2cd567f | -15.73153 | -46.24863 | 2025-10-09 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0b04a87-8aba-3af8-b4ae-4febbede0f22 | -18.05542 | -57.55638 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 92577bda-3c34-310b-9b68-c245d23a1824 | -17.45904 | -43.3814 | 2025-10-09 04:21:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f539af82-0dbe-3969-95ff-4d58dfb16c59 | -18.64659 | -43.91945 | 2025-10-09 04:21:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| bcd99b2a-c941-3e17-b887-7b697b7c1bc3 | -17.829 | -57.65157 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9c6a9862-c9cd-3f66-b9f0-6d21d56a696c | -14.98205 | -46.2864 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25c94c5c-d595-312f-8bf7-c21f2c0434da | -15.47233 | -47.96034 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4f519a8-dca7-329f-8386-0fe7597a90d1 | -16.63133 | -45.42912 | 2025-10-09 04:21:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31542b3d-774d-35c8-bf8a-4adfa38645ab | -18.64726 | -43.91463 | 2025-10-09 04:21:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7c3be839-db0b-3f57-82e8-99999afd1365 | -15.2934 | -46.1843 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76b20a10-01e6-3644-95c0-d06dc141060f | -14.85 | -48.43929 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db24fee7-b2a0-3c3c-a678-8f7fefcf0933 | -18.39645 | -45.2491 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44176a99-bf53-3bac-8811-44c14bc63e56 | -15.22242 | -46.37746 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f051dda7-2ad2-3e58-abbc-32367ec99e0a | -17.32608 | -46.84103 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4256bba-d49a-32ae-bfac-d85e7db83c9b | -17.92058 | -57.52151 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 59150bde-721f-3cff-b542-6078aeed60cb | -17.55884 | -43.51874 | 2025-10-09 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1309e51-2799-3302-9f7e-77a6264478f1 | -14.85062 | -48.43549 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb010095-bfde-3642-b4eb-a637c89634e7 | -14.93592 | -46.79341 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c11b7bc7-1e99-349d-91a2-c637b54c22fe | -16.60139 | -58.16401 | 2025-10-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2d2d909c-c827-3794-8ab3-995b6f61a1b9 | -18.39616 | -46.87922 | 2025-10-09 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20a26876-6bcb-3e47-a743-1de86d3054e9 | -16.26402 | -48.63441 | 2025-10-09 04:21:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14efb50b-f59b-37e8-aaf9-947975183a57 | -17.91635 | -57.51418 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4c98b37e-d5fe-3c38-8941-0bb8fbcb16e8 | -18.08647 | -44.46437 | 2025-10-09 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98d872ad-b852-347d-b074-fa24bb049eb8 | -19.71497 | -44.00497 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be89448d-5ece-3a50-90d9-e1e3da38b3f8 | -17.89549 | -57.6586 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f983ef2b-13d4-3776-8960-f047051ae26d | -17.82664 | -57.63543 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| deceec12-16b1-3b2b-9103-cb78a175d18d | -18.03899 | -44.9947 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46ce54a2-572d-302a-965b-5fe9fe54b541 | -19.50264 | -43.84126 | 2025-10-09 04:21:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 535c48d4-639a-31a1-960e-b342b453061b | -16.71153 | -47.60941 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b48bd5c2-671c-3471-8b35-002c87801101 | -14.84532 | -48.44636 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f664125-7dd8-3e78-8908-cb8e65411f1f | -16.26269 | -47.83841 | 2025-10-09 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e07b42fb-7443-3eb8-8e64-7a99a2ef7b7e | -15.25113 | -46.36757 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17aff950-141a-3a85-9547-387507f80c83 | -17.87994 | -57.65926 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b96a5d8e-957e-3e26-a087-291ed0b3c41f | -16.00236 | -59.55306 | 2025-10-09 04:21:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6f672d1-3911-3636-9137-f994415c2688 | -15.22186 | -46.38102 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d4d48a80-09fa-3dab-87c5-cfdf4a32922f | -14.97424 | -46.29227 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37d2e58f-01cc-3791-8042-0f301abc46ae | -15.05773 | -48.07541 | 2025-10-09 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5502d7c2-6362-3ad6-8dca-7dcce8c97f47 | -17.94904 | -44.41692 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 857f56f9-290e-30c8-ba05-cc89985ef97c | -17.84693 | -57.64973 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 910de349-2154-3ad5-bc96-f896a9fedb59 | -17.58323 | -46.07794 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec369c18-9741-374b-9aff-3a396dbe4efd | -19.18699 | -46.49829 | 2025-10-09 04:21:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65b30922-4b33-3950-8108-60e1ad613bad | -16.3473 | -47.10344 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1d79928-f3eb-3e48-bdfb-6c763e896f97 | -18.39672 | -46.87559 | 2025-10-09 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56b7222e-663d-3784-bb09-0dc4fdfb2c59 | -14.88575 | -48.24634 | 2025-10-09 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d432f68-7c40-3ac1-9ad0-5851758cd122 | -18.09467 | -44.45748 | 2025-10-09 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8232a6f-2c51-36e3-bcf8-4622fa675fed | -16.28476 | -47.13326 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50f67577-9aac-3991-b56d-1c55ead8c3ae | -17.98018 | -44.96984 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8de14ca6-2ab3-3c14-80f9-13826c002241 | -15.29399 | -46.15876 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86612f03-f1bc-30f3-b2e0-c28a69885ce0 | -14.84252 | -48.44199 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b61640f-7b99-3e80-aa2f-2989b4d4be2b | -14.94093 | -46.78328 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7af2f0d-80b2-374c-b270-7fe5446e0ffd | -17.94845 | -44.42102 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35379fa2-5c0d-3b7e-8023-ed62b977ebd7 | -17.98766 | -44.96705 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f932852f-9c82-388a-8e3e-c5dd5aadf7c4 | -17.84059 | -57.65203 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 480ae796-d636-36d4-80f4-249673cf9ed9 | -16.27699 | -47.1393 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49f6c63d-4ec6-3469-931f-1288115c57f8 | -15.37988 | -48.0392 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a03db25-ddd8-35de-bda7-2b253ae52319 | -16.06631 | -47.77154 | 2025-10-09 04:21:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9058920-4122-3c09-b84a-dd57387d86c2 | -17.65054 | -44.43663 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6674a5a6-c52c-3196-87cf-49b1b171d4be | -15.22684 | -46.37088 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4877647-175f-3ae1-8095-55980cbb019b | -18.41304 | -45.23167 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ca9695e2-a2a2-3f6f-8912-32f1f922f635 | -15.28093 | -47.87384 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4998d46f-d6e2-3889-92fe-57d2b35aac81 | -15.29615 | -46.18842 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 123dbf7b-196b-3fc0-b0ce-06b255ace8b9 | -15.75458 | -48.70015 | 2025-10-09 04:21:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 068139cd-0c8a-3399-8a6d-8d9dc4979eb6 | -16.70889 | -49.75471 | 2025-10-09 04:21:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 84a4985b-b395-37c5-b355-11bc057b48a2 | -15.39334 | -48.04156 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58cc5deb-7179-3944-9367-3bf727fcdfd1 | -18.0338 | -44.98175 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ea19fd60-b6da-3a32-a95e-bba3034aa7e8 | -15.46957 | -47.95609 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5f1f0fd-d5c5-3eee-a33d-87b87bd563a7 | -14.93261 | -46.79287 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4de435ac-254f-3f12-9873-cc67dbbc99bf | -15.15873 | -49.56738 | 2025-10-09 04:21:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 51abaf5b-dff7-333f-a776-b9d15c863ca3 | -16.26903 | -50.98697 | 2025-10-09 04:21:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b20e6ee8-a962-3921-9e6d-255fda8ea552 | -17.90386 | -57.6565 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9ebb1ee4-7a24-3682-a145-867068bb7216 | -17.95653 | -44.9864 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7e07d620-0d8b-336d-9974-b3b2982d0b27 | -17.97729 | -44.96539 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 921b7f33-8a95-3886-936e-0ffcef40c278 | -17.37413 | -46.66396 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 210afeb7-f45e-32c6-9919-5a2ac738353c | -15.39273 | -48.04527 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0adf759b-4a19-3f08-abe6-cde4f30e1f39 | -14.35893 | -50.76659 | 2025-10-09 04:21:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ebd4e4e-f2d8-3ccc-bafc-72c5a08494ae | -16.28533 | -47.12968 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6421bc06-3c0f-3cab-beab-4feb5e126cef | -15.22517 | -46.38156 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccb788c9-ebe4-351d-b465-f7ff64974a40 | -17.63843 | -47.20782 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f5ed1363-665c-372f-9847-d7826679f51a | -17.47088 | -46.93504 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6c12ced-63c4-318b-9192-92776e5b3354 | -15.48591 | -47.95078 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dad9698-216d-3e36-af89-63d6af477f98 | -17.39321 | -46.88851 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5815c13e-3070-35a1-88c0-571a0dd52b1b | -17.99524 | -45.6212 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c00e8072-a366-3bc3-97f7-fa3cf9f0f4a6 | -15.75379 | -48.74731 | 2025-10-09 04:21:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82cb84be-d898-3413-a0c7-1405cfd2352e | -15.48072 | -47.96132 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c836125-e4ed-30b0-bb84-b53ed3755f1a | -17.62965 | -47.1989 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fbb629f3-960c-32d1-8f3f-e1f0640c3576 | -17.91212 | -57.50686 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 9a9d6e68-797a-3208-9bfc-00e1a473b52d | -18.30594 | -45.43798 | 2025-10-09 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 151abaa9-62c7-3ef8-b7ac-1758f76f71cc | -15.06836 | -46.62186 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abf9857f-2072-374a-b910-7869e2a59a20 | -17.89221 | -42.86935 | 2025-10-09 04:21:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f64019fd-1d3d-3733-889e-07f8a9264885 | -15.21911 | -46.37691 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa5f9daf-5ad0-36a3-865d-6fde7a8fa24d | -17.38219 | -46.89496 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da32436a-93c0-3f8d-8e55-363232281f04 | -18.04147 | -44.45074 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71d3e335-c503-3fde-9331-c78ab5e774cd | -14.93705 | -46.78631 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c5b6f0f-1e79-3fbf-ad94-120e40db0574 | -19.71865 | -44.0055 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96013c67-03ef-31dc-804d-8047cdffb5ca | -15.47614 | -47.96812 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README46.md)
