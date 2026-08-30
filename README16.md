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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 327dc47a-4aef-345a-a552-65848ed5f9c8 | -16.1383 | -43.0355 | 2026-08-30 00:55:00 | METOP-C | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 17fadca9-dd14-391e-b073-ba719730343a | -6.9359 | -55.6936 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ba9cd84-2274-3fc0-a4e2-ff2ad7f1b4e4 | -10.488 | -59.612099 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa9bdb36-2b2b-3679-acc5-af730d6492f7 | -11.8315 | -51.115799 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2784efac-c1a2-34a7-bc16-bd07f518d0a4 | -5.9886 | -57.682301 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb3d4495-94ac-3a1f-94eb-eb520155009a | -3.6324 | -60.550098 | 2026-08-30 00:55:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 394cce7f-00b9-3940-a956-f87ec899f95d | -9.8817 | -60.270302 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90c97012-812d-3b75-bc85-00ebde5545ce | -9.8949 | -60.285702 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 099a50c0-d0a2-3d62-ab3e-d801e1648909 | -6.9431 | -55.726101 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b1f3f92-051f-3194-989f-bf0291fad741 | -9.8914 | -60.268398 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38a7270d-d84d-3ffe-9592-baef55055f99 | -11.0453 | -57.225201 | 2026-08-30 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac80a8f3-4946-324c-a00f-5250056dc411 | -10.9374 | -43.0131 | 2026-08-30 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1b849b7-3c49-355c-952f-3136dbeb28d1 | -5.4919 | -57.149799 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 237015eb-db79-3019-ae20-7a656ab44dc4 | -14.4159 | -52.549301 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0143036-be70-3fef-94ce-a5b3d670d0cf | -12.553 | -55.737801 | 2026-08-30 00:55:00 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c5a7f28-967c-3f27-b143-2004be0eea00 | -3.8151 | -52.367802 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5158ab63-cdc3-3e64-a728-632e0ed46efc | -6.8667 | -59.4664 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7583dd7c-9f95-3c8a-a0b8-4b529765bffc | -6.7898 | -55.682999 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96a308c2-572c-3e8c-a05f-ae94ddfd97fb | -9.6734 | -55.0644 | 2026-08-30 00:55:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe8c26e6-8a69-34f4-a29c-9d5e378c41fc | -8.5035 | -55.301498 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df5c8119-e2ca-3857-86f1-09633de15aeb | -13.8585 | -54.111198 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77cbf43f-d2e4-3f0d-b6a9-aa7218ac18ab | -12.6898 | -47.456501 | 2026-08-30 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17ca9b34-9db8-3f2b-9236-c91a962f4385 | -5.7821 | -51.680901 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d7f3ab0-9057-383e-8d64-2d9b949db22d | -9.1666 | -59.6054 | 2026-08-30 00:55:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c64ca2c6-5207-3a02-8daf-f06d7a9bbdb6 | -15.129 | -53.576199 | 2026-08-30 00:55:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0e5127f-95db-330e-93ee-6b68a6e9c93f | -7.3991 | -60.581902 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a027cd8-0c56-3cce-901a-7f401f86af60 | -12.551 | -55.728199 | 2026-08-30 00:55:00 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d53a3702-c3aa-3089-8b63-e15b0aa4d4b2 | -14.4387 | -52.559601 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a5edcaaf-9061-3f38-8b68-483c72e4d818 | -11.0072 | -50.534302 | 2026-08-30 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd96e11a-a754-335e-953b-37b5c4673c04 | -6.9395 | -55.709801 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a1b68fc-73db-3910-ba15-252d05b2803d | -6.8638 | -59.452702 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 536a859e-79b8-356a-a301-50579ff0e38c | -6.7826 | -55.6507 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96ed3f9f-6fb4-3d7c-940d-6079c5e77194 | -6.9297 | -55.711899 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6392e8e5-8061-370a-ab58-74b91c57afee | -11.0429 | -57.214001 | 2026-08-30 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b78341c3-c2a9-33e8-a522-d46346a0d215 | -11.0281 | -57.240501 | 2026-08-30 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d99d9c7f-6740-3b0c-ae00-7a30cfb770c0 | -14.4175 | -52.556702 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 18bfb54c-54b4-3a89-90e4-e071613bbc9f | -7.3018 | -60.602001 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 166d0238-3e15-37f9-acf4-c703ab323dea | -8.1871 | -54.938099 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10963cf5-faa3-3797-b981-e897a02e09e8 | -6.9377 | -55.701698 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49f818cb-e9b6-3a5f-ae7b-dabe151ec95c | -9.7085 | -60.7146 | 2026-08-30 00:55:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b53eef67-a868-3179-99f4-d0dcaafc3e0c | -3.221 | -49.224201 | 2026-08-30 00:55:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe41b0b1-b7e0-3571-8ffa-8519ab2a1850 | -6.1549 | -57.785999 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1661b57a-96f1-367e-b165-df28d411ede8 | -14.5899 | -53.069099 | 2026-08-30 00:55:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08b288ff-fafc-3a32-9f53-fad9f2662d87 | 0.2206 | -51.4491 | 2026-08-30 00:55:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d1d7995a-4bee-3339-9a8f-f980f45bd6d9 | -15.3687 | -52.679699 | 2026-08-30 00:55:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 34862108-73af-3883-814e-4478254d1a9a | -10.7469 | -54.054699 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc6248de-757a-31f0-b53a-8b23e9a41054 | -5.8555 | -57.542999 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc569c49-4a52-333b-812c-9a9c0eb6bd66 | -11.298 | -54.0378 | 2026-08-30 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7d2e81e-f460-3738-a9da-3d535d60760b | -8.7986 | -50.490601 | 2026-08-30 00:55:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfdba6af-a698-3e51-9531-bae7f992500e | -9.7659 | -48.150799 | 2026-08-30 00:55:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f78a8be5-6030-3d5a-a4d5-e0af7eb2841f | -6.7924 | -55.648499 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfe94f83-d8b0-3249-8153-0fb22c35642e | -4.9654 | -55.847198 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 574635e8-376c-3976-bd8e-5dc6418c2941 | -7.5119 | -55.3241 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c97fc4e-c81e-3688-bc21-24ffda788c1f | -13.862 | -54.1278 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92be188c-1a47-3ff9-a945-53522ad2b60c | -6.854 | -59.4548 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 506796b2-26f0-3ad1-a6c5-1b7072abc4c1 | -7.5112 | -55.274502 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f589eb0-7b28-3e93-b0cf-82e4fb70e4e6 | -6.9261 | -55.695702 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84c73365-b20c-314c-8cd1-1709c2697acf | -5.9691 | -57.686501 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 354a8806-4f04-3ec2-adb7-eee3b7e8af0f | -14.2046 | -52.8536 | 2026-08-30 00:55:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4507049f-226d-31e8-82d9-0dd3bc61d240 | -5.8997 | -57.743999 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea2564d6-17d7-3330-9f67-21168c8f8198 | -10.7517 | -54.029701 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5b3514-04db-3957-b82e-6d251410bc9e | -9.4212 | -51.581402 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a12d2c73-3e10-3133-8dce-4721d6c32eb5 | -6.4247 | -55.52 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28bf7c05-ae93-3243-a83b-f180d85b2ad1 | -2.8005 | -49.585899 | 2026-08-30 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b25c699d-b585-3b7b-9894-ceef3aa1558d | -15.1307 | -53.5844 | 2026-08-30 00:55:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc4c2000-f306-38cd-86f4-9a5f1a41be42 | -11.7976 | -51.0574 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f910acb-117d-3db8-8498-1bccaa79d753 | -5.8922 | -57.756302 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b660dba-d8a8-3bc2-83ea-4be2310d1c0f | -14.4273 | -52.554501 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f86bdf5a-4b16-3870-bc1e-4801d9187db3 | -8.1854 | -54.930302 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de401ba7-00e5-313b-a5b6-da29d81786b6 | -14.2764 | -57.034698 | 2026-08-30 00:55:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c63d71c-90dc-312a-a2ee-36bb9462fa2d | -11.712 | -54.527302 | 2026-08-30 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8df96f1b-3c13-3df3-928d-da6433bad9bb | -6.119 | -53.562401 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 979c62af-18d7-319f-802c-8dbd55204077 | -3.4935 | -54.662899 | 2026-08-30 00:55:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60946d4c-3d2b-35af-a8b8-d587a769301c | -2.9415 | -51.484901 | 2026-08-30 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec833512-5e02-3eef-b2e5-952006740524 | -11.8074 | -51.055199 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a50622b0-22b7-34c0-b1f9-83e7bfeda8d8 | -11.239 | -54.002499 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0264cf1-df2a-3885-b248-d5d0d5588686 | -6.788 | -55.6749 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d698e07f-c774-32d9-98a1-357098b284e4 | -10.7534 | -54.0373 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bad69849-2c2c-3afd-9fb5-7837ec286ea0 | -10.7749 | -44.8876 | 2026-08-30 00:55:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 93284b84-5ff9-321b-ae6c-3dd7b5359b56 | -3.6886 | -51.996799 | 2026-08-30 00:55:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffa5067a-3faf-3fc3-ab2d-6b40778324d2 | -5.4821 | -57.151901 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddc37728-bb69-38ba-882e-dcdbc0b06bdc | -13.8232 | -54.041401 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a325352-d5bb-3a70-976b-a09c08640213 | -13.8736 | -54.1339 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ef360d7-911c-3bcb-b560-ae76c484eeed | -6.4941 | -53.2617 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee835e48-115b-3814-80b8-0478af4a6a18 | -9.1545 | -59.4981 | 2026-08-30 00:55:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3476d3e-719b-31cb-b280-0eee3cb6a8d1 | -7.0873 | -51.570099 | 2026-08-30 00:55:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39b32f22-243a-38d4-84f6-761f3422ba50 | -15.1209 | -53.586498 | 2026-08-30 00:55:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f17b875-5e53-3220-80ba-065f1257a0ae | -6.7746 | -55.6609 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bb66d1c-bd81-3e36-a4d8-34b0fcb0f355 | -11.6344 | -54.595501 | 2026-08-30 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e207ba8-0ce1-3b00-9a1f-a18e7033fde1 | -10.9941 | -50.522301 | 2026-08-30 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e417a009-3820-3942-a3ae-6befcf36ab27 | -4.9265 | -55.7654 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e821596-da37-336e-b2db-7a79529a1742 | -4.9539 | -55.841599 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 391d47ad-e9b0-35b8-ba6f-aa0791e4ffee | -14.2528 | -54.6703 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4c1aec5-45d9-30a9-a49a-b932a12e2850 | -16.3596 | -50.9972 | 2026-08-30 00:55:00 | METOP-C | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 26e3dc76-06cb-35d3-888a-7acedebfca93 | 2.1915 | -50.704102 | 2026-08-30 00:55:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 024db6e9-7fab-3033-8a44-e7997cbb6b78 | -6.1571 | -57.796398 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0508034c-fa6b-34fb-ae7c-a184081e5f7f | -10.7444 | -50.827499 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5bcb8393-8686-3211-964d-70a5e9240317 | -10.1275 | -45.687801 | 2026-08-30 00:55:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f38f0fe6-bd52-383f-bc0a-d8a104f44539 | -14.1507 | -52.842201 | 2026-08-30 00:55:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c64c73d7-9518-3ddc-a558-932c9788503a | -14.4305 | -52.569199 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README17.md)
