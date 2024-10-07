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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a56a62db-2f89-37da-ae48-46fa5c3bfcff | -16.99523 | -56.69402 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9ad15780-274f-363d-88d6-92684981820d | -16.9912 | -56.7245 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7c3ad7b6-6886-3e8c-82ef-89cae81d614f | -16.98596 | -56.73406 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 19900ad2-331d-3427-b481-3c23491930ff | -16.9854 | -56.70812 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 1650a069-1a59-30c6-bd5c-0ea6a0376483 | -16.98529 | -56.73912 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 06537312-242f-347b-8407-82664c93b48b | -16.86864 | -56.71902 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1fa2b146-f32c-339a-99d4-f1bcad2d290f | -16.86795 | -56.72406 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 36ddbf5b-cbfe-3d44-a0b0-150219f74665 | -16.86655 | -56.73415 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6ffeed97-abb2-3c1f-a873-344a371a1a7f | -16.86629 | -56.73556 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 50881f12-9b59-3bdc-9e4c-0bf5d87d3cc7 | -16.86506 | -56.71478 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 14d6f14d-c8c3-30c9-9a6e-83a087747a8a | -16.86475 | -56.71846 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b93f63d4-b81e-3c69-a72c-e189a3db8388 | -16.86197 | -56.73861 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f5444b89-791f-3610-9dbd-3b5e4b9de290 | -16.86085 | -56.7179 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6a2e0d8b-600b-33e4-aa4e-8232033a2a55 | -16.85808 | -56.73805 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8dcd181f-7356-345b-aa47-3b23a186da60 | -16.85785 | -56.73945 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b47c275e-c39c-32c4-8fc0-96699badde64 | -16.85739 | -56.74307 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| edd0745f-43db-3c72-bc03-daa628b9eba5 | -16.85719 | -56.7445 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4e995e1f-ba62-3ee0-8cb6-f57371a15676 | -16.85419 | -56.73748 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 347b747a-032b-328b-8aab-5a5a21540f50 | -16.8535 | -56.74251 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0ca54c7c-a5fa-3946-b964-3965828dbea8 | -16.85099 | -56.73188 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 348a0563-d8da-3b8b-966c-16ab8d3618e7 | -16.8503 | -56.73691 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a95b6f43-926b-31fa-97fd-197d0b95a654 | -16.84892 | -56.74696 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dd9cc71a-dedb-3393-9b91-77f0022fc4d7 | -16.8471 | -56.73131 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3ee0608d-4646-3096-bc72-575e7b2fac40 | -16.84572 | -56.74137 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 750bf2b1-80d3-3d75-9f9b-8719f17813b6 | -15.67009 | -59.44418 | 2024-10-07 05:18:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae330a18-e3ba-3a87-81bc-8988b14d45f0 | -15.66953 | -59.44787 | 2024-10-07 05:18:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63fd32fb-32a8-35bb-bcfc-d2d3be029f93 | -15.66614 | -59.4473 | 2024-10-07 05:18:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b169174-51dc-38ef-8cd1-47750c3b87a4 | -13.38716 | -61.93581 | 2024-10-07 05:18:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 18a4fb82-fb50-36b3-b1f0-3b33924a5de5 | -13.39116 | -61.93268 | 2024-10-07 05:18:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ee0dad9b-2e31-3449-919d-980242cdd051 | -13.38777 | -61.93211 | 2024-10-07 05:18:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 990eba4a-edc2-325d-815f-0b4c788a38fe | -13.38721 | -61.93244 | 2024-10-07 05:18:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 06e47f21-fece-3299-9eab-bf049ac1b74e | -13.38661 | -61.93615 | 2024-10-07 05:18:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a71a9ceb-d7f8-36dd-a9b8-080bd01db5d3 | -13.7375 | -60.64685 | 2024-10-07 05:18:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c251be3-b928-370d-ba1b-5bf5dee9439c | -13.73474 | -60.64276 | 2024-10-07 05:18:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce5a832f-f1cc-3bb7-859b-53041cd08fbf | -11.90017 | -63.23923 | 2024-10-07 05:18:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b299ebf-0817-3a5f-b844-a869da0887bc | -11.89946 | -63.24345 | 2024-10-07 05:18:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a190f552-a42b-3b35-bf79-51a990db0e95 | -12.72209 | -62.90761 | 2024-10-07 05:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b76e422f-7d13-3f8c-b5f6-c4e09172fa16 | -12.70051 | -62.94943 | 2024-10-07 05:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 92b91a6c-ee3a-3536-8fab-7bb59782e328 | -12.69766 | -62.94477 | 2024-10-07 05:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 74880daf-c37e-3084-b8eb-59ade8092371 | -12.67362 | -63.0868 | 2024-10-07 05:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 152c4da1-9b96-3acf-8b7f-988c0a1bd55f | -12.87152 | -62.79362 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2380f06-e836-314b-929b-19449f9582cd | -12.86868 | -62.78905 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4088834-dc69-3976-9335-a475c21b865f | -12.86802 | -62.79301 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edb45bad-93c4-3c46-942c-df2aeb964fc8 | -12.86101 | -62.7918 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 26553c3b-445d-3e4b-8230-11ce58d71d2e | -12.82827 | -62.9009 | 2024-10-07 05:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c103d3bf-bb8f-3b14-a567-384e2177824d | -12.70337 | -62.95408 | 2024-10-07 05:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 72110ff9-8588-385b-85bd-9d48ed1d6efc | -12.99547 | -62.72039 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c90bd7a-b16e-3145-b0f0-79d1b393060a | -12.99133 | -62.72372 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2b0cfce-fa65-3113-adb5-d6e0cb0dcd5f | -12.98457 | -62.6781 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf54adc3-a83b-3507-b7b0-46d05a3e2b58 | -12.98174 | -62.67358 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 142f23d1-42de-324b-9934-19c3d862d2db | -12.98109 | -62.6775 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15a734a8-e924-3963-a5e7-d4f53ca9393b | -12.97695 | -62.68082 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aac222a-7682-3dff-a350-bb2af8cda64a | -12.9763 | -62.68473 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a482e5c-1fe9-3709-ba53-3abf38c8d5d5 | -12.97281 | -62.68412 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 679a68ee-c72a-3530-a327-eb702564488d | -12.97216 | -62.68804 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40e5b06f-274e-3bd0-8f03-a53a6949a7df | -12.94298 | -62.49187 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb0896ed-771b-3261-83a7-ef4d6b984ea9 | -12.93952 | -62.49127 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4aaabad7-955e-3398-bc6f-cf8ae70dc68d | -12.92913 | -62.48948 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ed7e8c74-0630-347c-bc4d-49b682e7b0bf | -12.82349 | -62.47137 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82e6e905-e533-3e6d-ad20-5f789ba4483a | -12.82003 | -62.47077 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82ca5995-5da7-3818-8a6b-0f68ca91d80f | -12.98523 | -62.67418 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 082d8325-7983-3f1e-a91c-abad3f03120d | -12.98044 | -62.68142 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a4f474b-f46f-3fcb-bc33-8e63986ca1a0 | -12.94708 | -62.4886 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 111b0c2b-3101-32f7-bf15-b1171b0d9d72 | -12.94361 | -62.488 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f8bd337-b0ee-3283-932d-96fc860578d6 | -12.93542 | -62.49454 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d34a14b0-f652-3b2e-8cdb-7527173ef6c6 | -12.93259 | -62.49008 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f1b4e993-31f5-3f52-924c-900330166e13 | -12.88401 | -62.78354 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e94b3ae-5667-30fe-9d38-ccf0509387d8 | -12.88051 | -62.78294 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd1f771a-a755-3621-8f5a-fe3327776ec0 | -12.87634 | -62.7863 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ccb8285-963b-34a5-8a69-4991bd3b6c65 | -12.87218 | -62.78966 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d73e513b-dd63-3c20-94fe-eb29529625d8 | -12.86517 | -62.78844 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b4a95f09-203e-3bdb-8063-6651117872cd | -12.86451 | -62.79241 | 2024-10-07 05:18:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 03ca7719-75d7-35dd-8c0e-155f019b698f | -12.86167 | -62.78783 | 2024-10-07 05:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 19047ad3-5954-3832-8b80-4783c810b8b2 | -10.6399 | -64.52758 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a99aca3-9c84-38c5-a596-7cfd5c4aa170 | -10.63903 | -64.53267 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd609db5-552a-35a4-9dbd-a2625fc1502f | -10.61247 | -64.42786 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b3a0c42-003d-319c-a76b-246149b9c401 | -10.59248 | -64.40636 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25fa4b5b-8112-3eb1-b903-07275ac1f0ba | -10.58771 | -64.41072 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b7506bc-39ed-3dc4-9ad7-a8f60dcad8df | -10.59956 | -63.74187 | 2024-10-07 05:18:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae0acea7-793f-312b-9174-f74622124df9 | -10.59858 | -63.74386 | 2024-10-07 05:18:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb663f39-d7e9-3021-bb20-f99c95d3e296 | -10.59579 | -63.74122 | 2024-10-07 05:18:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb49b745-a7a0-387b-9295-e1f88233971a | -10.59481 | -63.74324 | 2024-10-07 05:18:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b82172b-3345-321b-bf31-e8095519e87a | -10.52737 | -63.59668 | 2024-10-07 05:18:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13732a38-a7aa-3821-8b47-89273a6d5cf6 | -10.34103 | -64.25639 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 247bab90-e1d5-3ed6-8938-72563d49ac14 | -10.34018 | -64.26133 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67832e31-e2d2-3bea-bc7c-05b5e18ada14 | -10.33713 | -64.25568 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 404e76ae-04bd-32d7-b98e-0754eda48e72 | -10.33628 | -64.26062 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4076fae0-c29a-39ee-9eae-6d1a636f84ec | -11.74252 | -63.81873 | 2024-10-07 05:18:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 625f4837-2900-312e-bb4e-10e57b245a2f | -11.00881 | -63.90139 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a653d8b-e581-37eb-b882-e62accce3c84 | -10.99574 | -63.91595 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95683140-6985-3c46-ae12-c3f933f1016c | -10.99496 | -63.92059 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6e6e652-23e1-37ff-a24f-8831f6fe1fb6 | -10.99426 | -63.91783 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a40174b4-f71f-3dc7-b0c0-36636b03c392 | -10.99348 | -63.90616 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0bd7ba2-3ba4-3510-ac47-364de175eb52 | -10.99344 | -63.92253 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb0e3c45-41f9-3ab8-b30e-c725fc1bfc54 | -10.99269 | -63.91087 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdb49a3c-1aed-3cb5-a996-3208077d967d | -10.99205 | -63.90811 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 80864cd1-dd01-3d78-a1a0-d72671a37665 | -10.99111 | -63.9203 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d91618cd-dd23-326b-8ee7-44eec9447359 | -10.98965 | -63.90578 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6435556-5f11-33fc-9b6a-f6ca74ec2ba1 | -10.92239 | -63.88864 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b80547d2-3736-3fc6-92ca-9c10f15c8179 | -10.91781 | -63.89257 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README125.md)
