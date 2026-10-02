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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bef2895-59e3-3ecc-a0da-4c5c4b69810f | -3.10388 | -50.29909 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69d617eb-30eb-31bb-8ff5-aab633a98978 | -3.1335 | -53.74056 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 5d54687a-ce75-363d-bbf7-fe62f4115cb3 | -3.13795 | -53.75529 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 140d22dc-1973-3d9a-a155-5ea981fc662e | -3.01456 | -53.2367 | 2026-10-02 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72298548-a0a2-3529-9e9d-ee60da5fd440 | -7.83655 | -55.12724 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 374a72b8-d812-368d-b822-1c27cf988327 | -3.00362 | -53.87436 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66fea074-b6db-3b0b-94c1-3b09ab8efd2b | -4.27118 | -50.75541 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbdf71ba-4a96-38c7-a7aa-4eff54d2e41b | -5.16782 | -56.00286 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efc26bd6-08c1-3a54-9584-3a6cd7d27ef6 | -6.91392 | -43.68372 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23cffa67-e285-3415-8372-f4faf343da6c | -7.46187 | -46.83964 | 2026-10-02 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36d018f0-6119-39e6-86b8-e862e3ff08f4 | -3.58108 | -53.4628 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6de43074-a4d2-3080-b4a7-dc1eb248b4c2 | -4.27165 | -50.77679 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f0015ed-588f-31a6-b7a1-2d9c58c32237 | -6.79048 | -55.54381 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c03be651-8d89-3958-8009-fb4224ad3a4f | -7.60319 | -55.05068 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1672f8bc-59ed-30b5-a207-263c707786ad | -3.11015 | -50.28265 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6501c9d-1875-3716-bf20-a2d4a2ebf79c | -3.2991 | -50.32157 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb02ffdc-77d5-3ff0-ad50-fcd66a8af285 | -3.72696 | -52.39255 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aea1c100-1e67-3873-b7eb-6aa5013f839f | -7.71793 | -54.75337 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca06cc56-fd86-369e-9c68-250d926768fc | -4.06631 | -51.10492 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f38d8e9-da2f-3e36-b199-7f6332e82725 | -5.86651 | -43.59142 | 2026-10-02 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d045a4cd-6d5b-3e1a-bd6b-2f2e91d3c704 | -6.70899 | -44.83624 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6faa4fd5-6aa7-39ca-96e3-1e86a576b29e | -3.27583 | -54.00158 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7096a475-26ed-33da-9fc2-168e4fd3293e | -4.25081 | -50.74379 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6bddf363-b817-39da-8556-b2bc2f0bd40b | -3.93845 | -49.00403 | 2026-10-02 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47881c68-0069-3c3a-88bc-74226bd89982 | -1.45709 | -48.91103 | 2026-10-02 04:57:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e08fd82-a6ae-3bb2-b935-88e5cf36ab67 | -7.691 | -48.4142 | 2026-10-02 04:57:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 745bc5e4-ebbc-327a-9ac6-f338838f55e9 | -6.12768 | -53.29767 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e72917c-89e6-3107-ac5c-80c15445c46a | -5.98295 | -55.37864 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e47628a9-9169-3d0c-92e8-29d30757cc47 | -5.84818 | -53.47694 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23c71e45-577f-3786-b42e-c8799ab7a8a2 | -4.27042 | -50.78496 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7685319-9591-39b7-99b8-d39933fa8e73 | -9.52346 | -45.3325 | 2026-10-02 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6fb32929-dc3c-3f85-b736-89a441398c84 | -3.12174 | -50.28265 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f695d71-c779-3fb9-aa65-ed5c7df40db2 | -6.19703 | -52.80484 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf320539-d4a2-3f06-b476-df3973e7b634 | -2.83652 | -48.4365 | 2026-10-02 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58683e32-5235-3c02-80b8-09f45fa622cc | -6.68761 | -52.97162 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c961b951-522c-3af7-9a92-00302c4a9a4d | -3.1224 | -50.27586 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f506ee4-7e06-3dbd-96b5-70d62c67f346 | -7.84576 | -56.61045 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0a5dcaa8-5d52-3460-a88b-56e61aaeb675 | -7.56353 | -55.02309 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbb03960-fd99-3c0d-8ed4-4a21f0231043 | -5.26819 | -56.0529 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80faffb1-9287-3510-a968-6cb1d8344613 | -7.75159 | -49.20559 | 2026-10-02 04:57:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60171ebd-694f-39ea-9525-c454e1530c70 | -3.04098 | -53.8731 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10ce402a-f926-33f4-addf-a443624c0d4c | -3.28952 | -53.84912 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47ab2ca9-4392-31e3-b974-aa14dd441193 | -1.81431 | -57.10471 | 2026-10-02 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6965234c-d782-33d5-a68b-16efd07f6a8d | -2.93198 | -54.15535 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b692f4b3-f6ca-3ce7-a3c6-92c36ec9d32f | -4.24957 | -50.75208 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b43e0b07-164e-34fb-85a7-108070773803 | -7.56407 | -55.01962 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5cc7a8e-43dd-375e-817a-727a1d84dc39 | -7.5514 | -55.0141 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78daff5d-6b61-3248-9c02-2151bf74725e | -2.89616 | -54.14629 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72799382-c5ba-384d-a15a-d7239b22325d | -6.10819 | -53.09172 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f7a8fc6-c98e-39da-a6da-6415f053e53d | -8.1676 | -54.79269 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b6cb417-f1f6-34d4-a930-14a7db730ac8 | -3.80316 | -51.0257 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b2ac2ef-8b63-33c8-939a-43a167f262b6 | -7.87437 | -44.17183 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b8be6039-03f6-30b0-88b0-7685b95ed82d | -6.40225 | -56.40939 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 171e6c63-b649-361e-a99e-f9b7c766dbb4 | -4.25913 | -50.76208 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74737712-152f-3471-95e1-591adc989a75 | -6.18595 | -52.89898 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a622b45a-54a5-3bf9-89ab-357056fa731b | -8.26373 | -54.74466 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ade04283-e4bb-3690-a9e5-3d74bcce94e0 | -7.34336 | -55.5773 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2e6c67d-20aa-3e3b-bc84-2dc0459229fe | -4.2884 | -50.78778 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 724d5d45-f169-3aa1-aae0-0d63074e755a | -6.87047 | -57.71948 | 2026-10-02 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50276dc8-fbaf-3745-91f8-f301f91da2df | -2.57693 | -49.99849 | 2026-10-02 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 204ff947-b902-3a0a-8a4a-57299b02d13b | -7.04572 | -55.63105 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 782f34fc-e06e-3229-be4c-2d1d188b79ef | -3.41781 | -48.33551 | 2026-10-02 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1974fcad-6d4c-3263-a3ed-93e8eae2d1cb | -6.15175 | -47.46874 | 2026-10-02 04:57:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0f30c761-2744-3480-8bce-894f646c1a4f | -7.56865 | -55.11987 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3ff4b3c-d2a1-3667-b5f9-3522edc1b5b4 | -6.84936 | -55.53864 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9752404d-0e61-3b46-bccd-c3cda425e9c2 | -6.21535 | -53.25739 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e23e2d25-055b-3f5c-ae6a-bb17b3df8479 | -7.86716 | -44.17579 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b250143-719e-3c35-9f38-a1796582c46c | -7.46384 | -54.98549 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a25767a6-485c-38de-ac07-d597382e9840 | -5.27263 | -56.04963 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fabf8a1f-5a38-3177-9671-7d4c62bec9c8 | -5.12204 | -56.02277 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfa939e9-073b-3654-ae49-9d7162b7173d | -6.00769 | -45.78015 | 2026-10-02 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c28a8e4d-8fae-3f72-a6bb-fd490309ea10 | -3.27199 | -54.0045 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24d97e69-6444-3d76-8879-71459ef90a10 | -3.16555 | -54.07585 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9e399955-cb13-371d-807e-52670e2f3b56 | -6.8896 | -52.49934 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e693ce49-79b0-3786-a5a7-be7c08d6909c | -3.1717 | -54.10144 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 878f6974-570b-3d9a-a32f-3009179a801a | -7.74061 | -54.80297 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3821b28-45ae-3be0-ac26-b4df87476fa6 | -7.52772 | -50.52884 | 2026-10-02 04:57:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb58e313-248e-3e4c-bbf6-4a23c3b44644 | -6.12633 | -53.19611 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb5358c5-2629-3d22-982c-4e89c6bce9e9 | -1.26279 | -54.55589 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7c982fe1-967f-37e1-8774-45d64ef4e759 | -4.28668 | -50.77483 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9410ee67-451a-3c5c-adfe-7269517859d5 | -3.16394 | -54.08616 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23ff9cff-4973-33de-9876-58e1baf6db45 | -5.97628 | -55.37759 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42cf594d-faa7-3160-8984-3473dfc5a450 | -4.06506 | -51.11302 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7197748e-37f2-377c-bb70-e0ff5fb08d6f | -6.44916 | -55.0123 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b2542c3-bd5d-3cb9-aeed-ae8592c1b2c5 | -3.12913 | -53.74691 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d3a4f0d0-6968-3994-bd5c-1e348f9296f6 | -8.17972 | -54.80169 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a57be859-c8fe-36bd-a14e-1aff4a1bc6a5 | -4.07672 | -50.33151 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 635ee3ab-c30f-32ce-b268-4da96e34f0bc | -3.42275 | -54.5413 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59439141-dd13-34c3-a2dc-c63041596d82 | -2.54725 | -57.40429 | 2026-10-02 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ee6ea65a-ea84-30dc-b62e-4865f541bc7d | -6.50273 | -55.89569 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea7cb65f-d31e-3ddf-92a2-4e8566809326 | -3.28399 | -53.84125 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| aea72c9f-0eaf-3917-8cb4-10c0ff3248a5 | -3.28783 | -53.83833 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 349727f6-2d4e-36ca-a517-d2fb51ad4784 | -1.63033 | -55.14 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4adf533c-a39c-3d21-8aa8-081de905e566 | -6.23897 | -53.14868 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9c3f2647-98c8-3d86-b243-d67ba363167d | -7.82003 | -55.12463 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7b514bf-31fe-3ec9-a7cd-8957e780a4f9 | -3.14508 | -53.75288 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 489d9005-f8e3-3d13-8847-d8bc2a27c20f | -4.29823 | -54.79662 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5a6684b-b62e-3c5b-b67d-5a368bcdf913 | -2.89501 | -54.132 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f97a869-1cb2-3fe3-90e0-6708f1c66619 | -1.49923 | -55.83258 | 2026-10-02 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de408c10-6207-3c92-8114-8dab7ce444ce | -6.23161 | -56.04586 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README55.md)
