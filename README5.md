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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2769908f-0c3d-3768-85f1-1cfc62d44a45 | -2.56299 | -53.87643 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c4f6e3b-fa12-3907-a6e5-f5bc2343dd07 | -1.33663 | -55.42706 | 2026-01-04 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b739c10d-fe4a-31c1-a864-464970476e91 | -2.09074 | -53.48551 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66ccb1a1-7169-39ac-aa54-25ae0ac2c1b2 | -1.01308 | -48.88643 | 2026-01-04 05:08:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c86476b9-0876-31ae-ba9c-7652ecfcbc25 | 2.55727 | -60.36216 | 2026-01-04 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fdc1704-5429-3637-8a35-c169163a6292 | -1.90452 | -53.24972 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f6a037a-8005-34fd-b5c5-4be191bbcb4e | 0.46736 | -60.44113 | 2026-01-04 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 003e3ad4-e6e5-39a4-9af6-bb8e98586128 | -2.99657 | -54.10275 | 2026-01-04 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52f78595-c7f8-33a4-89bb-1f1a86d280b0 | -1.60548 | -55.16102 | 2026-01-04 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f73ac931-4d3a-3304-a221-6477a206f180 | -2.42674 | -51.8312 | 2026-01-04 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e2ce43a-a68a-3535-b05e-00df747feed5 | -1.3333 | -55.42654 | 2026-01-04 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f759cb6-5474-3d06-a0ad-833300c746f0 | -1.66906 | -53.9221 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c420f623-117e-3193-a33a-511433c20811 | -0.16796 | -51.50102 | 2026-01-04 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9d927bb-c6c2-3837-ab7e-733d1111b15a | -2.14372 | -53.68041 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e3e6ba8-9b88-3d8b-af3f-918851b0ecc1 | -2.38821 | -53.70012 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d4bb405-786c-308b-847f-aa09bc4f245a | -1.19388 | -54.10203 | 2026-01-04 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bdae2e7-3874-311f-834e-dc0fc7a06bd6 | -3.06362 | -54.02623 | 2026-01-04 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4aa34f31-4e19-34f2-8e17-3d3a03b9eb1b | -2.11659 | -53.47799 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab04eb8d-0f1c-3775-8f76-1bc5d2129db3 | 2.5528 | -60.36282 | 2026-01-04 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a7fe8854-71ab-3f50-8402-5ae0f72a7d5e | -1.33718 | -55.4236 | 2026-01-04 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52bf0fdf-657e-313d-822d-7a5ff6dcf437 | -3.00158 | -54.09268 | 2026-01-04 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb440270-42a5-39b6-a6a9-bb26c53c75a3 | -0.08703 | -51.2776 | 2026-01-04 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e161142e-cf41-3c24-a5a2-17b0ca2ffd35 | 0.72433 | -59.99655 | 2026-01-04 05:08:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c7004df-4ef7-33fa-9134-0f6ebf38cd7e | -1.25607 | -53.48893 | 2026-01-04 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86998cdf-0053-3c47-b0d1-7291ca4807e2 | -1.25381 | -53.48131 | 2026-01-04 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee4aa50c-1914-309d-a169-12127f486dc3 | -2.91023 | -49.3775 | 2026-01-04 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b05ce1a7-166b-34fa-bcd6-de53a761808c | -3.00213 | -54.08916 | 2026-01-04 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 246e1c09-e791-3669-8e95-9057caf73037 | -2.91509 | -49.37422 | 2026-01-04 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bea92be1-e9ce-3db6-bc4d-949ab2bad9cc | -1.09702 | -53.16684 | 2026-01-04 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06edf5cb-7a49-3b87-bdf9-ff85a54db415 | -4.2593 | -48.83714 | 2026-01-04 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 294632e2-c6be-3943-a668-6ccb681b41f0 | -1.33275 | -55.43001 | 2026-01-04 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78930fa6-ba4d-31f2-9ab0-a7b5bd1b76f5 | -2.45063 | -47.78645 | 2026-01-04 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b03f8d6f-5abb-3711-a2a9-eb75a9331c02 | -2.90836 | -51.56191 | 2026-01-04 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95f50019-f192-36d9-91ca-5185fa8ea36c | -1.96248 | -54.05757 | 2026-01-04 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cee86fab-dcf3-3c7b-85cc-49f18367fce8 | -6.23445 | -55.62775 | 2026-01-04 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7fe9bcc-21cb-3080-ad33-0eee29528ae4 | -6.23113 | -55.62722 | 2026-01-04 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26ab6401-06f4-30b4-afd9-4460e3b64747 | -18.54723 | -52.78526 | 2026-01-04 05:12:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19c87c05-0d6c-3c1d-be32-e3e5663aa3be | -18.82241 | -51.61195 | 2026-01-04 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8ce33b66-9bc0-34de-96e4-8d79f31aada5 | -18.81841 | -51.60637 | 2026-01-04 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5e4b2780-be25-313f-835b-08fc8c9c39f4 | -18.81381 | -51.60564 | 2026-01-04 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be2ee20b-edba-31ff-a8df-9cec09f0fbeb | -18.55247 | -52.744 | 2026-01-04 05:12:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 946cff89-e574-351c-ae44-e2764835ae27 | -18.82302 | -51.60699 | 2026-01-04 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7281bc79-dc67-31da-9a99-4cf7b5c7924a | -18.82641 | -51.61756 | 2026-01-04 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1166962-640e-359d-a5db-1cdbcd2324fa | -18.81781 | -51.61128 | 2026-01-04 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3cb1617a-0ca4-30dd-8518-0b75d6a17c5d | -18.55147 | -52.78586 | 2026-01-04 05:12:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9215591-3a47-3e3c-95aa-6f0d3be7768f | -18.8218 | -51.61696 | 2026-01-04 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a35c75a0-12a7-3adb-b8a1-db047958d56b | -18.82703 | -51.61255 | 2026-01-04 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3309fb2b-38c8-32d4-9018-de87adb2f313 | -18.82256 | -51.60338 | 2026-01-04 05:14:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc63e424-64f0-35d9-8542-c78c245756cb | -21.25679 | -48.65211 | 2026-01-04 05:14:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3448ec7f-cd15-3a48-b64d-110a80804afa | -22.02805 | -56.30592 | 2026-01-04 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ec968cd-9e22-3ae3-a9cb-07dc906ef177 | -18.82199 | -51.60837 | 2026-01-04 05:14:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| eb029d05-0a2d-3620-8ca8-bff7af443517 | -18.82603 | -51.61397 | 2026-01-04 05:14:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| baba9478-d107-33e0-bddf-c13823accc37 | -18.82142 | -51.61334 | 2026-01-04 05:14:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 05857bc6-6632-31c6-821c-046d81c9df02 | -21.25638 | -48.65633 | 2026-01-04 05:14:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cbeb1fc0-8f02-3215-adfa-5341e36cd204 | 2.55252 | -60.56615 | 2026-01-04 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03bfc684-0994-3961-a22f-c2aa3e715668 | -1.33484 | -55.43039 | 2026-01-04 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f8d4f5d-29eb-3725-84e9-564d46ce130b | 0.62226 | -60.28541 | 2026-01-04 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c45ae48e-f7e3-3d65-b9aa-7915559ee82b | 0.81424 | -60.61747 | 2026-01-04 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3b0ae58-1a27-3b7a-94a4-c4f79fbf5ece | 4.21378 | -60.41431 | 2026-01-04 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c87a44b-29fa-3f78-912f-f2d539de3059 | 2.5536 | -60.3583 | 2026-01-04 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a823b8ae-ddf8-3e9f-a4f3-513eb8bba0fc | 3.06774 | -60.44966 | 2026-01-04 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 842060d1-f85e-308d-9ef2-66b0ab691226 | 1.57642 | -60.19523 | 2026-01-04 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa8d7f3d-1721-3d09-b152-2a8a94935757 | -1.96322 | -54.06068 | 2026-01-04 05:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1270b612-18bb-39f4-b842-7e9eff34c928 | 2.55583 | -60.56564 | 2026-01-04 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4340383a-d3fb-36fe-a33d-1028f6076dbc | -1.33545 | -55.42644 | 2026-01-04 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f89f1407-afe6-3d7a-bf9f-a24e00679f92 | -1.14702 | -54.174 | 2026-01-04 05:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bde7c490-6ec0-3676-beae-031d8c7cea5a | 1.12556 | -60.52283 | 2026-01-04 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b643239b-c26a-32ad-a3f6-8900f8b88de2 | 2.54753 | -60.36276 | 2026-01-04 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 11ac1852-0c5a-38f6-b37e-1789c918aeb1 | 1.65989 | -60.74499 | 2026-01-04 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36a72964-3deb-31b0-9616-d936a598876b | 0.67189 | -59.59055 | 2026-01-04 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 99efd68b-1179-34fd-8c76-2ee214cd8a17 | 0.46689 | -60.4401 | 2026-01-04 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9d30593-6050-34dd-9f68-529b39c88f93 | 0.72608 | -59.99645 | 2026-01-04 05:29:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74668afb-00d6-30ff-aede-d2c6011dc647 | -1.19557 | -54.10536 | 2026-01-04 05:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7426043-7ff3-3cea-a60d-60774bdb3176 | 3.35934 | -60.36135 | 2026-01-04 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb6cd26d-71de-3317-bafa-17bf660f3158 | 1.12886 | -60.52232 | 2026-01-04 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 142a8e65-0490-3f14-8473-097fa58936ba | -0.08653 | -51.28001 | 2026-01-04 05:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bef33d2c-f290-377a-b2e3-0e23a5d13fea | 1.82974 | -60.87315 | 2026-01-04 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eeb0720e-c93e-30e3-a38a-9d03ba7686e4 | 4.33156 | -60.81996 | 2026-01-04 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f7e4804-0670-3469-bd21-129e9ae9d3df | 2.55745 | -60.36122 | 2026-01-04 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86063a47-a0b2-363c-87c1-9d6d9a2d0479 | 2.5503 | -60.35881 | 2026-01-04 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b8140413-4ca7-3020-ae6d-0c4523c4dc7b | 0.67523 | -59.59003 | 2026-01-04 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9b17a96c-43db-3b32-8066-5aae3d9044f4 | 0.46911 | -60.43271 | 2026-01-04 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e3e0da80-eef6-3e60-9aec-e0c5525f2062 | -1.19542 | -54.10219 | 2026-01-04 05:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02210e15-c013-39ea-8be8-a5a730b181eb | -1.60528 | -55.16189 | 2026-01-04 05:29:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2497ccb1-bdc0-3374-8d9c-5acfb35b2a29 | 0.46857 | -60.42927 | 2026-01-04 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 26a4daa6-7e12-35f8-9e10-ea2dc1f6107b | -1.19473 | -54.10674 | 2026-01-04 05:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df2f87a3-f194-322f-be67-cfd947ef7b58 | 3.37123 | -59.83476 | 2026-01-04 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98a355d3-5d95-3721-bd4d-2cbfc6ad270e | 0.6337 | -59.71141 | 2026-01-04 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fea21d1f-cc50-3038-9ccc-d63b20d70f07 | -1.60959 | -55.16256 | 2026-01-04 05:29:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e882271a-7677-3703-96ec-063cb4763cd9 | 2.55414 | -60.36173 | 2026-01-04 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc6d934c-f2ce-37b3-9d79-b2d1a663acf6 | 0.91165 | -60.37388 | 2026-01-04 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf1e480e-0a37-39b3-a882-71ee3fe073c2 | 2.55084 | -60.36225 | 2026-01-04 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3b98d92d-ddc8-3196-92e7-b392bca80d78 | 1.07651 | -60.38672 | 2026-01-04 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14406c19-e043-3629-a472-2d503c18cb64 | -1.14244 | -54.17324 | 2026-01-04 05:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfdfaeba-d17c-3eb8-9a56-0354a2be9f7e | 1.07982 | -60.3862 | 2026-01-04 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9af3dd9e-0ed1-3e3c-bce8-99b133ec460b | -2.07173 | -54.25975 | 2026-01-04 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2586c937-08ab-3a77-adc4-fe40da0e2c95 | -2.7761 | -54.52781 | 2026-01-04 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 802dfcf1-393c-315a-a823-208ac527f5b8 | -2.11305 | -53.47666 | 2026-01-04 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2ee5ba4-41da-32ef-b3c9-23e40a1cf6ba | -2.91111 | -49.37379 | 2026-01-04 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d528ac70-41ea-356f-a297-7b9d94628d5b | -2.91032 | -49.37917 | 2026-01-04 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README6.md)
