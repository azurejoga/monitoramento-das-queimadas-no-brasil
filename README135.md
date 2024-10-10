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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 037d586b-a4ff-3650-9ca1-5946085bcf68 | -9.89304 | -58.12329 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5037a1e3-669f-37f6-95bc-7158398d15b4 | -9.89244 | -58.12761 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85bec1a3-3b65-3ae1-80cb-020382d3b64b | -9.89184 | -58.13189 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 156da608-082f-3546-950d-5fbbdf5b86c3 | -9.82375 | -57.7443 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1a8848d-9227-368f-97f8-4b28f0025c69 | -9.79752 | -57.38924 | 2024-10-10 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3fb21ca-8a00-33a7-bb27-dc2fbbb08507 | -9.73171 | -57.86303 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aad02de5-2841-3621-bcfa-505e095c669b | -9.68435 | -57.22197 | 2024-10-10 05:38:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fa23e92-b016-3ae3-a13c-efa5b5b49eaf | -9.65823 | -56.9502 | 2024-10-10 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0c1fd72-8d66-32a1-acd5-a7c4d0fe6e52 | -9.65668 | -56.95433 | 2024-10-10 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32ab0ac4-ef35-36e6-939c-948af613ef5d | -9.65282 | -56.95464 | 2024-10-10 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8352d0d5-d835-3fe6-82be-81b2ff22d823 | -9.65195 | -56.95362 | 2024-10-10 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d327a72-714f-3ce5-9776-57ca780f39f3 | -9.54535 | -57.90586 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37c58415-1c7b-3c22-84b8-95534f0847c8 | -9.42549 | -58.029 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac64b256-ca6d-34d8-825f-bc2526c30f58 | -10.11247 | -58.22559 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4f61227-845a-3305-92a9-7a1df33e0047 | -10.1087 | -58.22062 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 389d1e93-581c-38c8-a8b3-5302931eccfd | -10.1081 | -58.22495 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47f34b38-0570-3d44-989d-c5546ff7ae8b | -10.04708 | -57.91982 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87900cb9-a997-38aa-8d52-a1e932d6fb3a | -10.28373 | -57.70029 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39eba240-95e3-3f4b-98e1-ddc69484784f | -10.28308 | -57.705 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14cc20ab-ccc1-3d02-bebc-2519a7f1b6dd | -10.28116 | -57.71907 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4c96032-ee74-39ae-8aec-4a879451a8fc | -10.27919 | -57.69954 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92c4481d-cdd1-3f24-98d9-15ec98a91a69 | -10.27661 | -57.71843 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f073800-a5ea-364b-82ad-95583472b38c | -10.26254 | -57.9539 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de8a43a4-2415-3d04-9544-40a4c26813ca | -10.26193 | -57.95831 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cbca032-9279-311f-a0bd-6c7ac7a3bab0 | -10.25807 | -57.95328 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4af96164-6f80-3ca0-bc18-ff36ecb7b00b | -10.25745 | -57.95773 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23f55f7e-9a9c-3097-b8e8-404943a8ad72 | -10.25298 | -57.95712 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13be84a3-1600-37ef-b9e6-e49c12025f8c | -10.22721 | -57.81036 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 205e8915-2cb5-33fc-96bb-375b7dd4498a | -11.02962 | -57.21598 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 03f4079e-f952-3631-8396-9ae47427ab28 | -10.22269 | -57.80975 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00f564ae-879c-31f6-b9a8-2593e62d8913 | -10.19338 | -57.99389 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1737fa8-555d-37a1-a795-dd5065e5eaa9 | -11.96667 | -57.59455 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2beadfa-bed5-3423-afc3-a90480eda3ae | -11.96603 | -57.5996 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d46618f-010c-3090-b1c5-16ddce33a49b | -11.96198 | -57.59382 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc55ebb3-3e96-316f-b3f5-20ae74879dd8 | -11.96134 | -57.59886 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4e50454-d9fe-3702-85fe-dc6d34933ca2 | -11.28069 | -57.8758 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08769002-205a-3d20-93f8-705730f4c9ec | -11.16 | -57.18754 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b9e47c7-fd3e-36e3-824f-f55f9ddb5ab6 | -11.15522 | -57.18686 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbeff707-39bb-3d8d-bae9-9966f25d843f | -11.04455 | -57.21295 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af3300e8-bdf6-3d9f-a20c-bb70999e7285 | -11.0432 | -57.22336 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c93f3f88-0cbf-3164-9ed4-5bafef4386fb | -11.04252 | -57.22863 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 237603d5-34c9-3a02-8ce3-308aff8481f1 | -11.04049 | -57.20684 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f214f492-c104-3da2-908e-9f7f88ae5774 | -11.0398 | -57.21222 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4d44c6c2-0fa8-3f59-bdbe-240277853d70 | -11.03913 | -57.21742 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f5dfc3cd-2295-394a-bf54-d8c9a22a3ce1 | -11.03845 | -57.22265 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f2ecd87b-af9c-34dc-a4a4-18e701594e18 | -11.03777 | -57.22797 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 937b008e-671b-3e60-85b1-115d4d5a24e8 | -11.03574 | -57.20611 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a169d88c-f6ff-393e-abef-c0acd3b2e68d | -11.03505 | -57.21148 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 18fedbe8-f63a-362c-8945-3d89ff67bb8e | -11.03437 | -57.21671 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7cc49693-9983-3d6a-8b68-ef863728bc5b | -11.0337 | -57.22192 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5d5b966e-e537-31ee-b33c-59c82e9081f2 | -11.03302 | -57.22721 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 00b85f4e-dcd9-304b-a009-be8b54a592b9 | -11.03171 | -57.2374 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e31e166-1cae-387b-a120-909201215206 | -11.03104 | -57.24261 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 888492ff-d6f5-3db4-82b2-9ccfd523c511 | -11.03098 | -57.20537 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| db7b6bb5-6bbc-3c4d-ac71-e2409f30fbc7 | -11.0303 | -57.21074 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d71de1e9-4915-3909-8980-2b095ec1980a | -11.02969 | -57.20858 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2aa0c986-d77c-3843-a15d-3186c0d00664 | -11.02897 | -57.21389 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 4aae1803-f5b4-300d-a695-2f3426ea1103 | -11.02896 | -57.22119 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f7512f25-2cf8-3ccb-82ce-a4c4582e008b | -11.02828 | -57.22645 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 23c0998e-ac8e-3cd8-b00e-1405b396c284 | -11.02826 | -57.21907 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 477b6197-a039-3d97-94de-f7387b65badd | -11.02762 | -57.23162 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1478ae75-d376-364f-9b1b-eac4de7d488d | -11.02755 | -57.2243 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f7774c93-c139-306b-a031-4ef8b7d0e661 | -11.02697 | -57.23668 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a05d9714-d043-3d1f-9bb3-d3a8bf6ebf46 | -11.02684 | -57.22952 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65a5c497-d8eb-3ada-9c1b-3cb9e1f35c01 | -11.02615 | -57.23459 | 2024-10-10 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2be75ce4-6f1a-3dca-99f7-b63af554c3a3 | -8.80772 | -58.19968 | 2024-10-10 05:38:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af8b942b-9d37-3623-82fc-a715a7f53053 | -9.34659 | -59.02776 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2c440db-e3dc-3db7-ba41-a253a0890853 | -9.22384 | -58.92356 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72b0d2ae-fec8-301e-ac5d-1cbef04ecda1 | -9.18621 | -58.89148 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc6b6c7c-6f72-3b73-8355-57dbf07d74cc | -9.1857 | -58.89515 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88d9972c-831c-32f6-b2bb-4f243d583b5e | -9.18208 | -58.89087 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb41d5a7-2ddb-3428-b3c4-d74423b8c8bd | -9.18157 | -58.89455 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ef94ff0-6342-3225-8243-74cc755bc3d0 | -9.12374 | -59.01542 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eec858f9-583e-3df8-82c7-cac18ab8bbb0 | -9.12142 | -58.97306 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dff43b73-92f2-3a95-a726-dc60efbedeaf | -9.10905 | -59.53178 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e029949-5811-3dec-8ad8-b28a2de84117 | -9.0564 | -58.96402 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aac016a5-1b87-342b-8e6b-e4295c4ce667 | -9.05583 | -58.96282 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa1c2955-cd4e-3ad4-9630-93d93a823a10 | -9.0523 | -58.96342 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 836d388f-a73d-3060-8f8e-2d8f39007d05 | -9.05173 | -58.96222 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7e91990-8db2-3183-9a78-986a45c4d4f0 | -10.69763 | -58.54497 | 2024-10-10 05:38:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f76cc4a1-f9d0-3da6-a992-280596cd21b7 | -10.68958 | -58.53941 | 2024-10-10 05:38:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b650365b-5f28-3138-b38e-f177540e8e61 | -10.68899 | -58.54374 | 2024-10-10 05:38:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb993ab7-165d-35fa-9455-7fda888674ec | -10.57683 | -59.49971 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd643c8a-8797-36f1-b67b-b33b3a90c6ce | -10.57633 | -59.50328 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53fd53cc-aacb-3702-b137-03ffd0fadac3 | -10.57279 | -59.49911 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e3cbd23-91f7-322b-9a81-e4302a6b2f03 | -10.46796 | -58.76973 | 2024-10-10 05:38:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50206716-3ba4-3e6b-8b17-6af8fd10e29f | -10.46743 | -58.7735 | 2024-10-10 05:38:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8999eb96-2997-3cb4-8233-a2a973b130b3 | -10.40611 | -59.14872 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87079eaa-c657-38d3-9c62-dfbc1c034ab1 | -10.40557 | -59.15252 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a9336ff-2352-344a-a589-ab8debb4e933 | -10.40251 | -59.14429 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 967a3e17-7436-36af-9bdf-803b0f3a3925 | -10.40198 | -59.14808 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45946ced-77ef-3df4-967c-fe11a370b11c | -10.40145 | -59.15186 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a711835c-3029-3665-acec-a3eb3631d9c6 | -10.39839 | -59.14363 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ae246e1-c9a7-3ea4-97bd-5ff08ec54721 | -10.39786 | -59.14741 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bf3d5e3-ec88-384b-b33e-ed0a3fdad742 | -10.2207 | -59.40196 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53230314-fac5-3202-b14a-7a1a1d8df16a | -9.90936 | -58.6868 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 560a7a6c-1a4f-3a5d-96dc-a00a05ea29aa | -9.89414 | -59.50683 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f97901f-9fd5-36be-9cab-b9e95250d0ea | -9.89364 | -59.51036 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87a2f347-6ac6-3c5d-809a-62fede96ed8e | -9.88609 | -59.47674 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c29cfbe-f503-3430-b554-a1dbb4faafcc | -9.77329 | -59.3919 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README136.md)
