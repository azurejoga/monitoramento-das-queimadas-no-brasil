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
| b8b9fdc3-6c94-309a-8e02-7a7fcfb552f7 | -20.9178 | -48.8271 | 2025-05-08 03:49:00 | NPP-375D | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 31bb2088-21c2-3d4c-ae46-a19bc6ae5151 | -20.06564 | -49.36411 | 2025-05-08 03:49:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73ab3673-cdbd-3542-ae1b-5f0e2e4859ba | -21.18192 | -43.98083 | 2025-05-08 03:49:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6ccdf383-537c-3982-ace7-830a7f108622 | -20.91749 | -48.8273 | 2025-05-08 03:49:00 | NPP-375D | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a5dffa95-6e7f-362d-afff-4fc70d04e198 | -14.6414 | -45.1263 | 2025-05-08 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e071b868-fa05-3515-864a-bb8f78ab3467 | -14.6414 | -45.1263 | 2025-05-08 04:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 82c966bc-6f7b-35bb-b37e-efdc3a623df6 | -8.07 | -43.1216 | 2025-05-08 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 01241b30-258f-3bde-ae2f-35a9c5f27cc8 | -14.6414 | -45.1263 | 2025-05-08 04:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 9c37248c-e426-3821-b7bb-2bd98a0317e0 | -8.07 | -43.1216 | 2025-05-08 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 2ccb0028-59f9-3670-8013-57ceda8ccddc | -14.6414 | -45.1263 | 2025-05-08 04:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 0e812a5a-3cbe-3010-8088-10df2ee2aad4 | -8.07 | -43.1216 | 2025-05-08 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 6861db3d-31ec-32d8-a45d-d9b4f8393fe3 | -14.6414 | -45.1263 | 2025-05-08 04:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 2ac47bd1-534d-36fc-a3b1-65402862ee0a | -14.6414 | -45.1263 | 2025-05-08 04:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 0c768b75-1223-3c1e-a165-406ad407c1c2 | -14.6414 | -45.1263 | 2025-05-08 04:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 071f0043-bf3b-3a19-839e-047b73e67dae | -8.07 | -43.1216 | 2025-05-08 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.0 |
| 12f0153a-0206-3ac1-9f52-1b39242822db | -8.07 | -43.1216 | 2025-05-08 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.6 |
| 64449a56-e2e1-3b32-918b-60fad6644ac9 | -6.5631 | -51.1126 | 2025-05-08 05:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 456d5291-cdf9-31aa-b902-4033a9530bdb | -9.32323 | -49.48497 | 2025-05-08 05:23:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d6d95d3-fd6b-3f08-8e99-42c484d72534 | -9.31691 | -49.48399 | 2025-05-08 05:23:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0723e3f5-f6d1-3552-83ae-ef8f1795b8b0 | 1.1207 | -60.53768 | 2025-05-08 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c16f9d2-e099-39e7-8972-f06a727c1d3f | 1.11672 | -60.53455 | 2025-05-08 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe00db8d-e7bf-357c-9ee7-c29a7e4856ab | -11.38966 | -52.94659 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a31d1b33-4808-3982-a92f-fc795cb9f46f | -13.49699 | -52.96385 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3588a3d3-f843-3edc-a959-c2e68e638c89 | -11.39094 | -52.94347 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 08fddf3a-1f07-3f4b-b9d5-40637c5474b9 | -13.49124 | -52.96642 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 828789cd-185f-3798-a6d4-d8dfedcf428f | -11.62924 | -54.93822 | 2025-05-08 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc1bb8cb-899a-38e0-a9c2-44775d69e77d | -13.49205 | -52.95974 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 691c6f84-8e64-3232-a40e-83b81e07075f | -15.36711 | -60.17075 | 2025-05-08 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04be11b8-eeb3-337f-af56-8a98f5dcd83f | -9.48464 | -61.88276 | 2025-05-08 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de6a87a1-6a57-310a-898c-374b8f09f964 | -12.65049 | -54.05876 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 191134d6-4005-3119-8708-2fc2793a10a1 | -13.05243 | -53.72495 | 2025-05-08 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a45b0997-50d9-3308-9920-db3fee53c359 | -13.50191 | -52.96803 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f5e84983-fc21-3b84-8a50-cfb0e4e390c0 | -13.62839 | -54.88039 | 2025-05-08 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3c8acb6-5ab2-3ce5-a572-5decc8b518a7 | -13.04155 | -53.72976 | 2025-05-08 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b798398-3978-3afe-a550-83b20aa9942a | -15.39051 | -60.18269 | 2025-05-08 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be447aa3-6d8f-3ffa-a4a7-e1cb637d67bc | -11.39008 | -52.94341 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e773cd7a-f27a-31c5-a438-38d4ceb963f2 | -13.05317 | -53.71898 | 2025-05-08 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 89e81d92-7757-32ac-943b-5a3289de969f | -11.39445 | -52.9504 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5de4ee96-4324-3e6e-be5c-41220b72d04e | -13.50109 | -52.9747 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 722cf66c-4fb1-3bbd-bcda-639b051a8acd | -13.36994 | -54.2536 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 626a5e19-fe1a-3b8a-8457-4fdeeafcebd4 | -11.92231 | -63.95265 | 2025-05-08 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc7c383-80ad-3091-943f-22d36c05befc | -13.37082 | -54.26567 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| adcb8603-6421-348a-9c79-4e257b528863 | -13.4863 | -52.9623 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a9e39c5-4cd4-3907-a630-84e0f8c30064 | -13.92928 | -55.97524 | 2025-05-08 05:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a4330d5-b78e-3124-ad8b-c40aae18f497 | -9.48131 | -61.88221 | 2025-05-08 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cc07ad3-7340-3d9d-a22e-2e4160412528 | -11.62862 | -54.94283 | 2025-05-08 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3cf884b-5433-3b89-a063-449c240e9e7a | -13.49082 | -52.96978 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 911ddd55-f626-37be-8b1f-044ffebd3ef3 | -13.37482 | -54.25433 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcd84033-77aa-3d44-b66e-f5dbd31a2f29 | -11.26331 | -52.47473 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c69ebc3-819b-3d7f-ac53-dfec68fc01fa | -13.4974 | -52.96051 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26ebb6df-3ee2-30ee-b84d-049acb6a92e0 | -12.63998 | -54.06295 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa62109d-3931-336c-b9e1-fec5da357947 | -12.63885 | -54.06174 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70f3a7c0-7656-318d-92f5-1a363ce52329 | -11.25796 | -52.47393 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8a76e3e-7439-30fa-ab7a-ef4fb4c91821 | -11.39091 | -52.93702 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f4f9384e-f2a7-30bb-af77-672712da04c7 | -13.37411 | -54.25977 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3d8b642-c2a7-3082-94fc-fd8ba40f66f7 | -13.04736 | -53.7244 | 2025-05-08 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fec0b346-570f-3d82-9d5b-9592ebdbc60e | -11.39173 | -52.93706 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa6e343c-eec7-3ebc-af45-8b5ae3b41585 | -13.50725 | -52.96879 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fd028078-4bcc-3429-98a5-fabb94177c2d | -13.48549 | -60.37353 | 2025-05-08 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6930366f-bb1a-3f74-80de-8fb480511362 | -13.3734 | -54.26519 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 081d4cbc-80dd-3055-9b4b-e23c3d6f225c | -13.49165 | -52.96306 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a5e039a-c485-38ce-8aa1-f3b29eac5efe | -14.17966 | -60.03004 | 2025-05-08 05:25:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 819c4710-bc1e-371c-aa0c-846722ebae4b | -11.39055 | -52.94666 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a693d09e-3ecb-364d-98d4-aa46e52191af | -13.37571 | -54.26634 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6eedb36e-35eb-3131-b041-49a0cae1be1e | -11.39487 | -52.94726 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b277212-ef0d-3b5c-870e-96210a1d583d | -13.37216 | -54.25478 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd6f2f16-62d0-3310-9774-66695a139b0f | -11.39134 | -52.94026 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a8e8575-9634-3ea6-952b-089ad71e3831 | -11.39576 | -52.94734 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6df55218-a4f0-3f32-9977-6daa65762eb2 | -11.39049 | -52.9402 | 2025-05-08 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc6cb00a-1fe9-3d2d-bbbb-ac5ff6440629 | -13.37705 | -54.2555 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3377e517-22a5-36db-8b1c-c43a18958c6f | -13.49658 | -52.9672 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 692a8d46-fbac-375d-a1cb-a84d9e76737f | -13.48589 | -52.96567 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2891adbc-2bec-3d3b-8114-12efc8dded93 | -13.37149 | -54.26025 | 2025-05-08 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c859eb81-7605-36f0-a130-40e90386a43e | -13.5015 | -52.97137 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 63ecd14b-62fa-3240-83eb-5b4ce89a0fe9 | -13.04661 | -53.73038 | 2025-05-08 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0b436037-a2ce-3411-8d77-4b97c0a7d0c0 | -14.17906 | -60.0313 | 2025-05-08 05:25:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a22ac068-021f-3706-a63a-b94fe63d75aa | -13.50684 | -52.97215 | 2025-05-08 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ab9959e3-fea7-35b6-867e-2058ef4fa73a | -18.41745 | -54.70232 | 2025-05-08 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cef224e-c751-3616-b61e-6d1c7962bab4 | -18.42072 | -54.70278 | 2025-05-08 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a161b8e3-6f05-3535-87bd-6087e46ed8dd | -17.47295 | -53.82078 | 2025-05-08 05:27:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb58cf5d-359a-31a6-85bc-115d7a96f441 | -19.83965 | -54.22052 | 2025-05-08 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 899eafd7-1114-3248-9d0a-845a0c3027f4 | -21.04909 | -56.00037 | 2025-05-08 05:27:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a55ea03-859c-33b1-8533-a3783f33bf60 | -20.38681 | -55.39044 | 2025-05-08 05:27:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c5000a3-e8c1-3eba-875e-e91d4e08c5bb | -19.05836 | -53.45479 | 2025-05-08 05:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 569a835a-97f3-3d1c-ad46-3879cbf7d31f | -18.41531 | -54.70505 | 2025-05-08 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a5dcd5f-abdc-3c05-84cd-4b39192b60e6 | -19.84194 | -54.22043 | 2025-05-08 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc1a2f1c-4800-3499-97bf-a9a06d179dc6 | -18.42038 | -54.70589 | 2025-05-08 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6ec34ab-760d-3b0f-bd4e-d8fae817e417 | -20.56216 | -54.06807 | 2025-05-08 05:27:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1d31fc7-5e20-3cc9-866e-9af05104557c | -18.41238 | -54.70152 | 2025-05-08 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23215f48-d3d6-3696-834f-eaff9009f727 | -19.05281 | -53.45403 | 2025-05-08 05:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f0e642a-8019-3187-b1c0-30f7b28b70cf | -18.41202 | -54.70461 | 2025-05-08 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7b2414b-54da-3e14-b990-dc3d453243a4 | -21.89901 | -56.26897 | 2025-05-08 05:27:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0430e34d-e3fd-3531-b599-b1d1512e3d0a | -21.22989 | -56.24736 | 2025-05-08 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 596c2923-0151-3a79-b7bd-2aba8b81073f | -21.05453 | -55.9953 | 2025-05-08 05:27:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69b3dd33-b949-3be9-940f-c4a037a90290 | -20.56178 | -54.07185 | 2025-05-08 05:27:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27b69619-a81f-3079-a0b3-d778085d6feb | -18.41565 | -54.70195 | 2025-05-08 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5acd6e73-4ccf-333f-9611-903fc18314dd | -21.05391 | -56.00106 | 2025-05-08 05:27:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a6550a6-1a1b-34dd-a3c9-8f5329344d88 | -19.84231 | -54.21677 | 2025-05-08 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02abcc9b-24f6-3944-82fc-578075b794cd | -18.41673 | -54.70851 | 2025-05-08 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d09800f5-11fa-3a36-a28e-9292496b9c89 | -18.41709 | -54.70541 | 2025-05-08 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README6.md)
