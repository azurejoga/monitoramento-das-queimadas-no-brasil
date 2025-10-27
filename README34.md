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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce449e75-a71f-39bc-a825-2d9b5cc3ccec | -4.26365 | -50.51208 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d71f6402-d6aa-3e34-87a1-4f276b9ff928 | -8.32839 | -46.16882 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99fd639e-1219-36fc-93da-05c8385c8080 | -7.76403 | -45.39795 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02dede7b-54e0-3ca4-aa87-f2173510d712 | -3.15145 | -50.33146 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1daf5a2d-ea4d-34b3-ba06-18290795f064 | -9.99062 | -47.18956 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3218d2fd-84b9-30a5-9322-f90bf493d736 | -3.1441 | -50.45079 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a56095f6-9455-3eba-8138-0ec7b72599ed | -5.26934 | -50.97805 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f299453-fb8f-3677-8083-d9aab3e15d74 | -5.60505 | -47.09476 | 2025-10-27 04:32:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85f0d7b2-cabc-336f-8e43-12e45f44783c | -8.5634 | -47.38745 | 2025-10-27 04:32:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4413166-1270-3791-b426-05922cf56611 | -9.13256 | -45.85574 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5cb805a2-641f-3bb5-bbaf-3ffbb73db7a0 | -9.27716 | -46.40947 | 2025-10-27 04:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27db9c73-5fd6-35c3-a22a-ed08064b1f8f | -8.27684 | -46.88218 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d761318-9f90-32b7-b779-be29c63ddc26 | -4.44853 | -43.42816 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e88f5c27-4e68-32f2-ad3f-c83c621d0d37 | -3.15246 | -50.33036 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 76f89e5e-201e-3893-a69b-cef86f2d1b23 | -6.43836 | -42.3515 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f9d0a91d-58be-331b-b147-c90c2e9f87c2 | -5.61596 | -42.67082 | 2025-10-27 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 646af18a-9683-346f-8a9e-93d7a733af65 | -8.09451 | -44.39611 | 2025-10-27 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43f8f3df-dcf1-339a-ae86-c77feca16591 | -7.58929 | -43.57726 | 2025-10-27 04:32:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb63c474-e87e-3eca-af8d-911793203701 | -6.89061 | -43.57151 | 2025-10-27 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3af435e2-a136-3cf4-9251-5279d6bb977e | -8.09351 | -46.94942 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45844791-4cf5-35ab-9233-063b9f3541f6 | -1.68826 | -55.67036 | 2025-10-27 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3fec472-f9a3-36fa-9a87-6a73136e3d6e | -7.8616 | -46.4239 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9af9eef-54a4-3c25-85ce-82d176c5e082 | -5.71755 | -49.31189 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b326ddcd-5893-34e7-b050-86ad8ce8a057 | -4.26685 | -40.68488 | 2025-10-27 04:32:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 55836344-7177-317a-b837-19a209aac821 | -7.78102 | -45.38047 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94f8bf51-e580-391b-8d35-3d611d971103 | -10.01168 | -47.11877 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e64fcb04-ce8b-33ad-8707-b6dcde5dcefa | -5.64319 | -47.63327 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 444feb51-56ad-33a6-86a2-82354a849ee6 | -7.30934 | -42.47672 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 16c89f29-ad79-3138-ba08-6b212d01e854 | -5.07541 | -44.7334 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5815e9ce-fa54-3f0f-b53f-f1a2427d2757 | -4.16035 | -51.08194 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0acec96-311c-3459-8ec0-7ea3905113a7 | -4.46419 | -43.42591 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a337b54b-251f-3cb3-a7b2-c60e61647207 | -9.02775 | -47.46347 | 2025-10-27 04:32:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98eaf5d1-bd13-337e-a704-e2f5bde88214 | -7.83354 | -46.47172 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 8c715a29-9d3a-3047-9e7d-127fb432f19c | -7.06637 | -46.75395 | 2025-10-27 04:32:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 00715380-7cfe-3104-b8f3-28b152875ba8 | -7.15219 | -47.78095 | 2025-10-27 04:32:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 619b320b-2f4f-3eb9-9142-99154ff721ab | -3.10887 | -50.17908 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bed579d2-2d37-3b91-9393-e850899e8bb1 | -3.39229 | -50.40051 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe8ea5aa-2bf9-3f48-9483-05e34af488c1 | -6.67985 | -41.51069 | 2025-10-27 04:32:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 669c76bc-eb5e-3741-96a8-25a11903072f | -3.42669 | -52.43259 | 2025-10-27 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 438213df-5789-32ba-9981-312ec9951cfa | -7.85684 | -45.38259 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbbd8e9f-ae7f-3160-9620-c48879a128f4 | -4.31467 | -48.22742 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc4d0686-008f-354d-9b52-60492295cea9 | -6.15387 | -43.12911 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 35074a1b-e6c3-37b0-ae07-724d8a8f69f8 | -3.23278 | -48.76204 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a9b6261-44b5-3289-951a-f6111a4281ef | -9.86278 | -44.88464 | 2025-10-27 04:32:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3b6b403-ae6b-333f-aa25-cdc6c9c90a47 | -7.18364 | -46.25035 | 2025-10-27 04:32:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8161d6c3-d340-3d1b-94df-00deefee54f0 | -4.16978 | -46.70028 | 2025-10-27 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6742a849-55ee-36a2-a74e-aa1a8b73a188 | -6.89782 | -46.14388 | 2025-10-27 04:32:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 322e1f7c-2587-3655-896b-f9c0a9a4710c | -7.36157 | -50.42921 | 2025-10-27 04:32:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e27a2b7-56fe-302b-82fe-3a489f9b263d | -5.96897 | -42.77316 | 2025-10-27 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e724e67e-7b2c-3c76-831e-d949124ddd76 | -9.63265 | -46.86395 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1dcc961-98fc-34f1-a803-aaec0fb0b133 | -4.89347 | -43.22499 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32fcd619-7267-353a-ae9f-249b65d3d482 | -5.77864 | -42.97874 | 2025-10-27 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 105c51ad-1f8f-32bc-9b24-e5d10a0ae83e | -4.22419 | -48.36784 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4018e9f-1d3e-3e56-acf3-f83f091dabb6 | -8.96128 | -47.18884 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b0f4cffa-95f5-3500-a89d-3609bcc1e229 | -4.26138 | -50.50316 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5cf2ff9-3c84-313b-b43b-ca2cb82a192c | -9.21365 | -44.54638 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60fe0193-37ee-3194-a525-d15c28468cf0 | -4.0042 | -48.31882 | 2025-10-27 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d20ad81f-8c44-38dc-a0c0-f50dfd76082c | -4.44478 | -43.42759 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5f4cf79-46b8-377d-875d-54e6fe5a70ff | -4.95541 | -44.87685 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68a80a87-047d-3e46-af00-c5bb565fe46f | -5.36065 | -45.04692 | 2025-10-27 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac994eec-9db4-31ad-98a9-bfa93fdaaaa4 | -3.3712 | -50.17603 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 90896c1b-2518-3cf5-9a5d-28e48992da39 | -5.03265 | -44.68216 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f14be133-fe76-3f2f-98c1-53878e229ea7 | -9.99164 | -47.16015 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08c71227-b70b-311b-a959-c6cb0c8be516 | -4.44394 | -43.42534 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31bbd7ff-16ac-3fc4-a5ac-37411173743a | -7.04839 | -47.22223 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e43be63-9990-3487-abad-a8f0b607803a | -4.81329 | -38.65142 | 2025-10-27 04:32:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9bb0cda5-1de6-3184-8968-278a4986d3d6 | -5.63714 | -47.6288 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c0b6429-536e-36d7-bf1c-0dfe89e4ccde | -8.321 | -46.17135 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9a7a656-90dd-3860-9536-f586ffabbda0 | -3.86523 | -50.88889 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f9d71642-ccd4-38cd-aea2-ecf324bc6591 | -6.44303 | -42.34841 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1e397d37-896b-323d-94a7-1ea57574eb8e | -4.61151 | -49.47965 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c0e3975-fb7b-3fde-94dc-76ff1a1bb501 | -6.89704 | -45.16847 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68a94f20-5136-396b-94f8-07cca48ab2d8 | -8.69715 | -50.81527 | 2025-10-27 04:32:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e0dd2564-7b99-384c-bfee-2bfadbaa054f | -9.57592 | -46.89625 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4a6579b-303f-3989-aeee-e9fef1d035ec | -6.44594 | -42.34877 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1e2457cc-bc5f-3ad2-a434-cfe6857fe594 | -7.88424 | -47.24896 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b3cea9a-d52a-3daf-b08b-0751ab39eac4 | -5.72152 | -49.30877 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0e020ff-dd6f-3065-a7e9-08059472718d | -4.47677 | -43.41865 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 3e6c6222-992c-3fd0-95e8-b201e5df2147 | -7.395 | -45.12951 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b138aaea-d430-3d87-a8c4-75d7ff8fd8d2 | -9.62293 | -45.47885 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c35ea5e6-1613-330d-8bd5-7267344f43eb | -9.98944 | -47.17463 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5bbb1a3-1bf4-322d-9671-17319838d5fc | -4.87319 | -48.65495 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fed0440d-70ba-3d0c-aad8-baaf052c3f4d | -4.38707 | -43.31917 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01bf3b41-557b-35f9-a0f2-df9e5a8fa641 | -8.65413 | -44.76673 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c81884c8-f361-3dc2-b4b2-786e5ad9c85f | -3.06251 | -49.37343 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| daab86a6-8e20-30f0-a6b5-c214bd36e267 | -5.60679 | -51.86568 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a3cc185-73b1-36b2-91c0-14ff69cf8aac | -5.77496 | -51.85474 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7984faee-1ff4-3e5a-9717-d23bd768c506 | -9.21922 | -45.61378 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acd837ed-c939-3d06-a953-491c2815cd70 | -9.04084 | -47.62068 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cbe08e46-dd1d-392b-a0b3-7f0f82177842 | -7.85275 | -46.50428 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c79b2c9-666f-3fbe-9c18-5807f2cec21c | -4.22013 | -48.35238 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d85a8e37-8928-3289-8e0b-5c1e939e2167 | -6.44769 | -42.34541 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dde01c24-430b-3ec1-9244-55a0b093f0af | -4.42756 | -45.98095 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08089524-8ba9-3d7d-9f48-c55bb88444f6 | -7.77575 | -45.39169 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d4b832ce-49af-3f19-be8f-cd09a5f810eb | -6.49502 | -44.44006 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ed48ec1-4c8e-3450-8494-75d443231b34 | -5.63546 | -47.61797 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12dacc3f-4194-3adc-a5c1-f5a2f32601c4 | -3.29108 | -50.19311 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9892f5d-ae72-3b52-ae38-3743eaa498dd | -8.35803 | -46.15824 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62c22709-dc1e-3e35-8b97-26cea4450685 | -7.85775 | -46.47166 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 43913904-4d3f-39c2-a7ef-37793098eff8 | -5.08686 | -47.14777 | 2025-10-27 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README35.md)
