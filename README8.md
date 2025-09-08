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
| b8b32380-432c-3780-85ae-907441fe330f | -12.9286 | -54.7949 | 2025-09-08 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0ad2708a-7e1a-3003-aa78-eb63d7c830c7 | -9.4344 | -61.8347 | 2025-09-08 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 59a246c6-c267-3038-ac30-2d7abc4a9511 | -9.481 | -60.4902 | 2025-09-08 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 0caae73b-ccd9-39b6-b051-ac7c235d8e34 | -7.3983 | -61.6346 | 2025-09-08 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 243.5 |
| 3a40f805-def3-3894-9554-8193bb702317 | -17.5022 | -39.9394 | 2025-09-08 00:30:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 157.8 |
| bd411351-18f0-3ec9-92c3-ed1966a4c778 | -6.6384 | -53.3566 | 2025-09-08 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 0fb9f426-3559-310c-adfd-e01a18cc60cd | -17.503 | -39.9133 | 2025-09-08 00:30:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| 59978624-0f5e-32f1-aa87-59bfe34bbfc4 | -12.6153 | -56.9742 | 2025-09-08 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 432.8 |
| c36a57ae-6d60-343c-8678-bb02bfd50cb8 | -14.5067 | -48.8085 | 2025-09-08 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 62bbe17f-9323-39d3-8a13-0bfece430724 | -12.6151 | -56.9943 | 2025-09-08 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| aedc0f82-b624-3d2e-8d6a-13f2e9a792da | -8.8821 | -64.2238 | 2025-09-08 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| e2aa0469-e2f1-3c08-8c7e-986509e67077 | -6.6384 | -53.3566 | 2025-09-08 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| aeeb33eb-5e6e-3dc1-9adb-a44e48d816d5 | -6.8282 | -52.7938 | 2025-09-08 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 535756ce-7765-38a8-946e-34b4c52d2b95 | -3.316 | -48.7134 | 2025-09-08 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 05248c18-d562-36d0-81e5-f7cd6cee168b | -7.3983 | -61.6346 | 2025-09-08 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 247.7 |
| 41a5a2ce-319b-30e0-88aa-a3aa3396656b | -12.6346 | -56.9524 | 2025-09-08 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e7ac2fe7-fe59-3722-9a58-c142ba429e05 | -12.6341 | -56.9926 | 2025-09-08 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 9e6a8188-3d62-3790-b181-79f7ab9342d2 | -10.0495 | -59.3547 | 2025-09-08 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 6d972781-daae-36fb-9081-fcc1fb61abc3 | -11.2005 | -55.0195 | 2025-09-08 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 3759f18e-3d7c-37a0-be9a-d01fa7b4fd55 | -10.0493 | -59.3742 | 2025-09-08 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 23c5f331-b876-3759-88ce-0c0135bae404 | -11.2007 | -54.9992 | 2025-09-08 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 2098003f-0e93-36b7-a4ce-ee9f6e3c9264 | -12.9286 | -54.7949 | 2025-09-08 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 10158b56-a289-31f2-b214-3ee4cbc43ea4 | -7.3799 | -61.6353 | 2025-09-08 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 2137c439-be45-38ec-8cbf-f5a16d85ba98 | -12.6156 | -56.9541 | 2025-09-08 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 025f868f-e220-39f7-b184-7468ea31ca09 | -11.3748 | -50.3783 | 2025-09-08 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| c81b21af-cc78-3c27-b065-add389b585af | -7.3984 | -61.6156 | 2025-09-08 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| d0e767d5-2d44-38f2-812e-025e3605c0e3 | -12.9477 | -54.793 | 2025-09-08 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| b7f7ef0e-4888-3625-9e45-76221dac91be | -9.4624 | -60.4912 | 2025-09-08 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 725763b2-0655-3a4f-8ff3-6e40be2af992 | -6.4605 | -43.9532 | 2025-09-08 00:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 9e946c8c-1109-3843-b36e-fab1d32e15f3 | -14.7133 | -55.9169 | 2025-09-08 00:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| b912cbfa-349b-3bd1-b48d-08872afc2f8f | -6.6198 | -53.3576 | 2025-09-08 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0d655120-a16b-3162-ae53-a066c8bbfe7f | -9.453 | -61.8338 | 2025-09-08 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| ff56ec21-8d16-3c8e-bc2d-84bdb870a90e | -7.4168 | -61.6339 | 2025-09-08 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 9c1f95ec-7d22-3b76-8260-9ded5801f546 | -11.3745 | -50.3997 | 2025-09-08 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| c9e60919-2656-3670-8bce-f189bc8388ba | -11.2831 | -46.4591 | 2025-09-08 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b97baded-ab34-30eb-b6f0-62d4fb4e97a2 | -12.6343 | -56.9725 | 2025-09-08 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 371.2 |
| 2feec83d-fae0-3090-baf8-d1025c1fb082 | -6.6382 | -53.377 | 2025-09-08 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 729f1791-3d90-377e-9ce9-3c1410669d49 | -12.948 | -54.7724 | 2025-09-08 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 5987607e-5062-3e41-9264-a10d99084fce | -9.481 | -60.4902 | 2025-09-08 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 3bccbea0-302d-3a39-b088-888382b22864 | -11.3742 | -50.4212 | 2025-09-08 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 33fb87bf-339d-311d-b678-0914cd2f989d | -17.1564 | -44.4266 | 2025-09-08 00:40:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| e408cae0-d594-39ae-8c7a-eda77288beb4 | -10.8253 | -47.7455 | 2025-09-08 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 05aacb00-9527-3366-a5eb-7f0c1d225c2c | -12.9474 | -54.8135 | 2025-09-08 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 90acce54-18eb-37ce-8bd3-d2c6443cb9f0 | -9.4344 | -61.8347 | 2025-09-08 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d99e2008-0bae-3a72-9537-36e081a43ed0 | -10.0682 | -59.3536 | 2025-09-08 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 100ac4b4-0aeb-30de-be04-15cf51ba9b63 | -14.5266 | -48.7833 | 2025-09-08 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 5a95a4bc-3854-3c9e-ada7-369dbd65fd5a | -9.4531 | -61.8147 | 2025-09-08 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4669f342-0d2a-35a9-b4c5-c54f2d16117c | -9.4345 | -61.8156 | 2025-09-08 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a9e230af-247a-328d-b426-6ed5d8a7f449 | -14.5072 | -48.7863 | 2025-09-08 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 1bfdde2e-c95c-3be9-802b-bb4750656935 | -8.6219 | -40.2058 | 2025-09-08 00:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 90.5 |
| f5edda81-4447-37af-8c75-953d78c91f4a | -22.34851 | -51.92617 | 2025-09-08 00:48:00 | TERRA_M-M | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.8 |
| 802fbc69-45c0-3621-a411-6e5d2ea86fcb | -23.18753 | -47.24438 | 2025-09-08 00:48:00 | TERRA_M-M | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| e3fca68c-92af-368a-bcb1-d9eadb513bb9 | -22.32779 | -52.26453 | 2025-09-08 00:48:00 | TERRA_M-M | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 29af772a-7c63-3118-8078-ac9b3f2be9d4 | -23.18918 | -47.25513 | 2025-09-08 00:48:00 | TERRA_M-M | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 5674be2b-ec1c-311d-b2ee-2922fa4775d3 | -19.40022 | -44.50959 | 2025-09-08 00:48:00 | TERRA_M-M | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| cc64a484-d87e-3919-a6be-0cf160d07408 | -23.07076 | -50.40707 | 2025-09-08 00:48:00 | TERRA_M-M | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 34df83a5-3c36-34da-8af1-b5ca0997cacd | -19.47339 | -47.89758 | 2025-09-08 00:48:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7e264523-c2dc-3adf-81cc-883072f6ef08 | -22.33724 | -52.26304 | 2025-09-08 00:48:00 | TERRA_M-M | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 8908aa84-c6f5-3e08-9bb0-4f20e4e515ce | -19.77882 | -47.23102 | 2025-09-08 00:48:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0bfc8f89-b56a-3be1-8dd7-f568021124f5 | -22.34716 | -51.91546 | 2025-09-08 00:48:00 | TERRA_M-M | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 138b8d7e-86af-38d1-a487-cb037fbb9e90 | -22.32915 | -52.27552 | 2025-09-08 00:48:00 | TERRA_M-M | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.7 |
| 6e8108d3-1f77-3c84-8113-02ed826246a8 | -22.33862 | -52.27406 | 2025-09-08 00:48:00 | TERRA_M-M | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| 871c8ae9-eb13-33c1-856d-81ea88c66f8e | -20.92812 | -45.26543 | 2025-09-08 00:48:00 | TERRA_M-M | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| feb90bae-1430-3c13-a401-d21ef76ef617 | -9.453 | -61.8338 | 2025-09-08 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 9d04ef94-ba03-3298-8925-6c690480e4c6 | -8.6219 | -40.2058 | 2025-09-08 00:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 1bb3357d-80d7-3a26-a8f5-681ff04a83b4 | -13.6399 | -43.8018 | 2025-09-08 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| d45d04af-b0ea-38ec-9787-e24e44a85323 | -14.5067 | -48.8085 | 2025-09-08 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 202.4 |
| 0f1c70e6-597a-3e48-8cd1-e9bce3822603 | -7.3983 | -61.6346 | 2025-09-08 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 214.4 |
| 16a150e5-9bae-3ef2-be3a-d0176b141063 | -12.6156 | -56.9541 | 2025-09-08 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 522a3c6f-34e3-3b3b-bc6b-cf2a0159747c | -12.9477 | -54.793 | 2025-09-08 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| d6d8fae0-6417-3fb7-a172-98467e5e6afb | -12.6343 | -56.9725 | 2025-09-08 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 283.3 |
| 503a62da-607e-377c-913b-a6b72ba5d26b | -9.4344 | -61.8347 | 2025-09-08 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 40921b0d-4b84-351b-83a6-c3b3f187e442 | -11.2831 | -46.4591 | 2025-09-08 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 0d211db0-640d-3c89-869a-4a555bc58d53 | -10.0495 | -59.3547 | 2025-09-08 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 53fd059c-2af6-384c-b8bd-3e4d6a148167 | -12.9286 | -54.7949 | 2025-09-08 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7cc8a016-323c-31b3-b7ba-5a1ccb873069 | -12.6153 | -56.9742 | 2025-09-08 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 376.3 |
| b35b0f06-b1b5-3ec3-9a08-d8cdf8be7805 | -11.3742 | -50.4212 | 2025-09-08 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| d0c0b91e-7f26-35be-8939-497f46fdafd5 | -17.1564 | -44.4266 | 2025-09-08 00:50:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 86aef77f-0d80-3be4-b64f-b97a5aca28b5 | -12.6346 | -56.9524 | 2025-09-08 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b0814641-becc-34c5-a2ce-bd8e00560e6a | -12.9474 | -54.8135 | 2025-09-08 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| a5b7066d-941c-3535-a5da-c08009f72141 | -9.481 | -60.4902 | 2025-09-08 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 2cb7f43a-c16c-38d5-a944-c511d1efe316 | -11.2005 | -55.0195 | 2025-09-08 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| eaca8d07-0414-35e9-8566-cbdc3f920e1e | -14.5266 | -48.7833 | 2025-09-08 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 7c36673e-98eb-31e3-b831-926409be9eb9 | -12.6151 | -56.9943 | 2025-09-08 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 90befd42-c63e-3bf8-93c9-1292db306829 | -9.4345 | -61.8156 | 2025-09-08 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 76a92288-2bfb-3299-94d5-37e8c1f568c6 | -10.0493 | -59.3742 | 2025-09-08 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c89f0728-7f45-34c3-933e-e3b8c3d58c7b | -9.4624 | -60.4912 | 2025-09-08 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 873b2574-6fcd-3540-ba37-349b02a06681 | -11.3745 | -50.3997 | 2025-09-08 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b90e6fa2-11dd-337c-af61-49c00f2df89a | -11.2007 | -54.9992 | 2025-09-08 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 3f65a4e9-85c5-3c8d-b7e0-6d6362b0a8d0 | -7.3982 | -61.6536 | 2025-09-08 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| dafc7bc6-a707-36b3-9097-86ab3a1fc0a7 | -7.4168 | -61.6339 | 2025-09-08 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| ababe5c2-1634-3232-9f2f-0178886915ed | -7.3799 | -61.6353 | 2025-09-08 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0ffb590b-f650-3c98-8be3-852f1d88405d | -9.4531 | -61.8147 | 2025-09-08 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 2635f351-9745-3f0b-b0b9-51cf55a46aa6 | -6.6384 | -53.3566 | 2025-09-08 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| dae8df5e-d9e4-3b97-b0f2-ec488af0a229 | -12.948 | -54.7724 | 2025-09-08 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 295e8bd9-465b-3b0e-a18e-d4f11a99821f | -8.8821 | -64.2238 | 2025-09-08 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 624b1249-8666-3fa8-ac32-9ba8ebacc4c3 | -14.5072 | -48.7863 | 2025-09-08 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 9074874b-540d-3470-9f8b-2e9147e50a0b | -14.5262 | -48.8055 | 2025-09-08 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| efd8e80b-3ae6-3cf8-ac00-c57045af0405 | -7.3984 | -61.6156 | 2025-09-08 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 394be5c3-9493-363f-8404-49dea5b5da90 | -6.4605 | -43.9532 | 2025-09-08 00:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |


[Clique aqui para ver as próximas entradas](README9.md)
