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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4e0c6be-42dc-3d06-8a1c-81fbcbdb376a | -12.98045 | -51.12454 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 203689fd-4ab3-3cd2-9420-e94a3a615f43 | -16.09993 | -50.45302 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de3fc97c-acd5-327b-88d8-e5896f751d0f | -12.97982 | -51.12831 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5d88bf3-c5e6-3eb4-977d-d3b7b57cf3fa | -12.97702 | -51.12395 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49c1e2fb-f895-3a51-83dd-42d544de5f70 | -12.9764 | -51.12773 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34f512de-83ad-3721-bad9-689b11d49205 | -12.78667 | -50.57739 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e85e1c9-327c-31dd-a9db-512ee4089fb2 | -12.78329 | -50.57681 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f775d770-4296-3064-9f37-f7172450fd18 | -12.77653 | -50.57567 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46741165-4c83-3b2a-a4c2-11c1da820fef | -12.61461 | -49.64779 | 2024-10-04 04:34:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d701b6f-91a6-33be-a074-a086a17ab90e | -12.61405 | -49.65134 | 2024-10-04 04:34:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fad3ab32-9f38-311b-81f4-63cc4b73a2f1 | -12.60964 | -49.63605 | 2024-10-04 04:34:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0beba88-e97b-3937-96e8-859dcc78df36 | -12.41296 | -51.0277 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 479aa72f-a992-3a9f-a36a-614fd56f9b01 | -12.41235 | -51.03149 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dffa8676-27f5-31ce-a784-56e0889804fc | -12.41096 | -50.95368 | 2024-10-04 04:34:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10e3dea2-bc5a-3a72-b567-ea3bcd4f101b | -13.2653 | -51.22335 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d546a9f1-ad3e-3f7d-a7a6-828a8286340f | -13.14383 | -51.19513 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e39e7b7c-ebe6-3e61-b2bc-0a98567d7648 | -13.1404 | -51.19455 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ccb6be2-77ce-35da-b817-5878c34b7924 | -13.13073 | -51.18898 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7febc404-e56b-38a6-801d-2c8cbc3b2d2b | -13.1273 | -51.18839 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 199b76bc-94eb-38d7-b185-3a61f0881ddb | -13.11919 | -51.15198 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1d57dee-1cfc-3eba-a17f-34f2e4cc8c78 | -13.11857 | -51.15576 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ec9f660-133a-324f-a176-10f50ab447a7 | -13.11639 | -51.14761 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 680c2b18-9aa1-3087-8b79-801ae00ac296 | -13.11577 | -51.15139 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 167b58ab-13f2-3288-8e56-775b00e0d702 | -13.11514 | -51.15517 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ae00f3c-128e-3edd-987c-4c1efa78c187 | -13.11452 | -51.15895 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c5b9a98-231f-3fe0-ba11-cb3f0c362a31 | -13.1139 | -51.16273 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8b1bf72d-95df-37a2-8c7e-a8430081c049 | -13.11297 | -51.14702 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d5dba668-0725-33b5-afb1-52c2f11139cd | -13.11234 | -51.1508 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fad670d9-7d44-3711-b334-7ee4eea46001 | -13.11172 | -51.15458 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d7e75ce-863a-3e66-8b68-cd271cd8ab89 | -13.1111 | -51.15837 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3e171ef-0870-3201-b2f3-036110d5d607 | -13.10954 | -51.14643 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b8271c9-91a1-32e3-b1d0-b8f3bcb3e51b | -13.10923 | -51.16972 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d43a4e3c-2d81-3f8b-828c-8575571f6336 | -13.10892 | -51.15021 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c64064c-f1ae-37b4-9456-a67f46e2ecd5 | -13.1086 | -51.1735 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2388b6e5-0ff6-339e-9e5c-30e068b34232 | -13.10829 | -51.15399 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f2dd7a8-798f-3311-b16a-29bca40ca727 | -13.10767 | -51.15778 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 233baedd-0125-367d-bb0a-078c79b37730 | -13.10705 | -51.16156 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d6fc210-e6b9-3191-b21d-ff3d28034873 | -13.10424 | -51.15719 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75806fe3-0842-3788-a12a-f74a49030d57 | -13.10362 | -51.16097 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a23ca8c-951b-32b5-92be-f4c42fdaf7e8 | -13.10019 | -51.16038 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87060a5f-1446-3332-9908-6f83255c914f | -13.09957 | -51.16416 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 762760da-bef6-3034-95af-d9dc57a63553 | -13.08557 | -51.14232 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5f19c87d-3ea8-3816-902d-53f2e2f06cae | -13.08214 | -51.14173 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b650226f-a6e4-35c2-86b5-cdfbc6cb4154 | -13.08152 | -51.14551 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2a798cfc-e64c-31fc-9f9f-3633883674cc | -13.07809 | -51.14492 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 81875504-2993-3728-aa93-ae713072d684 | -13.07746 | -51.1487 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa54c06e-82c6-334e-b7d7-942b188c2e62 | -13.07529 | -51.14056 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fab75c7-fd76-3a0c-b310-294d2a95820a | -13.07467 | -51.14434 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1993a51-d12f-39fa-ba2f-73983def65ba | -13.07404 | -51.14811 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1bd2868-2b5d-3ca0-b149-846414985667 | -13.07341 | -51.15189 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66ba3d65-dbe9-3d04-a3c1-285db6b7b3c5 | -13.07187 | -51.13997 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4302535-52b3-3c65-8b7d-61620035e3ca | -13.07124 | -51.14375 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88fbca39-323c-3704-a07c-6e30e94dd628 | -14.40987 | -50.03848 | 2024-10-04 04:34:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73523207-5aa6-3539-a085-b7ba358b85c0 | -13.9332 | -50.85489 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa500231-5f10-340b-8af7-dbf820da97f3 | -13.93042 | -50.85063 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e5c304f-a18f-3811-8a88-8ffba716835a | -13.92922 | -50.85799 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0583fd8d-a48f-3562-8275-54ae94ba7f4b | -13.92862 | -50.86168 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6b4211d-c57b-319e-8b88-57ddd7edfd2b | -13.9284 | -50.88439 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae8514f6-c460-350e-adc8-68faa70d3f8c | -13.9278 | -50.88808 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07333192-5908-3622-960f-4f977a4ba98a | -13.92764 | -50.84638 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c4e6b0f-b95b-323a-ad58-e86e5aad6f68 | -13.92426 | -50.8458 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a597ea2-8e61-3433-825a-ada7ba984823 | -13.92066 | -50.8679 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfe2ddb8-f454-3949-ba3e-b95c9092c00b | -13.91728 | -50.86732 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 193793ac-16d2-333a-ad90-a2aeee93ac10 | -13.72435 | -50.89244 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eb28784-42bd-3c46-b5e2-03202547cb03 | -13.72096 | -50.89186 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0e3e6fd-c336-3bd4-a780-e8b82ebe8952 | -13.71758 | -50.89128 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dddb08f-4ea2-3739-a40d-900f1f9645f5 | -13.71419 | -50.89071 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87f000f1-0d66-344a-99ff-f2848e42023e | -16.12506 | -50.43912 | 2024-10-04 04:34:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54df93f0-0ca3-374e-9991-f773315e8b9b | -16.12449 | -50.44273 | 2024-10-04 04:34:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64d5a2f7-5368-340f-8ea8-d8b07405c9e2 | -16.12391 | -50.44633 | 2024-10-04 04:34:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53101a3d-234f-3f29-802e-ccb0dbafeafd | -16.12288 | -50.43135 | 2024-10-04 04:34:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 690e1e93-96bc-3e02-80a4-8681845387c0 | -16.12231 | -50.43494 | 2024-10-04 04:34:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55d27d8e-0924-3eb4-8c46-7ae8fc51236b | -16.12059 | -50.44574 | 2024-10-04 04:34:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e82d533-b2c5-3048-b65c-32867ba1bb74 | -16.12001 | -50.44936 | 2024-10-04 04:34:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbf901c5-8a71-3a99-af2a-fd3b58d14e9f | -16.11956 | -50.43077 | 2024-10-04 04:34:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56beebe9-b12e-3e2b-ac56-18a8aa901f27 | -16.11943 | -50.45299 | 2024-10-04 04:34:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50e99c40-f23b-3b15-80b6-4e4f6aaf9065 | -16.11669 | -50.44877 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6f7abe9-8807-3a9c-9261-d87db249aaa5 | -16.1161 | -50.4524 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c3cf4e3-284d-3132-824f-d98c733581b9 | -16.11552 | -50.45602 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4a86304-25ba-3b18-b6cd-53cd60e3ae4b | -16.11278 | -50.45181 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 821b1d83-7b2d-36b0-ab83-dacbd3d9d809 | -16.1122 | -50.45543 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85f3d633-b05f-3159-83d9-61add28677e7 | -16.11161 | -50.45906 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d1a963a-7cee-374b-8132-652cb0202c15 | -16.10887 | -50.45486 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1188fde3-f29f-330c-a327-98690add4e73 | -16.10829 | -50.45848 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9518530e-35ae-31fd-b1c7-1662b2a7a249 | -16.10554 | -50.45427 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3b7463d-cbc9-39fe-a9ad-1e37b68eed0b | -16.10496 | -50.45791 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d15d43ed-038d-3eff-b767-68009dfd865d | -16.10221 | -50.4537 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3da5477e-b9d8-3f83-9a70-d37292ec3355 | -16.10163 | -50.45734 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 838810b8-ca13-311c-9137-442df4e8d6ca | -16.09935 | -50.45667 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12d7e090-ebd4-3db3-9d25-e0870c6dde28 | -16.09878 | -50.4603 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a31db2fe-e2cc-3f7e-b48e-c846d6ca4665 | -16.0966 | -50.45247 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b72b43a-4560-3804-b34f-b960ff700279 | -16.09602 | -50.4561 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be6837e0-3f7e-3fd1-938b-9cc55bd5adb8 | -16.09384 | -50.44829 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f727886-1926-304a-b036-6affff1a898f | -16.09326 | -50.45192 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41ae8911-52c5-30ef-91a4-f17d1cbc8372 | -16.09269 | -50.45555 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80504b80-2486-3d36-9607-a636ba2a9c2d | -16.09166 | -50.44046 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a76650c-69d5-3e68-9756-51f95efc64a9 | -16.08224 | -50.43524 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4231a54a-f703-37f8-a973-61066b696be1 | -11.22066 | -51.21477 | 2024-10-04 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 261dfbe2-85fe-306b-a42c-de515b39e3f2 | -11.22001 | -51.21866 | 2024-10-04 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51312f96-e47e-3948-93f5-759a9a9e2c26 | -11.21717 | -51.21418 | 2024-10-04 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README123.md)
