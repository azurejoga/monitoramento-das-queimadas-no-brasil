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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1373e131-d383-319b-a95c-ffda1ff0eb19 | -20.38469 | -48.82341 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25d489e8-dfbc-3d38-92c2-adce19fb1c51 | -20.38406 | -48.82937 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faad646d-77f8-313e-94d3-0aec2122361b | -20.38343 | -48.83536 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c46924f9-c9b0-3791-9de0-aab1feebdec7 | -20.38279 | -48.84136 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9d78f215-9211-395b-a1e2-d57288acd381 | -20.38215 | -48.84739 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c8b1855b-47b1-3077-a09e-17712f1f4a05 | -20.38177 | -48.80432 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58c71a80-e445-3642-9fe5-971dcc63d93f | -20.38158 | -48.80482 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9021b2c-264e-3e36-8419-834149355037 | -20.38109 | -48.81033 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 806d6217-6b6e-346f-809c-f442292914bb | -20.38095 | -48.81084 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b252d358-7cd6-3881-bbb0-8d2d5fd0fcb2 | -20.37973 | -48.82238 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f91269c5-bf02-3a61-9a99-a19390f445b3 | -20.37968 | -48.8229 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e992df87-6dea-3257-8c4b-7e722f596628 | -20.37906 | -48.8288 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 586f1f4d-c46f-3441-948c-d8bd9587b20e | -20.37906 | -48.82826 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3e6b32d6-046b-3047-b386-f95c836aa38c | -20.37842 | -48.83478 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 60999627-ae7e-31dc-a60a-02aea7804f5b | -20.37839 | -48.83422 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1de388e5-2165-304f-a93c-231ad9ea2a65 | -20.37779 | -48.84083 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9aac8cc8-d4ae-3e44-92ec-0cf50e6361e0 | -20.37771 | -48.84026 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 9649f8cb-c8e6-3383-81a1-5da23ec1af7b | -20.37715 | -48.8469 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 531b243a-2dc3-3d39-8d80-c7ce1eb0a21b | -20.37703 | -48.84632 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.7 |
| f50f95fc-dea6-397f-9389-8395b6a10a2a | -20.37652 | -48.85284 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a2272ddc-526b-3d65-a8df-567dfa5c66b3 | -20.37636 | -48.85226 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2d6357b9-c055-3efa-9491-15b818e28c12 | -20.37607 | -48.80983 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5880c49f-7915-38ce-b068-c2e280f88307 | -20.37593 | -48.81034 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 109d89a7-1542-34a3-b73b-cc1a086fd9e4 | -20.3759 | -48.85864 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 7a4429a6-27ba-3238-9b32-758a479a7d17 | -20.3757 | -48.85806 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ea173c56-2916-3e9b-a26c-80c4f3843b90 | -20.37539 | -48.8159 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbe24c53-b18d-3ced-88d2-9c5dfc2cadf0 | -20.37529 | -48.86444 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 22.8 |
| c0ee7dd4-7d37-3e7b-917d-0c135add18b5 | -20.37529 | -48.81641 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37174bcc-328a-3b1c-ace7-715cfcb4e63d | -20.37505 | -48.86383 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| e4a59a9c-f52c-3f79-aec7-9ef2363b9bec | -20.37472 | -48.82188 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9b09b47-a385-33d6-ac32-bfe45ee3e6ca | -20.37467 | -48.8224 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 00653fc2-75dd-3d9d-97e7-1a4271f11480 | -20.37406 | -48.82774 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 98352de7-7efe-3577-bbd8-a81b02a49be8 | -20.37405 | -48.82827 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e8d338d2-9589-3de2-a444-b99b17dd127c | -20.37342 | -48.83428 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 89bf8afd-95b1-3223-9bfa-9471ec3f7c5e | -20.37338 | -48.83373 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6a3a2e14-e3b9-3a98-ab9b-1ac954a0516f | -20.37278 | -48.84035 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e321b38e-d801-3e31-9ee2-a8f43cee21c1 | -20.3727 | -48.83979 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.7 |
| e7855ffa-0b98-3dd6-9da4-2a5010895886 | -20.37214 | -48.84637 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.3 |
| da7148c1-3f25-3bb8-8940-0cd9477db7c1 | -20.37202 | -48.8458 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.7 |
| e51d7fd7-9eea-38c5-9659-293fb7bc9bd2 | -20.37153 | -48.85219 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.3 |
| b61b6a8c-0eed-3b47-b092-efbab20ca842 | -20.37137 | -48.85162 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6c1c0c69-3f18-3411-9121-e5c218f18310 | -20.37092 | -48.85796 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6f88319e-81d8-3119-b01b-4526a44c36cc | -20.37072 | -48.85739 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b897196b-81e2-361d-88b8-ca99ec60185f | -20.37037 | -48.81541 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4281a98c-dd77-3298-af87-901ea6bd9896 | -20.37031 | -48.86379 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 57447c22-2ee5-3c8a-b34c-9bf3cd9c9187 | -20.37028 | -48.81591 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2de0176-be63-3365-b317-b8ada932aea2 | -20.37007 | -48.8632 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c08e1473-a652-3609-9123-2eab85e3af9f | -20.36971 | -48.82135 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cd1c8cb-1cdc-33e3-802c-32cd1e000285 | -20.36966 | -48.82185 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b7bb0e82-afd9-3c27-a42d-0a40480652ab | -20.36905 | -48.82722 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 8916dae7-bb19-3c2f-a910-bc2ec08f9ecf | -20.36904 | -48.82774 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1d7a1d9c-cbca-3fa4-bebc-cecc5508286f | -20.36841 | -48.83376 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 63.7 |
| d9c78291-41f5-31e7-b7cd-a4ce902f3fe4 | -20.36838 | -48.83322 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 24.6 |
| aee2b9c4-7367-3ed7-b9cc-4f493bc2cd1f | -20.36778 | -48.83979 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7c34531b-8e25-388a-badd-7d372a9b1f77 | -20.3677 | -48.83924 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 910297e8-6215-3e9d-af12-97e7684a4d88 | -20.36738 | -48.79685 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8f047b63-2560-33c7-b8dd-bd7450d15e9b | -20.36716 | -48.79729 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1158e513-5d30-3095-bef9-2ac7c076a5e2 | -20.36715 | -48.84574 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 4b02c75a-3ff1-3f83-b639-754bb46b2650 | -20.36703 | -48.84518 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 90e9d725-342e-36ea-b01c-5267324c35d8 | -20.36672 | -48.80273 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7424fc47-9b2d-357b-8abd-4ec1d82ef069 | -20.36654 | -48.85155 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 70803a80-7474-3c80-af7d-9d627007de03 | -20.36654 | -48.80319 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 156277c0-53a3-3f7c-b72f-4ba78c6c72d4 | -20.36638 | -48.85099 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 414f6cdd-028d-36b0-b4a3-d4f92903a4e9 | -20.36593 | -48.85735 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 599f1b6e-cd3e-35ca-9990-5473d7394e74 | -20.36573 | -48.85678 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c008d745-f790-3496-8161-df37d76b4e41 | -20.36404 | -48.8267 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 24.6 |
| bb914576-b04e-3127-94e1-2de2f9662f2d | -20.36403 | -48.82721 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c811103e-d6d4-3be5-9868-28c29c65db44 | -20.3634 | -48.83322 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 25f987bd-4f25-3471-a3bf-d8f7fadf27c2 | -20.36337 | -48.8327 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 01e49b78-ba73-3ad0-86ab-cb2169d80dfb | -20.36278 | -48.8392 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d3f2b3d2-9d86-3b8e-8a4d-852532257484 | -20.3627 | -48.83867 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 3466e2e5-c6e1-3d25-b179-992e52b5a145 | -20.36236 | -48.79631 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e72d622a-694f-37f5-92c6-f36338ec773b | -20.36216 | -48.84509 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 50750d32-752a-3cff-8347-27546528b69e | -20.36214 | -48.79675 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 28ebd8c5-f00b-31e5-ac20-7afcd84bdd51 | -20.36204 | -48.84455 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 76fefef4-2a37-3655-a449-a275f11e5a74 | -20.3617 | -48.80222 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0d0089e-76ae-32f8-b597-7949c4ab482b | -20.36155 | -48.85094 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fad1b174-e7ee-3706-a0dc-5eddc6db1e18 | -20.36152 | -48.80266 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d910f15f-af39-3c55-99cf-9f11aae757dd | -20.36139 | -48.8504 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 85fe3fa5-63ac-3031-98f0-123fb51cc087 | -20.36103 | -48.80825 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf60c663-f3cf-36ea-98ca-da5bb8fb72a2 | -20.36094 | -48.85678 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| d8e40cba-7777-3b38-bca3-5c66b9146ca7 | -20.36074 | -48.85624 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d5d3e289-2b9a-3c06-8fbf-5db626821a97 | -20.36009 | -48.86204 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e6844c45-4920-3736-abdf-f7364f08b7bf | -20.3597 | -48.82019 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35564bf4-501a-3880-9479-bcf05b4e3db8 | -20.35965 | -48.82068 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ca6dd0fc-baa0-3f08-bb19-ae09347d4b48 | -20.35903 | -48.82619 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b2d48a3d-b3ec-371b-a0fb-737f7d234e0f | -20.35902 | -48.82669 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6809fd36-ddcd-36b0-9624-178d2b9cdd40 | -20.35839 | -48.8327 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.1 |
| cf3e2112-a91d-3c6e-9e72-c1b39a75198a | -20.35836 | -48.83219 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e30c3141-e1c2-3e21-b229-18f90b0734df | -20.35777 | -48.83868 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 90c4471f-196b-3c22-810d-b1300ebfbd94 | -20.3577 | -48.83817 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d7390551-c944-3648-aa96-8096e0e7b62e | -20.35715 | -48.84462 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ea97d35f-c971-3ec7-8022-f22e4fbd8e08 | -20.35703 | -48.84409 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 61b490f5-6c28-3610-94d7-46a96b81760d | -20.35654 | -48.8505 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b55140b9-a206-3cc1-bd81-b75ee6277594 | -20.35638 | -48.84997 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| c0bd9140-bb54-35d5-b667-e75e50e91e00 | -20.35601 | -48.80775 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84f4b8d6-3798-31e7-a502-ae001f25fcc6 | -20.35593 | -48.85632 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 9782cfaf-eb7e-3cfe-af6b-133903601143 | -20.35588 | -48.80821 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f51f079-2f59-3b16-a03d-1290bdc2503c | -20.35573 | -48.8558 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| bc927d57-fd65-3d64-af41-79f946f84172 | -20.35533 | -48.86206 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |


[Clique aqui para ver as próximas entradas](README94.md)
