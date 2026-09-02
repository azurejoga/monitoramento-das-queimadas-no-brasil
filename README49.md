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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49211414-44e3-3291-a9bf-074beef2b13e | -3.1928 | -61.1427 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e24571af-3c10-3a42-9c77-561d3486cabd | -5.85615 | -57.55447 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ea35174-8fd4-3dcf-a9de-fa696697a49a | -5.2515 | -55.88848 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 801c9ae3-f030-337d-aeff-cfa92adfe029 | -3.97616 | -55.64157 | 2026-09-02 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c19a3e89-136e-38a3-aa1c-4c0c4169808e | -6.1285 | -56.3815 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 374ee125-11b9-3784-99a9-832eb8dca50f | -6.69479 | -59.94781 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ff6f3ce-db4f-32e3-b77c-cd7169ac9ab2 | -2.50442 | -48.13513 | 2026-09-02 05:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d999d333-1a4d-3dde-9f13-ae0d312d3fee | -5.25208 | -55.90698 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ede70bf8-8247-3015-9fe6-f91d0200139d | -6.09807 | -57.69939 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 157793fb-9d8c-320c-8bef-b998659e76a5 | -6.0422 | -53.84568 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7a3f25c-d8fb-34c0-a657-12954377ee62 | -9.42957 | -45.61747 | 2026-09-02 05:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e51b131-fe45-35f8-a0f1-e8dc3f1b51fd | -6.80176 | -58.7418 | 2026-09-02 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc4d9956-e154-3356-a0dc-4dbd772c9aa9 | -6.95683 | -59.78278 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ec96295-0d62-30f1-b83f-1ec330e89fb8 | -6.19204 | -55.28178 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4810427c-62b7-3896-8584-de289b637bbf | -3.61856 | -60.54736 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 87c98bde-27b2-3a44-87c5-4c74944dd586 | -7.19952 | -60.66972 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2254704d-7637-31e5-8571-a8f3f97a26a3 | -4.4971 | -45.90874 | 2026-09-02 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0004a40a-d089-38b7-bf8d-0d2b0a3ed978 | -8.50615 | -55.29821 | 2026-09-02 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 773bd955-16c1-34c7-b538-49cf5bdf0f7a | -8.44704 | -54.71802 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4260ffa7-679a-3090-a167-5728c6fb83fb | -5.85561 | -57.55793 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46233f07-1454-358e-9848-5f5df901ae5c | -6.76982 | -59.44337 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff755cc9-4351-38db-b0dc-0bebec25c00b | -8.43441 | -54.70311 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 68b2bd94-0445-32d4-a545-fd0e0c5b6249 | -7.20396 | -60.68714 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aa7e3ec-4736-3cdd-bb1e-4f972c3da8df | -5.87787 | -57.78101 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51358e30-2ae5-36e5-8a53-095134bfffa0 | -3.066 | -61.20407 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00d45bec-879e-3855-a218-3e14a0e532cb | -6.08926 | -57.71217 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7e0ab24-3b25-305e-aaa0-2b3b1da271f7 | -6.75959 | -59.44175 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ebc9379-4b9c-3e34-8a6e-999715bc516f | -1.43199 | -54.23087 | 2026-09-02 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ddb0ed5-7473-31ce-be8d-889add00053f | -6.00328 | -57.82608 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f45e42f9-42b8-330c-add3-6a3dbdf5b8b4 | -8.43677 | -54.7121 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e44cd67f-0a44-3f49-a6e3-6cd87f0b838d | -6.82082 | -58.87265 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed9454e2-a645-3b58-bbf9-9177b9a6e9f2 | -5.97649 | -53.59127 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdc6fe4e-5106-3778-b86c-06a682717fcf | -6.11688 | -57.75199 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e58a467a-16c7-3fab-bbb7-baf613a7f666 | -4.54397 | -54.91496 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 129b8f65-cb2f-391d-a86c-1616e16d2d9f | -6.08264 | -57.71112 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c50c6098-7f51-3655-b6df-3b67832aaa3b | -6.19768 | -55.43015 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dac1f904-7b9d-362d-8fc1-152342d35613 | -8.44405 | -54.71321 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e52f029b-55f2-347c-8c07-b2a6323091fb | -6.12067 | -57.68525 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7195a783-ae9c-3133-bcf6-4f385c53877f | -4.35561 | -55.02554 | 2026-09-02 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8aab401f-c7ff-3f3d-aac7-ff6ff9e75421 | -8.25795 | -54.95653 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aca43870-f458-34c5-9b49-384053bdd961 | -6.14907 | -55.67825 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a28da767-6af5-3699-867d-81cbe08a9dd6 | -4.11629 | -51.02634 | 2026-09-02 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 23f3ca8a-6aae-3f22-8e99-9dc2aa59eaef | -8.44534 | -54.70471 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56da2a62-57eb-3cf1-bfec-713df4fb0e87 | -4.9703 | -55.84595 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84e59598-17e3-32b6-baba-aec53b39d2f9 | -8.44899 | -54.70526 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c107ec5-2ee8-33a1-b918-f7d6e8978f57 | -6.1329 | -55.64662 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04969e0b-0991-3c82-ac6a-1c44eb7a4d7a | -6.93072 | -59.64023 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e25fe009-69fe-3301-9ac8-a3377b881992 | -4.69628 | -56.05494 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3655c1a9-3355-3da7-904c-79fafe669426 | -5.95517 | -57.68026 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7d49c09-a173-310f-9c7a-4deb5852f773 | -5.93141 | -50.21217 | 2026-09-02 05:16:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eabc90dd-0ab3-3c50-aeb3-e7c2a703798f | -7.19663 | -60.6651 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 616b9cfc-83b7-3373-a41d-a567dc107870 | -3.11236 | -61.23636 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cbf9e7d5-9485-3387-ad2a-214b76c52171 | -6.85513 | -59.47948 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3b343b8-fbd8-3c9a-bd18-461444ded7b2 | -8.28623 | -54.93961 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b202d14d-5b13-3217-9072-e88a4c0d63e1 | -6.70823 | -56.34344 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1a67088-29b8-3c9e-a1f7-db2d4c67e5c7 | -8.43741 | -54.70787 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e7bed3e-61d9-38ab-9f45-3a43c0019649 | -7.57389 | -61.30277 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e50f069-b241-3516-b9e5-7370940ddbff | -5.17945 | -60.29005 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 866f3925-fab9-33cf-93f8-cd69b59dc769 | -4.21983 | -56.082 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2edd0802-f628-3d19-b602-4b8abe194fa5 | -5.95462 | -57.68372 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1996440-0808-32a6-8aa0-1a589a18aa48 | -8.44768 | -54.71378 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39c8e7d3-8cb3-38dc-85f5-9f6d695aa665 | -3.36252 | -59.40438 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86668ec4-1966-3896-84ad-131c4af42337 | -6.10594 | -57.86368 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4ba4585-e153-326a-bee2-6620bf306eac | -7.2978 | -60.62255 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8676d85a-2a75-3960-b291-cc568b202a4d | -7.54975 | -61.31203 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 031a1a3c-b98c-3ed3-a2f4-59ca0250f745 | -8.44513 | -54.7328 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0c19216b-fdef-3f33-91f5-24d4400a41ce | -6.12286 | -57.67144 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 156f030d-cefd-39d4-b07a-8d4668152af0 | -6.2023 | -53.47957 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 45e1ae6f-dc50-3ec0-8f33-78fdd370fbfd | -8.29169 | -54.92788 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40dfc551-f9ad-3341-8f0b-b1edd575b4c2 | -5.85891 | -57.55845 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 945b687a-348a-3bb1-9dbe-8868446ebe42 | -4.09756 | -60.66068 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09ce8e23-11e4-37f2-aff9-af052e2ff988 | -8.26154 | -54.95707 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9ed7b0cf-43ef-3705-a0ec-34391837d37d | -1.59229 | -50.4334 | 2026-09-02 05:16:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 935e2bf2-a3f2-37ef-b1c9-40074e614428 | -5.25264 | -55.90339 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05e82e89-3998-321f-8f04-acd8e558a427 | -3.14385 | -57.66806 | 2026-09-02 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dadbad3-6b87-3e96-a9a4-ea948fb01e22 | -8.26994 | -54.95005 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68859dc6-f23f-386f-9179-69fc73025a28 | -1.46703 | -52.96433 | 2026-09-02 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba093144-f9ba-3ab8-ac24-0541bc7d12f5 | -6.18485 | -57.73125 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bab0b6a8-e8a0-33f2-95ca-e80499977cf8 | -3.57467 | -58.74521 | 2026-09-02 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d2ae65f-4911-3044-a313-aafa78011322 | -8.43119 | -54.72428 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4f13bf1-56d6-3c71-8207-140f27bd0de6 | -4.26894 | -55.15355 | 2026-09-02 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad8058f6-ad7a-3ddc-8cf3-46702eec779d | -6.11791 | -57.68127 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04eea4c0-5bf5-3bc5-a1ea-a2019493aaf0 | -7.29486 | -60.62321 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3629e281-7629-383f-a12e-1bf1badcd7ed | -5.86142 | -51.71275 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64390065-b986-3a91-97ca-959cff243443 | -5.57503 | -60.19196 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51174d0b-f61c-3ab5-9c29-232e22b19820 | -5.25097 | -55.91417 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fee8149d-a84b-3c36-8506-e04961745d7d | -4.2678 | -55.16092 | 2026-09-02 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07c9d4a9-b6dd-3ef2-9b7f-ad8408e4faea | -8.70582 | -52.36342 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47f0c8ec-fe4b-338c-9a5e-8ae484e00182 | -2.83831 | -49.51648 | 2026-09-02 05:16:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bff4b3f-125a-360e-93e3-ffa4cbd49868 | -6.18504 | -55.46665 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2872da0-387e-3e7a-a7ac-7a8f2afe544c | -5.97785 | -53.58227 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 818b4035-9bd6-3e95-891f-f544ca9bb269 | -7.32996 | -61.14644 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b881115b-22e9-3e14-8844-fffd91f59a2b | -5.17808 | -60.28848 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 28cabeb4-cf0d-3244-9e17-dc27bc6a914d | -5.25432 | -55.8926 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d690d57c-be1c-33e6-bc89-7d1cbe62a11d | -9.00213 | -50.78006 | 2026-09-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d6d0f5a3-7719-3a06-9156-1cbf35ddd4a8 | -8.44662 | -54.69635 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2c55338-6dd5-316b-93dd-4db1dfbcb38d | -6.77772 | -56.29543 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1173b726-4f83-35e1-bca7-8633c711d012 | -3.84802 | -52.03823 | 2026-09-02 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de1169b3-48fa-3efa-a927-e6e017d98b23 | -5.85285 | -57.55396 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 343dc1cc-723e-3a73-8948-c54c87ceea24 | -3.63317 | -58.4077 | 2026-09-02 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README50.md)
