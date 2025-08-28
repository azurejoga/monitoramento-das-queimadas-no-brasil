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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76418786-f28f-339b-95e5-e009e5e91058 | -11.6539 | -44.8765 | 2025-08-28 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 853ec5c4-972b-3f60-87f9-9b8be160b10b | -9.1155 | -65.7699 | 2025-08-28 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 592.3 |
| fcc201f4-f04b-3f33-a706-7ad3429c59f0 | -15.191 | -53.79 | 2025-08-28 14:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 7fdd3d11-056f-3617-814d-342bb7f205c7 | -6.8583 | -43.6169 | 2025-08-28 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| b4dabbfe-64dd-3fd9-b404-75543b1d8247 | -12.9963 | -56.9 | 2025-08-28 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c753287b-6ca5-331d-ae1b-0bac270c55a3 | -12.6878 | -48.1677 | 2025-08-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| deea1575-d6af-3465-8b03-ce635179c1e6 | -15.2104 | -53.7876 | 2025-08-28 14:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 5cb9de04-479a-32f1-a8d7-057ab3af3810 | -9.1339 | -65.788 | 2025-08-28 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 969.3 |
| d1f96328-006d-333a-891c-b6e51bf057f3 | -8.7322 | -47.4003 | 2025-08-28 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 9bf63fd8-90fc-3f1d-a612-0a0a8f2a2f22 | -10.4738 | -57.9366 | 2025-08-28 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| cc348b36-5f1e-30eb-a89f-648819646296 | -12.8998 | -48.1158 | 2025-08-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 74392212-3f91-37bf-be83-2219b402d720 | -10.8421 | -60.8009 | 2025-08-28 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 2c787ef0-c949-3f54-a0ff-210ea5983572 | -10.8419 | -60.8202 | 2025-08-28 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| d23ec766-d10c-3e3f-84e9-62ced1c34de4 | -9.2632 | -65.8959 | 2025-08-28 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 82bac62f-1810-35ef-9596-0328beb152a6 | -7.0569 | -44.3623 | 2025-08-28 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| afa06a69-49d2-39b1-9d96-5bbc34f71934 | -15.1906 | -53.811 | 2025-08-28 14:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 46485be3-a5ee-3c72-bd6b-14ac105d89be | -6.2755 | -43.6907 | 2025-08-28 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c6efcb4b-e803-3da9-afe4-57277eb2f762 | -13.4212 | -46.9637 | 2025-08-28 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 2d5a6327-9486-34cc-a986-6152d7f55faf | -6.1595 | -44.0472 | 2025-08-28 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 168.2 |
| a428b227-6404-3e22-b0b7-ebb9e19c7d95 | -11.5707 | -46.3751 | 2025-08-28 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d2f8bd3f-9005-37ef-af7d-85ee1d9d65b5 | -9.134 | -65.7694 | 2025-08-28 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 302.3 |
| 9736de8b-e9fe-3cfb-873c-8b3312ed7bf9 | -6.4543 | -44.5749 | 2025-08-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 2596917d-d393-3777-9216-1663fa847eb4 | -14.3309 | -53.2477 | 2025-08-28 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 3bc6f2b2-e1f1-38d0-a969-a28fe3b043a0 | -7.3196 | -46.109 | 2025-08-28 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 4c85e255-d52a-3227-864c-8fa41f66fd44 | -11.6127 | -47.2907 | 2025-08-28 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 7d140f64-ec01-37f2-a25a-e28056644225 | -11.2189 | -55.0585 | 2025-08-28 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 8edb5511-7031-39c2-b379-84be75d78163 | -8.2705 | -45.1605 | 2025-08-28 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| a1d74ffd-11bf-3a65-93f1-4bd37bd50a0f | -10.4736 | -57.9563 | 2025-08-28 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 04764f19-bfbf-3191-b0ae-1b5b23640e33 | -6.4355 | -44.5764 | 2025-08-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| e7edc430-f7e6-3738-a4ed-610f7bf87c9a | -9.5423 | -62.4014 | 2025-08-28 14:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 75f75d69-0123-39e4-a7de-ca29ce106917 | -8.7514 | -47.3764 | 2025-08-28 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 87d5e0e2-f0e6-3ac0-8ac6-7aec937be3ea | -6.8772 | -43.6152 | 2025-08-28 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 194.4 |
| eed427aa-7017-3eaa-8fe3-53e5cf40974f | -9.5424 | -62.3823 | 2025-08-28 14:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| bab5769a-ff00-3fef-81d0-e73ea10ae502 | -9.6794 | -47.0798 | 2025-08-28 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 5090b001-f991-3770-8a21-47577598a017 | -12.8805 | -48.1186 | 2025-08-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 03cd2b2c-2337-3645-937c-4790c82aa179 | -9.0971 | -65.7332 | 2025-08-28 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| fb194c7a-537c-3bf2-9145-bf894e1c7e69 | -14.3696 | -52.0813 | 2025-08-28 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c9f0442c-06f1-313a-bc2d-99afe7eff7e7 | -7.192 | -44.0501 | 2025-08-28 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ea63b35c-c009-3a15-88e2-919af0bc6818 | -11.2378 | -55.0569 | 2025-08-28 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 3f190626-23ce-3a98-83f6-847f0e0782c2 | -10.4549 | -57.9576 | 2025-08-28 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| e8ae440b-00db-3bdb-acc3-1a8ecc238b1d | -12.8228 | -48.1267 | 2025-08-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 0f1bb19d-bf86-34ab-b2fb-4ed6a01ccdaf | -12.8032 | -48.1516 | 2025-08-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| c985ca49-8fce-3ea4-b1ed-95f98d78681e | -12.8224 | -48.1489 | 2025-08-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 8d940c89-41d5-3ce0-8d0d-2e936aa71a7b | -6.1783 | -44.0457 | 2025-08-28 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5a88846f-9396-3711-ba2c-6decd926f437 | -11.1017 | -44.7476 | 2025-08-28 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| cb529312-8eb9-35d1-8f2c-b6aa12173979 | -8.4407 | -43.6666 | 2025-08-28 14:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 701c09f8-8d1f-3055-bcf7-ece0a0fef229 | -6.178 | -44.0688 | 2025-08-28 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 4a6886ea-8959-3742-9fe4-7f735460421b | -12.9961 | -56.9201 | 2025-08-28 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 234922ae-93ca-3e46-82be-742660a07397 | -5.8169 | -42.6043 | 2025-08-28 14:00:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| c794b138-148f-37ec-9309-7ebe50cef93c | -10.8049 | -60.7644 | 2025-08-28 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 8805fadc-0382-3af3-aa0f-a0722e10d75a | -7.3542 | -59.6476 | 2025-08-28 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| b37ba244-aa2a-3ba0-bfb2-70a2aa040e1a | -9.6816 | -48.3139 | 2025-08-28 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 54f3c953-b796-3bd2-9dcf-494eb3011af1 | -12.8228 | -48.1267 | 2025-08-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 76e38594-6555-3c67-879e-f7ce521029c1 | -10.3709 | -45.1686 | 2025-08-28 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 9ee8dc01-91a3-3909-ae83-27ef9151be77 | -11.3526 | -43.5187 | 2025-08-28 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 0aeface4-3759-3c92-a9e7-2b00ee79faf5 | -13.0154 | -56.8982 | 2025-08-28 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| e3d7511b-40bd-3e42-b4f2-3cc68dcc23cd | -9.5424 | -62.3823 | 2025-08-28 14:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4126834a-0589-358a-8f62-6d3d5418f465 | -13.0151 | -56.9184 | 2025-08-28 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 11a87d8b-2179-3505-9ffe-d50837987592 | -7.1917 | -44.0732 | 2025-08-28 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 17f4531a-3b7a-3dcc-a001-0c2d46c64633 | -6.4357 | -44.5535 | 2025-08-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| d0fdd365-db70-3f98-af23-60782d1bc3dc | -11.2189 | -55.0585 | 2025-08-28 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| c9152de9-823c-3afc-8231-5a8e76b3f8e9 | -12.8224 | -48.1489 | 2025-08-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 361cca4d-5f2a-3de3-8632-4827be3bbf6f | -6.1595 | -44.0472 | 2025-08-28 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 72b0060c-22ea-3754-9e2e-364e373a8f6e | -9.1155 | -65.7699 | 2025-08-28 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 478.6 |
| 2a5a638e-975c-3346-9dcd-b405e885e58f | -8.3314 | -44.8115 | 2025-08-28 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 5fd8cd6e-5153-368b-910a-0e296dfbd067 | -9.1363 | -65.2835 | 2025-08-28 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| caa6367c-81bf-3a0e-83b5-0237eef97b74 | -9.5423 | -62.4014 | 2025-08-28 14:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f4f5d2ec-0384-31a4-8aaf-7249044b7fb7 | -12.6878 | -48.1677 | 2025-08-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 76c03a4e-98ab-367c-866c-ee2140d42836 | -6.4355 | -44.5764 | 2025-08-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 9aeda51d-d89e-337b-bf3f-376be7a6c16e | -9.4363 | -48.3174 | 2025-08-28 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| bc017198-3126-3949-9c19-46c0923904ee | -9.134 | -65.7694 | 2025-08-28 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 257.4 |
| 5b0782c2-ffe4-3e69-8c80-05a52313d4c9 | -7.3542 | -59.6476 | 2025-08-28 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 24b6663d-9f8b-3ac7-9ee3-6b80c8e8527f | -14.3113 | -53.2711 | 2025-08-28 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a034a637-ce07-34f5-91eb-fa673e5c996b | -7.0569 | -44.3623 | 2025-08-28 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 6545f890-3960-341c-bf4b-82f136345b91 | -9.1525 | -65.7874 | 2025-08-28 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 476b1520-3d00-34b2-8937-9f96553885c0 | -8.4407 | -43.6666 | 2025-08-28 14:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 90a33070-ce6b-3cfb-8278-62e18f20dd00 | -8.7322 | -47.4003 | 2025-08-28 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 45e457fe-adf6-31f4-8dba-471a98aafe0d | -10.8049 | -60.7644 | 2025-08-28 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 7768323d-2cb1-3f12-812d-1e9015d46fb5 | -14.3693 | -52.1026 | 2025-08-28 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 973055e4-290f-348b-860d-023743787fb8 | -10.8419 | -60.8202 | 2025-08-28 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| b5f8d2a5-4223-3bb4-8b71-12662825c6ed | -7.3357 | -59.6484 | 2025-08-28 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 6021bd06-9eb8-300b-98a2-8a5703790fea | -9.2632 | -65.8959 | 2025-08-28 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 4ebe0a0d-d39c-32e0-a4f0-f9a028a56a66 | -10.8047 | -60.7837 | 2025-08-28 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 84d8277e-2e9a-33c3-bf0b-5b3f457c2af7 | -10.4549 | -57.9576 | 2025-08-28 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 1f9530a5-9c54-307f-ace9-3c67579d7c6e | -9.0971 | -65.7332 | 2025-08-28 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| b680f1d5-f85a-34fa-8188-4af45a03028c | -13.5193 | -46.8805 | 2025-08-28 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 98485031-5e92-3bcb-9a88-c0beb89772dd | -14.3309 | -53.2477 | 2025-08-28 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 6337b2f7-7d7f-3bba-b7d4-df8755f6df81 | -9.4372 | -48.2518 | 2025-08-28 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 175dd1d6-b072-3340-a301-c6f9a808e0a5 | -15.191 | -53.79 | 2025-08-28 14:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| fd2924bd-ef8d-30f6-a2ae-58b4a15906ea | -15.1906 | -53.811 | 2025-08-28 14:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| e63f4b2e-408f-310e-8e8c-acf0c6b4d2e7 | -12.8998 | -48.1158 | 2025-08-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 4cf757ba-f5ff-377d-8d5c-dc12aab020a1 | -12.9963 | -56.9 | 2025-08-28 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f529ed4d-26d9-3e12-a583-f5fab7c12a58 | -9.2446 | -65.8965 | 2025-08-28 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 076a8d01-9f2e-3b6f-8829-cb0c127be141 | -11.2378 | -55.0569 | 2025-08-28 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 132fcdb0-3b35-37e7-9176-e3e81105ffd0 | -6.0244 | -44.4716 | 2025-08-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b7ec9eaf-11f3-3333-ae3f-947e88471758 | -8.7325 | -47.3783 | 2025-08-28 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 859f3120-15d9-38f9-bff4-98447433b12b | -12.8617 | -48.099 | 2025-08-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 1669bde8-5a2a-30bf-b366-70fc35b99deb | -11.0676 | -52.0416 | 2025-08-28 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a759a447-3a84-3c1a-b411-04b69bc041b6 | -11.0679 | -52.0206 | 2025-08-28 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 9b8c818c-de15-311d-b7ff-df005601d44c | -6.2755 | -43.6907 | 2025-08-28 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |


[Clique aqui para ver as próximas entradas](README99.md)
