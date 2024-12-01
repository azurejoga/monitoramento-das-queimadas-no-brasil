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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45f1d39e-4a9e-3ff5-97c6-93dc23763217 | -0.6033 | -51.69602 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a798bc54-779f-3315-9068-1b8db4fe3eae | -1.24023 | -51.79584 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 389c387c-85ed-361d-b9ba-8766d66897a3 | -2.11934 | -46.56246 | 2024-12-01 05:05:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25f248a0-fb9b-3025-8776-6e1ade7103a2 | 0.08354 | -60.46818 | 2024-12-01 05:05:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e60ca21-3475-3bec-85aa-f452d26f5418 | -1.25345 | -51.74597 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d4d8fde-64c9-3f10-962a-7d7e816e76d1 | -0.59946 | -51.69542 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ea08a5fd-6ad0-3095-a368-aab35c34d225 | -1.15746 | -53.54874 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69dc73a3-f14c-3936-92b5-b9ac3e475542 | 1.16957 | -55.96233 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c73fbbe0-4ae5-35df-a801-44b5b29d06ea | -1.24082 | -51.80303 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db63f6cc-8e36-3158-ae78-cb7f5814c533 | -1.28128 | -51.74533 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aff7f3e5-bb8a-373e-956e-30d9d45d3247 | 0.93512 | -50.74852 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 263aa87e-5df0-3345-ab21-18e838584989 | -1.27027 | -51.632 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96f30f61-c590-3a3f-81e3-573e756aed89 | -1.25458 | -51.79043 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ab44a57-d0bb-360e-b2a3-6b5a385ae3cf | 1.17841 | -55.95392 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8d36d78-b8c1-3780-9b0e-69fd49d2fe1d | -1.19164 | -51.92915 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 205ce12c-367b-3beb-8ea9-15c720dfaae0 | -1.00589 | -51.73136 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 74e105ab-71fd-306d-b6b2-50b7208e30e2 | -1.31952 | -51.97289 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89a42e30-e034-3ab2-9d3e-35b760f94149 | 1.14872 | -56.00381 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8349c16a-1db5-3f80-b5c4-48f513034e92 | -1.03985 | -51.74148 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3adedd64-1159-3ecb-9a79-55969b96c032 | 1.17827 | -55.9962 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcd30f2b-bf08-3be9-9a56-c662487a0235 | 1.17436 | -56.01442 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2113c011-4752-37cd-bfe1-7aa1f5da181c | 1.17489 | -56.01785 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71a51907-7c41-3e4c-a661-22be8b4cf5fe | 1.65116 | -50.933 | 2024-12-01 05:05:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe90a266-0423-3c04-b2ed-1081c0183c1f | 0.9887 | -50.26913 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cae88b86-6501-34ed-abe8-7742f42c91fe | -2.28394 | -45.60459 | 2024-12-01 05:05:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 27018404-924a-3f83-9e45-36e28cfcc117 | -1.05956 | -53.22613 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dfba42d8-86cf-3cb8-a233-58c77cf24a03 | -0.87672 | -53.68042 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a6ee40d-b83f-3208-a7fd-25f76174de61 | -1.24155 | -51.79824 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ae35834-fb0e-33d1-b1a6-1bac8fe9b29d | 0.69547 | -51.44152 | 2024-12-01 05:05:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9437818a-4584-3783-bc9d-6085070c0d13 | -1.24686 | -51.78925 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b3aea71c-1a6a-32ba-8af5-8d442898a290 | 1.25854 | -50.68658 | 2024-12-01 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bb85204-ae08-3b37-9a5d-7883aa2f30e7 | 0.62183 | -60.08391 | 2024-12-01 05:05:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af4c4306-30e9-3e6a-ba7a-37a92ed8ff0c | 0.9784 | -50.12177 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 308ba8a7-7dbd-35c3-95f4-4aef516c94ae | -1.30363 | -51.72893 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 023a0fc0-da74-323e-82fa-22607560bb34 | -2.12264 | -46.57806 | 2024-12-01 05:05:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f647e34c-335e-3448-8102-f6932262a443 | -1.07248 | -53.63454 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44a98848-b867-3cfb-8534-453ee24ba837 | 3.63669 | -60.11954 | 2024-12-01 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 697858bc-2527-317d-87bb-91730f311e9b | -1.26358 | -51.75739 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68623019-dfd6-381a-9f93-b1f22c486547 | -0.00729 | -51.16415 | 2024-12-01 05:05:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 220fa0bc-a457-3672-be47-ae78a92ca087 | -1.36439 | -51.85881 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83aa02fd-42a6-3b06-ade1-374c916a7d6b | -1.32086 | -51.97038 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2baa8167-e285-3bb5-8200-7aa86a27d381 | -0.24807 | -55.91334 | 2024-12-01 05:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9482ad30-9c70-3982-8f2d-6eda97b99e4f | -0.76711 | -52.46143 | 2024-12-01 05:05:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32df6615-8329-3c15-83bd-188824481969 | -1.28285 | -47.90604 | 2024-12-01 05:05:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 968d77d9-72a8-35de-8c24-b932dbc0cfaf | 0.34625 | -51.08715 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b688bc70-b0b9-30c9-8d70-598648d64233 | -1.23486 | -51.80481 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a6faffb-0293-3890-a937-acec330db0ea | -1.28813 | -51.72656 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2835357d-ad49-3155-af54-47bd3b64b1b6 | -1.16554 | -53.56579 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92465213-9278-3b73-890b-e3cd3080ed98 | -2.70987 | -52.00209 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bce1764-6dd1-3960-9afc-4bb51c6ec440 | -3.10252 | -53.74953 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| de45ae9d-af40-3cef-ba46-f581b53466a3 | -3.79858 | -58.97482 | 2024-12-01 05:08:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82413efe-2781-3ed8-881d-80fe41d1643b | -1.71716 | -52.63126 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e546dcc-9620-3d73-9667-c3718358e4a4 | -2.84106 | -54.08639 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fbe3f867-c1cc-3a8b-9fbd-12f9723ea548 | -3.27143 | -53.63771 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7a0fe18c-ceb7-348f-8c30-0de678f44f98 | -3.72293 | -54.52813 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74ffdf17-4856-3cae-aeee-cec8438d7352 | -1.33486 | -55.85146 | 2024-12-01 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ddbda38-51d2-3678-a760-6ee6b170fc9f | -1.47883 | -52.34245 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6474ce55-d717-38fc-9a27-b2b8327f3f6e | -4.11261 | -54.23338 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22927f08-b77e-382d-99c4-09adee391c0c | -2.43776 | -53.88502 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04f830a9-6c18-3789-8c6c-0bd9fe38e8e6 | -1.64413 | -55.07147 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c355590-a2a4-3f82-b9ad-2c81eff2235f | -1.62234 | -53.86468 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e5d6f63-6bda-359b-a1b7-95004d7ff072 | -3.22582 | -54.25732 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03635d25-7d8b-3e78-9bd0-6cef38252ce7 | -2.82375 | -54.07332 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 669f22f0-a0f6-3b9e-a2b3-20ac93eb31eb | -3.23607 | -54.16891 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 867ad373-6347-3ae2-8c30-6899f1707db3 | -1.87436 | -53.96032 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cea7131-da33-38c1-aee3-8c0bab323cf2 | -2.80427 | -53.04921 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 987028b7-bcea-3bb5-9ea1-4005344d32c1 | -3.50231 | -53.83093 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c38d097-9f52-3166-8949-f473286cb444 | -3.32248 | -54.17333 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca02e25f-1dd2-3880-973c-9409e0a5e2a2 | -3.24707 | -53.62978 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69791291-81ac-3c18-a320-4ad3ef293dac | -2.98939 | -53.28162 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd9393d1-a8fc-38ac-b996-ebaf4a66a88b | -3.18973 | -54.32955 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b542ed7-a98c-3ed2-a237-67fd45f3b2a4 | -2.88079 | -54.01359 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2390234-50fc-33f4-95bf-934244b22bc0 | -3.06519 | -53.68611 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a10b0d06-a9fe-397b-9d30-98a5883aacac | -3.51473 | -62.7579 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dc6c54e-f11f-3785-b6f6-803a87f2b1dd | -2.57519 | -53.67262 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50c7b896-4ce8-3a67-90c5-afb396fa9ed9 | -2.36366 | -53.65915 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20faffe3-0b1d-3c0b-869e-2650abfac54f | -2.59026 | -54.22184 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a75846a-5a5d-3a0b-84ea-290fd9ac0538 | -3.30822 | -53.86879 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e121864e-b7db-3ce6-8aca-55b675d8de94 | -3.84555 | -52.02417 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50331d87-d021-3f29-8513-1ae286a379b9 | -4.0622 | -51.06722 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5cf08cf-8ed8-398d-96a8-0c0de0de9959 | -2.89073 | -55.21945 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91190310-375d-3fdc-8e0b-70f991e3c9b8 | -2.86748 | -53.98375 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b54432b0-35c8-3a11-9fec-2255e8e5f49a | -2.75311 | -51.75054 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 62399add-1b59-3807-8b1e-b92893e08a3b | -3.74459 | -54.68089 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9780944c-c75a-3941-bc32-07ead1fbc5e0 | -2.5116 | -51.83216 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 671df49b-fe23-3325-a95e-6cd92a6b90bc | -1.36559 | -54.65831 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1b96ff9-39f7-352c-a6bf-247fe51d66da | -4.85874 | -50.71902 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 426ed7a7-2653-301f-9405-66edda054de1 | -3.09955 | -54.02589 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44606e83-434a-3738-9808-fe432ab0e971 | -2.89967 | -53.96084 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9edfe3b3-6165-30c1-b917-9b8d97915ad5 | -2.79699 | -54.22135 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| debfebb4-8280-37c7-90f2-a11c1bfcf26a | -2.39124 | -50.48825 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89f1d6f8-14f4-34bb-a951-4d7daee696b0 | -3.14145 | -53.8474 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c7ad8b9-e045-3c97-bba0-7ec7a270ddd8 | -1.4569 | -54.96664 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bab1ba16-2d60-3d79-9b71-c8a252e0a55e | -4.08116 | -50.0319 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dafa15df-5b16-333f-8c2f-87fa63c9f614 | -4.41265 | -54.98149 | 2024-12-01 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b86106ae-c141-30e4-99fb-ea2757e6ec34 | -2.77397 | -54.02625 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7185241-4400-3836-94d7-39a1ac5b86bb | -2.48379 | -54.02628 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be99086e-fab7-33b4-8803-f7bc6b6ccfdf | -3.00734 | -53.2371 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f51a856a-a92f-3ec2-b8a9-b2fe5911aa16 | -3.06102 | -53.68958 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87db365d-91b6-3740-9386-5b8362b19868 | -3.22034 | -54.17836 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README76.md)
