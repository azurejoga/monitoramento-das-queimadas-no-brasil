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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9198c55a-d834-3ecd-8506-44a9c7c87f60 | -4.07221 | -50.36023 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf393613-4f8b-379d-81bb-99142296e258 | -3.45756 | -50.22433 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d876715-f13d-338b-866b-ab58aed61f69 | -4.14609 | -50.68684 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 551cb0b5-ba9f-3504-bf4c-6b0dd67660e6 | -7.40443 | -40.06945 | 2025-11-02 04:48:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a58632df-a2e0-34f0-938a-0c91f17f6c2f | -1.81897 | -55.16716 | 2025-11-02 04:48:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 521afd6d-a725-3cb1-8623-964d87a256d4 | -3.15948 | -50.82553 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14d29ad6-fdff-30aa-a8c7-1c9726d78c97 | -4.15684 | -46.79537 | 2025-11-02 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c3e6d62-b749-3b9a-b5da-e3d104f99ef6 | -3.59382 | -54.04199 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 430e3fb4-bc92-38de-825d-495ce6550b18 | -5.03509 | -43.61995 | 2025-11-02 04:48:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d7b2fba5-ffcd-3bd8-a00c-d5f86510e601 | -2.93149 | -54.02894 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0dce3b0-99bb-30c3-bbbf-9dde77c23898 | -2.82388 | -49.12999 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 692359e6-509e-3f16-8910-6ec48ea56cb1 | -3.13849 | -50.44691 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e484ad74-2c7d-3e6a-bbcd-7a8cfb51c86f | -5.07301 | -43.66684 | 2025-11-02 04:48:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72553317-2a9b-33d6-a1d8-fa9c5ea6c177 | -4.37179 | -49.74454 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3ccc877-f9a2-3ae5-b44e-488a6972b5c0 | -3.08583 | -52.92309 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61778ee9-55f0-315f-aaad-a69df059a5a6 | -3.65871 | -50.19262 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2b05b42-37dc-3ebd-a919-fb4ecc1994b8 | -5.1248 | -43.37477 | 2025-11-02 04:48:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9b18744-bb14-3c41-8a37-45b3c66b3584 | -3.43016 | -52.89018 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 606bdaf9-43f5-3564-a844-cb9543473b2d | -3.85706 | -49.66475 | 2025-11-02 04:48:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f626d3f-1893-3b2b-8468-6df943d30d6c | -4.3201 | -45.64228 | 2025-11-02 04:48:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98b97669-80e3-3993-bdf6-1341704c509d | -3.71333 | -53.37324 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b58a21b6-bc95-3745-a72e-39a11f2c2320 | -4.28066 | -48.65164 | 2025-11-02 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8c1a414-1bcb-3fbf-878b-7840309788c9 | -3.7952 | -53.87948 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 020cda64-c314-3ee5-bf18-a2f01e614060 | -3.07142 | -51.25117 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a15f4b83-9346-35a0-a7af-6a812df69ba4 | -5.09447 | -46.11071 | 2025-11-02 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 979c1c15-28d6-3e97-b64b-7a0792da7403 | -3.58327 | -50.26591 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d65a2271-a79e-31fa-bbc1-1d89c11683f2 | -3.90144 | -49.91802 | 2025-11-02 04:48:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d57e4e6-db7b-35f8-97e7-ed7da70a4311 | -2.83948 | -49.40278 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ed874f0-f34a-354d-b4e0-560072a38151 | -4.54903 | -46.01882 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b538c10a-2e38-347b-8c9d-8e2317f4df01 | -3.29291 | -52.95892 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6616bf0b-7255-39de-a2f5-948e6ddbfbab | -3.85537 | -49.91457 | 2025-11-02 04:48:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d349d3b-230d-3531-bdba-b94f5e3c7745 | -3.56525 | -54.59012 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d9acd58-3a54-34bb-95c9-452f47dd23ee | -3.50793 | -54.37862 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9bf1a90f-ba84-3b0d-8d43-83bed46414fd | -4.3708 | -45.87941 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eecd8b8-7f1a-3cbf-a234-a5a803c02b65 | -2.98755 | -48.70427 | 2025-11-02 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fa024dc-576b-3b8c-82ae-ec7d57335175 | -1.55813 | -55.42311 | 2025-11-02 04:48:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b95b5298-218f-3024-b9ce-3111840bf89b | -3.34844 | -51.68314 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e52e8720-e9c7-339e-9d76-1b89b6aab0ad | -3.83688 | -51.31434 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d99f1411-68c9-36b0-9131-c9da50b86d0c | -3.27446 | -53.27393 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78abd686-9fa1-3883-a3ff-e8b18be4c570 | -5.03976 | -43.6207 | 2025-11-02 04:48:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b350051-03c7-3e56-b9c4-e9d1973a5356 | -4.13583 | -51.15356 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 410acaf5-d779-34c5-9e2a-2acc43788a65 | -3.08645 | -52.91914 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ec77748-08e4-30f0-b1e6-e2f562c197af | -7.40382 | -40.0741 | 2025-11-02 04:48:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 96f65407-737b-3b9b-ab90-f7c061b1b878 | -3.12863 | -49.23462 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ea622aa-28a7-3281-842e-20ca41c2db0b | -3.58929 | -47.51632 | 2025-11-02 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e242e2de-68d3-3091-acc9-9be482119b67 | -4.50428 | -50.49554 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd926304-a27a-3ce8-ab07-b54a7f3fcaa8 | -3.52033 | -50.31973 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a11dd1c6-9325-3e7e-93a9-cc6f08705ade | -4.13139 | -51.13857 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83fdc67c-0ce5-3114-92f3-f942b4477e97 | -4.58296 | -44.79166 | 2025-11-02 04:48:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eba8b74f-d3e9-3869-8656-67d2c4d37257 | -3.04123 | -50.26853 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abf11a7e-d138-34f4-900b-4f44e66a80b3 | -3.59287 | -47.51687 | 2025-11-02 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7d12c65-107c-3ce4-8888-4c301157736f | -3.2346 | -51.47875 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82c57be2-c447-39cf-b04c-e9c80e44a3b5 | -6.48132 | -42.05662 | 2025-11-02 04:48:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20b0fc1f-242e-3e68-b830-3f5240ecea2b | -2.8317 | -49.40874 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c9189f5-6379-3018-91be-e500240ba3a8 | -4.37458 | -49.74857 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89c4199c-74b7-35c9-af4e-91d55bd3b519 | -3.50946 | -54.36929 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 231a07a9-f5e2-37be-9223-188b5791cd4b | -1.8149 | -55.16644 | 2025-11-02 04:48:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0538c0ae-1988-3b9f-9177-4dde2b31bb0d | -4.48485 | -46.07061 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ef8b036-4008-3810-92e9-91aa72ff25f4 | -1.75009 | -54.44705 | 2025-11-02 04:48:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db9597f0-e5fa-36cc-a6b9-bda24aad7539 | -3.2345 | -58.88762 | 2025-11-02 04:48:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1ee0ac2-d7a5-38fb-8109-8b1d9b61f5f2 | -3.60105 | -50.6222 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a4b76d5-b6b9-3a41-8303-23e095843e74 | -5.12535 | -45.82637 | 2025-11-02 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68de22e5-eab9-3535-95a2-8c4e17fd0baf | -2.26729 | -47.85744 | 2025-11-02 04:48:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6189d0b0-c4ac-31fd-94f6-2f6f8b8554d6 | -2.44756 | -49.03205 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 694db429-a540-3f5a-be4a-830d0076f8a8 | -2.87332 | -53.9796 | 2025-11-02 04:48:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da160f7b-9753-386b-aa18-1b591974fb27 | -3.24207 | -50.79591 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd2f950e-41d1-36db-bee1-1431f9615996 | -3.2288 | -50.5812 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f231f9a-144d-3a4e-84c9-4c003c57b806 | -4.63646 | -38.569 | 2025-11-02 04:48:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1257c8e2-3e97-3ec8-96bc-1975a1f29a54 | -3.02199 | -49.4452 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7710715-44cd-34de-85fb-3b1e42443c3d | -7.32412 | -41.54407 | 2025-11-02 04:48:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c60233db-9d4d-3ea3-b068-3764319b1ac8 | -4.1818 | -48.59056 | 2025-11-02 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8d56964-1239-3483-bc35-2cda68282410 | -4.8474 | -45.83241 | 2025-11-02 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc96cc2f-c60e-3489-818e-8f137f179b16 | -3.61898 | -51.47417 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ac123c44-5918-38f8-9547-6281cef7e42a | -3.07589 | -51.24467 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5d0baaf-daae-3d78-b131-4db74e05ac5a | -2.82779 | -49.12698 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ae0909b-4e49-340d-8b08-5b0296965541 | -3.39276 | -51.67146 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae883c47-aec1-36f9-80d3-9eb4e000fe67 | -2.8306 | -49.41574 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 530194c2-f731-32e5-8442-78adc1d6cc55 | -3.56508 | -51.64003 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05b85b5e-45f0-3739-b9de-fc8238bc3b89 | -3.23964 | -58.88848 | 2025-11-02 04:48:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92ca384d-e91f-3d0f-8a1a-6e4f713df578 | -4.54759 | -46.02832 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4adcacc-65ee-39ed-81da-b6fb540e0e98 | -3.66765 | -51.71794 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00c2631a-190c-39ff-8fe9-8826470e0e23 | -3.14357 | -49.42442 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 483a7ef2-5b3c-3bc3-91b7-8fe69633ba6f | -2.59275 | -51.3422 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8a16288-725d-38ce-8729-e53ae07b634c | -1.5623 | -55.4238 | 2025-11-02 04:48:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be9faa2e-12df-3825-85f0-13c442a9d010 | -3.28609 | -51.54501 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5e2cdee-b907-3adb-8cf7-736de77ad764 | -3.46142 | -50.22139 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98f8f422-4ebd-35c1-b36f-2455091d9ce6 | -7.50384 | -42.45054 | 2025-11-02 04:48:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| a8603b76-bda7-37c6-a722-bf7ed27aa0d6 | -3.28932 | -50.19823 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be81fd37-b4b8-3e68-aa92-4a285424b48e | -4.13416 | -51.14259 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e114e5c-6d83-30c5-b517-283a54f1027b | -3.60051 | -50.62565 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc49752-1789-3324-9b2a-ff7f481b73f6 | -2.817 | -45.19805 | 2025-11-02 04:48:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df37e627-88cd-3ace-9f19-0fa935416128 | -3.06366 | -49.37626 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 012640c3-e1e7-31f0-aadb-cfe521dd4d79 | -3.60437 | -50.62272 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c035e86-91c1-3531-be0d-29325c3f3868 | -4.08065 | -48.04117 | 2025-11-02 04:48:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c100060-cde4-368a-bc82-866580867c80 | -2.83614 | -49.40226 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfbd068a-531a-31c6-90c1-de99d0a2dd46 | -4.13305 | -51.14956 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 00902823-5d53-32f7-8230-afe8047707f4 | -1.419 | -55.23421 | 2025-11-02 04:48:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0944b6ee-eff1-3d27-b4c8-de84770b738c | -4.1336 | -51.14608 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcad020e-d126-3215-8b4c-6fc06faa97db | -3.55644 | -50.15555 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e58aa5a-eff3-3b25-ab02-2d404c04f372 | -4.50115 | -49.80761 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README19.md)
