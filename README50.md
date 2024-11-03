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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4128821-217b-3332-9979-ccde17c6f3da | -3.18076 | -50.59117 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0c3edef-3d63-3311-aae1-197afaa45afd | -3.17907 | -50.58035 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9e5a01e-cf7e-390a-987e-469e365ca875 | -3.17853 | -50.58379 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e63b3efe-0c94-3eb7-90f6-f2d02fb45351 | -3.17577 | -50.57984 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2be6566f-0226-3012-be0e-0fcc2e3af7d1 | -3.17523 | -50.58328 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 402c4e10-1dfa-3f48-8cf5-8d3316257be8 | -4.41293 | -50.7809 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d0f146a-97e0-3454-9f59-d5201b2ed9b2 | -4.14647 | -50.74647 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8975c34b-a187-3e98-ba11-8955522081e1 | -4.14594 | -50.74991 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 406389f9-80ee-31a9-8af8-b11d770972f5 | -4.12674 | -50.76455 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db045e63-0b95-3fce-bc57-73d8f2930850 | -4.1262 | -50.76799 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 35aec1a1-b414-36fc-942f-53028df66512 | -4.12398 | -50.7606 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fe2901f-f760-3b00-8538-50696dee84c1 | -4.12344 | -50.76404 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb7c7715-26a4-30e8-95f9-c567ec52e127 | -4.1229 | -50.76749 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcbc831a-c007-3abe-90c5-a79bba84bd1d | -4.0981 | -50.75308 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8f39ba1-6cbb-328d-9cb4-1a523b511ee7 | -4.09757 | -50.75652 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2083fe6f-cfc3-3fc7-a0e5-acceb12c58a4 | -5.13589 | -49.69608 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ae084e7-f030-32e8-a874-38633fcf3c84 | -5.13255 | -49.69556 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f767f3eb-4e01-3231-9e61-bbb4cce35b03 | -5.03977 | -49.96796 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0acd273a-3cb0-3ee2-a11a-052067d8abab | -5.00223 | -49.85867 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24315303-3c34-3624-a466-438f1b5a0aeb | -5.00062 | -49.86915 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf3576ed-881e-3037-a78c-f300c3722ce4 | -4.7107 | -49.60904 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2bb61132-1a34-36de-aa06-06885e36e133 | -4.70552 | -50.58754 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 24dc9ea7-7f2e-3865-83a9-43d32ba582e5 | -4.70032 | -49.76537 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd94a036-b7de-31ef-9c91-d493fde4e362 | -4.67592 | -49.52815 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49251afd-9afa-38d0-bcc3-1355844c5653 | -4.59403 | -49.48632 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09e89409-dad7-346a-b8e1-392e4f6ab13f | -4.41185 | -49.67419 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 758d1d11-d9ad-31f3-91e8-d14c832e9ded | -4.39558 | -49.75746 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d037caf6-28ec-3f36-9601-6d10c5ec89b5 | -4.39504 | -49.76094 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 194a2c72-64d3-3068-b0a3-af308d79fdaf | -4.3945 | -49.76443 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f066f94-c2fa-3eff-a7db-72a8dfdc0f36 | -4.0633 | -49.26759 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9182cd8-aa7f-3d76-901d-c02074d384be | -4.06276 | -49.27113 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc86d776-e411-3eec-b16d-4fad97983452 | -4.06221 | -49.27467 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| add46d0d-3b60-3287-b280-0daa242cb2c2 | -3.99433 | -49.27547 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff56dd4c-2378-34a5-ba25-19989d39df69 | -3.99378 | -49.27899 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6c41f42-b3e2-3543-bf2f-ace6d7bab259 | -3.99323 | -49.28253 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7ab3350-06bb-359c-a4af-b3624ac85d8f | -3.92442 | -49.37321 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91e23ba8-a9fe-308a-aa59-8a5cc30e7ec4 | -3.65981 | -49.91651 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 676db461-919c-3dd1-a17e-f75d68442454 | -3.65927 | -49.91996 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ba814718-cc81-3671-8b78-0a4a7608a676 | -3.55859 | -50.30587 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2180960a-10d3-36d9-824e-921a7d1af578 | -4.36123 | -50.63564 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7542ff95-5f39-34dd-b073-8712e23cc976 | -4.35463 | -50.63462 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5745996d-2e11-3787-aaa9-867c0818cf44 | -4.35409 | -50.63805 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5df8d10-b328-30e6-a3d4-263665bc81ee | -4.22539 | -50.6356 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be20204c-191d-3753-a64f-03af0b27a347 | -4.22485 | -50.63904 | 2024-11-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6850a37-96df-3a4e-aae1-49aaf49343ba | -3.8217 | -50.56176 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49c204e0-e3d6-3b2b-a7e8-161566bcfae1 | -3.82116 | -50.56519 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9784504-ef58-3630-a084-deaaa6e178d9 | -3.81382 | -50.65551 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc5032d4-8f33-321c-960d-27ae3948bdfe | -3.70439 | -50.15601 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4535f763-4904-3f3f-b97c-377620c18b75 | -3.70109 | -50.1555 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 891044ca-60ad-35a5-9a0d-859a65576f48 | -3.70055 | -50.15894 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69afe846-9c7f-3176-9e92-eea437fa81a0 | -3.69832 | -50.15155 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9957cf66-1782-3108-b158-aafaf374693e | -3.69449 | -50.15448 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfbe66e8-fbdc-32d1-bfeb-c0c97f4c7fdb | -3.66904 | -50.1224 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c557361-8c05-3bc4-8c37-e766ea3b9772 | -3.66136 | -50.12826 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f33ea15a-005c-3268-a9e7-1b9a5cbb840c | -3.65165 | -50.169 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 891ab779-ba96-38b5-a238-29fa55f2adf8 | -3.64888 | -50.16505 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfee3c48-8d35-3c37-a22b-536362bd3489 | -3.64835 | -50.16849 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3d3644b-c172-3d17-b59d-0957bb457f67 | -3.6482 | -50.25641 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8579545-2a5d-3c01-9898-3cfe3abc92ac | -3.64781 | -50.17192 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f2fdd34b-0bda-341c-ad51-81cb122e2b90 | -3.64766 | -50.25984 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52e8cc8e-f3e9-3646-bb71-edb158dd660b | -3.64558 | -50.16455 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0d9fc76-f97c-38d0-bbec-3f8070fb1d17 | -3.64505 | -50.16798 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9294d26e-caae-3c55-b999-f7642e025f39 | -3.64489 | -50.2559 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bc086e7-5a1e-3e72-af16-ae050a46d821 | -3.64451 | -50.17142 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cd6e534b-b02b-3c39-932e-cc192b21fa1e | -3.64436 | -50.25933 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d90a6684-b13e-3498-ae2c-b61fd3a0d289 | -3.62843 | -50.18302 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b9b78f3-6a4e-3f8c-adfe-fa0c86133c6d | -3.62513 | -50.18251 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57ed884c-8771-33ad-a10d-3fea7ce73c26 | -3.6246 | -50.18595 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd107241-a040-3d98-8607-aa4683f0b735 | -3.62237 | -50.17857 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dcc5601-9ce9-361d-9f21-13a1f8930559 | -3.62183 | -50.182 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dd8e3b3-c67b-31a9-96d9-d6ac228b1f01 | -3.62129 | -50.18544 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a380ed7-0b18-36b2-b2bc-1dc296051c1b | -3.61423 | -50.40936 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f28f38b5-a141-37d5-a9b1-66731fd09481 | -3.61369 | -50.41279 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db124a31-f59f-3a7b-b603-8d93c5047b34 | -3.59319 | -50.17056 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66078325-4699-3b56-ac4a-903a506b2322 | -3.59301 | -50.25845 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b14add9f-fa82-3c4b-9477-f8dad8e02668 | -3.59248 | -50.26188 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a29d62a2-4094-3709-9a43-b0e0988480df | -3.59194 | -50.26531 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9804b873-f920-32d9-81a4-326912ba75d7 | -3.58918 | -50.26137 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce624ccc-2f25-3ef9-b68c-7ad5f2e1b0d0 | -3.58864 | -50.2648 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04900b12-607c-37f6-bff5-b0bc2d3e1d4a | -5.94068 | -50.84902 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6aedb1c-7a3f-3355-807b-9e9bc728a62d | -5.93738 | -50.84852 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a32bba2-fd29-3f5d-a03d-5ca4e9d5181e | -5.91539 | -50.11125 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d53a6bab-8fcd-3568-8965-0a8bff1d7a38 | -5.64829 | -49.99094 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d3a8299-bb61-326b-bfef-e7f94238aeee | -5.50701 | -49.58279 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac79f21c-3f57-3adf-831e-10d87817e5c1 | -5.50475 | -49.57519 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1bc88c7-c981-39d7-9f20-325de4a4989e | -5.5042 | -49.57875 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99b0e35e-5682-3617-898e-acb1128b5ba5 | -5.50312 | -49.58582 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1ffd481-1040-3fb2-a501-808c3a2cecca | -5.50139 | -49.57467 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 534eba00-c4dd-3a3e-ad78-9c792bc77cd0 | -5.45523 | -50.57897 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e61b883d-7f44-3317-8517-1dc2a5611fb0 | -5.30094 | -49.50794 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 626194ab-4d85-35c9-b0ae-539adfd080f7 | -5.24661 | -50.25618 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a0419da-6898-34a5-83a5-9492a8abdf29 | -5.23871 | -49.93476 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6abb92ad-2bff-3852-af80-f6694be2b42f | -5.13418 | -50.36977 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 843cf8f7-5ce1-32a1-9005-1a7464ef3e6e | -5.12983 | -50.37201 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb84623c-914e-368a-be3f-2d59ceac5e59 | -7.30219 | -50.1348 | 2024-11-03 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 260f5325-f815-39d3-98d0-4939b957422d | -8.73036 | -50.41677 | 2024-11-03 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25ea9ba0-2987-36b7-b659-a08df92dcd72 | -2.26493 | -50.44033 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b0eb8c4-1cdb-3aba-a8bc-32266e2930d5 | -2.26217 | -50.43638 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4037ae92-0b8b-3319-ab3f-43d17a4f3209 | -2.2594 | -50.43244 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f9d6441e-282d-3288-9d00-b2bae18ffc0e | -2.25886 | -50.43587 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README51.md)
