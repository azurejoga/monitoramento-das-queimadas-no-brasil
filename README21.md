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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 794947bc-eb9a-378b-a8e3-99538af409f9 | -11.44354 | -43.89053 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9939b24-6d72-3282-8cf7-d7ed9379df9a | -12.47978 | -47.26604 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8f4285c-d38c-3793-a04c-4fb377eae7ec | -11.47103 | -44.97201 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 262ed11e-9846-3641-86f2-6fa882fc7f1e | -10.54292 | -43.64936 | 2025-10-02 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 034d3f1d-cc95-329f-97dc-47d3f0d700db | -11.48191 | -45.00874 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d066f15c-207c-338a-8567-ffd99eace9af | -11.61847 | -45.0496 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 58cf0d39-e019-3dc3-921f-903acb12839c | -10.26745 | -50.33254 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 27cc42f0-cca2-3642-afee-0fe64b6df6da | -10.65778 | -48.50161 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0818013a-4f6d-3537-89e9-a31a01559905 | -6.08631 | -42.42628 | 2025-10-02 04:02:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c98f526f-a338-3afd-b922-50023eb34669 | -10.23186 | -50.31514 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c2ddf79e-9981-30df-9645-1a39c2efe0cf | -11.26779 | -47.80954 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 380fd4ae-12e3-335d-9402-382367b5baa2 | -11.85808 | -44.99031 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0cac5af0-a5c5-3200-baf2-2d03979f7faa | -6.72165 | -44.5624 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7f1db1b3-8f5b-3f58-892a-42528713d42b | -10.84158 | -45.38267 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a327a78a-f0b9-3a10-8dae-3b296fec16dc | -11.26727 | -47.66022 | 2025-10-02 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84e4477e-404f-3968-b792-cf042752c4f3 | -11.85147 | -44.98442 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a6885ea-d6c6-3993-a789-5f0b572bf4cf | -8.66303 | -47.09147 | 2025-10-02 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a6635d5-210e-386a-92f6-bec3c4f3ac54 | -11.80153 | -44.97266 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c37a612-3b5b-3d43-a3df-2d1a5f6aa4ca | -6.72369 | -44.14869 | 2025-10-02 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b1369fdf-8447-32d9-8ccd-cde18d76b229 | -11.03291 | -47.82851 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7ba5b613-4093-3deb-871d-2d2e88698ef0 | -8.64145 | -43.98493 | 2025-10-02 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b802fb5-b935-39d3-8c41-1e4cfe64ff01 | -9.79512 | -45.94596 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f80b33bf-ac28-3e6f-981e-579cffc881a2 | -10.22257 | -50.33485 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e90ee2e-f03d-347b-93d8-3d4bb297ce04 | -10.35116 | -48.20338 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0136aacc-d8e8-3869-8d05-c4224b50d6ce | -11.44002 | -43.88993 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad4b4566-8583-3c37-bbbd-1b53dfbf6841 | -12.84462 | -46.95434 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b2a099e-c6f6-3b25-8103-f16b25aa89a6 | -12.83124 | -43.80584 | 2025-10-02 04:02:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ecb99c42-fac3-356e-b06f-0af6dae41e98 | -11.44321 | -43.50078 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4bac85a-c332-35ba-9a38-831e6b7fc3fd | -6.47994 | -44.28661 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b358958-abfd-30e5-94ab-943533519bf9 | -11.46706 | -45.06431 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f2ae5c6-8af0-3601-b73c-244305903ebd | -6.32849 | -43.04067 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 584075ea-8e95-3307-a329-95db54324a2e | -6.69704 | -48.70195 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4bbb978a-4aca-3da1-81c7-c51b7403fddc | -12.07478 | -47.83585 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a78853c3-f3d7-3da8-b378-2500019cb293 | -8.88081 | -46.5924 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 388d32ef-6ac8-3a32-b8a5-9f44c07f024d | -9.93834 | -43.7023 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8886239e-f77a-355a-8f9d-b67123be4100 | -11.36218 | -48.33241 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ea0b6a6-7dea-3bc9-a911-ff7910e59c9d | -12.05696 | -48.77273 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad718743-e99d-387b-9fa5-09083bbe38c9 | -9.94164 | -43.74908 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e651fff0-7846-3989-9b95-1368ab5b0cfd | -12.67736 | -46.85872 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a64a634e-3557-3984-89c8-b0caa5c6dd43 | -10.23396 | -50.33341 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6ba08b48-f2ff-3d52-85d7-446208b380c7 | -10.2681 | -50.3291 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0f44546a-3079-3d60-ac8f-8fd1d22c41e9 | -10.89344 | -44.29274 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9803c1a-7805-3f4d-9337-dd511ee92a32 | -12.22028 | -43.7607 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0edb12a8-7188-3993-95d7-4e3b344565f0 | -5.91959 | -44.85868 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc3a609c-7506-3a77-88ec-b4a8949292a7 | -6.11373 | -41.7943 | 2025-10-02 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1b7009ea-2f01-3979-a723-998d3c7c55ba | -10.24128 | -50.32405 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 762bf2c5-77fd-3471-95bd-e95e736d7873 | -9.42392 | -47.35262 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7a9f2b6-dc80-33c9-a951-558d92b25fef | -10.75863 | -46.14219 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e77f4d19-c5a5-32d7-9740-29583bfa2ea1 | -11.47028 | -44.99933 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30ad4dee-1bf9-3c1a-bbb7-a81e05d8a195 | -8.55765 | -48.64265 | 2025-10-02 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78247637-75cf-3261-94ee-c6d32ec8c9b8 | -10.19123 | -50.27888 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0c4c165-d4ab-38a5-9de0-1afca00400e5 | -9.92019 | -43.65763 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdc4aea7-6720-373b-a460-7d6b40452f30 | -7.17337 | -41.69696 | 2025-10-02 04:02:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4fbd2524-6eb2-360b-8325-afce5f52dc67 | -8.90279 | -46.06843 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75db762f-38af-3d5f-933d-0abe6e1ca4fe | -11.98907 | -50.5727 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59d0b7ee-f0be-34b2-9d12-bdf9c86b2b92 | -11.45295 | -43.5064 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae7c2eaf-e874-363e-bd35-cf6ffe047892 | -12.19805 | -47.80624 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bce4d422-3fbc-3a9d-8062-4b481f50547d | -11.59562 | -47.21717 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 671bbb98-3552-350c-88c0-96c2d41f6a38 | -11.53023 | -43.54733 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2132e08f-0569-3a4d-a1be-d010eb888735 | -6.49295 | -44.29607 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 226c3c01-4d31-3182-a767-61cc950a6274 | -9.93921 | -43.71922 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 77805b36-c92e-31f0-8366-31898b707932 | -11.82212 | -47.67745 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7dd7220-bd8d-301b-ab43-3e102c75d8b6 | -11.80959 | -44.9927 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c905d496-5166-3755-8d6a-ff1be109adaf | -9.93029 | -43.75146 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 199064e2-6f11-3c4e-8189-386915581447 | -7.56227 | -42.40197 | 2025-10-02 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3b1cc25c-a163-327f-8e3f-88c9a5651e0e | -10.99377 | -46.59824 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 2055b329-afe0-39ba-820c-a206d3b31165 | -11.47257 | -44.98565 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 620a329c-2166-318d-9349-e8249fb4e8e1 | -12.84791 | -46.86448 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2cbbf1ce-8185-386f-bb2e-364b961daa19 | -11.79164 | -47.57294 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 827452aa-3974-3724-b1d6-33ff8a684575 | -11.8293 | -44.98057 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22615785-91ea-39cf-b9c1-b59039974648 | -9.94897 | -43.70409 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b3e98214-6a9e-3971-b8dc-ba2ccdaa8dc2 | -9.92926 | -43.64669 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6def6d73-9fb7-3faa-a841-9e674fa2b504 | -11.47401 | -44.99989 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1f853f5-05bb-3800-b212-154658392748 | -10.85225 | -46.58978 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6747c0b4-df9a-30e5-9726-aaafab327d9a | -6.28342 | -44.06052 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc7c1f5d-4e70-3998-a7cc-3ebd0a7928eb | -11.00147 | -46.59237 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| e6b4b134-de41-3b64-8dc3-ff800a4582e7 | -12.10989 | -43.42478 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3c74067-3854-3b68-8d39-7bcd52ebe1ed | -6.31304 | -43.43776 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07deabcd-5203-34ac-8816-194181706c39 | -9.94761 | -43.64563 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97d5d68e-4009-3d5b-8d4c-b8479bcdbb6d | -11.56946 | -47.022 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8829d1f9-f3ee-3710-8277-3c5fa74147a9 | -12.12646 | -43.43126 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b5a757e-7d0c-3ce5-ab78-ec62bc3abffa | -12.88637 | -46.93313 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c9550f4-ba00-3917-8d3c-96c5e63257bb | -9.93828 | -43.76962 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3d5d08ff-44e8-345c-b556-a26842c8c764 | -12.79872 | -46.8572 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 608d9cb2-7262-313f-87a0-aaa76e00e3bc | -11.87657 | -51.22572 | 2025-10-02 04:02:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27bf58e5-dae8-30c6-9276-f00557b50da3 | -12.11458 | -43.41772 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb9e87f4-8128-34c2-9c4c-989d9ffe4e38 | -11.86791 | -48.07541 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d300775-fc14-3492-b1ef-6b85dff5d5eb | -12.86668 | -47.02163 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c08c8bd-5c5d-3416-b92e-1fb662d87a24 | -11.92493 | -47.05671 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cf16769-336c-3309-bd82-70a4eaf2215f | -11.00494 | -49.5853 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49d7c2ee-7231-33f6-b051-2dc4e57362a2 | -11.8472 | -44.96498 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49839bba-d6f6-3aec-a313-d5f45f224979 | -11.10868 | -49.80552 | 2025-10-02 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fb1576b-8073-3877-8c3f-498d0df2b184 | -7.78932 | -42.51975 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| fcc7dea8-b563-3dde-bcfb-05a37c23c897 | -9.93741 | -43.75257 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| c5960589-266b-34cb-9403-f56435e9e969 | -10.66706 | -48.56477 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9bfba8ff-b3ca-3012-bd19-4356a721ae7f | -11.00692 | -46.58563 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f549a50-133b-3aa5-a287-2cdabddb61f8 | -7.05392 | -43.31258 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cdd6786f-1aa0-3879-8a49-000d7fc5a663 | -6.33405 | -43.02893 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b20c07d-0275-3441-b154-4a6fd7c4181e | -7.78056 | -42.53009 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1ec6780a-1e5b-347d-b631-99d516d366e5 | -13.01862 | -45.21695 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README22.md)
