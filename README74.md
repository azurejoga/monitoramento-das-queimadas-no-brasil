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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d7ed13c-4715-3bb2-89d2-b70de30f8b81 | -13.1694 | -51.4471 | 2026-08-23 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 32c0eeaf-32d1-399c-8f85-f91d3ad4b323 | -10.3902 | -50.3984 | 2026-08-23 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| f12538ce-24e3-38fb-9f97-9da12e92a0fb | -7.0006 | -48.012 | 2026-08-23 12:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d4e266f4-37fa-3fcd-9b8b-6fea6c134187 | -12.3004 | -43.1541 | 2026-08-23 12:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 115.2 |
| 39448333-703a-312c-863a-10bb1ab15aba | -12.2613 | -43.1845 | 2026-08-23 12:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 37109079-ff55-3488-91e4-a0e395e3e734 | -14.5659 | -53.0292 | 2026-08-23 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 118c5eb5-f0df-34b9-8070-907cec54b35d | -12.281 | -43.1574 | 2026-08-23 13:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 854569fc-f71e-3674-b423-3e3b200cc34c | -10.3902 | -50.3984 | 2026-08-23 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| cbbed73d-92c8-376b-9198-5429c430d626 | -12.075 | -50.5974 | 2026-08-23 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f0e0b39d-d329-3dce-9848-c7e5ef6c3c81 | -14.5852 | -53.0268 | 2026-08-23 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c97a54d5-323e-359b-978c-be42b7142bf3 | -13.1694 | -51.4471 | 2026-08-23 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 8d2200aa-42db-3dee-8c1a-201ba7af0845 | -13.1886 | -51.4447 | 2026-08-23 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| cc012f2e-e320-349c-bd8b-84709ee98996 | -12.2806 | -43.1813 | 2026-08-23 13:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 200.3 |
| e6690f5c-dddb-3f9d-821f-041bc07bd423 | -16.0509 | -50.4363 | 2026-08-23 13:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 35616d54-a2b4-36c6-9b74-383171996f2d | -12.2613 | -43.1845 | 2026-08-23 13:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 9b2325c9-a9f3-35f2-b6ae-e6392e632bbb | -7.9654 | -43.9274 | 2026-08-23 13:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 2c189bf0-aa24-390b-98f9-875e3d7dad0e | -12.0559 | -50.5996 | 2026-08-23 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 428919e0-337b-3bdd-9d3e-f03db8a7531a | -13.1505 | -51.4281 | 2026-08-23 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 53da46a1-8da8-3433-bb04-7c8d557fa84d | -12.2999 | -43.1781 | 2026-08-23 13:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 126.2 |
| 8fdd9dcc-e1b5-39ea-8a6b-cd9760ad335b | -7.9865 | -45.2801 | 2026-08-23 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| dc7b7b45-8586-3f8d-9377-bb9db35e3a66 | -10.4905 | -49.9604 | 2026-08-23 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 0c2fbbc0-3120-3af9-baa0-d2ed76931427 | -7.9868 | -45.2573 | 2026-08-23 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 00b80a8e-e88c-3706-b037-8f819df7a598 | -11.638 | -50.5625 | 2026-08-23 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 1d03cd3b-9cb0-35a5-aa96-48c774b9cea3 | -11.5804 | -46.9369 | 2026-08-23 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| a9df7d3d-1531-33c1-92eb-f83c20ed0fbf | -6.1285 | -57.8393 | 2026-08-23 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 01a878c5-5a10-3d88-99c7-dbc4f40fab32 | -11.7852 | -47.2453 | 2026-08-23 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 89dadfb9-bda2-3c98-a155-5a7653e47f4e | -9.1332 | -65.9559 | 2026-08-23 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 78ea8658-84bd-37dc-8d52-1887181449f5 | -12.2806 | -43.1813 | 2026-08-23 13:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 239.3 |
| 061cd1d4-d343-3076-8486-ec7dd888280b | -14.3168 | -51.7901 | 2026-08-23 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 01014759-b75a-3b28-a8e3-afcc29551ecc | -12.2999 | -43.1781 | 2026-08-23 13:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 99.2 |
| 8763d44c-d348-39c0-be47-78c68ddc8d72 | -11.9872 | -45.5187 | 2026-08-23 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| d32626ca-f32b-396a-8bce-1fca74e96f44 | -11.5804 | -46.9369 | 2026-08-23 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 3a985c77-178e-333c-b1be-7f815ab28e07 | -16.0509 | -50.4363 | 2026-08-23 13:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 61f31c6e-c34e-35cc-95fb-321fbd07b1dd | -6.1285 | -57.8393 | 2026-08-23 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| eb489e44-c2e4-364d-8831-07f30d9b675c | -14.3365 | -51.7662 | 2026-08-23 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| befe07d6-775b-3e73-80c0-abe75292a268 | -12.281 | -43.1574 | 2026-08-23 13:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 29474a3d-2208-33e0-9d8e-fb4b7f17564b | -12.0559 | -50.5996 | 2026-08-23 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 7b597361-df46-32bd-9549-b2ae5c2c4145 | -14.2337 | -52.1415 | 2026-08-23 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 0e8aa36f-4c0f-306a-819a-fa260430559a | -10.4905 | -49.9604 | 2026-08-23 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 8888693f-291c-3001-a99a-75116ceb932b | -7.9868 | -45.2573 | 2026-08-23 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 3764baf2-b814-305d-8eac-2283ae0b7873 | -15.5368 | -53.9763 | 2026-08-23 13:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| e5d1775f-808f-3c1e-9822-9f37d5353edd | -12.075 | -50.5974 | 2026-08-23 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 95454e63-45b7-3f44-a1e4-43a6f8c8825a | -10.8358 | -50.9903 | 2026-08-23 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 475a90d0-e005-3268-aaf6-4158dd9eb281 | -12.281 | -43.1574 | 2026-08-23 13:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 45cae5f6-5453-3c86-8a2c-6c5570fd1c49 | -14.5659 | -53.0292 | 2026-08-23 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| e0cf1a6d-ee2c-3e14-a4a0-856f6306d87d | -10.8174 | -50.9498 | 2026-08-23 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| fc2731eb-1ae8-3524-8174-727facd8effb | -12.2999 | -43.1781 | 2026-08-23 13:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 105.8 |
| e2d1ee05-0861-3749-84b2-7150aa9ec56c | -10.3902 | -50.3984 | 2026-08-23 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 3f38a97f-8cae-3891-ae4d-67b14b9b7cc2 | -10.4905 | -49.9604 | 2026-08-23 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4b74eced-73b2-3bb9-ac1c-d9ae4854493c | -11.5804 | -46.9369 | 2026-08-23 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| fb9b4ce0-e71b-338c-8c05-9b2491aa8d19 | -11.7852 | -47.2453 | 2026-08-23 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| ca44e0a0-6be5-3cb0-a7ef-dd06bdaecd15 | -16.0509 | -50.4363 | 2026-08-23 13:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 600a26bf-0b9e-314f-b392-1f3b1f47cfb3 | -10.8355 | -51.0116 | 2026-08-23 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 2b6f6922-f29a-359c-8390-312b672ef195 | -6.1285 | -57.8393 | 2026-08-23 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| d5bf85ed-4c6b-3b94-9be4-2cc04173cfcb | -9.1332 | -65.9559 | 2026-08-23 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 669e6466-2740-31ea-80b6-13180e0a25a3 | -12.0559 | -50.5996 | 2026-08-23 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 9b387afd-df26-31e9-b76e-5ea1973621dd | -12.075 | -50.5974 | 2026-08-23 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 9c55a37e-1d7c-3c55-98bc-8cf36385f30a | -10.3899 | -50.4198 | 2026-08-23 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 69169694-4e43-3289-bc72-203d418cfb57 | -15.2462 | -52.8349 | 2026-08-23 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 29505201-fae3-39bc-951b-c6bcc9df2457 | -15.2462 | -52.8349 | 2026-08-23 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| b94bdcb2-a9e4-3e6a-8533-e98da5a90f6d | -6.8992 | -55.6977 | 2026-08-23 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 98efd658-0c33-35bf-8027-785b04d480c0 | -12.075 | -50.5974 | 2026-08-23 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e42b7912-8757-3a72-9c9a-486abc7acc37 | -15.2278 | -52.7738 | 2026-08-23 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c29bfa97-0867-3b3e-b25b-6272572114ea | -10.4905 | -49.9604 | 2026-08-23 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 587e8693-bcd6-325b-bf8f-5a4d743f889c | -11.8497 | -51.6859 | 2026-08-23 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| d9525e32-0f29-3720-882d-bf07322f5bae | -14.959 | -52.6402 | 2026-08-23 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| efda3cfe-79b4-3f0f-987f-fca8d2eb2930 | -12.2999 | -43.1781 | 2026-08-23 13:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 161d0c3c-e039-3f92-ad36-6868792ac348 | -9.1332 | -65.9559 | 2026-08-23 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 7716fc72-0093-35e4-a890-cfc82a4c1d43 | -10.8174 | -50.9498 | 2026-08-23 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| ae51afb6-f534-33ae-9639-a04f385af112 | -10.8547 | -50.9884 | 2026-08-23 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a409fdb6-7a34-37dc-8560-01c4e31101a8 | -14.3737 | -51.8466 | 2026-08-23 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 7bd4994b-4da9-35da-8284-68420a35e36b | -13.8384 | -54.0158 | 2026-08-23 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1b9a7e89-d724-33e9-83c2-ca29c990660c | -10.8358 | -50.9903 | 2026-08-23 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e710f54a-7b7f-3489-a3c6-a9e5f21d912e | -14.9586 | -52.6614 | 2026-08-23 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 1ce47be3-8478-3083-ab06-7ad6e3e6bf5f | -12.8554 | -48.4541 | 2026-08-23 13:30:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 408bdcce-eb43-389b-9501-b2c1e971a226 | -16.0509 | -50.4363 | 2026-08-23 13:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b9d9ab46-4292-30f8-a679-f40afdab4f93 | -12.281 | -43.1574 | 2026-08-23 13:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 122.4 |
| 7ff8fc67-fbf3-3e1f-9107-cf0f4ba6bebf | -6.1285 | -57.8393 | 2026-08-23 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 81f8ad99-ddad-3b9f-939b-517b1e9ea3dc | -12.855 | -48.4762 | 2026-08-23 13:30:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 99878491-a10a-3bf1-993b-12cb95ffb428 | -10.3902 | -50.3984 | 2026-08-23 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 749d41fc-2cbf-393e-ba5c-d32f2463c08b | -10.8364 | -50.9479 | 2026-08-23 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d43feb4e-b2e6-3209-a4fb-2430c0c804e6 | -11.85 | -51.6648 | 2026-08-23 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0a25bfc8-10e9-3f29-8804-9a52ead54acf | -11.5804 | -46.9369 | 2026-08-23 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 45638a67-d09d-3f13-b9c9-afd594f24ef8 | -14.2337 | -52.1415 | 2026-08-23 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d3f7fc53-8f64-3ed1-b028-f8984927ba18 | -12.2806 | -43.1813 | 2026-08-23 13:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 246.2 |
| 5d47b229-fd64-3fe4-890e-6a0822558cfb | -10.8361 | -50.9691 | 2026-08-23 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 152.5 |
| c8bf129c-ba3c-3388-8879-4eece619f180 | -10.4905 | -49.9604 | 2026-08-23 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 493cf0e9-6132-33ec-9d86-c85b8a81fb96 | -12.8554 | -48.4541 | 2026-08-23 13:40:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1f27b0f6-a1dc-35b3-9e4f-cb090fa26e8c | -9.1332 | -65.9559 | 2026-08-23 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 083d9d94-aa59-3c7f-aa1f-a27346af00f2 | -16.0509 | -50.4363 | 2026-08-23 13:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a4d3c087-03e0-3767-8712-1eab6a167278 | -11.5804 | -46.9369 | 2026-08-23 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 311524fa-4694-3fe8-bb60-088ceb2f00a1 | -8.56 | -54.7377 | 2026-08-23 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| adc5487b-b78f-3c5a-a853-9bce6102cc0d | -11.7852 | -47.2453 | 2026-08-23 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 2d0b6a2c-85b6-32b6-baf6-459329c80c24 | -15.2462 | -52.8349 | 2026-08-23 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 37097a5e-b34e-358f-84be-899e4e997d1d | -11.8497 | -51.6859 | 2026-08-23 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 229.7 |
| 5dae8d78-77cf-3c53-8a8b-8273616ef4e8 | -6.1285 | -57.8393 | 2026-08-23 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| aa34e783-f603-347a-974e-90e420896874 | -11.85 | -51.6648 | 2026-08-23 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 201.7 |
| f9cfd4b9-d1b5-31f0-877d-16f9746723e9 | -10.3902 | -50.3984 | 2026-08-23 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 7d0367cb-f5a0-3642-8507-9b39d4b3c078 | -11.5613 | -46.9395 | 2026-08-23 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 17e55861-7d6a-3da9-a7c5-6aa6fc8055ad | -6.1286 | -57.8198 | 2026-08-23 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |


[Clique aqui para ver as próximas entradas](README75.md)
