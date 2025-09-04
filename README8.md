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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fc1736c-8e0e-3785-843e-827ebd24d35c | -15.5196 | -52.891701 | 2025-09-04 00:57:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d685bd9-a188-36cc-ab6b-8f5168af67d0 | -6.6984 | -63.136299 | 2025-09-04 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e17f2254-c9ef-3cd6-b9c7-590e86cdca7b | -12.8723 | -54.781399 | 2025-09-04 00:57:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af093c98-b250-3287-8685-a9c59a00837d | -7.6106 | -50.3391 | 2025-09-04 00:57:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dc1ad06-f52b-32fc-9153-ce8ad4a4a9c8 | -10.3625 | -50.364399 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33b35e10-57d3-333e-a143-d0cc5f9f573e | -7.6151 | -50.315899 | 2025-09-04 00:57:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65e7597c-eea1-33de-af5f-42db6f24f74d | -10.4303 | -57.782501 | 2025-09-04 00:57:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0992ba13-e5bf-3b2d-8c36-ff2efa526832 | -11.4889 | -52.141998 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5239320e-2636-38e8-b31f-ee40d656a35b | -10.3935 | -53.6576 | 2025-09-04 00:57:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9479913a-75eb-3019-846e-e0aa045d066c | -12.4025 | -53.852402 | 2025-09-04 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5605a91b-5ef7-3c3e-8f75-de002ec6d8cc | -12.8154 | -56.9352 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2b022ba-06b3-3632-8920-6c50355ba2e9 | -12.8171 | -56.942501 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 938a4a10-c0a8-3f79-ab26-6b894a7e7465 | -15.9013 | -55.990898 | 2025-09-04 00:57:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b33d37ba-bed0-3655-a3be-1103087dbfd3 | -5.8176 | -57.718601 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed65a6a6-7373-3372-ab9b-84a6ff397d91 | -6.6868 | -63.1301 | 2025-09-04 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2c9849f-5290-396e-bdee-82d53d56a49e | -14.9039 | -59.391602 | 2025-09-04 00:57:00 | METOP-B | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d2ba369-7a78-3449-9a7f-67b19282fec2 | -14.9394 | -50.051498 | 2025-09-04 00:57:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9e61bd2d-499b-370d-87e8-9266b93c2216 | -4.9024 | -56.25 | 2025-09-04 00:57:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c172235-16ae-3fbe-91f2-997236a07fc3 | -9.4097 | -57.827999 | 2025-09-04 00:57:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1871b0f-623a-322a-97cf-d3ab6d281397 | -5.7676 | -57.770302 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe292fb0-7406-3d53-afea-12eb0adaf0f6 | -6.6966 | -63.127998 | 2025-09-04 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb4e81cb-b509-3cfa-9318-596db2d0f635 | -11.7869 | -51.555599 | 2025-09-04 00:57:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8304452c-1029-3d42-8280-87d56e13147a | -10.3429 | -50.409 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d64e371-ba20-3204-9529-238e4a0732c3 | -10.3382 | -50.390499 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e60b4bf0-91e8-3a8f-83ac-112dc65f66f6 | -12.3918 | -48.062599 | 2025-09-04 00:57:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb436a38-215e-3d18-b763-8ff888a3c669 | -11.5347 | -52.2019 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6f80031-ff86-38ce-8f86-b7ac8a363058 | -17.0707 | -46.278801 | 2025-09-04 00:57:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d6e27ac6-bda8-3c4b-b1c9-47952366316e | -16.4627 | -55.111401 | 2025-09-04 00:57:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1c09260-986a-3a7a-9990-952318840de1 | -12.4366 | -53.822102 | 2025-09-04 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85d7fa04-7287-3b0e-94a4-f7a0cf9ce847 | -10.3578 | -50.345798 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df823dda-3ab1-3a77-bda4-88b859139e2b | -15.3253 | -55.954498 | 2025-09-04 00:57:00 | METOP-B | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6cffd6f7-3dda-3e07-b1bd-dc7762f79b20 | -11.5658 | -54.542301 | 2025-09-04 00:57:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1894189-4086-3cb1-8032-273f8ba4f2b5 | -6.685 | -63.121799 | 2025-09-04 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c338417-1b44-3e83-9707-89ebb3c53efe | -5.1847 | -55.956902 | 2025-09-04 00:57:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 746ed01a-7025-35e3-a4b6-410a599168fc | -10.4417 | -57.787498 | 2025-09-04 00:57:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f3bcbc1-9a68-3c41-a1a8-c96c3b5bf35b | -12.7992 | -56.954498 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2bc8b1e0-e294-3c23-a828-3792e9b090f3 | -12.5218 | -57.004398 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9bd3c36-ab11-3886-9f24-2a1fe5f638d4 | -12.824 | -57.018299 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf149d2f-1b6c-3491-a099-eb556945495b | -16.4491 | -55.097698 | 2025-09-04 00:57:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 69250e21-e090-3c11-ba59-6c9eec4a95b1 | -16.4645 | -55.1194 | 2025-09-04 00:57:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e76e449a-2c21-3486-8a1c-32f2b0710ee5 | -15.3235 | -55.946899 | 2025-09-04 00:57:00 | METOP-B | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9fcb06d-a5fc-3be2-ba71-e3fea447bbc6 | -22.060301 | -56.483002 | 2025-09-04 00:57:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0218a2a0-05c2-3f30-8d1c-467d01fdc1da | -11.5561 | -54.544701 | 2025-09-04 00:57:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 553df873-784f-34d2-9eaa-2cd050697718 | -5.8078 | -57.720798 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3eeec0ee-1683-38b3-99a1-0136150e02fd | -8.2536 | -48.343899 | 2025-09-04 00:57:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3d236ec-7423-3cf6-a41c-24dac0a60843 | -10.3479 | -50.388 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea14e68b-b72f-3e6f-b852-ba7084df178d | -12.8745 | -54.790401 | 2025-09-04 00:57:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c90de59-ca69-3a7f-a3d0-34029e692c64 | -11.4956 | -52.168999 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66217878-3f47-31a9-8646-b0434c3dcc47 | -14.9062 | -50.043098 | 2025-09-04 00:57:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0370f65c-69cb-31de-8777-e7d94cdaaf7f | -6.4769 | -51.1078 | 2025-09-04 00:57:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c3b389a-d857-34d5-80b5-432a1e5bb758 | -11.1133 | -55.028702 | 2025-09-04 00:57:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8b97fb-5df4-3176-95c8-23f057bff0c8 | -3.0239 | -59.436001 | 2025-09-04 00:57:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6052730e-6bfb-3c04-bcf2-f3def839b0f7 | -15.9096 | -49.285599 | 2025-09-04 00:57:00 | METOP-B | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e084eb13-029b-34b0-8980-8739f7d1585c | -13.6477 | -46.947899 | 2025-09-04 00:57:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 108fb1bf-4ea3-3221-8193-2e20fc6887c6 | -17.7537 | -51.539299 | 2025-09-04 00:57:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b8177a61-f241-3781-955d-1c71e02866ba | -22.061899 | -56.490398 | 2025-09-04 00:57:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0108e1da-0146-3510-9a5a-0d2caa56cb4d | -11.4952 | -52.1259 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4264c6-e0de-34d9-bdde-048f2ab6b3b4 | -15.5222 | -52.902302 | 2025-09-04 00:57:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f646803e-17e8-3cc0-a80a-a5e6cf485811 | -11.4855 | -52.128399 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80dde3cd-100d-3448-a417-1182dfb0b9f9 | -20.188 | -46.723801 | 2025-09-04 00:57:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eab43f1c-c352-384e-87a6-6f32f06e71ea | -11.7699 | -51.528702 | 2025-09-04 00:57:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac5517c3-7632-3eb6-9ea2-915bb3144be3 | -22.063499 | -56.497799 | 2025-09-04 00:57:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e3aab117-1c23-34de-9759-c53feef503c1 | -22.1373 | -55.981701 | 2025-09-04 00:57:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e71e0612-b87c-301c-9eda-93807c8b1c44 | -12.5545 | -57.012199 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d88c1135-ae2a-3509-ab12-571a1dc1e401 | -1.9922 | -56.6642 | 2025-09-04 00:57:00 | METOP-B | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8aa6984-39fc-3647-a4d3-0bc0816ec771 | -5.8148 | -57.751499 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6605e308-e0c5-3b3d-ae83-7fb6aa69bcda | -11.761 | -51.452099 | 2025-09-04 00:57:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63a354f8-0716-3b3f-8763-08602ec6fdd6 | -6.008 | -57.7397 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 382e6195-8231-366a-bf67-141b534a6f0c | -18.0487 | -51.807301 | 2025-09-04 00:57:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d37c81b0-0430-313a-b701-1e72bf792031 | -10.4401 | -57.7803 | 2025-09-04 00:57:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb590a34-bddd-3e5d-8510-6674c1a7408a | -16.4212 | -51.887901 | 2025-09-04 00:57:00 | METOP-B | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1b9978d-f96d-3d36-b937-fe75ad780bd4 | -12.8207 | -57.003601 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79cf1354-2a55-317c-aba0-28587e1922b2 | -10.3528 | -50.366901 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5647093c-9382-3d46-a894-0cc6e5eb098c | -11.4919 | -52.112301 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4046aae-5ec1-3b2b-b9dd-44a9917f3062 | -15.2122 | -52.777 | 2025-09-04 00:57:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c446365-f49b-35eb-a491-aba09724bf2d | -5.8309 | -57.731602 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36cd2b49-d074-3be3-9447-2aec7ba27a8a | -9.0296 | -61.486698 | 2025-09-04 00:57:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc56d960-b2ad-3d83-b75d-0ac4cd57fec2 | -12.88 | -54.77 | 2025-09-04 00:57:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d2c47c6-e7b5-30d3-a4de-0481486566c2 | -11.5445 | -52.199501 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7fe25ae4-59b1-3bcc-a331-56f750f4c126 | -16.2206 | -52.964802 | 2025-09-04 00:57:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8b46bb99-658e-3cef-9121-610457ee4869 | -2.8561 | -49.364899 | 2025-09-04 00:57:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fdd6457-8d15-3cba-b778-8d66a1f5beaa | -5.8228 | -57.7416 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c76f3994-54b6-3e12-a807-a02a35123148 | -17.061199 | -46.2817 | 2025-09-04 00:57:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b56007d-f04a-3d32-984b-b85cc59a0d2a | -5.8113 | -57.736099 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aab3dc79-e1b2-3bde-9cab-878207821ad4 | -5.8193 | -57.7262 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c455f811-92bc-3509-867f-6d82de2e1939 | -5.8015 | -57.7383 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a85b22c9-6966-3e73-a21d-4893f413441b | -10.3575 | -50.385502 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c644f9e7-b3ac-3562-8a96-62fa25d66fad | -10.5139 | -55.420101 | 2025-09-04 00:57:00 | METOP-B | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca236a65-1db1-3f41-8af0-ee8d41f1b4c2 | -13.0122 | -57.120201 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3707b23-3412-3fb2-a54d-099a7391e7b3 | -5.908 | -57.7311 | 2025-09-04 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 42ae7b5b-8814-3be6-8cd0-46ad30941b4b | -6.0923 | -57.7238 | 2025-09-04 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| f52ea256-6b45-3172-85e6-88bb325435af | -5.9264 | -57.7303 | 2025-09-04 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 5b5d3976-1a8e-3710-858c-ebe1a148ebdb | -5.6079 | -45.0265 | 2025-09-04 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 321.9 |
| 4bf1b095-c8b5-3b00-a355-c62ae34e729b | -11.0568 | -45.146 | 2025-09-04 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 304.5 |
| ca3d8756-aaf1-3493-a024-593128489f6e | -6.7832 | -63.1474 | 2025-09-04 01:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 2527af94-388f-3508-99ce-bae4e1a8ada8 | -11.0572 | -45.123 | 2025-09-04 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| dbe1a433-aa6b-37bf-81d4-2ec0ce3435ae | -11.6599 | -54.5297 | 2025-09-04 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 83ee22bd-792c-3b9a-acf7-4bf3ee5cca7b | -12.8816 | -56.9505 | 2025-09-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| c6015c96-34bd-3d48-8ec2-04ef990aa9ec | -11.0377 | -45.1487 | 2025-09-04 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 73efc159-6a25-3123-9115-2f8a83d7a711 | -6.7833 | -63.1286 | 2025-09-04 01:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |


[Clique aqui para ver as próximas entradas](README9.md)
