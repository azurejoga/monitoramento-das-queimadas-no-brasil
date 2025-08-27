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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e791964d-9853-3c59-b1c0-2dd6eb21a7b2 | -8.95908 | -65.97279 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8561372c-a4f5-3186-8c0c-8a4843cffc72 | -12.80368 | -48.11166 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 377bf244-c9f4-3eca-9420-22de33e3f2d4 | -9.58684 | -55.36847 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2761611-9ec5-32e1-a3b5-984dbd713dcf | -9.80018 | -64.27055 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23eb3f17-7b8b-3415-8287-ab70a7ec1a6c | -9.41911 | -60.5019 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0af6c5fc-6e64-3651-8334-1de276aaa762 | -8.94531 | -65.94868 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 0a762b1a-94df-350f-a288-41cb1eba4cdf | -9.4062 | -60.5326 | 2025-08-27 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f96f84a9-b46f-3dfd-9336-4fac7b7cb278 | -9.4064 | -60.5133 | 2025-08-27 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e65bfbb5-8a4a-35b9-9013-ef7c5fd88afb | -10.0977 | -62.9085 | 2025-08-27 05:20:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 44.2 |
| a111abe0-d17d-3703-bd17-307c37f55ee1 | -10.2743 | -64.4907 | 2025-08-27 05:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 08037794-cba2-312a-8a74-767e5c2adf9f | -12.804 | -48.1072 | 2025-08-27 05:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a6579828-6fdc-396f-8212-917a2624984e | -9.4065 | -60.4941 | 2025-08-27 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 52992f63-6d0f-3a05-8921-b76830c27c33 | -14.30204 | -53.06081 | 2025-08-27 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4dd56e26-c4f6-38be-815e-70f682a01b28 | -15.62064 | -52.71227 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e3d125a-2675-38e8-93f8-e05bc88ab9f9 | -14.30786 | -60.38264 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f4c5134-b29c-3a4a-bb48-390094c4c8d9 | -14.75892 | -47.9313 | 2025-08-27 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e78c132-ae8b-38bc-8226-35331b7a3f92 | -14.29723 | -53.0599 | 2025-08-27 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 778fe258-b4ee-317d-b3dc-5b08caa7cb87 | -16.71036 | -50.41339 | 2025-08-27 05:21:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f79aeb47-f2a3-30a1-8952-3e5859e5bf6e | -15.08749 | -48.63121 | 2025-08-27 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b60a7591-7044-365e-ae10-e9421fddef8a | -14.77432 | -59.70989 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6ebaab1-a4d8-3c57-b520-5d7fc32712ce | -16.74213 | -47.59246 | 2025-08-27 05:21:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 76e88fa3-5bfc-3f75-950a-8ac73014d4fe | -15.66362 | -52.73928 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81ab32b1-dd21-3d9e-9fda-4c3b947e6acc | -19.07854 | -48.14318 | 2025-08-27 05:21:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b34b13e-b7fa-366a-8f17-2c8ad8b281d5 | -16.73958 | -48.54134 | 2025-08-27 05:21:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f3b47de-cff2-3e83-a959-631cefecfdc5 | -16.704 | -50.41673 | 2025-08-27 05:21:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f8728ef-c6d9-3e68-bf08-596541bbe64d | -13.44035 | -46.86365 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6e03aac-ce03-3dc3-ad7f-c7aef113e352 | -14.31227 | -60.37605 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17c804b2-43ed-3ea2-9a6a-352db4475aba | -16.23356 | -58.72842 | 2025-08-27 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7a37f92f-e585-3dff-9365-2466cef215b1 | -15.62096 | -52.71444 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6c7ebdda-5812-35c5-b57a-5f263c7b96db | -13.01248 | -56.88976 | 2025-08-27 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb8e3fbf-f3f5-3611-8336-993f39736070 | -14.31448 | -60.36174 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0c1ee0a-2dc4-3c76-8e36-922ab746e273 | -15.75675 | -50.41317 | 2025-08-27 05:21:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73f8d330-1e63-3f03-8209-ca3a9f6bbaf3 | -16.38355 | -51.88815 | 2025-08-27 05:21:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f177f83-20f9-3dbd-a8ec-ae40a80b107d | -15.62431 | -52.72513 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48e686bf-1ddd-3cb9-91bc-c41c389afd34 | -13.42277 | -60.54403 | 2025-08-27 05:21:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 937f4b16-b9ee-3bea-b971-53b644d4db42 | -15.66433 | -52.73312 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37862991-4031-37b8-b27e-c90c432733ff | -11.69587 | -60.17068 | 2025-08-27 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2b9d4f6-da84-3489-87b0-5d75f556f8b2 | -16.70811 | -50.41333 | 2025-08-27 05:21:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db111058-f47b-37d5-a577-f2189e50da70 | -11.69641 | -60.16718 | 2025-08-27 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49711502-12a6-3e9f-aaed-17c420d7523b | -13.39383 | -46.92352 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a2d9840f-aeb7-3aad-932f-3be8423fbc51 | -19.07798 | -48.15011 | 2025-08-27 05:21:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8015bd40-90ca-32ec-8055-58a9fe38183b | -14.30731 | -60.38617 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de697638-f477-37e8-a87c-c7b7c2d7826d | -15.62023 | -52.72055 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14238af3-3a16-356d-baaa-cfa3d6775814 | -14.30177 | -60.35588 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09b2f701-bce8-3522-9832-ba0aaf123fc3 | -13.38504 | -46.91618 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 561cd69a-0add-3cbb-9fef-88176c4b930e | -15.6233 | -52.73399 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20707968-b003-317f-a2a7-4ec60dba10a8 | -14.58924 | -54.51497 | 2025-08-27 05:21:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 943f889a-41f1-391b-ac33-f1b9e3285732 | -11.69147 | -60.17715 | 2025-08-27 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2eaffc81-5c9a-3090-96e6-ace91824cea2 | -15.60585 | -52.71234 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a36abc2-626d-3085-992c-e83d75b075e9 | -14.7721 | -59.72458 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67618c43-6e59-37e8-b24e-079a668068c3 | -13.49779 | -46.86253 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 72dd94b0-817d-360e-9f0f-67063f46da74 | -14.41075 | -51.94239 | 2025-08-27 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 211fc328-bb82-3262-a6b1-f1b6be16fd62 | -13.39141 | -51.76423 | 2025-08-27 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62d4ae61-d552-30ab-b413-b368a852fd00 | -16.2377 | -58.7283 | 2025-08-27 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9dad9710-13db-31b4-8d8a-21e858d6d207 | -11.70248 | -60.17174 | 2025-08-27 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85b01d68-4faf-33d0-be1b-660645d16550 | -15.6669 | -48.23774 | 2025-08-27 05:21:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6a151ba-c386-3ba6-8aeb-d8101d907d9e | -17.9712 | -48.04753 | 2025-08-27 05:21:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9506337f-02d5-3bef-bb25-b747bcca0061 | -15.63776 | -52.74174 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68b64304-a2d2-3f3f-8511-942be9312dc9 | -12.17126 | -60.74022 | 2025-08-27 05:21:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 27c6fade-cb5f-3b01-9aa8-00ec79eee3bf | -13.10933 | -57.12354 | 2025-08-27 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 744cbe93-de69-3c3e-97f2-257647bffe18 | -15.09396 | -48.56234 | 2025-08-27 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 46454f1e-3d8c-39d5-adf4-dac8cd97111e | -14.30067 | -60.36308 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1f65aa9-4e64-3780-93f5-3894a8450e96 | -15.18858 | -52.32093 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c33a1b3f-3779-3b65-9e1d-4754460c6ae0 | -15.61987 | -52.72349 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b497fe8-21c4-3e97-ba0c-f11ea119221c | -14.771 | -59.7318 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bfcd9489-7ecb-36ff-bf59-87bb841f5b69 | -14.3084 | -60.35699 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bd7318b3-acb2-3ebf-b006-3f367286739a | -12.07798 | -63.14961 | 2025-08-27 05:21:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e18aa21e-b110-3ea6-9123-6122b79d1446 | -13.44804 | -46.85852 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 35a5b17a-e033-3d74-82f6-272572bcc71f | -14.5942 | -54.51117 | 2025-08-27 05:21:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5608529-8276-38bf-b7b1-2a5cc2912bfb | -14.63324 | -59.55841 | 2025-08-27 05:21:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5ebbfd3-1ad2-38b6-b5fc-0bc6a7fae651 | -15.18779 | -52.32771 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c25fa6b4-faed-3109-930c-2660bfc4b261 | -13.39273 | -46.91063 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a2da334d-a709-3490-8370-1638ce0f43bf | -13.39526 | -46.90991 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| df4207a8-4da5-3046-b614-ca9f9dc90376 | -15.04216 | -48.6893 | 2025-08-27 05:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cf1d2945-1eab-3519-93fa-ab5c86f65b04 | -15.32293 | -56.16888 | 2025-08-27 05:21:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19632a1a-f9ea-36e4-98ff-93649404b338 | -13.00747 | -56.89826 | 2025-08-27 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c6e5adc-e45c-376c-b9cc-6cbfc9acbed2 | -14.77376 | -59.71358 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6aee2c1-4984-3fac-ade1-c109f912d4fd | -14.77321 | -59.71726 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06595dec-a85b-3a99-85ad-cc13dc70811b | -11.34189 | -63.27327 | 2025-08-27 05:21:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08a64b82-32cf-3b0f-a0f8-b3ebc4e04291 | -14.30895 | -60.3534 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 028defc1-78ed-30e7-9152-c8d04f77b513 | -15.64277 | -52.74266 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 096e4825-8959-3bd2-b2c2-16a1ffef370e | -15.62865 | -52.73194 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d0225f6-b49e-381f-9828-021a078103c9 | -15.62397 | -52.72811 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40bb148b-bf19-39ba-8760-2acea7ee10e4 | -11.69202 | -60.17366 | 2025-08-27 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42638762-edac-3042-a8f4-9746817b538c | -13.44104 | -46.85687 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 927ac0df-2174-36d0-bc89-aebece1b4df3 | -15.61257 | -52.73837 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ec763be-8d24-3d8b-b1d6-ba239f39e23f | -16.70445 | -50.41245 | 2025-08-27 05:21:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 576fdfe1-6b59-343c-a61c-32d2a0d1e046 | -15.64243 | -52.74553 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfc105b4-bed0-3bcd-9de5-bf1d06387efa | -17.97805 | -48.05055 | 2025-08-27 05:21:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b38108e0-441a-3e6d-ad88-e2d389b7751e | -13.37934 | -46.9016 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a59b560c-0aa9-3183-b320-8afed00206e5 | -15.6203 | -52.71536 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5df03be-b7f2-3f46-af67-539a8a93a1af | -12.45999 | -58.00616 | 2025-08-27 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1424809-c7e3-3623-a4a6-5b8e31efec51 | -17.97057 | -48.05613 | 2025-08-27 05:21:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02d698e5-5010-3831-a1f8-40509f1fc424 | -11.70966 | -60.19086 | 2025-08-27 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 486d58b8-8942-3f73-82ca-b8f39bdcc451 | -16.24236 | -58.72071 | 2025-08-27 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 33d04856-7278-35a4-8022-37ad8452d521 | -15.62059 | -52.71753 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b6ece4d-e082-31bf-9b2c-6db452233571 | -15.62363 | -52.73106 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0ec406e-67fa-377c-a7cd-6fd6b8ee3700 | -13.39139 | -46.92422 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 219293a4-6b18-35a7-b5fd-739c74c66ae5 | -13.62254 | -48.21637 | 2025-08-27 05:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98d0ff68-0006-3547-8235-6c35f24948f8 | -12.22501 | -64.22807 | 2025-08-27 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README68.md)
