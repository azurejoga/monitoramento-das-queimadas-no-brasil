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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30ba0fde-2859-3886-a4f3-38045a342ed2 | -13.13748 | -46.90331 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92d9204e-6435-3e24-b910-c2c7eecfc07b | -13.03312 | -45.20201 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6eed114-2b66-39eb-881d-6fbb1dd70c5c | -12.94892 | -46.27487 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34abd2ad-3fa4-3abb-bb6d-fd3b6b542c78 | -7.85786 | -47.00909 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12da0060-317d-3ffe-80ce-690f99362970 | -13.14325 | -46.89783 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 177fcfc5-9f8f-3966-a2e7-dc4afd2e0b43 | -12.99953 | -45.22307 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ae213ad-8934-3f1b-adb0-5b1230432474 | -12.9568 | -46.28176 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12ce1831-2aec-3659-8d4d-35dd6d51b10b | -13.03411 | -45.20508 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c74cb44-4d83-3017-8cf5-5ff3ec38664d | -11.31596 | -44.94856 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97c7378b-940b-3da0-8856-c20b56ecb992 | -14.7334 | -46.65523 | 2025-08-22 03:57:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efd94b0d-b357-39b6-ae7e-fb10e42c977e | -14.76143 | -45.22717 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81221686-2467-3f36-802f-fbf5fb54cb12 | -12.95743 | -46.26125 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6eb231ef-9661-3ea8-8e45-3e94b76cd778 | -14.82801 | -47.92927 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42038edd-b7a6-311e-80e8-2f55ef639a94 | -14.87698 | -48.05301 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b466dc4e-2843-315f-a71c-b865cce11b82 | -10.29008 | -46.76105 | 2025-08-22 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d3d62d6-8435-3eac-9b8e-29702e6098b4 | -12.95382 | -46.25586 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a57f4cb-df72-37c3-b998-2086bf302909 | -9.14068 | -46.38769 | 2025-08-22 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58d08358-5889-32b7-a442-6eba7acd4b10 | -12.94784 | -46.28907 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 51bff44b-089e-3531-ab7a-3d467c0e999d | -7.85599 | -46.98972 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1302764a-b977-3940-90b9-516c8997af7c | -12.95431 | -46.27863 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4afc87b4-743b-32e7-8e91-0f878a021b88 | -11.30693 | -44.95086 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd65a429-37b6-3778-a76c-97973bca47e0 | -11.30488 | -44.96251 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54b2ec0c-3d27-3330-a239-128483dd1cbc | -14.91053 | -49.45186 | 2025-08-22 03:57:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e656056e-1871-390b-8b5e-f1a8065f2a46 | -14.76693 | -45.40334 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cdc27cd4-ebca-3068-a173-8a5a61a5c526 | -12.94989 | -39.55479 | 2025-08-22 03:57:00 | NPP-375D | ELÍSIO MEDRADO | BAHIA | Brasil | 2910305 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b4d1536c-81ca-38ff-bd25-76ce26d7882b | -14.76828 | -45.39596 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a34681ab-2c24-3371-99f5-12c94aa7ad42 | -13.49143 | -47.04523 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6d080aa-bbea-3577-97d4-379bb1e86b06 | -7.85545 | -46.99281 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4dd7990-81ca-3c07-b4ea-16eb57c45003 | -14.91579 | -49.45299 | 2025-08-22 03:57:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3be22cd-6063-3350-9635-3a230f0d1708 | -8.67771 | -47.98648 | 2025-08-22 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b9ff0ef-e85e-3725-a452-687e27810a89 | -8.12428 | -47.1516 | 2025-08-22 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70fc821e-842b-3b04-a1dd-972c05bd3d60 | -14.87573 | -47.93904 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baf9f100-0843-3c14-9015-ad485511152f | -14.8982 | -48.05644 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9aa0430a-c9c1-3213-8cf4-811b76e585c8 | -14.87898 | -48.05243 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9e063fd-d25f-3e40-821a-65c6dc8d510f | -11.12909 | -44.73104 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aba8f31e-4949-3dba-8d92-58a6bcf805ea | -8.51025 | -48.82538 | 2025-08-22 03:57:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d243909-fd6c-39be-a6f3-e737968720f7 | -12.95001 | -46.27703 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 654bc807-004c-35b2-8258-a172471f0509 | -12.9628 | -46.27415 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9f14f7b-4c37-3a9f-88ed-e97138a25d00 | -13.02687 | -45.18908 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87cf9754-1cd4-3a40-aa21-f7c6e8b0cefb | -15.8946 | -43.4585 | 2025-08-22 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 94.3 |
| f60e7516-64a2-35fa-a4f6-d479ab386af3 | -13.73891 | -42.6831 | 2025-08-22 03:57:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c4415a15-a863-3f4e-b3ae-f2420e7d43a4 | -14.8269 | -47.93496 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35e856c6-bfac-38cb-b2e0-035a7db85bc5 | -14.75814 | -45.40548 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b812ac9e-811c-3947-8722-0c02699efdd4 | -15.13772 | -48.10883 | 2025-08-22 03:57:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e6884ad-ed78-385f-9684-7c5b17e465b6 | -12.95604 | -46.28582 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2852d1bf-1d09-38d6-a47b-d7c1d48b9b76 | -10.72751 | -48.23143 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dfac626-f7dd-3dfc-84bc-5535c0efd224 | -12.67846 | -44.96243 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34c6126c-e3ea-311a-a851-f93f6801a8e4 | -13.03378 | -45.19822 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 172553e3-2ae9-3fd9-a88f-15401fea0f54 | -13.83166 | -44.46409 | 2025-08-22 03:57:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7870ee88-85be-3bcd-9dcb-93f1fe3ee932 | -12.96027 | -46.27097 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3dc8f7c0-3da7-3db2-8a93-81ee5a3668b4 | -13.64919 | -45.70623 | 2025-08-22 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 397c147c-fffa-3f12-9289-47fa2c1cd4f5 | -12.94744 | -46.28276 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 382108c5-229e-334d-aa10-cbdf78a9761b | -10.1883 | -47.5635 | 2025-08-22 03:57:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7791a1c0-4363-3af0-9c22-73924ca90a98 | -13.03444 | -45.19445 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad224b2a-98ad-3d76-a1af-14dc7fb751c7 | -8.77389 | -45.45244 | 2025-08-22 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54efff8e-8fbb-3b64-9e26-f4b66f9ba65d | -13.02276 | -45.18829 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 501bbc5c-b560-3d56-b337-8aebf2bc6cd5 | -11.44187 | -47.30984 | 2025-08-22 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00098039-f4f4-3e9a-ab65-80a984eeba28 | -11.28671 | -44.94334 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 248aa89a-d75c-353d-8f7e-c19da5d341d6 | -14.97623 | -47.13708 | 2025-08-22 03:57:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a8c636d-6a95-36ce-a3de-6534ab6cd904 | -12.9975 | -45.23449 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7b56a18d-5e55-3e81-b11d-7d8c5e4389c8 | -14.45986 | -48.3602 | 2025-08-22 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76df469a-2546-33cf-9519-98cdb5411dcb | -14.76154 | -45.43287 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9287b708-c8b9-3505-ac71-2af038c0e0c3 | -13.03856 | -45.19527 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd2a17ca-3474-3b3b-aadb-515a1a44a1db | -12.42675 | -48.70604 | 2025-08-22 03:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fda3b16-be3d-309b-b2a4-dcf00f3ecf24 | -13.38205 | -47.49161 | 2025-08-22 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce6e537b-51b2-3266-8468-943642b83ed8 | -11.31528 | -44.95244 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33158777-92bb-3a40-9b7b-abeb08ce0adb | -9.7198 | -45.63561 | 2025-08-22 03:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dd4714a-cfb2-3dee-a7b2-c8cd8202debe | -12.94929 | -46.281 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7733e1d7-cfac-3c2c-a0b3-417d08533ebe | -12.95172 | -46.28439 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f81ae1de-5d46-327f-baac-2e9b9fb988f8 | -14.83381 | -47.92495 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4823116b-f75d-38f0-8147-01afd87853f7 | -12.9272 | -46.17585 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8bd2184b-6c8a-3a34-b495-87a257ad8467 | -10.71235 | -48.22527 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb4556d6-6b5c-313f-ad9d-9e7d7fe6b246 | -13.38737 | -46.24891 | 2025-08-22 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7adaa1ad-f387-3ca0-9c11-fb3adbe3ae00 | -12.99682 | -45.2383 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8b2044b0-e6a7-337b-83d0-0a410d565a89 | -10.73681 | -48.23996 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a248abd2-7cc1-3316-a4ff-ea51f75f46b7 | -12.49263 | -53.81146 | 2025-08-22 03:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e751e0e-775f-32b5-bcb3-3d678b9c8df3 | -13.02621 | -45.19286 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad69bf6f-da60-3deb-8056-395aed53e4c9 | -12.94668 | -46.28679 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2c95b5ed-794d-32c4-b077-eb957ca0a42d | -11.81665 | -44.25695 | 2025-08-22 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ca00cad9-d889-360a-b199-4c99ce259762 | -13.36685 | -46.2645 | 2025-08-22 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 406cd37e-1462-316f-9725-56698f1b526f | -13.32345 | -43.5718 | 2025-08-22 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6db688bc-bd06-368c-91dd-e5210674a722 | -13.35968 | -46.25395 | 2025-08-22 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d50d307-d3bf-3f28-bed6-30ce5a543be3 | -12.00697 | -44.6642 | 2025-08-22 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 209454c5-ed20-3eb2-aac3-3a382150095c | -13.37685 | -47.49468 | 2025-08-22 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4a5946d-0b38-3ec8-be75-8075df373a2e | -8.1197 | -47.14767 | 2025-08-22 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae6016eb-8c90-3f99-bbce-4a581b12e4c7 | -13.46186 | -47.0496 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04154ace-9b08-3f19-8f93-d80214bf5211 | -12.00164 | -44.67074 | 2025-08-22 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a049453-927a-3fda-869a-e7244944526e | -13.37357 | -46.25253 | 2025-08-22 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0d706c1-5f86-3e92-b70d-f64a91f6fe7f | -7.86072 | -47.00908 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0468d93-d924-31f8-8dcf-9694dd72e74f | -8.14172 | -45.55321 | 2025-08-22 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfd8a469-0578-352d-bb3f-aedf989ea146 | -14.30638 | -47.06802 | 2025-08-22 03:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37edf467-de4a-38d3-a8dd-3a7ff2b3fea8 | -13.02554 | -45.19663 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a55022f-41ad-3edb-9a6d-51c64a1cc5de | -13.02833 | -45.205 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47ba25e3-aa07-3864-b18a-db2d16483308 | -14.83169 | -47.93587 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be35ffbe-a8cf-30cb-a565-1bc690eaa5cd | -11.81757 | -44.25179 | 2025-08-22 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3113efe1-fadf-38fb-8592-2cd82d35cfed | -13.03618 | -45.19378 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c70b258b-3e01-30e2-8926-c506d88cc7c2 | -12.95097 | -46.28838 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03c02422-4b12-3bf3-b519-d73488985398 | -7.85842 | -46.99286 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7d8850e-c172-3ad3-bebe-1750ea50c7a8 | -13.38752 | -46.25074 | 2025-08-22 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c37309d-1d02-3f67-af7d-e12c39983b06 | -12.92488 | -46.18859 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README17.md)
