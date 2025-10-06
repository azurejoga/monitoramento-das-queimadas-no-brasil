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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b42f6887-e33a-3001-a62a-8a9ec4208ea2 | -14.6806 | -48.37682 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 04d09002-5718-357c-9ed5-4ac2209e8e7f | -13.68477 | -47.35553 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82f34198-eb7c-3bd0-a1cf-a532f808c373 | -13.68345 | -47.36183 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7217a1f9-ecd2-3095-98fe-97951287c010 | -15.14353 | -45.72511 | 2025-10-06 03:38:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb681dfd-df04-34e2-9955-0fcc858cdc07 | -15.84261 | -43.31016 | 2025-10-06 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40f9f395-8dd6-332e-afe2-790abb98dd92 | -14.54676 | -46.66129 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65f78496-0db3-39f6-9223-7ea5a6442f7d | -15.3437 | -47.35528 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70e77796-51bd-300b-8b3d-48ddb1fa7c7e | -21.39258 | -45.08187 | 2025-10-06 03:38:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 1722e1c1-75fb-3834-8446-996b5291c595 | -13.49653 | -47.25543 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1cabec55-be0a-3e44-9b65-144f6ed8e3fd | -18.27588 | -45.41831 | 2025-10-06 03:38:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dee8052-4c7d-34ec-9d51-ac863e511c3e | -14.67506 | -48.40252 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b58ddc30-7302-31d7-b35a-d8de7a4d5c9f | -14.90868 | -46.85185 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 891b0d91-e8dd-3e7c-97bd-dd12924eaaf9 | -15.34354 | -47.35333 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4ad52b7-f75c-3689-aacb-04cf0bf370fa | -15.74125 | -46.25984 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cfbe5ba-513d-3c33-957c-956b5c26490d | -14.54185 | -46.96478 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c32333b9-c363-37ba-8ce0-501a98a9c456 | -13.29693 | -48.07284 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c09cdc69-9776-3bdb-96a9-fe558c7ed023 | -15.29373 | -46.32624 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5816b9c7-2f6b-3e24-98a3-56ed4d8c01a5 | -10.4099 | -50.3324 | 2025-10-06 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 5cfad1f3-759f-3e50-9dab-4fb07a8e6d2d | -18.1167 | -53.3977 | 2025-10-06 03:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 69878a2d-12bd-3eed-bd97-a9439a0d7d56 | -8.6327 | -46.3208 | 2025-10-06 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 076ed919-f016-34c4-bf27-e8756f27d07d | -10.4285 | -50.3518 | 2025-10-06 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| dc9e0e68-8d66-3f8a-ba7f-20f75a93cd62 | -17.8617 | -57.6024 | 2025-10-06 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 1cd75b8e-f2a4-367c-beed-f44d19b03c20 | -12.8954 | -47.2909 | 2025-10-06 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 30b60eff-0d22-3112-a639-68f5d7a979aa | -10.391 | -50.3344 | 2025-10-06 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a568d35e-7a71-387c-9da8-0a23c9746fc4 | -10.3162 | -50.278 | 2025-10-06 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| cfb8ebf5-1465-34cc-80b3-3fe2ad1e41a1 | -8.6139 | -46.3227 | 2025-10-06 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b582a45e-f70b-3fa1-a256-dabbb50a39a3 | -17.9813 | -57.5262 | 2025-10-06 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 2d248615-fc0e-30f8-b5d6-8678258a3c6d | -18.1366 | -53.3946 | 2025-10-06 03:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 774bdc58-81dd-32af-b275-bea4ce273c66 | -17.8621 | -57.5818 | 2025-10-06 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| f1592cc5-5715-39d4-ab85-7afb56f07d01 | -23.7362 | -51.9193 | 2025-10-06 03:40:00 | GOES-19 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 91.1 |
| 5f06bc3c-d556-3faa-a760-7c8e821fb063 | -10.3165 | -50.2566 | 2025-10-06 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 509976db-4087-3da8-8c6d-8fd9bec96b64 | -17.981 | -57.5468 | 2025-10-06 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 8e68988a-0262-39c2-8277-1914fb49eadd | -23.39157 | -45.38984 | 2025-10-06 03:40:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e80a20c3-b79d-3ad4-a75a-a8252d6e6c8a | -22.60208 | -44.68716 | 2025-10-06 03:40:00 | NOAA-20 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 6c5e7d70-fa22-3132-92f1-4fefb74de3c9 | -22.96792 | -47.60473 | 2025-10-06 03:40:00 | NOAA-20 | MOMBUCA | SÃO PAULO | Brasil | 3530904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d4f28951-bee6-35c2-81f0-bff895fa70e6 | -21.61657 | -45.29372 | 2025-10-06 03:40:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e0b76e48-fe8c-392f-9391-b20c2e815f4e | -23.19051 | -47.24641 | 2025-10-06 03:40:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 76c065c5-fe6c-39fd-9204-8b99cae15d7e | -22.28941 | -49.91578 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 11bde996-c043-394f-b144-390f164af325 | -22.57853 | -44.87077 | 2025-10-06 03:40:00 | NOAA-20 | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 79d3af7d-3251-3c20-b066-cdab1a7a43b9 | -22.85712 | -43.31294 | 2025-10-06 03:40:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6ad5efc9-55c8-3287-964e-007cb3df5370 | -22.377 | -50.02015 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8db9402b-da62-3fe7-9cc1-ae73ef5a7ef8 | -23.83913 | -48.52643 | 2025-10-06 03:40:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f475d5f5-943c-3023-b659-770310796556 | -23.58176 | -50.27596 | 2025-10-06 03:40:00 | NOAA-20 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4cdecb03-27a8-3d14-9b9e-e3b5a728b844 | -21.94715 | -46.45944 | 2025-10-06 03:40:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2d3fb46d-d3f2-3be7-8721-f6c9bdd8bc63 | -22.28784 | -49.91042 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 04a8b12f-aaeb-3526-9c65-7cfd0a8bce4e | -23.43154 | -45.47772 | 2025-10-06 03:40:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c4d90e32-350b-3cc7-8ff3-f1fcb2968491 | -23.44074 | -45.48053 | 2025-10-06 03:40:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3d883ce3-11ac-3516-99a5-b38039af0dd4 | -23.52616 | -48.29045 | 2025-10-06 03:40:00 | NOAA-20 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7d1415cc-deb6-3899-99c2-f7fe62120cb9 | -22.36147 | -44.21483 | 2025-10-06 03:40:00 | NOAA-20 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6734b0b4-3457-3cdd-a56c-6f430fffd22c | -22.90076 | -44.7159 | 2025-10-06 03:40:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8c45a9de-519d-31ca-bbe3-7b6e3c865f90 | -22.97239 | -47.61001 | 2025-10-06 03:40:00 | NOAA-20 | MOMBUCA | SÃO PAULO | Brasil | 3530904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bb6e7ea3-a71c-393b-9f03-3a8886be73c2 | -23.52552 | -48.28659 | 2025-10-06 03:40:00 | NOAA-20 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fc1a1f9c-f6ac-3df4-ad30-5c59e730a8d6 | -21.6034 | -50.96321 | 2025-10-06 03:40:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 17ed2d55-d43b-3898-b330-c725cdce2e7c | -23.57993 | -50.27544 | 2025-10-06 03:40:00 | NOAA-20 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aecabda7-448f-3325-909f-0115961f1cce | -22.36588 | -44.21581 | 2025-10-06 03:40:00 | NOAA-20 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 394a244f-9fd5-328b-918a-c2bbb762780f | -21.60094 | -50.95546 | 2025-10-06 03:40:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 57e469a6-be30-3ff4-8f6f-722480a2dfa0 | -23.18682 | -48.97436 | 2025-10-06 03:40:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89cf0bad-0361-386a-94c2-e04c8425469d | -22.64524 | -43.80418 | 2025-10-06 03:40:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9a0fd949-186b-362a-accf-6796d0f6a4bc | -22.36247 | -44.20992 | 2025-10-06 03:40:00 | NOAA-20 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 75eab521-87f6-3264-8f9f-e48d2a5c683f | -22.29065 | -49.91055 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 01bc1c0a-7072-32f0-a3c6-b344db48003d | -22.95365 | -46.13223 | 2025-10-06 03:40:00 | NOAA-20 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3d510422-ea3c-39e4-8f56-4af573724439 | -21.61182 | -45.29247 | 2025-10-06 03:40:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c73ea38a-8499-3d12-9437-150e5ab5f312 | -22.36552 | -50.02614 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| cd0ea1f2-3b73-3940-b34e-e9e70005c508 | -22.70166 | -44.87376 | 2025-10-06 03:40:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bb38bde6-21ae-3df6-8206-02db924f7090 | -22.54459 | -44.21312 | 2025-10-06 03:40:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dfb63048-666e-31c4-a517-9dc487e709cc | -23.33067 | -46.78994 | 2025-10-06 03:40:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 70491116-042a-34dd-a673-5900705fd1b0 | -22.12308 | -45.00625 | 2025-10-06 03:40:00 | NOAA-20 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b398d014-ae51-3289-a117-3a1b0928433d | -22.1219 | -45.01199 | 2025-10-06 03:40:00 | NOAA-20 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 00461290-36cd-3ed3-aa59-8224d5083a7e | -21.70711 | -50.0827 | 2025-10-06 03:40:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f6901f22-0a4c-3728-ab8c-f1df32ca6d22 | -21.60586 | -45.29701 | 2025-10-06 03:40:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| da591e8e-37b4-390b-af58-600f33260660 | -22.52598 | -43.57284 | 2025-10-06 03:40:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| acb51ee4-18c1-346b-b1de-dfa8e90d9cec | -22.37212 | -49.97058 | 2025-10-06 03:40:00 | NOAA-20 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7b6f40db-bc93-3515-bc28-ee0e2db7d6fd | -22.8605 | -43.31767 | 2025-10-06 03:40:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a8dd5813-339d-33bc-83f3-df8edba7f8f0 | -22.70622 | -44.87483 | 2025-10-06 03:40:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 443c24a0-d49c-3860-9008-a2724de1a6a3 | -22.86132 | -43.31356 | 2025-10-06 03:40:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0de1aaca-ee67-3fe9-9eaf-4dc8bdabae65 | -21.59931 | -50.96201 | 2025-10-06 03:40:00 | NOAA-20 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| fb413a7a-8254-3c34-8332-88ffec43ff24 | -21.60708 | -45.29116 | 2025-10-06 03:40:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 58404489-9627-30b9-9156-a833c74e38b9 | -23.58426 | -50.26566 | 2025-10-06 03:40:00 | NOAA-20 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 85858fc5-c27c-33be-aa45-df0abc61d9e1 | -23.58723 | -50.27247 | 2025-10-06 03:40:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ad633c62-b969-3736-a6f6-8fc32fb5983d | -21.94784 | -46.45621 | 2025-10-06 03:40:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 790c3529-2c14-366e-863d-e47419d2f959 | -23.43049 | -45.48271 | 2025-10-06 03:40:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 19418a3f-cffb-3fda-8279-ae708b303803 | -22.56825 | -43.6428 | 2025-10-06 03:40:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6b07f7ff-90f2-32ba-b8b3-3555c8e553af | -23.58248 | -50.26522 | 2025-10-06 03:40:00 | NOAA-20 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7617fc24-67ff-3220-bd59-21b153492339 | -22.56748 | -43.64661 | 2025-10-06 03:40:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 70635456-1dc5-3b0b-81ed-0ab44a274467 | -22.97593 | -48.3471 | 2025-10-06 03:40:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| af8ce924-8a19-3bcf-bbb9-e6ac656d7c61 | -21.69586 | -50.095 | 2025-10-06 03:40:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| acf4adf5-af67-30ac-be03-ba4cf6177f0e | -22.38821 | -50.0284 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| edfe5aee-18cb-323d-84b9-0b1ce9f83e21 | -22.57751 | -44.87573 | 2025-10-06 03:40:00 | NOAA-20 | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 5acddbf6-277d-3f6b-8f15-c6c9ee372fc6 | -22.29496 | -49.90818 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3e0637dd-06c0-3c31-a8a9-2e025115f0e6 | -22.37304 | -50.02226 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 28169e33-d013-371e-9648-40073b0848dc | -22.98618 | -46.14878 | 2025-10-06 03:40:00 | NOAA-20 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d9b8e80f-e312-3da4-8402-b1800278d464 | -21.70077 | -50.08113 | 2025-10-06 03:40:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 068d31a2-c6cb-3a25-9aa0-cd83eebebc04 | -23.33646 | -46.7879 | 2025-10-06 03:40:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2b30cc9a-e400-3874-af21-467f97dbfda1 | -22.52672 | -43.56905 | 2025-10-06 03:40:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 70b27854-70d3-35e0-99ef-3615b52f9960 | -22.29376 | -49.91312 | 2025-10-06 03:40:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e258563d-d08b-3f4e-a440-cc97934e9a5b | -23.58852 | -50.2673 | 2025-10-06 03:40:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9e530e24-1ed0-3967-9ef9-0d587a996e34 | -22.7194 | -44.85704 | 2025-10-06 03:40:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6e2c86a2-d9bc-3713-b1f5-802931743eda | -22.45029 | -43.81968 | 2025-10-06 03:40:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c84c807f-73f0-39b1-b210-62bcce2b15a4 | -21.31779 | -48.66785 | 2025-10-06 03:40:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2703adcd-dac8-3a6c-852c-8c214cf7b855 | -23.5246 | -48.29053 | 2025-10-06 03:40:00 | NOAA-20 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README21.md)
