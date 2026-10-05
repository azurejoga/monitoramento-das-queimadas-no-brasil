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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46855be7-01d4-3061-ad38-32e479cc21fd | -4.04238 | -50.76497 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0abf3c69-8670-32a6-810e-7e5bff25598b | -2.69546 | -49.04009 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2787684c-a49a-3c55-8078-21ca8cb805ce | -6.87864 | -43.67656 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0d000470-48d7-34c6-851c-201f7e51fde5 | -2.8053 | -54.12246 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24eef34a-4346-3bca-845e-5508f85a692d | -3.13351 | -53.71498 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| d8997c12-7a71-3614-85a0-dad52cc8db95 | -2.97728 | -54.10278 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d02abf28-36de-31d6-96fe-e3c6994edd03 | -3.70735 | -40.34998 | 2026-10-05 04:57:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4a58d0e-0b0b-3820-83ea-c71c0aba390d | -2.47354 | -48.04238 | 2026-10-05 04:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ddb5a92d-34a0-3ae7-94ec-61e6f46945da | -3.05394 | -54.21461 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9846e31e-a54e-3955-9b7e-e6dee708306a | -2.94103 | -54.19733 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db4f8093-789c-3483-aef6-4c7c7c234e5e | -3.12673 | -53.7139 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 6bd21658-2d2b-3521-b6dd-2e10f1285636 | -6.9177 | -43.67153 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04b2e60f-81ef-3fbf-ac72-c46c7977a45c | -3.33052 | -53.38897 | 2026-10-05 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf9fc4ab-eba7-39f4-9b9b-819522d20816 | -3.87413 | -55.80598 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f72a2c26-803f-3a58-8c01-d0abb336d0c6 | -2.79333 | -54.109 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f8570ca-1cb8-3728-9034-5898857c6a50 | -2.81177 | -54.10422 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8f32e36-887c-3e18-8d66-c05cc74cbad5 | -3.01245 | -50.47066 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0829887-f923-3667-ba85-67517c535552 | -7.44428 | -63.569 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1490171c-ad76-329a-a1cb-a147aee4ff85 | -5.99381 | -53.52562 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d5adfd4-d235-3e9b-8435-029026d80c22 | -2.82934 | -54.21553 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd82ba24-525a-3e72-babb-8f3155254bc3 | -6.21622 | -52.78968 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15bf7da6-ab68-33e4-8a90-639c99eab11a | -3.06114 | -54.16941 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e178e969-6291-3422-81e5-09be40ee1817 | -6.06117 | -53.465 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e9c4d1e-fd9f-3513-9506-a4c30c606eba | -2.58996 | -51.8517 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07889c5a-d68e-39ba-b5b0-b4feb4fcb02f | -3.10977 | -53.71121 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c7defa35-7bfc-35be-bc23-0f32dd0d89e9 | -2.80549 | -54.09937 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 818aecdd-7ce9-3d43-bbd0-42c021afb3db | -3.2768 | -54.00411 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53a56d73-1e77-3515-995f-1afeafe74247 | -3.31915 | -53.84873 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 308d2bcb-d6b7-3ee3-9c4e-6f783dc65108 | -3.37605 | -54.10748 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b590388c-c963-380a-be00-3af240363447 | -3.26996 | -54.00303 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d03b4355-f73b-3f08-bebb-34ce06a1d27e | -2.98072 | -54.10332 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dca67a99-5143-3c85-befd-19010a6480d1 | -3.15752 | -50.44483 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 56e25f38-1c93-3782-a415-811b85362365 | -3.12258 | -53.76177 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 96604450-392e-3ac2-bfe0-eaff8fa37a5c | -6.00491 | -53.52016 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71bc7a28-ea31-3a76-b1de-1ca5e1cd99e3 | -3.31574 | -53.84818 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 314e0896-345a-3153-8cdf-26780f913f82 | -4.45514 | -54.96561 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33dbd3a1-843e-35f8-8bcb-abd661a7afa8 | -6.17944 | -52.93608 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b128cc33-46cf-3a89-90c2-a960b5aa6812 | -8.67658 | -54.55603 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c034369-b9e5-3f8d-be6c-935a68179b3e | -2.89836 | -54.13255 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28e5426c-1b1e-3186-8379-8801da3bec6d | -3.0196 | -54.18594 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df025646-f525-3618-b1ef-7940bbfdb92c | -1.20921 | -55.8625 | 2026-10-05 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79e6cdc7-4a59-3ec4-af5b-7ac7d6b83c70 | -3.88151 | -55.80722 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 12b7ea99-f37b-3652-9b06-716b48346340 | -4.30663 | -50.78373 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0959603b-807a-359e-876e-38c4ac7fd46d | -2.92954 | -54.1144 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd72f8bd-1b65-351f-8244-dc3cbc5f8277 | -2.90623 | -54.0838 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| af8e5206-731f-3ad3-bfa6-b5b65f181f66 | -3.83956 | -50.31638 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ab1a6a5b-0afa-309c-bf3e-6f1e770dd447 | -8.66872 | -54.56212 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 50c8e3f2-bab2-34eb-aaf8-90ef74e01d08 | -2.75671 | -45.5511 | 2026-10-05 04:57:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f94810e9-1d28-3bd9-9b4d-114726a6fed9 | -8.22314 | -50.21809 | 2026-10-05 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0be7e9e8-3b69-3c09-b1ad-0cfdb68627b9 | -3.57525 | -54.65146 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d34a542-818e-3a57-afa2-fa263d650195 | -3.11423 | -53.72683 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 831411d2-e6a7-3dd3-88b8-c9169fd84e39 | -2.7992 | -54.09452 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd4dfcf5-e4db-3499-9810-d412df418d62 | -4.29535 | -50.76715 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0165d5cb-1305-3763-a735-346fc7488add | -3.57463 | -54.65532 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12c05b25-9817-39b2-9736-e024341bd740 | -2.91396 | -54.12346 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 912d2ce1-ee98-339d-97aa-885d6bf5d610 | -2.93265 | -54.16116 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a036329-49e2-31e7-861c-8bf43338d544 | -2.81866 | -54.10531 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 144d9b51-546b-3e72-a816-b7af29cbcf7a | -3.61611 | -54.59831 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47f47ca1-0405-31f5-b23b-15780b1031c0 | -3.50985 | -54.60602 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b7182f66-a55a-3dca-9344-7fe0fcfac71e | -2.95004 | -54.14082 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f6d552b4-c6a4-33dd-8333-07b5006660c1 | -2.8128 | -54.1198 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 176bb203-5e9e-35f3-b1c4-a8a785f0bdf4 | -2.94555 | -54.12468 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93bfede1-5c07-33d0-9f3e-580ee171c982 | -2.81642 | -54.09725 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3ff4f10-371c-39e0-ba01-3e89e0c8babc | -2.89125 | -54.15462 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df376bf8-9761-33e6-86f3-eb295496a376 | -3.28006 | -50.4006 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c0b0d32-3151-3807-aafd-32aeab35e60e | -2.58941 | -51.85513 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ec65a91-8b49-34b5-8d98-37e19e58a97e | -6.26721 | -52.85388 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e13a0d9c-8d23-357b-a043-ee7400131743 | -7.21832 | -55.20193 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 292a2373-a239-340e-9569-ca8b70c4a6af | -3.60768 | -50.97599 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9fe2738-5ae2-33c5-9083-68c71393f50b | -3.64882 | -55.32106 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 841ece54-5d9c-35cc-b95c-57d8f25f64a9 | -3.28341 | -50.01962 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30b1df5b-9c46-39a6-ab2c-92f978862dbc | -6.00547 | -53.51666 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d16b14eb-ff7d-3b39-855c-d67769951cf2 | -2.80325 | -54.09131 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5974517d-9e94-301c-abcc-caaf08c3bb4b | -5.89438 | -53.63928 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 252643a4-7426-34eb-9d88-2f1b7e6380c1 | -3.76839 | -53.41419 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2c2b992-5cec-3253-8964-8fd380a71e73 | -3.09668 | -53.72778 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c92e3055-d70a-301b-8a4d-cb15f6ca69c8 | -3.11481 | -53.72319 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09a3c79e-779d-3ccc-8e73-ae27254c9ec6 | -3.4844 | -59.72958 | 2026-10-05 04:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6c74e377-e3f8-3e09-9acd-d076c59f1067 | -1.64346 | -55.14675 | 2026-10-05 04:57:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af96c9e7-a8f3-386f-9048-9899e7cb80e0 | -6.00768 | -53.52419 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 578cf070-6533-3a30-9179-18f343658a30 | -2.92997 | -54.13373 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 407e442b-8885-3a7f-b755-02d1fea86174 | -2.90219 | -54.08699 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 509c9b46-c97e-330a-a239-2ca428aef449 | -3.07888 | -51.27428 | 2026-10-05 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9eb79d3-d5f7-31da-8227-74e0fa1e0c5f | -2.9304 | -54.15309 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45003691-e874-3299-b6f6-b05c1791a6d3 | -2.57954 | -51.87471 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cb865a0-71a9-3246-aee2-30b8cf8f7999 | -2.81358 | -54.09295 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5418cd66-1f1d-30f4-a36d-796a7fbf8cf0 | -3.69534 | -49.63141 | 2026-10-05 04:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a24011dc-ac4b-3939-9796-898ab9e30ca3 | -7.22993 | -55.19601 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22de771a-db0a-360d-aca5-18894996d02e | -6.42838 | -43.72119 | 2026-10-05 04:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5709d941-6c4e-344e-97b0-fe2b8ff6994b | -2.77872 | -54.09573 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 803df2cc-cb71-34d2-ab8e-bb38b713b412 | -3.01188 | -50.47427 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c2077f1-822b-3828-8e70-5f3a9b4eb738 | -2.95064 | -54.13707 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21f0f731-2f2b-3d96-a5ca-ec6177cb36da | -3.12057 | -50.34263 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3db3497d-43a6-319b-871b-21dedbd81fbe | -2.82659 | -54.12199 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d423366f-7db1-311c-ad37-3821939f95d5 | -3.1056 | -53.75908 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3ed311ed-8900-3f4d-b7d1-3fdbcaf1edf7 | -3.06744 | -54.17427 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d52bcf36-91b7-30dd-b35c-4ce0b272128c | -3.84071 | -50.30898 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 511de1a2-3f63-31ca-bea2-6aeb86db4f1e | -5.95834 | -55.3502 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33e87991-4128-3d88-b128-20d76b7519d8 | -1.51033 | -54.80994 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49087fe3-7330-3bdc-9eb7-167a8e0e0f12 | -2.48423 | -56.10428 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README42.md)
