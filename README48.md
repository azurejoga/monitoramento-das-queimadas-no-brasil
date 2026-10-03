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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6fffe90-4e2f-3eb2-bcc2-23654a0d90ae | -10.9879 | -59.1393 | 2026-10-03 14:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 526d11df-edfa-37eb-8bf0-ceb5101d34fa | 1.9132 | -55.8011 | 2026-10-03 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 4e30f901-2422-39e7-8abc-7691a75e392f | 1.9315 | -55.8205 | 2026-10-03 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 54997941-37eb-39c5-8d09-fa3387181eff | 1.7853 | -55.6251 | 2026-10-03 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 90cf123e-4bfe-3b09-aed4-260b7415cdbf | 1.7854 | -55.6054 | 2026-10-03 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 37106522-361d-3b6c-8a63-4554c5bad5f1 | 1.9133 | -55.7813 | 2026-10-03 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| a00376d6-a1e4-3d47-88d9-cebf5a020307 | -8.8705 | -66.7822 | 2026-10-03 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 294b71fc-0bcf-3a07-8c9a-c6c43e003935 | 1.9132 | -55.8208 | 2026-10-03 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b3714bc4-4dc9-352a-932e-0fc34d54ee6d | -8.852 | -66.7827 | 2026-10-03 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| aa477ccb-9758-3389-9817-618c6768769e | 1.9793 | -50.84 | 2026-10-03 14:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a98ebd52-5407-3dc4-a4c3-3821f60c8ab4 | 1.7041 | -60.8399 | 2026-10-03 14:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 3eda28fc-1a2e-33f0-9699-c71e1976ee41 | 1.9316 | -55.8008 | 2026-10-03 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a5e7cd6b-2475-3a8a-9b26-03c767879441 | -13.31 | -42.39 | 2026-10-03 14:15:00 | MSG-03 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2c4ef430-f88e-3b47-946e-624cc49cfe29 | -4.19 | -44.28 | 2026-10-03 14:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4961ac35-cb28-361b-942a-0e0c4803c07e | -13.34 | -42.4 | 2026-10-03 14:15:00 | MSG-03 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 18df02fa-ab13-3544-bb1a-a4c749553de5 | 1.7854 | -55.6054 | 2026-10-03 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 48354550-dec0-3695-9c79-2764d2e7913a | 1.7854 | -55.5856 | 2026-10-03 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 75d48fa2-c808-3a82-872c-2edc0284bbb7 | 1.7853 | -55.6251 | 2026-10-03 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b4ec10bb-c81c-3931-9645-c109dd872c5f | 1.9315 | -55.8205 | 2026-10-03 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 2fe1d514-c97e-3b91-ba9b-64d7872c02a8 | -8.8705 | -66.7822 | 2026-10-03 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 017607eb-8401-3199-b9ae-4c036c647379 | 1.8037 | -55.5854 | 2026-10-03 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f6ab405f-8ddc-34d9-944e-84c8f4f98ed9 | -10.9881 | -59.1197 | 2026-10-03 14:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b01d0e3b-0b49-3aec-ac6c-3d209f9fbf0b | -11.269 | -54.0334 | 2026-10-03 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| acced2b8-2f62-3308-85bd-bff806530070 | -10.9879 | -59.1393 | 2026-10-03 14:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 205.3 |
| cd8c2cd1-6a18-35d7-b530-f38ee43321cf | 1.9132 | -55.8208 | 2026-10-03 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 7fa45937-361b-3220-a5f8-b94b3e868e40 | 1.9132 | -55.8011 | 2026-10-03 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 865eeec3-beac-3772-9072-33cd00c550c7 | 1.9316 | -55.8008 | 2026-10-03 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 70ce09d8-2fa0-3590-9f0c-4de2d90774c0 | 1.9132 | -55.8208 | 2026-10-03 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 9b508a36-cdc5-3dfb-9e83-8cb83b350c4b | -1.1533 | -48.978 | 2026-10-03 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| b92ccc77-0f03-31a2-bec6-b99622a65d86 | 1.8037 | -55.5854 | 2026-10-03 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 4a7d9ee7-abf3-3986-894e-ce63cb7bd4e8 | 1.8692 | -50.6753 | 2026-10-03 14:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d9224cee-8e28-334a-bceb-a9c5552efcdb | -10.9879 | -59.1393 | 2026-10-03 14:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 274.3 |
| cb765d30-220a-3b96-acbb-0a15eb7a57e9 | 1.9132 | -55.8011 | 2026-10-03 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 873315ee-81a6-3bb4-9b93-2c46d6e8ccfd | 1.8038 | -55.5656 | 2026-10-03 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 682899a8-ae9e-3150-91ba-064387b44094 | 1.9316 | -55.8008 | 2026-10-03 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| ae11d791-4957-3cfb-b7c7-ffda2634fd9a | 1.9315 | -55.8205 | 2026-10-03 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 706aa3c1-8b27-3242-ac3d-cd153cce15f7 | 1.9133 | -55.7813 | 2026-10-03 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b3e4c79a-1e27-3a31-a874-b856a8b56e9e | 1.8037 | -55.6051 | 2026-10-03 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| df100619-3cc9-37fd-949c-65be5aff5299 | -1.0423 | -49.2134 | 2026-10-03 14:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f781b902-ce80-3e5d-b6e9-31e3edf815d5 | 1.7854 | -55.6054 | 2026-10-03 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 155.4 |
| 309bf43f-3680-3f8f-aa34-044b30518700 | 1.7854 | -55.5856 | 2026-10-03 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| bc213ed1-d255-3784-a7d9-6d85198094d2 | 1.7041 | -60.8399 | 2026-10-03 14:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 63365d8a-8cdb-35db-a0ea-982daebc6e6b | 1.9132 | -55.8011 | 2026-10-03 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 760b5d86-3595-30ea-a22e-999c566122e3 | 1.9316 | -55.8008 | 2026-10-03 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a2c1fef2-2621-3282-b46c-01fa20275bc2 | -10.8187 | -57.2192 | 2026-10-03 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 9e453cd7-0fba-3a3b-8a2c-d241376c37f0 | -5.1388 | -42.961 | 2026-10-03 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 855134d3-9a2a-321a-b2a6-8aa11c9ba838 | -11.3823 | -54.0434 | 2026-10-03 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| c56cc251-4f4b-3092-bebe-c74ed3008754 | -10.8189 | -57.1993 | 2026-10-03 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3ab92b86-863b-3601-80c5-cc2234934d28 | 1.9133 | -55.7813 | 2026-10-03 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| cc9ca602-2ddd-3646-b147-06eded9a61dd | -10.9879 | -59.1393 | 2026-10-03 14:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 347.6 |
| 163e957b-e028-3293-8253-9d0b29956b56 | -9.0046 | -65.6988 | 2026-10-03 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| edd2ff96-e931-3e9f-a102-380ada6ac717 | 1.9132 | -55.8208 | 2026-10-03 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 7127b221-bad8-3091-8847-b820bcbea2d9 | 1.7853 | -55.6251 | 2026-10-03 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| dee9a288-1391-3233-8ebe-e5529d81a5eb | -1.0911 | -54.1001 | 2026-10-03 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6d84cfa6-1807-3f20-97ac-55b2ad0338a3 | -2.185 | -49.7665 | 2026-10-03 14:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 0ae2bc56-c123-3459-8d5b-6e3c385fb338 | 1.9133 | -55.7813 | 2026-10-03 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 37d086d7-9e65-30a4-aca9-d1843cbaa80b | 1.9132 | -55.8011 | 2026-10-03 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 8395ea10-8f16-34d7-981b-9686fb085f8c | -8.6665 | -66.936 | 2026-10-03 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 681e7159-27e2-399a-811c-abc5c20e1ca8 | 3.36 | -51.3454 | 2026-10-03 14:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 0a8b62b8-0609-367c-9d53-c96105a1ace1 | -9.9175 | -65.0313 | 2026-10-03 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.9 |
| aad37aaf-22ed-39e6-924f-f3770b1f867d | -1.0423 | -49.2134 | 2026-10-03 14:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 58cafaf3-b4a1-3213-9d59-fef80188da16 | 1.8037 | -55.5854 | 2026-10-03 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 5f8c1248-ae05-34c5-b61b-f937e73ff99a | 1.8038 | -55.5656 | 2026-10-03 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 430d4b60-c872-3e60-ab07-945b34c79b36 | -2.8167 | -48.6653 | 2026-10-03 14:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| d7a9e7d5-a9b7-34ec-9769-f455df5257a8 | 1.8037 | -55.6051 | 2026-10-03 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| eea5bedb-1295-36fd-a313-e0271c2ff823 | -9.0046 | -65.6988 | 2026-10-03 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| b4cca5d6-bd8d-3e85-bdc8-285e5b07f988 | 1.7854 | -55.5856 | 2026-10-03 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| c37cb935-d781-3bd3-80f3-68b6f06bf201 | -1.0244 | -48.8087 | 2026-10-03 14:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| eb0befc6-0392-39fc-9f7e-950248df7894 | 1.9132 | -55.8208 | 2026-10-03 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 8abb14f4-0ba7-3570-95f8-00e0fe7e821d | -9.0232 | -65.6982 | 2026-10-03 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| ce1cb13b-7494-374c-bc5c-258339495804 | 1.8038 | -55.5656 | 2026-10-03 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| c473b7c1-f0af-3ed1-a3ee-46650bfc8b8c | 1.9316 | -55.8008 | 2026-10-03 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 989f8604-ce58-32ee-bf3d-e1edc6ccd928 | 1.7853 | -55.6251 | 2026-10-03 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 41592a16-f857-3c64-b922-ac24b7acb518 | 1.7041 | -60.8399 | 2026-10-03 15:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 658888e9-b6b5-3b9f-843f-afff7ab452bd | 1.9608 | -50.8612 | 2026-10-03 15:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ffa7b4c7-cf6c-3db1-b626-27abbf1a9bf2 | -12.1967 | -57.1103 | 2026-10-03 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 14d872c1-4f1d-3f17-96bb-f394c3404b95 | 1.7854 | -55.5856 | 2026-10-03 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 37f776a3-36e5-376b-8faa-293cf7d17f0e | 1.9609 | -50.8404 | 2026-10-03 15:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 71.4 |
| fd840f9b-95c1-3782-aaad-00b27d513c05 | -9.7319 | -64.9631 | 2026-10-03 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c1fab4f0-c64d-3189-b59e-9e8d70366afa | 1.9608 | -50.882 | 2026-10-03 15:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 236b1839-fa7c-3d25-bea6-99539c852c77 | -8.3903 | -62.6963 | 2026-10-03 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a376a1dc-53f9-3f04-81c7-8253908460ab | -8.6665 | -66.936 | 2026-10-03 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.3 |
| ea29d812-ab5d-3d87-ae58-1798257a60db | 1.9315 | -55.8205 | 2026-10-03 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| baee5b4b-dca3-35be-87b5-a0b278ccd1f1 | -1.245 | -49.3172 | 2026-10-03 15:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 623396d4-f94a-30db-9882-6da6257406a7 | -9.0046 | -65.6988 | 2026-10-03 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 17935dce-52b0-37d1-8521-5667aebdaa86 | -1.1897 | -49.2966 | 2026-10-03 15:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6197dd18-8e13-3c8f-8559-0b623a24554a | 1.7854 | -55.6054 | 2026-10-03 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| ce316360-764e-3513-8bee-03bc9b42a388 | -9.0232 | -65.6982 | 2026-10-03 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| ae679a97-0359-3637-971d-3f1354245a67 | 1.9133 | -55.7813 | 2026-10-03 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 66fbdc51-ee7c-3e40-a2d2-ec25337a8d7f | 1.9424 | -50.8616 | 2026-10-03 15:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a92785f0-d949-3b4e-a5cd-459ae6b90f60 | 1.8037 | -55.5854 | 2026-10-03 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 69c4fa08-4687-3702-9786-e0fde494d862 | -2.185 | -49.7665 | 2026-10-03 15:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 8ad7cd9e-a99a-3480-9826-dabb3bfe74bf | -1.1348 | -49.0421 | 2026-10-03 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d97a06dd-fa4b-3fba-818f-34bef6b209ae | -1.0244 | -48.8087 | 2026-10-03 15:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f2048725-6af3-387f-b80a-203b222e0a45 | -9.9175 | -65.0313 | 2026-10-03 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 773a580c-83f8-3216-8f68-8521a8a7b960 | -9.0231 | -65.7169 | 2026-10-03 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 60bf0b63-e8ba-31b7-b608-2fdb6798cbc5 | -1.0423 | -49.2134 | 2026-10-03 15:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 20993633-8a09-33b3-97ba-0750342bc8af | -3.1061 | -50.2686 | 2026-10-03 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| df18c958-bdaf-33be-ac08-83796bf1f8ab | 1.7399 | -50.8235 | 2026-10-03 15:00:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 5c7d4dec-cd29-317d-b5ec-c56029521f96 | 1.9317 | -55.7219 | 2026-10-03 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |


[Clique aqui para ver as próximas entradas](README49.md)
