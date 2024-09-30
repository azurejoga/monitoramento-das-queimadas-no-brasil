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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4d3686b-4044-3bd7-ab68-c9ce90854dba | -11.1493 | -53.889 | 2024-09-30 01:12:19 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 718bd08c-3f7f-3166-b32c-bf8a9c11fdcf | -11.1513 | -53.897301 | 2024-09-30 01:12:19 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f208ba0-3a4c-399c-ba8a-4305c0c06860 | -11.1532 | -53.905602 | 2024-09-30 01:12:19 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a77cc58-148f-383d-8a2b-782059eaf626 | -12.2232 | -58.896999 | 2024-09-30 01:12:19 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92a22751-da66-3b03-99bf-d6587fbcc48b | -12.2248 | -58.904598 | 2024-09-30 01:12:19 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd500bfe-100a-3458-9082-5028895f9f85 | -11.2134 | -54.740799 | 2024-09-30 01:12:21 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0728bad6-4c08-37b7-bf73-4bd934174331 | -11.2152 | -54.748501 | 2024-09-30 01:12:21 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 641399c3-05a0-3cbc-a9cd-183425cfaec9 | -11.2169 | -54.756199 | 2024-09-30 01:12:21 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99854582-d936-3692-8139-662aeb092b96 | -11.2187 | -54.763802 | 2024-09-30 01:12:21 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bca26c50-7b35-3435-af0a-a2b1bfa45aa6 | -11.2205 | -54.7715 | 2024-09-30 01:12:21 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3980ffb-c37d-30c8-9615-b3e56e8bf292 | -11.2222 | -54.779099 | 2024-09-30 01:12:21 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10f37780-6a86-3ed0-a09a-2b07a44e1466 | -11.2036 | -54.743198 | 2024-09-30 01:12:21 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6990bdcd-9bb9-3c1f-8615-2d9ab8068a01 | -11.2107 | -54.7738 | 2024-09-30 01:12:21 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45714364-2274-3618-942f-85858db66f89 | -11.2124 | -54.781399 | 2024-09-30 01:12:21 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13d25820-665c-35c1-a798-58a7966de7db | -11.1929 | -54.785999 | 2024-09-30 01:12:21 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a86fe9d-dc54-3802-9c1a-23aa099068c2 | -12.8125 | -62.8269 | 2024-09-30 01:12:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 12bac3fb-9f7c-3fea-8e53-61a8944e27a4 | -12.8151 | -62.8395 | 2024-09-30 01:12:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 69505c3c-0a52-3e01-b7e8-d0e32a537549 | -12.8028 | -62.828899 | 2024-09-30 01:12:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6d7480-e95a-39a7-ad59-aea53d15bb85 | -12.8053 | -62.841499 | 2024-09-30 01:12:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9c9320a6-8006-3be8-bc11-db015956b46b | -12.7955 | -62.843498 | 2024-09-30 01:12:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2d1ca466-bb5e-31bf-8da9-5ae9458e831f | -12.7857 | -62.845501 | 2024-09-30 01:12:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 43563ce2-aa24-3221-95f1-733f7b1f1b42 | -11.8589 | -59.016998 | 2024-09-30 01:12:26 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc39b3c0-fcad-301a-a131-4b6b4d27c2c0 | -11.6842 | -58.873199 | 2024-09-30 01:12:28 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b43556d-74e5-39e7-9207-1cfb0176c9fd | -11.6858 | -58.880699 | 2024-09-30 01:12:28 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2063dcef-5476-3a5d-b990-caa9954a8339 | -10.6089 | -54.2267 | 2024-09-30 01:12:29 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a5137ee-6bab-3455-9c48-1c9b9925ca3d | -10.2305 | -52.710602 | 2024-09-30 01:12:29 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec2ab2e2-9951-30de-9fc1-9d8b6a8683f3 | -10.2328 | -52.720402 | 2024-09-30 01:12:29 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38c3ed6d-389f-3ddd-aaa9-e7986218f6f0 | -10.2184 | -52.703201 | 2024-09-30 01:12:29 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b138381-46fc-361d-a95d-f27692466d26 | -10.2207 | -52.713001 | 2024-09-30 01:12:29 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89be3c23-f9cb-316c-881a-b41cba21b19f | -10.2231 | -52.722801 | 2024-09-30 01:12:29 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36aba743-22dd-3979-b09b-6a5e0f880229 | -9.5727 | -50.1731 | 2024-09-30 01:12:30 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49f67e6f-5f72-3c76-86e4-22b138fae60e | -9.5763 | -50.187698 | 2024-09-30 01:12:30 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07630ae4-4726-3f59-b552-0a68307d13bf | -9.5666 | -50.190102 | 2024-09-30 01:12:30 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d74e9ad-0016-3d28-855b-d8c99fbf8956 | -9.5702 | -50.204601 | 2024-09-30 01:12:30 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6be2c058-ba65-37ad-a6a1-3a36e9e5b1ee | -9.9006 | -52.195202 | 2024-09-30 01:12:32 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c71b6698-f349-309d-b260-b6e9fe529af4 | -10.5586 | -55.617199 | 2024-09-30 01:12:35 | METOP-B | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bddb09f3-9e96-3947-8791-4e40bbafc88e | -9.667 | -53.162498 | 2024-09-30 01:12:40 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0179d6de-62e9-3295-801b-cb927f44add4 | -9.6573 | -53.164902 | 2024-09-30 01:12:40 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 673342e3-c493-346f-b344-10f839eb5868 | -9.6291 | -53.569599 | 2024-09-30 01:12:42 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecf52ed8-0eac-3df8-802a-b0f3ce8c529d | -10.6919 | -58.515099 | 2024-09-30 01:12:43 | METOP-B | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef513e64-de12-3d99-901a-590bb9a93318 | -10.6935 | -58.5224 | 2024-09-30 01:12:43 | METOP-B | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae864fcc-a309-31c2-905f-41b8de6bf0f5 | -10.5168 | -57.766701 | 2024-09-30 01:12:43 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94315fa9-4fd9-3b9d-9cc2-43e4ac86094a | -10.5184 | -57.773701 | 2024-09-30 01:12:43 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 105aa490-0842-3ccf-886b-bc78005fa913 | -10.1242 | -56.746601 | 2024-09-30 01:12:46 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2d2d20f-9433-37f4-a329-d936e5d4a123 | -10.1257 | -56.753601 | 2024-09-30 01:12:46 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 505b7fcb-06f5-3796-94a7-d0b76980fa3b | -9.2697 | -57.1161 | 2024-09-30 01:13:01 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adf1ce94-3799-3e9e-a073-a257a96a0909 | -9.2713 | -57.1231 | 2024-09-30 01:13:01 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7da7354f-3c54-375b-99c6-cbe97a8267e9 | -9.6998 | -62.162102 | 2024-09-30 01:13:12 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 78013248-912d-3eeb-830b-d4dcf6da6dac | -9.0888 | -61.115299 | 2024-09-30 01:13:18 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b0d7a9d-05e3-3b58-8cd1-28e9785e4730 | -9.0583 | -62.318901 | 2024-09-30 01:13:23 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7175ea17-7b22-3ba1-b16b-9b71e5d1ec04 | -9.0485 | -62.320999 | 2024-09-30 01:13:23 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bb460364-4b82-3674-9bf5-edac17f4b073 | -8.8355 | -61.798901 | 2024-09-30 01:13:25 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 91f3aad1-ead1-38a2-aa50-a0062977ead1 | -8.8375 | -61.808399 | 2024-09-30 01:13:25 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b1ec6ac6-df82-3761-b5d9-1265c81efea2 | -8.4806 | -62.680698 | 2024-09-30 01:13:33 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b9dbc04e-3bd7-34d5-9ddf-4dd6ef995d9d | -8.4708 | -62.6828 | 2024-09-30 01:13:34 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be7f8ce7-fdf4-3903-8f7c-4cdbf1543d9e | -5.0035 | -49.737202 | 2024-09-30 01:13:42 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2c7a63c-1edd-30b6-97c6-6937fb74803b | -5.008 | -49.755699 | 2024-09-30 01:13:42 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70ad7033-5e50-3562-af5e-f953057bced0 | -4.9938 | -49.739601 | 2024-09-30 01:13:42 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc27a947-4ed8-3463-b18a-c817e4068160 | -4.2665 | -48.638199 | 2024-09-30 01:13:50 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 876262e8-f038-3dbf-a403-7ac9915ace32 | -3.1058 | -49.377899 | 2024-09-30 01:14:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c80bda5e-24be-373d-832d-9fc227c7ba08 | -3.0911 | -49.3591 | 2024-09-30 01:14:12 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3323c25f-3645-38ca-aa67-033f9c2faed2 | -3.0961 | -49.3801 | 2024-09-30 01:14:12 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0096ea2a-1b09-32c6-ba4a-280b66e4a8b7 | -3.1011 | -49.4011 | 2024-09-30 01:14:12 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c26bc601-12c8-3beb-bf6a-6e54b66bc88a | -3.0864 | -49.382401 | 2024-09-30 01:14:12 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d93b1b1-bb6f-3ed3-92e3-d85519fda7a8 | -3.0914 | -49.4034 | 2024-09-30 01:14:12 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df605739-3075-3209-890c-603fa3b5a9c4 | -3.0674 | -51.204399 | 2024-09-30 01:14:19 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddd7c9af-cd86-3374-99ee-06720ac6b253 | -3.0271 | -51.4258 | 2024-09-30 01:14:21 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bace4880-a214-31a5-9678-c4e27ee37938 | -3.0307 | -51.441002 | 2024-09-30 01:14:21 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eeada29-5582-30f9-a342-b4bc471780bf | -2.6957 | -51.324001 | 2024-09-30 01:14:26 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa1b721-f30a-3c46-b6b3-ae8dd67533b2 | -2.6993 | -51.3396 | 2024-09-30 01:14:26 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f7cb772-8066-3297-9d07-82a7522937ca | -3.0769 | -53.0453 | 2024-09-30 01:14:26 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80044d78-744b-3f0f-a1ef-301e29b4455a | -3.0797 | -53.057098 | 2024-09-30 01:14:26 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcf917a8-ca9a-3d44-89e1-729367c19de9 | -3.0672 | -53.0476 | 2024-09-30 01:14:26 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e74a8d8e-c926-3f03-aa15-d7b4372cdde8 | -3.07 | -53.059399 | 2024-09-30 01:14:26 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10832321-242c-3688-9466-d6dd2184aa15 | -3.1228 | -53.730099 | 2024-09-30 01:14:28 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 737b9513-e230-3827-818c-f6fcf0613be0 | -3.1326 | -53.727798 | 2024-09-30 01:14:28 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67c1ebbd-eea7-307f-ac56-4af7d4c05984 | -3.1351 | -53.7384 | 2024-09-30 01:14:28 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43655eca-8b45-36e5-9e59-4fd3fb001b41 | -3.1179 | -53.708801 | 2024-09-30 01:14:28 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea4fa752-8f99-3349-8d36-833c5e80e060 | -3.1203 | -53.719501 | 2024-09-30 01:14:28 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f09eb2ae-4f27-3058-9c1f-2b76b5ce0cd4 | -3.1253 | -53.7407 | 2024-09-30 01:14:28 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5dad49-28d5-3233-93ff-58458dd311e4 | -2.8495 | -53.305302 | 2024-09-30 01:14:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed103f77-6440-30ef-b330-f3334e3811db | -2.8522 | -53.316799 | 2024-09-30 01:14:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af4d6d87-caff-3cc4-b1d1-ce6277de7505 | -2.7572 | -53.2173 | 2024-09-30 01:14:32 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b4717b1-aa71-389f-8900-61366ce1db16 | -2.7474 | -53.219601 | 2024-09-30 01:14:32 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb887f15-6352-3321-a573-ce7aff6cd579 | -2.9699 | -54.716801 | 2024-09-30 01:14:34 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d720e46e-b130-3cd9-a83f-070dc51bd983 | -2.972 | -54.726101 | 2024-09-30 01:14:34 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93147d0a-a679-3b6a-8b7d-ddb4430c5cb5 | -2.9602 | -54.719002 | 2024-09-30 01:14:34 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f722760d-e2a2-304d-a8a5-7664bf2e326b | -2.9623 | -54.728298 | 2024-09-30 01:14:34 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7238ed57-2acd-3192-8748-aaea6e112454 | -2.1956 | -52.036499 | 2024-09-30 01:14:36 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b3f629d-84a1-3742-9247-a7d1f41c7683 | -2.3557 | -54.328201 | 2024-09-30 01:14:42 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d0332dc-0e19-38ed-b0a3-af897be06ce6 | -2.1343 | -53.634899 | 2024-09-30 01:14:43 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30eb3ac6-fcba-34a1-ba94-3254318fec88 | -2.1369 | -53.646 | 2024-09-30 01:14:43 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57f0e384-2c15-3ed9-bf55-05673aa37454 | -2.1395 | -53.657101 | 2024-09-30 01:14:43 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54b8a387-df5c-372f-b8a4-67e466e87b69 | -2.6853 | -57.483299 | 2024-09-30 01:14:49 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce9295f-b6c6-3ca6-aed9-d4982fb44ad5 | -2.6739 | -57.478401 | 2024-09-30 01:14:49 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5e2f3bf-3c1a-382e-91db-ee68f42ccbdf | -2.6755 | -57.4855 | 2024-09-30 01:14:49 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c3410e4-e392-357d-941d-372ce270a59c | -2.6771 | -57.492599 | 2024-09-30 01:14:49 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28c40e8d-28ab-3a5d-990d-d65ea14d4b05 | -2.6641 | -57.480598 | 2024-09-30 01:14:49 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 201ae0d5-cd54-3380-90e7-77cb52c31f99 | -2.6657 | -57.487701 | 2024-09-30 01:14:49 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8a2dc9e-9175-3755-949a-35cf3212f824 | -21.86822 | -48.37363 | 2024-09-30 01:41:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 31.8 |


[Clique aqui para ver as próximas entradas](README13.md)
