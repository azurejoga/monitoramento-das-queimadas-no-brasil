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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39acfa0a-7ea6-3ca1-9c97-1a2df7c9fd0c | -15.7198 | -53.56245 | 2025-09-06 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 79a51875-a7bf-313b-8cbe-ea33d112317b | -9.70865 | -49.51358 | 2025-09-06 01:09:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| c865763e-9fd3-390e-8475-ef727448fc47 | -12.52138 | -53.8545 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0c6a4738-ce5a-3630-8719-85f0afac1050 | -14.83701 | -48.20045 | 2025-09-06 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| fcd91755-8937-3bf1-9da0-dcdf9d476c32 | -12.97417 | -54.81889 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9b279943-9764-37c9-b97c-ac6a553c5add | -15.72145 | -53.57328 | 2025-09-06 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| e29dcf2f-b748-3eea-b2d0-ae384cb586c6 | -11.20811 | -55.03176 | 2025-09-06 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 910955d1-d3ac-32ba-9ac3-ab2165801448 | -14.26625 | -52.18842 | 2025-09-06 01:09:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4847e0b2-6da5-3517-8281-e81b195005db | -15.43351 | -52.97771 | 2025-09-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6743fcb0-573c-3e47-9777-45976fd8f36b | -15.06467 | -48.1115 | 2025-09-06 01:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 28.8 |
| ed2cff5b-e134-3f82-905f-c1db0c7c6d57 | -12.50351 | -53.86877 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 9e6cbc73-733f-3091-b139-8cf704c65545 | -9.80461 | -54.88932 | 2025-09-06 01:09:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fe951530-2156-323d-b79e-2cefdc922c17 | -10.44758 | -53.61281 | 2025-09-06 01:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 31f197f1-ae74-355c-9e9b-c68833a0ca53 | -9.46693 | -60.51263 | 2025-09-06 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 330f7281-0e0c-3bf0-8691-c986be9af487 | -7.34065 | -48.51033 | 2025-09-06 01:09:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 9412105b-0883-37f7-9c03-308b7e0d28b2 | -12.95428 | -54.81189 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 30dfe312-6471-3282-aec0-bc80eda67faf | -15.73426 | -53.59342 | 2025-09-06 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 07fd0946-1f82-3f50-b51f-167f921cb9dc | -12.95282 | -54.80202 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d56f2659-7110-3a95-a922-fadc5a1ab8f4 | -12.51327 | -53.86724 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 9ff482b7-4f51-35ec-94c2-16d3bd711423 | -9.21585 | -57.09652 | 2025-09-06 01:09:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eb128860-4954-3b77-a008-863580ec34ed | -12.51162 | -53.85607 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 24f5cfed-79e9-325b-bc6a-7b086b0c3ce9 | -15.72309 | -53.584 | 2025-09-06 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 418db758-41f9-31f3-ac92-a8fcd4fd8ad1 | -9.33283 | -55.21346 | 2025-09-06 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ece7708e-4f24-3c0d-82d5-a0358e5ce28b | -12.95573 | -54.82173 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9d43e372-3425-3508-b1ef-fa67719d8378 | -12.98577 | -56.90761 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1c3b107c-71c8-359b-966e-371d165a883e | -8.36739 | -52.5676 | 2025-09-06 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 575c7067-c570-3284-bd41-a9dd2d8a2b34 | -13.8113 | -56.5556 | 2025-09-06 01:09:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08bd9842-51c4-380f-a8f2-570ef76d9657 | -14.33753 | -60.33075 | 2025-09-06 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 4647458d-899f-3984-8a81-3b6093d3d249 | -15.19685 | -52.37549 | 2025-09-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| a1ba6918-b782-3215-8050-99b98760254c | -16.33234 | -52.95449 | 2025-09-06 01:09:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 4b4b802a-65c0-3b1e-99f5-30707678f4a8 | -12.97562 | -54.82875 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f036b6cc-1093-3049-839d-e3f0ce5fca26 | -9.39589 | -54.74899 | 2025-09-06 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 69299967-43e9-36fe-908f-12204a217570 | -12.95912 | -54.78077 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 705f509f-eb58-3e18-8909-ed4d6cc19a56 | -11.55161 | -47.32324 | 2025-09-06 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| c0373f2d-0a69-3b3a-97ad-5bafc5ce30f0 | -14.90215 | -49.45957 | 2025-09-06 01:09:00 | TERRA_M-M | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 16997cff-7869-3a19-84eb-be7967368725 | -12.42665 | -52.14672 | 2025-09-06 01:09:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0f69bca5-652c-3a1c-8bcb-d535ca61d124 | -13.01248 | -54.82305 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4a382757-5a2d-35c7-8036-597534377dfd | -9.24869 | -57.07357 | 2025-09-06 01:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 794f001e-9194-3a14-a85c-e46ad0e493a2 | -9.99617 | -60.01923 | 2025-09-06 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 9eb8224b-3e5f-319f-aad2-a4d6b2039ba4 | -12.96205 | -54.80062 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e3d89b96-f003-35a4-aff3-0e4d0521f2bb | -12.9635 | -54.81047 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| b1c72d93-8adb-3e2d-b4a1-0eb94c1ea9b1 | -12.00482 | -47.77678 | 2025-09-06 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 7b08abe4-de62-328a-b064-47fe39a47596 | -13.01535 | -54.84282 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 32251b1d-ffa7-3594-b912-80ddd34b1cbf | -10.46692 | -53.61661 | 2025-09-06 01:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| faac2e2f-f768-36fe-8c3f-666098123afc | -15.21548 | -52.35892 | 2025-09-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b8aa4654-4206-3eda-88b4-4a11ad36a08e | -15.76288 | -53.65417 | 2025-09-06 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 576c54b9-3aae-333a-bea1-895441af3ac9 | -10.05602 | -58.38581 | 2025-09-06 01:09:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f878e25-ecb8-356f-9fe7-60947ca056c9 | -15.70993 | -53.59262 | 2025-09-06 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4701972c-b6db-3e05-b953-6a2db931fef4 | -11.54514 | -47.3317 | 2025-09-06 01:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 21cb4942-6a0c-3818-9b2a-0b985620293a | -15.73097 | -53.57182 | 2025-09-06 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 9c768963-45f0-3ca5-b8c6-a729c931d917 | -15.54336 | -49.82341 | 2025-09-06 01:09:00 | TERRA_M-M | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| b846abe2-28f4-30d6-b098-70c2704738ad | -12.47896 | -53.83829 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ea6f5423-389c-3c37-bac7-9fb6a9d67865 | -16.31192 | -58.11244 | 2025-09-06 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3d2b4b67-2cb9-364d-addd-8012c2893dcb | -9.70669 | -49.48062 | 2025-09-06 01:09:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 275.6 |
| 4689466c-0ac6-3dcb-8e94-cec0d1675002 | -13.00327 | -54.8245 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 62514100-d2cb-35cd-8e86-2ec5b63306cb | -10.18286 | -56.83978 | 2025-09-06 01:09:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 37603176-fecc-3733-925d-89161e1c86a2 | -13.0047 | -54.83437 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c8557e31-b1bb-35af-9c4e-0ed0466884cb | -15.22579 | -52.357 | 2025-09-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 71c61fca-e765-325b-9582-43008d3ee2f4 | -13.00038 | -54.80469 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c1f055e6-5835-38b8-bde4-6f1467978db2 | -9.33134 | -55.20332 | 2025-09-06 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9544903b-78d7-3fea-b1f5-d0c2ff1be57c | -12.49374 | -53.87028 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 34.7 |
| b8d9c6d1-2435-3f6e-9702-224a8866b193 | -10.46881 | -53.62889 | 2025-09-06 01:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c0657422-6d5a-38c2-8457-9e10c91b7a7a | -15.18019 | -52.40426 | 2025-09-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f18f4ad6-271c-3ba4-a368-2411cfced842 | -11.64318 | -54.55154 | 2025-09-06 01:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a9e05358-6ea8-376d-a7da-1f6ca5176988 | -15.45852 | -47.13606 | 2025-09-06 01:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 3f720f97-989d-3eaf-a3d8-9d1f3864ad62 | -13.08857 | -57.11653 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c8e8a373-18f4-37cb-b1da-02abdb20098b | -16.32079 | -52.94449 | 2025-09-06 01:09:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c403b437-c4fb-3b25-ae73-053bf499f16b | -11.47543 | -55.54574 | 2025-09-06 01:09:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 33bf42b2-05ce-3b9e-8c31-7a578972df1d | -7.32773 | -48.48474 | 2025-09-06 01:09:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| dbb38f98-ec09-3ee4-ad32-14308c5093e4 | -12.49041 | -53.84795 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a1b789dc-7851-34f5-a408-312716cf14e6 | -13.81255 | -56.56463 | 2025-09-06 01:09:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a005d03e-d7ac-3dfa-9cd1-1828e59bb4ea | -12.51807 | -53.83204 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 5b37a18c-19f0-335a-aa7b-b27cc42d5b3f | -15.86911 | -56.05091 | 2025-09-06 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 26ac6fa8-1a1a-3329-ac75-239ffaa04741 | -12.48564 | -53.8829 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 476a0c4c-30d2-371f-b964-0570c854b910 | -15.73263 | -53.58272 | 2025-09-06 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8281787a-e7d3-3c12-813a-a7ff50a01e57 | -12.88239 | -56.9562 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f8dfdba-df3f-38e3-8a86-ff45b875fa11 | -13.01677 | -54.85264 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ed2314a8-ee9f-3e7d-bd31-4691d127c6e8 | -9.70017 | -57.80084 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 482100fa-a3a4-3ff4-a2e1-26bd63a270ed | -15.19887 | -52.38837 | 2025-09-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6e323d52-e165-3294-909c-4557874d3b37 | -9.68426 | -51.09521 | 2025-09-06 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 360bda40-8ad4-3145-8a9a-7fc3b7795ff1 | -15.06665 | -48.10565 | 2025-09-06 01:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 9e4544a2-84ef-342c-b62f-982b817e7290 | -13.00613 | -54.84421 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| a0362aaf-b5a3-3b22-8931-ba86f244a401 | -14.90364 | -55.08564 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 795d0618-d172-37e3-bfd9-b24325ea78a6 | -8.65242 | -54.84415 | 2025-09-06 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3f6edcf3-b9f8-3695-9963-8df384b2a03d | -8.05365 | -52.37988 | 2025-09-06 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 5049b98f-8c88-3358-9930-65dab22bd3f3 | -10.13605 | -55.16031 | 2025-09-06 01:09:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 2ce736a7-91c2-3dc7-9837-2747e259ac96 | -10.14539 | -55.15889 | 2025-09-06 01:09:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| daacc746-c6c0-3f3a-a548-ee2fd0d532bd | -12.50996 | -53.84488 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d8f1cea2-3658-363a-98d2-4ec0c5293f41 | -12.52091 | -53.83716 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| f4a75842-c543-3d9f-b01a-72d6dfc8349b | -15.72933 | -53.561 | 2025-09-06 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f67cb15d-5a7d-3260-b746-db0246958af2 | -14.54751 | -53.14502 | 2025-09-06 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ef3fb398-e6ae-3034-857a-7b6d3fa7a3ff | -15.84992 | -52.2856 | 2025-09-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 5ad054bb-8461-35df-86c5-0e0a7955be07 | -9.70446 | -49.4876 | 2025-09-06 01:09:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 345.3 |
| a4382183-616d-3301-a44a-7867beda0e7e | -8.36801 | -52.55839 | 2025-09-06 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 61139dd9-5b0d-3d7d-9c05-55bc20235473 | -12.88115 | -56.9472 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e2ffdbe-4d70-3dd4-8583-96914a96fa81 | -11.48442 | -55.54833 | 2025-09-06 01:09:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 67b61be7-dd07-319d-83d3-9e54e55f9575 | -12.48398 | -53.87177 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| b66ca025-dcd5-3f66-9e21-441b41497b85 | -14.57211 | -48.01479 | 2025-09-06 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 03482630-5aa9-39ef-bee4-d4c6ff6897e9 | -7.33321 | -48.51875 | 2025-09-06 01:09:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 94cd9712-aa12-3a1f-a573-68197564ea65 | -9.2146 | -57.08762 | 2025-09-06 01:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README15.md)
