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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16caaee8-d3ce-35bb-8464-0c7e97d900c3 | -15.4454 | -43.6429 | 2025-09-12 03:38:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6dd32f41-2d48-3c50-9360-b0ba6261d4fe | -14.18231 | -46.17154 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 619e78ac-c8c2-323d-8110-cbbe23d50d78 | -11.67861 | -46.54662 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0365bcec-7450-3605-8c3c-fb425395f569 | -10.35832 | -46.39159 | 2025-09-12 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05cbc8a9-575f-3825-be96-1344aff09889 | -10.69879 | -48.61737 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 08729f45-e33b-325d-8c4e-8c907bb5aa14 | -11.15763 | -45.31654 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b527016-0ac1-3e98-b3d0-7f86da3de23e | -14.12885 | -45.37945 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a10664d-1497-3299-8ca6-5e7906e0e448 | -11.6642 | -46.65079 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bdcb946b-d438-324d-8a5b-e165e26d5424 | -15.08508 | -48.00452 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e35553b-0299-3733-9fee-702e80428231 | -12.02453 | -43.78674 | 2025-09-12 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a5c05e9-2ce9-3f2d-8ce9-66f861e3ff6c | -15.69401 | -47.02424 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8f17b3a9-f683-32dc-b272-4509ef8d1c1a | -14.43602 | -48.41933 | 2025-09-12 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9fe432ae-5a90-323a-87b7-c8c028bfe9d5 | -9.66039 | -43.53229 | 2025-09-12 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42ae84bf-7eba-38a8-a59e-ba5c7fd7402c | -11.66227 | -46.66045 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3a1cd9ed-11c0-35f8-ba9d-183f1d394aaf | -12.8266 | -47.9604 | 2025-09-12 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef2aa48b-1aab-3778-9a76-6d8f45ed4baa | -9.85862 | -43.12728 | 2025-09-12 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 233f4afd-6b3e-34b2-8de2-5fb7345a2d6a | -8.50272 | -45.65599 | 2025-09-12 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5251fcb-4e9d-397a-96a2-8e07ee23b115 | -9.021 | -46.12379 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfe4efc2-901f-32b5-8330-43180c52ed05 | -12.00392 | -47.7642 | 2025-09-12 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 77500e92-4ce9-3f99-83a2-0c4e6d440e6b | -14.44023 | -48.4283 | 2025-09-12 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7c061cd-c156-3f51-a9c2-8fc6eecf9246 | -14.17753 | -46.20055 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f21d1a68-e87c-3458-962a-17e8cd144ba0 | -14.17757 | -46.17161 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e7d984b-e554-3be5-8188-13bb19b89dd2 | -13.35976 | -41.9214 | 2025-09-12 03:38:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 462b8b0c-1677-3796-b570-48e05a2d5702 | -11.86395 | -46.76308 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c3f60c21-a1c8-3548-bd27-03086384d8ed | -15.12441 | -48.6093 | 2025-09-12 03:38:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ae41f2e5-36f5-3a2b-8e11-27f2cac5b009 | -13.77954 | -46.28857 | 2025-09-12 03:38:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6a78db8-29e8-3c9b-93de-386c7bc63a7a | -9.68175 | -47.53835 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61234efd-8b71-33eb-a365-8642a98f1da5 | -11.2015 | -37.22808 | 2025-09-12 03:38:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 198b3534-5c28-3cdc-b299-4a961363ec0d | -9.06336 | -47.04175 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8d092db8-f6c3-395a-8e87-7ac8c4a03e4a | -14.18242 | -46.20083 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0997eee4-d123-376d-b7e5-e5f7d463e9fd | -13.24279 | -43.79514 | 2025-09-12 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc31b90a-da53-3ffd-8d0d-8b949b606afb | -14.18716 | -46.21171 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e596ba05-d91d-3eec-b333-0e95b4b2871e | -9.08195 | -46.95436 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e636f0a7-3fa9-368a-b7a8-dd019c6552dd | -11.14697 | -45.31031 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1880295f-6161-3f18-b4a4-b14bc6c2226d | -13.24669 | -43.77428 | 2025-09-12 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 996b2e22-c7d5-3606-918d-6a9ca74a270f | -9.03886 | -47.0965 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 2ca0eaab-dd64-3f7a-986c-23a37540aadd | -10.68185 | -48.66388 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1fc98cbd-1a05-3660-821a-6d27f522a527 | -11.43402 | -43.56345 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e002c3f-ff36-3e09-b7ff-9f35c6157935 | -9.44618 | -46.42125 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0223e88-3762-3484-9d31-92ee348091b0 | -13.90202 | -48.26495 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3b0a685d-ff66-3f6e-9102-e0d9ff5f3254 | -15.23041 | -44.04173 | 2025-09-12 03:38:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50ffe16f-60c9-378f-9790-291327436319 | -11.86496 | -46.75803 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2cfe652c-4845-3031-8fa5-8e67015dbb6c | -11.6766 | -46.55667 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7040dfe5-8c72-34a4-8077-327e428b20d3 | -11.93858 | -44.30243 | 2025-09-12 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e5ab4da1-19a0-3dcf-9707-cb61cff42eea | -11.7063 | -46.50314 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89cf2196-5600-31ef-990f-b528a4066926 | -14.17679 | -46.1991 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea6dfa16-c127-3637-9b82-4f27c43b47ea | -9.66099 | -43.52903 | 2025-09-12 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2fa1e68-b852-3e51-b897-bd50086e3911 | -9.05681 | -47.04037 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7a2b7833-702e-3820-88b9-e03ab1050665 | -11.67959 | -46.54166 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eae84618-0140-3dd7-a45e-49c6c7d2ec17 | -9.7263 | -43.5271 | 2025-09-12 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f879facd-d479-392f-be4f-c3bf17edf614 | -14.18313 | -46.16744 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8965794-f44e-35e6-ac13-6631d7aaf2cc | -9.77454 | -47.85378 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7bc498f1-9b13-30e9-98de-f5080f698a5c | -9.67504 | -47.53706 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0b34983-07de-336b-b7cd-01de1950ec50 | -12.4708 | -47.49533 | 2025-09-12 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fdb57524-3c0c-31f0-bd8d-c80735e4b6e0 | -14.14636 | -44.4491 | 2025-09-12 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55d84624-95b2-3a54-9e9b-299e6e4ad3d7 | -9.70469 | -48.30751 | 2025-09-12 03:38:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a175f267-0f18-3798-9f4c-ef502c4b39be | -14.12105 | -44.32045 | 2025-09-12 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89238422-ed6c-337b-a575-1c92fb371f0f | -9.07252 | -46.96072 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 95cf495b-5d32-38d8-8a66-e4c8aab8d9ca | -14.12877 | -45.37572 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28a83e2e-52c4-3356-b35b-db40d6b53b8c | -15.10483 | -48.00423 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 62c447a1-19da-3e17-b22e-54b0777c6614 | -15.11661 | -48.61385 | 2025-09-12 03:38:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6a4ff64c-0544-38eb-961e-9458540c59bb | -11.93721 | -44.30278 | 2025-09-12 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17a4c9b2-18db-33a2-95f8-cf023b00115b | -11.49818 | -43.64288 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00106c21-5187-3d38-af00-386a05f83587 | -14.17674 | -46.20435 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce111ff8-3fdb-3762-bb47-bf653fd6ca5a | -14.47745 | -46.35016 | 2025-09-12 03:38:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4000e0e-f209-3a40-aa8e-c226307a355c | -9.1103 | -47.11668 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee6b83c8-3e35-3703-a74c-505b7d59d366 | -13.9155 | -48.2336 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 263682b3-6a2b-31fb-9439-246cb3191b73 | -13.33959 | -40.34324 | 2025-09-12 03:38:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5ecd8d53-3d08-36a9-bc1f-af3c7e04399e | -10.71248 | -48.62174 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4f4f916b-6921-3e4d-9326-d557170ca378 | -11.65612 | -46.65917 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e3828a84-68ac-340b-a4aa-00fe6d6da529 | -14.42986 | -46.40731 | 2025-09-12 03:38:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f700add-1244-3aaf-b493-540f62fe51f5 | -9.03539 | -47.11398 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 60d37f7c-b319-3fe2-b3a2-49f6e7503c1f | -9.0456 | -47.07381 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bdb2ad3e-aa7c-3a8d-bb17-b39b09dc50d9 | -14.1672 | -46.19279 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88f450b7-9c27-3fda-bb9b-0c1f03f8667e | -15.0793 | -48.01481 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cb49222b-f6d0-3f67-abee-62f1498054f8 | -9.07351 | -46.95573 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| eae4002b-ca71-3082-81fe-729d2ba11091 | -15.67674 | -40.9881 | 2025-09-12 03:38:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 72d64263-ec6b-3e0a-9658-98f7885bfd3d | -11.67965 | -46.66965 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 60d1e672-0d6b-3532-aa0c-4f2191e1ea1b | -11.15351 | -45.30717 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b31b0ecd-58ec-3f88-b726-52869534736f | -15.24748 | -44.04253 | 2025-09-12 03:38:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 22b3a814-10c2-30d8-851f-27721643a539 | -14.16643 | -46.19127 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1915d9a1-4106-3979-a00d-0edb17c44c4d | -14.12414 | -45.37473 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0db60742-0b20-3545-8ddc-f539ce04a5ab | -9.81079 | -47.81411 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 639904ce-9686-3ca6-8b86-f16c2744c37a | -14.12334 | -45.37455 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76b3337c-59d4-3fc6-9f70-87a6bfde934a | -15.69579 | -47.01582 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| db42fa2b-f7ad-31e7-9c6e-b56f2f3f0042 | -9.01412 | -45.73314 | 2025-09-12 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f371cd0a-b092-33dc-a0e7-6359083c5404 | -13.90961 | -48.26126 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 55bd3af5-3567-3786-9ef3-48a292b25fc8 | -9.0596 | -47.03617 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 70f256ae-d3dd-3fc0-8d60-a63bdb8c17c0 | -13.24725 | -43.77133 | 2025-09-12 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad3374ac-0813-35d5-be60-3f1bf9e9272e | -9.05848 | -47.04207 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fa8fc192-deca-364f-b3c1-65ff71878c2c | -9.03657 | -47.08529 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9bbb33c7-02f2-3c62-949d-1db04b3494cd | -15.10786 | -48.00443 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 68ae496f-7d1a-3b4b-8f06-24d116e49828 | -9.03459 | -47.08346 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d0289233-a383-3cad-8886-06652a4ae2b9 | -13.24273 | -43.79482 | 2025-09-12 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd75d1ff-2c02-3369-91e3-469a9498dabd | -10.84906 | -48.16365 | 2025-09-12 03:38:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0162dd6a-adf0-3978-9f64-48f67e3ca750 | -14.1815 | -46.21022 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f806bda-ee39-3635-b3a0-1febe85cfc81 | -11.43076 | -43.56463 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8149107c-fccd-37e7-941f-1ee2a8a184e1 | -13.36403 | -41.92102 | 2025-09-12 03:38:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9fa78dae-499d-35dd-ae9e-c13520506e10 | -15.08058 | -48.00899 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2feacb2b-a96b-34d1-a6ce-1d33ff87bf84 | -12.90688 | -43.57478 | 2025-09-12 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README21.md)
