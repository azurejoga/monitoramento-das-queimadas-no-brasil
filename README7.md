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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74e68785-295a-36b6-9d5d-2d860c1d8703 | -3.3638 | -50.4492 | 2026-09-18 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 2f386023-1139-3ede-8f7b-06cdad3a623d | -4.5961 | -42.95 | 2026-09-18 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 258.4 |
| e59b1df0-0de9-3ff3-bbe9-4cde5790a1c8 | -19.1806 | -48.7946 | 2026-09-18 00:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 72.1 |
| ae53f238-489f-3158-aff2-7ef86690f80a | -17.8054 | -53.1249 | 2026-09-18 00:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 7646b5eb-2b7b-3a01-94bd-62bc766a13e9 | -9.699 | -54.8176 | 2026-09-18 00:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 0e84be09-d082-3540-9723-7d379f4228b0 | -4.5774 | -42.9512 | 2026-09-18 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 906.6 |
| 4834806d-6ada-39f9-926b-6b83683185ad | -4.5772 | -42.9746 | 2026-09-18 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 330.7 |
| e744f910-fa6b-3d1a-bb2d-43274c453b10 | -4.5585 | -42.9758 | 2026-09-18 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.2 |
| ecc23537-8cc2-3c20-8c47-a7dcd64a9673 | -12.263 | -50.7677 | 2026-09-18 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 189.0 |
| ca795733-8db2-3337-8094-a8582d32500a | -4.5776 | -42.9277 | 2026-09-18 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| ef56ba28-5bb7-3053-897b-cd3fbf68ef08 | -2.8101 | -50.4658 | 2026-09-18 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| b68218f3-4f46-3520-9122-64f308137023 | -12.2439 | -50.7699 | 2026-09-18 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a4e84b0e-b877-3d35-aaa3-5dacf083422c | -12.6427 | -50.893 | 2026-09-18 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 5acca9f4-c83b-3a90-88f4-766e766432c1 | -2.8285 | -50.4653 | 2026-09-18 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 8e72fd99-e520-3d9a-abcc-67680259a21b | -12.643 | -50.8716 | 2026-09-18 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 145.8 |
| a4d0ff80-2025-33df-9e39-3cd060c9883a | -12.2821 | -50.7654 | 2026-09-18 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| fd82be3e-e5c1-335b-bc25-9e9affdda17c | -9.7179 | -54.796 | 2026-09-18 00:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d8ac5c87-0f38-36ee-b6f4-f70c7bcfaf88 | -4.5587 | -42.9523 | 2026-09-18 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 401.1 |
| b5e3ccc2-ef70-3f51-9e92-d0e19f4be991 | -12.2633 | -50.7463 | 2026-09-18 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 21271e6c-331d-300d-8fc8-d11ea8c9a953 | -6.1174 | -59.9644 | 2026-09-18 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| a1aae943-d7a5-3c11-ad37-59caa41dcff6 | -6.1358 | -59.9638 | 2026-09-18 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 0dc52b0d-3371-3c52-8b07-4672af29caf5 | -2.8284 | -50.4863 | 2026-09-18 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 473f340b-fa3a-3ef5-bf97-93c02c51383a | -4.5177 | -56.0751 | 2026-09-18 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 2a8ea1b3-09cc-3569-857b-df647335ed7e | -19.1749 | -48.774399 | 2026-09-18 00:39:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c9e42119-35bf-3d3d-b6cc-8ebd4c27a029 | -9.9388 | -45.3508 | 2026-09-18 00:39:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 072b4edb-c82d-3368-a5aa-b9e7c307a1d1 | -12.1671 | -46.978001 | 2026-09-18 00:39:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 348f492f-e10f-353d-8dca-9d14ae783e63 | -6.4477 | -58.159199 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4898a53c-bf89-3088-a07e-5939524602c4 | -4.4917 | -55.487999 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7278fa93-0cc1-3078-b2ed-fd0542cf664e | -12.3792 | -50.688 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b705dbb-2c0c-3cf3-a777-aa30a891ac00 | 4.1152 | -60.664001 | 2026-09-18 00:39:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0500b055-dee9-396d-a66d-9f82f02db730 | -21.456301 | -48.681198 | 2026-09-18 00:39:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 442985e2-3cb5-3a63-84c5-6c61a558eac5 | -3.9604 | -56.139301 | 2026-09-18 00:39:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a39f0112-42ed-36a9-adc4-010b729d9869 | -12.2855 | -50.769798 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad03de5c-8e35-334a-9c07-3a7b057b0a68 | -15.6602 | -52.736599 | 2026-09-18 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 527ae5ed-ad2b-3b93-9ed3-f88fe4bc9a0e | -12.4668 | -50.665798 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f53fc825-73e1-3702-8726-7867056b6eee | -4.4474 | -55.474098 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e54a7c6-4369-3fd3-8d2e-83f1c3c64492 | -15.8061 | -52.564899 | 2026-09-18 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 780cd281-4eb7-3eb8-8462-b559c81dd60f | -4.7791 | -55.7071 | 2026-09-18 00:39:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afe662de-a46a-3e3a-801b-c7a6ab1f9805 | -10.9986 | -57.054401 | 2026-09-18 00:39:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b72fe0f1-3de3-3e7d-b50b-56661b3c3cf9 | -10.6046 | -46.558899 | 2026-09-18 00:39:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 673180b7-c4c5-3548-962e-2f87dec030f8 | -11.0582 | -48.2864 | 2026-09-18 00:39:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a13ef1b6-2c93-33ce-b77e-31bea79ff056 | -4.4287 | -55.078899 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cfe5193-c16e-3fbf-a17b-9c450ab82057 | -13.3832 | -57.048 | 2026-09-18 00:39:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e073967-0137-30ac-a9f5-ba5bc86e90b9 | -14.7682 | -47.160999 | 2026-09-18 00:39:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c8880a6-3bb1-3418-ba28-58c7af8e08ca | -9.0919 | -45.722599 | 2026-09-18 00:39:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ab3158c-e506-3340-8470-f29e54994343 | -12.443 | -50.695099 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 70e03e0d-d865-3aa7-af80-f7aa037bf3d6 | -4.5482 | -54.926201 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58e3e88f-b7e3-39fc-a2f2-6b1608a25e20 | -12.3651 | -50.714901 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78a96ee7-0ccb-3736-8e26-ac63ea7850e5 | -9.7086 | -54.808701 | 2026-09-18 00:39:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9133098f-d426-37a0-bac2-2bc191d0a6d2 | -3.4531 | -58.218498 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c844f47-2ef3-34e0-a0de-34b5f0a33ff4 | -11.0002 | -57.061401 | 2026-09-18 00:39:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5efa327-acc8-3855-8507-ce550b5bed07 | -12.6222 | -50.879002 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0934e5d7-1a28-3667-aeab-6ffca663c2b2 | -12.2987 | -50.8242 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f1125fe-8923-3ab2-8916-177af28f56f6 | -12.4527 | -50.692699 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd5e0a38-11bc-3143-82f2-959a74b11b4b | -3.6015 | -59.059898 | 2026-09-18 00:39:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9f969fe-8fb1-334c-b644-7a9b71da13f8 | -6.0241 | -51.803902 | 2026-09-18 00:39:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8242fb00-6808-397b-a2eb-ef46a570a5ca | -10.8011 | -50.192799 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08a3ec75-9db6-39ba-80d7-0b77d637af0e | -3.3194 | -57.854401 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ddc5511-dbeb-3b53-9564-c3a90e29168f | -3.5582 | -58.547001 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a461177-8062-30f5-bdcf-2ce51d7e096a | -19.177799 | -48.785999 | 2026-09-18 00:39:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8ff1052b-a1d5-3122-b1d0-c0648c13fe96 | -3.4372 | -58.193501 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b62d8cd-f188-337d-859a-47256d129828 | -10.6383 | -50.286598 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17b79ed9-062e-3b49-99f9-acc1197baeee | -9.7005 | -54.818401 | 2026-09-18 00:39:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e060579-39e3-3d36-b145-433c514e1606 | -15.8079 | -52.573002 | 2026-09-18 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da319084-a9f5-3eef-9c12-eb04c8fb72ab | -10.8742 | -54.002701 | 2026-09-18 00:39:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3b6c432-39c2-33f4-9422-4731172cd3a1 | -4.8807 | -56.0611 | 2026-09-18 00:39:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81171153-2763-3a34-9030-dda4287f2d90 | -14.136 | -48.727299 | 2026-09-18 00:39:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7fb1cb58-ca46-35ad-8135-3f1469e1680d | -4.298 | -55.722099 | 2026-09-18 00:39:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07971487-853f-3318-a8e7-11a9179798e1 | -3.3012 | -57.865601 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92f8eeea-2074-3cbe-b8d6-9da8ef8b3ad5 | -8.8994 | -62.405602 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 04a9a823-5fd8-3abc-9ca1-320560d269e0 | -10.6291 | -50.249401 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2571f03c-5f78-377d-b26b-91d16df3b587 | -12.6248 | -50.889599 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6720a882-10b8-3307-9c99-0c788f340f7c | -3.3717 | -50.458698 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66f8c443-0555-3e8b-ae95-9073b90bfba6 | -12.2731 | -50.761398 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 786ece96-0168-3c22-a5ff-1f2675de68fb | -11.3076 | -43.417801 | 2026-09-18 00:39:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21968c53-625c-3ff2-a7c1-a95549b5cf8f | -3.035 | -51.382999 | 2026-09-18 00:39:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 213310b8-f2f4-3275-8422-3563824e889c | -12.4419 | -50.648701 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ed7b4a1-70d7-3b79-93c3-4e9bdd3e531d | -2.0487 | -52.174 | 2026-09-18 00:39:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb7c8fd-44c3-3b3c-b3a4-9a2588433cd8 | -12.2758 | -50.772301 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6b9dbf5-1220-3d50-ad53-e074e34ebade | -12.456 | -50.875801 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a9f67ab-869e-36fb-adcb-7d6c8c38bac7 | -12.162 | -46.9585 | 2026-09-18 00:39:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f22dd98f-d8e6-364a-a081-b07df4aa6078 | -2.8996 | -57.775799 | 2026-09-18 00:39:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90c2f8c8-7054-3907-ace6-3a16a765a801 | -13.3784 | -57.026299 | 2026-09-18 00:39:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ea2043e-5ca0-3870-9109-42cb44b98627 | -14.7637 | -47.143799 | 2026-09-18 00:39:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e9298e5-1533-3fef-9742-bb43866b3dff | -3.9251 | -55.7593 | 2026-09-18 00:39:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc97ab1d-5d1f-3590-8aca-bfea0371c5aa | 2.9639 | -60.421299 | 2026-09-18 00:39:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e910eaba-8a55-3d2f-8fb2-61778ef880a0 | -11.8084 | -58.171799 | 2026-09-18 00:39:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5da1d4e-c666-3e84-9a95-580644fbbe6f | -13.3863 | -57.0625 | 2026-09-18 00:39:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07ea6dd7-6256-340d-b36c-879bb08c547a | -12.5255 | -47.0854 | 2026-09-18 00:39:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a32d0de-4d7b-3c63-90b6-55a0f2a7fc0d | -8.8603 | -62.413898 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 80deb8a1-1e28-3414-b7a8-9f2a3ba70044 | 2.9623 | -60.428299 | 2026-09-18 00:39:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ac047c95-adc3-37f6-8728-48ce8879607a | -2.196 | -56.085499 | 2026-09-18 00:39:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee574266-2afc-339c-a991-70edd4c3468a | -5.7423 | -57.586601 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac9ad22-5313-3a66-a9aa-11465c270e0c | -9.3857 | -46.858799 | 2026-09-18 00:39:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7a93e7d-a89b-308f-ad52-0e3fa765d9b7 | -8.8896 | -62.4077 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8dfa3bd9-7abc-3d88-a026-253b7401d314 | -8.9117 | -62.4151 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 75d3d27c-29cc-3569-abaf-48b096dec305 | -8.9214 | -62.412998 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5bf8df6b-13ac-3138-8394-d2d565ab5b45 | -17.7857 | -53.130699 | 2026-09-18 00:39:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff513b81-be0d-3753-a059-3ef095e8d3ca | -12.4684 | -50.884102 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ca0abc05-c2c1-3a23-9af7-e77def817f2d | -12.3916 | -50.696499 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
