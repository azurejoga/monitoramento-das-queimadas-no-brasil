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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 818cb1a2-96f6-35a4-b3fd-1dad46a4adbf | -2.8984 | -50.73039 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e120db3-0755-37f4-9361-2f8d46954e8d | -3.60949 | -51.03636 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80d32fb3-d1fe-3089-bcda-3c5ead64c810 | -3.09082 | -47.79009 | 2025-10-05 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3979790-4e9d-3361-b00e-1c5723f6ba8b | -4.37082 | -54.753 | 2025-10-05 04:44:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48419e0a-619a-30ed-b75b-7209b86bb6a2 | -4.07435 | -52.5302 | 2025-10-05 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d0bfb890-f23d-3be1-a24b-84bc320df472 | -4.65017 | -43.18329 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 97fc0d23-ea55-3ceb-a556-ee469c2697ad | -5.66704 | -42.74897 | 2025-10-05 04:44:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 81d8ace6-346d-343a-b7a9-2dccb658ee7e | -6.72701 | -42.16075 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e1acda8a-fc30-3087-b41e-7662e5166478 | -6.40123 | -43.05918 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4f58b69d-e0e3-3e08-94df-aaec62ab0741 | -5.30664 | -42.54794 | 2025-10-05 04:44:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e767d243-0b30-3a44-9e06-e592c5d8d4be | -4.43614 | -43.23775 | 2025-10-05 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ecf66207-991b-3c9d-b1e7-80182f882970 | -3.69003 | -50.89003 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dca10d99-b342-308d-a857-58372c0828d8 | -5.06707 | -40.47055 | 2025-10-05 04:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 2217eb24-b552-36e7-b304-f9909132ddfc | -6.63725 | -42.80315 | 2025-10-05 04:44:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 402b5398-93bd-32e4-aa0a-60330096fa34 | -4.27346 | -46.74284 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8999d9e2-7ff8-38b8-ae7f-3117cee8eaf9 | -5.91432 | -43.31453 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 688f6546-c5bf-3be3-b8a2-154c89ca9d84 | -5.64338 | -44.05386 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 495ad4d3-b77a-31a1-afa4-c46bd9ce22df | -4.81921 | -42.76392 | 2025-10-05 04:44:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65285da0-66c1-3a1c-ac9f-da3223a8a03f | -0.09918 | -51.27684 | 2025-10-05 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03c3751f-af2f-38b1-b4d0-11eb10a9215d | -5.79031 | -42.93491 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ecd6eb3a-9134-3c00-a53e-538faddacf15 | -6.2365 | -44.26769 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50cf6e1d-5ad0-3439-846d-2411f17c5e82 | -3.84956 | -41.56295 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f800729c-6c17-3717-a02d-60ec92500a73 | -6.25684 | -45.36849 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| daa5ec61-ffc2-317b-b84a-1bc9eed27fcc | -5.92645 | -43.33262 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 90f03691-4dc5-3763-89b7-97f04814d920 | -5.30651 | -42.5477 | 2025-10-05 04:44:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d8a04eb3-f71f-388f-a576-b6ca37ec1559 | -6.13285 | -44.63809 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2f15bcd-647d-36f7-9da9-7d7498620722 | -6.253 | -45.33574 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50b013ef-1ab8-3630-801d-daa50897f356 | -5.90612 | -43.75696 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69cd450f-479a-3a6e-8d17-02d1af0a30b1 | -5.89106 | -42.91087 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| c8783842-c5cc-3e88-8a32-df549dd4cc20 | -4.77771 | -49.32473 | 2025-10-05 04:44:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e253ca0-1042-344a-ba01-4b82b81d0d35 | -2.68696 | -48.40053 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68c9018f-488c-3dea-ab63-18160ab4b0bb | -6.29136 | -44.05217 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82402815-bf43-31d4-9f94-84aaeadb7096 | -3.23292 | -50.63884 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 517c0426-9602-32ef-b87b-f8a80f5c237c | -3.8491 | -41.56617 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 15be9db6-43d6-3dfa-b58a-84f5716cacb2 | -5.76655 | -45.7621 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 278dcdf7-75b9-39c0-8853-938f5b2e7f82 | -5.85327 | -42.80935 | 2025-10-05 04:44:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e95801c8-ba76-3836-afb5-209fffdd76ac | -6.24902 | -45.36329 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2107f18-4594-35d5-9bdc-50f69dbfc20a | -5.64949 | -43.91653 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 46421a35-d79a-31dd-ba41-53fb02bd0881 | -6.08788 | -46.19209 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 188fc06c-fcf1-35cc-bbb7-86a650e1ee96 | -5.8878 | -44.27951 | 2025-10-05 04:44:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 90dca2d8-ad08-3081-ae37-0db5bfb77c85 | -6.33317 | -41.63114 | 2025-10-05 04:44:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a332fe65-6e70-38c1-a3df-288f2b00e22a | -6.01966 | -44.0176 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20fba05f-f2a0-328d-be04-40a07a7bac6a | -6.35453 | -41.63698 | 2025-10-05 04:44:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a6177a21-ddde-3958-a0a2-a02cd9c9366a | -3.3909 | -50.14731 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea500249-5055-3c9a-8615-265e999ac782 | -6.15672 | -44.65958 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| cc869bc3-3b1e-3763-860d-18f54ce923e1 | -4.23213 | -46.75299 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5db47a3b-5615-3b02-87fe-8e3132a81cf0 | -5.36033 | -45.95383 | 2025-10-05 04:44:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db14409c-894d-3477-885a-43250fa82a74 | -5.85998 | -43.55901 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a0835e9-13e1-36bb-9ccb-31717a344d64 | -6.15541 | -44.60644 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7dc2a0c5-f40a-3da7-b49b-a23a85cb903e | -5.42953 | -47.09699 | 2025-10-05 04:44:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67be9797-8da2-3992-8df3-b9668f9a188d | -6.20848 | -44.07436 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2cc1a7ae-1224-3ec1-8e51-7c74b1ec9c1f | -2.60922 | -49.39989 | 2025-10-05 04:44:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 868cdd25-fc2b-39fe-889f-c72a9da76d5d | -5.91817 | -42.89732 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 9223e17c-58e8-3c83-b865-2215a188851b | -5.34507 | -42.97242 | 2025-10-05 04:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d940d970-7efc-3242-b63b-142f1c241a53 | -5.49136 | -42.80178 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| ef5a385d-a1c3-33db-8375-1fca11e2c331 | -6.39701 | -44.77402 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e10a35d-5919-3bdd-8648-a2e9b95f9a07 | -4.81694 | -45.03545 | 2025-10-05 04:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4caf1dfd-4aaf-39b3-ae6e-6f2a2f226369 | -5.84249 | -42.88602 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 136d5195-64ec-3c48-8a6d-936dcaac7124 | -6.65967 | -41.59061 | 2025-10-05 04:44:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 057d7fa6-f444-3d5f-8d18-a2aa246ca789 | -5.36084 | -45.95032 | 2025-10-05 04:44:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc98f328-1056-36a6-b78b-b75cb4c2d590 | -6.38563 | -44.75592 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bba9359-2676-360f-a5ee-48c5ec3d727d | -6.17712 | -43.83563 | 2025-10-05 04:44:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26df9e41-4e04-3c96-9193-f30d71618734 | -6.06938 | -46.0778 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e9bb0d7-7fdd-3f41-86c4-b2172c2a48b6 | -6.40773 | -43.06083 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8ef9047b-6b1e-367c-affc-587698de9fa5 | -5.92165 | -43.33187 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77e853cc-ab54-3b20-9dd5-9d37a8ce285c | -4.87999 | -45.07925 | 2025-10-05 04:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28b670fa-aec8-36ac-aba8-ea48d800da34 | -4.11115 | -51.09038 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61d65508-dc50-340c-ad06-9a107175203d | -4.44162 | -43.23342 | 2025-10-05 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f9683844-d204-34dc-a820-8c9e9bfd9e45 | -5.76708 | -45.75848 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17b14d40-e0d4-38a3-9092-68cc7a890807 | -6.40724 | -42.69022 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 87299a62-45ff-3957-8752-562530e0dd9d | -6.14541 | -44.64453 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 34056b50-3917-334e-bec0-29710f15ed57 | -4.44752 | -43.23532 | 2025-10-05 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6d9537d7-5af8-3806-b82b-2986815d4669 | -6.40536 | -43.0655 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc0b0c87-466d-3017-ab58-a7a12983b958 | -6.12736 | -42.86527 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8dbb8d81-a28b-38da-898e-40ce7cf27ed1 | -5.60147 | -45.811 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae7173c7-6bbc-38f9-8d5c-e9757e1a2956 | -6.35406 | -41.64037 | 2025-10-05 04:44:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e64e2946-05f5-3b52-9cab-652b07d83ff2 | -4.68764 | -46.82432 | 2025-10-05 04:44:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12cde666-5a6d-308d-a8ad-de0a1478b68e | -2.90446 | -50.73485 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cc50763-1ff5-3e73-99f8-83612109ad41 | -3.78072 | -51.97298 | 2025-10-05 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a1f968d-20a5-3f49-969d-9ceffd349eac | -5.46599 | -42.79205 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| dc3d9eb3-cdd7-373f-a3ff-46e1978df284 | -4.42854 | -47.60017 | 2025-10-05 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bf5d844-3952-3613-a858-7ccd6b49a68e | -6.37429 | -42.89083 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a54fa8c-b74a-350d-b527-720f935215a8 | -6.70631 | -42.15491 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| baf56462-feff-3576-9e1e-02566b4f7e49 | -3.6451 | -51.86722 | 2025-10-05 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79358cab-edf2-3806-a8de-0867c8633f8c | -4.25221 | -48.56378 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ff995236-159b-3c77-9c0e-263cd67e8569 | -5.91429 | -42.52199 | 2025-10-05 04:44:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b6d5aabf-8721-3d58-85f5-08b4f177aeaf | -5.87621 | -42.53485 | 2025-10-05 04:44:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2011d8ba-3d96-3832-81a9-54e88f416f28 | -6.24888 | -44.21461 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef90529a-47d8-387b-bdd0-c83dddc30832 | -3.81336 | -53.83797 | 2025-10-05 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb7f49ce-1096-30fb-a568-44f6d3fd4ace | -3.83808 | -44.55035 | 2025-10-05 04:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d80ffe00-f165-3937-b4ef-f24b3fc6ea12 | -4.56483 | -48.60689 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f8ec9b2-0b0d-37e5-9670-d7380ceb6acd | -4.22772 | -46.75682 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58943da1-76cf-3157-b071-53a18c2965c9 | -5.91757 | -42.89135 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d07fbc1e-7343-3077-9a81-39e7a5bab8c1 | -5.2573 | -42.97434 | 2025-10-05 04:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1ad4c3e3-7d4b-3218-930f-9d9de2dde5d0 | -5.51997 | -44.20367 | 2025-10-05 04:44:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be48f7a0-7700-3c1b-8ae2-96f255f300f7 | -2.25186 | -47.87748 | 2025-10-05 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f29ccb99-6f9b-39dc-b192-55498e486c21 | -3.8412 | -44.55015 | 2025-10-05 04:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a326c1d-0bd5-3368-8793-b21f5e508bfa | -5.88457 | -42.90979 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b4da0e91-1694-3184-a2af-5db1271ed7ef | -5.4522 | -43.15958 | 2025-10-05 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 589adb3a-783c-3ce5-85b1-c7b35678b676 | -4.81275 | -45.03477 | 2025-10-05 04:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README74.md)
