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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c1a8599-56cd-30e7-8c91-8a4d43c97297 | -11.29539 | -43.3245 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 456c0fa4-4dbb-3816-bf91-1aa9284c8308 | -11.51216 | -56.12185 | 2026-06-24 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9916d64-3a6f-3f8a-8b44-a5c72ca644f8 | -11.8911 | -47.59645 | 2026-06-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a82871a-b0ca-3fa0-a259-642b07957000 | -9.37853 | -58.20576 | 2026-06-24 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9efe2aea-40a0-3929-83a1-5c0c3a08a674 | -14.8767 | -48.37038 | 2026-06-24 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd2809c2-70d5-3db2-bfb6-88359c16060f | -12.73064 | -49.08648 | 2026-06-24 04:34:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62f2eeb0-9494-36ce-a492-93a9ad6c1cc6 | -12.83184 | -44.36268 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| de31a369-54ad-34b1-8410-1629c82264c5 | -9.46048 | -49.83102 | 2026-06-24 04:34:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e26e876a-6336-316a-a845-a24eb8d3299c | -11.91678 | -44.17587 | 2026-06-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2111bff4-f6e2-35a4-8f46-7668f13182ef | -12.51659 | -48.26758 | 2026-06-24 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9319b728-3b63-3211-afbe-6495a2e04240 | -9.22103 | -45.33782 | 2026-06-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d51d253-7421-3f65-898b-e53e232802e1 | -8.61398 | -46.00147 | 2026-06-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 403106a9-30e8-3193-9c35-76ca6c7187a9 | -13.0688 | -53.35147 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| beb1db67-9524-36cc-ad12-0e6af887402d | -11.29219 | -43.31692 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 19130049-8b31-3cd0-8554-1606902c9554 | -12.83255 | -44.35752 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d74800f5-ab45-3dba-a956-cc918586d458 | -11.64204 | -52.86101 | 2026-06-24 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c29fb3f-1971-36d9-9303-f68120e13622 | -10.84396 | -48.77056 | 2026-06-24 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 550af10f-7a1b-3375-b0ec-0bb2af29e401 | -8.60767 | -45.99657 | 2026-06-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 5c00d8db-d13e-3632-aead-fb83c59667a4 | -12.81649 | -43.89915 | 2026-06-24 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fa21be0-f3ea-3f00-8daf-e8acd94446a4 | -12.19513 | -47.96877 | 2026-06-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3c7b449-5f5b-38a8-bb0c-e2562c70c8f0 | -11.40988 | -54.43726 | 2026-06-24 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 343a10d9-2f88-3545-9be4-19092fb2b34e | -7.60255 | -46.47524 | 2026-06-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ff569e3-5364-316e-a546-6331dc498238 | -10.87693 | -49.40404 | 2026-06-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1843ed49-f763-3918-b00c-5bb1e3b84be2 | -11.238 | -43.35569 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7ec1d3e2-0ec2-3b1b-a447-1e135067df44 | -10.10991 | -47.55555 | 2026-06-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 44a113ea-9112-39c6-9034-baa12d4114ab | -11.28268 | -55.79617 | 2026-06-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7acdfad1-11d9-301f-a120-9530d88a5c23 | -7.92399 | -48.292 | 2026-06-24 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 64511cf1-5663-3826-863b-65c6ff34df64 | -10.70073 | -49.61389 | 2026-06-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ce32bf0-3df7-339a-b65c-77f977101b6d | -12.5155 | -48.27471 | 2026-06-24 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ef099a8-5616-3667-afc6-e875d50f429f | -9.51071 | -48.06903 | 2026-06-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c115a81d-239b-3075-b423-c432a4394476 | -11.30367 | -43.3256 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 40a85a30-8309-332c-a4be-fa0768b83633 | -13.06126 | -53.35015 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 34352ac4-11cf-3396-a896-92dc7ba34678 | -10.16235 | -56.62557 | 2026-06-24 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55da8efa-f23e-3b68-89c4-4e4a571e96da | -10.87748 | -49.40052 | 2026-06-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbb2fdd8-fb77-30c0-b0a8-88666af025ef | -15.72878 | -41.35122 | 2026-06-24 04:34:00 | NOAA-21 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8d574435-9767-347f-8afd-d30640763bc2 | -8.07403 | -46.39416 | 2026-06-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d09e2b98-552c-3ba3-bc49-0ff870e4a618 | -8.82417 | -47.06964 | 2026-06-24 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17232eac-5803-37f8-90bb-d50f6374baaa | -11.54853 | -48.26291 | 2026-06-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d179fd83-0544-3906-8f31-8aeeed245e4e | -12.83507 | -44.36843 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 147ad497-057b-389a-9fd0-74874cb48e37 | -11.29589 | -43.32081 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c25cb889-b08f-3303-840b-9ab8ba6cd689 | -10.63283 | -44.8567 | 2026-06-24 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a265e318-1dad-3b23-ac64-cc36ef971499 | -14.52638 | -49.10687 | 2026-06-24 04:34:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49a1c106-1416-31fe-b2b1-0f3fa4dc04da | -8.6134 | -46.00526 | 2026-06-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06475303-88b1-3f48-8a45-9ebccf29d00d | -8.85326 | -46.94611 | 2026-06-24 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a34ba5e-bd21-3542-a7f7-742674ec6f26 | -9.36939 | -50.54459 | 2026-06-24 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6bba07c8-7cef-3e00-a44a-0ce2f79e5a05 | -9.19194 | -48.62618 | 2026-06-24 04:34:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaf37cba-8718-3062-ab1b-bcae251bb64e | -13.06341 | -53.36026 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 572d1f62-4dd6-353e-b163-1dec95bad781 | -10.5772 | -57.31702 | 2026-06-24 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ab4e957-e903-33b6-b6e5-0d574b4f8a55 | -10.54085 | -53.73391 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea37e69e-8b42-35bb-ba45-852fe8390d54 | -10.69797 | -49.60982 | 2026-06-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c0b347d-5d35-387e-bffa-0f773b688089 | -9.08693 | -47.53018 | 2026-06-24 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07556b12-f461-3d68-a1ba-2274db246978 | -9.41124 | -50.69577 | 2026-06-24 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24d1d194-6149-39bb-b434-624571ae6ac5 | -12.29199 | -44.18191 | 2026-06-24 04:34:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a48146a4-decf-38ab-bad6-05b50a81511a | -12.82789 | -44.36209 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 50dbe79d-8387-3740-8c32-ed30bf48a501 | -11.54799 | -48.26644 | 2026-06-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e73fb18a-80fd-3d3d-8af6-67181c139ecb | -11.25345 | -43.33534 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 26cc7e1c-733a-3e64-977a-253351c8fe22 | -13.06719 | -53.36092 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5e169247-65cb-353d-86cb-76650c02887e | -11.3073 | -43.32993 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a2655912-588b-3a0c-bf67-b8d57e3d6cd1 | -10.16132 | -56.63116 | 2026-06-24 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f39f83fc-2056-3e3d-ba51-a195d9694e7b | -11.54313 | -52.77911 | 2026-06-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02d270f4-eae0-3a92-87eb-0f6b21d070c4 | -9.03492 | -42.70257 | 2026-06-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4842ee42-d031-3eae-829f-eac97774ea3a | -11.50218 | -46.70171 | 2026-06-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5b02b92-0b1f-3fe7-978b-05e0a2fbc031 | -10.76888 | -54.10716 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c289e522-54fd-3aab-a9b4-8d758cf28cbc | -9.21316 | -47.92553 | 2026-06-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0ed085e-00a4-3c06-a206-32233afb35e4 | -11.23747 | -43.35952 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ead78ffe-ea96-3aee-b67a-afd0c8d000e3 | -9.51409 | -48.09095 | 2026-06-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc248d2a-d8fd-36d8-9599-d3e90bedcf7b | -11.2702 | -43.35548 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 136f22d8-c409-3bb6-a646-4d86dbbc672c | -8.61514 | -45.99387 | 2026-06-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fccc09e6-a6de-3af2-863a-27a015c232d5 | -12.84044 | -44.35873 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| c647943b-c60f-3115-a357-da5c73868578 | -10.88024 | -49.40457 | 2026-06-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b0d972c-9343-3388-9b94-96d7c4f9db98 | -11.24007 | -43.34071 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8690006f-25de-3a72-a2bb-7d3886e5921d | -8.13411 | -47.8863 | 2026-06-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6ceda3e-ebfc-354c-aa2d-286fe5e2d67a | -8.2698 | -49.35942 | 2026-06-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d795c68d-be9b-32b5-8385-2484eb45edcb | -9.1871 | -58.07076 | 2026-06-24 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5f1dc77-fae8-3498-b18e-599687cb5598 | -13.06045 | -53.35487 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 70f53b60-5c9c-34de-8ac5-4890823f892a | -13.068 | -53.35619 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 230c1cd6-2de0-3a2c-9b79-d4fe1633f98c | -12.78369 | -44.45004 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 31ae54d2-81c3-34bc-aa83-11f9cd3cec43 | -9.00762 | -48.00011 | 2026-06-24 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f085154c-3939-3359-ba1d-709fc744d7e7 | -12.8469 | -44.37021 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 29370f82-64c1-312d-8fbe-25d6d399811b | -8.12751 | -47.88527 | 2026-06-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0939aa65-32f0-3b67-a31a-aa0ed2de6941 | -10.63347 | -44.85215 | 2026-06-24 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc0b9796-c631-30fa-ba34-11ef5e6cb8eb | -11.29903 | -43.32878 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cee9ca29-e5db-3170-87da-e29b038a8cfa | -11.76205 | -47.07581 | 2026-06-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e123345-620d-30f3-9732-4c0f2f8128db | -10.37666 | -47.61158 | 2026-06-24 04:34:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1c1649a-6128-38d0-b967-a017109f6fe1 | -11.75809 | -47.07902 | 2026-06-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13f316f7-5ad9-33de-afc9-11701d95bf10 | -8.68354 | -47.85285 | 2026-06-24 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c2b45140-7535-3d62-9a2d-72aaaf70c615 | -10.70158 | -50.13676 | 2026-06-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1adb097-ae5a-37c4-a277-6020077c78a0 | -13.1236 | -53.53072 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbf57bca-064c-32f2-aded-828e6e473ee6 | -9.18776 | -58.06715 | 2026-06-24 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bea3c8e-d90e-3ec7-bb79-b60f29da90d6 | -9.58499 | -49.11531 | 2026-06-24 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78e2634f-9b46-39d0-9364-477195aa8de6 | -9.06432 | -44.75018 | 2026-06-24 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b95ba16-903f-381a-94c2-24cb9d4512fd | -8.33781 | -50.49397 | 2026-06-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b789ef90-3e1a-31eb-9a63-4b64d1f15efc | -10.80437 | -48.56425 | 2026-06-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c672c9c-efa3-3424-ac53-81d85b125242 | -10.16337 | -56.62002 | 2026-06-24 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c2438c7-ab84-3e54-8e95-047d126a785e | -10.63142 | -44.85443 | 2026-06-24 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b18e952-46a5-3587-be89-64e618ed6fd9 | -11.30831 | -43.32243 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 90cd1089-e65b-3213-b545-316dba5285f3 | -9.00815 | -47.99664 | 2026-06-24 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ac80571-28c6-3c87-a863-124c399c1a3e | -11.23543 | -43.34381 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b548b35d-c02a-32c5-8e62-fa7dffe75b0a | -13.54153 | -52.95921 | 2026-06-24 04:34:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c98f7b64-d78e-3593-ac0b-61d7d06392b8 | -11.24057 | -43.33707 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README14.md)
