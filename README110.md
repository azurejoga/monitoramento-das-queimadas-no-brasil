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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 145a7a62-42a9-3912-b1ad-5cdf91e439ae | -2.87775 | -51.68053 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bc3a6ff6-24cb-3205-9185-02459b2ab99b | -2.87745 | -51.38257 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 443e281b-2361-3ac5-9dda-d2202b495535 | -2.87488 | -51.66186 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad2ab362-cfe1-36c7-9bd6-f83c081308de | -2.8745 | -51.66209 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6579fce8-f15e-3766-ba5a-13f4bc1ce9a4 | -2.87435 | -51.66544 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 424f9cb9-bbe4-3dff-9235-438e00a8af77 | -2.87395 | -51.66567 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0c6f061-93ba-350f-9772-e5fbad07b003 | -2.87383 | -51.66901 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 94ecbbef-9a0e-3dd7-bd26-4a56e79dac70 | -2.8734 | -51.66922 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| edb5882c-bbad-3081-b7ba-249f15bb117a | -2.87331 | -51.67257 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ef389786-93c0-3f14-a745-5450b07ede55 | -2.87285 | -51.67277 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c6fdeb00-1ab6-327f-bdef-54f58dee6760 | -2.87279 | -51.67616 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2a693b82-e2ab-377a-929a-456cc71cdcc8 | -2.8723 | -51.67635 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d65b0175-7426-3fd4-9376-0ea50d9ba92b | -2.86886 | -51.66467 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ec29ee47-9ef5-3a33-a323-f8f66f6c91d8 | -2.86845 | -51.66489 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c511ead8-d3be-35e0-bff2-58c77b31e21e | -2.86834 | -51.66818 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e2ed0978-82c2-3719-9d1d-0daa79276ce5 | -2.86792 | -51.66839 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 482fff22-cc25-3031-94c8-ece1c0d684e3 | -2.86783 | -51.67171 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 20e0a195-f720-3707-b3d8-0f98fbb78887 | -2.86737 | -51.67193 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8104959e-f5f4-3943-981c-8fa9a9a97707 | -2.86731 | -51.67529 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e2559418-2ef2-3069-96c4-329380cfe5cc | -2.86683 | -51.67549 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ac41764f-c7a0-3dc5-a1aa-ecb4dc2da9c2 | -2.86286 | -51.66732 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 06c0a11e-f63c-35a0-b890-634ea2b0400e | -2.86243 | -51.66756 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34b999ef-4884-32ca-8bb9-56949f4f1b83 | -2.86235 | -51.67086 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ac021d76-1127-3934-bb41-3f52c8d644c0 | -2.86189 | -51.67109 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2eed66d2-a21f-3eb9-93c9-97b25fcfd35f | -3.29985 | -50.66415 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c75d52e-7456-387d-a6a0-59158a5caddc | -3.29922 | -50.66843 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3483f403-fed5-31db-952a-bb3ff6c6d0d6 | -2.58134 | -51.92226 | 2024-09-27 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38dc9bcf-9d6b-3b24-b81b-39a9e32a26ac | -2.40529 | -51.29511 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 906dfd6a-7f4d-3013-9021-579bfc322413 | -2.4008 | -51.28685 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 759be30f-409f-3fe5-a6aa-2ca8d012c757 | -2.40025 | -51.29059 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccd0c5ce-00fb-33a0-8d6f-b2fd662ca2f9 | -2.3997 | -51.29432 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2948685-a04a-3eb6-88d8-a5e79924ab0c | -2.39717 | -51.2822 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc86c606-df79-3bb9-9b05-85e58247607d | -2.39659 | -51.28594 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d812a36-9213-3f82-a411-05b2a3852ea2 | -2.39601 | -51.28968 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 551c8a19-759e-3063-8388-c39ac38a4795 | -2.39576 | -51.2823 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92836b4f-2288-33b5-b926-a7061a226e14 | -2.39521 | -51.28605 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e607d58-9529-31ef-bf9e-e8fc282a25a0 | -2.39466 | -51.28978 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88a105fc-80ef-3f8b-b3e9-e4902c558840 | -2.39157 | -51.28141 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8020c10d-89ab-3e8a-89ed-e3b231bd4880 | -2.39099 | -51.28514 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afb2e082-a554-3da0-9790-da0c299d5ff0 | -2.39072 | -51.27774 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16ebc38f-2f18-346d-be7b-80a65bf8bbdf | -2.39042 | -51.28888 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cc84578-6eb7-393c-8599-b42bcf0ce884 | -2.39017 | -51.28148 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76f75b4a-3840-36be-b444-306b3b28d1ce | -2.38962 | -51.28521 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed6f2b89-b15f-3b51-b268-71811fd97305 | -2.38598 | -51.28062 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e7eb828-62e0-3300-83aa-5c82f5b3482a | -2.3854 | -51.28435 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e26ee96a-5666-33de-bdcd-47ae876dd427 | -4.61323 | -50.96234 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00942853-ecd1-373c-bf27-07954212af24 | -4.6126 | -50.96671 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0810a3cf-2a44-3ebb-9aa4-493256e85513 | -3.88375 | -51.92567 | 2024-09-27 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81959259-0566-30e5-930d-d6aef22ce83b | -3.87826 | -51.92499 | 2024-09-27 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f26b53e2-60dd-3c7d-abed-2cd5375ba298 | -3.87223 | -51.16574 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aec76c10-324d-3d5c-b310-915bfe574768 | -3.87164 | -51.16971 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d311a25a-1b2f-3bcd-bf85-df855ba9dac2 | 0.90681 | -51.99709 | 2024-09-27 05:25:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 18f5b90f-18f4-397f-8ea5-5ccc0a056e24 | 0.90638 | -51.99439 | 2024-09-27 05:25:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f8e297d3-1067-37e2-b6c4-528c7282a3f8 | 0.90596 | -51.99176 | 2024-09-27 05:25:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a11c07c1-23c1-3a5b-a311-930bb07e71ff | -3.39417 | -53.71634 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f041502c-c315-366c-907a-1c99384e0307 | -3.39333 | -53.72184 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1513ac16-2714-3b05-ab8b-8cb1fc71279b | -3.38938 | -53.71552 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 746cdbc4-7ee3-3ec8-a877-fd751e987634 | -3.32545 | -53.2239 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1fc5d13-3983-36b7-a184-12275f52c14d | -3.3246 | -53.22958 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7476c12a-f412-313b-b80e-eaed8a63a028 | -3.32214 | -53.212 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07e77695-5cb9-3c22-a805-cf6ebc0b383f | -3.32132 | -53.21751 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cc804ad-91ae-342d-99f7-0a1d8688ea03 | -3.30811 | -53.37404 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9eae7cdd-98d2-303e-a271-5edc0509a4f9 | -3.30418 | -53.69347 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d401138-3023-32d3-931d-d7b5df65c6da | -3.30392 | -53.69773 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f12d382-a89a-3a81-9c47-0658aa962218 | -3.30343 | -53.69864 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83b656e9-e397-3096-ab65-2024743b42c4 | -3.30319 | -53.37336 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4e1334c-d287-3ec1-8d83-a0ec3db671bb | -3.30314 | -53.7028 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c96519ad-f0af-35e2-be1e-dfbb093f03d9 | -3.30269 | -53.70373 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb97d557-1f96-342a-9046-acfb45fe3977 | -3.29983 | -52.98705 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94a2da21-7b5b-3e49-949e-adcb6764d91d | -3.29911 | -53.69703 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cced26ef-e552-3d52-9480-657f607caecf | -3.29862 | -53.69795 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff4113c5-c1c3-30cb-b75c-cfc03eae73ce | -2.86125 | -53.31773 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29db920b-477a-3a14-849a-298d709f1b7d | -2.85634 | -53.31703 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d59790a-163d-3349-8d73-01a5317c4e6b | -3.82345 | -52.29236 | 2024-09-27 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f5a282f-ee76-3253-b884-2b7a63cbab7f | -3.63066 | -53.60898 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ebbe80c-d219-35e4-a2fb-4a5198ee7593 | -3.59142 | -53.47046 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4f189c2-2236-34b8-9649-64cbda0f1b14 | -1.19287 | -54.21091 | 2024-09-27 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c5b2ee4-5b00-3226-8b8c-65d98351cb0b | -1.19084 | -54.20845 | 2024-09-27 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42bb7825-6b85-3b3c-ba67-f67eb7cf8435 | -1.19016 | -54.21293 | 2024-09-27 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1bca082-27ae-3899-b3c8-87245488bc00 | -1.18838 | -54.21022 | 2024-09-27 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7358b1bc-4d8a-3bb3-9fb6-2320169caaf9 | -1.18635 | -54.20777 | 2024-09-27 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d177626-05a4-334b-a084-7facfe85964a | -1.18568 | -54.21222 | 2024-09-27 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79942748-1a92-358c-90e5-433827001307 | -1.17818 | -54.15833 | 2024-09-27 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a43d5b95-7648-3a80-822d-1a1480659ace | -1.17748 | -54.16278 | 2024-09-27 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc29d525-bb36-3f97-b78d-ceed6ab24acd | -1.04915 | -53.36045 | 2024-09-27 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac4993ec-f943-3bb3-996d-d979c304c457 | -0.94535 | -53.72976 | 2024-09-27 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0c8c6e3-691f-3a74-aae1-9713fbf830c1 | -0.94491 | -53.72745 | 2024-09-27 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e00bfb35-ae95-34c7-b4af-79beef318e88 | -0.94416 | -53.73242 | 2024-09-27 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5d1d0f2-fe7b-3b99-a008-ec71f2623f66 | -3.64357 | -54.04274 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e12d2bf9-ce25-3112-9241-65ef6e770dbe | -3.6428 | -54.04789 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e884fd15-dc47-3a97-ac75-81e19e5c8cc6 | -3.63888 | -54.0419 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7512c1f4-7624-33f2-93df-6bda5e59ecbd | -3.63811 | -54.04702 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fe0f4f59-c129-320e-8c9e-dc8bbbf7ae59 | -2.76529 | -54.77306 | 2024-09-27 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 79fb3665-c479-3fe7-8142-b33b13f94562 | -2.57505 | -54.57359 | 2024-09-27 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29c5b3ae-8197-377f-bdb0-435197d51485 | -3.35519 | -53.7798 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b05906f8-8d70-38e2-8b40-eb58efd0887d | -3.35445 | -53.78475 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fe3d72d-98a6-3734-b51f-50f530765db8 | -3.35041 | -53.77905 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef7ba76d-d42a-3f9a-84cf-5127458237f3 | -3.34967 | -53.78402 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5faf730b-a55b-316a-994d-84afaab2c36b | -3.34489 | -53.78327 | 2024-09-27 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 44fc046d-fb38-3d87-b7eb-a7a0cff1a2e0 | -2.95806 | -53.7192 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README111.md)
