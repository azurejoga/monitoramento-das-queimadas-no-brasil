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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8c47705-d2ae-3f17-b897-d241e9053c80 | -5.71608 | -44.82707 | 2025-10-08 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9787f99-db7e-3662-8d92-b818c9630d8c | -11.7965 | -45.04953 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3020d7fc-4127-38df-a003-7ce5b0ac9a19 | -13.36303 | -47.56009 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 63b4dc88-ec3b-324d-8d31-a85fa1e8a6bb | -11.37765 | -54.3451 | 2025-10-08 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6011203-aebe-34fb-8f73-0704da29ac35 | -10.42169 | -48.10048 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 486781bc-5f5f-3428-b4df-a283bc84931f | -11.11894 | -54.03848 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fe2f26c-a4da-3bbd-aaba-0c75efa48250 | -11.70642 | -46.35599 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d5f06ff-760c-3231-876f-8e64844a5fe1 | -5.30089 | -45.84825 | 2025-10-08 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 558b280f-0aa6-35ae-8aad-cf266b9b404b | -12.01431 | -45.19093 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 859bb2cb-a474-3172-947b-9569c1cf1a91 | -11.68266 | -46.3284 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a96df7a-3c75-3bbb-9b20-8e969c583bef | -4.25997 | -48.55976 | 2025-10-08 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 152eee11-7f5f-3d98-833a-9d4182d23734 | -13.34902 | -47.25457 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8b8dc44-db43-31c2-b1e1-2c1a1c026eb9 | -7.03058 | -42.86813 | 2025-10-08 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7626ac34-64dd-3c44-b247-24cb5abb8b98 | -10.38565 | -50.22878 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5f2f5d2-73ac-3b58-b237-18a821fefbf1 | -11.70245 | -50.99626 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99222b95-f2df-32f3-aa2f-e793a5b0f726 | -3.19478 | -51.02057 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dd181c3-b9ea-3c15-955e-c74de5b5d85e | -3.09397 | -47.02152 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4776e9af-93cd-3387-b056-7e0d5ef78523 | -5.77905 | -45.74218 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5782a7c5-2b29-36a9-a4b3-8264f5d6675c | -13.27471 | -47.56272 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f70bef43-9734-3255-af66-971047c0ca80 | -3.43183 | -43.14714 | 2025-10-08 04:17:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d512d402-e8bc-3365-8d69-bc2b62d085f0 | -11.78479 | -45.05845 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8164e4d8-3a0a-349d-a0a6-c70065a13404 | -12.11886 | -45.12757 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 511e06d3-57b9-379e-afc8-8a4c72c75882 | -4.57524 | -41.29678 | 2025-10-08 04:17:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b5ddf408-53df-349c-97d9-c44333741d24 | -4.91914 | -48.54388 | 2025-10-08 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f28c181c-2686-343d-8250-eae15d575fbc | -7.00344 | -42.88886 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| bc5fbaa5-8361-3af5-8367-9c5dd0a5d15d | -6.27533 | -39.68511 | 2025-10-08 04:17:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ceb34bf9-c522-32a9-8004-92cf3883e978 | -11.16591 | -54.88374 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba9f7db1-df84-35e4-b264-a91ed7bdde56 | -3.83738 | -50.9697 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69874dd0-2003-318f-8ce1-6b5cc5fde014 | -11.7807 | -45.10523 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23391463-1f06-310a-9fe1-d0f77c8b6023 | -3.57855 | -49.43692 | 2025-10-08 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 553676e3-60e1-3741-bf55-43a2ff329dc6 | -7.00896 | -42.87543 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 96382ac3-c243-3310-b497-2b2d0639ce7f | -3.45433 | -45.59785 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d627b7b9-05e5-3082-b455-7a9028dcdfdb | -4.30836 | -48.08147 | 2025-10-08 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 264d8000-db02-3531-864d-7f59a6cbe2da | -5.13545 | -44.96792 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7217be9a-8238-38ef-b55b-f13043b22d45 | -7.79227 | -42.6246 | 2025-10-08 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6ae069f6-2206-325e-8e5d-b344626c7511 | -4.69542 | -45.83696 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 097cfeb4-b307-3da9-aa46-46838942a375 | -11.13608 | -54.88877 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e614d9a2-1a85-316e-99b2-b5af301465b9 | -11.80765 | -45.0441 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dddca005-ba71-3306-805d-950c983a25b8 | -11.44449 | -43.47967 | 2025-10-08 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc468096-6f4a-3a8a-b169-41079f8ba528 | -6.99618 | -42.86985 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 88d18110-9d26-35fb-8552-c1810649a8ff | -11.78107 | -45.14569 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63b9e48b-8f79-3e93-99fc-bcc839c1130a | -11.15592 | -54.87978 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91e233e1-faa1-3c39-ae06-f5f580f66980 | -13.03412 | -47.91702 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b626a27-0f43-32e1-9610-8f5754a23c3c | -12.24217 | -43.77129 | 2025-10-08 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67763203-d26a-351a-b861-2fb4a071831e | -7.437 | -43.14651 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 166253eb-95b9-35f4-974a-be0d27e1b6cc | -11.90611 | -46.20212 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c425bbee-88d2-380f-9bb0-dc57cd74c211 | -7.51172 | -42.71415 | 2025-10-08 04:17:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d43e1f59-35d4-34bc-9067-f9d260480be0 | -11.16492 | -54.8644 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 116c051a-016b-3fe6-9948-9dbdc9df021e | -11.02331 | -51.20998 | 2025-10-08 04:17:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c1f0f97f-1800-3d8f-84e3-f3cb58a48c94 | -7.79282 | -42.62108 | 2025-10-08 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d53e72d6-cb5f-3875-afb2-5228e28c47e0 | -10.82891 | -42.69653 | 2025-10-08 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d0ac86bf-313c-3255-ad42-9d008dd0c11f | -12.63783 | -50.56213 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a8c7d5b6-31fd-37e8-bbdc-91fe16d0225d | -5.25671 | -44.14048 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8b78604-0d30-3531-960e-8f28a1e276da | -12.92618 | -46.82092 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64712e96-c768-338e-b78c-bae3f7f63499 | -6.25361 | -45.04443 | 2025-10-08 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3715af17-be56-341d-8030-35d2ca25fe56 | -7.26255 | -44.11669 | 2025-10-08 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 443c5dd3-9b35-334d-9494-adfea5e9650b | -3.24034 | -46.79078 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aed68634-a790-331a-b96b-1f27ed567938 | -13.36236 | -47.26113 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bce88de-5c59-35d5-9e48-f5d3aeb409be | -7.00066 | -42.88485 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3da9c240-ea33-3c20-8764-7c9be39f59b0 | -12.93429 | -46.85816 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 621fc516-f9d2-30cb-9d95-76bd45e4537a | -11.66727 | -46.40009 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56299354-eb2a-3d08-96e8-15eed341ff9c | -11.16839 | -54.90908 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 216684ad-3dc6-3e8b-8369-e5f4492770cd | -13.05362 | -47.89033 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f02373e-4420-3b38-937b-16b4df4b5112 | -12.24992 | -47.86662 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f7cd7eaa-feb9-366a-93f7-d17d0d4dd6d6 | -12.24162 | -43.77482 | 2025-10-08 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bb8f446-d6fa-3793-a9e6-d8626bec421e | -12.70294 | -44.94625 | 2025-10-08 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6c0361e-2494-3711-b89a-faf66a94b363 | -11.47742 | -43.48857 | 2025-10-08 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b12bf669-e741-3097-acf5-98a640621013 | -11.70152 | -50.96521 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1aa8fe3f-77fd-3eeb-b022-bad74192bb8d | -3.14234 | -50.29752 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e42c2186-0f2d-36e9-a5c2-5c4f2a8df5f6 | -7.47741 | -43.10648 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 90e9cd01-1ca0-3dea-8fec-794b1d12ce7a | -4.40401 | -49.76559 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00d57347-bbf5-399e-a302-3cba5b25ecd3 | -6.1362 | -44.60388 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ab6cdaa-d100-3b1d-a96a-ab1350ffe147 | -10.67741 | -54.69843 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 789156cd-ea7d-3144-bec7-a018688640f9 | -2.51562 | -51.93257 | 2025-10-08 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9271f6d-ee1f-3aa2-9e68-43478be7b11b | -10.38998 | -50.22957 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a5e34556-38f3-3205-8b73-66a74378594c | -12.21544 | -44.26125 | 2025-10-08 04:17:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 88668ab3-e793-3b52-a228-615a60e42cff | -3.73923 | -44.26577 | 2025-10-08 04:17:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3fb3e971-f7f8-327a-b433-1856648e6e8e | -7.46231 | -43.02905 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7fc1cf62-458b-3966-ae9f-decd04c76407 | -6.06688 | -44.31898 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d954781-68dd-3623-be3f-316d34630d07 | -13.06168 | -47.95271 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4a99fce-dc27-31c8-a2aa-0983da932f40 | -10.99782 | -51.25256 | 2025-10-08 04:17:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a8c7daa-040c-32e5-bb7d-e5d04adf924a | -11.8603 | -44.92879 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d0dbb30-75ca-35ee-916d-1cf032a6d090 | -11.72012 | -44.29716 | 2025-10-08 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c19d6c7f-a270-3028-95b2-2ba111e4c1cc | -11.81009 | -45.13589 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed3a84f4-f3af-3d68-b94e-cada6b0f906c | -13.82263 | -41.29286 | 2025-10-08 04:17:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ec4473b9-6cb5-3e6a-a3ee-5d6b14533d9a | -7.35063 | -43.8647 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a6f5cdcc-fb6d-3862-9fb0-1cb5e562bd19 | -10.04968 | -48.28324 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85dd2d10-6d17-3f11-a024-c728405c648e | -4.69045 | -45.84467 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 756afa38-5128-3b96-a7b9-55bf995544d2 | -11.16757 | -54.88195 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d4f66b4-39ae-337f-9a3c-2d5bb912b70d | -4.05316 | -47.50383 | 2025-10-08 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1880d5a-416b-30f9-b41b-9645d5f6f147 | -13.04935 | -47.89344 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2518e20-f66d-3a25-9125-dc905aa5ae4c | -13.35947 | -47.55955 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86fb5fa6-6ccb-3160-9bcd-6b0d5db94e4e | -5.39631 | -40.99461 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 8d4aafe9-31e3-3259-afe3-766cd63b79b0 | -13.06973 | -43.59205 | 2025-10-08 04:17:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ada3bcf6-8b11-388e-aafe-6f1677bf9e50 | -11.04991 | -44.78519 | 2025-10-08 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d56cec96-840b-34ed-8297-2daef62d3f64 | -7.72845 | -42.40353 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d02cc686-3c98-38b2-bbf7-5685c1b7f249 | -12.0254 | -45.20742 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fbc03f83-388c-3904-a636-003891c94da6 | -11.14663 | -54.86551 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4222898-d919-3d50-9add-eb6f57a75615 | -7.15501 | -43.84027 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9940abb2-a2d8-393b-9a97-02befb3077f4 | -7.28831 | -41.9766 | 2025-10-08 04:17:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |


[Clique aqui para ver as próximas entradas](README39.md)
