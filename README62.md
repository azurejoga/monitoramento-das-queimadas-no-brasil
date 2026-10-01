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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f94c7a56-d4fc-32a7-9407-07374a639fbe | -9.19905 | -45.81786 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0576d6f-7800-3bf3-bf64-82d557a79154 | -13.42749 | -48.83284 | 2026-10-01 04:34:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d77f99d-0511-31ef-bd79-6845ae17a19c | -11.18609 | -45.1072 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7052d17f-3fe9-3b7c-920e-8a49d783356d | -12.26104 | -53.99644 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2661351f-7133-3611-afd9-f35b9ac9ae7b | -9.81044 | -44.83482 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67c5f4a8-f212-3398-8991-5a1fc33d0103 | -6.13887 | -53.25694 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6543b922-44c9-3bb6-b894-dfa9ec93b429 | -8.137 | -43.43222 | 2026-10-01 04:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef0fbbb4-bd4c-394c-9f3c-0902f53e36ee | -12.86346 | -44.34072 | 2026-10-01 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ab1ed47-4b5b-340f-bfe0-b98d7f97e388 | -11.2236 | -45.18942 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4dde2483-22ff-39c2-8464-f16c16848a81 | -10.66056 | -50.76371 | 2026-10-01 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b006923b-00c3-3840-ae95-6b110483bd22 | -10.5302 | -57.77736 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87769afd-718b-3658-a7a7-08e6519797d2 | -10.84454 | -48.70642 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ac35e98-d16e-3459-8c00-73f84ef873df | -9.80929 | -44.81872 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 519fcf6f-0ad9-3a4c-9f92-2312f1ff9abe | -12.70003 | -54.0707 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef552fd0-a0bd-370c-901f-355cf16c58a4 | -10.78512 | -50.53611 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c03dd18-3803-3e04-be00-74b2aa603e8e | -12.70935 | -54.0682 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f80e398-e02b-3836-a1bc-eadbe6f54743 | -7.84487 | -45.82245 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 44af27e4-35a7-3104-8119-3e0badb9c1ec | -9.21184 | -50.6821 | 2026-10-01 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2c81491-2c45-34fe-9453-1ea4899c4bd3 | -7.45546 | -54.99391 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e77b0efb-d356-372a-813c-c262c1e12b5d | -7.54535 | -55.03848 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f74d37d4-74c4-3396-bfe5-982f3ca3d51d | -7.1907 | -46.54795 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 392ccb1f-2c15-3e7d-a16b-e68c34404b68 | -8.04622 | -45.47036 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44b1a038-a090-3346-8abe-223537c44cfa | -13.37747 | -46.83837 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eba95059-98c7-3a57-a5b8-716880ad3431 | -7.9934 | -47.20621 | 2026-10-01 04:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc5d154e-ffe4-3553-84b1-0a453d62743a | -11.83566 | -44.74876 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f1575a0-983b-30f3-ac24-25cb6b734a4f | -13.51652 | -46.8866 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e5d3a85-d8ea-37b2-bf6b-b2b0ac2db23f | -9.52787 | -45.36018 | 2026-10-01 04:34:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc3308ad-fc4f-3991-a0cd-dd0dd1117959 | -13.37411 | -46.83786 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 949631fe-82db-39d6-b18b-937d0184c95f | -8.19994 | -45.50174 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 958bb642-f52b-3cb5-a40c-27c75bbeb163 | -7.50793 | -44.53979 | 2026-10-01 04:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3104fe99-8218-3d23-8216-cd2df562baba | -11.44604 | -43.43851 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fe0470e-f8fd-3ef0-8f23-9e4e872df3a9 | -10.45974 | -46.77242 | 2026-10-01 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fa48f55-1f45-362b-91d5-9d87b42f8f88 | -7.49049 | -55.00013 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c223e98-aa10-3acc-b58f-c654557a4cc8 | -7.56759 | -47.21283 | 2026-10-01 04:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0f736ab-5af8-301d-8abe-d734fe2cece4 | -9.08583 | -45.00272 | 2026-10-01 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 24a0d883-3c76-386f-ab77-1d6256c82bbb | -9.21246 | -45.82017 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45b67d48-9465-31d3-a131-3d18ce133198 | -11.86253 | -47.07165 | 2026-10-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98393f55-c2a3-3d51-aae6-a154b2abba0b | -8.95345 | -48.42342 | 2026-10-01 04:34:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6e690df-dade-34b9-9723-d2ab61370d8a | -11.81935 | -50.52967 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1f352908-f27f-35bb-9e72-1a0ce0a60734 | -11.26398 | -54.81933 | 2026-10-01 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e0ea3f5-8390-3892-ad5a-5ee1501aefe2 | -7.34001 | -55.60144 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d1a4431-9ae8-38a7-bc0a-7091111423e9 | -6.7317 | -55.59203 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0012832a-1cbe-3e4f-bf92-ffc1dd76301e | -11.83657 | -50.95184 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdac8195-274a-3151-834a-cdb7e9067f93 | -11.26804 | -43.52011 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b21578e0-88b4-36ca-8258-d35a774969ce | -12.90148 | -44.81667 | 2026-10-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 364d853e-7a63-364f-844b-95532f83b4a7 | -7.45493 | -47.17306 | 2026-10-01 04:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61f0ec47-2b74-353e-97e4-2d439c1b0642 | -8.79372 | -48.00141 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60c4d3aa-02df-32fd-8ed2-8300facfec3a | -11.12128 | -44.5931 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7db8a98-1b76-31ce-81b5-1de4cd9ba39a | -11.41511 | -43.40961 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1006bc6d-9e3d-329c-bcba-d6c2900bcb36 | -11.26404 | -43.52283 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b53be313-c14f-3096-94b9-dc15bbc24162 | -12.58165 | -47.16161 | 2026-10-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53892b38-4278-3dbc-9c00-11ccb02690d7 | -7.18485 | -46.30569 | 2026-10-01 04:34:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84e59118-08f7-3196-84ac-a513f74017ad | -11.42725 | -43.40652 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 174dd9ca-253b-3694-85ea-484e16882b5f | -8.19939 | -45.50531 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a7de6a7-6452-319a-a1eb-e8f065f2cdaa | -13.54737 | -49.18066 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ab1cada-e790-3b9f-896a-8eddc8e87bb1 | -7.54056 | -47.12614 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4106961b-646a-3cac-805b-6c3f03645cea | -10.85299 | -48.69682 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2061304-8c46-35d2-8fa2-315adbb82db0 | -7.72257 | -49.54685 | 2026-10-01 04:34:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4c89eae-901c-3918-ac49-ed4b32a145e5 | -7.3882 | -47.01691 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6bb99ca-6fc9-3cb3-b6e0-2a80c3563292 | -7.54706 | -55.03092 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3a957ff-272a-37af-8e96-8aafced9f894 | -11.22131 | -45.18106 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fa976d3-8f68-3c26-964d-c00a7acf58de | -11.42207 | -43.41549 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3abc3d68-0f06-3667-a2f5-f2bc3c742426 | -11.19118 | -45.16832 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 926f1b9e-d3a0-3b1d-ac8d-4d736d42f416 | -10.29803 | -44.64292 | 2026-10-01 04:34:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dbfec07-67c4-3815-aa74-019cc32896e2 | -13.38866 | -46.83261 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39ccd09c-add0-306e-b291-be59edab3221 | -8.37187 | -45.38368 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 880a6b11-1e06-3710-990e-360bd5b903eb | -7.70085 | -54.79685 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13de7379-9dfe-3341-bda0-8e5cda9166a8 | -7.69559 | -55.0627 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6ea6f5a-de52-34dc-8fb9-239e225712c9 | -6.74569 | -55.08307 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52382ed8-74a9-372f-90f2-023b2d0cbfb7 | -10.71934 | -45.30386 | 2026-10-01 04:34:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55e1e4a1-0769-3af3-8b24-b307784dea4a | -14.23133 | -44.23014 | 2026-10-01 04:34:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd399044-2b2b-3b31-bbb7-50df6befbb17 | -6.02505 | -53.36959 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00698d97-3f88-3b1f-a3cf-bebfce8509a6 | -15.60175 | -38.98305 | 2026-10-01 04:34:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7b9cffd8-573a-38b2-b275-820417fab613 | -7.03689 | -50.73344 | 2026-10-01 04:34:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67e3a575-7b48-3182-8d5f-63c267d50395 | -11.17706 | -54.1143 | 2026-10-01 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afcc1573-d019-33ad-b0ac-766ab8340ba6 | -11.41757 | -43.4197 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| faa0b3f6-3e57-3130-bec3-d53db892c209 | -8.48523 | -54.9111 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4832e93-0e4a-3cd2-b7dd-6a5c04667676 | -7.5481 | -55.02491 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1913caf7-57d2-3ec1-ae99-36cff80acc26 | -7.33375 | -54.9834 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e075147-9909-3439-a294-bdec47398190 | -12.9636 | -51.10006 | 2026-10-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3129b26c-4256-3742-a8a3-4be995d4de92 | -6.66422 | -58.87697 | 2026-10-01 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 11bc87b6-7c8c-3800-aea7-2b5fe3215ace | -13.38473 | -46.81321 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 95015cb3-18c0-3d39-b83a-463b0ab81196 | -10.54984 | -50.01033 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a5500b3-7699-325c-a5f1-0c1b5617d3c3 | -11.43284 | -43.42196 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bda3210f-0ac2-3966-bcc3-193f2381675a | -12.77535 | -54.01038 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 011e9ce4-8a87-3761-891d-6dbfda003206 | -13.36597 | -46.83388 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc980ce4-5212-3b74-91e8-cc6e55422ccb | -12.90806 | -44.82192 | 2026-10-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b4c057b-1809-3051-a29e-8aeaa9b74a57 | -6.92162 | -59.28838 | 2026-10-01 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14dffd1b-7f6e-35b1-941d-82397d6dd74f | -9.20015 | -45.81069 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa146985-b8b0-39fc-852e-e8b957184c5d | -7.54554 | -55.03971 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e552e37-d195-38fd-ace3-67603d4f9c62 | -8.84359 | -50.50948 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc278e0f-6211-3e36-81d3-fb421746afd1 | -9.20797 | -45.80463 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a416accc-dac1-3a77-a19f-fcf258d2051a | -13.34306 | -46.82641 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08199f03-68d5-311a-876a-5578ead1b818 | -6.35513 | -55.34188 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e292525-adbf-381a-baa0-99308970ca2e | -11.18549 | -45.11121 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18746c73-9c7c-35d1-9b13-e5c6ca703121 | -7.04526 | -50.73014 | 2026-10-01 04:34:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05028859-eca1-331f-9922-622cce92efb4 | -13.13931 | -48.55389 | 2026-10-01 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ace9ab7a-25cd-3cad-ae8b-f3739a771ef2 | -11.81581 | -50.52906 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f57dc72-35a6-3032-94d3-a2a1d8749cbc | -8.84429 | -49.69176 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9a4fb86-c498-3c29-b2c7-7db964c81c79 | -14.45323 | -47.76308 | 2026-10-01 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README63.md)
