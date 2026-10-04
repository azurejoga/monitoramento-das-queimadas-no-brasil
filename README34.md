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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 846b17f0-b9cc-3910-8344-1b97492434e2 | -3.77046 | -51.85602 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9188bab9-ed03-3514-83c0-ce1b093c08be | -2.92472 | -54.10147 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75dc2c9d-f62c-3489-8165-4f447aa9c461 | -2.80148 | -54.09811 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2758d1c-072e-311c-a483-31c2db1da013 | -2.95647 | -54.09721 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d897a28e-e1bc-3c54-9105-c0005d8513f2 | -3.06947 | -49.52845 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffbed03c-c9f4-3220-b4fb-22b942f76f34 | -2.81099 | -48.66151 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 454143ec-f43d-30aa-b731-bf7ac31185d1 | -4.11489 | -49.07185 | 2026-10-04 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d3fcb98-56cb-3483-a2e1-c23e6b07e80c | 1.83981 | -55.53947 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dfdb84d-2ed7-3cce-8aa8-502d2110b123 | -2.80453 | -54.1033 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7f78e4e-6b33-3ebe-b931-df19e09a2104 | 2.35987 | -50.75693 | 2026-10-04 04:55:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f10092eb-3a17-3495-9257-add3320b8e5f | 2.87391 | -60.54702 | 2026-10-04 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e7ec3505-82fb-31e3-81ad-f202e68fef2e | -3.36198 | -43.38248 | 2026-10-04 04:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d99b3e7c-6d65-386e-997b-8e087b20cc5c | -3.80691 | -50.85546 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e59499ac-d9b4-3f6f-b9fd-4919a4fbeb75 | -2.43953 | -49.02488 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6c8a789-c501-3c5b-8846-1b1c8375b400 | -5.36442 | -45.03301 | 2026-10-04 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 454e02b2-6a14-3549-9055-a6dd6a17296d | -4.15802 | -47.5372 | 2026-10-04 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4ca3d2e-8d54-3fc9-90b6-0ba41d3dbe30 | -3.70295 | -50.65795 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65700503-3a65-360a-b4de-c621aa84bdcb | -2.24395 | -51.92261 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b581edf8-89ba-3aab-b20e-aeff7d225c3a | -1.62732 | -55.01834 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 44ce628e-28d8-3b8e-9e4b-590fea3db871 | -3.31857 | -54.17125 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f105213f-0dd0-36c4-91c8-d27ad97497ef | -4.27454 | -49.97805 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 526e7950-9380-3e67-b0d3-fca9c3b055a1 | -2.88695 | -54.14248 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02f54502-acf0-3c17-9ff4-492bd2bb6540 | -3.08342 | -49.54849 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1d9d73f-870a-37d0-83f8-f957f59d6290 | -2.25247 | -51.93539 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a10d123-72bc-3a3d-a858-c00cf1b4aa8a | -2.5619 | -48.25038 | 2026-10-04 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47510efb-5a86-3709-b158-660969927dd8 | -3.08507 | -49.53803 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3d7c655-ad2c-39d9-a064-5e10c056f1ab | -2.92639 | -50.43205 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12bd2455-027c-31a0-b4d9-e3901e29711b | -4.27066 | -49.98101 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3112281c-14fe-30d5-9feb-31138d203477 | -3.30831 | -49.13729 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4642d8e3-7cd6-31c8-b8ad-2a3ab0397d24 | -3.1769 | -48.68829 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb41e650-c25e-3ccf-acbb-bd61823fbdc2 | -2.93178 | -54.15442 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef90e1f9-301b-3034-bcfe-22a67af73daa | -3.13203 | -53.74371 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faeda480-583d-316d-9ef8-8efb4b4f2353 | -2.8915 | -54.13845 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfa62db6-46a6-3099-8903-5495a7db2a10 | -4.47103 | -50.97449 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f66fd836-1d69-3a13-aa11-f5404b9889b5 | -4.46044 | -49.69554 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 206b1d21-dab0-3ce8-a091-997b81b88230 | -2.59781 | -51.85296 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ee87acd-cf7c-3e53-be6a-19f0c75725fb | 1.92503 | -55.72433 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb4017c8-84d5-3bd8-8b64-f7848090597e | -2.58696 | -51.85497 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5800933e-3be0-347a-8be4-861478f4e5e2 | 1.8068 | -55.56277 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b24400bc-1b0b-3688-9c0c-fdd15fc4fffa | -4.46323 | -49.69957 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e25d9028-d59a-3297-8bfc-7e9fc83e92d2 | -1.10278 | -54.10991 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c18a42f-11a7-3956-b447-e82d6b4b804f | 1.8949 | -55.80626 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e30c419-c55c-302d-bcc1-49e96ff43019 | -3.45248 | -53.16804 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d4613c1-3857-32be-add4-913914ec7ac0 | -2.35491 | -52.70874 | 2026-10-04 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c586618a-52ea-3a43-9dee-96ec8e011d1d | -3.75681 | -52.44386 | 2026-10-04 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64262f80-f885-3b1e-aadb-55db0557c6c0 | -3.11514 | -53.75438 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b8573732-1cf9-36a8-8c72-f3dd2e41ec0c | -2.83211 | -54.21461 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddf50d04-97e3-3f7c-a069-8766ad6e5837 | -3.00379 | -53.87636 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39e6c381-10b3-349a-92f2-b43233f09deb | -3.08672 | -49.52757 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3cc9fc3-8e96-3b52-af9c-b81ffa89654b | -3.47003 | -50.0998 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c2a94c53-b6af-3663-b24e-2ab3f6b14813 | -2.4771 | -50.87751 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47951a45-9dbc-3e3d-85a2-4a0d3a930133 | -1.6238 | -55.0141 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60535946-5243-342f-9bac-79c6f59da2b8 | -2.97623 | -53.26978 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41939c16-15ae-34b6-bb49-d633bb30865a | 1.90712 | -55.79499 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0254f467-03c6-38bb-9f29-f62ae27b6e36 | -3.47058 | -50.09634 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c1afede2-62bb-3249-82c7-14eab4034f38 | 0.44354 | -51.0647 | 2026-10-04 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea209aa0-e8c6-3e51-9f6b-53132d447676 | -3.04133 | -54.21691 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a7004914-97f0-3ec8-b948-8b2be4d11816 | -1.21249 | -55.86094 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 82f8c59f-b9b5-3c20-aacf-cf45c4cfb611 | -3.12764 | -53.74747 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8209abc1-868c-3919-a9a3-7e711d1e1918 | -2.91032 | -54.09448 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f395ab42-a17d-3718-989d-2ab0848038d3 | -3.80746 | -50.85199 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd146ceb-bdfc-388d-a3d3-ae08d2764d7c | -3.11422 | -53.73636 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 76e7c280-5ca0-3e08-a1b8-aa82152ee27f | -3.28456 | -53.8324 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f69314e-07a6-3093-b686-69e0e8cc85f5 | -1.7442 | -55.24147 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0368c9c0-3b52-3968-abc4-58ddf396144e | -3.11353 | -53.74071 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 3ab36e6b-75c4-37ee-9e16-378ecdf59799 | -2.81145 | -46.78251 | 2026-10-04 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 954ffe5b-6a81-3090-8964-484f1279ad5f | -3.07038 | -51.27396 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2e2aea3-de27-3e51-982e-9288951aab88 | 1.7625 | -55.64434 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d66afbb5-0db8-33ea-a934-82c7a7e1c4d2 | 1.75732 | -55.64059 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50d6abf0-55fd-318e-8211-7300532074f4 | -2.75184 | -51.54532 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de5ee7ff-c34d-3f30-9dcc-8056d8f21340 | -3.18031 | -54.09701 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6abec80e-bb40-3e03-8d43-7df58820ee4b | -4.26244 | -46.38003 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1522258f-d60a-3cf3-a569-c232123f43af | -3.18746 | -50.53729 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b15baa72-87de-31ad-b3eb-4e4f12e972c0 | -3.27473 | -50.03027 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 205db889-3601-343c-995f-7a4ce9c963b2 | -2.79926 | -54.11187 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a6c1b33-d1eb-3425-b864-73a6dfdde80e | -3.17942 | -54.07603 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 29571920-905a-3d41-9323-c78a74069331 | -3.76486 | -49.56166 | 2026-10-04 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 17cdf1b0-acf1-3844-9f19-8e45300e4646 | -3.12024 | -53.74626 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b3e4e20-453e-3ae3-9d30-93d77e92a6e3 | -2.95195 | -54.10119 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f385c1a1-9b93-3276-879b-35ef5a21f295 | -3.11052 | -53.73576 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| d6e1fc15-ad07-3555-8871-7b38b940a45d | -3.28828 | -53.83297 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4951ab8d-c028-31bb-833e-3f996ced2629 | -4.27121 | -49.97753 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65c7b7bb-a4de-3d26-82f5-653b627e20e4 | -3.42065 | -48.33764 | 2026-10-04 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16224d9d-f379-3f60-b48c-5619658bef31 | -2.80916 | -54.1229 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9f51e467-925e-359a-8a00-03b8138b7e8e | -4.29224 | -50.26849 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| b31b5add-dbc2-3224-9c82-36556a484a6c | -2.89754 | -54.12526 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b8df4cf-b462-34cf-81a3-5736379ccebe | -1.87604 | -50.61488 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c959d84f-30c4-3e41-a5f9-3a198137400e | -3.28757 | -53.83735 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 831218d6-245c-323b-9e61-6c00a5c70bd7 | -4.30264 | -50.5432 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 248ec04a-57f3-31b0-9afc-3e32d912e468 | -1.16991 | -49.26308 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 801109bb-7d62-3479-88ec-0d8318ff5559 | -3.04673 | -54.23203 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| eb8fbe5f-ee17-3f87-a4a2-fa84ef991d26 | -3.18547 | -57.919 | 2026-10-04 04:55:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53a6be36-1e47-3037-810c-953d14cf28c6 | -1.41006 | -49.26484 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c5b573c-3506-32ec-b4a1-942333003b32 | -1.46284 | -49.46543 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5462f3af-d968-3fb3-9010-8fbc88f4a9c6 | -3.07619 | -49.55093 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 30d112aa-984e-3d3b-8c33-dd5356ea1b95 | -3.4678 | -50.09236 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7702d983-61f7-3978-bf1d-7d4b024a0b78 | -4.51269 | -45.89228 | 2026-10-04 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 540406c0-d200-36a6-9f06-4f18e5a4a675 | -0.72223 | -47.84996 | 2026-10-04 04:55:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef72f8a3-39cd-3ec9-af8d-7bd7875890e6 | 2.34218 | -50.75592 | 2026-10-04 04:55:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a013bec4-af6d-376e-9a0b-19120f9b9da7 | -2.91099 | -48.99957 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README35.md)
