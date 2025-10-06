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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea0f182e-f03b-3c2f-afc0-7c81f2fae2e5 | -13.34952 | -47.19098 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b6d09097-9754-39dd-9c85-ba66dfc2dabf | -7.79661 | -44.14062 | 2025-10-06 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b8bff5b-8772-3e8e-bdb6-edf8501c9833 | -13.26628 | -47.83869 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d05350e5-7b59-3497-9b00-23c0671329e8 | -8.54136 | -47.22177 | 2025-10-06 03:36:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ceeb7ac4-2c83-3851-ba70-9c1b586efa0d | -13.07951 | -47.95312 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 307158a3-ea05-36e9-bab9-8bc0caa9776e | -12.90089 | -47.30331 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 377c07f7-12a5-3677-8c5b-2ceb35b01eff | -11.93907 | -46.43779 | 2025-10-06 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f4e380a-b602-3ff4-937a-becace84c10d | -13.25195 | -47.80968 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7a29602-523f-3af2-a892-c93472d58320 | -7.98469 | -45.48944 | 2025-10-06 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1d3ac604-ee18-32e8-9e45-b9257460000e | -11.04636 | -47.76989 | 2025-10-06 03:36:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ee11ce9-f745-3015-b78b-a70ca516defe | -7.79802 | -44.13309 | 2025-10-06 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10581016-397a-324e-b926-e10dbac9f4e0 | -7.98717 | -45.48676 | 2025-10-06 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2424df3-d0a1-3bec-88ed-c9f94e4e6358 | -11.04831 | -47.72707 | 2025-10-06 03:36:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b32b6082-9c05-3b24-87e1-6b88995734f7 | -13.1243 | -48.00209 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5533f318-37c4-354d-be6b-7021c6753051 | -9.32033 | -46.009 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b8c6dd25-0131-307d-b017-f2295eb21131 | -12.48112 | -45.55568 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 49f9444c-e83f-305b-9278-98874c4d7ee0 | -8.66254 | -41.6805 | 2025-10-06 03:36:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6becb72c-a2c4-3dfb-9445-cc77468fbcd9 | -11.79898 | -45.11656 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87846633-03c2-3978-a447-5614d7abb3a7 | -11.15389 | -47.93435 | 2025-10-06 03:36:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a2b7e2be-6e2f-3c0a-9e49-22f64f783c28 | -9.31704 | -45.99239 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 072266f3-f4df-3369-b52e-945e64c05d51 | -12.48368 | -45.5431 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd726058-67b8-3aad-87a3-b4187f167f20 | -13.26441 | -47.59195 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bb81497-c155-38e8-8e57-4640d9e2bf5c | -9.37085 | -45.91515 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5805b902-8e77-3947-ac81-461a781807af | -8.16087 | -43.34357 | 2025-10-06 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d7c1f11-c9b0-3ad8-a13e-4b524313ea52 | -12.89256 | -47.30582 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cd8d111-136f-3654-8771-10986d837eb9 | -7.79723 | -44.13127 | 2025-10-06 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 416fa293-1406-30d4-a60a-fa12b0696419 | -13.22964 | -47.81844 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98516d75-0294-3056-b054-4b23cc6a29c1 | -13.32413 | -47.17345 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aa60b6f-1a8c-3733-a229-be2831d0d892 | -8.6593 | -40.60184 | 2025-10-06 03:36:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8bf0ab3a-a4d8-3460-a2a8-394594dc16c0 | -13.07894 | -47.89167 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 599390b0-fe74-34b2-84c1-9539caf01f50 | -13.26336 | -47.59705 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dabe3993-b136-3ff8-995c-0b6151003bcd | -11.84032 | -45.06487 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 199a2b6e-25c9-3359-a24b-a4cdc4bcdc73 | -8.16532 | -43.34041 | 2025-10-06 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3016c72e-1aca-3723-a12b-223d0dcd0561 | -12.90743 | -47.29809 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fada9c51-ef86-314d-b4b0-b852fc312ab0 | -7.79872 | -44.12934 | 2025-10-06 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| feeb7219-b09f-39ed-ac07-73ea59187189 | -11.71533 | -44.30887 | 2025-10-06 03:36:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff9b43b5-4199-3d8f-91aa-9a5090f9cc5b | -7.98626 | -45.49172 | 2025-10-06 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b3bb3a1e-0ff6-38f6-a0fb-f3dd895cd004 | -12.25346 | -49.21778 | 2025-10-06 03:36:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a9a20c1-ec04-316c-b261-7c16408f89c0 | -13.11628 | -48.00739 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bb742985-7e7d-3074-ac91-ff60d48b9150 | -13.0996 | -47.92359 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6535f8db-3c0e-38a8-9f77-78dda299f20d | -12.48689 | -45.55734 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4854e474-2f60-30c1-9819-5a367d1b0a12 | -12.91467 | -47.30106 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6781d082-d11a-3098-aa10-ac9e2b95af20 | -11.43892 | -43.48462 | 2025-10-06 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dc13b1b-f00b-381c-bd8b-e689fb8ad893 | -13.04939 | -47.91153 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1b1b214-dfd4-3d97-b5d9-1176ecc910f2 | -12.39388 | -45.00234 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b11bcfb-b373-3e73-a10b-aa3de93e29e9 | -8.52721 | -46.40108 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6852ba12-4160-397a-b3ea-4e6b555599ba | -8.87708 | -47.61575 | 2025-10-06 03:36:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6eefc21-bb27-37a9-89b5-6cfb9f31f162 | -13.07028 | -47.89997 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7eeb9165-99a0-3cb8-8862-2ad512d4dc55 | -11.03217 | -47.79728 | 2025-10-06 03:36:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea178db7-bcfc-39f6-b622-2a5c31b9f5d3 | -8.86805 | -46.84121 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5b2635a-b4bb-33c3-b3c9-7f6088c41ffa | -11.9399 | -46.43364 | 2025-10-06 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a305687-5007-3535-b094-02276ad9b5ab | -12.45233 | -45.54965 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e98118b-8a99-3ab2-a2c4-197e43593e1e | -8.6448 | -44.91219 | 2025-10-06 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97eeda86-cadc-3507-ad7d-1d2cd85e3cc1 | -11.79819 | -45.12065 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 179c9740-851e-3d8b-aa55-a076d06ced2e | -13.28075 | -47.5783 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6bfdb83e-94a4-3475-85e8-43b25b18c33f | -7.99277 | -45.48081 | 2025-10-06 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ac8fb91-78f2-3f77-a99a-2aff90f986a0 | -7.99896 | -45.48214 | 2025-10-06 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56871a6e-6ab2-3d2b-97f7-d5ba10d7f65f | -11.80364 | -45.13023 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39a1984f-0aad-3549-adfc-97b3369474e9 | -8.55535 | -46.25319 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 408586a0-dadd-367c-9631-f697ff3c7beb | -13.26971 | -47.18277 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfe8878d-7ad6-3c4c-9589-3ab1fdcb5faf | -11.84181 | -45.05738 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d3b6c44-2fc5-3034-8fb6-a91458dd6c3a | -12.2198 | -44.23885 | 2025-10-06 03:36:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c78679da-11ba-3ba6-ae80-63310266b4d7 | -9.3117 | -45.98638 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| eaba38cd-0b9b-3d64-942e-ed5aa273e005 | -13.24426 | -47.81379 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0579e3a8-c09c-3873-bf4b-9bf561e05e89 | -11.25259 | -47.7777 | 2025-10-06 03:36:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d32164e5-7695-33fd-ad17-964a2311520d | -12.44156 | -45.57363 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad347c36-6ed4-35b5-9d09-349bcf1804f4 | -11.79899 | -45.12388 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 391d98b7-d94c-3be3-ad13-f1ee09ea7494 | -8.56202 | -46.25326 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d4b02ac-e621-3ed9-87db-34f115529fba | -11.90559 | -46.22623 | 2025-10-06 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e1a1e02-dfcc-3ca2-829f-05c0e7f422a4 | -13.22161 | -47.82408 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa999410-d489-36f0-8194-6f689fcc986c | -11.8383 | -45.06564 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83c85f3e-676c-34b8-958b-0b248f45839e | -9.3151 | -46.00237 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 45ee9902-86f5-3829-a181-550329d48d66 | -8.87181 | -46.83861 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a2dc62b-ef52-3fdd-a3c9-b46617ac746d | -13.08459 | -47.83356 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1c92228-e817-3fba-9f95-d7c287ed4371 | -13.08061 | -47.88395 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55a5aca4-357b-33b0-bbf1-ce4dbc538f7f | -12.58103 | -46.73793 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ad2ee1c-6659-3937-a6cb-e8c2c02c7c8b | -11.67219 | -47.48145 | 2025-10-06 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bdc9dd33-f0e5-3900-9b7b-bae252dc824f | -11.02973 | -43.10395 | 2025-10-06 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06dfa697-e611-3a48-af73-d5161dae780b | -13.10825 | -48.01265 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58b8e889-b195-3a14-aabc-aec58e6fcb7d | -12.89889 | -47.30736 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4e32be95-7f19-3ea5-9003-838916fd0ece | -8.62849 | -46.32573 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| efa84432-134e-3b3c-b7c9-efafac129f50 | -11.84912 | -44.93217 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 388719f8-9086-3848-9e65-c099cde7f8b1 | -8.56195 | -46.25434 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d4c80d8-00cf-34dc-9fcb-c6c8b5420938 | -13.35759 | -47.20206 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1bafe4c-c8c6-3b29-ba1e-8a0798e4ddac | -8.65877 | -41.67757 | 2025-10-06 03:36:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0f3e2f46-0ff9-315f-b043-6ba5b3b9ecb6 | -11.70597 | -45.40947 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f05218d-9624-31e5-9281-771aaeb1bb24 | -13.35406 | -47.18728 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e3a1987-5636-3733-bb0b-50d25d69d71c | -18.02259 | -44.99835 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 085472a8-7a1a-3197-846e-3217e4b85294 | -14.69361 | -48.37081 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 84aab5e9-11d0-3c71-9712-e781f62933de | -13.3553 | -48.04495 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3a8844b5-9af5-37c5-898f-5ba2b0495da2 | -15.67599 | -46.28677 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94c4c1ff-6d32-3d1c-ae51-7ca000a6ac0d | -13.55825 | -47.24252 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32d5cc9d-0e8c-3117-97af-18030f36c606 | -20.26672 | -43.63574 | 2025-10-06 03:38:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6919c2f2-d082-3fbd-aa7d-4e177a64ea23 | -20.11624 | -44.40343 | 2025-10-06 03:38:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 027695d3-ab32-3ef2-8321-3d8e46c18300 | -13.35739 | -48.04829 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| de875ff8-d071-3413-924f-97a8cb6ad1e1 | -17.66427 | -44.43426 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58d2f27e-e64c-3804-92fa-17769b0ac7e9 | -15.33953 | -47.31447 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df7539c0-98d8-3a72-911d-0ff66dd92520 | -13.3588 | -48.04158 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 038d824e-4c82-3da3-bbe0-110b494e9d39 | -14.90764 | -46.85687 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf5b6d46-63e2-39e2-b32f-439486bd9e97 | -14.70538 | -48.3798 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
