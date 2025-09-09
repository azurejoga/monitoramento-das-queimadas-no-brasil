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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dee31a3-c627-3381-ba54-e541bdda2740 | -15.78359 | -53.57602 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49ff15e2-fe70-30b0-a6c1-fb3e329c18af | -14.60346 | -52.11772 | 2025-09-09 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fec93ace-a7f2-323b-a690-45fe29a9b5f9 | -12.1949 | -53.88334 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32e034d0-230f-351a-b8e3-f941c620f382 | -11.89639 | -64.99581 | 2025-09-09 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a5173ed-a68a-3a36-ab8c-e11844c8d771 | -12.19418 | -53.88894 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a8c1f97-3f70-3463-b6a9-ed6070aa1710 | -9.09461 | -49.51823 | 2025-09-09 05:23:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f9ac168-0cae-3d15-bba3-cf99a6175750 | -14.91252 | -55.83561 | 2025-09-09 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 02a1c8a5-1e7c-3605-bf88-61ce3c527428 | -13.94426 | -48.24015 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5e4744a2-7c02-3162-9ebc-30229168771b | -10.33808 | -47.73051 | 2025-09-09 05:23:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62346cd1-62fc-3650-a05c-0f5013ba1912 | -14.36368 | -60.30897 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d50b607-1655-3e51-a36a-75a29b889741 | -15.78839 | -53.53558 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b3eb5c0-ecc7-3e95-af29-f238af6fe3a1 | -14.17589 | -48.99268 | 2025-09-09 05:23:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9888ce8a-e0f5-330a-be1f-4c7904937c75 | -4.40723 | -48.94567 | 2025-09-09 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac4f4bcf-6bd5-374c-a171-ad2bdd0234c3 | -14.53668 | -48.73984 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 378c8c95-1747-3b9f-8a82-218ba4562e57 | -12.92995 | -54.78596 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a01a7dc2-05a0-31af-aa1c-0761ce4b87be | -16.06928 | -50.4844 | 2025-09-09 05:23:00 | NOAA-20 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f59b1fdb-f4e4-3950-b757-808d0ad4f836 | -12.62378 | -56.96673 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e22b3d5-062c-3630-9c6f-99079aed3cf3 | -15.50928 | -52.7635 | 2025-09-09 05:23:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c69f72a-cdb7-3f39-b404-9f78661009a1 | -8.27032 | -61.45666 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c574044-7d44-39e4-bd3b-ab584aa1337a | -3.3299 | -54.90981 | 2025-09-09 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d5992f4-cf10-36c7-a0e7-8c258de9f4a4 | -13.9546 | -48.25013 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dc571739-9c29-3fe6-87f4-9c0da5105b4c | -13.94798 | -48.24432 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e0b2a96a-eb9e-378a-b062-e3059eb76710 | -4.9922 | -56.25322 | 2025-09-09 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1451d8b3-c960-32c1-ab39-93b4dcd58b7f | -15.24868 | -52.34876 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27b22c2a-2e47-3a27-a945-6b744b89a41c | -14.78742 | -48.23249 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c49a4cc4-7705-3450-ac29-1ab2ef79b4c1 | -10.33578 | -47.72793 | 2025-09-09 05:23:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb3563ae-db70-3bf8-97ed-ac44a2925bc4 | -13.69588 | -58.5334 | 2025-09-09 05:23:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 888e4fcd-b458-32e1-a898-175959fc67b6 | -15.25432 | -52.34962 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8adcf054-c29b-3b14-b753-153ac752f1dd | -7.3418 | -49.56953 | 2025-09-09 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 409ad3ea-b3a2-3dbf-96e3-867df4187c59 | -15.81798 | -52.27256 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5fe010ea-d4ac-3411-abba-db0883ab281a | -15.82631 | -48.95302 | 2025-09-09 05:23:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ceb2a3a-c738-3835-919e-c71f6040ddbe | -14.17018 | -48.98838 | 2025-09-09 05:23:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59235e03-e028-3d68-8b2a-12551ace627a | -12.20818 | -53.8964 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f25aaf89-637c-30aa-a855-c1d6066a3feb | -12.63633 | -56.96481 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 46657028-3b14-3f1a-be7c-aa5eb5caa6a1 | -12.95253 | -54.75865 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 62999338-aa7f-396e-a6b2-dde350031119 | -15.81734 | -52.26676 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7817182-1ebd-36cf-be2d-b3b4575a631c | -12.64587 | -56.98437 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c54a89d4-29c3-35f7-a711-d563f61e95c9 | -15.77714 | -53.54021 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8bf7a457-9935-3523-8cf8-5c0aeda27c1d | -12.63483 | -56.97557 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbd00b0c-73b8-3531-952c-4a8a5d2ff445 | -13.95812 | -48.24619 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c64b95bb-d8ea-31dd-bb2f-b6f8c66d021b | -14.16892 | -48.99285 | 2025-09-09 05:23:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9b0e779-0b56-3122-9a98-352e5a904170 | -12.82662 | -52.94717 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffba3611-bb2c-3800-bd50-8f250516a041 | -14.87798 | -55.79933 | 2025-09-09 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0a9c2bf-e362-3cf3-9b5c-f1397c58014c | -15.26556 | -52.35174 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 118eb0ed-cd2d-330b-8948-ac56d99e6a31 | -15.83134 | -52.25614 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53c6ea93-3df6-33ba-a17f-4859c25851d7 | -13.02078 | -48.03932 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2d1bd58-d0fc-3732-b28e-6b79ea2ad648 | -7.87667 | -61.32585 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae215588-c8e4-3108-a833-d647226507c8 | -7.82651 | -63.57725 | 2025-09-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 249d9992-062b-3f49-9577-b20e5bb10cc2 | -12.64688 | -56.97722 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 019953f4-fdc2-3c15-80fe-a4ed2851f662 | -6.40172 | -58.2026 | 2025-09-09 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3dcddba-340e-39cb-a503-d99900d5a9d8 | -12.87233 | -62.10078 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c0d5288-f278-3a21-b53d-8a07ff53f1cf | -6.94899 | -62.93613 | 2025-09-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ef2ab85-f0ad-3267-b674-689988e00252 | -14.53525 | -48.75433 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91aa560f-0316-3845-9c24-cf2a54146972 | -12.87564 | -62.10132 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df145d77-7920-39b9-9d26-3fc8e327f961 | -15.81241 | -52.25888 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 907667f5-e136-3703-bd8a-7dbf6b9ae031 | -14.3643 | -60.30492 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d6745b6-c4b4-31f5-bbc8-f597e3f3c4a9 | -12.87122 | -62.10783 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 479d743a-970e-32e7-bb55-e4d5df2d4ccc | -14.5486 | -48.76221 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a463cb37-d65e-3e36-a959-3f457bc25c87 | -14.36295 | -60.308 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe271971-1270-3096-8e9a-1f0283ba3595 | -12.87289 | -62.09725 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4694393-d75f-31a4-a9b0-a98d49451cba | -12.94136 | -54.8075 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 987e302f-9162-3317-906f-c857dd955b43 | -12.83842 | -52.93848 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f03b9b78-dad5-35f1-b505-94290a933d87 | -15.54099 | -48.374 | 2025-09-09 05:23:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a09e992-ae4c-34f7-8ff3-d863ba8b3d1a | -15.2684 | -53.79228 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3afeeb25-8810-3457-9458-6027b877a88e | -9.2745 | -56.8982 | 2025-09-09 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f42e248d-6c92-3c90-9a0a-9b24ca2f5c08 | -3.59303 | -58.54199 | 2025-09-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 171f3c74-5e20-33be-bbcd-921b8786e1d0 | -12.86846 | -62.10376 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a025e28a-7c7f-3a7a-92de-7afa7d3f2ac4 | -8.05672 | -48.62943 | 2025-09-09 05:23:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.1 |
| efc97f63-7454-3dee-8eea-0424cd60cdd1 | -16.43634 | -49.2967 | 2025-09-09 05:23:00 | NOAA-20 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcef6182-d006-3add-9b88-f0ce4f5d6312 | -14.37441 | -60.30193 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f204552-784e-339a-9e00-3ba4aaaefd03 | -12.89322 | -47.98458 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e134cdd1-68cf-3299-8651-714284f251cb | -15.70045 | -49.90113 | 2025-09-09 05:23:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d92bdf8-b4a0-3be2-9307-0e8ac20977c9 | -12.95187 | -54.76366 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 691765f8-2303-3aca-9820-3fd97a4ccd7a | -6.4046 | -58.207 | 2025-09-09 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad1b99d5-7ea3-3425-8023-be91642d6c45 | -12.88614 | -62.09942 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cf62ab4-2cd5-3550-9462-31393fdbf6a8 | -14.59162 | -52.1202 | 2025-09-09 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0e3c61d-3b2e-3c80-958a-a6406fce76e1 | -8.2371 | -49.5465 | 2025-09-09 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 455f00f5-cc1a-3d59-9ac2-3988e2264f0e | -12.85343 | -52.94716 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84f87409-57d8-39c6-adaf-21ad84ad4384 | -12.90328 | -62.07713 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39816421-ff64-34de-a300-3ec3102747f2 | -12.19836 | -53.89513 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| a042ba8b-9761-3ee9-99a9-71819c26e502 | -12.94786 | -54.75799 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 354fac50-bf1d-3677-b699-2a66e4a65da3 | -12.87066 | -62.11136 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7308bd2c-6142-39a2-a16b-c3006822eb79 | -15.524 | -48.39997 | 2025-09-09 05:23:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f2ff3e9-bfbd-3aeb-8302-69401d246099 | -14.53048 | -48.74689 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1b2d4f0f-866d-3d91-bd81-05160963e50a | -4.99599 | -56.25374 | 2025-09-09 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| faf57e3d-04f0-32e9-b418-8295bfce6997 | -14.35565 | -60.31554 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3d2aaab-5749-3d2c-b086-2d2d53fca7ee | -7.47432 | -61.59048 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01bd3e64-badc-373b-907c-95b097ad757e | -9.85273 | -47.79797 | 2025-09-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27e7124b-46ab-3932-a634-7d9d19c0641b | -13.93767 | -48.23357 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6a2072b1-ef0e-357f-8870-dfe4cece02fe | -13.01738 | -48.03384 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 033eb73c-92d5-36ef-908a-ca9c008bacc4 | -15.81772 | -52.26339 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| baf799c6-8e01-3745-a6c4-3605808b9303 | -14.16952 | -48.98723 | 2025-09-09 05:23:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f544700f-ec83-3286-b1af-0d8923bc45db | -12.90659 | -47.99527 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adf21f53-7858-3f96-9c75-4475f2ce6b6f | -3.92624 | -56.06295 | 2025-09-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2824a27-85c5-3725-bc23-b83f8ed3f19f | -12.83759 | -52.94515 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 234b5df7-63b0-3471-8632-7427f4a2078c | -15.82563 | -48.96068 | 2025-09-09 05:23:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dd6770e-8e59-3799-ab53-a2497b78a2ed | -12.64638 | -56.98079 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57db055d-b933-3f69-8992-e6cb7a0a9a17 | -12.83801 | -52.9418 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e4c4d70-5258-350b-9980-225c312dece9 | -15.82333 | -52.27695 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0cc6063a-3a6c-38ca-ac7f-8c8b9dcc23ee | -15.83089 | -52.26038 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README58.md)
