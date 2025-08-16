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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef97ad32-7f88-3198-967e-6b7078f36141 | -8.9868 | -60.550598 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6144e6b6-1b63-38cd-9e22-b35facc9c972 | -8.9957 | -60.500702 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adaf0bbc-85ff-334c-886c-841e00a423f4 | -9.2136 | -59.6278 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0df31a2-a4f4-3d48-978f-e5dbb10d088a | -8.9993 | -60.5158 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71214d1c-fa6a-3a27-ae90-d628ac41f5d9 | -9.5142 | -60.553799 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 621c42e1-2a7d-33d6-9847-212917a4a257 | -14.9806 | -54.7155 | 2025-08-16 01:39:00 | METOP-C | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 954aa12e-8149-3ce7-8731-767da4e3919c | -8.9903 | -60.565601 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2108d2ca-c7b5-3f39-99d6-e3a3fa0b3fe7 | -8.47 | -64.054901 | 2025-08-16 01:39:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e9e52b4-360c-3cb1-b649-4100dbfde0fd | -6.9531 | -59.545898 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ae393c8-512d-306f-8ed3-cbc0ac7af6c5 | -7.5325 | -61.310001 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20812fb6-4e73-34c0-838a-98ba27985e77 | -9.1647 | -59.6394 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0328c9ce-e8d6-3d3e-b698-323da67b9ab2 | -14.9452 | -54.739201 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 03ff14cb-b1f5-3197-8199-9edd97d27737 | -6.6289 | -60.0089 | 2025-08-16 01:39:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 033632fb-e6aa-3ecb-a871-0378737f12a9 | -7.5261 | -61.3269 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b54c432-3780-3a0f-a38c-048cc9276e20 | -8.0439 | -61.511501 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06752b3f-dd79-328c-81db-8e64a99970a1 | -7.6275 | -63.337101 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 853f497a-58e0-3bb6-ab2a-9dca035ce886 | -9.0028 | -60.530899 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb42621f-aec8-3b2a-8416-17d02a9d6108 | -9.2213 | -59.6605 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd121bbb-fa8e-33c4-aa27-532ad20c55c0 | -9.1745 | -59.6371 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 230c8067-cc34-396f-b860-91b473d73118 | -8.9859 | -60.502899 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18492beb-55fd-3cc8-af42-299a95da5252 | -8.6744 | -62.456699 | 2025-08-16 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 40bb6fda-df5a-3581-babb-5271ce467f20 | -9.5044 | -60.556099 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 876cea90-b38c-3ae5-b3ee-4ef1c71cb0f6 | -7.6832 | -63.3102 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ade06e4-f2dd-3ebf-9c30-d96108362425 | -11.3486 | -55.416199 | 2025-08-16 01:39:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc89b9b7-3294-34aa-90fc-fca48e501e35 | -6.143 | -57.925301 | 2025-08-16 01:39:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74794620-39af-3291-aad5-41decb079db8 | -9.5054 | -60.516399 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4eeb174e-0a9a-3e97-be5d-c650af2d3d8e | -7.8369 | -61.331699 | 2025-08-16 01:39:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77fdb047-d583-3fae-92ef-11dc12ee445e | -9.5062 | -60.563599 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 629c6894-0152-3195-9932-95f7c367dbec | -13.479 | -61.000301 | 2025-08-16 01:39:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c4bc7da-90cd-379e-b5a5-2919c62c11f1 | -9.0073 | -60.505901 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b16bb493-e2c7-31d1-8c86-7314db108506 | -11.3715 | -55.424801 | 2025-08-16 01:39:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd30d835-ada0-39b9-baa3-b987912e5fc4 | -9.1764 | -59.645199 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 146c2851-b931-37ea-a73f-8f2a583ad91a | -9.2194 | -59.652302 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eda8d317-11fe-39c9-b9a1-1b00b14e180f | -6.8006 | -59.817902 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d78b115-b7ad-36d2-9e2d-a0112b114c6a | -7.9102 | -61.7369 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e90308fa-d494-3d1b-b6a7-79204b1c62c0 | -7.4586 | -59.937401 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00660ea8-6e04-3770-8298-08f1ff0b0f1a | -9.1861 | -59.6861 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37c33fef-e603-3e42-b536-c5ccfe37ea6b | -9.0011 | -60.523399 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2ff980-697a-3ccc-8ee9-2cc2a904c003 | -9.071 | -58.941399 | 2025-08-16 01:39:00 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddc592a2-6ab9-33b6-a9ce-3c9d2d173ad7 | -8.98 | -61.721001 | 2025-08-16 01:39:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b26bdc18-72bd-384b-9221-244128a423a0 | -7.95 | -63.213902 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c57055b-2ef5-3747-9fa8-a1c5031741a8 | -9.5187 | -60.529099 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0240e567-7dfe-310a-85d6-3a867c40563b | -13.4431 | -56.674801 | 2025-08-16 01:39:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6add4cb1-826b-3d28-aba3-8b2eac8a6253 | -6.9433 | -59.548199 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8dfb798f-b6af-3c75-bad8-07ff7f8fdecb | -13.132 | -57.1353 | 2025-08-16 01:39:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96f7a48e-cf14-3261-9c6d-ad8a2f7ad8f4 | -7.9233 | -61.748798 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4cec4dc6-f236-341d-a548-9b59b8645cd8 | -9.3879 | -60.5439 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2d2cd70-dfa8-3892-ab00-e0694c13e2f1 | -9.5072 | -60.523899 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 979bd19b-8342-34ce-902f-1301070fed0c | -8.898 | -60.745098 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7db2aa11-acfb-3fab-9357-3b4e1e00f19d | -14.9384 | -54.7127 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ceb40fd-8169-3718-a16b-79751f26126e | -7.437 | -60.0205 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca8165d5-92ba-31a2-a4da-82131e0b4be3 | -9.5089 | -60.531399 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea277e1a-c238-3ac9-aec3-ca80809cfee3 | -7.8254 | -61.326698 | 2025-08-16 01:39:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac99370-6250-3a72-aadc-1b4f8121b9fb | -7.6243 | -63.323399 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65f0284a-e72a-3eda-9329-d78a233a20bf | -14.9447 | -54.696899 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6181f5ea-a8c4-3e24-9c6e-1d70f9f156c0 | -8.9975 | -60.508202 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5588166-e296-344c-addc-afafe00d70cd | -9.517 | -60.521599 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a55c4fb9-0de0-3a59-8d76-ad1e796093ad | -9.1706 | -59.620701 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15517630-0e5e-3060-8530-0293fb97aba5 | -8.9141 | -60.7257 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74c2e104-eda0-32d3-8b3f-8ee1f9714064 | -8.9784 | -61.714001 | 2025-08-16 01:39:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 26432414-69ca-36cf-bd3c-885bc7187bfd | -9.0379 | -67.428902 | 2025-08-16 01:39:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e1dad09e-1fdc-3cfe-afa4-2cb2a52694f5 | -9.0055 | -60.498402 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01422073-6689-3eb6-9022-2a0ac02dffca | -9.2058 | -59.638199 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 535ca0ee-e668-3507-b420-fbed9754ed0a | -8.114 | -61.191101 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3327af1c-e68e-3453-a5b9-66ce3edb6a50 | -8.9948 | -60.540699 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc54dbf1-514a-37c2-9f36-3b57c8129e7f | -7.675 | -63.319199 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8f91758-6d4a-377a-b450-71e620b8a951 | -8.1482 | -62.771702 | 2025-08-16 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 586d4d64-7c6b-3173-98e8-ff5a3baca045 | -7.4991 | -63.815601 | 2025-08-16 01:39:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d17e6fa-a09b-3a75-b8b7-66b7aa28e665 | -9.1705 | -59.663898 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b8c1168-c0b9-3523-9c06-7e50b4ec096d | -7.4291 | -60.030998 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bbcb278d-5037-362c-8371-3d4874e8d184 | -9.2078 | -59.6464 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 092d199d-2691-3c3b-ba8f-128140430908 | -11.2749 | -50.4953 | 2025-08-16 01:39:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 439562bd-dc03-3468-b3e9-bf76ec420f9b | -8.9078 | -60.742802 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35904d50-1628-3b04-8a9f-1e21bc3e90e2 | -8.5556 | -63.9319 | 2025-08-16 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86d41d8a-1fab-3a39-99a8-a48987ab9438 | -14.9646 | -54.734001 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cb21531e-307d-32c1-bca0-f7fcb626369a | -7.9315 | -61.739498 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 078e2e1c-cecc-3c27-9305-cad31fa8761b | -9.1666 | -59.647499 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3936646-c0f5-3cd0-a284-cfe7835b7c91 | -10.4022 | -64.5056 | 2025-08-16 01:39:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3f03fde0-8c47-392f-a1c7-8e76e7c7c251 | -14.951 | -54.680901 | 2025-08-16 01:39:00 | METOP-C | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9dc50d5-4b3e-31ce-90a1-b6ae1ae0b551 | -7.9217 | -61.741699 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a2c8eec-1438-3128-9b2e-d8b2322681e2 | -14.9743 | -54.7313 | 2025-08-16 01:39:00 | METOP-C | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b88f5c9f-3655-397d-a3a2-dc522976f4d4 | -7.4567 | -59.929199 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14b2a6da-c9da-3686-b232-b1791369b2c8 | -3.8209 | -47.7444 | 2025-08-16 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 04fec2b9-780c-308b-b319-ec611b8ca000 | -7.9148 | -61.7478 | 2025-08-16 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 0e26d5ac-c4a9-30fa-b594-603f6d3c44eb | -9.1708 | -59.6568 | 2025-08-16 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 301e4a33-0e11-3674-af9c-b8ce7b356cc9 | -9.4992 | -60.547 | 2025-08-16 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ed76dca0-9a34-322c-903f-d76b88e86b78 | -7.9334 | -61.7281 | 2025-08-16 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 670cb784-2fe3-3b6e-a6fe-ce143d2d49c6 | -11.3466 | -55.4326 | 2025-08-16 01:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3c917474-eafc-396d-9a68-a9432cf8abb8 | -8.9709 | -61.6842 | 2025-08-16 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 106.3 |
| be4ba70c-5f54-39f3-b475-e4598a1790a4 | -12.5942 | -46.9527 | 2025-08-16 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| da4d0419-91cc-3461-bb15-3f61a4a30798 | -9.1711 | -59.618 | 2025-08-16 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eb6fc24b-cb20-3a72-ba6f-277b27f85279 | -12.6139 | -46.9273 | 2025-08-16 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 1e6d2b72-f66b-32aa-a317-ee69b3f252bc | -7.9149 | -61.7288 | 2025-08-16 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 530ccb39-580f-3cb2-9afe-eb6dff55d8e5 | -13.4294 | -43.6733 | 2025-08-16 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| e7e83a36-236a-3c73-b41c-1fb84f791d67 | -12.6135 | -46.9499 | 2025-08-16 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| a5117d59-1f27-38e4-be74-37ac83b52b99 | -9.2082 | -59.6354 | 2025-08-16 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 921ee2dd-e6aa-3404-b302-6d0b5375d26e | -9.0346 | -67.427 | 2025-08-16 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 3db15229-8054-3202-92de-193b9c445e76 | -12.5558 | -46.9583 | 2025-08-16 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 339.4 |
| 066c9ec0-58bd-3772-9394-baf9e99f4118 | -13.1267 | -57.1293 | 2025-08-16 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 665ffb7b-9902-32fc-95de-b4f1b7cee788 | -9.4994 | -60.5278 | 2025-08-16 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |


[Clique aqui para ver as próximas entradas](README15.md)
