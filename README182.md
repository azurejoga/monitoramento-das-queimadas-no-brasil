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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fdf17e8-3a2d-3d71-a6c4-896c660f639d | -14.69723 | -48.74453 | 2024-10-03 05:29:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 93a80ee8-508c-352a-9eb7-9460e59197c7 | -14.6958 | -48.75436 | 2024-10-03 05:29:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 123.7 |
| cd6a6cbd-e01b-36c8-8f6c-2ec892a8f08a | -14.69443 | -48.76385 | 2024-10-03 05:29:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 00deda6b-4a22-3766-b664-5b60556cd1f0 | -14.50371 | -45.22541 | 2024-10-03 05:29:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f46d4d4a-1fad-3633-b5cf-f2d6bc359b10 | -14.49907 | -49.28788 | 2024-10-03 05:29:00 | AQUA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 48.4 |
| fea6bb50-5cec-3ebf-ab33-836057a38029 | -14.49018 | -49.28646 | 2024-10-03 05:29:00 | AQUA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b15aac17-236c-30d2-a20a-21bb36c77fd7 | -13.73738 | -48.31084 | 2024-10-03 05:29:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 85b723e0-da50-3adb-bd78-90c92ae68665 | -13.72827 | -48.30967 | 2024-10-03 05:29:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| cba6380e-81ff-35d8-8f88-5fc7aaf5a986 | -13.49306 | -48.59918 | 2024-10-03 05:29:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 429b66fc-8ec9-33a3-b7c3-fc7a5032690c | -13.49172 | -48.60842 | 2024-10-03 05:29:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 386dd4ab-d9cd-3a30-bd35-e5716e5fddf3 | -13.21989 | -48.63519 | 2024-10-03 05:29:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4243edf8-8af2-3d93-a703-5503e09eebc2 | -13.19929 | -48.65094 | 2024-10-03 05:29:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8271f7e8-8dfb-38d5-9956-b1b205c7f055 | -13.19702 | -48.60333 | 2024-10-03 05:29:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 147e2072-8696-307c-b96a-7662b54e0338 | -13.19567 | -48.61271 | 2024-10-03 05:29:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| afb6af7c-e4ca-3232-9054-eb2c1d8154d4 | -13.19433 | -48.62198 | 2024-10-03 05:29:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d661ce65-ad98-38a5-b195-c184ad881bcd | -13.19299 | -48.63123 | 2024-10-03 05:29:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| edbace89-c389-36ca-8140-4466353f3483 | -13.19165 | -48.64045 | 2024-10-03 05:29:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 69b11217-fa9e-3ac8-b792-b28bdbfb8677 | -13.19032 | -48.64965 | 2024-10-03 05:29:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a69c0b7e-31be-3860-95ce-0f7fa9cc4f10 | -13.18806 | -48.60196 | 2024-10-03 05:29:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 914c82df-f35c-3680-bd08-90f75e00369b | -10.7262 | -46.16946 | 2024-10-03 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 11bea72a-cd54-3ffa-af74-f65eea03590c | -9.59254 | -50.17843 | 2024-10-03 05:29:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8b70c36e-f242-337f-a72d-e6479b191bcf | -9.59111 | -50.1878 | 2024-10-03 05:29:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4dddd247-6bb2-3818-a076-25cbd6bd0cdb | -11.08352 | -52.52363 | 2024-10-03 05:29:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b3ec486a-64db-3118-8422-5517b36de001 | -11.01967 | -46.49088 | 2024-10-03 05:29:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1a36a8b0-58f4-3c6e-897a-38b6ba860e40 | -17.07148 | -56.78308 | 2024-10-03 05:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.9 |
| 053f765c-7ad1-3ec3-9dfa-b03067d12c89 | -16.92451 | -55.8603 | 2024-10-03 05:29:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| d8e1b3b1-cc6c-341f-be5d-461e7d057406 | -16.91597 | -55.85302 | 2024-10-03 05:29:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.3 |
| aa65f1df-90b2-394c-a035-2e7b9bee2dda | -16.91295 | -55.8581 | 2024-10-03 05:29:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 26e04da0-0527-3326-bb13-4d16305c7c3e | -16.59017 | -58.22653 | 2024-10-03 05:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 85183de1-4b94-32b2-b54d-f45ac041a02a | -16.56706 | -58.19632 | 2024-10-03 05:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 12c48a25-224e-3b2d-b91f-7238657969a0 | -16.56403 | -58.18787 | 2024-10-03 05:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.0 |
| c5fcb7cc-d320-3bc1-8b8a-bc0cb35a72d8 | -16.55015 | -58.18494 | 2024-10-03 05:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 557.0 |
| 166ede8e-890a-304d-95d9-f0bef1b5e2fe | -16.54546 | -58.20995 | 2024-10-03 05:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1130.7 |
| 75eedc7f-31e3-30b5-89a1-a9129848d2f3 | -16.54078 | -58.23491 | 2024-10-03 05:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 219.3 |
| d90d3b75-1790-3a84-b6ee-e7baacf56cb3 | -16.53154 | -58.20705 | 2024-10-03 05:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.1 |
| 74a35353-0abe-3df6-9c19-3273cddc34b1 | -15.67714 | -52.49869 | 2024-10-03 05:29:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 179a2176-475a-3fbd-a32f-cee5a82791de | -15.67546 | -52.50916 | 2024-10-03 05:29:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 06588f37-d147-317f-a96e-d52894184489 | -13.60528 | -51.22491 | 2024-10-03 05:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9646ea4b-bb5f-3019-a32b-c027d1eb34a0 | -13.56286 | -51.25755 | 2024-10-03 05:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e1dd6c2e-cdc7-30b3-8fe6-c22c03d3bc99 | -13.56135 | -51.26719 | 2024-10-03 05:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 26fdb55a-6af2-35b2-9532-567db4b8a537 | -13.52714 | -51.13704 | 2024-10-03 05:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f9992c75-d8b5-3121-83f2-5cf9aff58fdf | -13.26525 | -48.57559 | 2024-10-03 05:29:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dccc7270-a7e8-3db2-b3a5-e1364533f3f9 | -13.2639 | -48.58485 | 2024-10-03 05:29:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1a59b357-4d37-3dff-ae5c-b6de848086a9 | -13.26258 | -51.22989 | 2024-10-03 05:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fc54a1d2-a8d7-3d97-9a64-118f8eb2ebff | -13.21377 | -51.18649 | 2024-10-03 05:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f969e0f2-a8cb-3940-93b8-0312a6f57ded | -13.13139 | -51.18649 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 0551c403-68e4-3b0a-997d-5cbe4f097866 | -13.1299 | -51.19614 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0717bb18-050c-3943-8666-5ceed474190a | -13.0979 | -51.16139 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e1e9ddab-e372-3fb5-9bda-1fcd824fa74c | -13.08878 | -51.15993 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 514a24a0-e720-3f09-afab-3db931dd3591 | -13.07965 | -51.15847 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 9bf46a40-454e-3fbb-9bf3-230339507b29 | -13.07351 | -50.83979 | 2024-10-03 05:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| eeeb3f43-f3cf-33b5-a5ef-41b932e1327c | -13.0551 | -51.13884 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 61f53432-7023-3fe7-b4cb-40b2a167c1aa | -13.05361 | -51.14846 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 43708ad2-42fa-31e1-af8f-716464702601 | -13.05212 | -51.15808 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cf776143-3874-31d5-833b-b59f6120dec6 | -13.04598 | -51.13738 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 283.6 |
| 2baba329-f5f1-39b0-91a4-35b7c8f65ded | -13.04449 | -51.147 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 9163cc1a-1dd2-32f2-88a4-3362fc842daa | -13.03836 | -51.12631 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 55783acc-ab6f-3ca0-b0f0-9ed1e87fd6f3 | -13.03687 | -51.13592 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 31149d71-0742-3af0-873a-cba56c6bec4f | -13.02775 | -51.13446 | 2024-10-03 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 75229d94-59cf-313c-9c53-ee9b756b5d30 | -12.50146 | -53.13828 | 2024-10-03 05:29:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 93384ca0-97c7-3a3f-a22d-f819991927bd | -12.33243 | -54.08118 | 2024-10-03 05:29:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 06f92723-fa78-3b3f-9fb5-a8f81bc05434 | -11.07347 | -52.52192 | 2024-10-03 05:29:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| bfa78c63-dd10-3f52-bd3f-fc511180a323 | -12.33042 | -54.08865 | 2024-10-03 05:29:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b2c0b20a-c5ec-3978-ba76-4dc4761770cd | -12.19758 | -46.75826 | 2024-10-03 05:29:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 71fd930e-61be-3789-86be-435626c57809 | -12.15111 | -54.26386 | 2024-10-03 05:29:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b931e0e2-f851-366e-96e7-d089c46ae0de | -11.0843 | -49.5924 | 2024-10-03 05:29:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 540ff54b-07e9-38ef-80a1-cc332760e776 | -11.68511 | -47.71147 | 2024-10-03 05:29:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 935e3d3b-a46f-3ad6-b58d-b6c059013dc6 | -11.67731 | -47.70076 | 2024-10-03 05:29:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d7388b17-9e2b-3fdf-9e3c-a9874e9ff527 | -11.67599 | -47.71 | 2024-10-03 05:29:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 078866d1-defc-3dc8-8340-e176c647e306 | -10.42989 | -50.79995 | 2024-10-03 05:29:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 227ea03c-f962-38e4-a85e-28d5272f1648 | -10.62872 | -53.69637 | 2024-10-03 05:29:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 915077ae-d612-30bc-b85a-c0f1b87def94 | -10.63262 | -53.68776 | 2024-10-03 05:29:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| fe12b057-21fa-3441-aa6c-9f82f6d95a52 | -10.65466 | -53.69156 | 2024-10-03 05:29:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6264bf27-12fb-327c-8935-ac1aa74a61ba | -10.90472 | -52.42171 | 2024-10-03 05:29:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 40968541-462b-3b0d-bfec-10f8b0a36370 | -10.90658 | -52.41005 | 2024-10-03 05:29:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| df2fcd0d-c884-3393-92fb-b892905111c6 | -22.99535 | -49.60688 | 2024-10-03 05:31:00 | AQUA_M-M | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 4571f31d-8e28-3e3b-a75f-d4a9760515ca | -22.6836 | -50.47568 | 2024-10-03 05:31:00 | AQUA_M-M | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 05260990-b197-3cac-9ff0-5be5f0e50bf8 | -22.4415 | -46.87167 | 2024-10-03 05:31:00 | AQUA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 9eefa432-9272-31f4-8bdc-fd2ff34823a1 | -22.36311 | -49.27201 | 2024-10-03 05:31:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 43157d77-426b-3e86-a30a-b7b113db4b22 | -22.36164 | -49.28294 | 2024-10-03 05:31:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| a27cb73d-adbf-3f25-8f71-90809e780ec0 | -22.15501 | -48.62123 | 2024-10-03 05:31:00 | AQUA_M-M | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 346dec7b-f7fc-3d95-a600-7b706d165c7b | -21.39634 | -47.63367 | 2024-10-03 05:31:00 | AQUA_M-M | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d6874262-dc7c-371e-b5b4-f3d3d33f910c | -21.38603 | -47.6321 | 2024-10-03 05:31:00 | AQUA_M-M | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3952c6d1-f82a-386a-bba4-2595cd0356e9 | -21.34471 | -55.66558 | 2024-10-03 05:31:00 | AQUA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 31a9430f-5a71-3be6-ba29-b25f55d63ee9 | -21.34235 | -55.67904 | 2024-10-03 05:31:00 | AQUA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f2b894b0-8f56-3868-a29f-9f9c257e900f | -21.33426 | -55.66339 | 2024-10-03 05:31:00 | AQUA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 77c346a4-f9ab-3f8c-87f7-f615e1f4fe92 | -20.76455 | -46.28091 | 2024-10-03 05:31:00 | AQUA_M-M | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4e37e3c7-6118-332c-9ca8-2d795ec62d38 | -20.76271 | -46.29666 | 2024-10-03 05:31:00 | AQUA_M-M | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8abfa7c2-ddf9-3780-9673-22460303f93a | -20.53926 | -46.2518 | 2024-10-03 05:31:00 | AQUA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a77a8d0f-579d-35ee-be2b-2bf03141d590 | -20.53737 | -46.26743 | 2024-10-03 05:31:00 | AQUA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4a5d9042-b929-3649-9bef-71a2d422b9de | -18.69354 | -57.30101 | 2024-10-03 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.5 |
| b8f56f59-90c3-3b15-8dc8-206bc16ea337 | -8.9791 | -67.4099 | 2024-10-03 05:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 4b2db4d5-6796-35dd-99a2-64bc0c7fa23d | -11.6931 | -64.9974 | 2024-10-03 05:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 9148cb42-ed95-37a3-b5aa-f1c97c2cd35b | -2.87706 | -61.87983 | 2024-10-03 06:05:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abcc6138-68e5-34a6-8153-c9ae9ae67452 | -2.87755 | -61.87658 | 2024-10-03 06:05:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82372059-0a2e-328b-a5d3-825bd1211712 | -2.88232 | -61.88072 | 2024-10-03 06:05:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11b251f9-4b1c-33bc-b5b2-5ff0c888dcfc | -2.8828 | -61.87748 | 2024-10-03 06:05:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f906f8f-88d4-3872-8c66-2cb1bc1e1876 | -2.8833 | -61.87417 | 2024-10-03 06:05:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8b3c277-35f8-33e4-adba-9493a8976001 | -2.88379 | -61.87091 | 2024-10-03 06:05:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b52717cb-80cb-3543-be73-6fc82387470f | -2.88855 | -61.87509 | 2024-10-03 06:05:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README183.md)
