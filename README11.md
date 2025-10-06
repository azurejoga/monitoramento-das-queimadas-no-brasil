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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 835bba2d-f72e-3f6b-ba74-3b0f90ed8555 | -7.25298 | -44.1349 | 2025-10-06 03:34:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82239203-e3b5-3743-bd91-e06c569e3e67 | -7.01254 | -42.80916 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79bf3b9e-dcf6-39f8-884f-a03c197d4690 | -6.75789 | -42.23781 | 2025-10-06 03:34:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a148a472-78d7-3375-8d54-a3f7e32c839f | -6.75725 | -42.24141 | 2025-10-06 03:34:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bd0fc357-2a81-332b-85d2-358154aceaaa | -6.64618 | -41.97429 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7053f3a3-4a6a-3e93-9579-f6b73c621441 | -6.31383 | -44.69224 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0f666d76-3d50-3fce-bafa-5e0efd8182a4 | -7.00723 | -42.8081 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cf39c62a-c000-3704-a6e8-273e16b1785f | -6.25016 | -43.89647 | 2025-10-06 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f025d889-b17b-36d4-ba0d-200e76a20ba1 | -6.64008 | -41.97932 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 10c462b6-bc17-3c1b-a43b-ad30bcff49ce | -7.0321 | -42.76081 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 43930552-0242-32a1-b5d1-4bbc1af2e8a9 | -5.2804 | -45.17913 | 2025-10-06 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dddd500-85a5-3748-a946-c63b01f0b9f5 | -5.40937 | -41.07235 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b7f7a0e5-279c-3664-a45c-1d1bd7c6502b | -5.96123 | -43.53463 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 743cabb6-3b60-349e-8780-29729dd119b9 | -7.01017 | -42.79159 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 27c197ea-6d2b-356b-affa-47eb49d6fcb3 | -6.62486 | -41.97662 | 2025-10-06 03:34:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bcead765-c692-3ad9-8d74-f449eb53f0d7 | -4.76492 | -46.6106 | 2025-10-06 03:34:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 987ce63f-c538-38c3-9fac-ed5e6903083f | -7.72913 | -42.39339 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7735360c-8b04-349d-8b8f-0c3ed2c70b1e | -7.02203 | -42.78672 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 75df84dc-e1d5-3508-9d4f-92ed826bddc6 | -6.42749 | -44.61939 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5416889b-d8f1-3e19-8856-e34b01a4e17a | -6.78416 | -38.76103 | 2025-10-06 03:34:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a299f6c4-a2b3-31d5-aedb-b90ab7a76368 | -5.96397 | -43.5308 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a1f9909a-61d9-3535-a0f9-b99dc1968041 | -6.61924 | -41.97882 | 2025-10-06 03:34:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 79878294-27da-3bcd-bcd7-3010d7aa5576 | -5.96762 | -43.53157 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3f846b5-1013-3046-8fe0-ef290fcb7791 | -7.8029 | -42.58429 | 2025-10-06 03:34:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e31b6c1a-777f-3845-86c2-b809095d9d7b | -7.35599 | -45.24406 | 2025-10-06 03:34:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fdad20e-b29d-394d-a359-68a8598d7589 | -7.02142 | -42.79011 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4ec589df-d65f-3eeb-9677-869809e401a7 | -6.95498 | -42.06204 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4bcc50d0-167e-3c7f-a2c2-1833abd75108 | -6.428 | -44.62345 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 143a5aea-4462-3b06-ae39-ef79d973ad36 | -6.40318 | -43.61324 | 2025-10-06 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 825af89e-19a5-383b-af95-61589136dc39 | -6.10667 | -43.53093 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ac5faca5-d659-3a72-bf0e-ceac06cf327e | -7.55172 | -44.93243 | 2025-10-06 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9286dee5-dfa6-3e52-8c33-9ff14e9a66b8 | -6.65791 | -40.91167 | 2025-10-06 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 069dbd5e-7d9c-3d43-b550-5f9aa9b2000c | -7.46102 | -43.03825 | 2025-10-06 03:34:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 20942ba8-3d70-350a-995b-b8e410910b91 | -7.02117 | -42.30089 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fbe42222-8834-3781-a461-e90c4f15113c | -7.2105 | -45.89054 | 2025-10-06 03:34:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f006ba83-8ae6-3a2a-93fe-afd0b91349e5 | -4.44716 | -44.19596 | 2025-10-06 03:34:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2b6cb815-6c89-3241-a3c9-ac84123b4c5f | -3.79402 | -44.47103 | 2025-10-06 03:34:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 874f65e7-9d98-3efe-a300-78a47f7679f6 | -5.41769 | -41.34445 | 2025-10-06 03:34:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 514b7eba-f264-351f-9467-82266222b580 | -7.17927 | -41.69283 | 2025-10-06 03:34:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bdfa23ba-e933-31f0-a1a2-20fca113d742 | -7.78853 | -42.60468 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be78676a-a5fa-3183-8413-096e36728d65 | -5.3339 | -43.3782 | 2025-10-06 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b012767-68ac-3727-ab2e-affe27275a4a | -7.0149 | -42.79593 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| aa548afc-8908-3c68-a4cc-7dfb1a6830e5 | -6.3086 | -44.6882 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 952a9414-6cc1-3ab3-8ea9-66ffd16ad24e | -6.64566 | -41.97728 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f469b30-073f-3ca6-94f4-b3371166a669 | -4.74382 | -44.44558 | 2025-10-06 03:34:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a362af47-81df-3c6d-97c3-4fbac6355935 | -7.78968 | -42.59832 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 63fe1a06-4ab1-3506-b248-81bb6e038cf8 | -6.0664 | -42.54566 | 2025-10-06 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9e24111d-4f57-3238-a5f6-cb7f16b34505 | -6.31468 | -44.68929 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70512c5b-159f-3bf3-b682-49560eaf959a | -7.72509 | -42.3864 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 53bb8cea-8de1-3069-bab5-d1fe4d9b58ed | -7.00319 | -47.48346 | 2025-10-06 03:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f21576ab-84f3-3cfe-ac13-f5dcc96e6b3a | -6.07527 | -44.0431 | 2025-10-06 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5acab0ef-6b9e-3398-8410-7cd333747ef1 | -6.63397 | -41.98438 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 116f574e-9d4c-3154-b7dd-313003ef7fa4 | -7.71323 | -42.39357 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6a1687da-d6ce-3d6e-8dce-10c5646f1daf | -6.66173 | -40.9176 | 2025-10-06 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 258b0ca8-3833-321b-af25-65a4df9b78de | -7.71378 | -42.39053 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d79c9efd-3dea-394d-85c2-1bdd3ae36528 | -6.23027 | -44.39518 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fab17570-70c2-34b3-94ab-880d88b17c62 | -7.51826 | -41.2795 | 2025-10-06 03:34:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cefc1c9b-8451-3b84-a34b-421ca3836550 | -6.61977 | -41.97581 | 2025-10-06 03:34:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d49e0b63-d130-32f9-bea2-1f59684ff84b | -5.89666 | -38.47709 | 2025-10-06 03:34:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2c8b6f1c-06b6-3441-923d-779e7c3f720a | -7.78223 | -42.60986 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c8fc422a-1441-32b9-b117-c5c9066ee298 | -7.72859 | -42.39641 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3dd698fe-dc82-3406-a5ae-5494b9528a8d | -4.7662 | -46.60368 | 2025-10-06 03:34:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8c5ec3b4-d1dd-3ee4-a0dd-7f32543dbec6 | -7.24624 | -44.13827 | 2025-10-06 03:34:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b796d832-0932-3998-878b-f5ad0ff0021a | -6.09462 | -43.50024 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f9f3508c-876e-3805-b434-922ae7afd39b | -4.89289 | -45.74021 | 2025-10-06 03:34:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a48ed7d-05f4-34bf-becc-1ff5127a0288 | -7.35676 | -45.23267 | 2025-10-06 03:34:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8698a66e-a36d-3690-bd5b-bda06af22788 | -6.25048 | -44.26698 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 30bfd74f-09e1-3f80-b875-ef335d9af1f7 | -7.7105 | -42.55735 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a6b217db-583d-37ec-a423-e14d8864069a | -5.96194 | -43.53055 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30780611-cb26-30b7-a6c6-61aec5d241db | -5.46012 | -42.80058 | 2025-10-06 03:34:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6658fbe0-f4d3-3545-bace-292628f28e7a | -7.43123 | -41.12866 | 2025-10-06 03:34:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7f9cb678-7d2d-3d9d-a5d3-e4f70c533905 | -6.39462 | -43.62812 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7292efae-12e7-30f4-a73b-a54fc1253ac8 | -7.68299 | -42.5913 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6860280d-b9ad-375f-a957-9999ccca644e | -7.7828 | -42.60672 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 04424076-791f-3c44-a39b-cf27e2805147 | -7.36115 | -45.24325 | 2025-10-06 03:34:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41a50273-58bf-3f04-916d-314a4202a2dc | -7.46597 | -42.62666 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4ead88e7-3501-3665-8444-e81d779faf54 | -4.89941 | -45.742 | 2025-10-06 03:34:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6029e6d9-e460-3651-b321-09649e7ccd92 | -6.23177 | -44.38708 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cbfb548-a777-3509-ba6c-605e6a1fdbf7 | -7.47698 | -42.62543 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f8e52d5-11bc-327c-82c9-af6cb10f83c8 | -6.63853 | -41.98827 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0d04cf8-57fd-350b-a024-3dc74f12c030 | -7.71726 | -42.40061 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ee9347d2-7e9b-34b6-a34e-d39929accdfb | -6.04684 | -42.56306 | 2025-10-06 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b2af857a-3331-3d52-9d5b-c35a8b7e9a2e | -7.02082 | -42.79352 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dbb8012b-86b3-39f3-ae45-a33cf7c539f9 | -6.25166 | -43.8882 | 2025-10-06 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3f0601e9-ef81-39da-b82f-43b7abcfc65a | -6.05868 | -42.55827 | 2025-10-06 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cc1d7b5e-6890-3c4d-890c-3ab75f17ec2c | -6.69605 | -42.15734 | 2025-10-06 03:34:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af516db8-9f1b-39cb-99fe-62af15fe0427 | -7.35775 | -45.23447 | 2025-10-06 03:34:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0bd2d6ac-0e26-3f56-b211-6ff416548c7d | -5.48163 | -43.26835 | 2025-10-06 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db5e94f5-6851-373d-a40f-5f69243b2c73 | -7.80347 | -42.58113 | 2025-10-06 03:34:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 48cb3e3f-e41c-306b-bef4-f1930a8a2e0e | -7.73371 | -42.39737 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 36773c3f-bc06-3d07-a196-1e5ee6ceaeef | -7.0258 | -42.30482 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 22080e72-6090-35cb-baaf-3d06fd726e08 | -7.00954 | -42.82603 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b62bd55b-ca38-3885-ae78-bde2d12c75bd | -6.27066 | -40.62179 | 2025-10-06 03:34:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dd0d0a48-f2d9-3b5a-908b-e1d615f9a60f | -7.78394 | -42.60041 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bcdb2d19-a68e-3ce9-8102-93ea88a0542a | -7.00302 | -42.83172 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3288292c-8baf-3a99-8b14-cb64cfde563a | -6.63956 | -41.9823 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3a430141-ea11-336e-ab01-68797a199ac8 | -6.03799 | -42.55103 | 2025-10-06 03:34:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 84711fcc-ab79-3c95-a3e2-492946818531 | -4.7668 | -46.60921 | 2025-10-06 03:34:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| aff5e2cd-68e8-393a-b574-f8e5bc283209 | -6.04331 | -42.552 | 2025-10-06 03:34:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d1b17772-0ed8-3bfa-ad1d-b1d57d178adb | -6.42894 | -44.61834 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README12.md)
