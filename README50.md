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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 857628e6-7de8-3210-9a14-705811979b19 | -15.44963 | -48.46438 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3de9156-7716-3ced-88f5-afc5196ae7ee | -11.01417 | -54.13753 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e56c0a4-6932-3561-9746-8a0505458e54 | -10.46379 | -51.34122 | 2026-09-21 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 801b14d6-b3e7-3a20-83f5-6d4da1f32809 | -11.79233 | -51.11754 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b55f0b53-78e9-346c-8e38-e8b12cb4dd0f | -10.08949 | -50.267 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 771e1768-d9a7-3594-8749-aacfd9779801 | -11.95496 | -46.50182 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e43dd17a-95e5-3cda-97ad-5755b82332dc | -11.88851 | -49.00344 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad9e036b-0d57-3366-9d96-1ad72e51e228 | -12.31244 | -50.69215 | 2026-09-21 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d9f46ba-0364-31f0-897a-7e4a0d91a4c6 | -14.64738 | -45.70138 | 2026-09-21 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90fe56fd-5203-3cc5-a0f4-4d47e0cd583e | -10.91716 | -53.96178 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9866660-41e2-3e6e-b2e0-52db312fc702 | -10.80203 | -50.84059 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fccd2646-464e-3007-924a-1278ce0987a4 | -10.38255 | -48.91436 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9c11b47-5075-3652-bbde-b6cee0377428 | -12.6858 | -50.95877 | 2026-09-21 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9eb5aec-8671-31f6-8d1b-e8bf86389e85 | -10.15327 | -44.82778 | 2026-09-21 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c81c9aaa-d742-332c-85a1-5abc785fe619 | -14.07263 | -52.12715 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f73d0c4-6ce6-3b70-b19d-68ce117600a6 | -11.987 | -58.07527 | 2026-09-21 04:21:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04437dc1-d0ec-3751-a10a-0bb30b55e898 | -13.7129 | -45.51242 | 2026-09-21 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c23e5a5b-0528-3b89-b8cc-6f2753a6223d | -10.16045 | -46.54937 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e90714fb-81d8-3d4c-85f2-3048cd9cda80 | -16.03024 | -52.52489 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9633702-61aa-318d-86e3-11e306cdccda | -11.7543 | -54.57527 | 2026-09-21 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04eadd69-f43c-3db5-aa90-4ae17d7fca75 | -11.80739 | -49.81587 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ad9ce25-a1d2-3a7a-b13a-4929cd521862 | -9.74535 | -46.06984 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33d0d700-994b-31de-a5fe-b4ca4dfe8390 | -15.45179 | -48.47336 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f47e0c49-fabe-3c99-9837-9bb1b69d4475 | -11.80868 | -49.80855 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bd592e78-75d2-3cb9-944b-0ef25f7ced6f | -11.86612 | -49.9796 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94e621eb-2986-3a50-8f17-53a4d39cd3a4 | -16.03111 | -52.52022 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 32efb925-22ec-355b-bd79-c1c29770d7c9 | -11.34216 | -43.38159 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4826289-92d9-3abe-8695-2606c34e8b9c | -11.47831 | -47.76903 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 74ca93d7-dd30-3fea-84bb-d8789fd0fa3a | -12.48359 | -44.72132 | 2026-09-21 04:21:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79036d77-7c64-3c7f-af2a-b1e7ea019a96 | -11.03943 | -54.15411 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdd710dc-2dfd-3815-bf7b-d7e4b5b607c2 | -14.92342 | -49.90063 | 2026-09-21 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d66f4f20-31cc-37e6-8ea7-59072901e714 | -12.7735 | -52.85756 | 2026-09-21 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8bb2114c-823a-36fd-991d-edba3f697160 | -11.05032 | -54.15664 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54c481f7-1dd7-38b2-91c6-c3478429f592 | -10.79994 | -50.82656 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f59a675-3086-34e8-bbe8-760c775c0329 | -16.03288 | -52.51786 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 532f2d91-f243-37cb-adf6-c26e622ac942 | -10.80584 | -50.83993 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b66fea4-1fff-3893-9396-e80942eaa121 | -10.87136 | -54.05297 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5a88a35-a18e-32b4-b46b-bf65e4a24e53 | -10.37692 | -48.92377 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3a107187-2863-36e2-baa6-da478885aa8c | -11.09482 | -54.01656 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 407dacdd-a8c1-3b84-aa93-d04e6b4a5079 | -11.08289 | -49.7539 | 2026-09-21 04:21:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab6a6562-4bb8-3228-bf08-ad04bb17e4e3 | -11.07717 | -54.02044 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aba4efeb-a07d-31c7-9211-d471a641fb9c | -12.66077 | -47.02339 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b23c9af2-c47a-33bb-81a1-1cf0825feca4 | -11.75505 | -54.57145 | 2026-09-21 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06ea160a-8063-3312-b941-76f5f3ba2527 | -15.46937 | -48.40485 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fc6294c-4d68-3d12-b588-df85d1109f7a | -12.1127 | -47.03772 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 838d5001-7ef4-334f-ba18-d4e7936d3083 | -12.3167 | -50.69296 | 2026-09-21 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0c7c164-0547-3fdd-aecf-928138e7297f | -15.85916 | -49.9059 | 2026-09-21 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7379979e-f34d-33f0-885e-0a211de3629c | -12.30173 | -49.18063 | 2026-09-21 04:21:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 821fe957-efe7-3f30-83e7-5f594eff5954 | -11.47398 | -47.77254 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8ae4bb66-2a84-31b9-901f-5f999d15d359 | -9.98188 | -50.26098 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a78b4242-2b70-32b0-bfc3-debee14266cf | -12.89679 | -50.9697 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 01d5c63f-2a14-3f36-99ac-d81d29bef23f | -8.19361 | -54.70308 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae4d21c6-4f6b-3fc3-8beb-549e79e0d57e | -10.58805 | -57.48036 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 636d5ead-fdc5-3a39-ad0d-2211b65f7492 | -13.89671 | -48.571 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 399203ee-932f-375b-ad25-453d64730460 | -11.11247 | -54.01261 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d44cc14-f9b3-375b-a2aa-b7ddb2698adf | -10.47645 | -45.09797 | 2026-09-21 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51b10a89-9d42-32a3-b5ab-5b10efe57210 | -11.32255 | -47.29714 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60e66ddd-34ec-39e4-a738-faa159c2477c | -10.77268 | -50.82597 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99552f3e-7892-3ae9-b603-def8d480d187 | -12.10868 | -47.0486 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca884439-d934-3535-b314-63ed655d42b8 | -10.76827 | -50.82512 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb90fbe3-6e32-34e7-8eb6-9717098e1116 | -10.37241 | -50.21933 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4dd6b36-30f4-38db-8f78-a87729061cdf | -12.80439 | -54.05317 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 965a27bd-c941-3d3c-b2a8-1d6e1d2c2cdc | -10.87038 | -50.93886 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 955cf510-235e-3e0c-a276-2243c4f7a765 | -11.04556 | -54.15173 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae73e60a-64dc-34f2-a8a1-ba237eab55fd | -11.62262 | -47.78009 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d54c3ac-cb6b-3f80-a516-53d896da2943 | -12.80342 | -54.06419 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84931cce-fa1b-3c77-a07b-76b64edcfa1a | -11.08151 | -54.02061 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ef76df6-5ffd-3c49-ac20-97cf3c2079f6 | -11.94347 | -46.50749 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61009397-5a12-3c3c-88a3-27655e14f83d | -12.79879 | -54.05975 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e04622b0-63cb-31b4-8ab4-633970e71fd4 | -10.46581 | -50.2805 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 82d6edc2-50e4-3709-8638-18fb9b114e4b | -11.0121 | -54.14839 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7493a555-cbc6-3849-aa82-4bd2e96a56fc | -14.10066 | -52.1283 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3c94e310-12e7-3ea7-8448-42569f5a96f3 | -10.08738 | -50.25381 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c3ecdee-1cc1-3e86-9749-ef24aa6de7b6 | -10.39035 | -50.23285 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8aaa2c4f-b480-3025-921d-797b6eae58d0 | -11.01828 | -54.14578 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74fd2717-f7f0-3443-b2f2-665689735a2c | -11.67924 | -43.44184 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32de2cbb-ed42-342d-b0e4-87dc22841fb1 | -11.79115 | -49.81285 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a28389c-5f0b-35eb-99b6-b543630401c4 | -15.45683 | -48.47652 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7f4a18ea-6fe8-3e67-bcf4-98a49356a4d7 | -16.02751 | -52.51452 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b60efe5b-7fb3-34c7-9c36-1bb573ec4dbd | -13.02637 | -46.96077 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 992b7f59-8d1a-3428-8696-67c8315b32f2 | -11.88382 | -49.00763 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c449f321-1238-37fb-a3f6-7e5d5708e2d4 | -12.82151 | -54.04974 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37559bbd-bb8f-3a11-8419-3920610b65b3 | -11.03907 | -54.91382 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 186fb0c4-830a-362d-a09f-1d09ae906136 | -11.47108 | -47.76765 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9b60fe96-1f85-3697-a9a9-995c757e7742 | -10.50957 | -51.37311 | 2026-09-21 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e89e361f-0ea1-3bdb-9826-d3004675cf2d | -7.58536 | -57.69082 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6e5cbc42-841f-331c-8524-ef4317e0346b | -11.34296 | -51.35609 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d42ab5f-9c85-379c-b8f0-8b5261fda477 | -9.81679 | -48.30918 | 2026-09-21 04:21:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f716dba5-595e-3775-b76e-23d9a0dc912f | -11.3852 | -44.23627 | 2026-09-21 04:21:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c805e4b-49dd-3ab3-930a-5c3e729e6ed4 | -12.11416 | -47.0374 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b57c453-91fc-3898-ad63-e768ccc6d72e | -11.04428 | -54.15952 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 54d5cce1-9ba9-3d88-94c6-db78d411f18e | -11.94718 | -46.48497 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cd4f18a-c693-39d0-9031-46a38703f030 | -16.04633 | -52.52076 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e6b47fa8-1c6b-3c38-8302-ac63847ed083 | -11.94409 | -46.50375 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8610f01d-9081-34ed-9dd2-2438530b06a2 | -16.01943 | -52.50785 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a042638e-abfe-3d33-bc5b-8a8d5e0bd19c | -15.96974 | -50.11698 | 2026-09-21 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0e4a772-c794-3d7c-8dda-61605d38b013 | -11.79521 | -49.81361 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fe1e939-5765-3fbe-9a17-744f20d02cc9 | -12.86396 | -50.95479 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 799a1b5b-1df4-3807-965d-feacf0cfc266 | -13.92626 | -47.84122 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 912a5fd1-28e1-3cb5-a7b8-24626e569195 | -11.76042 | -47.43304 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README51.md)
