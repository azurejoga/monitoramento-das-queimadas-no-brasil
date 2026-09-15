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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9acfce90-5c3b-34f9-a10d-cc5f377c8510 | -11.7962 | -46.5926 | 2026-09-15 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| df86f571-4884-3a2e-916b-9608e836daa9 | -11.8365 | -50.0028 | 2026-09-15 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| acec9ddf-1836-3a36-bed2-d12936a2a84e | -13.2867 | -51.3046 | 2026-09-15 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 3898333c-4033-3bcc-8a57-699b609a4cc7 | -2.7768 | -49.4553 | 2026-09-15 14:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 9072d9ab-b428-3622-b180-97adb32dd126 | -7.082 | -42.1346 | 2026-09-15 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| 66ee09cf-b7e0-384c-ae9a-dd5c2a88d845 | -13.5722 | -51.4391 | 2026-09-15 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 9ba8091e-d8b8-337c-9696-c9983daa4dec | -7.0823 | -42.1107 | 2026-09-15 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| d5c5e6cf-da43-30bf-838e-ef6bf007a35d | -8.4852 | -44.5885 | 2026-09-15 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| c5255b95-5b9d-3f57-9206-6a3d6ce9a650 | -11.4357 | -51.4351 | 2026-09-15 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 5058bb96-11d7-3fb8-9546-7ede6dc39fc1 | -13.7006 | -51.8061 | 2026-09-15 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 257c7a4a-4f78-3f8e-8ba8-c90a51204446 | -4.6776 | -42.0713 | 2026-09-15 14:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 144.7 |
| 90890404-f157-3da8-b05d-848683af6916 | -10.8665 | -46.3105 | 2026-09-15 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 679b0e1d-9d7f-3d02-b936-600f4a8bc745 | -5.5286 | -43.3771 | 2026-09-15 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 84eb01a8-acac-3f01-afe0-ee6bf006076a | -7.1523 | -44.2385 | 2026-09-15 14:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 289.3 |
| 7c5fe70b-9e58-3642-a9c3-0ed7b5f04ecc | -13.3202 | -51.5986 | 2026-09-15 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 2f29c630-4907-3bc9-bbb8-3a5c45ba7765 | -3.3494 | -59.8097 | 2026-09-15 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ae221aaa-8c3d-3399-b75b-9f44850e9fbf | -9.7687 | -46.1067 | 2026-09-15 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 5e3b5ed0-cbbe-3948-9cbe-1fd8ba26ce22 | -8.5468 | -50.4423 | 2026-09-15 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 7583eccf-59ce-30b4-abc3-3b82a8b3ec28 | -8.638 | -44.4567 | 2026-09-15 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 346.7 |
| b666c1cc-ca90-3741-b648-85ce4ba1ada9 | -10.7726 | -46.2322 | 2026-09-15 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 8d5c09c9-04c7-32c9-a6e0-18a4d9a75a57 | -7.5608 | -62.33 | 2026-09-15 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| dc7bbd7d-bcd0-30e6-a325-b6c56fcc80fa | -8.5656 | -50.4407 | 2026-09-15 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 147901c1-619c-3f0a-874e-64e20e0d5e6d | -10.7084 | -50.6212 | 2026-09-15 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 6957b832-e379-3327-8298-d832c1af84ea | -13.553 | -51.4416 | 2026-09-15 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 80f9ee04-e85a-3832-8479-b8584ab6d489 | -18.1709 | -51.7685 | 2026-09-15 14:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| f05c8dac-04d4-30f9-b870-69c4efdef445 | -10.312 | -45.2907 | 2026-09-15 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| f2bc77d5-c277-3947-9706-f7f53c36430f | -9.4266 | -60.3003 | 2026-09-15 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0828cc0e-ffe4-3349-8eb3-c1080897c06c | -11.3642 | -43.9407 | 2026-09-15 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 5bc32cf9-3328-385b-b940-6752d0978169 | -6.6952 | -58.7097 | 2026-09-15 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b566312a-bfe8-342e-aa2b-78d647b25824 | -6.6021 | -58.849 | 2026-09-15 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 31346f22-5952-34b7-a28e-0c282b669719 | -8.8078 | -45.8979 | 2026-09-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 1b6f5f28-9869-395e-9c53-772ce5a8e304 | -7.1711 | -44.2367 | 2026-09-15 14:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 183.9 |
| f78dbc10-3683-3ae6-887a-1771eccbba25 | -6.1178 | -59.8877 | 2026-09-15 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 014e5ba3-fe72-395f-9538-eab9d2eb877d | -7.5608 | -62.33 | 2026-09-15 14:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| f2234662-e657-3941-acda-cf1d44f93e91 | -13.287 | -51.2832 | 2026-09-15 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 2cff4a35-a66f-3ec2-b462-9970d11832a0 | -13.3 | -51.6649 | 2026-09-15 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 52c5c061-f9e2-3830-bc62-6810a6ad54f8 | -8.6191 | -44.4588 | 2026-09-15 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 9ba36a59-34e5-3221-a012-87ad07af9a5a | -11.3642 | -43.9407 | 2026-09-15 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| f656b69f-5cbe-3f8f-a252-288f070d7397 | -8.4756 | -46.8498 | 2026-09-15 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8d4ebaf8-76ac-3998-b44a-23fccfb35cb2 | -11.2304 | -54.0985 | 2026-09-15 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 00a01287-deca-3ff6-8587-ab6edf8dbaef | -6.6952 | -58.7097 | 2026-09-15 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 44f310f6-9c77-3271-9b99-4d2fce038e19 | -2.9395 | -50.3994 | 2026-09-15 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 7e504b42-8278-3756-9b6b-665a6e72b7aa | -13.2867 | -51.3046 | 2026-09-15 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 5e7c38b3-da4a-3190-a982-c88162889387 | -13.2239 | -51.6318 | 2026-09-15 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 89b6ccf8-f5c9-3cef-8792-557670f5bc9e | -3.3494 | -59.8097 | 2026-09-15 14:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 4273e5d2-f10d-32d4-9d0e-e9e141d9a642 | -3.4943 | -54.6567 | 2026-09-15 14:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1ce76ff0-659c-3f84-bbc4-ab0f06cdb284 | -9.7548 | -47.0937 | 2026-09-15 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 2041becd-6247-3eaa-a023-e87c294b6341 | -13.3946 | -57.0444 | 2026-09-15 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 62e184de-ee08-36e9-adea-f720f588e60e | -10.6417 | -46.0906 | 2026-09-15 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 5e56851e-9346-3017-a911-6834fc1102c0 | -10.6335 | -50.5651 | 2026-09-15 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 2cbd1df0-36c5-34af-9314-2c81dc9eed42 | -10.6827 | -54.1679 | 2026-09-15 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 984655a3-5e68-36fb-baad-9134b8eaaabc | -6.1362 | -59.8871 | 2026-09-15 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| de4b823e-5391-3b65-a93b-d41c35864baf | -13.2235 | -51.6531 | 2026-09-15 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c6f6e326-1191-3757-a7cf-14a2e28ebcd4 | -10.2929 | -45.2932 | 2026-09-15 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 7b365da2-f893-399d-8d74-442bab38fddb | -9.7687 | -46.1067 | 2026-09-15 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0623eceb-5fcc-32df-a566-613a6301886a | -10.312 | -45.2907 | 2026-09-15 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 147.4 |
| e44fd0b6-dcce-3682-ba3b-c394931767c9 | -15.3598 | -52.989 | 2026-09-15 14:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 6ec338ec-fdae-3e45-938c-73cc2a4833a5 | -13.9941 | -53.8731 | 2026-09-15 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| a0fc457d-748b-33e5-a433-50f6f9801ee2 | -13.3062 | -51.2808 | 2026-09-15 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.8 |
| cdefff60-7533-3922-907f-6185485034e0 | -14.2985 | -51.7286 | 2026-09-15 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| abf8913a-5924-3ecd-9902-04d94bf0d03e | -13.7002 | -51.8274 | 2026-09-15 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| abe0e4d7-d937-35c7-9a27-373594a71e0d | -3.1174 | -57.6779 | 2026-09-15 14:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3d27aeb5-97e4-3b73-ad0b-4ce0bb5370f2 | -12.6824 | -54.6968 | 2026-09-15 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a847a58e-cc26-395c-94f3-8c6fcb9aa936 | -5.2023 | -49.3348 | 2026-09-15 14:50:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3887d522-9fd0-35f5-9af5-6686c878040e | -3.3676 | -59.8285 | 2026-09-15 14:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f39d93c0-a1fa-3fff-9708-5355eb19b331 | -11.5045 | -45.771 | 2026-09-15 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 80b79ffa-4b16-3e24-90b3-e2dcf7032402 | -15.5786 | -53.8031 | 2026-09-15 14:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 2f31f323-5f51-3196-9542-a2623a061b1f | -13.3949 | -57.0242 | 2026-09-15 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 9646aa5f-9553-35f0-a315-d783beca6651 | -11.8365 | -50.0028 | 2026-09-15 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c97a3af3-a900-3ded-8b53-d1cc07f57297 | -8.8078 | -45.8979 | 2026-09-15 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 7f7842c2-d34a-354a-b45c-76d20f4b33a7 | -9.1337 | -65.8253 | 2026-09-15 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 2a8c8c31-41d4-3a5f-a0ba-d08999aaa4e1 | -15.2827 | -42.783 | 2026-09-15 14:50:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 89.4 |
| dca904b9-d2b3-38be-b88f-ad439e4cf10e | -13.5719 | -51.4605 | 2026-09-15 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 038804df-3c88-3818-914b-ee2125fab962 | -6.1177 | -59.9069 | 2026-09-15 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1fed3dd1-f80c-35aa-ad99-1f5aa53d5683 | -6.8217 | -43.5271 | 2026-09-15 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 041f1575-14b8-3120-b332-92b5509604f3 | -10.3116 | -45.3136 | 2026-09-15 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 111.5 |
| d8dd85ff-1cc3-3cb6-96a2-173f551fa396 | -6.0256 | -59.9293 | 2026-09-15 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e246e769-536a-360c-9495-ac001e901fd8 | -11.4357 | -51.4351 | 2026-09-15 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 2924a4d3-c487-30d9-800a-e97f692220ad | -8.7889 | -45.8999 | 2026-09-15 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 3e55098f-e31d-3910-894f-5d4c9ce2c0c2 | -3.1816 | -61.1235 | 2026-09-15 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b74c71d6-294c-3ca2-9824-1c2871216068 | -4.6776 | -42.0713 | 2026-09-15 14:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 153.4 |
| b4891e30-a14c-31e7-98fb-f0f683003ab0 | -6.5837 | -58.8498 | 2026-09-15 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b4ff14ea-8e31-3ac9-8d33-3f48263b48c0 | -10.6829 | -54.1475 | 2026-09-15 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 5eea6b26-5985-33fa-bc03-0ae1e8c5239a | -10.2926 | -45.3161 | 2026-09-15 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 527549f8-3a0a-300e-9952-7db45b016273 | -5.5286 | -43.3771 | 2026-09-15 14:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 8c4bb89e-d191-3952-a2b7-e999d0991ef5 | -11.383 | -43.9614 | 2026-09-15 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 73fa1fba-a56b-318a-af5d-5355f6e57d2a | -11.8154 | -46.5899 | 2026-09-15 14:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 235.1 |
| be0b96dc-9b68-3596-9af1-44448a1fc608 | -13.2232 | -51.6744 | 2026-09-15 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| e279fe57-0c51-38f2-80b9-84a6d736ca69 | -10.2922 | -45.339 | 2026-09-15 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 3353a372-fb5c-386f-a75c-53c2eabaa919 | -6.6767 | -58.7105 | 2026-09-15 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 69a795f8-a12e-30ad-905c-6b55aeed46eb | -12.1265 | -44.199 | 2026-09-15 14:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| cf55962a-f2c3-30a5-8814-074f7658a8f0 | -11.5041 | -45.7939 | 2026-09-15 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| cddbb95a-b743-3814-b9ab-d15d73737be0 | -10.3113 | -45.3366 | 2026-09-15 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 58ed8b03-358c-3996-87b6-bd8be9720969 | -6.1178 | -59.8877 | 2026-09-15 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0a1e3fb9-1b3c-30be-a2f8-963262db1655 | -9.1337 | -65.844 | 2026-09-15 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 0b22ba1a-2a3b-30b3-a75d-c3aeb0e05a2f | -6.0991 | -59.9459 | 2026-09-15 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 757faadf-cb1a-3861-8476-d038b92d85a0 | -13.7006 | -51.8061 | 2026-09-15 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 604ef02e-bd4c-3c3e-afd1-f3a3bbd114e5 | -11.2302 | -54.119 | 2026-09-15 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4e572368-3033-3300-a512-0b05642284c0 | -10.6641 | -54.1491 | 2026-09-15 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 5011469a-03d7-3195-99d2-acf6bcb60fb7 | -11.3638 | -43.9642 | 2026-09-15 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 255.9 |


[Clique aqui para ver as próximas entradas](README83.md)
