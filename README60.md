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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f1d46b5-a8be-3522-ac73-0b01a8b57874 | -2.81013 | -49.13628 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ea10e5a9-fa1f-36d4-8c8f-d4fb520121f7 | 0.45261 | -51.0147 | 2025-10-25 05:38:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e198b52-116c-3900-a949-8705c68b6abb | -4.83393 | -50.93579 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c03d0364-f183-3b23-84ce-d0b723821f0d | 1.63948 | -55.73244 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2acf469f-015d-3a3d-86be-9266e86a6caa | -3.12321 | -49.10684 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c7384835-173f-3ed8-9028-0ea21f406776 | 1.63576 | -55.73736 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c5b40ba-54cd-3971-a9fd-66c4b4948bed | -2.80363 | -49.14827 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 7807ca96-c282-3f93-829b-98c2873e56f2 | -2.80886 | -54.38133 | 2025-10-25 05:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3be1d732-8302-330e-8e14-975f69e2d30b | -1.34596 | -54.61441 | 2025-10-25 05:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76e1f45a-c7a7-37ce-9968-bfb4efc31e2d | 2.51102 | -61.02765 | 2025-10-25 05:38:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8216cf0c-3ccd-3f72-9a53-e3335a10a072 | -3.83015 | -50.20071 | 2025-10-25 05:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f610e702-09cb-3cec-82a1-66c70e1cbc56 | -1.77115 | -55.53152 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ec6bc13-2e7c-3999-ba84-b579385c6ff0 | -1.59116 | -54.30649 | 2025-10-25 05:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba02e0cd-97d0-37fa-a484-65cde634ce08 | -2.80907 | -49.14327 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 82098af9-f44b-3aa9-add0-ebe55234900d | 1.63204 | -55.74223 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e92d2032-ac5e-3c24-8714-5c244896f704 | -2.69338 | -54.77185 | 2025-10-25 05:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eac12d55-fb3d-31f4-91e1-1d268fec04fb | -2.80465 | -49.14127 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 2987b487-8fca-38f7-820f-1e74fc14e5d4 | -4.83791 | -50.93686 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4170ca68-dd14-340b-8750-ab83e547d3b0 | 0.35586 | -50.92364 | 2025-10-25 05:38:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3bf60e6-a914-31ab-9497-1bc07ccc29be | 2.32869 | -60.92006 | 2025-10-25 05:38:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 450b42ea-1688-3a7e-9a6e-a3190a735ae3 | 1.63921 | -55.72984 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb277d7f-2060-3d7e-9e5b-b05f4e670fa9 | -4.83203 | -50.93029 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1259e41e-3c1a-37f6-9519-b33673039604 | -2.80323 | -54.38359 | 2025-10-25 05:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7a3e6bd-f834-3cb0-8e56-3f073a4f0e06 | -2.69481 | -54.77018 | 2025-10-25 05:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caf188fb-167c-3f1c-bdd7-7496462f93b2 | -3.83108 | -50.19451 | 2025-10-25 05:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e26fe2f-d631-3ac8-930b-9ab38cb092de | -3.12402 | -49.10803 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2bbdd7dd-0d62-3fe1-b818-6d93c230afdd | 1.63642 | -55.74152 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91461488-927c-37e1-a79d-f213f761e11d | -2.7964 | -49.136 | 2025-10-25 05:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 34fd0678-2eae-3d57-8318-f6bdddddb5eb | -2.8149 | -49.1354 | 2025-10-25 05:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 3f66508d-98e1-30d5-af1d-f7029b15cf8a | -10.07742 | -65.1634 | 2025-10-25 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 742b3329-47fa-3c38-b502-793ed4e7c745 | -11.93643 | -63.78702 | 2025-10-25 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a366ee42-17bc-3960-9c18-c2412cec432b | -9.59454 | -66.58913 | 2025-10-25 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 930c268c-25a7-39fd-90ac-2fe57256fe47 | -11.75465 | -61.07763 | 2025-10-25 05:40:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57e56234-ad53-38a7-8827-0a1d33d938d3 | -10.62217 | -52.19028 | 2025-10-25 05:40:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be994833-057f-3d64-9fc8-2be742f1cf77 | -10.07686 | -65.16692 | 2025-10-25 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fb7665d-1b9c-3baf-b41b-e9276c91614d | -11.8802 | -56.40064 | 2025-10-25 05:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00ff84ba-b690-325b-853f-050ea3e94cbf | -12.04339 | -54.24188 | 2025-10-25 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8bcac8b-f7d6-3f01-bdd1-aac5a7e21ecb | -10.40637 | -63.09868 | 2025-10-25 05:40:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3af5d57-9344-3b8c-972f-c0368203a9f0 | -9.83835 | -64.06754 | 2025-10-25 05:40:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3f1fd3c-3fb6-3242-b514-ad5ddf2004b1 | -10.75362 | -61.88581 | 2025-10-25 05:40:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cb94fe6-e86f-3b47-9fe4-358dedfbe4e0 | -9.45774 | -56.64666 | 2025-10-25 05:40:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d57759cc-9163-3420-9afe-3123f2e226a5 | -10.07633 | -64.98286 | 2025-10-25 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d5fe010-1832-36a5-8412-ba056465e791 | -11.97064 | -63.12875 | 2025-10-25 05:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2236c8e8-02fb-306c-8626-6e3437ff244f | -11.78158 | -63.18169 | 2025-10-25 05:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 469a1b26-3531-38a9-be24-75bc6355af1b | -9.28604 | -57.54861 | 2025-10-25 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24163376-ea6b-308c-9a58-a9082282ef0e | -11.95904 | -55.26162 | 2025-10-25 05:40:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4f4dcce-3842-3b24-aa92-a4271ac7f7a4 | -12.47744 | -61.05363 | 2025-10-25 05:40:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0340975-67e8-355e-921c-c32ea7aae1c7 | -11.71675 | -62.93515 | 2025-10-25 05:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 713ebecc-ba7c-3df9-9ea5-138a8158d2c4 | -11.7842 | -63.18142 | 2025-10-25 05:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 09c247b1-d569-3f1b-abb1-66fa02d04277 | -9.98833 | -59.95648 | 2025-10-25 05:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a11f2923-e4b4-31e8-a850-856922851eb6 | -10.40693 | -63.095 | 2025-10-25 05:40:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 444fe16c-6838-37e8-b2d4-73879881ed62 | -10.07798 | -65.15988 | 2025-10-25 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce94ee96-7f41-3745-9daa-76f0b8278eb3 | -9.45211 | -56.65142 | 2025-10-25 05:40:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18b5bc30-9896-3eeb-af60-6d0b9630d4e3 | -9.92317 | -65.00884 | 2025-10-25 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a743c15a-f35b-32c3-a2af-8f6d4fa7cd79 | -10.07409 | -65.16286 | 2025-10-25 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0fda270-e2f0-39a3-a432-11e405df47ab | -11.56154 | -54.52118 | 2025-10-25 05:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ab4fc46-886a-3825-a70c-89d018f0fa90 | -11.87981 | -56.40375 | 2025-10-25 05:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12b386b9-1ed4-3ed8-92f6-991a2eac2599 | -9.44305 | -56.64481 | 2025-10-25 05:40:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54e1e749-d9b7-39d9-a7e5-af19718f3c32 | -10.62094 | -67.9305 | 2025-10-25 05:40:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 355e976f-5526-35cc-ba6b-f79ef34234c9 | -9.26235 | -59.49184 | 2025-10-25 05:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebbd8c51-ec0a-3724-92eb-b4fe7ab10282 | -9.26637 | -59.49242 | 2025-10-25 05:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42449741-5752-3898-a907-180a2a440487 | -11.71329 | -62.93461 | 2025-10-25 05:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9358dab-6d4f-32b0-be04-60de04454038 | -9.72682 | -67.47271 | 2025-10-25 05:40:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83815816-2937-3e5d-85b9-961124cd631a | -7.00711 | -71.80424 | 2025-10-25 05:40:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a019e383-1ea9-3345-b0ab-aca7203e1236 | -12.04097 | -54.23977 | 2025-10-25 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79904cb5-ae97-318e-93fb-a115c9e272a9 | -11.55622 | -54.51624 | 2025-10-25 05:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62d28358-8751-3f33-8dc7-017c65bd5943 | -9.98721 | -59.95897 | 2025-10-25 05:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5caf45e3-444e-3783-89c4-bb1ce1738a56 | -10.62022 | -67.93477 | 2025-10-25 05:40:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54897c72-08c7-33b8-b3cc-ff01d408a554 | -12.04393 | -54.23749 | 2025-10-25 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09545834-95ad-3119-88fb-daddf8cb5d2c | -9.44231 | -56.65024 | 2025-10-25 05:40:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8448880f-1d0b-309f-8f8f-4d855f11a0ae | -11.78078 | -63.18088 | 2025-10-25 05:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6519a8bb-8066-39e7-bb10-8d83b1d2e725 | -9.72324 | -67.47208 | 2025-10-25 05:40:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac55aca5-a399-38b1-bfe9-b2c15df4d1f3 | -9.84223 | -64.06456 | 2025-10-25 05:40:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12c3cea3-59ea-3107-bcd0-7b4e9acfefca | -9.457 | -56.65203 | 2025-10-25 05:40:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db129f51-98d2-3730-9eae-e55b6ed55fdc | -10.62285 | -52.18459 | 2025-10-25 05:40:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1704d30-6b0a-355a-a944-1e4f818b6088 | -18.16494 | -51.75668 | 2025-10-25 05:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5bedc35f-4e04-3a5a-88e1-86043b7f2401 | -14.86039 | -59.63654 | 2025-10-25 05:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 551973cd-ddb4-315b-923e-ca79b648ae7c | -15.94511 | -56.11687 | 2025-10-25 05:42:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e561bb1b-6ad2-32c2-9b4b-9f20371ddaf3 | -18.16474 | -51.76196 | 2025-10-25 05:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bcf0f5ce-8d8a-32fa-94c4-f7b265574261 | -15.32354 | -52.99846 | 2025-10-25 05:42:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d36d8fa-313d-38dd-af41-3f6daa7a1939 | -14.79074 | -59.24135 | 2025-10-25 05:42:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3a23874-188a-31d5-9b5b-67475bbd8f2f | -18.17275 | -51.75468 | 2025-10-25 05:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fa94b4d9-5826-33d2-b5e9-addccc71c271 | -18.17167 | -51.76455 | 2025-10-25 05:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fc8d7d2e-c3c2-323f-9743-7718f4e863e1 | -15.94407 | -56.11541 | 2025-10-25 05:42:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7a167fce-d6e4-3ecf-accd-28b87f4cb1d2 | -18.16429 | -51.76414 | 2025-10-25 05:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f43233d5-1268-31b6-a741-d2040a8ae6e9 | -18.16535 | -51.75447 | 2025-10-25 05:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1a7b1bbd-bba4-32bf-b3b6-669993e32fe9 | -18.16562 | -51.74879 | 2025-10-25 05:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bfa04823-0f89-3c74-b0ba-78ca71c6c6b2 | -14.89283 | -52.45443 | 2025-10-25 05:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f57e4d43-da0e-3a83-89d6-96e56cebd532 | -15.94468 | -56.12059 | 2025-10-25 05:42:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 03fa4abc-b5e9-32c2-99a6-99a75323aabf | -14.89909 | -52.46109 | 2025-10-25 05:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e87208de-6d98-3c06-8a56-620595a785da | -12.60959 | -62.09138 | 2025-10-25 05:42:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87116a7b-9452-323e-a139-31750c51c939 | -15.93446 | -56.11184 | 2025-10-25 05:42:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 94896e7c-e6b2-3b65-b06f-6f4a53dbf2c0 | -14.8935 | -52.44775 | 2025-10-25 05:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5f08df6-7d90-376d-950f-53203f435d54 | -15.94 | -56.1125 | 2025-10-25 05:42:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e8dc98b3-51b1-35be-afed-3fd2ef13ce7c | -18.17213 | -51.76232 | 2025-10-25 05:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8c7a47b8-8346-3c92-86e4-5af3f55fd959 | -14.89132 | -57.84571 | 2025-10-25 05:42:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3648ab69-22c6-3e51-afda-a7a5eabb772e | -18.17149 | -51.77022 | 2025-10-25 05:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a2e91c79-a22d-37e2-a1ce-9472c7de19da | -15.94366 | -56.11913 | 2025-10-25 05:42:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 134ba4b2-f62a-359a-82d9-5ef859521637 | -15.93957 | -56.1162 | 2025-10-25 05:42:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2faaffab-238a-3019-a371-6733a3a09aae | -18.17234 | -51.7569 | 2025-10-25 05:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README61.md)
