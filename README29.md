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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05b204e5-4627-3911-9b5d-6f3ff270605a | -10.1995 | -42.45184 | 2024-10-26 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 98b8104c-404a-38c6-bdeb-029f7766c8c7 | -10.1988 | -42.45608 | 2024-10-26 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e73c1eb5-6369-3e29-a713-251f8388c2ea | -11.88928 | -43.06378 | 2024-10-26 03:55:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6fe94b21-200c-36bd-90ea-6924edb0f4c8 | -11.88637 | -43.05879 | 2024-10-26 03:55:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| ad1fbd3b-9f79-32d9-94ad-7aba3403ef49 | -11.88563 | -43.06314 | 2024-10-26 03:55:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 5b44a3c0-c213-3627-a6a3-2144a79cd67a | -11.80752 | -42.83829 | 2024-10-26 03:55:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 76c3d0ff-f315-3ef8-b139-d223b0fc1926 | -4.62717 | -42.84587 | 2024-10-26 03:55:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4d09112-370f-32de-8016-288132cd2672 | -4.62318 | -42.84524 | 2024-10-26 03:55:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b5304c2-ae0c-3813-8e64-3810ac5eb57a | -4.48562 | -42.8946 | 2024-10-26 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5aad1d86-27e6-3804-8576-16ec5db11a1a | -4.48503 | -42.89809 | 2024-10-26 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c44e066-2e9b-3140-b6bf-70cda3a336b7 | -4.48445 | -42.90158 | 2024-10-26 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 09854097-40b2-34d0-a525-d4141a76b23a | -4.48387 | -42.90505 | 2024-10-26 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0f22f03-5e09-3835-a720-301fcd8935e4 | -4.47985 | -42.9044 | 2024-10-26 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb6318ce-9672-383f-a426-fdc92699b06c | -4.92187 | -41.97564 | 2024-10-26 03:55:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 48128db9-c0c3-3cf8-bae6-9688f84eca2c | -6.21467 | -43.28011 | 2024-10-26 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a8c0b50-7eff-37fd-b156-739de866c7f3 | -5.95201 | -43.27858 | 2024-10-26 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 53dcdea1-3a05-3e7c-adab-785cf9f0eb1b | -5.83584 | -42.77113 | 2024-10-26 03:55:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3eb80097-1ec9-357f-bec4-fdce41dbb958 | -5.83504 | -42.77596 | 2024-10-26 03:55:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fe1b675f-6a65-3d33-b350-5fcee3887e98 | -5.81173 | -43.21239 | 2024-10-26 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 05463af3-7c3f-3d4e-b49d-4691afe2ab0d | -5.7819 | -42.63306 | 2024-10-26 03:55:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 65df2f18-7ad8-3e72-bbf6-7d383d987a62 | -5.77495 | -42.62692 | 2024-10-26 03:55:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7e216a09-e0a8-3757-96d9-71c4fac8e9a5 | -5.76336 | -42.6248 | 2024-10-26 03:55:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 234a6d3a-635d-31d7-8528-2b1dff20e278 | -5.69122 | -43.1842 | 2024-10-26 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3268b40c-cf6f-357b-a971-5193d4446466 | -5.69064 | -43.18771 | 2024-10-26 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ec89feae-1af7-37dd-9f25-c51683e5ff2c | -5.6548 | -42.69577 | 2024-10-26 03:55:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6f057f75-fa8f-33d3-b2c9-15b0bc590300 | -5.64883 | -42.7564 | 2024-10-26 03:55:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03dbcab5-2e10-3730-a53f-eb559ba6c181 | -5.63378 | -42.77452 | 2024-10-26 03:55:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| daa15e27-6ba0-376c-8a5c-4a7d8c7dcff4 | -5.61977 | -42.76196 | 2024-10-26 03:55:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3fd19067-1a77-36c8-827d-0959e7c6ef1a | -5.54747 | -42.8099 | 2024-10-26 03:55:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 147cbc5d-10f7-328f-9fa7-b1f902879819 | -5.41567 | -42.82725 | 2024-10-26 03:55:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a7befb5-1155-39ff-9ac4-35023acdc568 | -5.323 | -42.97896 | 2024-10-26 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a7bb33dc-80b0-37e7-96ca-ff6817345d16 | -5.32243 | -42.98247 | 2024-10-26 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 19cc3ee4-9929-3321-8175-25e263cfba3e | -5.48365 | -42.08293 | 2024-10-26 03:55:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 88d64343-7e7c-3c77-99b2-8bbd2c2afb18 | -5.48289 | -42.08751 | 2024-10-26 03:55:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ce474bf3-8d75-3133-b88a-4ba465f3a096 | -5.48286 | -42.08467 | 2024-10-26 03:55:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d2027ff3-2cd5-3c76-b35d-997774faa0eb | -5.47989 | -42.08231 | 2024-10-26 03:55:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 544dc0db-934f-389a-80bc-e652bcef6450 | -5.47912 | -42.08689 | 2024-10-26 03:55:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 721d44d6-dc1e-3d99-9919-94780da1927d | -5.4791 | -42.08404 | 2024-10-26 03:55:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 20adf994-3f67-38ee-a34e-8e6d8dde5097 | -7.68471 | -42.64053 | 2024-10-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4d5f1bb6-f1e7-3216-ade9-c561e0a40d3c | -7.68394 | -42.64513 | 2024-10-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ac259756-8b7f-3324-94f8-16939c05629b | -7.66299 | -42.95535 | 2024-10-26 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| df0e035b-d37a-34b7-8725-cc1409574de0 | -7.61297 | -42.29308 | 2024-10-26 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 834c8930-34cb-331d-951a-64aed0f70949 | -7.61225 | -42.29752 | 2024-10-26 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 386f472d-2019-326e-95d7-fc8f08bf825c | -7.60926 | -42.29249 | 2024-10-26 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6e3fe4dd-1e1b-37da-9abf-df03bfc2ec09 | -7.60854 | -42.29694 | 2024-10-26 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a7f0c837-67a2-3bc3-8a74-d2fb0f2219bc | -6.80637 | -42.40345 | 2024-10-26 03:55:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 33164f5a-d3e4-3040-aba6-14c85dc3d557 | -9.18505 | -43.24831 | 2024-10-26 03:55:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6187b72e-34aa-3d0c-a71b-e68533f76d95 | -9.1812 | -43.24774 | 2024-10-26 03:55:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f84007eb-f382-33ed-a07a-ad82d0fd19e2 | -9.16118 | -43.15657 | 2024-10-26 03:55:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4ce6bea0-e2eb-372b-97f7-334a5e526feb | -9.15738 | -43.15587 | 2024-10-26 03:55:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b18a5570-6311-359d-8097-30da4a9c2f4a | -9.10499 | -43.19308 | 2024-10-26 03:55:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6e18fb5e-50cd-31b0-ae01-3813fb81a9bf | -9.10358 | -43.19516 | 2024-10-26 03:55:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a367fe66-b8da-34f9-9b7a-786a3554c34e | -8.32952 | -42.80676 | 2024-10-26 03:55:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bdc567f8-90a0-323f-a435-ad0f838050a7 | -9.60923 | -42.92417 | 2024-10-26 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e17aaea5-6e1f-39eb-82f0-bdc77eb0894c | -9.60845 | -42.92874 | 2024-10-26 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| acfa389b-373b-3471-9057-7f4919a0d110 | -9.60704 | -42.91445 | 2024-10-26 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a1cc37f7-978a-31a7-b9dc-8c3c7b8eccea | -9.60628 | -42.9189 | 2024-10-26 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3fe054e0-515e-39dd-84f2-131ff980f79d | -9.60551 | -42.92342 | 2024-10-26 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 779f781d-173b-30a9-acea-1b015a7ecd2d | -9.60473 | -42.92802 | 2024-10-26 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d87ef755-f117-3d1f-a882-a5d06230c7ac | -9.60394 | -42.93266 | 2024-10-26 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9e77f230-a73a-3649-b279-697a59380b6c | -9.6002 | -42.93203 | 2024-10-26 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b718797c-925d-3d2f-b8d2-fbc84718dd2e | -9.59646 | -42.93142 | 2024-10-26 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6b551883-b261-3935-947b-2c13f6925d20 | -9.47385 | -42.98794 | 2024-10-26 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bdc47ae1-040f-3d1c-a029-a52077daad19 | -11.90781 | -43.81936 | 2024-10-26 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e487c207-a131-36fa-8b22-949fe471be9d | -11.904 | -43.81869 | 2024-10-26 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a7af324-3e00-3665-b0cc-b48b407da1bf | -11.54044 | -43.98668 | 2024-10-26 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54652433-5315-3cd0-9f1f-5d63ed70b31d | -11.5396 | -43.9916 | 2024-10-26 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61b5e9d4-2f5e-35c4-9fd9-2111950ed77f | -11.53658 | -43.986 | 2024-10-26 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 171475fb-c24a-3201-a770-4e29ededb8ff | -4.22321 | -44.53551 | 2024-10-26 03:55:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1044447d-f807-35ba-9c8b-26f4ea73d686 | -4.20423 | -44.24717 | 2024-10-26 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9d9cd30d-a46d-3eaa-add9-36c794ae8073 | -4.20054 | -44.24205 | 2024-10-26 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7d0f15a0-81db-35f0-84fc-543be2e0ef5b | -4.19981 | -44.24643 | 2024-10-26 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bf645038-c9c7-3515-acb6-08ee18792544 | -4.19908 | -44.25082 | 2024-10-26 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 246b453a-8ebc-3236-a7b3-7f66614ae5fd | -4.19612 | -44.2413 | 2024-10-26 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a95394e8-c9f7-3d79-a558-90565b5ba3a6 | -4.1954 | -44.24569 | 2024-10-26 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d635e0e3-732d-3444-94c2-bb9b43d82d22 | -5.06863 | -43.66504 | 2024-10-26 03:55:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 49e6f710-26ea-36c1-ae8b-ae11d914d962 | -5.06799 | -43.66888 | 2024-10-26 03:55:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aba309bc-ca8e-3521-b919-9029dc60e9cc | -5.06736 | -43.67273 | 2024-10-26 03:55:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e46fc425-44fb-3f49-8483-478af975f77f | -4.74332 | -43.25349 | 2024-10-26 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 969cb533-e7b9-32c2-b62d-74c27eb3c5fc | -4.74271 | -43.25714 | 2024-10-26 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e511ced5-0a73-3940-8840-36ea2c5ee1c5 | -4.73982 | -43.25317 | 2024-10-26 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7978aa21-4dd9-3b85-9230-6e147ed5bf2c | -4.73922 | -43.25288 | 2024-10-26 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55d772c4-6c5a-3381-a875-d7b42e24b81c | -4.52567 | -43.43216 | 2024-10-26 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17e5e5ec-bdd1-3ac2-b0ba-9ba61eebcec2 | -4.52097 | -43.93715 | 2024-10-26 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e80f8dcf-98e3-37b4-9ce9-fb7297dfafe1 | -4.92119 | -44.10045 | 2024-10-26 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a687511c-3107-39ab-b069-26b53ae5bc05 | -4.91936 | -44.10016 | 2024-10-26 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bd497512-5253-3f6b-b2d9-4ad12b0fe317 | -4.91868 | -44.10429 | 2024-10-26 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfc5d550-1fa7-3884-8bbf-a1999441a63a | -4.91504 | -44.0994 | 2024-10-26 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2843cbb8-79d6-337d-9c2b-bc049cc35d1e | -4.91437 | -44.1035 | 2024-10-26 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d3038b3-22aa-322d-9619-fa831848f750 | -4.73046 | -44.39788 | 2024-10-26 03:55:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| aef1603b-da4e-3723-a6d3-63879e3766fa | -4.72973 | -44.40228 | 2024-10-26 03:55:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f6a4a82e-d12c-3a76-90d5-37f97bbac11b | -4.72605 | -44.39709 | 2024-10-26 03:55:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 82c8bd37-0fcf-3d1b-85c8-6fe94bfceef7 | -4.72531 | -44.40151 | 2024-10-26 03:55:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 34186431-9b85-3e84-b9bc-10576564508c | -4.70253 | -44.48363 | 2024-10-26 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f34c013c-fe65-362d-a00c-ff75200c67b4 | -4.69806 | -44.48298 | 2024-10-26 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 629fae69-d183-37db-aa7e-e277b381e4c7 | -6.47006 | -44.01872 | 2024-10-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3e20340-32f9-37e0-a8ef-d28c989ecfe7 | -6.45527 | -44.68018 | 2024-10-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9ef181c-94d4-3f6d-acfd-6f557db1fd89 | -6.45125 | -44.67929 | 2024-10-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21672c59-270b-363f-91c3-392a385920c3 | -6.45085 | -44.67962 | 2024-10-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e93827d6-8179-3692-9d21-8ebd6650fb4a | -6.40584 | -44.52101 | 2024-10-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README30.md)
