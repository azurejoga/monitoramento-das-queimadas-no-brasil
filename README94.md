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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8321a73-b8ad-3416-a264-bd77d696034b | -9.86612 | -65.0347 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 359c9d75-e6e9-37a0-9a4d-4e06dcb6e44e | -9.12824 | -65.84507 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 813999ea-0d16-3b9a-aba9-9385ae31919e | -8.7308 | -62.39841 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2279bc71-6c90-300f-9320-408fe100ea56 | -9.00618 | -65.69505 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a8a6fc7-3f74-3aa6-8631-2ef562cea3c4 | -9.07372 | -65.45563 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17d5eef4-9e92-39be-9498-2e5c6dcabd7c | -9.48417 | -65.5971 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e851f30d-bbd6-39ad-a062-64f6c5fbf1c5 | -9.00189 | -71.5807 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17946d11-6029-3a76-87d2-a2ac4b53e469 | -7.10316 | -63.0331 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d246d26-baa7-3032-a5e7-e1d0286382be | -8.85341 | -70.62535 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 488ca856-4a13-34cd-92f4-a12c8468158c | -10.36196 | -68.59292 | 2025-09-01 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d787aa13-26b4-3c4d-abac-ce7b2fe516fc | -8.2252 | -62.94342 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b838796-931c-3b5f-9028-54b747269185 | -9.45283 | -70.46056 | 2025-09-01 06:14:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38827547-724e-3a24-900e-5427a220a392 | -12.44634 | -63.92496 | 2025-09-01 06:14:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30597463-15e7-3016-a445-d5a5cfbdc586 | -7.69487 | -61.47844 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee7dd810-520c-30e0-9eb5-07186bf8d1b7 | -8.97339 | -65.96992 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 624ae0e8-d9c5-37eb-8314-c75d46ebaa9d | -6.92712 | -71.78068 | 2025-09-01 06:14:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a065b293-d3f1-327a-bdae-8d28609c6f5c | -7.83384 | -71.7593 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77f0ad0f-e502-3cb3-8e42-8df9390afcb6 | -7.56742 | -63.40853 | 2025-09-01 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ca3c0d0-cbc8-31c9-818a-7c2ac2cf67eb | -8.65086 | -67.24611 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 75531343-dfb4-3cb7-b082-c5828d51b5c5 | -9.13354 | -65.54829 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 418f5397-46ea-3fa1-ab19-64fe3fdb5345 | -9.00698 | -65.68923 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7c10943-1e85-3d4a-af7f-5f096b5bbedc | -7.67356 | -61.08758 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ad8dfbd-d11e-346c-806e-3f556fedf53b | -7.91848 | -72.95769 | 2025-09-01 06:14:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ef74109-7ca9-3a33-a12a-0a2bcd02ca24 | -9.86701 | -65.02813 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95ade632-6876-36ea-9664-2ac9cbaa31fa | -9.88447 | -65.01049 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81e6dd39-eafd-3a52-a367-6ed55dbd1138 | -8.73559 | -62.41701 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 361b886c-60b0-3fd3-ae8e-40cbf028e9b7 | -7.59546 | -61.6366 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eceab817-2a63-3c60-a65f-3a6ff491aaca | -9.87137 | -65.02883 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d0cff67-0f1f-36bc-8de2-b9798b09670e | -9.07842 | -65.43178 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 158e697f-c398-3652-8fb8-f4c0c1408f4a | -9.13818 | -65.55192 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 595b8a18-2cdf-3db5-b4fb-d9bb834b9ad3 | -7.46231 | -70.13708 | 2025-09-01 06:14:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4054df48-6adc-3706-8c1c-09b1cb1a1ace | -9.12924 | -65.8465 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e77eeed6-6bf2-31da-8e53-4390f62292bf | -9.34371 | -65.42461 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffda83eb-d254-3127-9680-d374839632ac | -9.17277 | -67.71223 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d39b6067-cf5c-3e9e-9b94-fdf6a5c4e7b6 | -8.03758 | -70.08679 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42d24fff-970f-37bb-bc2b-96f762108055 | -9.07001 | -65.45507 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc52f3e4-2aca-3ffd-bac9-dfe523bd93c2 | -7.84036 | -71.80907 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ad9646e-3b3e-35e2-939c-950cc8ee6b68 | -8.73697 | -62.39932 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 990ce567-f3a7-3563-8395-e7950d3df0f2 | -9.05891 | -65.42297 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fd095874-b06a-343d-b82d-237494385cb2 | -9.13811 | -65.84658 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5d1b592-db1b-3780-bcd8-4a90ef437738 | -8.96926 | -65.96373 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 46b56d87-4806-3c38-aaa7-783200a0b58c | -7.93286 | -63.01795 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a10c01aa-e3a0-37ca-864d-eb4671de2f5d | -8.76541 | -61.4361 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cdc4203-2b8a-3df7-9271-e7d6db04b87e | -8.81403 | -71.0511 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1056786-b831-3acc-88f5-c7a5de74aa7f | -8.72102 | -62.42643 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74399568-07f0-3c64-8496-b76c0ce6f6a8 | -9.83625 | -65.0573 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87da0f60-cd83-3749-88cf-656ec8536ddc | -9.12808 | -65.55055 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2a8b881-4ed4-37e2-879a-ed13c7e1d34d | -9.07417 | -65.42507 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ade123b-8bd8-3472-b897-b88b25413243 | -9.12849 | -65.54759 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c72ab694-97df-3421-bb0c-0e68c10e09d2 | -9.07251 | -65.43703 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a5de2c1-60f2-3365-af4d-5f7effd9c466 | -10.08703 | -68.46911 | 2025-09-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d17b663-8e4a-31df-b99e-f327358ef3f4 | -10.57422 | -67.75933 | 2025-09-01 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40312902-aea2-38b3-b728-e5b0f3eb622f | -9.17216 | -67.71645 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e405eb25-cd40-3c54-9d0c-6c55022e34c4 | -9.13394 | -65.54533 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62191bd0-21f9-35da-aa48-ebc98267bdd4 | -7.90443 | -72.87294 | 2025-09-01 06:14:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dc8a786-4d8a-3c63-bec9-811e6a5d9121 | -8.97415 | -65.96443 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 66b033e2-17d0-3910-b0d5-12a121796a1a | -8.7222 | -62.41691 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0bedc265-eb03-3ac7-ba0b-d112994cd342 | -7.66174 | -72.29136 | 2025-09-01 06:14:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d2fcaad-5acf-32c1-9ad4-dac2d0a3f68d | -7.76753 | -72.18642 | 2025-09-01 06:14:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c9de80b-0668-317d-960c-89684aef42d9 | -8.55282 | -63.01672 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80026125-6b0e-38c0-b917-9ab86b25b33c | -9.02195 | -65.69131 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54cecddf-4084-39b0-a4c5-90c35b4f44d2 | -6.97146 | -71.74601 | 2025-09-01 06:14:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b2a855f-ec26-3cf4-8129-7c6fa211622f | -8.72957 | -62.4082 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5c77f4d-9939-39b0-8930-39f72098c166 | -8.8446 | -64.14514 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1be7a3f2-9b41-3556-ac8c-2a273464c6cf | -8.75959 | -61.42967 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3daf383-ac94-3ba5-9338-0deda5210484 | -8.55337 | -63.01237 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35e257a0-c593-347b-b59b-f3cd79446ee7 | -9.14407 | -65.84872 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5f45440-e079-3e79-b280-9dbdb438096c | -9.69248 | -65.01012 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce8ddb2a-209f-3d5d-ab79-fdf0c4443630 | -9.07759 | -65.43774 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebabacf2-4ca7-3726-bbca-c0b585148dd5 | -9.65973 | -68.97622 | 2025-09-01 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a12307ec-43d0-3a18-9f21-abdff60737bf | -8.09194 | -70.22182 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d97be327-b9b4-3d0c-9b49-278f20e17ebd | -8.66327 | -70.99783 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3c08f86-7953-302b-9736-29cf3a1a53e8 | -8.04061 | -70.09171 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79312bf2-fec9-307c-bc99-5a8fae575e54 | -8.75886 | -61.4352 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd2ff79c-cc69-3cb6-b0fb-5ed23d98d5e2 | -8.0443 | -70.09228 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1acaff58-6961-3633-a343-4008bd60f96f | -8.81429 | -71.05228 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c46608d6-b6cd-3735-b66d-395ebf0a0f79 | -9.86567 | -65.03139 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02d10778-c803-3ff6-94db-224de4df9beb | -8.84412 | -64.14883 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 547090d9-c07b-3d09-8002-a8be3e039e69 | -9.07257 | -65.42484 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43016d24-4867-3f1f-9504-57c63dfc19bb | -8.45888 | -70.19159 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80fd5cc3-80e3-3072-bf96-2b29818cc5e9 | -7.0587 | -63.05614 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57393aa5-f802-39d7-b311-496155539bf8 | -8.08891 | -70.21696 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5bed660-a9d2-3330-800c-2728e7f2b8a7 | -8.74187 | -62.41026 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebb21545-d229-39fa-807c-b25a0cdcc85f | -8.7425 | -62.40527 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4098a8c8-313c-3790-a8db-87c699e91ccc | -9.82569 | -65.05592 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16316b50-6415-3247-8eb8-fbbb2c0b7d4d | -9.07043 | -65.45207 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f49bac36-b332-3ed8-8c51-8b3b4a6067bb | -8.8386 | -64.14802 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8341879-9ca9-34da-bd67-c269e60ddcec | -9.13492 | -65.84166 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a397f2b8-0717-3e3c-bbbd-fdd7704dd71c | -8.73073 | -62.4063 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05d4b5b7-6b7e-3bb5-af0b-cb45a80a8637 | -9.07609 | -65.43756 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8a85480-1530-35e0-be3a-4903f78a6390 | -8.65575 | -62.92381 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b453dab1-70f2-3163-a743-ab4c2f37a12e | -8.51133 | -67.12996 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f172ca8a-f6ce-3184-b8da-2a140cbeb542 | -7.56689 | -63.41251 | 2025-09-01 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88173ba7-1dc5-3c77-85d1-a49144072728 | -9.13344 | -65.85284 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 908971f6-b41a-3e1a-8796-541cd39d2c5b | -9.14483 | -65.84301 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24c1d15a-52e5-35fb-8554-87cfd8856ca4 | -7.28253 | -60.66946 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b82b1d34-bae0-3f61-bb34-9e7a083af973 | -7.09044 | -63.03971 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3db3ec2-6aeb-3936-ae96-abb147683564 | -7.7991 | -71.93854 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32e1402f-8d33-3f7e-84b9-ea8225a848e6 | -9.66425 | -68.97325 | 2025-09-01 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e604742-3077-377c-be02-f958a7a44e76 | -10.57547 | -67.75703 | 2025-09-01 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README95.md)
