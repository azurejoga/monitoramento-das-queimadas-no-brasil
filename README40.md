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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28e535b2-594e-3036-9573-beed5d0fac5f | -5.21974 | -43.19157 | 2025-08-15 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fee64cef-b341-3820-8189-a4e616bb6cb9 | -3.11012 | -47.4977 | 2025-08-15 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af30e34e-6533-3116-b4f3-7faf1e2ead20 | -3.43431 | -49.0494 | 2025-08-15 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a7a7c375-1c5e-3966-a85e-35ca0aec6fe6 | -5.68371 | -43.65764 | 2025-08-15 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e66f11e4-3061-30c6-b2d8-c9d473ead561 | -2.91358 | -48.30385 | 2025-08-15 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5d3a4ea6-b259-32be-8f36-8dee9b0c76b8 | -3.43073 | -49.04886 | 2025-08-15 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5e4a189f-9ab4-3858-8cee-606c3b7f898a | -3.48253 | -51.18822 | 2025-08-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84f2ad6d-0b1b-3a2d-a511-867b654a3e15 | -4.22364 | -47.21474 | 2025-08-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae55780d-7a1c-34dd-8d32-a0996a978beb | -7.38537 | -44.88667 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 12d90723-ebaa-3e19-92b4-f983ceb1a42a | -2.6023 | -51.94845 | 2025-08-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2b0cbb5-6d25-314f-84a7-bbbc308eaee4 | -4.66379 | -48.86686 | 2025-08-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56747af3-e23a-3d90-8e6b-87b744cb7c45 | -2.90794 | -48.25125 | 2025-08-15 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bee8a10-8364-3437-b996-1bec7093d3c2 | -7.37883 | -44.89724 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef5b70d2-71c6-3ff4-b940-0d538a100ba0 | -3.45003 | -48.97226 | 2025-08-15 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d781395-82b6-3c86-b0b2-e94f91306d0a | -5.76104 | -46.66854 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1c47e999-65df-308c-bd98-580932eacdc9 | -4.18587 | -42.43011 | 2025-08-15 04:49:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dafbde27-62d4-3885-8aa7-b685d9565ca1 | -4.06775 | -47.98434 | 2025-08-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff0ffc41-8e3b-34e0-bb8c-b6e4a3eddeef | -2.54286 | -47.71206 | 2025-08-15 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa7e62ab-8891-349b-8c26-11fff0957914 | -6.55735 | -49.49229 | 2025-08-15 04:49:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ed2a8cb-f749-309a-ba4d-c1ddc9d40df0 | -2.50965 | -51.82453 | 2025-08-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad242c2a-0ac6-38ac-892b-3bdfef2da063 | -6.55309 | -49.49595 | 2025-08-15 04:49:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cf2c89e9-da89-356d-9c44-200efc3088e5 | -3.32074 | -48.72475 | 2025-08-15 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58728368-3548-3db7-a974-a138bd9cc569 | -2.60561 | -51.94896 | 2025-08-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e4d3aca-6a04-393d-96d8-b71b2e3ef6e5 | -4.59709 | -43.31767 | 2025-08-15 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26eb9033-a012-3d6f-95eb-c2a08c8e1fb3 | -6.33105 | -42.80325 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a78a85d-62a8-34e9-99c1-aed6d285a3b4 | -6.95213 | -44.55237 | 2025-08-15 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab234925-ca58-3f05-b377-7f0a5b6889f8 | -7.38198 | -44.87488 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d76dbeb2-1232-3ed1-b02c-9e72a0be55f1 | -6.9609 | -43.86509 | 2025-08-15 04:49:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39844056-d955-374b-8974-245e2c6a8379 | -4.68776 | -43.24353 | 2025-08-15 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4baa95d-fcda-3c95-8176-dd91295ae544 | -2.58404 | -51.91394 | 2025-08-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad82b977-4974-3156-9be5-07ca9516451a | -6.94755 | -44.54834 | 2025-08-15 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8271d531-1196-30ba-acb3-e39cf141bd54 | -3.42715 | -49.04832 | 2025-08-15 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 994dae04-3879-34d2-a5f6-147de03b8771 | -2.54214 | -47.71674 | 2025-08-15 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e05e4ab-07ee-3ce2-9dc6-9cf3c87ea1f5 | -5.76567 | -46.67392 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c9dd7ea0-932d-3b2c-804c-6da4f6b9cd1b | -7.38459 | -44.89217 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90051842-db02-35c9-9249-4e442243d196 | -5.37373 | -41.2377 | 2025-08-15 04:49:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 47987f3d-4338-3f22-a0d8-2cf4244d7950 | -7.38858 | -44.86398 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5174dbd4-4785-3173-b06a-fe8069076eec | -3.00898 | -46.69343 | 2025-08-15 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0255d5b9-58a1-39f4-9ad8-f067ddcda851 | -4.22311 | -47.21828 | 2025-08-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1cf305d-8bb7-3d95-8112-f6d0a2512585 | -2.95596 | -51.66568 | 2025-08-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdec3984-e684-3425-9688-069046b27231 | -6.90513 | -45.20827 | 2025-08-15 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 880d4fc8-b0cb-3e89-95a5-f73491279e0f | -3.44644 | -48.97173 | 2025-08-15 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd7bb752-89c3-364c-9650-68d44e936e3b | -5.23053 | -43.19293 | 2025-08-15 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7afde182-d6a6-307f-9dd5-57396880faaf | -7.63822 | -44.93805 | 2025-08-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a31d167-9f2b-39aa-9479-7a0183e275a0 | -5.68417 | -43.65433 | 2025-08-15 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 402bb798-f9cf-30b0-a547-ad13e4569cc4 | -3.49303 | -43.31455 | 2025-08-15 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 780f7ce8-2374-3f96-ac9a-309268525fbf | -2.9108 | -48.30563 | 2025-08-15 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58f2ee71-d7c8-38d6-9618-e4b366b67037 | -6.55184 | -49.50437 | 2025-08-15 04:49:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9d71557-e9fc-3a23-9e4a-75cfac907702 | -5.09365 | -47.71445 | 2025-08-15 04:49:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da3c4d38-e978-3e90-8f66-eea73b2223fb | -5.22513 | -43.19227 | 2025-08-15 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c793483d-89df-33c4-b442-b43539232008 | -7.38776 | -44.86979 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa8c53ed-f868-3a82-961e-d1b3e244ebd5 | -7.14725 | -44.40344 | 2025-08-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcf69de2-4b11-3203-b255-bc9d2f3ec49f | -6.90995 | -45.20891 | 2025-08-15 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1e48590d-3961-3e8b-9180-70b35da70601 | -5.61432 | -43.46759 | 2025-08-15 04:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39d94c79-5249-38fa-93e9-249c3b1a6b5f | -7.32126 | -44.68841 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59159473-98a9-32e0-87c3-d26a254f4410 | -2.67962 | -52.16835 | 2025-08-15 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0644368-d260-3a2f-b310-33f334ea7a76 | -5.54299 | -45.37273 | 2025-08-15 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f75f6c40-3e0f-3f80-8731-02408a612d58 | -3.64836 | -48.32345 | 2025-08-15 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30594513-1d59-3ecf-a201-189d4ff1e5f5 | -4.59757 | -43.31438 | 2025-08-15 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 793c5faf-01ff-3ae1-91fe-4eb0f70af03c | -3.10936 | -47.50263 | 2025-08-15 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80660dac-bb75-3ce0-a046-01f0d1e30871 | -3.73393 | -48.9318 | 2025-08-15 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dfed3e9-6774-3f4c-9f6b-ce46b8b4eab6 | -5.36761 | -41.23676 | 2025-08-15 04:49:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 54946304-e246-3557-9657-67117ccaae6b | -3.95626 | -41.47936 | 2025-08-15 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6049b6be-c89d-3674-b631-de0781258e32 | -4.39533 | -47.77348 | 2025-08-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c58a3a6-901e-3073-869c-9f2355b1b8d2 | -6.6099 | -43.88886 | 2025-08-15 04:49:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02586df0-491b-3064-be87-4f85dd8625c7 | -5.76531 | -46.66917 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 55e79dfa-255f-3ed4-8fb5-c59518264260 | -3.44708 | -48.96761 | 2025-08-15 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f95c8988-6a60-3d72-b4eb-74fd98daabe3 | -5.76474 | -46.67318 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 98df5994-68ac-34db-a720-8389de0a6827 | -2.91149 | -48.30124 | 2025-08-15 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 46f2ad0b-ba99-3ea6-a744-8fc09658ff4e | -4.60237 | -43.31848 | 2025-08-15 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aac4d71d-010a-36a7-8764-12918c96fae6 | -7.07655 | -44.95011 | 2025-08-15 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b23036d-d0ae-3d01-9be6-df52bfc1d5f9 | -6.95587 | -42.87357 | 2025-08-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c5f80ea0-f025-35c1-a189-9d209b8509ec | -5.762 | -46.6693 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d23e9843-2467-3ca0-afe9-0a77cc144c38 | -5.37344 | -41.24036 | 2025-08-15 04:49:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7d39b450-a603-3d43-9187-3998ed67eba7 | -7.14684 | -44.40633 | 2025-08-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12924906-d95f-36f3-af6a-e6179d97d07f | -5.70268 | -53.65117 | 2025-08-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ad01a89-963f-3ba4-844f-23036c213b93 | -3.38186 | -47.61061 | 2025-08-15 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6807ab6-367f-33cc-a098-443ef9c641c2 | -7.01894 | -44.29528 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40fd5fc3-d1ed-3465-b43d-823319dae311 | -5.70603 | -53.65169 | 2025-08-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2951445a-03bf-361f-bf92-da04f13ad11c | -7.63913 | -44.93946 | 2025-08-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73c805cc-fb6f-36ab-a10a-d46fe25afe33 | -6.9467 | -44.55453 | 2025-08-15 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7e5cafc-25e7-3350-aa4b-b4c5235ea5bf | -5.54765 | -45.37336 | 2025-08-15 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 411be27e-8188-395f-9b46-f958a6c70a05 | -7.14805 | -44.39777 | 2025-08-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd1f5422-b845-31ec-ae62-a04b9ea268dd | -6.95787 | -42.87581 | 2025-08-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 14ff2e59-8a3e-3446-a8d8-eb7760c64f08 | -5.59887 | -45.38097 | 2025-08-15 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a0d5a018-1897-3b45-a4ee-b724c8b1c666 | -2.53905 | -47.71152 | 2025-08-15 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c954d7d6-aef3-374a-a936-6b493c47da21 | -5.78744 | -43.60552 | 2025-08-15 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03dfc6f6-cc37-3c4c-b3f6-5b4abe355ba6 | -6.94628 | -44.55756 | 2025-08-15 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2477261-4bcb-3b2e-bfad-57107a694f78 | -4.47903 | -47.67192 | 2025-08-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57a1d6a8-6791-3813-939b-f1de13d6ae24 | -4.22767 | -47.21534 | 2025-08-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8004c44d-a702-334a-83bf-8ac7122af4c8 | -6.00793 | -46.07435 | 2025-08-15 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d780604-f342-32b1-85ec-1545ff9f2bca | -3.44348 | -48.96706 | 2025-08-15 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7ef7ce3-1830-3b54-87fc-9da264e65432 | -4.66443 | -48.86273 | 2025-08-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfbd8d04-4623-39fa-b0b9-c10b42a0a053 | -3.98974 | -47.83436 | 2025-08-15 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40fe46c6-67ae-3610-afc4-74c488aea24d | -4.18641 | -42.4264 | 2025-08-15 04:49:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 379c1deb-26ca-33b8-b92a-a8c454170aa7 | -7.16043 | -40.4188 | 2025-08-15 04:49:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e82b0440-57bd-3f7b-be82-266673ebfdec | -6.96769 | -42.8712 | 2025-08-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2e33505a-66e1-3702-8b61-e1d271221152 | -3.31775 | -48.71999 | 2025-08-15 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5ac1b35-fa6d-3561-ae34-7e9451a7e4cb | -2.91425 | -48.29944 | 2025-08-15 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fd0974c9-ef2e-3cb8-9552-ff877b3f4f42 | -9.1706 | -59.6762 | 2025-08-15 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |


[Clique aqui para ver as próximas entradas](README41.md)
