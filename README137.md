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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 705357e0-33f6-3970-b6c4-d7cb68110e3d | -3.25438 | -54.18513 | 2024-10-12 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4a1f47d-6dbf-3586-8b3e-bea12ce34d6e | -3.25394 | -54.19909 | 2024-10-12 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c620f625-70ff-3dd3-8485-e5e640fe28db | -3.25354 | -54.19065 | 2024-10-12 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 678cbcdc-bdaa-3115-8917-4437dc0d48da | -3.25274 | -54.19595 | 2024-10-12 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f87afb17-078b-3aec-b6ba-5e8553a635a9 | -3.24905 | -54.18756 | 2024-10-12 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14644096-a686-31f3-9285-2e1cabd92416 | -3.24829 | -54.19284 | 2024-10-12 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b97a6aa1-2df6-355f-adde-a6075e70eeb5 | -2.95915 | -54.12381 | 2024-10-12 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ad8d115-1d29-33ab-ad8c-2f082ddd2aa0 | -2.80461 | -54.08638 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cc45d17-af83-379f-8a80-c58dd407de45 | -2.79819 | -54.08543 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90ea74ba-74b5-3a37-8724-a402c9a44d71 | -2.78919 | -54.01372 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 23648d92-631c-342e-98aa-b47d3a5ead1a | -2.78839 | -54.01909 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7bf56630-c2ed-3e54-88f0-58149f9ab551 | -2.77958 | -54.03411 | 2024-10-12 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27f35cc5-7d6b-338f-b68c-1dd76637c7ea | -2.57751 | -54.26703 | 2024-10-12 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 604a935a-f4cf-3eee-96ed-cba131e7f577 | -2.57117 | -54.26617 | 2024-10-12 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57a74276-ef1d-312c-8261-1061db11984d | -2.10445 | -54.69786 | 2024-10-12 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8da161be-b081-387f-bc19-ae86d6a9700b | -2.10377 | -54.69908 | 2024-10-12 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a19404fc-7141-3440-ae94-d09faa1cba31 | -2.10376 | -54.70253 | 2024-10-12 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 648f5fda-89f3-3e3c-b499-ec5bdc6554c8 | -3.95225 | -55.34834 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ecb0702f-19f6-3022-9b90-4175f4ac2bc3 | -7.87761 | -54.71576 | 2024-10-12 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 01dcee22-0bc1-31e0-85e6-d058bf611352 | -7.87102 | -54.71482 | 2024-10-12 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 72990416-271a-3cce-ab34-a9f043b9c10b | -7.87033 | -54.72024 | 2024-10-12 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3341c67d-3b83-30c7-8b19-beacfe39a3ba | -1.66654 | -55.13844 | 2024-10-12 05:46:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55145f6e-94c2-35d0-9d3d-d2d4fde3a205 | -1.66588 | -55.14277 | 2024-10-12 05:46:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14c9a225-7457-3309-8b4a-87cb88d3bec5 | -1.52786 | -55.42111 | 2024-10-12 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d37b5d3e-b2d1-33a7-98f5-d2e5755a39ae | -3.6009 | -55.46029 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c74cbc8d-a2e0-3bb9-9bd0-2d6e0463a525 | -3.59831 | -55.45798 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 104db662-05ad-373c-80c1-3df33359cf86 | -3.59767 | -55.46239 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fec204c-3c67-3eb2-afbe-4bd08759e962 | -3.59495 | -55.45942 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 621fa5c3-6743-3c10-a766-48760dd118bf | -3.59429 | -55.46377 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9956c6bf-cf82-389d-b8a5-9e42d96c48a7 | -3.59238 | -55.45692 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd78a0b9-f6e6-3e73-8557-df9c30912c7c | -3.59175 | -55.4613 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edfdb8a5-06cb-3253-850b-41966d139175 | -3.58525 | -55.56377 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4869308-5f1d-33c1-8f24-84ce75f8f169 | -3.58455 | -55.56841 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f48fe56-a2ea-37db-8823-283ce3c5285d | -3.5124 | -55.44211 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 677de355-3635-39f6-80cb-80604e54abb2 | -3.51177 | -55.4465 | 2024-10-12 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb1826f4-87f6-3f0a-80ec-94789bd8d1e4 | -4.85244 | -56.18323 | 2024-10-12 05:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0ed74de-7a85-3bd6-b5b2-2acf2fd5b810 | -4.852 | -56.18158 | 2024-10-12 05:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c7b129a-1d32-3012-bd35-6af1d14e2a98 | -4.85142 | -56.18555 | 2024-10-12 05:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bf2dd90-1106-3f17-b490-6aa00d6bd7f6 | -4.6061 | -56.11967 | 2024-10-12 05:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0e53e39-0c4e-311b-8633-ededb9946df8 | -4.60552 | -56.12368 | 2024-10-12 05:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c42fe69-522f-3890-80e9-1495cc753b9f | -3.99406 | -56.08393 | 2024-10-12 05:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bbe8315-eb20-3c96-85d0-811815c000bf | -3.99349 | -56.0878 | 2024-10-12 05:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7ab3a9b-bafb-318f-896c-9b8b3ab91c6b | -5.18046 | -56.00105 | 2024-10-12 05:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 763defa7-3d3b-3909-8a8a-d00c28c0c6ab | -5.17453 | -56.00057 | 2024-10-12 05:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1b3255a-cdb6-350c-8840-160ed636e7cd | -3.44279 | -57.97433 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dbb0f87-2751-32c7-9faf-e4088393041d | -6.47473 | -58.43678 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bfa65c2-a3cb-3420-9add-7c4932143c54 | -6.47431 | -58.43969 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac5d4f80-0561-3be6-b243-b92d22647951 | -6.47293 | -58.43816 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5f8fd90-9f3f-3b9e-9313-7d395419853a | -6.47254 | -58.44105 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50ef5c6e-ff2a-376f-bf9e-9b6fe6f0541e | -6.35205 | -58.17915 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 644c0cc1-4388-3cce-8d2c-80b1e8bbed7b | -6.35161 | -58.18227 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3fd4828-27e8-34fc-8c0a-d785e47332c7 | -6.35117 | -58.18539 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d71c92e4-2f76-3d59-a27d-8b3927a76ed7 | -6.34775 | -58.17221 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d4f09f1-aa6b-3d74-bda6-2fdbc77176b1 | -6.34731 | -58.17532 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 360b71a0-d7dc-39c8-b315-7e29543fbde7 | -6.34688 | -58.17842 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a73982a-d95b-371d-9d7a-517df227cae3 | -6.34644 | -58.18155 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48261895-bf88-30d5-b3ed-9d8e7528efb9 | -6.346 | -58.18467 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 413bae57-ba2f-3467-84c0-694155bed748 | -6.34214 | -58.17459 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 429007e3-74ac-37da-a1d2-081151e887d0 | -6.34171 | -58.17769 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 267789fa-738f-3e45-886e-dfd27d036417 | -6.34128 | -58.18078 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0b24677-2581-3616-b6c3-20088c314d06 | -6.33686 | -58.32398 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bc23e9b-9a92-3410-9f4e-804e189a01f6 | -6.33175 | -58.32322 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c651515-fbc7-3179-9d5c-dfd73b0fa8e9 | -6.33132 | -58.32626 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 636b0c9c-371c-3851-8b46-526bf97e452f | -5.95941 | -57.69387 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e9889a6-fd15-3492-9625-a386abdacf4e | -5.84539 | -57.70425 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ba108d8-d093-3cd8-ad5d-8b724a219346 | -5.84105 | -57.69655 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5de66aa8-7614-3644-ac17-57db6588395d | -5.84059 | -57.69985 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31e0c34f-3cb3-3951-a63a-9af4c4d85080 | -5.83702 | -57.69555 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32108485-2a8e-3344-a9d6-3dbbbcdcb45d | -5.83623 | -57.69227 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11ad90b3-39dd-37d0-ac43-ed139ddc08ff | -5.83577 | -57.69556 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63cb29e6-2da0-3ff5-a878-a9eb81cd4088 | -5.80465 | -57.73249 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 144b12fb-49e3-3ed0-8355-d93a904905c4 | -5.80419 | -57.73566 | 2024-10-12 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 031f1501-e69e-325f-a857-f9c6d439ed08 | -6.86897 | -59.07941 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4681183e-9d30-3207-9629-fd842cfbf990 | -6.86818 | -59.085 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a7ed1a4-54f3-3535-be34-53ca194156cf | -6.86563 | -59.06765 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e698424-072c-34cb-b96e-5a1fc1da9a82 | -6.86408 | -59.07863 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c455a57d-a75a-3ce7-9e35-d5d1892fd3c1 | -6.8633 | -59.08425 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be168f84-4f7e-3f03-adbc-1c3390299809 | -6.86252 | -59.0898 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a53a7a8-16b5-313f-ac62-73bb37140237 | -6.86176 | -59.0952 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe898535-6736-3928-afed-15f71111351a | -6.85764 | -59.08898 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2d9e2eb-229e-3d09-95f6-a8ff3aa5babc | -6.81395 | -59.04362 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25f128b9-3ccf-3b1a-97d5-07a33632237e | -6.81185 | -59.04145 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b216b8db-f9aa-379c-a282-be39f4e68bc9 | -6.74907 | -58.88034 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3efb59ca-7d9b-3aa0-8a50-0dfb20584322 | -6.74821 | -58.87904 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1453f937-41d7-3ee3-bd62-b2cb1e700177 | -6.74735 | -58.88494 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98503701-2b54-30dc-a9ad-6dceed00fca9 | -6.74409 | -58.8798 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f4a9fef9-f1f1-378b-9511-dfe7b0aec96b | -6.74329 | -58.88556 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22dcb617-8c37-36c5-9581-b3048fadbb12 | -6.74324 | -58.87844 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f53755e0-b365-3114-a4d4-8470e9b25dc3 | -6.74241 | -58.88416 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 194aed41-769c-377f-bfe4-bdd5f4ba0fc6 | -6.67086 | -58.78135 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76aa795b-545e-345a-ba4c-3abe6de59e0d | -6.52509 | -58.39929 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d344d8a7-6d81-3e17-ba5e-ba7b30e11f0b | -6.52465 | -58.40238 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be8e1837-eb56-3a6d-8924-3ea545fbf010 | -6.52423 | -58.40543 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0351d31-acfa-3502-8852-a6b94fd598b3 | -6.51911 | -58.40479 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6d5b3c3-4c09-36b4-8ce8-c8bd41b286ce | -6.51869 | -58.40782 | 2024-10-12 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d913c5ea-4698-32ed-b2ed-229383a9acf9 | -3.4443 | -59.6184 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6974baaa-e485-33b5-9563-9541abf42cd5 | -3.44364 | -59.62283 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7536da27-7859-3fa7-aab2-f971c9cebb3b | -3.44049 | -59.61331 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34928c23-e07f-330e-96b1-f02329ce3dfc | -3.43982 | -59.61774 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8bd0e360-5ab8-3f44-949f-be3099353cc9 | -2.86407 | -59.56548 | 2024-10-12 05:46:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README138.md)
