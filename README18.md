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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3548dbb4-ef2e-3841-98a9-c78c245af21d | -11.58703 | -47.44066 | 2026-06-25 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03a18443-6ba6-3ca5-9048-2cd724ded2c1 | -11.32141 | -51.41623 | 2026-06-25 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff3373d4-6e0a-336b-9419-1a7b35e540d8 | -11.35883 | -55.82221 | 2026-06-25 05:10:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49863006-aa33-30e0-bf86-f25362e6cbb9 | -11.87286 | -51.75128 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 62d2558b-8b3b-3680-92fd-db06f2e06b88 | -11.30338 | -51.41097 | 2026-06-25 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3badc9b7-921d-3669-824a-dd6f06fd3944 | -12.54141 | -54.60129 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a32a411-c1bb-3397-976a-0656423a4ee7 | -13.06774 | -53.35791 | 2026-06-25 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbf6caf0-811c-3678-ad5c-965e950a18e3 | -11.87183 | -51.75859 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d9dc4a2e-4d68-33a1-af5a-2ce4a14fb6f1 | -10.38604 | -56.72352 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0085ec80-1907-3fd0-98c3-01f977e9cdd6 | -9.61988 | -54.51002 | 2026-06-25 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26ba4e67-0ac1-3f82-992c-32177d21d997 | -10.61756 | -47.12564 | 2026-06-25 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c70d97d3-83cc-35ad-9cb8-5026db265091 | -11.54037 | -52.7767 | 2026-06-25 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24a6da17-0b12-37b4-b9cf-ecee01fb5dc9 | -11.7945 | -56.99081 | 2026-06-25 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c235fad8-c497-3589-bf88-cb31c9d233c2 | -12.6706 | -54.58331 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c124f71-98c1-311d-ac95-76439f5d8251 | -12.739 | -44.45702 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e72c1082-56e1-3381-826b-6425d5f0586b | -11.89443 | -51.74685 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fd7d36e-f9c3-3f4d-bae0-280bd25e8c87 | -9.49626 | -57.31767 | 2026-06-25 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c86aafa-3215-3036-a973-5e87b1bf3d34 | -10.15973 | -56.62957 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b960c10e-95d9-3644-8bb2-b0af34d3ba52 | -11.91985 | -44.17226 | 2026-06-25 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81b98983-cceb-3a9d-a499-3d4db4a764e5 | -10.52719 | -48.1587 | 2026-06-25 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eb2d6e7a-a1c9-3d02-b28c-4b84f563ad2a | -11.09907 | -49.45488 | 2026-06-25 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c55e79b-a307-3e86-9f28-9cbd3c7a0237 | -12.22164 | -55.49553 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47b215a9-9f19-3404-a0cd-a5aa20cf5c41 | -11.64035 | -52.86115 | 2026-06-25 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 121afa92-0d23-3511-9572-ef07abb025e3 | -10.16303 | -56.6301 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ccc3bb0-9ddb-3e4f-8ce3-29ae4ce56f43 | -11.50626 | -54.49707 | 2026-06-25 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 572d4c29-4d0f-3567-a8a0-56a106ca120e | -11.89032 | -51.74627 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23e13d57-709e-304a-9601-5863af3795fd | -12.22787 | -55.50032 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e002267-ee5b-3688-95cc-296c60fc0d5a | -12.54551 | -57.2032 | 2026-06-25 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0679710e-3f58-393f-af39-e796b62f3988 | -10.58044 | -57.31758 | 2026-06-25 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7e4988d-a045-33b4-ada7-57098ae9b5a7 | -12.22079 | -55.49559 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e9efa5f-4d1a-3584-a586-70ce274bbf5a | -12.31374 | -46.73562 | 2026-06-25 05:10:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a0c2a8b-6084-317e-9bf8-a91ac4fef47c | -13.20422 | -48.32125 | 2026-06-25 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cdfac02-458c-3b63-822f-5ab5dd2b70c2 | -10.16358 | -56.62661 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0483ecb6-da32-3c26-a76f-e1d5f7b83e56 | -11.89496 | -51.74313 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fe1d1ba-f457-3b86-9c90-f600a6d076fc | -12.22136 | -55.49188 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1197bd6-c3fe-3723-974d-da2e4367a2aa | -13.20372 | -48.322 | 2026-06-25 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ee64056-6e7b-3553-b9eb-de99d096eda8 | -11.30789 | -54.70846 | 2026-06-25 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 484ca552-be84-37ea-ad56-e2316b126830 | -11.63653 | -52.8606 | 2026-06-25 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9806bdd5-83ba-35a0-b44f-e4bff597edb7 | -11.87697 | -51.75187 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ea6e1720-d3eb-373c-96f8-d10a7eb2fd71 | -10.36639 | -47.33754 | 2026-06-25 05:10:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 116a209c-c0b1-33c5-b08a-e5e3c0df6f5a | -11.78796 | -57.35326 | 2026-06-25 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a02a5ce-b096-39d7-898b-3464a481af28 | -12.22336 | -55.50719 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5675c98a-188e-3e15-9f5f-13602c75e7b6 | -11.2089 | -54.33247 | 2026-06-25 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f19b2f28-cb7b-3609-a654-bb4a29bb0059 | -11.88211 | -51.7451 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c201c99-3ea0-3cab-9a62-3d5117c774f1 | -13.06841 | -53.35326 | 2026-06-25 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d15a825-7b75-379b-b7fa-0f2f67f27e31 | -10.37093 | -47.34523 | 2026-06-25 05:10:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4207d8ee-9fa3-36ad-8768-1645e1446bc0 | -10.39662 | -56.76458 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c37090aa-cd41-3d7d-a725-8e3dabb79fae | -13.06464 | -53.3527 | 2026-06-25 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a8f0ebe-b705-3b2c-bb3a-5bba5051a9d2 | -10.15642 | -56.62903 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50c8137b-bf81-3bb8-974b-5fb52ae8d62d | -11.88159 | -51.74879 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 2fbef76c-1792-3bd2-b56c-75a28e734c88 | -12.8318 | -44.35769 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5989576c-ba0d-31c7-9e3f-052dfcb211b2 | -11.50452 | -54.50141 | 2026-06-25 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 220ccd31-9327-383e-9362-b7afe425c053 | -12.13904 | -48.26351 | 2026-06-25 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 639de8c1-b83a-3981-995a-f57f666bf61c | -12.689 | -54.58082 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51040530-64b7-3dd4-bec6-05e50f0351f7 | -11.49312 | -52.92247 | 2026-06-25 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 293c33f7-a220-35d9-bc3b-2c12ad5ccf60 | -11.91028 | -43.39815 | 2026-06-25 05:10:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63882007-0b47-3e0d-9f21-f65940693b11 | -10.57713 | -57.31704 | 2026-06-25 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45ae8672-1a4c-34fc-8588-1996d896faee | -10.12614 | -52.10655 | 2026-06-25 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4701abbd-804e-3c44-a4dc-497ca341db69 | -11.31725 | -51.41561 | 2026-06-25 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a240c79-af4b-3c39-85c7-a0f3da9bb2c3 | -11.53749 | -52.77861 | 2026-06-25 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d99c9b8e-ecdc-36f3-9672-93377375222d | -13.07186 | -53.35602 | 2026-06-25 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00c1d507-8212-3de6-854b-c7b1129c441b | -12.74636 | -44.45182 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 29eb8153-f6a8-3a59-a13c-71d43acca858 | -12.21909 | -55.5067 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9152e6c3-2ac8-3728-816d-7b37133c17a9 | -10.77261 | -54.1077 | 2026-06-25 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef47c790-7838-324d-995e-4c3059813184 | -10.15697 | -56.62554 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c83f2e46-5b25-3bb0-8473-6f09c09ee1f6 | -11.88622 | -51.74569 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15ea2855-d070-3908-bf9c-5b7e258478c2 | -12.21797 | -55.49134 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6418f4cc-647c-3f2c-8ee8-b14da1f932d0 | -13.19847 | -48.32108 | 2026-06-25 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a02012d-ff1c-3aaf-bfef-882edccd463e | -11.87645 | -51.75553 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8c132a74-382e-32eb-ad8a-d4f327444975 | -13.83192 | -47.01719 | 2026-06-25 05:10:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 051cf322-0d01-36e6-9286-9ac18e8da594 | -11.24657 | -43.32446 | 2026-06-25 05:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8bdd5d67-4e74-34e1-a4be-bf0f35158018 | -11.20239 | -49.41335 | 2026-06-25 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5721b262-4d49-3831-95b7-3d807a6ce597 | -12.22676 | -55.50773 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59e010b6-4ccf-3ca6-abb6-089d23a9f557 | -10.38659 | -56.72003 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2751abf0-96f0-3bcb-b69e-74789fa529fd | -12.2222 | -55.49182 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2baa2280-bf4c-39af-8444-97f8c3174a99 | -12.21626 | -55.50245 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cae21058-2707-3616-80a7-5db615569126 | -21.07925 | -57.45355 | 2026-06-25 05:12:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac2b7234-60b1-3f62-a8bd-5e1443a12716 | -21.09174 | -57.46366 | 2026-06-25 05:12:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33d39bc8-430d-31ff-bb85-8e4b17c21745 | -18.46157 | -47.25497 | 2026-06-25 05:12:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 615c4d02-eea9-31a1-9f5b-0af4888fe141 | -7.7498 | -44.6184 | 2026-06-25 05:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 98f10b14-0fb2-3c16-b399-8e5ef512e5c8 | -7.7498 | -44.6184 | 2026-06-25 05:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 5263376a-f3f1-313c-a9e4-c207c9717fd5 | -7.7498 | -44.6184 | 2026-06-25 05:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| f6f0db2d-ee78-373b-b9f8-298cb3a09add | -11.8678 | -51.7473 | 2026-06-25 05:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 2c8023b4-8552-3e50-9ae0-230daa6df445 | -7.7498 | -44.6184 | 2026-06-25 05:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 7e7cd761-e7b0-3455-a6d5-dca7d39a1ec2 | -11.8868 | -51.7452 | 2026-06-25 05:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 01743b46-5b79-3f29-ba19-253f0515920f | -11.8678 | -51.7473 | 2026-06-25 05:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 151.0 |
| ba881774-cd0b-33aa-9b72-3d8f3dc1ad6d | -10.16588 | -56.63043 | 2026-06-25 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67e910a9-ed07-3f00-a197-09e4ff1a2441 | -10.27544 | -60.53931 | 2026-06-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76f80bb7-8fad-3d12-9424-d4d77146ced7 | -10.28058 | -60.54009 | 2026-06-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c02504de-eb4c-3800-8d53-44644ff82957 | -10.15767 | -56.63112 | 2026-06-25 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1431c42b-b0b6-381d-98a2-0e7ec40392e6 | -10.16427 | -56.63198 | 2026-06-25 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a072dee-8a6c-3fc7-b0bf-4e63890b8ae1 | -10.15832 | -56.62541 | 2026-06-25 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08f13869-427e-3ec3-8bef-9174f0a6216c | -10.15927 | -56.62962 | 2026-06-25 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e386d0d4-e92e-31ea-a67a-ba027ab21f2a | -11.8868 | -51.7452 | 2026-06-25 06:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 98d4a8f0-ce1e-3e42-b837-1a2af54409d0 | -7.7498 | -44.6184 | 2026-06-25 06:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 0e5a51b9-a0a4-3e24-8a58-9c7897dedef6 | -11.8678 | -51.7473 | 2026-06-25 06:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 0139cdce-edc2-346f-bc65-0206d2c54cfb | -7.7498 | -44.6184 | 2026-06-25 06:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 9f4c1b83-0923-30b3-ae32-8458440dc389 | -7.7498 | -44.6184 | 2026-06-25 06:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| d7939516-303e-3c03-a82f-41d7cf106917 | -7.7498 | -44.6184 | 2026-06-25 06:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f0404788-0d48-3841-9f5c-08148b314704 | -7.7498 | -44.6184 | 2026-06-25 06:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |


[Clique aqui para ver as próximas entradas](README19.md)
