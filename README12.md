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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a75bca57-c1bf-3201-9528-0565b98d6812 | -4.28932 | -48.27226 | 2025-05-24 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| acc56415-d155-34e7-9e9a-e475aacacc04 | -4.28877 | -48.27596 | 2025-05-24 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 48554fc3-b3d6-3526-98be-cbc28c2b1315 | -4.29347 | -48.27287 | 2025-05-24 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 3d4497e1-3eed-3cc8-b210-3eccce08e102 | -4.81986 | -44.35572 | 2025-05-24 04:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22667edf-6020-36d2-9df3-eeed1b02556e | -10.55196 | -42.42845 | 2025-05-24 04:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e9bd8ab2-2cdd-3723-bbeb-3579ce911ec5 | -10.71514 | -48.82579 | 2025-05-24 04:57:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1eab0e03-a0e3-392f-9069-da05fb070e54 | -7.65765 | -46.10292 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 392d9e28-2ca2-318b-b12e-cb71d79bb37f | -12.07097 | -47.34723 | 2025-05-24 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5661a2b3-d1bd-31e8-b346-a9d81a6faf06 | -9.37491 | -57.5516 | 2025-05-24 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6568c9b5-236f-36c2-a04f-004af7579600 | -9.08011 | -49.6659 | 2025-05-24 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bbc494a-8a12-3bea-9105-a9b2594b871a | -8.07914 | -43.11706 | 2025-05-24 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 2daa0642-4ee9-3770-87dd-3565dfa1d5e3 | -7.79497 | -46.22515 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0e8f83f-fccc-387b-9213-6f0c75883eaf | -8.37572 | -47.08976 | 2025-05-24 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8af2db19-7aa0-3e5b-a9b6-475ee51e9b3c | -7.6582 | -46.10758 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 896e0fbe-7cd6-3809-9ac9-308eae7888a5 | -7.54217 | -45.83134 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0da6aab-6dad-3222-b64b-1e6fe20a9a50 | -10.76946 | -55.265 | 2025-05-24 04:57:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6fcdf4e-3bf9-3b1b-bfef-e08a6689746a | -7.20921 | -43.1258 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1dee3246-76c1-3551-adfc-f216f272ccfd | -6.12904 | -43.94572 | 2025-05-24 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22643c7d-7754-3763-90c1-34723ec91d27 | -11.57763 | -47.61603 | 2025-05-24 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d6c91be-600b-3721-96e4-dc8613763ef3 | -10.72568 | -52.47345 | 2025-05-24 04:57:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9edb1843-8146-358c-8691-f78844dbbca7 | -9.07554 | -49.6689 | 2025-05-24 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7498a69a-9037-3349-a6e8-38e590bb7345 | -7.2018 | -43.13337 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 63b6c56b-a1ec-3a27-8e03-32ba55202b8f | -5.68541 | -44.12327 | 2025-05-24 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a9a9c2f-c25c-3030-a743-177a370ab499 | -10.54069 | -55.72189 | 2025-05-24 04:57:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb558b4b-fa3a-37a6-9e5e-fe4a39b4e291 | -9.37655 | -48.40199 | 2025-05-24 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed1db07b-e6b6-3248-8b0b-49a3f6ea081b | -10.36688 | -47.98298 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81c39ef3-ad5a-3b27-bc7b-d9d53b7d53a2 | -9.07958 | -49.66953 | 2025-05-24 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b959506-1cb4-3d82-961d-26be09b946fb | -6.61631 | -48.0138 | 2025-05-24 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35cf5414-d106-38eb-bad9-a401ed811b13 | -11.56035 | -47.45699 | 2025-05-24 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d79452f4-a8e2-3ec9-896a-8ae34b7439a7 | -7.57647 | -45.86753 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea5f408b-17ee-3982-bd0f-f15c55e90ebd | -6.70071 | -44.34898 | 2025-05-24 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b38fce73-90e7-3111-ac7b-edc5ba21d064 | -7.19568 | -43.13247 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ca889504-b35a-329b-ac98-15e63ff04805 | -10.36779 | -57.49759 | 2025-05-24 04:57:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2cd03768-1b1d-38c0-b649-4164a7bc55b5 | -10.46589 | -47.94031 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a8e158fa-f890-3615-914e-ad7ff6d29145 | -11.47713 | -48.02514 | 2025-05-24 04:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f9b8a9f1-6584-3941-b342-a5d5af7c94a2 | -7.21532 | -43.12675 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 69ee946c-a8d7-31cc-9a44-a02b5d1ba266 | -10.36162 | -47.98702 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7373240b-fa2c-3391-ac37-8ca89bf25247 | -8.75754 | -48.03952 | 2025-05-24 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4dffc516-daea-382f-9634-b0d0ba95834e | -11.56523 | -47.45768 | 2025-05-24 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e75701a8-3694-3366-a239-25b50e3a7229 | -6.22409 | -43.35525 | 2025-05-24 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec6c82b6-a712-375a-80e8-7710e9ca7e31 | -7.22879 | -43.11921 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 50da07cc-7efa-32ef-8b08-49d3a946a695 | -10.54895 | -42.43151 | 2025-05-24 04:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 474b1c9e-3268-3927-8ec1-838e47461613 | -10.53982 | -56.39034 | 2025-05-24 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a7f26e4-d3c5-3246-b170-c9c48409c5af | -10.95195 | -48.15368 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 272e5a57-46f7-314a-9d1e-8843f468e11f | -10.74586 | -49.28739 | 2025-05-24 04:57:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf6483e7-77e7-3348-82b7-c5c813aaee9e | -11.88287 | -49.19507 | 2025-05-24 04:57:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09458c7f-6e0a-3149-bcf1-fcc1dbe3c761 | -10.03227 | -48.6967 | 2025-05-24 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b6717236-9e91-389b-9bbc-b4b47fdc52cc | -10.53794 | -55.71785 | 2025-05-24 04:57:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12b4aa5b-ad2a-3219-800a-ab197e698835 | -11.1571 | -48.68084 | 2025-05-24 04:57:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99ba4c0c-9a7c-363e-8048-bdda343eb50f | -11.56305 | -47.45786 | 2025-05-24 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 85a81dbe-b5ea-30ec-a3f6-9966e013a45a | -8.07294 | -43.11623 | 2025-05-24 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| e110f292-b913-3520-ad19-784a16656541 | -8.74578 | -44.9233 | 2025-05-24 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a360bc75-b056-314d-950a-00d1a32207f4 | -7.65727 | -46.10583 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ff81354-df18-36dc-949e-c205a9e9a45a | -10.52784 | -47.58174 | 2025-05-24 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79400772-3c33-38a2-9832-7f2fd1190586 | -10.36652 | -57.50533 | 2025-05-24 04:57:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bfca0477-c32a-3e82-90d3-9a80293c6256 | -10.72216 | -52.47289 | 2025-05-24 04:57:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fcab89b1-0000-3f68-aa86-137d63e96ebc | -7.07099 | -44.93972 | 2025-05-24 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bbe7e6c8-66c3-3247-8a5d-83dad9244bc8 | -7.97336 | -49.69388 | 2025-05-24 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec50e2a3-24c2-380f-a7d1-f9395275ef85 | -11.47907 | -48.02938 | 2025-05-24 04:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e6fd176-4bb2-3254-a68b-4ecd9e30b632 | -6.23103 | -43.37473 | 2025-05-24 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4e5134d-ddd5-3714-9115-44b1a9fa46a1 | -9.38098 | -48.40265 | 2025-05-24 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f61804ee-7638-3c35-a575-9bda4dede42c | -10.36716 | -57.50145 | 2025-05-24 04:57:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| af6da7f8-4ab0-38cb-afe1-32d20557c36a | -10.3688 | -47.96863 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d564eb7-e4ee-31f5-afe8-5017aed2f790 | -10.36624 | -47.98769 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f244d3f4-3ece-3e23-bed7-271ade754c7d | -6.70227 | -44.35168 | 2025-05-24 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b356208e-3be0-385c-ab45-9f4ac2f76355 | -11.57695 | -47.6214 | 2025-05-24 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a9a9127-4fea-3430-a39c-cd70dd2af8be | -11.14529 | -53.92794 | 2025-05-24 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e94d72f7-190d-3a88-aeb3-50f6cd5bc285 | -7.21531 | -43.12586 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 52f3655e-46cc-38a2-96a9-13ad08446186 | -11.38987 | -47.96331 | 2025-05-24 04:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e3dbe55-183a-3f69-8b08-43e472f276c7 | -10.02729 | -48.7005 | 2025-05-24 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 037ac311-c84b-3417-9783-5b24d07a7340 | -8.75136 | -44.92402 | 2025-05-24 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11cf5e70-f731-3d23-a266-47c6581d9db4 | -7.20189 | -43.1342 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d85fd7d6-867e-30d1-b700-d36f0f316926 | -7.98681 | -49.68531 | 2025-05-24 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47886252-0621-3333-a7ed-fe40566dd739 | -10.93833 | -55.31355 | 2025-05-24 04:57:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d2aabac-d7ae-3f58-9211-7ffe30468a2c | -10.71952 | -48.8265 | 2025-05-24 04:57:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5c7d56a-d563-3505-b74e-797aa21990f0 | -9.41679 | -58.30424 | 2025-05-24 04:57:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d158b6c0-2b22-31e2-acef-e222460f5a8a | -9.80914 | -48.26151 | 2025-05-24 04:57:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53406ac0-e3b9-37bd-9ad1-177f94e9297a | -10.36751 | -47.97826 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77de5e56-fb77-34d6-9eb4-92f3918b8f43 | -10.93557 | -55.30952 | 2025-05-24 04:57:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8edb26e-a675-3b44-852e-675c45a8c4d0 | -7.22817 | -43.12393 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 945eecd8-d324-34db-94ac-3c51f8312a5d | -7.80039 | -46.22302 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24afe6fc-ea2a-3de8-959f-28dd4142d8d8 | -10.37151 | -47.98364 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdc86579-978a-3bd0-a913-7f81cafa9dd5 | -7.22206 | -43.12294 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8300b2e6-ca69-37d1-a715-0edc39f09f3b | -7.98333 | -49.68126 | 2025-05-24 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94199b4c-2cd3-3e8b-a2fd-fedffe725323 | -10.53463 | -55.71732 | 2025-05-24 04:57:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdfe7df9-be0d-33d1-9a84-d4085e195625 | -9.41751 | -58.29994 | 2025-05-24 04:57:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ea935e2-4ea7-3eab-9178-9397a451ae2c | -7.66271 | -46.10368 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0acfa292-11e2-352a-94ff-19ff4b8063c0 | -9.88729 | -48.77357 | 2025-05-24 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bc02dac-c2ba-373c-95f5-3876f95afe8e | -10.71953 | -48.82832 | 2025-05-24 04:57:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6dc555fd-6461-3090-89bc-d331764e4184 | -7.06806 | -44.93422 | 2025-05-24 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41a4df47-41dd-320a-be6d-eb869d73ee8f | -9.37614 | -48.40042 | 2025-05-24 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7015d60-135f-3ac5-bb10-8f717b40f6eb | -5.58115 | -45.19614 | 2025-05-24 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e653a513-796b-3858-abde-f52f9280931b | -11.62136 | -47.99963 | 2025-05-24 04:57:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26c84d3b-9b7d-3e56-8d67-7f6b95f484eb | -8.07232 | -43.12112 | 2025-05-24 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.5 |
| b319ed43-4b57-35b5-976b-ad565bc2a51c | -10.94796 | -48.14821 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be454612-fb2c-34c6-8fa3-c5f30ea817f6 | -7.22267 | -43.11819 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 40f9da5a-3242-30ee-9858-b40eadb2a0ab | -10.46987 | -47.94599 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe2d56ed-5168-39da-9718-cf9504903d22 | -10.30272 | -57.14178 | 2025-05-24 04:57:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 647ccea3-3030-338f-bb19-89cb53711a0d | -10.31333 | -47.04631 | 2025-05-24 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d0cb45e-79fe-39fd-b341-fa1de3496725 | -10.46523 | -47.94526 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README13.md)
