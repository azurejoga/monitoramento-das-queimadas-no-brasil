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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56899acf-6cde-390a-bdbe-0638f4e3633a | -13.37045 | -46.99814 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bb944535-2a36-3d8b-8d45-d96451591441 | -14.47372 | -48.38544 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 972f5de5-4ebc-3c8e-b060-b212fad2fc7f | -15.21875 | -53.80906 | 2025-08-30 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c9f70fd-e2fd-3362-a102-bbd1fac80600 | -14.33225 | -51.88155 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4f80dc1-0241-3230-b169-fc4d3e80d6b0 | -12.71925 | -48.19544 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12ae1ebd-8440-3006-ac7b-eedd6c0ba391 | -13.46446 | -46.94286 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bae6364c-d824-3a3d-8778-80903d27fa8a | -13.37455 | -46.97816 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ad26c47-bfe1-35e5-a9bf-aa7968a93dff | -14.00663 | -44.57961 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea6dacb8-efcc-3fad-a5f7-23fcf9531064 | -15.10384 | -48.40221 | 2025-08-30 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c464e157-da71-389f-b709-45f84ebfa076 | -11.30624 | -63.29739 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86796788-bc44-3e28-bc23-62bee856472c | -14.00174 | -44.53905 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de13ad44-7661-3b8a-8d2c-025edfd97829 | -14.59786 | -54.54969 | 2025-08-30 04:51:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebd9d3ea-63e5-36eb-a8ba-ba5c9e2c713d | -13.49895 | -46.94251 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c4803b3-f275-3a06-b949-ba6fd608136d | -10.35436 | -64.46686 | 2025-08-30 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f3f901f-19c2-3efd-a560-207cb913a50e | -14.79254 | -59.7299 | 2025-08-30 04:51:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 819c22ff-b5bf-3648-a2f9-63bed890a7ba | -13.51281 | -46.83759 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c08b8d43-5198-3091-b7cc-b9d914df17fd | -13.3647 | -46.98841 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8aaff45d-5d7b-3ebf-a079-d6995163b5c4 | -14.25572 | -45.2455 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba9b5a71-f9e4-3261-8166-926b123c69b2 | -14.34398 | -51.89458 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40c88f43-ea15-31b1-a474-cefe19101a45 | -13.37342 | -46.88474 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9e006e15-0e7d-3e1a-8bce-8d1aeee2fe6b | -13.41728 | -51.81712 | 2025-08-30 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69d45efd-af67-3afe-9c06-2b6ca7633945 | -13.54482 | -46.95037 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfb5dc16-d4fb-30e0-9422-1cfc5430d161 | -13.59136 | -46.89169 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0854233b-540e-36f5-8945-476eb17c67a5 | -13.39553 | -47.01196 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 540bb2d0-b519-34d5-9d63-929baec9c6ad | -14.31662 | -51.87159 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7309eec7-3d90-31b3-810b-c11250e34190 | -13.37737 | -47.02094 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d369f13-2b8f-31e9-a69c-cb349265c902 | -10.7429 | -59.82169 | 2025-08-30 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ce78bd1-fdde-3c07-9d53-6696fbe1fc4f | -13.58715 | -46.89106 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fe2f337-043f-326f-b121-28956e9dc10b | -14.01944 | -44.55826 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 80670a79-5388-3f37-843a-4d641fd58ca0 | -13.38024 | -46.96729 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b812e124-9a62-397f-879f-c090b42be9e8 | -13.36986 | -46.98153 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 34ac3cf1-6a41-3dfd-ae1e-f1ef1717720b | -13.97246 | -46.32746 | 2025-08-30 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adeb9c05-06a0-3cd3-a761-013cbe9aad1e | -14.61944 | -48.08247 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d6ed9384-387f-3939-b00f-8bec87eeda03 | -13.3844 | -46.96803 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1318d991-a80e-3f0b-adf9-a2323e35d93b | -12.63557 | -57.00794 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 191cd502-24b2-3395-b51a-8554ca8e4e55 | -13.66891 | -46.92322 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6a96047-4ad5-3bbe-b1fc-9878fc3f8b80 | -14.61821 | -48.07861 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 155de75e-8c89-3ad9-8418-f0d1a8b3fc81 | -14.1111 | -51.7799 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b7a4bd4-2e88-35b0-a9d2-dc7e5ec040ab | -12.62773 | -57.00648 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1f4e8aeb-f4f4-3735-a635-62da77e5b610 | -12.82037 | -48.18774 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fec7ffcd-bc98-3e10-9ae0-08d76da210fe | -13.50856 | -46.83727 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0c4f5af-eced-3a42-836d-04059a1100f7 | -13.63665 | -48.13433 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb9c41e1-77df-3c5e-b52d-571babe7ac4b | -13.47164 | -46.9526 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a8fb1e6-445d-36fb-9a10-e9279ad21342 | -14.00169 | -44.57891 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5411dcd8-1b13-30aa-bb62-7b9365296747 | -14.59628 | -54.49518 | 2025-08-30 04:51:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51334594-ac13-32e2-8803-2979694c9759 | -13.52746 | -46.95249 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 74441905-73cd-3463-a972-c165ffd36df1 | -16.53637 | -55.04566 | 2025-08-30 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5c71e93c-2272-3cd6-939f-405dccec0208 | -14.62216 | -48.07922 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 91056e97-9bf4-336a-92ce-392a7cc75fa3 | -14.49983 | -52.99556 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0076968a-802b-38eb-b16e-97dd0038526a | -14.50193 | -52.04966 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8676736-0130-3c15-a162-32884447ffed | -13.36632 | -46.99736 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9f2fd589-f231-3646-83c7-03eccb80baca | -15.30977 | -46.09394 | 2025-08-30 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1b69d1f-0830-33ad-ae6d-2fe4ff1cf3ed | -13.75731 | -43.77549 | 2025-08-30 04:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e8b6d49-39cc-3c23-bed8-01cc15ce2362 | -12.69011 | -48.15215 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d227d73d-ddff-3771-a795-0ab0439ae56d | -13.38538 | -46.96064 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 63fa96e2-1ba9-36b2-a610-28e89c76571e | -13.53167 | -46.95296 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3fc8f450-1922-37e4-a201-7669381557de | -14.449 | -51.98235 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd2065bf-4f1e-3416-9c62-52096599e9b5 | -14.60404 | -54.51204 | 2025-08-30 04:51:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7d03887-ef49-3d71-9348-a4c753c35aaf | -14.00027 | -44.58995 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b3f3033-49e9-33a6-96ca-cd29f8241ecb | -13.38391 | -46.97167 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da5ecd4d-6c4a-3238-91aa-fbec499ad059 | -13.66037 | -46.92303 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2445920-8658-3978-96ba-af3a44c3e87d | -13.52326 | -46.95206 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae9ca038-730e-3f08-9053-645280a2a5a7 | -13.36921 | -46.88424 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3935812-f0f6-36ae-a9ea-ab9c0417df00 | -13.44278 | -46.94553 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1fa0ead-840b-36dc-b3de-0d62e596b8c6 | -12.84076 | -48.09898 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbef2e57-57e3-3afc-8907-4aaef3b294ad | -14.50039 | -52.992 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15691183-07d0-3632-8442-d928ceaff714 | -14.3289 | -51.88101 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f296227-8844-36eb-bddc-e3ea9956f7ff | -13.59657 | -46.88726 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff157402-59b8-34c2-9cf3-382315330d85 | -14.49593 | -52.99858 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 799b2a35-8f5b-3043-8bb7-d73f1757b133 | -13.63357 | -48.18617 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0930957a-8796-393b-a3cf-c970621ca820 | -18.10367 | -46.93047 | 2025-08-30 04:51:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b927870f-22e2-3c37-b23e-9bdb181eadde | -14.34884 | -53.32652 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 531facd6-cd2e-32bf-9889-1487499f7cd4 | -13.37762 | -46.88527 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c3dfff79-acf4-33f7-ab54-9006a1f77aaa | -12.8259 | -48.12069 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2e9c399-e6b9-3dcc-99ff-8989ab2893e7 | -13.68765 | -46.91146 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76b72736-8918-30ea-9d62-fe3a86413e2d | -13.58241 | -46.89441 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e1709b5-d667-3ed4-afac-6b90e3eccd92 | -12.65131 | -48.19316 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecaba607-ba54-3a3d-b5e2-44773836dd01 | -13.38355 | -47.00635 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 37f2ed74-00a0-3916-b4e5-1ef13e9889b7 | -13.49612 | -46.83758 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16a7f8d6-29e3-345f-9009-75e3a87bafeb | -13.36679 | -47.0244 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c3ba8cd2-44ad-34e8-a956-7f47406050e2 | -14.49524 | -52.04857 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c26ea7ee-3d15-3ea8-bf42-89128e2e88a4 | -12.82597 | -48.0922 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abb4c1cc-d200-39d4-bf07-1928b8a9f4c4 | -13.5961 | -46.88842 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7aa67b09-55d3-39a5-8dd5-8d103fed93d5 | -14.32724 | -51.95849 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae9ca215-a1eb-3e93-8235-fe8615a6c717 | -13.54057 | -46.9502 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e136a6a-00f3-3b5c-9b8f-135ef24ecc13 | -13.97798 | -46.3196 | 2025-08-30 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3d46e3e-b91f-37be-8d57-4c4c605f6a13 | -12.89658 | -48.89963 | 2025-08-30 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9682b4e8-ba03-3c58-8592-8a6a412fbae2 | -13.3625 | -54.38828 | 2025-08-30 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01f480f3-64d6-3040-9755-ab81089be2b3 | -12.83689 | -48.09851 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a5c3361-3ead-30b5-84a4-47b54a538138 | -13.39669 | -46.84271 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4733eb29-1e61-3e9e-85d2-7d675693dcbd | -14.60252 | -54.54272 | 2025-08-30 04:51:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54a0f41c-9a77-3210-8aed-2a4b8f727eb8 | -12.62685 | -57.0115 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ca4279d5-d3e5-36de-aef1-4c625984d836 | -14.49537 | -53.00215 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c35b606f-8929-3492-807e-220b53bb5bfb | -13.36841 | -46.98232 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6fef36f-840e-3a5f-9ef3-e4b191716eb6 | -13.38467 | -47.02971 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02c47560-bfa6-3191-b627-3f05a3ee09c3 | -13.63427 | -48.18099 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1abbf987-6eba-309c-a40b-cecc1b6ac870 | -13.62903 | -48.19049 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7552829c-21a1-3f14-bec8-1b31ff990f1b | -14.3278 | -51.95489 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 630a3c70-0aba-3f89-82da-275ad43a09de | -13.3684 | -47.01292 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1003950-c473-3368-ac30-3c07bcc67434 | -13.36733 | -46.99006 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README57.md)
