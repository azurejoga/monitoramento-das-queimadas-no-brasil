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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1828c7dd-1ee3-3891-9514-7da7d9e4e2c1 | 3.1368 | -60.7285 | 2026-03-17 01:31:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 781dc2a7-72a0-3d2f-886f-af4e44e59409 | 1.6356 | -60.268002 | 2026-03-17 01:31:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| aef74629-bd74-316a-9ccf-488521a0a140 | 3.1386 | -60.720402 | 2026-03-17 01:31:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e93d381f-3c58-36aa-b8fd-d165a38a237e | -21.715401 | -48.429401 | 2026-03-17 01:31:00 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1d481659-8198-3c25-9c0b-a2af1e8ae7e3 | 0.8391 | -60.328701 | 2026-03-17 01:31:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 10cec694-e319-38d7-ab7e-355add38fbca | 3.1288 | -60.7183 | 2026-03-17 01:31:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 17f88d50-e7a1-3540-ae91-6a93cc1bafc6 | 3.127 | -60.726398 | 2026-03-17 01:31:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7a2cfea2-c3fb-3e27-b4fc-2a9628522d54 | 3.2265 | -61.196098 | 2026-03-17 01:31:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0748c059-b4d4-33db-bb07-9e4a6807c872 | 1.6337 | -60.276199 | 2026-03-17 01:31:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 42be9329-aaeb-38bd-b673-aabe9df99b88 | 2.7303 | -60.432701 | 2026-03-17 01:31:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ff987f3e-0d97-35df-9bee-32bd9940f411 | 2.7382 | -60.443199 | 2026-03-17 01:31:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e405894c-6c72-36c9-920e-99f372b830bf | 3.0866 | -60.7682 | 2026-03-17 01:31:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9c2d040a-0527-3999-9def-9a08ef48fd1e | 3.1069 | -60.8148 | 2026-03-17 01:31:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 88d13709-a4ec-3b3d-902e-137cd5134c8b | 3.1251 | -60.734402 | 2026-03-17 01:31:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6ffb73b5-11ef-32d2-8909-8eccf41b2877 | 2.7401 | -60.434898 | 2026-03-17 01:31:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f123ffe1-5b0a-320b-8e62-010e980bd858 | 3.1404 | -60.712299 | 2026-03-17 01:31:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bed3ac8e-7dcb-307a-ad84-622599319a6c | 3.1306 | -60.710201 | 2026-03-17 01:31:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3179f9af-ffc8-3751-8c00-bf086ba2729d | 0.8293 | -60.3265 | 2026-03-17 01:31:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| aa0d8175-6a15-3cf5-b123-63bfd38dd253 | 3.0097 | -61.107601 | 2026-03-17 01:31:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9244db67-b08c-333c-a383-a3839656f4ee | -21.7097 | -48.409302 | 2026-03-17 01:31:00 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 21302d1f-2204-3926-b921-7a8fd8e20f11 | 1.3225 | -60.692699 | 2026-03-17 01:31:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e409de09-c41d-3ce5-9509-0ecd4fba2094 | 0.8295 | -60.3342 | 2026-03-17 01:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 46.0 |
| c1b60f9f-7b86-3fa8-bb0c-98aed3f2a101 | 3.1277 | -60.7268 | 2026-03-17 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c1635003-dfcd-3042-ad71-606e9cb13345 | -10.0855 | -36.2324 | 2026-03-17 01:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 143.9 |
| ff5d8041-841b-3918-aded-438ba966d545 | 3.146 | -60.7265 | 2026-03-17 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 21dbf077-1c3c-3aac-853c-e2417cdda412 | -10.0662 | -36.2359 | 2026-03-17 01:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 129.7 |
| 447e8352-bc44-328d-a3c6-4777443bdbe5 | 3.1277 | -60.7268 | 2026-03-17 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 29c184b3-ef36-3da2-af37-5c843b56d0a8 | 3.146 | -60.7265 | 2026-03-17 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ada1b016-8039-376e-8f32-839a2d1e7bbd | 3.1277 | -60.7457 | 2026-03-17 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b280b91b-b0c5-3fbc-9bd7-98a5171cb0ca | 3.146 | -60.7265 | 2026-03-17 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 85c5525e-7521-3de4-b780-8258598bd121 | 3.1277 | -60.7268 | 2026-03-17 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 16dfa5c8-2448-3c02-999a-73a3e425d58c | 3.1094 | -60.746 | 2026-03-17 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 803db76d-e079-30cc-9821-32b84d39b5eb | 3.146 | -60.7454 | 2026-03-17 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 12537210-aabe-335e-834a-dc053d5513c4 | 3.1277 | -60.7457 | 2026-03-17 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 151.4 |
| a0198e22-ccca-34be-b41c-3fe4e50c7d30 | 3.146 | -60.7265 | 2026-03-17 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f4471cb1-9a30-3bb8-bf36-44af5f1568ec | 3.1277 | -60.7268 | 2026-03-17 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 91abae31-8cdf-374d-a143-433ce11d0f67 | 3.1094 | -60.746 | 2026-03-17 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 02764b82-001a-3f6b-a8da-62b677e7280a | 3.146 | -60.7454 | 2026-03-17 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a8a6a4b4-6665-3c72-9128-cc8ff77b3641 | 3.1276 | -60.7647 | 2026-03-17 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 179.8 |
| b49ad141-a1f0-318f-994f-94ca921e4d35 | 3.146 | -60.7265 | 2026-03-17 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c2e54d9a-9467-3fcd-b917-ae768ec2d5d8 | 3.1277 | -60.7268 | 2026-03-17 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 48a89cdf-e3ae-3ea5-ad98-aaef385b86e7 | 3.1277 | -60.7457 | 2026-03-17 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 477.6 |
| 632db53e-b493-3721-bc10-3fcd88c3075d | 3.1094 | -60.746 | 2026-03-17 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 09bbd18e-3066-3d99-9309-8c02acc47694 | 3.146 | -60.7454 | 2026-03-17 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d2e03e3a-d3a7-3c96-948c-b1739b73c2b3 | 3.1277 | -60.7457 | 2026-03-17 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 274.0 |
| 6289ea96-b721-3260-8393-65e1fb44319f | 3.1277 | -60.7268 | 2026-03-17 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 3f866328-218d-3284-b308-1a39314925ca | 3.1276 | -60.7647 | 2026-03-17 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 12756217-2238-3bac-8de7-5bcd5da13110 | 3.146 | -60.7265 | 2026-03-17 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| fdd83e6f-2156-3eec-a740-6e4697c32b81 | 3.1276 | -60.7647 | 2026-03-17 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 2733e0f3-edc1-3b92-8caa-29ba3ff2b194 | 3.1094 | -60.746 | 2026-03-17 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.6 |
| aa87f846-0b75-3b4a-9af7-2c9d3e3ebdc0 | 3.1277 | -60.7457 | 2026-03-17 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 275.2 |
| d2f111b5-fcf0-3a34-9595-889b88885674 | 3.146 | -60.7265 | 2026-03-17 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 17563387-11d1-377e-8369-3cba523ef035 | 3.1277 | -60.7268 | 2026-03-17 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 5f950922-48f6-36ce-ac59-26849aa6eab8 | 3.1277 | -60.7268 | 2026-03-17 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e1e39a4b-c240-34b2-8ff2-1c8b69b0fe22 | 3.146 | -60.7454 | 2026-03-17 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 56571a38-d27c-3847-93df-ff14389eab01 | 3.1094 | -60.746 | 2026-03-17 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 1fa2df98-3c32-3734-ab03-72b4a0ac7e15 | 3.1277 | -60.7457 | 2026-03-17 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 232.1 |
| d8ec0e3d-3727-31d2-89cf-a19cd1b46942 | 3.1276 | -60.7647 | 2026-03-17 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 59ae964e-c693-317a-8496-c22475f21b0b | 3.146 | -60.7265 | 2026-03-17 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c8a4685a-4e83-3f37-bc43-c7d5478dece1 | 3.1276 | -60.7647 | 2026-03-17 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.4 |
| af968d12-d7ee-3530-aefd-545bca9731a4 | 3.1277 | -60.7457 | 2026-03-17 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 043f3207-9d06-3940-83bb-2938672c60b1 | 3.1277 | -60.7268 | 2026-03-17 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 0d1a6775-e4d1-3e1e-a18b-083bf1b8d844 | 3.1094 | -60.746 | 2026-03-17 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.3 |
| be1d11dd-4882-353a-add7-3b3f4c3fcd2b | 3.146 | -60.7265 | 2026-03-17 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1a4915eb-c513-30de-b726-e688d5564000 | 3.1094 | -60.746 | 2026-03-17 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 089c51a8-d4c7-344f-bdfa-bcfe03f19f5f | 3.1276 | -60.7647 | 2026-03-17 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 848c7562-b9f2-33a6-8aa4-98725064fc70 | 3.1277 | -60.7457 | 2026-03-17 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 234.0 |
| 3e9aac8f-d50c-3f0d-bc2f-d5a0b964d70a | 3.1277 | -60.7268 | 2026-03-17 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 073be412-69e3-3f1d-ab98-fa0c009ae842 | 3.1276 | -60.7647 | 2026-03-17 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| b13789e3-e5cb-3268-8782-ae7579daeb94 | 3.1094 | -60.746 | 2026-03-17 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1d848378-8b57-37c9-a626-9cef0e4d55dd | 3.1277 | -60.7457 | 2026-03-17 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 180.9 |
| 3daca0ca-8d5e-3b18-a98b-a5c4f2bf4679 | 3.1277 | -60.7268 | 2026-03-17 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 5171a9e5-c614-3244-924e-5e76d3a449a7 | 3.1094 | -60.746 | 2026-03-17 03:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 2bd3a305-e2c3-380a-b06c-224ad1700616 | 3.1277 | -60.7457 | 2026-03-17 03:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 161.4 |
| eec5070d-5f4e-3332-81b9-daf73b5c823b | 3.1276 | -60.7647 | 2026-03-17 03:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 97.4 |
| a05ec66e-a3bf-350f-834f-2751ec2ac0fc | -5.52801 | -35.5225 | 2026-03-17 03:49:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 06aa9c15-f9a0-397a-983f-822cd2a865e2 | -11.74173 | -38.53284 | 2026-03-17 03:49:00 | NOAA-21 | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 875d6c7b-dd65-3ecd-985f-d0f96a5a67de | -7.98796 | -42.83595 | 2026-03-17 03:49:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 38773a45-da20-3197-9274-260f1113fbae | -10.52119 | -38.82328 | 2026-03-17 03:49:00 | NOAA-21 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f1502073-b1ba-3eff-981f-9245a63542a7 | -11.73842 | -38.5323 | 2026-03-17 03:49:00 | NOAA-21 | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 432c3d90-0c6e-3984-8cac-afa2f39fdf4c | -8.35137 | -35.73172 | 2026-03-17 03:49:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3aa536ff-d794-3f26-b7ae-a6e1e11c6cff | -5.1679 | -35.67469 | 2026-03-17 03:49:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ace1cbde-34e3-3220-a975-2798ca1638a1 | -10.08536 | -37.66782 | 2026-03-17 03:49:00 | NOAA-21 | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b0bd0229-3c91-31c4-bf52-ce05311447e6 | -10.08481 | -37.6713 | 2026-03-17 03:49:00 | NOAA-21 | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e462afa8-db4d-3f04-b53d-35e66ddf3f64 | -10.18231 | -39.25327 | 2026-03-17 03:49:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 09a82ed3-926f-3ef6-93c3-a4b37c38443e | -7.98732 | -42.83968 | 2026-03-17 03:49:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc175a5d-f864-31cc-950e-7fbbab55d552 | -5.66763 | -45.20353 | 2026-03-17 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94607e21-b20a-32b4-9742-cbe17fba5a68 | -10.60369 | -39.13924 | 2026-03-17 03:49:00 | NOAA-21 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 936f2bcd-4107-359d-961a-f97aec32f581 | -11.2927 | -39.66652 | 2026-03-17 03:49:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ee77df74-6abe-38f2-bffb-b8ad3a6b8ceb | -11.82145 | -38.26471 | 2026-03-17 03:49:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c3798464-5140-3238-b529-dfede51b77b3 | -8.348 | -35.73121 | 2026-03-17 03:49:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fee0fe0d-be9c-3488-bb47-777d5ae17fc3 | -5.67274 | -45.20442 | 2026-03-17 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb50d3b5-94b0-39ad-b80b-da466e805381 | -10.64071 | -36.93826 | 2026-03-17 03:49:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ce79950a-1f8f-3ebe-8316-02287d26738c | 3.1094 | -60.746 | 2026-03-17 03:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c43c0099-d363-3350-b4a5-86a1986f85f1 | 3.1276 | -60.7647 | 2026-03-17 03:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 9d2765c7-a0a5-3dcb-baeb-98e5cbf162ed | 3.1277 | -60.7457 | 2026-03-17 03:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 138.2 |
| ffadd76a-894c-3c65-b2e4-1d80d5366012 | 3.1094 | -60.765 | 2026-03-17 03:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| ef0178f6-f40e-3a59-acb6-a3faaa835514 | -12.10931 | -38.91691 | 2026-03-17 03:51:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5d56c58e-ebbb-3eff-9f99-75d805fd400b | -13.14109 | -39.69343 | 2026-03-17 03:51:00 | NOAA-21 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5691782d-6de0-3ce9-821b-aed1db4ceb83 | -13.01013 | -40.23126 | 2026-03-17 03:51:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
