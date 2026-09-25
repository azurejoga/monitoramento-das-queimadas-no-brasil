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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d6fce42-3640-3a5c-8e80-7a3596a362b8 | -14.76707 | -45.58947 | 2026-09-25 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fa7450d-254b-3a3d-b952-6374b0b7d5be | -21.05265 | -48.47366 | 2026-09-25 03:53:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 404677d0-9087-3800-b693-cb67f00f2398 | -21.04795 | -48.47243 | 2026-09-25 03:53:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e6cb5d3-4fac-3c36-9a49-2aa1980be86a | -21.38835 | -49.17853 | 2026-09-25 03:53:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 520a19c9-0569-3ac5-b60e-1e485f0d6b30 | -31.34539 | -54.06648 | 2026-09-25 03:55:00 | NOAA-21 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| cedf870f-ce1e-30fd-b8cb-a01489bb2023 | -12.2063 | -50.7316 | 2026-09-25 04:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ecfbec63-6d7e-327a-babb-9fccdb4ce455 | -9.1535 | -59.4834 | 2026-09-25 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 6a6c7034-86a9-398c-9373-7c31838fe956 | -12.206 | -50.7531 | 2026-09-25 04:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| cf7e0ba0-33c3-3649-b78f-642d0d5ec3c9 | -13.7804 | -54.0431 | 2026-09-25 04:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| aed10b95-06e8-3621-b1d1-086224e11493 | -9.1536 | -59.464 | 2026-09-25 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f2f1fdc9-96f9-3370-877b-01e0ef2ea1b0 | -1.41077 | -49.03042 | 2026-09-25 04:23:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ff52f57-1aee-3cc6-8f44-56767fe6b707 | -2.3285 | -48.54689 | 2026-09-25 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee2ceb20-ef52-3028-8cc9-abb3c9611fb1 | -1.2201 | -54.57098 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 188c5a45-72ac-3223-b507-a4c8c8588bcc | -1.14916 | -54.10404 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea819fbe-bdb8-351d-a0fb-17a0784a7509 | 2.11098 | -50.69938 | 2026-09-25 04:23:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a5d1fbd-41e5-34e2-afb0-791df6781c76 | 2.11058 | -50.7 | 2026-09-25 04:23:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f350928-c65a-3d01-bb0f-3d7eec82e51b | -0.5022 | -49.14646 | 2026-09-25 04:23:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 088b7de4-2065-33c1-9258-aebcd282c336 | -1.21502 | -54.55988 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9de07447-a61e-3f94-a905-15db937b47d1 | -1.137 | -54.09634 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 885ca4c2-128a-3397-88e9-5ddf14187076 | -2.47699 | -45.10421 | 2026-09-25 04:23:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f599935c-1dc5-32b9-9b99-a058b3eb49a1 | 1.59837 | -50.90616 | 2026-09-25 04:23:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ac143ce-c1dd-30d1-b189-237f48d36d59 | -1.216 | -54.56747 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d884263a-b60e-3f1e-b468-3e68b6d9ebe4 | -1.32961 | -47.7841 | 2026-09-25 04:23:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d467a97a-5fae-3e57-ab2b-035176811174 | -1.42475 | -49.03271 | 2026-09-25 04:23:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91d4cf1a-03ec-3461-8936-6deacbc3acaa | 2.11004 | -50.69641 | 2026-09-25 04:23:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6e26820-b97a-3352-a5ce-30134d5c4319 | -1.09822 | -49.20525 | 2026-09-25 04:23:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36343919-f1a0-39e8-b9e8-41cf9cb100d4 | -1.15093 | -54.09325 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c85e906e-5a1f-36b0-a9d6-1f3e25818824 | -1.22176 | -54.56077 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f5a8b4c-ae8a-3ca4-8431-975d2498e5d2 | 2.34587 | -50.77127 | 2026-09-25 04:23:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34f25afc-44f5-343f-a99f-ba881d5a0f19 | -1.96083 | -48.3829 | 2026-09-25 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f17ecfa4-f502-3694-b0b9-be063edfcc6b | -1.21419 | -54.56496 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d339835d-e410-3013-ab99-c57eaa5455e0 | -2.14889 | -48.4671 | 2026-09-25 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba687ec9-8500-3753-923a-1139d9571e2d | -1.21339 | -54.56985 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22780725-50a6-3041-964d-6335f521977e | 2.12769 | -50.70101 | 2026-09-25 04:23:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6dd44c0f-f286-3f20-81dc-879191b4e7b8 | -1.21683 | -54.56255 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 412d17bc-4061-31c7-9ff1-eb5165129ba8 | -1.22092 | -54.56597 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ec2eed2-35a0-3229-bb7c-8f5d5a01bb27 | -1.21774 | -54.5572 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 055dbdb3-745a-3f69-a9d3-ba984bbbe764 | -1.14442 | -54.09206 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 12242542-cac0-3d2d-85d2-ddeac9599eda | 1.59339 | -50.91068 | 2026-09-25 04:23:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7d10a9f-62fd-35cf-ab02-237b784036a0 | -0.84654 | -48.644 | 2026-09-25 04:23:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da8525dc-a69d-313c-b546-9a555507c0e1 | -0.93508 | -47.5541 | 2026-09-25 04:23:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 96367be6-6283-3e6d-9fd5-629528843501 | -1.14263 | -54.10294 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 292752d1-cac0-3302-82ec-f662da834c83 | -0.50476 | -49.1609 | 2026-09-25 04:23:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01e3ebb0-3bb5-380b-842d-2d97e70c94fb | 2.12824 | -50.70461 | 2026-09-25 04:23:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c7b9659d-3a2c-3b9d-b117-80f4a5ccb5aa | -0.50531 | -49.1574 | 2026-09-25 04:23:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b0c73cee-c195-3b58-92b8-03ce384db19c | -0.50555 | -49.1558 | 2026-09-25 04:23:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edf4faf4-e30a-3c78-923a-1599b0894eb2 | 2.11042 | -50.69579 | 2026-09-25 04:23:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b3df79c-6f87-320b-99aa-872a6859dca8 | 2.35144 | -50.77039 | 2026-09-25 04:23:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c47a908-6e3e-3d83-8153-b4b03ab19faa | -1.69207 | -48.21262 | 2026-09-25 04:23:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8ce6a16-6f71-3f06-ab76-30a33662396f | -1.13791 | -54.09082 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3393457-1269-34fb-bc97-e531441597c6 | -0.50157 | -49.14993 | 2026-09-25 04:23:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96498b41-b016-37c5-af64-44d8776da736 | -1.14352 | -54.09754 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f3163026-9f5a-3eb5-b245-b48ffbe4cb03 | -1.15004 | -54.09868 | 2026-09-25 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 13a9acf7-2781-35b4-baf9-fabdefe979d4 | -2.3104 | -46.99509 | 2026-09-25 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4be3e4c-11f8-3072-a765-254a2d022be5 | -1.96152 | -48.37863 | 2026-09-25 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b66f1cd-b336-3a16-a0e7-05bcce6af008 | -10.95384 | -43.87914 | 2026-09-25 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b48d7a3-80d9-3fe9-871c-542f3df2a032 | -3.23266 | -46.9286 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ceb0895-b172-3737-85d9-d46333fd7a02 | -10.40906 | -46.27467 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0765955-4449-3d80-8d47-06fcf3509104 | -10.9261 | -43.86023 | 2026-09-25 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d35ab0dc-2c9b-3a23-bb04-3f887166f2eb | -3.21115 | -53.41184 | 2026-09-25 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 150c987a-3a15-3484-8e97-8a0bd0c3e21f | -5.82875 | -35.48093 | 2026-09-25 04:25:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1bb99403-1a09-3294-8b31-0ad53319ce9a | -4.61339 | -42.79979 | 2026-09-25 04:25:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 036b48dc-6569-3e43-a8b0-6ea8337c1b75 | -3.94674 | -42.99296 | 2026-09-25 04:25:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b24c69c3-aa38-3b5b-9623-ad0ecc277155 | -6.92392 | -41.69545 | 2026-09-25 04:25:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8bf31d11-bc96-309c-8e74-e9ba4e314f6f | -3.78446 | -49.58635 | 2026-09-25 04:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 27f3af99-cb87-309a-8e6c-3c48538a67c6 | -8.33105 | -44.14348 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4449480c-0fc2-38f3-99cf-e046e334ea54 | -3.79494 | -52.37347 | 2026-09-25 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b855bf45-bca1-3527-b1e9-4a7110e71f57 | -3.9434 | -42.99244 | 2026-09-25 04:25:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d69b4772-5b36-3a6f-8d42-224146a7a545 | -10.94662 | -43.88158 | 2026-09-25 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92d869df-22a7-3f76-a2f1-2a4afbdae00a | -7.12167 | -41.725 | 2026-09-25 04:25:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f6b86ee9-1326-3051-95c5-daa6829ce6ae | -3.52056 | -44.00323 | 2026-09-25 04:25:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 533efa59-d68f-3a6b-95eb-9fbd92304f2b | -9.28568 | -45.90808 | 2026-09-25 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bf980b3-68ea-3861-abc5-3df09494ebac | -8.2478 | -54.69413 | 2026-09-25 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01f98bc5-32d7-398d-9700-19700e2bd746 | -5.45591 | -45.87344 | 2026-09-25 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2a9c39d-73c4-38dd-bc3c-ae84ac95ff3a | -7.38913 | -44.77065 | 2026-09-25 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da0e138f-11c2-3754-9dd6-a596f245e177 | -10.41538 | -46.27973 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ca8c553-16ea-31bc-a87a-f0b351226949 | -7.7803 | -44.77064 | 2026-09-25 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 437d8ff4-e270-3dd6-8efd-4f422f30ee2e | -3.01296 | -50.2989 | 2026-09-25 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ed5f7c8-1f18-3988-90a1-296ee4413c7b | -3.23145 | -46.94156 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 12039b1f-b134-32a3-abc9-e8d75b499fe9 | -3.20508 | -53.41079 | 2026-09-25 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5952c8a6-9abf-3217-ad83-ecbc88592ad6 | -10.41318 | -46.27139 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c3c0784-7b14-3a19-aabd-ee844a961a39 | -7.38853 | -44.77431 | 2026-09-25 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 438cfdf4-5abc-35c3-9148-0fde1f107965 | -9.02359 | -49.6368 | 2026-09-25 04:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eedbcdc4-8f9c-34f0-8342-d3e72352bde2 | -6.89144 | -43.74353 | 2026-09-25 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf9193b6-b56a-3f66-ac63-07c9c7e79c5d | -4.28593 | -48.61409 | 2026-09-25 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af7231fa-a36c-34f1-bf82-7caf553cb355 | -3.20663 | -53.40201 | 2026-09-25 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a02c663-1d74-3b8d-8711-319318b8530c | -3.23224 | -46.93659 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 93a32d68-86c7-3353-9e5e-cafa0ba2af33 | -9.62539 | -43.9599 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| aef53f30-d3cf-3a37-ab4d-da143e8be3bd | -7.91357 | -45.24289 | 2026-09-25 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 696a1c01-f9b7-3abf-b9c8-a07f758d9441 | -10.41254 | -46.27527 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c81f771-239e-3a3c-8711-63dbbd7d5f6e | -7.00882 | -42.08741 | 2026-09-25 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9ecbd2f1-2989-3453-b515-344a25248d3f | -3.05733 | -46.92627 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff85e939-3874-332a-aeec-a74c0a913b7e | -9.03471 | -45.02799 | 2026-09-25 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0963ac3-aad7-37ca-8321-cba4fe66d716 | -5.04466 | -45.53596 | 2026-09-25 04:25:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52695e5c-e680-36c9-b496-de190a17bcda | -10.40623 | -46.27017 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2a2cb90-bea6-33d2-a29b-4179fe5fed89 | -3.03277 | -50.39513 | 2026-09-25 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84951585-15ab-3f50-9460-e67570050b2f | -9.62816 | -43.96394 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 759caf4a-94c9-3fb7-90db-83107e570eab | -6.82298 | -43.56042 | 2026-09-25 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13ac93c0-afdb-38b4-a2c2-23c417834d22 | -3.97885 | -48.43257 | 2026-09-25 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 514bf39f-2227-35c1-a1c8-28b9d12f1637 | -3.17989 | -48.0196 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README15.md)
