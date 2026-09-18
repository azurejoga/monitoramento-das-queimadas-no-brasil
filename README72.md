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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4e91427-10a2-31a3-b7a1-6577f4501d01 | -9.90493 | -48.38223 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85c6b2e9-bf91-3b19-98e2-63b0845ab16f | -8.45603 | -45.83864 | 2026-09-18 04:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 812a88db-ac51-3934-8d88-95bc13ef906c | -11.13606 | -47.72576 | 2026-09-18 04:57:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c82e7b8-08cb-3679-8a8a-c3ddd5f5c407 | -6.94467 | -43.11007 | 2026-09-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 272288b0-d6c3-3079-b968-0121e4fd17f9 | -9.27368 | -48.24969 | 2026-09-18 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4914836d-8ebc-348e-a598-a9af541ec3f1 | -12.62146 | -50.88873 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb59a4a1-5746-366d-af79-eb6ac559a958 | -6.59078 | -45.88467 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e85318d9-051f-31fb-9109-8f1299c63a04 | -9.48804 | -54.48212 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07a33641-c826-395f-9f0b-abbf23146633 | -10.79656 | -46.65254 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c220a9f-6ae3-3598-b4e8-f424a92db6bc | -6.27135 | -51.74657 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8892f85e-93fe-3f55-a6d9-00ca81cb9b13 | -9.71161 | -54.82684 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee7a6362-27f2-3d5b-9d53-6559f5ecf34d | -12.39597 | -48.48014 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 687998fa-e774-3ac2-aa58-8eea7350c8c5 | -12.62771 | -50.89352 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8945a574-fec7-3512-bd03-1c880823bb36 | -9.94548 | -45.28185 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d735721-9d19-3672-9cfc-a81be495b7a3 | -14.22355 | -48.51292 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36430e7a-be21-3ad2-a781-f56825479871 | -13.74331 | -48.79168 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98fef847-4973-3ec9-bbfc-5f78a48bcd9e | -13.74518 | -48.80533 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10a121a5-f065-3142-b145-0d7ee521e5e6 | -14.13342 | -48.7225 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 87a37b0c-8aef-3b2d-9a10-76f7bbfa6e36 | -13.61924 | -48.3051 | 2026-09-18 04:59:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fe18b540-dfab-3483-985d-892d2cc983b1 | -14.71569 | -50.30899 | 2026-09-18 04:59:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f760798-47a3-397b-a98c-d2a62024afd8 | -14.22422 | -48.50807 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b0d1561-67e5-3a4a-bd54-80d4a04ee14f | -15.56257 | -46.4546 | 2026-09-18 04:59:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8043417-5503-3df6-87eb-cd32a67d1b43 | -14.82578 | -48.26882 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91096f88-9108-304e-b35f-62aa43c8635a | -13.61993 | -48.30011 | 2026-09-18 04:59:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87e1cdfe-4f40-3ed7-bde5-2c95976027c0 | -19.18681 | -48.79499 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5fdd23b-64ad-329e-9fab-725e6c8d7785 | -14.89467 | -48.15092 | 2026-09-18 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a078125b-59eb-3ad0-9590-b9d0fe7d5c39 | -15.57299 | -54.23695 | 2026-09-18 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b8330eb-1e60-3212-91e3-c919a3c0b244 | -15.56197 | -46.45913 | 2026-09-18 04:59:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7502454-b7cb-3ef7-861f-c501e70dc4ff | -17.77493 | -46.47752 | 2026-09-18 04:59:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e6df05c-138b-3efd-8e20-ea766437efe2 | -14.80329 | -48.54719 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f9af5d0-8323-3132-a544-e354586450b3 | -14.93419 | -49.92664 | 2026-09-18 04:59:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e00b7d23-8a67-3a83-92ca-1af4810ebd57 | -13.68606 | -48.59547 | 2026-09-18 04:59:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ed4cc2bd-fca6-357a-89cb-e7f7502203f1 | -16.56127 | -43.99022 | 2026-09-18 04:59:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68f681df-f1b0-36da-9249-5227f330189b | -14.12894 | -48.72669 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f1ff8d58-5bfe-3003-9669-466a895ec268 | -19.5537 | -47.62939 | 2026-09-18 04:59:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9117157e-65a9-3a89-ae0c-77a66c21f7f3 | -16.79618 | -49.10091 | 2026-09-18 04:59:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48b0e926-cd58-311a-8097-5e7c936c34c6 | -19.18114 | -48.77513 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff970908-654c-3316-9cb4-611d21f8eb48 | -13.74737 | -48.78986 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ec31dc8-5aa2-332b-b0fe-2f79e5d6aa3e | -14.72267 | -47.50795 | 2026-09-18 04:59:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b8619c1-fa69-3627-a7f8-5805caad7aa4 | -19.1766 | -48.77824 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6dfa3210-9a7b-3fbb-9a09-48a362471aae | -15.6382 | -52.72242 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9dd81d50-2a8f-3cee-8fcb-47707ac34362 | -15.46577 | -52.85684 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 074fedfb-fb09-34ff-93b3-2e3e299c86a1 | -19.55424 | -47.62501 | 2026-09-18 04:59:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 830e314e-d1c9-3a3a-bc02-561c30cb48aa | -15.66376 | -52.73407 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6894e76-c36c-3031-9f86-847acf408cc3 | -14.94261 | -49.91949 | 2026-09-18 04:59:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8086fe65-7223-3f9e-8113-4a6f097b2e27 | -13.74613 | -48.79868 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c3e3efe-8afd-3e73-8384-c4140ce4d418 | -18.02678 | -50.94469 | 2026-09-18 04:59:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 080e1244-99ad-37fb-afbe-66c56fdaadfb | -19.18729 | -48.79128 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4dfa5c4e-e58a-3cc0-93e4-93249f61aa73 | -15.44527 | -52.835 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce304fa7-3a6e-3d23-bae1-c375591bc3e5 | -13.63827 | -46.93361 | 2026-09-18 04:59:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eca9e054-0991-38ad-92e6-ff210917d67d | -19.18569 | -48.77194 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5915795a-a640-3de5-bcef-8366e519349c | -14.23768 | -48.63739 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60b4d08d-a9b1-3bc0-9b2c-377a220a1b9c | -14.93479 | -49.92248 | 2026-09-18 04:59:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f32c1afe-e907-3d20-b089-e12c2412be68 | -14.89863 | -48.15168 | 2026-09-18 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c1df824b-a68a-38db-9ce2-84b516d3f4d7 | -14.7024 | -52.44778 | 2026-09-18 04:59:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3a9c815-747b-302b-932a-97bdc5d36edf | -14.10943 | -46.94039 | 2026-09-18 04:59:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5a0f6cf-20a5-3c17-86a2-5972fd6299b7 | -19.55755 | -47.63435 | 2026-09-18 04:59:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99ba922e-85b2-3fba-8099-ad62a0e37929 | -14.95895 | -47.53398 | 2026-09-18 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81e0fc90-166a-3104-8a09-f58d5a569977 | -16.56625 | -43.99429 | 2026-09-18 04:59:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef3fc062-bab0-3432-8a2e-c887592d757f | -13.60444 | -48.29757 | 2026-09-18 04:59:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e9ebcba-27ff-39b3-be9f-d17d3ecc432a | -12.10462 | -57.19463 | 2026-09-18 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa374d5b-a111-370f-8d42-e7680d3982e9 | -15.34763 | -48.10999 | 2026-09-18 04:59:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5057f4ee-6c25-32e5-b957-b5bda6d48f69 | -14.15053 | -47.01038 | 2026-09-18 04:59:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43079db4-e341-38fa-abd7-89659fe6722f | -14.94679 | -49.91608 | 2026-09-18 04:59:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5f3ecfe-ac84-30c1-b19c-64d55c7bbd0c | -15.33287 | -46.03919 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a70f4091-749f-3fec-89b9-f85860528dd7 | -18.37465 | -49.39808 | 2026-09-18 04:59:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 558fc3d6-caff-36b7-84cd-1d3740d11142 | -17.23393 | -46.78843 | 2026-09-18 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90f4f2ec-1df7-3675-bf87-77d6866e0431 | -14.17193 | -47.85545 | 2026-09-18 04:59:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4225561c-4599-3c27-b74f-ec1eb3cdf2e4 | -19.17708 | -48.77453 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b561f5a4-e0e6-3337-b44e-93fe66df16be | -14.1118 | -46.94313 | 2026-09-18 04:59:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6f4e1b8-42d4-340e-9707-fbd7ace49caa | -19.55315 | -47.63385 | 2026-09-18 04:59:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5c76804-f8cf-3ec8-ac2f-395ab7c48ec1 | -12.01923 | -62.49552 | 2026-09-18 04:59:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8194e77-0d07-337a-8cf1-388d81b94309 | -15.47293 | -52.87647 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c44ff4bb-549f-39f9-9b0c-9b531bcee734 | -19.18324 | -48.79063 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe86897e-398b-30bd-9fd8-0a13b7871adf | -15.6632 | -52.73767 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d27658e7-713e-3cff-8239-75e795b2762e | -13.75807 | -48.82339 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e0ebc58-a7a7-35f6-a7e0-faa2e1a40543 | -14.80118 | -48.56235 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd8547e0-0172-3c9f-a773-605195028f91 | -13.76761 | -48.03551 | 2026-09-18 04:59:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e0bc4f9-5ca3-3f41-b03d-3ace7024eb16 | -13.60316 | -48.30052 | 2026-09-18 04:59:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80bfdaa2-3ce8-38f3-9bc5-18a9880e78c5 | -13.42815 | -51.90003 | 2026-09-18 04:59:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5295530-3979-3144-9696-c25291b1f95d | -13.31221 | -51.29441 | 2026-09-18 04:59:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f769314-85de-3fd2-bec8-ea9af0bf773e | -14.76337 | -51.40133 | 2026-09-18 04:59:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f59a400a-fc1e-3a86-8e28-0a42cce52258 | -14.22809 | -48.50861 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bea6e3af-115a-3239-bb85-708535ee836d | -19.19134 | -48.79193 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 201e74f6-855b-358a-814f-0b0dcc20b2be | -15.63632 | -52.72256 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e04dd59a-ec62-3f37-9927-2620e57a35a2 | -19.55259 | -47.63831 | 2026-09-18 04:59:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1693cb07-111a-3c5c-93ca-3ea412180303 | -14.80507 | -48.56282 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d0065d8-3a7b-36ea-afc6-d4b79829aae3 | -13.74452 | -48.80984 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 917a5920-1295-3f91-9c9d-c079db3d9f7f | -15.85758 | -57.5668 | 2026-09-18 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff9f4413-da26-36af-ab60-f4179b17ce2b | -19.18519 | -48.77573 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2d6a26e-20d0-3666-aa1e-288a0075aac5 | -14.75996 | -51.40079 | 2026-09-18 04:59:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 342b07ff-ca47-30e3-82e6-d09fbbfcacf6 | -19.18925 | -48.7763 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 192710d7-e55c-3773-b98c-cd1342e7d538 | -15.56431 | -46.45687 | 2026-09-18 04:59:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9c762ae2-57a3-37e3-898d-991bde2e607a | -15.56687 | -54.23209 | 2026-09-18 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00dd8ebe-9e5a-3eae-afb9-dbfc5da66132 | -14.80575 | -48.55795 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e5d240ba-3c0e-3674-b5f8-cbe19815652e | -14.13274 | -48.72728 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 98e55580-6f81-3977-b491-b552f7b482df | -15.39256 | -53.01754 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d4492a29-379f-32f0-a4a0-82f00aab45b8 | -17.83623 | -44.84927 | 2026-09-18 04:59:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 993fe718-bba3-38f5-b72c-25d4934e65dc | -13.74491 | -48.8074 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf86b2fd-45de-36a5-bcf8-3ed568cf63d5 | -19.18422 | -48.7832 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README73.md)
