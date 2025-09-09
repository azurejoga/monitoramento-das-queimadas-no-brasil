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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bb15c7a-5f24-3d79-a674-68de34112a6f | -15.8187 | -52.26574 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4176daf8-62ed-375e-892c-022f62bae9bb | -15.78156 | -53.54807 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2d3843b-15d3-39a1-a37e-b4823bd31eb3 | -13.94149 | -48.23719 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 422d6fce-cb66-308d-9a35-cc6177da7658 | -15.26215 | -53.80107 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ec5e3d7-4fca-3697-b790-91fe7fd3fbff | -16.06872 | -50.48996 | 2025-09-09 05:23:00 | NOAA-20 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f6e91d2-ed23-38bf-ae64-1966a8aecc75 | -14.35685 | -60.30761 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15371b0a-ad91-33d6-8532-cc7e1a6c4e69 | -10.33503 | -47.73452 | 2025-09-09 05:23:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff1a7e74-4c91-3d50-9d62-f8c08a8f24a8 | -14.90691 | -55.84409 | 2025-09-09 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03e52425-740c-34ff-aeeb-582fd6566087 | -6.95369 | -62.92906 | 2025-09-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e36cfe8a-dd4e-3095-b9ef-8e47aef34829 | -13.93327 | -48.24672 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b0c7699a-22d7-3bd4-8c87-6cbb5b19ef5f | -15.8271 | -48.94427 | 2025-09-09 05:23:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd6a07cc-d722-3f25-a763-bc7b9b6ed5a2 | -13.03898 | -48.03535 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| edf0b74a-8ca4-3ad3-bf1e-965f894d91d1 | -13.1313 | -54.92318 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| abc20cbb-f872-3d26-b032-0e124b1cabee | -15.767 | -53.53533 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d2120da-bca5-353f-a274-f9803646aa51 | -6.39824 | -58.20206 | 2025-09-09 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c069708-f99c-37a2-8cef-8622b4538526 | -3.32535 | -54.91273 | 2025-09-09 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae51d72e-668b-36bb-9b9b-83aec4a99e73 | -8.01515 | -63.48896 | 2025-09-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da67e5f6-6a2e-3026-a49c-127090fa35bb | -4.99501 | -56.25985 | 2025-09-09 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 842a5638-4d0b-3df8-b9a3-5993e2502ee2 | -12.63835 | -56.97969 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4e77b17-dca7-3b12-82f7-28c3ebc52953 | -9.10088 | -49.51904 | 2025-09-09 05:23:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33e00758-85c5-3a1c-933e-80034f48fd9e | -14.71777 | -60.24965 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32a82f89-0a5b-318f-af68-4b29657162d5 | -8.3991 | -49.10628 | 2025-09-09 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6adde51a-1422-344a-a142-4cc22dfff242 | -12.82218 | -52.9397 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c30487d1-4b5a-3c3f-80ba-dcd71f3acbdb | -15.53238 | -48.38814 | 2025-09-09 05:23:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3085eae6-231d-30cf-8156-ea6b4969a877 | -7.39939 | -61.63619 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7de3e5da-9370-30cf-8223-b377ca9704a7 | -5.50299 | -60.1394 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec703458-3950-3737-98af-c570b1d34891 | -12.43033 | -63.88979 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48341df7-6e94-3af5-b9ec-d1c028f7ef57 | -15.1079 | -52.35248 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99e7f584-bd66-3cf1-b31a-2dd048be903c | -13.63516 | -55.02643 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef8ee529-5035-392e-86b0-3d3c0bea3344 | -15.82954 | -52.26169 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09c5dfd1-0ef8-322d-a8c9-807089172864 | -8.48379 | -48.27075 | 2025-09-09 05:23:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 627b4b7e-3c4f-32db-828b-27ed7942157e | -15.81835 | -52.26907 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 87d68892-b13e-3f59-a9de-97fd62e0bcf6 | -12.93319 | -54.76111 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76cf5e18-1e7c-39f5-b50a-34637cc8d934 | -12.89938 | -47.9948 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20b37909-356a-303f-860b-00f91b7947a0 | -12.93786 | -54.76176 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18c5096c-afdb-3c53-8830-27f8f4c94248 | -12.92658 | -54.77536 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac69d1a6-1cb8-3267-a78e-aed6e2c38c24 | -14.44341 | -53.23644 | 2025-09-09 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb37ee58-b08a-300d-b29e-ceb96b925116 | -15.82188 | -52.27805 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| afa478eb-31b8-304f-8379-9000932e9d4f | -8.09242 | -54.75095 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5043cc8b-c201-3988-9e61-444479a2a801 | -10.33107 | -47.72906 | 2025-09-09 05:23:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63936b18-668d-3571-88c8-146f83f94af1 | -12.43777 | -63.93002 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5ad81e8-b9bd-32cd-975e-363f571adbc2 | -15.78355 | -53.53117 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87d4178b-8226-3e91-932c-d76fd3e72d85 | -12.62879 | -56.96012 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc3d207e-5284-3add-a257-923a9da85b33 | -12.8872 | -47.97292 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 030ab7fd-b624-3e28-85b2-db92f6b195ff | -7.51753 | -61.66223 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccce3dc1-e1d9-313f-9055-39731b2add85 | -15.26658 | -53.80784 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78307aca-1371-31ed-be5d-f15164479ac7 | -6.95023 | -62.92849 | 2025-09-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b685670-5acb-36a6-9187-fde0c9bc4866 | -6.54746 | -54.99335 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c760b73-61fc-323b-af0f-c3280d2764d7 | -5.41397 | -51.53751 | 2025-09-09 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5740f0ee-9fc8-3da7-9ca8-b8b7153f1891 | -15.78334 | -53.57692 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3cbb71c-800c-3646-8d16-d5400691be4d | -15.77188 | -53.5394 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a6e864b-abc4-3506-9800-f3051785b154 | -7.51974 | -61.66981 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2278488-3d7a-30c2-afb8-9de3b5b5aed9 | -13.93683 | -48.24218 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7b800e40-fc79-3f37-bdb5-ce2851c60251 | -10.28778 | -48.81981 | 2025-09-09 05:23:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d4410fe-1363-3a04-99d3-6fbb52eb1053 | -15.78435 | -53.52439 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dc52fa9-8b59-3cb0-8ad8-801a688d855c | -14.91194 | -55.8402 | 2025-09-09 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e45cd244-8ee6-384d-bf63-57f763ac4119 | -14.89022 | -55.83234 | 2025-09-09 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e35842e-736c-36dc-b438-b5a44f7aca2e | -6.8691 | -47.90997 | 2025-09-09 05:23:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4cac3644-a297-3414-b55f-83e6ba710713 | -8.08748 | -54.75449 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 948c9c50-3132-326c-a070-b8a8370dc07f | -14.72524 | -60.24697 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e4d87d8-fb8e-30e9-8209-fb174dff7e50 | -15.26431 | -52.36277 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e945ee8f-fe64-3531-89e4-6e68a58a7327 | -15.74668 | -53.52598 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d5e74ab-ff89-3d39-b357-faae4707e482 | -14.5422 | -48.75551 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 19798bf9-704b-369e-bbd8-94b77f744d24 | -14.52896 | -48.74644 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 129b5fe1-3370-3c1f-a827-e30ec1eaf097 | -3.66613 | -59.14216 | 2025-09-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbf34acb-0ef9-3371-ac22-791420278d61 | -14.35284 | -60.31085 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7c83eaf-dcd1-396e-a968-d41c7fb9238d | -14.72179 | -60.24636 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d2d3879-e960-3f34-8972-435cad5eaa1f | -15.83531 | -52.26204 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8afc382e-c0a6-3e6f-a3a1-f22690d65a82 | -7.90259 | -61.78162 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82a13e26-f68a-359a-9cac-4ef678a3ad87 | -15.25809 | -53.79106 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b27225d0-fa08-3ee7-9621-7095a0ef80d6 | -15.25293 | -53.79042 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78d3319d-e9fc-350d-a159-89e8f43ace37 | -3.32133 | -54.91212 | 2025-09-09 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3676aa7-1ed9-366c-ba9f-20d3b4291814 | -8.60671 | -54.66892 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90df842a-6208-32aa-8caa-bc342fa730d8 | -7.39606 | -61.63566 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d8e0011-48cc-331c-8dcc-70779130d384 | -15.2559 | -53.80989 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6b8c148-58e5-37bb-88f0-accfda6c02a1 | -12.64236 | -56.98025 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43e12837-2e56-3c43-b535-0eb9d45e0020 | -12.64186 | -56.98383 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d360f3cc-3cec-3122-8879-fc59e569a7f4 | -7.33628 | -49.56405 | 2025-09-09 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24582090-2fb2-3a8f-965d-89ea4595883b | -12.88338 | -62.09535 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f5f6889-8515-31e8-aa39-fdc55dadd218 | -14.3704 | -60.30526 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e5130cb-4df0-39ae-b305-ae878ec1ac71 | -15.25663 | -53.80359 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31c3f82c-d417-35de-8803-43b03b488d44 | -7.5998 | -61.59288 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22ece6f8-71e6-35c4-b156-392a2018b162 | -8.40614 | -49.10194 | 2025-09-09 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 689ff423-9813-3c27-8853-905f7a7084b6 | -12.93735 | -54.80197 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78bd0cbc-efe7-37c5-89a8-82ff24320e37 | -10.28112 | -48.81913 | 2025-09-09 05:23:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 611c9024-24a1-3e92-8d6f-c0ee971613db | -6.55221 | -54.9901 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 443a964d-691f-3567-8c3a-29a1992c9a5e | -5.5013 | -60.12852 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31af72a5-5b4c-343e-a9c6-287144b4e11c | -15.24559 | -53.80873 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cf147aff-0b04-38a6-a60e-5cc1a2277e27 | -15.71837 | -53.53952 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10e8d054-3b99-3132-90ae-6dd713f5f98a | -7.49005 | -54.95104 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c1b89e5-306b-3f43-9ae8-c3fe9fb48fab | -14.16962 | -48.99401 | 2025-09-09 05:23:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1bfffc2f-bfb2-3c3b-b171-a63366bf1432 | -4.69993 | -55.67747 | 2025-09-09 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7a3c572-9344-3eaa-b7b4-28f0c16cf448 | -12.87342 | -62.11543 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c47f2004-1117-3fa8-9b11-e13491d7b9a6 | -7.12467 | -60.73251 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5633502-1a27-306b-9d54-e9f9deadbf69 | -15.26995 | -52.36367 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bb82122-81f6-3e9a-9ac9-1005dba9b2ee | -12.6278 | -56.96729 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73ab0494-9fe3-330f-8b71-a0c24e1ba318 | -7.59925 | -61.59639 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f20ff1a-cfdc-3a81-8c5d-db5edb668245 | -12.81649 | -52.94238 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df092f32-77eb-3764-a2ab-429c4b5d97cb | -12.82176 | -52.9431 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9927d66b-718a-3d7a-b9c3-f0c92e634e6a | -13.95082 | -48.24688 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README60.md)
