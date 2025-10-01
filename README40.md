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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5696399-3c76-3c5e-a670-c4c8c72094b1 | -7.25776 | -44.80141 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c04c3e2-594f-3523-8f3f-d6e3d6fffe23 | -8.58206 | -44.75228 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a053005-2376-366c-9ea7-a5e3b6ef6f00 | -5.64273 | -43.94173 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10bfdbff-c0a0-3e03-be40-da95d80dcdd5 | -3.60688 | -41.37102 | 2025-10-01 04:19:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 13765ddb-3d01-32b4-9008-90b4351b743d | -5.70791 | -42.87821 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ccf196c5-5d19-3c60-9c73-5c989512e3f1 | -7.60213 | -45.4265 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63f0854f-8911-3356-bc4c-9ddbec2f2958 | -7.78804 | -42.51089 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d0ce2eed-a7ce-366d-a12d-b6a48cef6266 | -5.41333 | -41.33052 | 2025-10-01 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dbfa8491-9b61-35d7-ad28-7cd935475da0 | -4.00778 | -43.27392 | 2025-10-01 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec4cfd6c-ef66-354e-9eb0-f1688cc9b491 | -9.93769 | -43.61928 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c74d04a0-f49e-3ef7-86b0-77559027ad5d | -5.89056 | -43.83479 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9cc4821e-053f-3bc7-b895-7a5ed424555f | -6.09113 | -42.47983 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c8a85588-2a40-332c-b4fb-80adb83d64cd | -6.48707 | -44.28736 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c3a694c6-63d2-30b1-9a99-f2b7aefcb202 | -9.26171 | -45.6964 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84a00770-d375-39ea-a848-f860f309ded8 | -5.71912 | -42.82758 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fed7741c-bd52-38f9-83f9-29cc325ca3b3 | -5.16432 | -43.71371 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a642426c-3045-30fb-b0a2-b0bc33060c4e | -8.91075 | -47.61345 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20afc4fb-38bd-3965-9f95-567b80d7039e | -8.86112 | -47.6565 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d71a70cc-f5f9-39a8-bfba-37dd8c50c64b | -6.1449 | -44.73822 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0feec90a-4155-3abc-9d33-67252f66ceed | -2.702 | -49.07668 | 2025-10-01 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bb08f9b-118d-3d90-a74d-4ae0df9d8ff1 | -5.253 | -42.89425 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| feb80af1-b94a-39fd-a869-afa57324703e | -5.6532 | -43.93978 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad64a87d-92da-37db-9b0e-ff713b226f1e | -5.83636 | -43.94396 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7154b7cb-9f55-3028-9263-2f2d02fbb4f7 | -3.81234 | -47.58619 | 2025-10-01 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62a59540-eaa8-3140-a93b-be1a3a06d799 | -5.94623 | -45.868 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d9d270e-b0dd-3383-a538-3093d4d96ffd | -7.16233 | -41.70705 | 2025-10-01 04:19:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e73eea8e-1b8e-3324-8e6c-6c39f71ee9bf | -7.38344 | -44.03474 | 2025-10-01 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 69b163e7-945f-3da9-a6ae-116cc058152e | -9.94615 | -43.58611 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcd96453-d6f7-3656-8de2-7b1a9be93d8a | -9.2639 | -45.68251 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b3f61e1-2803-3beb-8c49-55c5ad0cd993 | -4.74175 | -43.60886 | 2025-10-01 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3899291f-7639-396a-826b-ac6cd6eb6ee8 | -5.47384 | -43.07568 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdd1e40c-4142-3a27-ba22-3c04412bbe49 | -5.8164 | -42.87955 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c2d74d49-58db-3c02-9fa5-c752ba05c808 | -8.55785 | -44.75565 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c15cbee2-e7fa-3cb0-bb1f-eab874c76184 | -6.72385 | -44.58296 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5fedafc9-d799-30e2-a8cc-e14fe2b829c6 | -5.94679 | -45.86448 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06a3c1ac-9fc8-3009-bfc2-247bf390aad0 | -7.56235 | -46.77565 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2297bdb1-8b99-30c7-abfb-43e132fb781a | -5.68303 | -42.62586 | 2025-10-01 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 927d0089-71e9-33de-8a51-047ee547dbcc | -5.90608 | -45.88358 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32cc800c-31e5-3776-9b92-3ed81f8dbaf3 | -8.53796 | -44.70618 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31fc04fa-7493-3b7d-bc42-c84ca38faf73 | -7.46808 | -47.27892 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1b71bbe-d2e5-3123-b013-e7e5cca56cb3 | -5.81979 | -42.88008 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eb97f939-129d-3713-b3c5-fa3a267365be | -6.36177 | -43.9544 | 2025-10-01 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 29e0f5c1-ca9b-37a2-9371-90668c685d5c | -4.03539 | -54.13642 | 2025-10-01 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1f87201-6a9b-3295-b63e-edfeb706ada5 | -5.94976 | -43.31742 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 926266d5-e570-35fa-a62d-286c7c063e42 | -7.51306 | -45.4296 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 007170a2-a8e1-3a6c-9962-7cab6f6bc0cd | -5.62343 | -51.94012 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f73031c4-219e-3fd5-af4f-b516f145c78b | -5.80789 | -43.73195 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 42a740c4-5266-3cff-9189-ce34b3644b17 | -3.89508 | -49.08593 | 2025-10-01 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0bf740c-11cf-353c-add8-675ad19eae4b | -6.54553 | -44.15094 | 2025-10-01 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 733a1210-e687-391b-96f5-2b23568f0e2a | -5.86489 | -42.63024 | 2025-10-01 04:19:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cba11949-5b60-3c6a-8adb-c535792e0901 | -8.54121 | -44.6853 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87296c01-ded8-3d38-863a-380883371913 | -5.81013 | -42.85234 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 66134056-d64d-3a14-aa7c-2db141c9df6f | -8.58177 | -44.66675 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9295fecc-8eb7-33dd-844f-3c83b84f09d2 | -5.80087 | -42.77601 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 060674d0-790b-385b-b4d3-3464dc50c0bf | -8.55617 | -44.7447 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c25ca1f8-71c8-3c15-92a7-b72ca8320d09 | -6.27938 | -44.07002 | 2025-10-01 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a4f84c1c-a40c-3ad4-9c18-9f6bd8990045 | -9.85708 | -44.60102 | 2025-10-01 04:19:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9a1fbc6a-374c-332a-b268-b35170e647bb | -6.28572 | -43.65599 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9020a86e-e3a3-368a-9bd8-db9e703bf2a8 | -5.27075 | -42.77789 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a2487e2-8ae5-3c74-b888-470ba3327859 | -6.04744 | -43.21872 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e10b3d18-d1e5-3c77-9461-c43adef3e411 | -9.80945 | -45.93409 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f9e3eb5-3fe5-3480-b208-ea05b8993449 | -7.40069 | -44.60489 | 2025-10-01 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fa91ed9-49dc-3899-8564-cb81ea4c371c | -3.50155 | -52.46333 | 2025-10-01 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eda44275-26d9-3fec-bd0a-61f6acfe57d8 | -9.92534 | -43.67852 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed52cab5-38ca-3b66-8782-fa9fc29443c4 | -9.32162 | -45.68097 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a562260e-004f-3236-a40f-2b83d19c4149 | -9.32988 | -45.69297 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57931fde-c02c-301c-a984-1c29249404ac | -9.4196 | -47.33522 | 2025-10-01 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ba7093a-e76a-3222-aa1b-bbe77b1d664d | -4.7634 | -43.3153 | 2025-10-01 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8fd349e0-fda9-3ec3-b791-7b273de1b0fa | -5.71177 | -42.83021 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e39afcb3-d50b-3456-93a5-12517bf0b150 | -4.99256 | -38.85859 | 2025-10-01 04:19:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4e644bac-76c4-31e1-bed5-6b1b4bc3d89c | -5.79419 | -43.29325 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d49b375-392a-3c97-b6f6-a6b9b82f24e8 | -5.83374 | -43.8717 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 401739eb-f755-385c-835c-3ca3fce75ea6 | -5.64588 | -43.89955 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5d213d9-a4f8-3e0c-ae0d-46c73064c496 | -7.21257 | -45.47752 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67ac755a-d9f7-34e7-adf1-32aa296dc7bc | -3.89189 | -52.28331 | 2025-10-01 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d6678f2-3251-38bd-bf6f-2045c6a90115 | -5.79038 | -43.0722 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2706948d-c7c1-3d66-9654-7c7b6555f5c4 | -7.77685 | -45.7211 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 771ff7d4-9e90-3297-b27a-fe1176e7ae7b | -8.89992 | -45.04808 | 2025-10-01 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 81169a78-9936-302c-b1ad-09f6d0f082a0 | -5.24087 | -45.59287 | 2025-10-01 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 65128763-080b-350b-912f-a62a9207f0c7 | -9.79735 | -45.92502 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b815f59d-b68c-3839-8cc3-ad6c20436376 | -3.52026 | -43.2371 | 2025-10-01 04:19:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 560fa1d9-77a3-3d42-957e-c0255320cd5f | -5.73042 | -42.82186 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| a85a1884-99e6-3181-b6f1-3f2f440fabee | -8.55771 | -44.71289 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4629e7cb-008a-3dc7-80e5-e8717baea6ee | -8.23238 | -45.50977 | 2025-10-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5810e2d5-8f63-394c-8896-8b9b0708a1a6 | -4.93006 | -45.74744 | 2025-10-01 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ba13315-930c-3cee-811c-736534713f2d | -6.89764 | -48.00449 | 2025-10-01 04:19:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b1aabd0-8193-32ee-b9ce-6c67cda62f42 | -5.9058 | -43.93348 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cba1fd0f-6b78-314a-9642-8da9dc0d46bc | -5.84446 | -45.75736 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e3eff99f-728b-3436-b5a5-26f3baf04789 | -3.9327 | -41.58949 | 2025-10-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8e7ab0fe-3ff0-3f52-ba29-ff8bcf9ddecd | -7.45794 | -47.25377 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3549fa6a-1f4f-3c47-8ca6-405d7f82a398 | -3.81302 | -47.58194 | 2025-10-01 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4861321c-ec63-3444-8069-bc64ee11413c | -5.94117 | -45.90004 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51981084-4619-3010-90a2-ae6e16bfed39 | -6.67999 | -43.43252 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e69c226-467c-3fab-a120-73a8972b214d | -8.55724 | -44.73775 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7065b59-88a3-31ab-9ec8-6a7ff78d35ce | -6.56412 | -43.43364 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb27c747-aafc-3dd8-bf43-0d5030488c98 | -9.27765 | -45.68111 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70353620-30df-3c0a-a343-cd67df71205b | -5.79822 | -43.06606 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 24888fd9-8587-3f1b-8613-44acbb5703d6 | -6.02823 | -43.78084 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48fcdc38-4493-3e03-b016-5ac57d217e5f | -5.86831 | -42.63076 | 2025-10-01 04:19:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a42f6510-fc53-368f-a751-b2b4f0841e30 | -6.82281 | -48.70969 | 2025-10-01 04:19:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README41.md)
