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
| 5ac80b4f-a814-38ae-92ff-3c6f1f6f04a6 | -14.88041 | -48.36578 | 2025-07-03 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93207a0d-357c-3556-b228-dfe6efb1e23f | -12.68067 | -45.03885 | 2025-07-03 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb5f7336-7ed5-3161-8f33-00a7de56e66d | -13.75066 | -49.55557 | 2025-07-03 04:36:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2852310b-7e09-3eed-8f27-c50c08236b08 | -10.88337 | -56.45152 | 2025-07-03 04:36:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68a7398c-aea7-3ced-a2de-44b9a3948b6b | -13.40676 | -47.80835 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d026309d-d6ed-35d1-ae3f-0f722ac9f2d3 | -11.32746 | -55.21429 | 2025-07-03 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1601946c-b146-3a38-a3e5-8962e209975c | -13.43331 | -47.81553 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6722d7f0-4341-3a83-b4c6-816d5a8b47fd | -14.63838 | -53.88404 | 2025-07-03 04:36:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12d55bd4-8c0c-3344-9cd5-91acfcb4c83b | -12.43333 | -50.02443 | 2025-07-03 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc835273-a7e4-35ce-8584-93bb1ed07aff | -13.39147 | -47.84011 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6917042f-c869-3a59-b3a4-1681e819afc6 | -12.03667 | -48.75189 | 2025-07-03 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cbd8abf-9167-3d60-a5fe-9b7e7c61a547 | -10.88765 | -56.45368 | 2025-07-03 04:36:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce1947c8-1325-3ce7-bab0-a547aa83a6dd | -10.88812 | -56.45244 | 2025-07-03 04:36:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bb17ddb-cf44-3655-82aa-7837b76fa454 | -15.56893 | -47.85704 | 2025-07-03 04:36:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50bbbd04-f347-3541-92bc-e1590172e2e4 | -12.0142 | -47.77453 | 2025-07-03 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad3a585a-ad12-3289-9cd5-1d20ca4c118d | -14.90092 | -41.98233 | 2025-07-03 04:36:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ba4a6fba-b71b-387b-8e75-60018a84aab4 | -14.80149 | -48.31196 | 2025-07-03 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c9acf7e-605d-3177-bf90-6205a6bacc3e | -9.62754 | -61.46187 | 2025-07-03 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8447c62-1738-31ae-8110-f6d4e2c96c8f | -12.42607 | -50.02688 | 2025-07-03 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edbcc576-c8ca-3960-951e-2caf5cca59e5 | -9.63417 | -61.46333 | 2025-07-03 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49cf4c2c-73d1-3700-89cf-39c102ac8acc | -12.5742 | -48.88534 | 2025-07-03 04:36:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b4f6310-bb67-383b-b357-4ec9c5f35218 | -10.88291 | -56.45278 | 2025-07-03 04:36:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2430013-b17e-307a-831b-e40b96fc3703 | -12.63268 | -54.21501 | 2025-07-03 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40a82516-4932-348b-acbb-3cb6cfd7a9f2 | -13.94933 | -46.37253 | 2025-07-03 04:36:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90e13064-e201-36f8-a48a-24ad8843788d | -13.38696 | -47.84687 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdaca643-fbbe-3d8c-9dbc-9b6043b8415e | -13.44869 | -47.82908 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6854ad5-0f44-3713-8923-9cb5359e774d | -12.57032 | -48.88835 | 2025-07-03 04:36:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e384315f-bc80-3c9b-839c-456a81f4116c | -12.57143 | -48.88125 | 2025-07-03 04:36:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d2cf321-5ad0-3814-a429-6b0c5858b012 | -12.57088 | -48.8848 | 2025-07-03 04:36:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af1dc5e5-9eb7-38e3-8c25-175dddbbce5a | -13.43275 | -47.81924 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 314dc374-8215-32e2-8983-2d85e088ef43 | -14.62535 | -53.8914 | 2025-07-03 04:36:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1431dbcb-8f48-3470-ae45-11cb6497b119 | -12.43609 | -50.02856 | 2025-07-03 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6bbe59cd-da2e-339b-81f5-c25ea519582b | -14.15268 | -45.22324 | 2025-07-03 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac23215e-8375-3f42-b219-11103cfb2d3b | -13.39037 | -47.84736 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac59d694-b338-3445-9363-134351c70ff0 | -12.42492 | -50.03403 | 2025-07-03 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a726d03c-8431-3675-ad2a-e25c0d4a4861 | -13.94586 | -46.37465 | 2025-07-03 04:36:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22a7d7b6-9a4b-3ff6-b090-e46ec58988ce | -12.4255 | -50.03045 | 2025-07-03 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 248c6249-28d4-3f99-84b5-c329d70c996c | -10.8924 | -56.45456 | 2025-07-03 04:36:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 794f2767-9f4b-3e10-8f76-0c667959f7d2 | -13.9501 | -46.37086 | 2025-07-03 04:36:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8d003b7-3238-38a5-8a01-c599539e63a5 | -14.88097 | -48.36207 | 2025-07-03 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4e85b95-7125-3238-9839-3f9832a90e0c | -9.62637 | -61.46769 | 2025-07-03 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ae5b62d-3c0e-3690-8449-f4e90b634fb9 | -14.63376 | -53.8881 | 2025-07-03 04:36:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf3e8498-f85d-394e-8e32-badb1f6bed01 | -12.58177 | -56.9902 | 2025-07-03 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf3d236f-fca3-3c4e-86bb-89f0003dff23 | -15.35409 | -49.23103 | 2025-07-03 04:36:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96da740c-b220-32f7-a40e-6a30ef23986c | -11.87438 | -54.68215 | 2025-07-03 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3db5629-ce9a-3b1a-a06f-31b0743c5959 | -12.42665 | -50.02331 | 2025-07-03 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09adf424-8714-3137-9011-9e50b48575a0 | -12.01758 | -47.77507 | 2025-07-03 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48776520-01f5-3ebd-8fae-d4bdf2253c73 | -14.15199 | -45.22824 | 2025-07-03 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbe792eb-18a9-3583-bf01-06600ea53465 | -13.39718 | -47.84835 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11dd3dec-aa48-36f2-ab65-cc41ef8a0d6e | -13.39433 | -47.84422 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aade03f-f2d9-3377-b4b8-3ca5e93677db | -13.65007 | -46.8138 | 2025-07-03 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de735bd8-b81d-3a9e-877e-7c1d6c9e5a24 | -13.94506 | -46.3763 | 2025-07-03 04:36:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd8068c3-277c-3ca1-a4a1-d15a9f88d21b | -13.39092 | -47.84372 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8675724-51fc-3e57-8b16-89b82dcee561 | -14.62619 | -53.88668 | 2025-07-03 04:36:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81cf3c20-17fe-3e9a-80ff-e9a9fe3b4f99 | -14.62913 | -53.89216 | 2025-07-03 04:36:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cecd412-2f49-3cc1-89c9-d2d03b6ec256 | -11.32822 | -55.21015 | 2025-07-03 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f261b363-5557-300c-bbc8-9e90a445fe26 | -12.41208 | -49.67461 | 2025-07-03 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c35ad6b-fbde-311a-aeaf-cfdf6224ec72 | -14.63459 | -53.88336 | 2025-07-03 04:36:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7d73cfd-d2f4-319d-ab59-4b11c9925b56 | -11.87506 | -54.67833 | 2025-07-03 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65521617-4889-3b64-905e-923fc4e700ef | -12.11204 | -54.58897 | 2025-07-03 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 315cc2de-3fde-34d4-9ddd-ed79e99407c1 | -14.85613 | -48.34271 | 2025-07-03 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0159d8c-a3af-30e9-9b57-9cfd31f47e45 | -11.86829 | -52.25452 | 2025-07-03 04:36:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a87319ee-e055-37fe-9e17-c8c487cea542 | -12.57476 | -48.88179 | 2025-07-03 04:36:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 841c8cca-5dcf-31da-a8ec-056c951a5068 | -14.63755 | -53.88878 | 2025-07-03 04:36:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 963abd47-bade-397a-86b8-bbab038e1848 | -12.42884 | -50.03101 | 2025-07-03 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1c1645f-42bb-37be-884a-923d4134f211 | -10.88861 | -56.44852 | 2025-07-03 04:36:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb9f9fb6-2a9a-38fc-9f58-e19f475774b6 | -13.4299 | -47.81502 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4208bbe-9a49-399d-bae4-a2b9629b694c | -9.63301 | -61.46917 | 2025-07-03 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bea42cf7-27d6-36e0-9c2e-5324d879ff99 | -14.85669 | -48.33903 | 2025-07-03 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75b8ac7d-b0f2-39d6-893f-32ed5630ff56 | -12.42941 | -50.02744 | 2025-07-03 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aff46b90-832c-3144-a5e1-a91904ec8396 | -14.62997 | -53.88741 | 2025-07-03 04:36:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2ee5a4c-f899-3277-998c-a6c82443dce4 | -11.79632 | -48.07883 | 2025-07-03 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ede906c3-59eb-3242-801e-78cbd3967d53 | -10.08841 | -47.99686 | 2025-07-03 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 378374e7-4eab-3283-b4e9-237a26f7c90d | -11.14383 | -43.32937 | 2025-07-03 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| d09861ff-d03b-3966-8766-4e0f43c98366 | -10.99588 | -45.19868 | 2025-07-03 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2996eb6-dfc7-3336-9f83-22f04bffb018 | -10.08507 | -47.99633 | 2025-07-03 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 076dac4e-c18a-3b8e-988a-5f8b29a66a3f | -11.47459 | -47.92514 | 2025-07-03 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3822d108-daa2-32d4-8ea4-a061b300f3d7 | -12.10225 | -44.73224 | 2025-07-03 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5aeb9efa-a980-33a8-99b1-1773f30798c5 | -11.66372 | -44.5934 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c93b2126-6f35-3afd-a5cc-22d9a3a9f93f | -11.6382 | -48.07966 | 2025-07-03 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b69f92d-7408-32f2-8bb2-4c49ceaf6b44 | -10.3916 | -52.16914 | 2025-07-03 04:36:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f622ab9a-0cfc-30ff-a5c4-7c31590402d1 | -9.80799 | -48.38485 | 2025-07-03 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80ec3e9e-9ec3-3c62-b467-e3a86280e8be | -10.08951 | -47.98978 | 2025-07-03 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 360a5897-9968-3719-9e5f-d2226c1a8ac7 | -10.30305 | -57.1381 | 2025-07-03 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67fcd003-fd71-31a1-9cba-c5287778da55 | -11.50362 | -48.95525 | 2025-07-03 04:36:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3833ed08-6f5b-3aa2-abc7-caa77e781669 | -10.94451 | -48.29866 | 2025-07-03 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1826ce58-0632-3c94-9caf-7146fb709e32 | -11.65522 | -44.59721 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 78499aad-8993-39a2-8c0d-f003f5a28fc9 | -9.60933 | -49.02016 | 2025-07-03 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76bacc2a-e4e0-31be-b1e2-df182bccaba7 | -11.65732 | -44.58231 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7915a44-eff5-368f-9e55-4d60f5d8d38b | -11.65452 | -44.60217 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2c9e7a90-ebc5-3bf1-92ab-3eff190d21e7 | -9.79558 | -47.74774 | 2025-07-03 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 130660a7-1c6e-3738-9e90-b03d8a62c2f3 | -11.54998 | -47.31474 | 2025-07-03 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e33ffda9-3b45-3416-8db6-ca62bac72597 | -11.50307 | -48.95877 | 2025-07-03 04:36:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b8f69c5-7d5b-31e8-ae0e-aa06ae344835 | -11.63876 | -48.07608 | 2025-07-03 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 53185f6f-408f-3232-a289-2eca64328352 | -11.84411 | -43.80016 | 2025-07-03 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 220bb518-e474-322d-961c-2ad51e6716c8 | -10.70685 | -49.67218 | 2025-07-03 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcb9148e-3f80-32ed-86ee-8d496546c456 | -10.82273 | -48.36259 | 2025-07-03 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24132bca-18f0-38bb-a483-56e0393f44f1 | -11.65912 | -44.59779 | 2025-07-03 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 1b320eb5-8703-37a4-a67c-179bd7e839ae | -9.70378 | -56.18758 | 2025-07-03 04:36:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23906f80-7306-3925-8359-3dae46261a5a | -10.30015 | -57.12545 | 2025-07-03 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README17.md)
