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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 216611ab-6652-3a03-9c4b-c1962af63aa5 | -10.9126 | -53.96042 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5808ac59-4d5c-38bc-8696-0381c51ca453 | -13.20693 | -51.71986 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44ad7fc0-0b5e-3a25-b9f2-b30233439129 | -11.76054 | -50.8218 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 59b47ac5-f8f7-3803-ac9f-a68225a65bc9 | -15.59841 | -48.32759 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36f5bba3-999a-3eff-a417-5b6ea6a7ab87 | -15.43776 | -48.44755 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b196b90e-0f54-31ce-a641-c68a962406a0 | -10.59628 | -54.00394 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe882af5-94ce-3b7f-be28-e3299c1f7290 | -10.86725 | -57.17088 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bf9b987-c283-3a61-a22c-fdf750209319 | -11.50922 | -51.51168 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3409d94-1b96-34e8-a561-5325f46ce6de | -15.44378 | -48.43271 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 16078a50-4178-3716-ab30-42183b701955 | -11.88787 | -49.00127 | 2026-09-22 04:49:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba389f36-081d-36ee-ab58-6e57f97f7220 | -11.95097 | -46.51963 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dddb1deb-9d90-3d3e-b586-fd1815bce32d | -12.14291 | -47.3847 | 2026-09-22 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ba050939-319f-3b11-99a7-1bebbbfbd4d5 | -11.04002 | -54.14908 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7af87e77-0522-346d-aabe-89dd40a1f299 | -11.04403 | -54.14592 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6df6e645-4203-3fb8-81fd-56c83060abd9 | -10.59769 | -53.97363 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82a26071-05aa-39c9-a0a2-708f585518ca | -10.59689 | -54.0002 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1f3725c-f2fc-3542-9a91-2e2446d016ec | -12.14094 | -47.39898 | 2026-09-22 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a598cd1-5d7c-379d-a1ba-5b313af7012b | -11.32281 | -54.05393 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5d158ec-f6bc-3c14-ae60-cfdb19839e03 | -10.58849 | -53.98735 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 178d032a-d9fc-3fae-9de6-c3a0cc94d581 | -15.44096 | -48.45372 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 46d8344a-024f-3e9a-8687-00d8711fb08d | -12.84318 | -44.33878 | 2026-09-22 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7730d1f1-074e-31d7-ac5f-c15ab0bf07dd | -11.49924 | -51.51009 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff9afab1-226f-3eb6-b227-f5be64cae4fd | -12.35089 | -50.22135 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6aab10c8-ba17-30aa-bc77-6eb8c13ec840 | -9.28023 | -60.61814 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76392b85-8a1c-3f00-8e43-0c7406dc8860 | -15.98605 | -43.27995 | 2026-09-22 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fc852999-b4f9-375e-a4a7-b9c72e1ab100 | -14.58608 | -52.17012 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd0463d4-dbb4-3406-9124-78b3c316c5b0 | -12.5651 | -45.96213 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 5c00e40c-086c-37eb-8483-80891b29c905 | -13.28335 | -51.77568 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a24d3b6-ca26-3eb6-a698-ee1fc67a7694 | -12.02646 | -47.81824 | 2026-09-22 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b8f56ab-665a-3c30-8d71-f341ce55f0eb | -12.66962 | -50.95612 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f474569-6dd8-308c-8615-165bcd6d5b1c | -11.88344 | -46.85615 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f2c0a09-7d8d-3689-a276-67e4672068f7 | -12.76286 | -52.83537 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f93aea73-09e6-39fd-8b5c-dfd7ffe80995 | -12.67585 | -50.9609 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efe7282a-fc7d-3ec8-b2d9-4b9aed296888 | -9.29838 | -60.53198 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64059362-3c16-3660-85ba-cadb77e080db | -10.91559 | -53.94195 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6107be0c-dfdb-364b-b87e-1a144e672b84 | -10.52855 | -54.48735 | 2026-09-22 04:49:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86453ce0-7373-35ca-8330-a7f0b5ae1a5c | -14.67566 | -45.67614 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2767a91e-b30c-35ad-ac34-23f6c6e94f7e | -15.75555 | -43.30441 | 2026-09-22 04:49:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2394f2a3-c36d-3537-8780-c9667c34ea86 | -14.92148 | -49.89226 | 2026-09-22 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d47fe4e-b835-3392-a645-fcdc56ea15c4 | -12.84782 | -44.34239 | 2026-09-22 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2410c914-9ea7-34cb-92b4-03b6de0f396f | -13.51193 | -51.52639 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 525384c2-cd0d-3f74-ba01-280d379f8263 | -14.11865 | -49.86799 | 2026-09-22 04:49:00 | NOAA-21 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0adcb0fd-60aa-3b46-b69d-a3f2acf744b6 | -17.86896 | -44.40821 | 2026-09-22 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b5d6c59-84f9-319a-8977-836b939bc377 | -12.3967 | -47.04858 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a36582f7-b826-38a5-9a41-ad6d1f69754c | -11.01557 | -54.14883 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48286bbc-6cf5-3892-ab36-a7ad19faf1fe | -12.29517 | -50.71677 | 2026-09-22 04:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a519844-d133-3ce7-a911-416aeb24d99e | -11.41788 | -47.3481 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 990b37c3-dacd-3a60-89ba-fdb9641e4510 | -12.5657 | -45.95763 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48f5e872-6e75-3369-a0e4-2b926fc4c1c7 | -11.44342 | -47.34058 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 51f2afe2-14d0-3cd6-acc3-c02be50c99e1 | -15.44277 | -48.4701 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa3800dd-4d03-3af1-845f-8590608a00e0 | -15.95942 | -42.95927 | 2026-09-22 04:49:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6624d618-6bf4-32df-a974-4bcb43de4286 | -10.60369 | -54.00136 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 967b76ef-6087-367b-af70-21083ff805a0 | -12.94128 | -50.91763 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 446af979-62ec-3ffc-8544-f04c993e44e6 | -9.40706 | -65.92265 | 2026-09-22 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4e3acaa0-8544-3fec-83df-8dfe4c9d0d9d | -13.40021 | -49.48091 | 2026-09-22 04:49:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9ed9c83-9f69-3fab-b26e-6d015f853cc8 | -14.91671 | -49.89987 | 2026-09-22 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93b3de9a-96a5-37ff-a8bf-b19a3a85a2be | -12.43654 | -47.08486 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2a1031e-de1f-3a12-931f-81512f58966d | -11.85061 | -46.81616 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4651f7e7-bc6f-3065-9bfc-aa64977546d1 | -11.35039 | -51.39539 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f576a1c-f2b1-389c-ac87-e7093b825f2c | -13.30561 | -51.7866 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1c480c0-140c-31eb-9cd8-2c9382bc0697 | -12.0115 | -51.4734 | 2026-09-22 04:49:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cdb42f8-48d8-38c7-bd69-0d76c36526d0 | -9.28298 | -60.61506 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5de1016-71fe-3fae-8dfd-67fc40cfb5ff | -11.70587 | -51.00082 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1c37a0c5-6370-3c9d-8de2-97f5394e4be0 | -11.32062 | -54.04596 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e08b965d-04f7-31cf-b073-16665883fed3 | -12.199 | -47.03916 | 2026-09-22 04:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34b3ad27-2b35-3b20-b845-1a04dc053459 | -11.03321 | -54.14794 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc00c8dc-8ef5-37a0-b5a4-f2e796460f75 | -11.04595 | -54.15811 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cc8eda5-c4dc-3a80-bd6c-e96580a6ccb1 | -12.3995 | -46.522 | 2026-09-22 04:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3c566006-8955-359e-88c4-425378f72aca | -11.33367 | -51.37087 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aed6c442-22d8-38bb-91f4-9494a5da1a07 | -11.93016 | -46.51296 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f32f0c8-bc64-3a22-b3d5-69f95abbd417 | -11.25883 | -54.14284 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b65af1d-c439-31d3-974d-c11f954c20b4 | -12.88299 | -50.93533 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a695bfa0-7ed9-3c88-83ce-359879866795 | -16.80207 | -50.5625 | 2026-09-22 04:49:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 019ca776-a3f3-32ca-9518-0ce879be1d68 | -13.30063 | -51.79688 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26535c03-4b65-39b3-8f88-cc20c9116856 | -11.88297 | -49.00943 | 2026-09-22 04:49:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a04b8f2-f79a-3699-830f-1a18dc923576 | -10.90536 | -54.06975 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c77c2f32-5519-3e8d-adad-621ae7fb7d59 | -9.16404 | -61.19363 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 063dbc75-e12c-31ee-af69-2811a73b8f3b | -11.81165 | -48.82969 | 2026-09-22 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edbebe96-86e0-3056-a8a3-9d344b8b806c | -13.33842 | -51.28192 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e568057-2ce7-3c07-a97e-88a679e21158 | -11.32585 | -51.35505 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29601bec-30c6-365b-a247-e0c17261e46e | -11.43736 | -47.32495 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed0c8824-ed82-3b90-abb0-770709ebe5cd | -12.10161 | -45.65555 | 2026-09-22 04:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e867664c-bb75-3794-a443-a750f7c62a6f | -12.77663 | -52.85556 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74cd252a-a800-3d19-aa69-76a05e718468 | -11.32476 | -51.36217 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c644e608-1785-3514-a2ec-57627aeefa52 | -11.41679 | -47.34378 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3721c7d1-1063-3f9a-8f2a-1f4feaf104a0 | -13.51975 | -51.52015 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03c3c73d-fb58-36e4-a1ec-335254808386 | -14.76667 | -48.44141 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7ba7dd4-7e1f-3c38-a437-459b6a6b28b3 | -16.65641 | -49.28357 | 2026-09-22 04:49:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 735dd802-b6b3-39b7-9a53-353c8b41c67b | -9.55815 | -66.035 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfd0c1eb-401b-33b3-a116-8e60d6522ac6 | -14.17072 | -51.79305 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e18278d9-afe1-39ce-86aa-f265b0701315 | -11.28295 | -54.12739 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed647acd-3c3b-361c-af1c-620d40a2447a | -12.89106 | -52.07568 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a2faa1e-2246-34a3-8017-7ab8dd346191 | -16.06573 | -47.96854 | 2026-09-22 04:49:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eba81328-d86b-36de-8a7e-62d59e802f4a | -10.60029 | -54.00078 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54df5c90-8753-33e0-97ed-8f368ef999c6 | -14.60978 | -52.05919 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f18294e-751c-35ad-b36f-97eda0faad62 | -10.41942 | -53.79274 | 2026-09-22 04:49:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6b92078-9352-362f-9ec3-02d696e0599a | -15.98752 | -43.28229 | 2026-09-22 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 694455cd-424d-3889-b18d-89ae028cd7b9 | -11.96796 | -46.51538 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed59a6ef-d0c6-3c9c-bf47-2e8171e2f790 | -13.30342 | -51.80101 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2f1e302-9e2f-36d5-9bf0-7c82078d198b | -12.93224 | -50.93153 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README72.md)
