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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c48f9c7-b9bb-3a05-909c-08838cf9315e | -10.95098 | -48.14662 | 2025-09-03 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 584d989a-2522-3362-bf41-fecfe3d09cf0 | -11.60942 | -52.13129 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1797617a-0ff4-30f9-a800-b187bbdbc178 | -10.48081 | -50.35445 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 897cbdd0-6545-3622-a42b-114075d1f03f | -14.60217 | -54.58215 | 2025-09-03 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4ce722d-594d-3856-9a70-450ca4614bf6 | -8.08052 | -47.60846 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c41a3aac-d690-367c-bef2-7d182504e0ba | -12.96226 | -48.08691 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db67752b-b8ac-3cdb-b5c2-3bfb77d72174 | -14.58833 | -48.04041 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07ced3ad-ff86-3819-b658-08eced4eb333 | -12.62656 | -56.99232 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50b4278e-0b8a-30a2-a8e9-def978fcdaf8 | -13.70584 | -46.94273 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4208daa7-3f1b-3e37-acf3-a1651f784221 | -14.96659 | -50.20479 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7dc1c1e-81e0-3601-874f-d87d68d90c4d | -9.77051 | -50.01189 | 2025-09-03 05:14:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 446232ed-580a-3e33-a45f-6246347cea78 | -11.60061 | -52.13002 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| abde5dc6-c34a-3626-8364-61d84b99a70b | -13.90406 | -48.11038 | 2025-09-03 05:14:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53e6098e-0c0b-355e-9ba3-c64bd81f5c47 | -14.76885 | -48.13789 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 962b8f21-4bd4-3ebc-9058-b80f7dc51085 | -9.62596 | -47.06615 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a204f240-6287-34cb-bd76-e8d618cc6fbe | -13.49988 | -47.02004 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e46569e-3470-3d4b-9812-2984108fe0f8 | -13.01279 | -56.87611 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceb5563c-7a58-3e7f-ba3d-8f1417e2bfc6 | -10.98923 | -46.83112 | 2025-09-03 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea65b972-fd4c-3304-8380-7a2f7dc1c02b | -11.86913 | -52.42284 | 2025-09-03 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62d9c17f-d885-369b-bfdb-81ed4f4dac3a | -12.9576 | -48.07564 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd107afe-f5b7-3cba-95df-aa0875dee9c4 | -11.58794 | -46.76874 | 2025-09-03 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c63aebf2-d5dc-3117-abad-a7abe786ac52 | -10.09444 | -54.75909 | 2025-09-03 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c42c4abb-bfc2-3605-aa49-289ed39bfecf | -11.5962 | -52.12938 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 12638fc9-7c05-3da1-80e4-416ac027a54d | -14.83458 | -46.69288 | 2025-09-03 05:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2d65d2f3-9eb0-3b90-89e2-a11887f95bdf | -9.42647 | -48.36247 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3b0f66a-0bef-3be3-8e55-3f0f1d43fb77 | -14.58073 | -48.05439 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ebb5944-cd61-31b7-b0c1-c999e4ed54ea | -10.08677 | -54.76802 | 2025-09-03 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2898670-5e9d-32ab-8e6e-1d048e09e5ad | -7.70759 | -50.29835 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6ca81003-4312-3b4b-bb51-489267f06745 | -10.47832 | -53.63384 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 539afea1-5b03-32a6-a6a3-7e2891953a9b | -12.93673 | -56.99324 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff9f9a7c-7fcf-3cd2-bb3c-d357b1984f79 | -11.06843 | -52.07327 | 2025-09-03 05:14:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 974480ff-e740-3913-85bb-8b63d251e376 | -11.58912 | -52.11526 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b70a4f05-2df2-3b52-a405-afbc484907ad | -11.60393 | -52.07262 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5742d48e-69b3-3b00-a096-7bacd3f2c93f | -12.93613 | -56.9507 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 05896d89-173d-31dc-8e7f-80c0c0c6aea6 | -14.26871 | -51.22859 | 2025-09-03 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05b177a3-969d-32ec-8ff3-6f87f5e1140f | -7.70396 | -50.29419 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0be99d58-d153-3584-9ff4-b0f7ed33ee5c | -11.42341 | -55.18274 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab95952e-849d-3cf8-a35a-1db78dc0af86 | -6.43917 | -58.13655 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47d6dd23-7c13-35c2-94b6-6e5b10d9e3a8 | -8.06626 | -52.35678 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a264162-fc6e-3486-b9c3-9c8e44ab8495 | -7.54352 | -61.34373 | 2025-09-03 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8669a08c-ab66-3a66-b9d7-4a2767beb54b | -14.97246 | -50.21115 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ca3ad32-3218-36fd-a673-b75e21697197 | -11.61216 | -52.07843 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11427171-23b0-3bcf-93bf-98ec345c2d2a | -14.2694 | -51.22311 | 2025-09-03 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bf6ee2d-1280-3e6e-9f2c-0ea30545efd8 | -12.90183 | -56.94523 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c36ea19f-a95c-31eb-aae7-508d0ffd9c49 | -7.68755 | -50.26986 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed4aa574-6864-3cb3-9335-17df9a46dbe0 | -9.34011 | -55.23045 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1265abe3-2715-37cf-87fb-a622cdb113f4 | -9.62717 | -47.858 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64e5cdad-c9b8-314a-baae-b6661fc698b3 | -15.01718 | -50.04449 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25e31545-61dc-3657-a5d7-0512881c64d5 | -8.89156 | -45.79713 | 2025-09-03 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 82353e5e-e566-37d2-89ba-028abd0fd6d6 | -8.37129 | -52.5407 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 55f22e5a-90c2-3187-9822-5cb4f0db7413 | -14.97324 | -50.20467 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 152547da-10af-371f-880e-be545472a285 | -11.41977 | -55.18219 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa241ca7-aa5e-3005-9728-573f0dc26447 | -11.41523 | -55.18681 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 548ab2ac-d4b6-3e25-be86-d78a29fcd8de | -15.01069 | -50.05395 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edf74f6e-9e18-378d-a97d-e492e1a7a626 | -12.62485 | -57.00356 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14572e03-a257-384c-be24-c80146d71635 | -8.34553 | -52.52291 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d019ee8a-9f7c-362a-8c3e-1c23d373c40a | -11.82435 | -51.44377 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 70f57036-82c1-3fc6-b4fc-14ded717d74b | -11.92286 | -46.6626 | 2025-09-03 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f125112e-e38e-38a0-a2ed-0593d9396c53 | -11.61336 | -52.06963 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd8caf73-e62c-37db-ac1e-96eaa224b6a1 | -15.01414 | -50.0709 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f7a1e89-fb75-38ee-bb86-60ec05121b8b | -9.95434 | -51.63589 | 2025-09-03 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5290acf2-c18c-3a18-822c-887680f41da1 | -12.62257 | -56.99551 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9c0a788-afab-367d-adcc-d8ffd3176107 | -9.33421 | -55.22136 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f371572-fc32-33e1-8374-5fb6f94c11d3 | -8.08105 | -47.60461 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f84b18e-7cdb-3d6d-9df3-b23839136493 | -11.84903 | -51.41932 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ea4e33d-7208-3180-bd99-250b2a546266 | -12.88456 | -48.03355 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88a6138e-5534-31ec-bbb2-f80432f5076d | -13.99123 | -49.55381 | 2025-09-03 05:14:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 379c6d52-f59b-39ee-9bb8-bf2d295091eb | -11.67533 | -57.35492 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 23421908-bfca-31eb-b21e-05d1b6b145f9 | -11.59089 | -52.10221 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c2794fcf-778a-3ef8-870b-eb6465fdab11 | -10.95819 | -50.76595 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1425ac66-b53c-36c0-8545-2532ba6f8f99 | -11.60894 | -52.06895 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a12fe3bc-cb31-3030-a9cd-e055a7f98176 | -10.96805 | -50.91482 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf1c8c40-63a1-34c9-9946-7436946afb59 | -14.57385 | -48.06165 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c9a3788-bf30-3967-9a7e-1d1f568d716d | -9.99513 | -46.89154 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b7b1797-b57e-3772-84fd-c94e707ab7f9 | -11.60953 | -52.06461 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73bd68ab-862f-3cb9-874c-414e91d31cd8 | -8.15007 | -54.93017 | 2025-09-03 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f2d9924-d28b-3505-b08f-252a46492ca2 | -15.0229 | -50.0418 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55940a02-bd6c-3466-acad-f8424ad6c6ff | -10.54423 | -50.41378 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0dea465b-c0ae-34d9-b2ab-64b9de4aebe5 | -11.5903 | -52.10659 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28553936-e34b-3964-971d-e794858ca2c3 | -10.9154 | -50.83288 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 389c2a15-60d3-3173-9f6c-87e9b79305c6 | -10.92078 | -50.8651 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 203b6df7-24de-352f-a856-bbd634112709 | -9.33716 | -55.2259 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a5100c2-fe00-3e98-8042-0694502c7bb3 | -12.9807 | -54.77486 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a51148b-dec2-3699-8967-57d588a438a3 | -8.06442 | -52.35649 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fc5127e-2fe1-3f29-962f-ad655ae7e994 | -15.02599 | -50.06185 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e910629f-cbab-382a-a39e-d7b2d9f542c8 | -7.70256 | -50.2662 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba957fae-9343-3c33-99a6-400958153301 | -8.35875 | -48.31435 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a6f7416-81cf-36d1-98f0-37a8e813ec41 | -7.53696 | -61.3357 | 2025-09-03 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6e8aea4d-251e-3172-8b7d-df534e3647e6 | -12.92875 | -56.99968 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc35d5d8-3680-373a-b2da-9aaef950ceb3 | -10.93595 | -61.53962 | 2025-09-03 05:14:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 799a60e6-c61a-3788-bdac-599e1b7656a6 | -11.61897 | -52.06165 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cc3973c-0ce8-3655-af63-36785907400c | -11.62843 | -52.05856 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a180d81-ec73-3726-a896-f33e1601e651 | -13.09042 | -57.12806 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b852ec6-35c6-3a5f-89d8-ba91ff00a2a7 | -11.84223 | -51.4166 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e93368c-b15e-329b-bc51-e9e53fc58430 | -11.59001 | -52.1418 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 17deab0c-df1a-3ba1-90f6-b0d773f7539c | -9.99568 | -46.88724 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6aea144b-150c-3628-b6ac-f25791fe8b0d | -11.03052 | -45.06298 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 028e1944-2649-307a-be60-2176ac1bb43e | -11.31378 | -55.21954 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94e26f80-0dfc-3ef7-a62c-0dfa67703c26 | -11.5901 | -46.77262 | 2025-09-03 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6933f71-293c-375b-a256-f41acd2dd730 | -12.90127 | -56.94901 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README97.md)
