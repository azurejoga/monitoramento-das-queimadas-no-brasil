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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 566d6281-a819-31af-8cfd-0b4bf34d88cb | -5.9901 | -44.1297 | 2025-09-07 01:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d195ee8e-813e-3436-81a6-bf6edefd42d3 | -3.5995 | -47.5142 | 2025-09-07 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| c7bae87a-4e29-33f9-ba00-a2e2d20c2371 | -17.3636 | -42.6532 | 2025-09-07 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| cea87af2-1bcb-3f5b-92f9-888461a39f06 | -11.408 | -43.6283 | 2025-09-07 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f63119bc-00a0-3091-ada6-b7e593c5db16 | -9.1987 | -62.4156 | 2025-09-07 01:35:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 52267435-9898-3ad6-acb6-e3faa2d82f50 | -9.1954 | -62.402199 | 2025-09-07 01:35:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 608eb0b1-ea1d-3b46-84af-08319c9b29c5 | -12.1511 | -63.953899 | 2025-09-07 01:35:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7e1074fe-8bad-30e6-80e6-ad32d4418f53 | -9.4255 | -63.223499 | 2025-09-07 01:35:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 03741352-a0bc-3d70-b7e9-acc7d32de6a5 | -9.0931 | -65.4729 | 2025-09-07 01:35:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3ce3722-ff1d-3828-b837-292e40af8dc7 | -12.1609 | -63.9515 | 2025-09-07 01:35:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5cd0a9e5-c41f-3073-b34b-57ccf67c0852 | -9.1792 | -62.420399 | 2025-09-07 01:35:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7dd8eeb3-1d06-3eb7-81e0-43bdbd9ce490 | -12.0991 | -63.693401 | 2025-09-07 01:35:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aafd8610-4ad5-3cde-8fbf-32bf0fdf58c0 | -9.091 | -65.464104 | 2025-09-07 01:35:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b84bd79c-8800-3560-9469-8ccddd50c024 | -9.1759 | -62.407001 | 2025-09-07 01:35:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 36368039-d22c-3a68-9e38-bc8690ea9045 | -6.0086 | -44.1513 | 2025-09-07 01:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 28da716e-48c6-3d2a-b663-f49178da9a08 | -19.4898 | -47.7646 | 2025-09-07 01:40:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4b87fd37-06a9-3497-b5c2-cfe71644bf5c | -11.408 | -43.6283 | 2025-09-07 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 4e411138-16e2-3eff-b250-9d29fe77651d | -13.9156 | -53.9861 | 2025-09-07 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a3bb0e6a-78d2-3f31-8bdc-c7b61d5f2929 | -7.7404 | -48.8204 | 2025-09-07 01:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9a5d6b85-c6e6-3440-8e7a-c7ac02e60da0 | -3.581 | -47.5149 | 2025-09-07 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 8084a3b6-b5ba-3685-98a9-d247e41bd698 | -3.5995 | -47.5142 | 2025-09-07 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| e2aa7862-e946-312c-be75-040f8ec34622 | -17.3643 | -42.6284 | 2025-09-07 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b67886af-66b3-3ba3-b907-33d984f85013 | -19.4904 | -47.7413 | 2025-09-07 01:40:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 47.5 |
| eebb58e4-3a68-315d-be41-94d6d771f0fb | -7.7591 | -48.8189 | 2025-09-07 01:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 77.4 |
| c2aba6fb-6092-3f6b-99b3-a7ebb7a794a6 | -10.8066 | -47.7256 | 2025-09-07 01:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 431121e7-4a08-32a3-91a3-f59e3eccc60a | -5.9901 | -44.1297 | 2025-09-07 01:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b1d35be7-9bff-3384-a60f-f6e7c3b84392 | -17.3636 | -42.6532 | 2025-09-07 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 97d16e16-0244-3efd-bdba-37553b0e1f25 | -5.9899 | -44.1528 | 2025-09-07 01:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 278.3 |
| f7a65d18-72b3-3321-bf38-34ca366085c8 | -19.8725 | -57.89973 | 2025-09-07 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 0d433efe-de4c-3717-8c44-15a62abc87b5 | -12.35947 | -63.63981 | 2025-09-07 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e82a2935-894a-3463-807a-fd6a27972741 | -9.68235 | -63.1705 | 2025-09-07 01:49:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 58b75349-a84d-3269-85e5-eb43e9321c2c | -12.62171 | -56.99336 | 2025-09-07 01:49:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 40088cfa-910d-33de-a7a9-d5f93180aeed | -12.41792 | -63.89399 | 2025-09-07 01:49:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| cd1bb5d2-a55a-3edb-afa5-1e2268bab070 | -9.3464 | -62.34964 | 2025-09-07 01:49:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b866f727-8ec4-3885-80aa-40c9a0215f42 | -9.34988 | -65.41709 | 2025-09-07 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fc7aeaff-3c5c-3f5f-886c-45dd4f660800 | -12.61193 | -56.98975 | 2025-09-07 01:49:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 555f8bbb-68c5-317f-b208-19840b8abe70 | -9.68886 | -63.17589 | 2025-09-07 01:49:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8b5dbc59-ef75-3ac1-be86-89648464d590 | -9.35129 | -65.42695 | 2025-09-07 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bea8351d-dffc-35cf-b6e3-cd71e9a43a8c | -11.77721 | -60.89148 | 2025-09-07 01:49:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 59d81c97-7ea0-3743-8945-b985953e97e1 | -12.41957 | -63.90498 | 2025-09-07 01:49:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2c3153a1-7fca-35fe-aa9c-6d610d854fbb | -17.3636 | -42.6532 | 2025-09-07 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 1862a49c-c748-3d10-b7c1-0300609fbe9d | -7.7404 | -48.8204 | 2025-09-07 01:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 6c81f8cc-675a-39f3-9222-dc4206aa8038 | -12.967 | -54.7705 | 2025-09-07 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 6cb98c99-72b9-38c4-8992-d775a276a272 | -5.9899 | -44.1528 | 2025-09-07 01:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 244.5 |
| c180354f-c888-3335-8a4b-fc05937abd14 | -17.3643 | -42.6284 | 2025-09-07 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 9fc7f87a-75e4-3844-9eab-ba5f1b458fc5 | -7.7589 | -48.8405 | 2025-09-07 01:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 5d74eb6d-78d1-3a16-b340-c0cb53f5fcb3 | -6.0086 | -44.1513 | 2025-09-07 01:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 83fd41b8-2bbf-353e-98fd-8fdb21374139 | -5.9896 | -44.1758 | 2025-09-07 01:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c676e768-3841-30f7-a0e3-5cb9ee38c0b1 | -3.5995 | -47.5142 | 2025-09-07 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| f936bdfa-c319-3561-abbe-fcc236870645 | -13.9342 | -54.0256 | 2025-09-07 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| c7b5d56a-1d80-3d0e-8906-142eb8416a3f | -7.7591 | -48.8189 | 2025-09-07 01:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 143.9 |
| b628feb6-18c9-386e-b409-5acd914703eb | -12.948 | -54.7724 | 2025-09-07 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 275.5 |
| fc51f2d3-0d50-3b9d-818c-3d213943af66 | -12.9477 | -54.793 | 2025-09-07 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| ded50ac3-33b1-3f60-9b95-51255f5cddb1 | -11.408 | -43.6283 | 2025-09-07 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b9d22364-9820-3058-920a-e8209b11f62c | -5.9901 | -44.1297 | 2025-09-07 01:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 295d977d-2f10-36d6-b76e-fff61345b389 | -5.9901 | -44.1297 | 2025-09-07 02:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 89577209-059a-31ae-9025-a0000c57e793 | -12.967 | -54.7705 | 2025-09-07 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6a42e29c-f838-3518-b895-b0c521bee088 | -13.9153 | -54.007 | 2025-09-07 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8348a277-d17d-3612-b6dc-e695e92b2672 | -3.5995 | -47.5142 | 2025-09-07 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 5b67d848-b6d9-3814-a7e7-a7f161f3421b | -6.0086 | -44.1513 | 2025-09-07 02:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| bdafefa9-45ce-3f04-9d60-4efb2b85d123 | -5.9899 | -44.1528 | 2025-09-07 02:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 6341ddbb-9407-3f4b-bfc5-1d76c1935ea5 | -12.948 | -54.7724 | 2025-09-07 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 280.0 |
| 868aff66-e0ac-3902-8f4f-1897a938f807 | -3.581 | -47.5149 | 2025-09-07 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 82f4adf5-019f-3104-bf3c-6a3d2edd2f63 | -17.3636 | -42.6532 | 2025-09-07 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| ba808538-5d25-32cd-9197-bd3fe9dd6abc | -7.7591 | -48.8189 | 2025-09-07 02:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 9a69b1f9-3a63-3875-959c-29ecce0d2c0f | -6.3008 | -51.3996 | 2025-09-07 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| e4f4826f-445b-3081-aefd-9fbdc8d9e822 | -7.7404 | -48.8204 | 2025-09-07 02:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 77712e5f-ade6-3fa9-8737-99235de1dff4 | -8.6912 | -54.6682 | 2025-09-07 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 29276d65-9f86-3e28-9bc8-127e92e62faa | -17.3643 | -42.6284 | 2025-09-07 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.0 |
| ce0e4ac8-b8a2-3dab-9b72-3b185fd00378 | -9.4309 | -62.3683 | 2025-09-07 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 309e0508-e1da-3b38-b967-3b881c04d6f4 | -6.3006 | -51.4205 | 2025-09-07 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| fe1621fd-4cce-38c6-b3e0-fecbb7abe39f | -12.9477 | -54.793 | 2025-09-07 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| b71da2a6-5503-3619-987f-ec65072aeb02 | -3.5995 | -47.5142 | 2025-09-07 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 63c42136-1965-3d24-b190-b9c4b596f1b5 | -17.3643 | -42.6284 | 2025-09-07 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 6695390c-9e67-3d50-a66d-921f912ffb27 | -12.9289 | -54.7744 | 2025-09-07 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 2fff217d-104a-3d53-9009-15cd6f5f62b9 | -7.7591 | -48.8189 | 2025-09-07 02:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 550b8333-9ac5-31fc-91fa-7b06d2403fd6 | -7.7404 | -48.8204 | 2025-09-07 02:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 98.9 |
| e6ae8dfd-6579-36d2-95a2-53622aa630a9 | -9.4309 | -62.3683 | 2025-09-07 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 13b5302f-190f-3a22-8098-5cb12cbebbbb | -12.967 | -54.7705 | 2025-09-07 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 6d2b26f8-bac4-34fa-9071-3fbe6aecf968 | -17.3636 | -42.6532 | 2025-09-07 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 8cb9b8fb-7cbe-3795-aa3e-06b6c17c9c7f | -5.8403 | -44.1181 | 2025-09-07 02:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| a4309541-329f-32cb-ab19-c573c35ffc92 | -19.4695 | -47.7691 | 2025-09-07 02:10:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 1726fe14-a6eb-3a47-9e54-8ac08c6b7f11 | -9.4495 | -62.3675 | 2025-09-07 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a8c45205-ca12-3a2f-a5db-5d65bb265757 | -6.3008 | -51.3996 | 2025-09-07 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 35e4aeac-ec11-3340-86cc-7f41b2dc3790 | -12.948 | -54.7724 | 2025-09-07 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 362.1 |
| 685ffa75-7a7b-3577-baab-f8681599cd0a | -6.3006 | -51.4205 | 2025-09-07 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c29fabfc-8c67-335d-a887-b76577ee0b7b | -19.4898 | -47.7646 | 2025-09-07 02:10:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 51.2 |
| babb79e1-28e6-3793-babb-5692667a6a6f | -12.9477 | -54.793 | 2025-09-07 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 31177e31-c058-3809-be54-8b109cf92e8d | -21.3449 | -49.1248 | 2025-09-07 02:10:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.2 |
| da3c707a-bae0-3b4a-b892-f6a6cca63647 | -13.0128 | -41.4025 | 2025-09-07 02:10:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 55.7 |
| c353a954-2092-39b5-a5a2-975ab21f2dda | -3.5995 | -47.5142 | 2025-09-07 02:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9666d4ec-da61-3c89-be91-0f94616f2598 | -3.581 | -47.5149 | 2025-09-07 02:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 35802311-6dfa-3c68-83e6-4e848a9e0b5f | -6.3006 | -51.4205 | 2025-09-07 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| e3efb64c-882f-3f53-b4e3-d3ac7e66f201 | -12.9477 | -54.793 | 2025-09-07 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 7406ac64-1743-342c-b892-af226cdadea2 | -12.9482 | -54.7519 | 2025-09-07 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 0a203c3f-ebbd-30a1-aecd-3ed3e6cd3a23 | -6.3008 | -51.3996 | 2025-09-07 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 5aa7b7fd-ccbf-35a0-817f-8a21e0b59afb | -12.9289 | -54.7744 | 2025-09-07 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 383d21a9-ef80-32d2-b2cd-2ac449edefa2 | -5.8403 | -44.1181 | 2025-09-07 02:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 9d75e317-b3df-33e8-be34-417562048c61 | -7.7591 | -48.8189 | 2025-09-07 02:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 3a845ab3-92e6-3fab-804b-220a7262126c | -5.8216 | -44.1196 | 2025-09-07 02:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |


[Clique aqui para ver as próximas entradas](README16.md)
