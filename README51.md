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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e01d995-77e5-334d-ad0f-a44c3c5947bf | -9.34575 | -49.54649 | 2024-10-30 04:21:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 861ac833-5c45-33b9-8196-0f673658bfc1 | -9.30734 | -49.40668 | 2024-10-30 04:21:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32afaf50-16bd-3dbe-937b-3c94c1d012ff | -9.04895 | -50.00628 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fd71b822-28ed-3739-821c-3213e177d272 | -9.04808 | -50.01138 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b422d265-31f8-39d9-88b4-200911280bd9 | -8.84854 | -49.85854 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecd28f6c-ce71-3e84-af14-44584a091707 | -8.84462 | -49.85789 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 40e1c2a1-7f5c-3ea8-9883-2c62a3672249 | -8.84375 | -49.86295 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0c5c99dc-e349-39f0-9f12-0dc8ca7de3c2 | -8.65594 | -49.14162 | 2024-10-30 04:21:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5094afab-3947-3d30-8830-b0a51ba3e69e | -8.15197 | -49.29736 | 2024-10-30 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e566508-9987-3c81-bba7-cecc9d09362e | -8.14815 | -49.29667 | 2024-10-30 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93573541-cc92-3229-b519-689b16d8a173 | -8.04751 | -49.66116 | 2024-10-30 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72eba17d-091d-3860-ae99-aa252f167561 | -9.94573 | -48.95839 | 2024-10-30 04:21:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b999bdec-805a-3685-9553-e7d0db828e6e | -9.94501 | -48.96274 | 2024-10-30 04:21:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6d3ca26-b8e9-3c6a-9ce1-6e8cd43439aa | -9.94135 | -48.96216 | 2024-10-30 04:21:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d98c8297-6402-3bc8-9986-565db0eeebba | -9.53897 | -49.18676 | 2024-10-30 04:21:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 816f630d-c796-3d63-b2df-58d8bd241982 | -9.48505 | -50.2885 | 2024-10-30 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64fad866-518f-3a9b-81cd-709afe9df415 | -10.34281 | -49.65472 | 2024-10-30 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 95110264-fd2f-30b6-bd7f-8c93cdfea456 | -10.34202 | -49.6594 | 2024-10-30 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a154f8c0-40c2-34ab-b05e-4e7e4bcaffbc | -10.33983 | -49.64938 | 2024-10-30 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0aea9c76-a63e-3dcb-b857-e7834d54ce6a | -10.33903 | -49.65404 | 2024-10-30 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 75e3e337-79da-3ef7-8252-284507ae9999 | -10.33824 | -49.65873 | 2024-10-30 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fca099b3-f6de-3987-87d9-2453f73194f7 | -10.19937 | -49.14659 | 2024-10-30 04:21:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ad5ebe5-72d4-39fd-b4d5-ad8f0761a6f0 | -10.19861 | -49.15104 | 2024-10-30 04:21:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 548d315b-f07d-3d7d-b537-e3995230f609 | -10.19493 | -49.15041 | 2024-10-30 04:21:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c17e4f7-cccc-3108-9c6d-d6af87bb5bde | -10.15795 | -49.32367 | 2024-10-30 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22d0ad61-e9c0-3d57-b9fd-d60359e149a0 | -8.51483 | -50.77442 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d6eb79d-44a2-36b0-9d4f-a9bb66ccc9b7 | -13.36019 | -52.40025 | 2024-10-30 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c381efa-e5c9-332a-8eda-07749cc5b91e | -11.22315 | -52.73515 | 2024-10-30 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b32bbe0c-2a26-3d16-8c67-d97de482354f | -19.94551 | -44.71727 | 2024-10-30 04:23:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 825ae605-21ee-3f04-8d72-10b247561af7 | -21.8338 | -44.79999 | 2024-10-30 04:23:00 | NOAA-21 | CRUZÍLIA | MINAS GERAIS | Brasil | 3120805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9dcaf91b-6202-3018-8680-257696b06878 | -20.58482 | -46.46763 | 2024-10-30 04:23:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12e495fd-9230-3e17-91a9-780d88ecf6a7 | -19.23712 | -48.46775 | 2024-10-30 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dff3437e-d46c-3e75-9c36-54cdd31497b4 | -21.11478 | -48.64677 | 2024-10-30 04:23:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77ea6bbb-344a-34e1-a7ad-88e1b8acf5d0 | -21.11419 | -48.65049 | 2024-10-30 04:23:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| da4c52fa-2ad8-37f9-906c-b7fe17504845 | -18.95983 | -52.39381 | 2024-10-30 04:23:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d146c1c-eb26-37bd-bbbe-634008214bf4 | -18.95962 | -52.39588 | 2024-10-30 04:23:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ec6e3e4-83f7-3f11-94b4-1922614f700a | -19.60041 | -52.25309 | 2024-10-30 04:23:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fec0617-8a74-34b3-838a-19a64bcfa715 | -20.03151 | -54.67175 | 2024-10-30 04:23:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 350314a5-a245-33e4-8348-7751ba75e1c3 | -19.48155 | -56.63237 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ad389ceb-61f4-3d17-bce0-6549e1c9720e | -19.4809 | -56.63546 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b9bb1324-e245-3861-86b6-8b189650e83f | -19.48025 | -56.63856 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f3706263-189b-34dc-8a2e-424c08ef2531 | -19.4796 | -56.64165 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 20d5a526-8a0a-3dad-a9c7-4b95f4a5a8c0 | -19.47895 | -56.64476 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 28e81fc3-b504-37fb-a5d4-7135c05c2418 | -19.47216 | -56.627 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7e0bea6a-e801-31b9-8a08-664679f214cd | -19.47151 | -56.63009 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c5ba0dd4-b265-3df4-aff6-80f9ad496375 | -19.47086 | -56.63317 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7cb56c84-b1dc-371a-9838-a86261663d39 | -19.46714 | -56.62584 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fa1b1f36-d4bf-348a-9d98-dcdb554775bb | -19.46649 | -56.62893 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2f22f68c-b513-36b6-8a64-d221eaed0cd8 | -19.46584 | -56.63203 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| bb22005c-344b-3b3a-b53f-a1de0897ce5d | -19.62533 | -56.69402 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 620d020a-a3d5-3457-83ac-8fdbd66bf096 | -19.62468 | -56.69712 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 596c4dff-5c9d-37ef-806d-8c99815a9bf9 | -19.62404 | -56.70023 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 906a8eef-4ed2-347b-908a-e467aeda341d | -19.61966 | -56.69597 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 40fcd75f-8cf3-34ae-a72e-990b2a5883d6 | -19.61901 | -56.69907 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 843cc12d-8a45-3317-871f-f5670f3dc83a | -19.61837 | -56.70218 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f1ce238d-984b-3383-a40d-6880088a6f75 | -19.61528 | -56.6917 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 89ef60b4-e438-32dc-aa86-32540ab9f0e2 | -19.61334 | -56.70102 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| debbef25-9f3b-36a2-9a10-e287ac187da8 | -19.60896 | -56.69676 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b195323c-1a25-3f97-b143-7f86c807a00d | -19.60831 | -56.69986 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d3c34f8a-c43e-3702-abdb-1c63499a203d | -19.60329 | -56.6987 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 04c577ec-2080-3bcf-8534-e5e2be57352e | -19.60264 | -56.7018 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 57a06f17-330c-3a5c-9032-67aa7c44cc1c | -19.59826 | -56.69754 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ef0afc8d-890b-3018-817d-8aa5149a4397 | -19.59761 | -56.70065 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 49c28923-5d47-39db-932a-98e2eaf05dbb | -19.58806 | -56.62065 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 576216bd-2829-3313-8320-d0b0f164732c | -19.52651 | -56.69483 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e68e8fec-5159-3bdd-9648-b261949b4bee | -19.52587 | -56.69795 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 272f979c-0c18-3c23-bbb9-b6cdc2d306d4 | -19.51189 | -56.58764 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6b568434-0788-3647-bcf4-870b34892b8d | -19.51125 | -56.59072 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c7d5f3d3-a0c7-3f58-a789-247fd2b8f2f1 | -19.51061 | -56.5938 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e353bee9-4f3c-31d7-ae4c-2c31eab97210 | -19.50997 | -56.59687 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b02ab359-6c71-3879-a583-2d80c478dd98 | -19.50766 | -56.68394 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 5b32588f-e0d5-3750-b249-e96e18be3561 | -19.50702 | -56.68706 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 735d699f-053b-361f-bcba-3fc812c9a383 | -19.50688 | -56.58652 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1da42080-d664-3f62-9258-e131698e32fb | -19.50637 | -56.69018 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 642c8dab-3d2c-3206-9348-18d5cac431a4 | -19.50624 | -56.58959 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| aab07170-4edc-3a3a-a3da-7a242b7b987f | -19.50573 | -56.69329 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c4b659a9-53f5-3fc2-b9ba-bc9f302ac521 | -19.5056 | -56.59266 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| ea5fb6a0-9692-3ef8-9d19-66a0e9695a84 | -19.50496 | -56.59573 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1d2dd3e6-395c-3e05-8d06-8e34437780c8 | -19.50263 | -56.68279 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 810af372-ffaa-3efc-8457-2bca7cb6cdba | -19.50199 | -56.6859 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 54eb265a-6088-34e8-80b1-ea348865628f | -19.50188 | -56.58538 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| defe29fc-bc15-3a98-8e7c-faa349f82394 | -19.50124 | -56.58845 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7354eb6f-141c-3b72-8510-37d86c442c29 | -19.50069 | -56.69212 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9fc3a7c2-9a3a-3a76-8f9b-7bc25c7b6ff4 | -19.5006 | -56.59151 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ba367c0d-7359-33e6-ada3-503075fb84da | -19.50004 | -56.69525 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ea458505-b339-3558-b77f-fa51da2a33de | -19.49996 | -56.59459 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a41fe967-ea57-33be-95bc-ef52d1dd8edd | -19.49932 | -56.59765 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a843c956-026a-334c-9c39-0ce0d80725de | -19.4979 | -56.62963 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2bc90628-238d-354f-9beb-e2a8f2b9e37b | -19.49631 | -56.68785 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b7ffc424-d760-34d5-bfef-87130648856d | -19.49566 | -56.69097 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b4a6d076-a23b-3166-b712-aa618233396d | -19.49559 | -56.59037 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 506d9027-d43f-3537-9e7e-d8c2cccb1f9f | -19.49436 | -56.69721 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 25032a5e-53e4-3d85-94d4-bc5335a0a9ba | -19.49417 | -56.62229 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a4c33015-2056-357e-b77c-fd78ad5d5e49 | -19.49371 | -56.70034 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2dcf1045-b9f4-32cd-81f2-edec3be78004 | -19.49353 | -56.62539 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 60d0e6f4-8e1d-3505-a6e0-89647bb1ea7d | -19.48997 | -56.69294 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5072cbc4-a122-350b-806b-6928793fbb08 | -19.48932 | -56.69606 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9ca9e5ae-f180-37c5-8f59-172e0cf66c5e | -19.48866 | -56.69919 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 011f41cc-5045-354b-bf94-3288359b8327 | -19.48705 | -56.65639 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 417f99eb-3e84-348d-a209-c934ad8bab7f | -19.4864 | -56.65949 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |


[Clique aqui para ver as próximas entradas](README52.md)
