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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7e602b1-53d9-3d71-aaf0-f68a9343bc9b | -12.485 | -63.219398 | 2024-10-18 01:39:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9e8ea6c-95e3-3234-903d-07f5f258df8c | -12.4866 | -63.226398 | 2024-10-18 01:39:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 15610f4f-3879-3293-946e-90a653338657 | -12.496 | -63.268398 | 2024-10-18 01:39:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f1e6d3ea-ca8f-3073-a8c6-7aaffcb5775b | -12.4976 | -63.275398 | 2024-10-18 01:39:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9f2ad2b8-7485-3ffd-a30b-10c0de65adc9 | -12.4992 | -63.282501 | 2024-10-18 01:39:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0f9ef9f2-e75a-32a3-8e65-478bea40eba7 | -12.5007 | -63.289501 | 2024-10-18 01:39:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a045dccf-4270-375f-bb2d-daceac6323fd | -12.5023 | -63.296501 | 2024-10-18 01:39:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b6dc1eaf-24f5-391c-bfdd-6eaede1ff2dc | -12.5039 | -63.303501 | 2024-10-18 01:39:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93a2a0ca-13a2-35ee-a957-42ab6921f1c0 | -12.4862 | -63.270699 | 2024-10-18 01:39:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 143ae019-bf0a-34c2-ac7e-6e2ee0d10dfe | -12.4878 | -63.277699 | 2024-10-18 01:39:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e6be0a1f-1149-382d-8fa5-b1d4dabb48ce | -12.3728 | -62.949299 | 2024-10-18 01:39:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 207969af-0532-3c4d-adf0-7d7ac92cbd3b | -11.9696 | -63.0354 | 2024-10-18 01:39:32 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9514136f-4d92-39a9-aa6e-eb93a90d50d4 | -11.9712 | -63.0425 | 2024-10-18 01:39:32 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d991ac18-bc8d-354f-a599-966e59e271ac | -10.5531 | -67.797501 | 2024-10-18 01:40:11 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| bce809fb-c193-3020-a992-87ae028e5f50 | -10.555 | -67.806396 | 2024-10-18 01:40:11 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5bc25fba-4aa4-3c5b-b20e-66a5da9c0aa1 | -10.9097 | -69.504402 | 2024-10-18 01:40:11 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e5c47f07-be05-3048-b93e-cfbb8183ea80 | -9.8692 | -64.882301 | 2024-10-18 01:40:12 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f28c8adc-0ee3-3525-bb8d-3e558205069b | -10.8803 | -69.510597 | 2024-10-18 01:40:12 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 287f9e80-3c0f-37a3-9afc-3e149006d6c2 | -9.8574 | -64.7826 | 2024-10-18 01:40:12 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c4f540d3-a045-3588-92c3-388dfe587dd4 | -9.859 | -64.789597 | 2024-10-18 01:40:12 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c7735ad7-ad8c-3437-8452-cbb8cac77fbe | -9.8806 | -64.887001 | 2024-10-18 01:40:12 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f9a73710-f305-37a4-82a5-db87c0388fd3 | -10.639 | -68.545197 | 2024-10-18 01:40:13 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 2fbcddd3-6a00-3222-91d6-282df8230991 | -10.4193 | -67.891098 | 2024-10-18 01:40:14 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 89e03e2e-83b5-3032-98a6-59156ad442ec | -10.5427 | -68.525002 | 2024-10-18 01:40:14 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d074840a-4374-31cc-a981-03b21d101a8a | -10.5447 | -68.534698 | 2024-10-18 01:40:14 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7ed09659-a020-34f1-8203-4b0750e2d458 | -10.539 | -68.556198 | 2024-10-18 01:40:14 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 20a62e61-e9fb-3668-a906-2387abfe95ba | -10.3937 | -67.915298 | 2024-10-18 01:40:14 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a9bd3537-5251-36cd-9f2e-a4f829b17f50 | -10.2919 | -67.725098 | 2024-10-18 01:40:15 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c1bd1699-6fb9-3954-ab03-0902625330ff | -10.2938 | -67.733803 | 2024-10-18 01:40:15 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6b4e507e-9efd-371a-841c-4cab6c093a94 | -10.2954 | -67.983101 | 2024-10-18 01:40:16 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e25093fb-4f23-3df8-a9bf-1c169e52b692 | -10.2974 | -67.992104 | 2024-10-18 01:40:16 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3c838576-fb48-315b-b8d5-51b7e63eb459 | -10.3871 | -68.417397 | 2024-10-18 01:40:16 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e6737376-ec77-326e-abf9-4c1cacd58680 | -9.4561 | -64.552803 | 2024-10-18 01:40:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b17cd761-0726-324a-87dd-92446d903da1 | -9.4577 | -64.5597 | 2024-10-18 01:40:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93063e8b-053b-3933-9e3b-12b3b01283ee | -9.4592 | -64.566597 | 2024-10-18 01:40:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3ba9a209-f850-324d-9efa-a6c04e68a04a | -9.4463 | -64.555 | 2024-10-18 01:40:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cd25e225-045f-3fb0-93f0-64717b4aef06 | -9.4479 | -64.561897 | 2024-10-18 01:40:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c39070f7-7eea-3f5b-a4fc-cfa577169a90 | -9.4494 | -64.568802 | 2024-10-18 01:40:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c632d63c-71b7-31cc-82e0-ee9f03f31316 | -9.4283 | -64.566299 | 2024-10-18 01:40:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f94592e9-e04c-3588-a0cb-ed13397df0f4 | -9.4298 | -64.573196 | 2024-10-18 01:40:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2573273a-234d-308f-804b-45b61fc834e2 | -9.4169 | -64.5616 | 2024-10-18 01:40:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 094c6b19-604d-3598-8b3c-b3b848a96bfd | -9.4185 | -64.568497 | 2024-10-18 01:40:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f2d29970-c791-3790-b6c1-8b5859eb97e4 | -9.42 | -64.575401 | 2024-10-18 01:40:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c87dd539-12d6-30d5-a322-3718bb4dba41 | -9.0612 | -63.666599 | 2024-10-18 01:40:21 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 243d8ccc-93ff-3d3e-b0fa-d4b166ecb587 | -9.5647 | -66.161598 | 2024-10-18 01:40:22 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a8f016a7-2bf9-3355-b9b5-b75c2ddd0459 | -9.5663 | -66.168999 | 2024-10-18 01:40:22 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a46992d8-eb8c-3305-beea-f695b0e7a183 | -9.5679 | -66.1763 | 2024-10-18 01:40:22 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ededa53c-112c-36ec-a5ae-f0051e475610 | -9.956 | -68.896004 | 2024-10-18 01:40:25 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 04f244e0-3e3f-32e7-b420-6532d0aee9d9 | -9.9581 | -68.905998 | 2024-10-18 01:40:25 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fa495bd2-29d7-3811-8550-a50e61c1c1d0 | -9.4708 | -67.052498 | 2024-10-18 01:40:26 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d250e603-6253-3c63-bb35-aba413fd598e | -9.4725 | -67.060501 | 2024-10-18 01:40:26 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a33dc775-0f79-39fd-addc-4aee828de0d9 | -9.4471 | -67.132599 | 2024-10-18 01:40:27 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6b53024-b836-3439-a386-9870e457ddf5 | -9.6663 | -68.540901 | 2024-10-18 01:40:28 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 76bee659-a4dd-3de7-a965-078965168b23 | -9.6683 | -68.550301 | 2024-10-18 01:40:28 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 8335bc4b-4ab1-300f-9266-d80504b8e834 | -9.6338 | -68.677299 | 2024-10-18 01:40:29 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 05b0903e-2871-3110-a20e-590c8c4cf50b | -9.6358 | -68.686897 | 2024-10-18 01:40:29 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fa2b2119-547f-39e1-8373-b1827e1ce7bf | -9.6499 | -69.044701 | 2024-10-18 01:40:30 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6569abc3-dcd9-3e3b-85b7-467a88a2a5d5 | -9.3898 | -68.2994 | 2024-10-18 01:40:32 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 40e5eb6b-496d-37a1-8684-0c5a05f7a622 | -9.3702 | -68.303596 | 2024-10-18 01:40:32 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 94444e22-d43e-3d2a-ad1e-6b56f15d9570 | -9.1344 | -68.783401 | 2024-10-18 01:40:38 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b8a1c872-f4f4-33ce-8977-f726c882c172 | -9.1365 | -68.792999 | 2024-10-18 01:40:38 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb3f8f8-39e1-3306-b36a-09d820e2cbb8 | -8.9724 | -68.455299 | 2024-10-18 01:40:39 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6de783c4-d113-3205-8e3c-74b5f0199180 | -8.8493 | -69.417099 | 2024-10-18 01:40:45 | METOP-B | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 73d0d54c-ff7d-3748-b47f-7575034b5ef5 | -8.6508 | -69.590302 | 2024-10-18 01:40:49 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6b41d7ce-fe92-36b8-9867-2c1e73b324d1 | -8.6169 | -69.720001 | 2024-10-18 01:40:50 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a59ee11b-9451-379a-b4e3-5dcfd99b93b4 | -8.5554 | -69.961304 | 2024-10-18 01:40:51 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 73ea9694-4631-3cbb-9909-b293cb931239 | -8.5578 | -69.972397 | 2024-10-18 01:40:51 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 238a78e0-057f-3211-a037-d6616bf26993 | -8.5003 | -70.2332 | 2024-10-18 01:40:53 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d036d80b-d121-3236-946d-f25c0c04ed26 | -7.238 | -64.675301 | 2024-10-18 01:40:54 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c322548-5628-332c-b8db-65f396f13bf7 | -7.6973 | -73.021202 | 2024-10-18 01:41:16 | METOP-B | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5754ea7c-f1d8-3907-a582-ab94f55068a8 | -6.6826 | -70.095703 | 2024-10-18 01:41:22 | METOP-B | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7a666e-06eb-3747-a12e-ec571183ef99 | -6.6849 | -70.1064 | 2024-10-18 01:41:22 | METOP-B | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2b85c54-e7d7-3f2d-8757-6ef34b426a89 | -6.6729 | -70.097702 | 2024-10-18 01:41:23 | METOP-B | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f831b501-f6f5-361b-b3f8-041eb7a7bcf1 | -6.6752 | -70.108398 | 2024-10-18 01:41:23 | METOP-B | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20604748-ab97-3b65-acc5-a6612476afdd | -1.619 | -47.0919 | 2024-10-18 01:45:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| ac558374-793f-321a-b434-b9d694d90022 | -2.8795 | -51.6695 | 2024-10-18 01:45:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f8be2d21-eacb-3757-a41a-b3190fe89ea6 | -3.1382 | -51.497 | 2024-10-18 01:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f8d10f55-f334-30d4-8437-6b1521b22c78 | -3.1566 | -51.4965 | 2024-10-18 01:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 8352be8e-d096-3cd6-b43c-e370e3a6f244 | -3.7009 | -45.9 | 2024-10-18 01:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 30b5649d-98e8-357f-ac3d-0f475e38a417 | -4.4072 | -45.9773 | 2024-10-18 01:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a38d1121-fbcf-3f4f-bfb5-6e62d9f11376 | -4.4258 | -45.9763 | 2024-10-18 01:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 161.3 |
| bc3a2ada-224a-30f6-a46f-fb8d681b7b26 | -4.426 | -45.954 | 2024-10-18 01:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 84.5 |
| c3d049e4-b846-312e-97f8-568f6a5281ed | -5.5716 | -44.8927 | 2024-10-18 01:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e5114267-6b53-3359-98b4-1b4842106743 | -6.6703 | -70.1174 | 2024-10-18 01:45:44 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| bfe62a56-a8c9-3527-ae8a-cd8857a616c6 | -6.6886 | -70.1171 | 2024-10-18 01:45:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| fbfa9ce2-7669-32d8-b358-8f7283ef61d0 | -12.5045 | -55.205 | 2024-10-18 01:46:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c2888249-c1d4-3152-968d-a60176bae3ad | -12.5048 | -55.1846 | 2024-10-18 01:46:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 9d283be0-5229-3e24-9d2d-98ff8ff99d4f | -12.4966 | -63.2066 | 2024-10-18 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 51affe25-b992-36d8-b81c-047ac54403dc | -12.5155 | -63.2055 | 2024-10-18 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 9631a6f5-6cc6-33c7-82ec-5dde05ce11fc | -17.0191 | -57.4768 | 2024-10-18 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 8dc2cf9e-2bb9-3d24-99bf-c4e4bbe2cc3c | -17.2177 | -57.3102 | 2024-10-18 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| a3280223-21f3-3487-89fe-4c5c29b81b91 | -17.2373 | -57.3079 | 2024-10-18 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.2 |
| 2e94285e-67fd-3527-a18c-70f0f1ade426 | -18.102 | -42.7173 | 2024-10-18 01:46:46 | GOES-16 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| 81404fb1-1a5f-3613-83b2-6d2251caf434 | -17.7855 | -57.4473 | 2024-10-18 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.7 |
| 05983dc6-cd26-310d-9805-3d7b70064d42 | -17.7858 | -57.4267 | 2024-10-18 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 311be86a-3b56-3412-a758-0d8367377848 | -17.8049 | -57.4655 | 2024-10-18 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.3 |
| 642047be-c5ce-3647-83ff-ff447edaa37b | -17.8246 | -57.4631 | 2024-10-18 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| e882e633-0468-302b-b04f-284f680ba524 | -18.0632 | -57.3514 | 2024-10-18 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 071a7955-8eae-3364-b9b4-46cf1544f499 | -18.2338 | -56.6263 | 2024-10-18 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 88ad6783-c393-37dc-9328-0b2c4ca127e3 | -18.2533 | -56.6446 | 2024-10-18 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |


[Clique aqui para ver as próximas entradas](README17.md)
