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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f1fed9d-5308-374d-83f0-65a8bbe78b2d | -9.60704 | -55.14591 | 2025-08-14 04:49:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d94dd35-bc0f-3a75-83e2-9bad1b574796 | -7.59959 | -63.52238 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49fcb57c-ea4d-38a2-ae5e-3625d5bd19b4 | -9.18168 | -59.66219 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 60d26821-dc18-3342-9efa-2a9a970ea53f | -9.5035 | -60.52821 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 057cf377-5f97-3b47-aedc-d6915ed0a5a4 | -7.6318 | -63.52251 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed408e87-7dd5-3731-a294-68e2505a8d3d | -9.15193 | -59.65686 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4375e2e1-d2bc-3010-9f46-b3edeb9d7cfd | -9.50164 | -60.51143 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3eafc9c-9142-32de-9f47-5d2804599e2f | -10.36064 | -50.81302 | 2025-08-14 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d94ba792-c7a3-3ad3-8a45-1b912a6f8b53 | -9.1637 | -59.67667 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8687b1e2-5dd6-3840-b26f-7bdbc1e6d246 | -11.03738 | -55.3754 | 2025-08-14 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dda36003-5543-36ec-bfb8-5a0bef43185f | -9.18268 | -59.65665 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0e40199-2d4d-3522-a83e-ce3d2e8319a2 | -9.18355 | -59.68029 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| da756592-79c7-3b0f-ad75-79dda157e0d7 | -9.50128 | -60.5113 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 322f33ef-aa0c-354a-8960-33b96ed4f588 | -8.92396 | -60.73219 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17ddb2dd-d1e1-3ec9-b8b3-7cc502cb5e0c | -7.88381 | -61.80396 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71672b9e-eff0-313f-8b4b-27fd98d11749 | -9.12878 | -59.66891 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9470a48a-afbc-31b9-8499-5797ae49a72b | -9.50049 | -60.54426 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98a677c0-c955-3d09-b850-5a8276e87daf | -7.55286 | -63.48475 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e1db152-828e-3462-859b-f348618c9e78 | -12.58698 | -46.97646 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5d59d25-29d1-3df4-8ad5-3357427da987 | -9.49819 | -60.53058 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 067e3624-6678-3de3-96c1-1d7248ad464a | -7.87331 | -61.82784 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b7b832eb-9f26-300d-a0d0-888824c2c951 | -9.21442 | -59.65209 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fca44337-cae5-3b13-929e-0d4e90ba6f1d | -12.32205 | -46.05069 | 2025-08-14 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 269ef36b-80b1-34d7-a403-26b6af42b27a | -9.20839 | -59.65587 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa79c5d3-6a0e-38cd-81c1-33ad5bd007fc | -13.43704 | -44.49784 | 2025-08-14 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 061a2cae-7f19-3f48-bf84-78ecb8d727c3 | -9.06583 | -60.65171 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ff5bba6-2a71-30cf-ad0d-1a76e670bab9 | -12.58435 | -46.96487 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c71700fb-639a-3016-8cb9-ce7377d0dedd | -7.87642 | -61.81124 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8b374149-dd8d-30ba-9a6d-3b2287880d75 | -12.42335 | -48.69677 | 2025-08-14 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8aefb0b2-8025-3d4a-891a-5123accb8f2c | -7.55373 | -63.48351 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec79f550-4e89-3010-a218-5e40b68eeaaf | -11.7546 | -50.11545 | 2025-08-14 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ff7e491-40e4-3911-90d2-507fa57186e1 | -12.35 | -49.91538 | 2025-08-14 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87b70555-d0b9-3175-a7de-7f62b8ccc34b | -12.32033 | -46.06343 | 2025-08-14 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7616ad5e-269d-32d4-929e-9a56054efac2 | -9.1449 | -59.66732 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bf2c82aa-be9e-32d9-9b5a-9b413df814ae | -12.57567 | -46.96692 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50246dc6-4774-37ae-9ccc-56860c55131e | -9.16472 | -59.67102 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf2d8865-a3e4-3779-9238-8930c5943fdf | -9.19054 | -59.66985 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8fc7682-5c2f-3a9f-8448-61215031cb6f | -8.11409 | -61.20399 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22a2379b-dad9-3a07-8aa2-9b20a9090b79 | -9.06053 | -60.65068 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81e03f10-ac34-3fae-a629-31bd54496cfa | -8.92992 | -60.72976 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6dc4942-b661-3630-b0b1-6680bd9953e2 | -9.82712 | -60.76023 | 2025-08-14 04:49:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8501a136-493d-3d50-a1a0-2dc84e0a9ec4 | -12.68644 | -44.95362 | 2025-08-14 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 798ef3e9-2451-3df5-ab3c-48f2d620f043 | -9.5041 | -60.52502 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1516db1f-54b3-39b7-ae81-a8d79886facb | -7.87422 | -61.82961 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30b4cc26-b4b2-3b32-96c7-8cfae2a172e4 | -9.1548 | -59.66926 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fdaeaa16-128b-3eea-a932-5678e24aa45f | -7.87489 | -61.81942 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 026aa530-a517-313c-aa1d-b61588c5194a | -7.86982 | -61.81423 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5a3817b7-2282-3bfa-ae15-200096cdc96a | -9.19752 | -59.65948 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93dc57b7-03da-34b3-9f06-3c990b89e2e5 | -12.58027 | -46.96399 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccd2895a-30a3-338c-989a-57b6642b6498 | -9.12978 | -59.66319 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| da764185-2cd6-3510-8183-340de1c747da | -10.35672 | -50.81607 | 2025-08-14 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0c272a8-4df8-3cac-8a77-abae418d4243 | -12.3209 | -46.05919 | 2025-08-14 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b29e232b-a9f0-3b7d-9831-07c1a44bd2d5 | -9.50107 | -60.5146 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a46fc12b-44e8-3419-b0da-25d8b46540f9 | -10.35839 | -50.80533 | 2025-08-14 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67b620cf-4ba4-312a-8b66-9c1a610d77fb | -7.87995 | -61.82463 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 023d9d9f-48d1-3d0b-925c-915fd5631222 | -9.2094 | -59.65019 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bd6de5d-c05a-3254-bb2d-c5868a97cd8c | -9.50167 | -60.5413 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32621da5-2eef-3192-9c2e-1f58dbc66866 | -10.36175 | -50.80586 | 2025-08-14 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12ba9d80-9a29-3d56-ac8e-e33f23073e2b | -12.58486 | -46.9611 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2abf11f3-0e79-366a-befb-2c584e3db4ac | -9.71928 | -56.17975 | 2025-08-14 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5dcf006-2507-3f79-a67a-f67f040fbdb2 | -10.34794 | -57.59291 | 2025-08-14 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dba9f8e2-0ac8-35b4-963c-196112f77b82 | -8.10501 | -61.19066 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5caf579e-65b6-3f7a-8d3f-fe0580597ab3 | -9.18953 | -59.67553 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e2b37ec-0069-3d97-ac6b-ad04c0377770 | -12.35349 | -49.91592 | 2025-08-14 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| affdcb12-6aa8-3466-8c56-a454028d46f0 | -9.15791 | -59.65214 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e40b219-bd06-3434-b7db-25b06c891fcb | -9.15584 | -59.66352 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 679fb8d6-b8f4-3f94-8d37-a808aa66a052 | -13.43635 | -44.50344 | 2025-08-14 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ffe59f7-11e1-3934-8f53-37c43502f4bf | -9.14985 | -59.66828 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b401cc57-3c43-3907-b6d6-90de4f7f9d1c | -13.07395 | -49.33049 | 2025-08-14 04:49:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa6e4cf4-b7d6-3b71-b722-a54d5ff4546c | -7.8741 | -61.8236 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4554bf27-c8a3-3820-b329-7ae836561443 | -10.09668 | -50.31096 | 2025-08-14 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14b6837c-fab4-3d4c-b7a4-c9f96c9cf025 | -8.11341 | -61.2077 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c5ce27ef-8aa0-3747-a862-14b7ea931f46 | -7.60063 | -63.51688 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f3e2a5b-c989-3bc7-9655-ce1b46e8733a | -12.57669 | -46.95938 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5342bcf9-5e6a-399c-a818-7ebf2d8706a4 | -9.16182 | -59.65879 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d8ad82d0-3192-30d0-a3d3-2c34e608bdbc | -11.68512 | -51.61857 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14aa629a-60f8-3326-a44c-13ae8cdb50da | -8.10989 | -61.19548 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d8b85680-1d02-3693-b954-2de037d3ae1d | -11.3193 | -55.2082 | 2025-08-14 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae3bfd67-37af-3930-a35b-eab2488186d1 | -9.15035 | -59.41621 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ffec99d-e794-3625-b99c-ee90cbe44c81 | -9.4989 | -60.52396 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0677519-6246-3d48-9e84-14b3ced2636a | -12.02553 | -43.62682 | 2025-08-14 04:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c53dbccd-afd2-3c4e-bf81-9c564b10d8bf | -11.66636 | -51.71699 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ae77f30-1bb4-363c-8d2e-a659376b5319 | -9.12898 | -59.67032 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5daf69b-f728-34c0-a373-0028bfa11434 | -9.50456 | -60.52522 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1de83e66-e48e-399d-856b-eeee209e772f | -7.62012 | -63.52068 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ff3eabe-258e-3eb0-a493-f83548277635 | -12.30225 | -50.01963 | 2025-08-14 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c3376e3-9060-3dd3-bc1e-68e384193861 | -10.36454 | -50.80996 | 2025-08-14 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9780142-6326-3253-87b5-d81aa29d966d | -9.20949 | -59.65112 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c749aae7-808b-3691-ae29-94c3c7d33d49 | -9.50187 | -60.50812 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24667d57-0fb3-326a-90aa-1ebc917b0bb7 | -11.31126 | -49.95591 | 2025-08-14 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e28a5df-13c2-3383-81aa-78bc9aae56bc | -13.43478 | -44.50221 | 2025-08-14 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d38c2bff-1bcf-3bbf-afab-1cb62c02c10a | -9.13707 | -59.65411 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f7090c0-0005-391e-b61d-8fe7115f5e50 | -9.50224 | -60.53811 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fdd15892-a42c-3021-839b-242442ef6d92 | -7.61362 | -63.51941 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6e2785c4-1e79-3780-b1f1-0d639157ce5d | -7.55935 | -63.486 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1387522-878d-37c1-bc4a-26fc54da4023 | -12.57767 | -46.95206 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6980a9de-8bb2-366a-9a8a-bc925964f601 | -12.0204 | -43.62617 | 2025-08-14 04:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 996db46b-fe7f-3d45-aff2-6c5de4cb33bd | -8.11273 | -61.21139 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6248d963-f102-35bf-b819-0787e0d540b6 | -8.10851 | -61.20294 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53c7bd0d-834a-3e6b-87dc-36c7970c4c38 | -12.32641 | -46.05134 | 2025-08-14 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
