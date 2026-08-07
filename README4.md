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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a4da690-eee4-3dc1-87f1-94f4341eb2dc | -5.424 | -43.432899 | 2026-08-07 00:32:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a539e3e-920a-3d84-8308-293cae4d3e58 | -3.1247 | -48.586102 | 2026-08-07 00:32:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 780a6205-a5ff-3966-be2b-f6761c298f71 | -4.8495 | -45.2192 | 2026-08-07 00:32:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3172411f-636d-3222-b1f4-c2f55e8b6774 | -4.2705 | -48.185799 | 2026-08-07 00:32:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4c5abb3-e56e-3fc1-ad00-16dd0eaa8b01 | -9.625 | -40.581902 | 2026-08-07 00:32:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 22ad9cf9-b3c5-3a8e-b94d-cb5b67766ffe | -4.4557 | -47.9119 | 2026-08-07 00:32:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb537bf3-9e3b-34f7-9096-2bcd61ccba9c | -6.8647 | -45.996498 | 2026-08-07 00:32:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9cf9b36-ef94-3106-a695-5c2ded541654 | -11.1513 | -44.491299 | 2026-08-07 00:32:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ffc4597-99a3-3636-bbc9-bd05fc87395b | -11.4582 | -44.569401 | 2026-08-07 00:32:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e85b58be-bc27-396b-a44c-874a3796d184 | -6.9189 | -41.945301 | 2026-08-07 00:32:00 | METOP-C | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 178ee4cf-d358-3639-a640-4dbb13debd5d | -18.1446 | -47.978199 | 2026-08-07 00:32:00 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d964c0f1-6df6-3368-8cb8-9d701afa57b5 | -15.8701 | -43.602798 | 2026-08-07 00:32:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf6c1b4d-15af-3b2e-874b-687e05f03c74 | -15.9269 | -43.9893 | 2026-08-07 00:32:00 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c85edbf7-8912-3ef4-b21a-85b9023afafb | -5.9769 | -52.149502 | 2026-08-07 00:32:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc1b320d-2f0b-3671-8f4e-7dd90e0faa57 | -12.6278 | -46.889702 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5c2c806-4940-39a8-9313-24bfa0e86656 | -13.811 | -53.7089 | 2026-08-07 00:32:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc022858-32b1-3c14-a7fe-c04e471a7be6 | -2.6899 | -47.357101 | 2026-08-07 00:32:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 200392d8-ede2-337a-96be-4c9dfabdcb7b | -11.4566 | -44.562401 | 2026-08-07 00:32:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b563d21d-1324-3c5c-8a8f-d96fb259bc23 | -6.8679 | -46.010399 | 2026-08-07 00:32:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5971f6e-e695-3e9c-b3ce-7163a0dedd6e | -16.6896 | -51.3615 | 2026-08-07 00:32:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e4a52130-f5b3-330a-aec5-55ecc42e970c | -20.6189 | -43.965698 | 2026-08-07 00:32:00 | METOP-C | SÃO BRÁS DO SUAÇUÍ | MINAS GERAIS | Brasil | 3160900 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd72bfe8-68e5-3abd-83a3-2110a5441b6f | -11.455 | -44.555302 | 2026-08-07 00:32:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e247135e-f666-3cac-8a43-46bdc82677f6 | -12.5509 | -46.9608 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7cad1e0-23e6-34a4-aa46-f26e229ac541 | -4.3722 | -47.771301 | 2026-08-07 00:32:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f326ee6-6295-3aee-b299-505934909266 | -12.5805 | -46.908001 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9d9d9f6-a722-30d8-b3c2-cbfa71515422 | -6.2751 | -44.559101 | 2026-08-07 00:32:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c33ed8b-d0a5-39c1-b29e-a10f317858a9 | -4.4588 | -47.925701 | 2026-08-07 00:32:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06cd03af-a260-355f-b303-fe6d1568524f | -18.1465 | -47.987598 | 2026-08-07 00:32:00 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 75b7a78e-ef6d-33c2-8adb-d8a09367be86 | -11.4648 | -44.553001 | 2026-08-07 00:32:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8888e6ba-6a39-3452-9b31-f1bd91e91273 | -14.4848 | -47.983501 | 2026-08-07 00:32:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 24e89921-01b1-3637-8555-0a4a544d7bfc | -16.679899 | -51.3634 | 2026-08-07 00:32:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1fe65bfd-79bf-3472-b795-e07df88038fe | -15.5914 | -43.737801 | 2026-08-07 00:32:00 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 0232e9be-83f2-3150-91a3-aae6c0d0cea0 | -4.3737 | -47.778198 | 2026-08-07 00:32:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 622e136b-f627-3c70-b4a2-942650a84bc0 | -15.1001 | -53.5984 | 2026-08-07 00:32:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ac03fae-2cec-31ec-8de3-b9e263141168 | -10.6327 | -47.495201 | 2026-08-07 00:32:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf382cf3-a766-3386-b2bb-ec4c2d609baf | -12.5672 | -46.9417 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d04953e-bc8d-339f-876d-7a6ca977a002 | -4.4572 | -47.9188 | 2026-08-07 00:32:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f98a828c-024d-35aa-a1da-ed3763015bee | -4.3706 | -47.7644 | 2026-08-07 00:32:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8b768eb-027e-3ce0-a92d-1c3a5a2f002f | -6.8663 | -46.003399 | 2026-08-07 00:32:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d34590a-d713-3807-8df8-eab8f0cd7702 | -4.2639 | -48.2019 | 2026-08-07 00:32:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 347ba18d-62e2-3b44-ba05-542455f04569 | -15.0966 | -53.5793 | 2026-08-07 00:32:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e37ab577-2059-3c54-8c9c-9a9ef50bf649 | -12.5788 | -46.9007 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c958cfa-5ea3-3dbf-acba-e137f54fbaf9 | -2.4803 | -49.332901 | 2026-08-07 00:32:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b76ddab-df77-30ad-a448-d243cd6ed786 | -6.4801 | -42.225498 | 2026-08-07 00:32:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 22548ebf-4165-3fe2-93b6-e03b7780da00 | -6.9171 | -42.414501 | 2026-08-07 00:32:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7c03915a-3b7a-32c0-b9fb-af4027c15caf | -14.4246 | -45.658501 | 2026-08-07 00:32:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3e20aa7-9dfc-35de-82d6-daa93fe4accf | -6.8581 | -46.0126 | 2026-08-07 00:32:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46892bf5-6300-3625-9f68-8fcf4066c8c9 | -4.2721 | -48.192799 | 2026-08-07 00:32:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 827ff1cd-acfa-3fa5-ac54-d138f23a12c7 | -6.86276 | -46.02544 | 2026-08-07 00:33:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 13e18a2a-b93b-3641-941c-4c6b63a2de86 | -13.4213 | -57.02476 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 30df734c-5f03-3798-a6b8-f25e3263a5e7 | -14.53997 | -52.11238 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b52ab42a-ead3-367f-9398-765bc77655a4 | -15.58542 | -54.2961 | 2026-08-07 00:33:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4af2e8b4-4f3d-3062-bc06-ca9be21c46b3 | -7.09467 | -46.53536 | 2026-08-07 00:33:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 06fddcd0-800c-3da8-97f3-3e9ef8bbfed7 | -15.11579 | -53.58204 | 2026-08-07 00:33:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 38a5b732-cc04-32b0-b58a-b2f174f4e380 | -13.82667 | -53.72238 | 2026-08-07 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 7c4113d2-d13d-3346-85b1-b89717cfcf5a | -10.63071 | -47.4869 | 2026-08-07 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 34b433d0-bba4-367b-a9c1-85d7a1a81beb | -11.08408 | -47.80682 | 2026-08-07 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 19055e42-59bc-3220-9944-d041b5039dc6 | -11.18405 | -54.85465 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 072bc13c-3535-3ef8-84c3-22b0284c06a6 | -15.11713 | -53.59142 | 2026-08-07 00:33:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 8156f6e2-76a4-3f97-b0d0-5f831d4bd782 | -10.63153 | -47.4813 | 2026-08-07 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| eedb81c4-994c-391f-9c85-62454a66f2ca | -13.78492 | -49.72242 | 2026-08-07 00:33:00 | TERRA_M-M | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 93d48539-0769-3fd7-a358-40240dfeb254 | -11.12615 | -54.90635 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| de5de39c-ea47-3ded-ac79-fb79030e1edd | -15.05829 | -53.56819 | 2026-08-07 00:33:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e0191d17-27b8-34ea-afce-e5a6eac04ab6 | -11.17392 | -54.8469 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 6c843e1a-115d-305f-a57a-d96768a5241d | -11.13722 | -54.90766 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e64bbb20-93cb-3f9d-9f2a-e63055dfea83 | -11.92209 | -55.92234 | 2026-08-07 00:33:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c36515cf-6a66-3536-8793-a279cea7ac6b | -12.01047 | -49.27851 | 2026-08-07 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 854f9895-1749-38e8-82be-f496600e1b70 | -13.43186 | -57.0334 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ed0f7aaf-72ba-328c-ad41-0041676003df | -13.62957 | -54.67814 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e37a4c8d-59e2-3c24-a577-4d3924a4775a | -9.09514 | -59.47903 | 2026-08-07 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 284635c1-93d7-344a-980a-f1600ba9b1b4 | -14.35235 | -54.91537 | 2026-08-07 00:33:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 402d1052-3325-3431-a19b-315c5013dd48 | -11.92087 | -55.91332 | 2026-08-07 00:33:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 8fee7181-3c73-3800-bcb3-8063bd7c976d | -12.3268 | -53.16795 | 2026-08-07 00:33:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3b7f56b3-c2c8-3d97-a928-b9c9fc6866f4 | -15.10818 | -53.5928 | 2026-08-07 00:33:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| f03c891c-dbe7-39f4-88ba-68d910b65848 | -11.18278 | -54.8456 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 11142843-bbb2-34f5-ad2c-f25e340612ed | -7.09006 | -46.54293 | 2026-08-07 00:33:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| da57acd4-0913-39a6-99ca-4080bf8ec20c | -10.92981 | -57.1768 | 2026-08-07 00:33:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| eb2b1161-32b8-3fd6-be7d-5e48330e7d33 | -13.68904 | -51.97647 | 2026-08-07 00:33:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 53e0df5c-48b0-35f0-b90f-02076ac8ae4e | -13.81689 | -53.72016 | 2026-08-07 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| db367f3b-4fd8-3be0-b252-13a1fcf59fae | -13.81556 | -53.71072 | 2026-08-07 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 168c778a-8365-3573-8e36-681e8a6f04f0 | -9.18028 | -58.07603 | 2026-08-07 00:33:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 15175414-e50d-372f-aab6-61e8f22c2cf7 | -13.82531 | -53.71296 | 2026-08-07 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 04cf817c-573b-3b76-b93b-c2e5fc6ba01f | -13.8343 | -53.71157 | 2026-08-07 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 9f1ccfc9-6710-35f0-839f-b8bdfe37e6fe | -13.4226 | -57.03468 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8577b1bf-8df5-3312-b440-624391fb078b | -10.93891 | -57.17546 | 2026-08-07 00:33:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fabc9e1d-5142-3e05-b8de-a8dc7cc8139b | -9.09666 | -59.49098 | 2026-08-07 00:33:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 42b1219b-451a-3b89-b798-d107c3c8d5f0 | -7.10066 | -46.57143 | 2026-08-07 00:33:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 99f1467d-bec6-3289-9e66-8000c7049f3a | -11.17519 | -54.85597 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 703be46c-8a87-3705-9b97-986232d415c3 | -15.58415 | -54.28698 | 2026-08-07 00:33:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 49dcaa15-1766-3da9-bb3d-b03d003cc06c | -11.08026 | -47.81334 | 2026-08-07 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 3b348191-8bc9-3fe6-87e1-14f31cad8e0e | -15.07487 | -53.55598 | 2026-08-07 00:33:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 91121d8f-3cd9-3def-92ed-1b9e8013849b | -13.62831 | -54.66911 | 2026-08-07 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 087f7be2-865f-3612-af90-5e226169ec8b | -14.44483 | -53.34109 | 2026-08-07 00:33:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 21bccc44-32b8-358c-b27c-130e3fcbf17c | -12.33611 | -53.16651 | 2026-08-07 00:33:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 305f94de-c088-3478-89bb-4407ef0ccc73 | -14.48196 | -47.98668 | 2026-08-07 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4b197b9c-6cbd-3be7-90e5-a8bcd6a719c2 | -10.6106 | -52.22503 | 2026-08-07 00:33:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 23760be8-022c-37ec-a3b4-4e3ae5b6df75 | -11.17645 | -54.86502 | 2026-08-07 00:33:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 734ff50d-4475-3846-8944-6db5557524f0 | -6.54245 | -56.54508 | 2026-08-07 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| d97cb408-aa42-3e7d-8d69-211abdded1eb | -6.95772 | -52.81033 | 2026-08-07 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b20d4c30-2ae7-3461-a84a-18034d63de60 | -4.26867 | -48.17689 | 2026-08-07 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |


[Clique aqui para ver as próximas entradas](README5.md)
