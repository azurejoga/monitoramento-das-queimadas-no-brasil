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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50d4cb12-811d-36b1-a29b-a964b1cdc744 | -7.86631 | -61.17378 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae2ceb12-c219-3d5e-8b87-c57c7c6698ea | -7.43407 | -44.85539 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68e90993-9025-3177-b60d-be63a356d723 | -7.3279 | -44.59988 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adf6d72d-9768-3b47-a0d4-5b9c133ef380 | -9.97047 | -50.30256 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 34f8b15c-5120-300e-b9b9-1f6bfc580b22 | -9.81005 | -48.89734 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3c02552-9c89-3463-b968-d86805f703a9 | -6.56385 | -50.87002 | 2025-09-13 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4997072a-5343-3031-b0c3-1082b8d7e10c | -3.22232 | -47.63724 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 54a8b1e8-8c8a-34ca-a753-5d390dc7f0f0 | -6.10706 | -45.943 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6348ea9a-a8e1-305e-be4b-a4fcd65c8e55 | -7.97144 | -55.30761 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61d61e35-d2ee-3396-86b8-d8126a572a7e | -10.34229 | -48.81157 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1b709030-7bbd-39a6-b06c-fe9adcef53a8 | -9.96054 | -51.70584 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ea0ae0a-ce90-3f75-98be-30dd60446485 | -9.26023 | -51.24619 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1e1f7e2-4776-32ab-a30f-f14f8d4a1ae8 | -5.94399 | -42.77393 | 2025-09-13 04:57:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0f0226a2-3612-380c-abf4-91f5ff7a2209 | -8.09582 | -50.18098 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19546be2-1d79-32b9-ae2a-7a58fd9c0cd4 | -9.9646 | -50.40144 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e4a8bc4-3a0c-3d9c-88c0-d5b9ec89adb2 | -3.21866 | -47.6324 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b805cdad-8bb4-37ae-9bd1-25e95a9ebc4c | -6.83497 | -47.86148 | 2025-09-13 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5540e6c8-3d07-3543-8793-1875170a7c18 | -6.90955 | -49.41373 | 2025-09-13 04:57:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f4675f0-77f0-379a-96a6-fbe9f5a28575 | -6.46724 | -46.03548 | 2025-09-13 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72b7446c-6f21-3dc6-a10a-0d7086d36f2a | -8.30743 | -44.8809 | 2025-09-13 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67ac29d7-4b9d-3098-90c5-8bd2d885029f | -3.79713 | -48.63943 | 2025-09-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9327be31-e2c5-3732-b549-3d466cd72e08 | -10.15214 | -47.90173 | 2025-09-13 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1cef0a15-0060-3961-86d1-f7fe69aee97d | -6.46803 | -46.0298 | 2025-09-13 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8b70477-3386-3031-a8f9-5fd56be0e276 | -9.8874 | -51.87085 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bad5899-ff72-328d-a1b3-cf52fc79d77d | -9.97192 | -50.2922 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| eecc9685-1354-3c13-9bad-d2bee2f22df6 | -9.90592 | -51.89548 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7c0f7f84-8928-3ac8-a6a0-0cdde04b5f99 | -7.31705 | -43.92764 | 2025-09-13 04:57:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89ccb5d4-82ff-35d8-9d79-2a5e6ea7252f | -10.32632 | -48.82891 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| afa75fdf-ca57-341f-9b6c-2610079d7081 | -7.31288 | -46.58716 | 2025-09-13 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4df2fe8d-84cb-30a2-9024-4d10088ffbb8 | -3.51904 | -47.21877 | 2025-09-13 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3df70933-181b-3c7b-a721-fbfbb0496e12 | -7.86263 | -61.16867 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a587094c-5899-3a5b-b61e-9ce067f5b61c | -9.19748 | -45.77811 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c792fb5-c41e-30f0-9064-6e7f65f71809 | -9.05763 | -45.82372 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc210e04-9ba2-3b12-b99c-d126257ba420 | -3.7936 | -48.63524 | 2025-09-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5e29ed6-4dbd-39eb-b1c1-a9f79216f794 | -9.79148 | -48.90377 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80fd93c6-c6a8-3774-992c-4af83a94f635 | -5.95576 | -42.78037 | 2025-09-13 04:57:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 51cbf1de-21b1-3e5c-bae4-8e49c38884cd | -6.11211 | -45.94367 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b45e6f8-ee7c-3932-99a2-e304c5177b58 | -8.87737 | -49.93684 | 2025-09-13 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 582f30c3-89de-34fb-bcff-5102de4e762d | -4.93154 | -55.78728 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf37c936-4d9a-38a6-a79b-1839a37929b2 | -9.49684 | -50.89008 | 2025-09-13 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 622e5fef-e5ce-3806-8dcb-2f5e133d3b7e | -6.47226 | -46.03636 | 2025-09-13 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec3f6e93-47af-3355-a807-eaf3801e82d3 | -10.1216 | -45.50234 | 2025-09-13 04:57:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0a2226e0-bd61-397d-af21-eea07535b58f | -7.45531 | -44.44552 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7b634cf-3d3d-3e5f-b14e-665667312e33 | -6.47266 | -46.0335 | 2025-09-13 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f3f5de9-bbef-3d6b-ac33-2a3afbd738f7 | -10.01394 | -50.38918 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cd4c4ad-7466-3873-8f2a-96e7d6e8d37a | -8.92468 | -46.14434 | 2025-09-13 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c8ad4e0-80d0-3c8b-ac78-0302128d1cf6 | -3.51093 | -50.38201 | 2025-09-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01343614-c387-3657-b4f0-01fe0844628f | -8.08779 | -52.35841 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39edce06-491a-31b6-9a80-b402f34ba99a | -9.23584 | -51.2174 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 36e201a6-c49d-3bab-93b2-6135b70d94ba | -10.23374 | -48.62055 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aeb9ea93-a2ae-3c69-9c90-fb493c4a7b14 | -9.96795 | -50.29162 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e9306a81-c125-3fce-b748-3d37576f787d | -8.09907 | -50.18593 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 219aa6d8-a2c0-3001-a387-e57dfa314238 | -8.50474 | -47.31688 | 2025-09-13 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46bbaa56-7727-3979-b816-cd54e88941ca | -9.96784 | -51.707 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3a2be93-6d7c-3de3-b422-7d3201c8db30 | -9.97453 | -51.71234 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d24c438-020a-34ff-9f4a-c3fcef880cea | -6.90605 | -49.40961 | 2025-09-13 04:57:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbf057c6-99f1-3614-a828-b76b7e4bd1dd | -9.24368 | -51.24143 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6233d1f3-9fad-391b-a97a-e19c0cd39beb | -7.31781 | -46.58773 | 2025-09-13 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0c561bd4-83ac-32f4-97bc-cd9f69325e90 | -3.90866 | -59.65096 | 2025-09-13 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d24e83e1-8abb-3617-9782-94776a19539c | -9.00414 | -45.78593 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e56adfed-11e0-3697-909c-e37a4e58e216 | -9.23733 | -51.25862 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f60d7e5e-b71e-31e5-926f-75cb60a3548c | -7.01818 | -44.88882 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07a5719f-4a0b-3eee-bc08-39c111365fae | -6.31865 | -43.33721 | 2025-09-13 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba4f0af5-9266-37aa-a412-7c4e3382f5ed | -8.42332 | -55.63516 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44b82222-476d-3d2b-8a76-e22fe70e9ed6 | -8.92387 | -46.15055 | 2025-09-13 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3bcc9521-cf83-3afb-947e-a96d1dde8477 | -9.66951 | -47.55053 | 2025-09-13 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35b8663f-2d24-3c74-a9e5-15d2006e9403 | -9.80513 | -48.90095 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1f6b72a-99a8-354f-918b-49fe321beab5 | -3.66761 | -52.17312 | 2025-09-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fab6245-4453-3175-96d2-f5a30dcfd9e4 | -10.24084 | -48.63496 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bb9be7db-f319-3c16-8857-0355b47631f5 | -5.1149 | -46.07226 | 2025-09-13 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f9c2262-656f-31aa-934f-c8d5e0ee80f5 | -9.9712 | -50.29739 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a0e6d5d2-b43c-3ac8-9c78-42dab7691c81 | -9.51768 | -54.62632 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| bde2740c-9864-3b6d-b584-3b6b7ac6160d | -8.09974 | -50.18142 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8b38534-329f-31e5-8ef5-ab4795671f9d | -9.57483 | -53.60836 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7f88a43-c926-3c0e-ae34-73ab6c0adfb2 | -4.08362 | -48.04236 | 2025-09-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55c790b5-6ec7-3b26-9bf1-884ebd87ab07 | -3.67098 | -52.17364 | 2025-09-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15e541df-4705-36a4-8633-9635fa185f8c | -10.2453 | -48.63553 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 31509279-456f-3631-baa1-006676016d29 | -8.08736 | -50.18438 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77bfe84d-1c32-37cf-9952-cec25a2ea564 | -9.24348 | -51.25729 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| cad6ba2a-f931-3345-b123-ef240c0fe144 | -9.69621 | -47.53904 | 2025-09-13 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d54a7063-b0fe-361d-b4d2-034a9e4da429 | -6.83374 | -47.87031 | 2025-09-13 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0246564d-2c15-3db1-acf4-5f62b5c71e38 | -9.95692 | -51.67908 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ba50503-24bb-3407-8fd0-2740a26f2de0 | -14.22442 | -46.29013 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c4cb9091-006f-39df-a8d7-6d0c491f3b5f | -14.21377 | -46.23481 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6cfd494-bb5a-3677-beb8-7236272c5be1 | -9.26611 | -59.41968 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| d78d826b-8aed-32bc-8a02-31807431ae19 | -11.15869 | -57.18033 | 2025-09-13 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 455bd136-efbb-39c8-b024-96043eeb08cf | -11.15629 | -57.19522 | 2025-09-13 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ceab69a-ed4c-30a4-ba82-7b48f6d6aa13 | -9.81227 | -61.51628 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e45cdf80-e32b-3dad-916b-4476fc422bce | -14.72346 | -55.63689 | 2025-09-13 04:59:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db37e56c-513b-3f31-8d03-35de604cb029 | -12.9572 | -54.74244 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34fe61f2-fc07-3bb3-a885-79e2e36f80c9 | -13.00486 | -46.74368 | 2025-09-13 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20bbf730-886e-31df-bffb-5a09f457ba22 | -15.11292 | -52.48706 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3fd2c0e4-959e-353b-b1a3-74369d2fa033 | -14.27911 | -46.05533 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbaccbf1-dff5-3b85-b1b5-0b95261f5202 | -14.71684 | -55.63581 | 2025-09-13 04:59:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08897301-c237-3363-915e-9bbabc6ccac3 | -10.50699 | -51.53975 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f9e8c7b-5e84-305c-a155-4f7da7b4314d | -15.59853 | -54.76603 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 319c6ded-f815-3a08-8019-d7d061be2fd2 | -11.12034 | -50.69979 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 01c43509-8258-3ff2-a228-5849cc3a14bc | -14.17188 | -46.25995 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b2ca8861-085d-37c6-9667-a1f8f96f990b | -14.27954 | -46.05153 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5571f502-840f-3f3a-834e-c2d85012eb20 | -15.59513 | -54.76556 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README79.md)
