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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 820a148e-ae9f-38c3-a939-978c6df5685b | -12.7542 | -54.00204 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b722f279-9a5f-37ba-99e5-d2f39bbeeb93 | -12.74445 | -54.01929 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2f6f211-c745-3ed2-b4ce-fa0880c2d524 | -12.74108 | -54.01873 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30337a17-8bf4-3f2f-b0cd-b8642a49e7f2 | -12.73771 | -54.01817 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be514c9a-6ad8-3fd9-bd08-9585f67bbda4 | -12.73271 | -54.11221 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d41c769-3cb8-31a6-ba6b-359eeb46d11e | -12.73055 | -54.10422 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ba9f69c-969c-39eb-9612-c69a464d03dd | -12.72994 | -54.10793 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59999884-c71e-36e0-854b-0bde99330ba6 | -12.72873 | -54.11534 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 804856c7-b4cb-3417-b633-6daa94b8a4a9 | -12.71798 | -54.11733 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 117b43c3-3220-30f1-963b-180cb291a404 | -12.71521 | -54.11305 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68780840-8c82-3e6a-9577-64156931d5c4 | -12.71183 | -54.11247 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97537927-63f0-325a-ba7e-3dbe8db04c2a | -12.70906 | -54.10819 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd23a143-2fc0-31e9-9e0b-c533a5a35be5 | -12.70845 | -54.1119 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33cad033-139a-3b78-8a43-01168ce50960 | -12.70629 | -54.10391 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5ccff75-04fd-3f77-8fa9-f5fa2e15919b | -12.70352 | -54.09963 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68b06bf0-2654-38d9-969a-04628ab82c25 | -12.70351 | -54.0052 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 079636a0-9856-3405-94e0-fec35c92ebfe | -12.70075 | -54.09536 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4a45dde-c247-3073-9cce-d1452581221c | -12.70014 | -54.09907 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0861c92b-6c41-3bf0-aedb-35840b8d31b4 | -12.70014 | -54.00463 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6d72437-bc1b-3008-a7cd-fefeff09342c | -12.69737 | -54.0948 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eada1614-9fee-3fd1-a8ea-0c36c483f8cb | -12.69617 | -54.00775 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd5863c7-6b7d-3779-98d2-2189fb24e8cd | -12.69595 | -54.09489 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b7132d6-402a-3738-9f2a-3e3b37b49a8d | -12.69257 | -54.09433 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74639aff-e1b6-31c1-97e9-355d427f3a57 | -12.68919 | -54.09376 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84fed8e1-43fc-3402-8ea4-4962571d6f57 | -12.68859 | -54.09747 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a706b78d-3c26-3065-b8e9-7ac3a85f2b87 | -12.68764 | -54.01764 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55c4fdd2-47f3-303c-889b-a29d005d63f3 | -12.68705 | -54.02131 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1287ac5e-e063-3d45-9202-d5ca27a03d7a | -12.68641 | -54.08947 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfde2da4-15db-36af-88ce-5182f98c40f3 | -12.68581 | -54.09319 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6883a40c-3c35-3925-a7e1-82275ae0fd03 | -12.68521 | -54.0969 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9b5e54d-1972-3680-8271-94b28851dd64 | -12.68308 | -54.02442 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed0898dc-8453-3383-85fd-bae2c76fd3e3 | -12.67808 | -54.07666 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2785b101-c4d9-3cce-b347-446ccad5853c | -12.67792 | -54.0349 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc0b370b-b4d1-3753-9ca1-3ab403ff7b8b | -12.67748 | -54.08037 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7268e76-b444-313f-80fb-eb0c42ec43eb | -12.6747 | -54.07609 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43c609a8-340a-3674-98c8-d6d11d6ad1de | -12.6741 | -54.07979 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c17a16f0-ad52-308d-86e6-4e0dc12d3bdc | -12.67394 | -54.03801 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9456a906-4dd2-32bc-8b7e-882a782feac7 | -12.67335 | -54.04169 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ecd1b74-c9ad-301b-b85d-183611b56347 | -12.67132 | -54.07551 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04426fb8-7536-3fbb-9aa8-ee9612ae08e5 | -12.67095 | -54.05645 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9532e87a-b26c-3807-8247-475a3e80a1b9 | -12.67072 | -54.07922 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25fae51c-0595-3c65-9982-6ba4798790cd | -12.66997 | -54.04113 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24e74dfb-29b7-3585-a31e-4f5e411e2d11 | -12.66937 | -54.04481 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d81fc445-c54c-3111-ae2f-7a84d936f657 | -12.66877 | -54.0485 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32c4a03c-386a-3849-948f-4776f9bfb183 | -12.66817 | -54.05219 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35c2f292-a90d-3d78-83fe-a0d953273bdc | -12.66794 | -54.07494 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96b75379-47f0-3fcf-8db5-4d63dfbfd3ca | -12.66734 | -54.07865 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e5b5dad-f9f1-3ea4-b323-31c061611d00 | -12.66697 | -54.05958 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a42c660c-ee14-327b-9b3f-d2139c640954 | -12.66637 | -54.06327 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 697dd2a2-6686-316a-8b09-af58719bde37 | -12.66577 | -54.06697 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15f39757-5a28-3ef2-a102-39a6ab1b72e8 | -12.66517 | -54.07067 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa650603-4562-3f0d-97f4-1f9581946499 | -12.66457 | -54.07437 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdb8dd75-0395-39f1-9264-0a00116db07c | -12.66299 | -54.06271 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a92be35e-6528-3834-a18b-d87a18dadca7 | -12.66239 | -54.06641 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c42931e-7859-3cd6-8472-298f0d66b21d | -12.66179 | -54.0701 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50d6308d-aa63-3dce-81d6-9ca8db0038f1 | -12.65841 | -54.06954 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8714b03a-ae88-361c-a5f2-05611722fbaf | -12.60843 | -53.49361 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 77fd3571-8780-362e-834b-e5c77cabe3ad | -12.6051 | -53.49306 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 98a9e6ee-4bb9-3bfb-b414-1c941bf93d06 | -12.60452 | -53.49665 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d0b86621-bffe-3cf3-bf38-7e2168ae662d | -12.58327 | -53.14125 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a91d8d3a-0139-3ce9-8af7-1f0a34980e8d | -12.5722 | -53.50937 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 855a1cf3-f935-3cf7-8698-c0e61711a943 | -12.56442 | -53.15271 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74df588d-fd9b-3a96-94eb-8aa007d41cd0 | -12.55232 | -53.4839 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ffe7cca-27d7-34cf-8a96-9ac15ff13700 | -12.55011 | -53.13581 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62a716ee-63a2-3e27-b4ea-6efce6322c81 | -12.54954 | -53.13936 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0b686ab5-e4a6-3fc7-ba47-ae96a31b0e02 | -12.54679 | -53.13527 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 146115ea-4b43-36a8-a9e5-6ce8105a3a8d | -12.54623 | -53.13881 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2dc4a68e-38f3-3090-bfc2-61a5838904ee | -12.54348 | -53.13472 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa796de8-a8f7-338f-9dfd-b3e1849ebf5d | -12.54291 | -53.13826 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8b474ace-1903-3662-981c-0f5024f38822 | -12.54073 | -53.13063 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 338850b1-3aa7-3977-be1e-0275874da629 | -12.54016 | -53.13417 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94a044fd-645d-33d8-a700-9f5a79815c44 | -12.51082 | -53.14759 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0907e28f-f1e7-306b-ac15-6ebb2beab4fc | -12.50792 | -53.18719 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51592a89-975a-3d54-bf11-2f4f737cf996 | -12.5075 | -53.14705 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2caf83f5-8526-3d7d-b272-f17f7c064a7c | -12.50418 | -53.1465 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d51676ae-2fac-3a50-830d-7857d645c3ad | -12.49535 | -53.5187 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e680ee03-d507-35b7-9a76-3de76fc494dd | -12.49477 | -53.52229 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7f2ba2d-7490-3f47-ba41-05f60db164c8 | -12.4926 | -53.51455 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba46d4a8-047c-3cf1-9114-d70aa3b8f8fc | -12.48969 | -53.53253 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d110e06-1b68-34e0-846f-fd685bb77b33 | -12.48577 | -53.53559 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ad7ce48-2f20-32b8-80e6-c2461fbf881f | -12.48574 | -53.19815 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdb61691-d22d-3f70-ab4a-8d2a038eb5e9 | -12.46463 | -53.45844 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a17958f-31b4-344a-bd93-4808b91aa4ae | -12.46072 | -53.46148 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a121f8e5-735b-3a32-ada5-31003d52b5bf | -12.45681 | -53.46451 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a12e72d6-f835-3e96-91df-4fcc347ca2f8 | -12.45347 | -53.46396 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a39713fe-4ee3-32f9-978c-e83a43c81de6 | -12.45014 | -53.46341 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10fd8ed2-a9bd-3f1e-ba1c-7b8e83dbee7b | -12.44978 | -53.52976 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d6db083-b3a2-3fab-8307-1ddc6b4b79cf | -12.44644 | -53.5292 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8158e407-43d5-306e-9560-37ec8b6eb0fc | -12.42307 | -53.52533 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41eae6ce-62dd-3b42-8427-53fbb8bb1dde | -12.38839 | -53.46423 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9624900-d21c-3570-80ab-a299ad6236ea | -12.38448 | -53.46727 | 2024-10-02 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d953600-8842-3248-b098-54761dc65222 | -12.33701 | -54.09995 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b7c6b35-042f-3a80-8573-d13f01be90df | -12.33641 | -54.10367 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9313259a-57b5-382a-abb3-99ef8d1af11c | -12.33362 | -54.09938 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e68cbaa6-24ef-3ee0-aa9c-bfdf8d54a764 | -12.33302 | -54.1031 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbffd9cf-b8b4-321e-afbb-059913c26801 | -12.33241 | -54.10682 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16a6eeeb-132b-3dd9-8c9a-be52d0b8f2fd | -12.33084 | -54.09509 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6451c4a-05f1-3928-8839-959f5785780e | -12.33023 | -54.09881 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b073826-1823-37b0-b92e-ebad1e9245ee | -12.32745 | -54.09452 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 200e6161-633f-3af5-8315-bd7e5c92b4ac | -12.32685 | -54.09824 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README102.md)
