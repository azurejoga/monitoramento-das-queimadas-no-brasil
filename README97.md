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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95e7c57d-0cb0-37d9-9632-e5c79892f25b | -11.31299 | -51.31248 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12ba1ef6-3f0a-324a-83b7-cffc3f554834 | -11.30731 | -51.42085 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b856f4b2-90b7-3a8b-8e92-4cb23af7d5de | -11.29678 | -51.08735 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8656f15c-e24d-3353-9594-cd5922d4640b | -11.24682 | -51.28653 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99c9f2b7-f8cc-30ba-b3ee-d66d6bd7d5c2 | -11.19081 | -51.38557 | 2024-10-09 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ea500c7-d29e-39cf-bbb6-111624e84ffb | -11.18621 | -51.38469 | 2024-10-09 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 243861ea-047e-3c25-8a5e-684bc098e146 | -12.77465 | -51.38657 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1bf3713-a21e-342c-9154-2eb576f7b475 | -15.67486 | -52.51799 | 2024-10-09 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 500c5795-57b1-33bc-bedf-7a9b21878018 | -15.67391 | -52.52294 | 2024-10-09 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 66b67b2c-e65e-314e-8c13-f9f87d54fc3b | -15.67313 | -52.50236 | 2024-10-09 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7a505986-8b4d-3adc-bba1-a58edc8bc485 | -15.67218 | -52.50728 | 2024-10-09 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 02a0c1bb-f8ad-3c69-9285-dbe83714e612 | -15.67122 | -52.51225 | 2024-10-09 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 055c5172-84de-3153-b3f2-527a311e3019 | -15.67026 | -52.51721 | 2024-10-09 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 881c08eb-8ed9-3380-85b8-44d28030e821 | -21.65608 | -54.48953 | 2024-10-09 04:17:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a1f5f720-440d-33b1-bc62-e005d28576e8 | -18.10683 | -56.39443 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fab1f3f8-261b-302b-b574-e81411eb4349 | -18.10048 | -56.38096 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 50e5586d-8f03-37fb-9464-d10de7c0bca2 | -9.47499 | -52.1021 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6902c848-c2fc-3eb3-860a-33a2641e2d42 | -9.47001 | -52.10117 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5072907-0d80-3b23-a058-5371e89454ea | -9.46557 | -52.0973 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0a7540e-87d1-3617-a3b2-58cb27eb7beb | -9.46503 | -52.10028 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23ea0752-fd34-37d8-99ac-128e61aba8af | -8.98537 | -52.7991 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d0f1f75-b6ee-3a24-b29d-75fd1f375663 | -9.67274 | -52.23575 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebe08309-3673-31cc-b0f1-6233e183c1b9 | -9.67221 | -52.23867 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3685e49-72ab-3631-a0a9-af37d00c4f99 | -9.66718 | -52.23787 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6006de73-0ff4-3645-9433-50e7e55482bc | -9.66663 | -52.2409 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 310200de-90dd-3f8e-8966-c50195e64cf5 | -9.66608 | -52.24395 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2edf09c-4ef2-3bc6-bff9-75b4826f0110 | -9.66267 | -52.23423 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63091fea-98cd-369c-a77a-27ccd4f96637 | -13.31608 | -53.72721 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e829107-03a9-3ef7-a331-e17491e09261 | -13.31154 | -53.72289 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d6bed0a-6eb2-3f9f-ade8-7eb50cb909bc | -13.31093 | -53.72605 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ddac0de-0f41-34ac-8e98-83dd16b1debb | -13.31032 | -53.72922 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efc55ca0-b536-3848-8170-8f7ec383324b | -13.3097 | -53.73245 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77176ca4-636f-39f1-85d3-6314694b47ac | -13.307 | -53.71858 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b49068b-543f-3096-b4b2-ba724b6f6659 | -13.30639 | -53.7217 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9983c37f-db59-347b-8716-ebc4210fb666 | -13.30578 | -53.72487 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49a11a2e-491d-3215-9449-f20c90c5f821 | -13.30517 | -53.72803 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff52f7a3-86a7-3682-ab9b-1fc9419c35bd | -13.30392 | -53.73452 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32ec9715-dc49-3cbb-9c3a-df634c5488a3 | -13.3033 | -53.73777 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca1a4298-2a28-344a-b0d9-4dde2ff2a6e9 | -13.29815 | -53.73658 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4da4d038-59ca-3463-9517-f8a499a60eb6 | -13.29752 | -53.73983 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a0a0558-1fb0-307f-af7a-147c9b604358 | -13.293 | -53.73542 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc85b5ec-a296-31e0-ab6b-8c63221887b7 | -13.29237 | -53.73865 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5792f50-9b59-3779-a83e-365d92a5ff74 | -13.29061 | -53.69227 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e887178-c894-3f79-931e-576cba20490f | -13.29001 | -53.69539 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d041886e-c24f-3b2b-8df9-e48c2712e26c | -13.28722 | -53.7375 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb3e497e-fdb7-36d6-8aba-9271c123e3c4 | -13.28423 | -53.6975 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f3a8c63e-dbff-35f3-b3f3-8b2f40313057 | -13.28363 | -53.70062 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a589632-63b1-3ca1-a98d-53879c78daf2 | -13.27905 | -53.69653 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d7175da-31d5-3707-ad64-d79d30205c87 | -13.27845 | -53.69966 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b20c965e-9334-3e39-9f26-b1483309bb61 | -12.88731 | -53.47563 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74383479-4abd-3be6-9043-1e828550a202 | -12.88278 | -53.47149 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e8a857e-34c8-36c2-bda0-e782f5e2b11b | -12.88218 | -53.47458 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a94848f0-9b03-3c23-b2cc-1b497a117818 | -12.84782 | -52.82284 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6dbab39-d701-34a6-b77a-e678a5e28282 | -12.84671 | -52.82852 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 088bf439-31c3-3228-b806-2f6ebb3829fe | -12.84638 | -52.82114 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a0c7c0d-eb18-34fc-a0ab-41ea480bc180 | -12.8429 | -52.82188 | 2024-10-09 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bc7ac80-7511-3727-9fec-970a5354b451 | -12.84179 | -52.82758 | 2024-10-09 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28283efe-3e28-3e28-b3bc-d9edf3066e21 | -12.84148 | -52.82012 | 2024-10-09 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38f82dfa-25e8-3253-895b-db3ef1fbcf30 | -12.84068 | -52.83326 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f3c29cd4-63ef-329d-9b9c-dba03e54588d | -12.8404 | -52.82586 | 2024-10-09 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01e87aa7-0b39-3c0a-8e08-ad61887a291e | -12.83933 | -52.83158 | 2024-10-09 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67bddfa7-62d0-30ec-baab-a95f420e4367 | -12.83549 | -52.82484 | 2024-10-09 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b03b2877-fbc3-3f76-85c5-ff1423a1a1f7 | -12.83442 | -52.8306 | 2024-10-09 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a13b7eb3-d15a-376f-abd7-8f30b0513094 | -12.6301 | -53.11823 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08ea515e-2f0a-3a23-b80b-17afec98e588 | -12.62449 | -53.12025 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63c19c53-196b-3b2b-a638-951dc86b9e72 | -12.61658 | -53.02605 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2fb6e82-4b06-3848-911c-d1880dbf1bb7 | -12.616 | -53.02903 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5af42fa-ea13-3eeb-8d6d-66fa15e31e90 | -12.61098 | -53.02811 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bf1f833-5b9a-35cc-afdb-1e67e5d8d109 | -12.61041 | -53.03106 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73454316-f45e-3e9f-9f30-0ab3b69a5943 | -12.60456 | -53.0364 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29294806-f1e0-3f17-8073-a621a3d6b907 | -12.60426 | -53.03599 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2035580-a380-3705-973e-fdf2c25aa1e3 | -12.58343 | -53.06603 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc1571b-44d5-3c69-8e75-de803ca140ae | -12.58287 | -53.06903 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6d9025c-9788-31cf-96d0-006d01dc47f2 | -12.58231 | -53.07201 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 824ee687-3c5d-3a2a-873e-c5564a0c8e3d | -12.5784 | -53.06509 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a67f735-34d1-3fbd-9964-b85100324b41 | -12.57785 | -53.06807 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f81fa4b8-18bb-313f-b02f-2695f8dad56a | -12.57729 | -53.07103 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee1376b2-0707-3fdc-a2bf-36c7c37ebcab | -12.57337 | -53.06419 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2c26b58-3a57-32da-8403-8a60d7d9fd42 | -12.57282 | -53.06711 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f94d495d-250f-3989-950b-6ad1ff8c7ccb | -12.57227 | -53.07004 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec8db0f8-e82a-324f-a46a-18e57ace6c15 | -12.56779 | -53.06618 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb9a2f0d-0dad-33b5-b8c5-244ec49eb641 | -12.47888 | -53.14843 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d069f60-72b0-3d14-bf61-393d54f4cae0 | -12.47565 | -53.14629 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 327390dd-a094-3780-b057-53b1c426e130 | -12.47382 | -53.14745 | 2024-10-09 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3af6fa13-fa90-3fc9-b8df-176ffce815a4 | -18.93143 | -54.56276 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 885da840-c215-383a-9f16-00148107c98d | -18.93071 | -54.55942 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 06cdc4fc-7102-30da-8be0-e5c56d713a56 | -18.92951 | -54.56537 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 84cc2aaa-0907-3a3c-8c70-1fdab4e46f6c | -18.92901 | -54.54979 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2a89421d-e3b3-356f-aa79-f37bcaae7cf1 | -18.92784 | -54.55538 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80d94f41-0169-3c26-9dd1-df22e440e18b | -18.92706 | -54.55215 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d1b4ec5b-2436-3b7e-b00c-8952eab0427d | -18.9266 | -54.56131 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 50a3422a-e273-3c7c-bc67-c059e3b2a4e1 | -18.92222 | -54.55071 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 012bf8d9-2796-3273-b636-79f49f40cb3f | -18.9211 | -54.5816 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| af3fa60e-f1ab-33e3-9452-f901a02b1b01 | -18.92106 | -54.55645 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8695d1c6-f9ee-351b-9a3d-16fe35e92be1 | -18.91621 | -54.5804 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ce09623b-4482-3c06-a9ed-d12dfa4e3ba9 | -18.91 | -54.58565 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9d46d47-3386-35a0-84fe-027194d41afa | -18.90006 | -54.58399 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2b97403b-f775-3be2-83d8-ef3da7778342 | -18.87016 | -54.57938 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18826a61-bc91-3d4d-a671-3b5492742174 | -18.86518 | -54.57854 | 2024-10-09 04:17:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a42146f0-52c4-38f6-aa06-86655aa3aee3 | -20.07422 | -54.52008 | 2024-10-09 04:17:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README98.md)
