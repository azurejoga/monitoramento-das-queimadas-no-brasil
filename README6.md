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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32559b47-8333-37d0-bbf8-a03d2ec53fa5 | -4.77387 | -56.11739 | 2026-09-06 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5d259d0e-b529-3471-adf8-1253d925b483 | -3.14312 | -60.64967 | 2026-09-06 00:26:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 337fe0b2-ad62-3e5a-8cb1-c6075d21e949 | -3.77899 | -58.85514 | 2026-09-06 00:26:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 67d84c25-c252-3d6c-a033-cc1e22df633a | -3.23121 | -58.88774 | 2026-09-06 00:26:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2ec8db88-6a23-3b43-b571-79b28afae8d0 | -3.14116 | -60.63526 | 2026-09-06 00:26:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| c3d13818-c0c5-3f57-aa9f-832835800487 | -3.71688 | -51.14001 | 2026-09-06 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 487c4ec8-44f9-32bd-91a7-250c4f6c2d7e | -4.47463 | -55.08835 | 2026-09-06 00:26:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 4b01f9d5-880e-3309-b785-31b7f3f1df56 | -3.62286 | -54.60355 | 2026-09-06 00:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 267d2b42-b4fa-3d3b-9e22-facffa906985 | -4.67712 | -55.6275 | 2026-09-06 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 19b4384b-804a-31c3-8d35-312f75826c37 | -3.95134 | -57.05621 | 2026-09-06 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c1970ec8-0204-386d-9c7b-fe49292272cb | -3.80912 | -55.89029 | 2026-09-06 00:26:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| cf507964-b8d3-3fd0-a65b-eab2c1162964 | -1.38859 | -55.18186 | 2026-09-06 00:26:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 6caa824b-9009-3ba9-bda3-fe537542b3b1 | -3.11745 | -57.6965 | 2026-09-06 00:26:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dd3cdf05-45a7-3745-87fc-c1f6b9522fcd | -1.56407 | -55.78799 | 2026-09-06 00:26:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aec17473-d135-3bf0-a842-3cd55a1b5f2b | -3.15389 | -50.82554 | 2026-09-06 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fdfee282-3934-3181-a940-2903535a770a | -1.48485 | -54.80943 | 2026-09-06 00:26:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2221a566-0db3-3eec-ad83-1af2fc840e53 | -3.05175 | -61.32883 | 2026-09-06 00:26:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b577b37b-9d19-3626-9ef9-00342542d4f4 | -2.2516 | -53.76741 | 2026-09-06 00:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c210525f-4ccb-3ff4-bde7-2a3c32b0c9c2 | -3.54572 | -48.17423 | 2026-09-06 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 3aa5edb9-754b-3449-b7d9-ab7bdf5b87cb | -5.25761 | -59.97646 | 2026-09-06 00:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 27230f07-b45b-34a3-9815-bf97cd4cc8fa | -3.76581 | -61.7663 | 2026-09-06 00:26:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| fbb9f504-fce1-393d-801c-cfe7ab5606d4 | -3.19841 | -61.23107 | 2026-09-06 00:26:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 0a2ad463-be7a-3d84-ae75-314d651099a4 | -3.79913 | -55.88277 | 2026-09-06 00:26:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 0de23ff4-c8cd-328c-b935-24d1797ac549 | -3.41989 | -58.30635 | 2026-09-06 00:26:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5b455135-bcd2-341f-b7ab-e813ab4f9bab | -4.66833 | -55.62873 | 2026-09-06 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bec90896-f437-324d-aa87-0015c0402f4b | -2.88834 | -57.30425 | 2026-09-06 00:26:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 211ac47a-806d-3c63-806f-f70453b370a0 | -3.77126 | -61.77844 | 2026-09-06 00:26:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8cbbde8e-54e2-37dc-b15c-3e8eb92b6d7d | -3.54931 | -48.19911 | 2026-09-06 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 23fecc2c-3473-35a8-b3a0-cf36ab66d3c0 | -4.47585 | -55.09719 | 2026-09-06 00:26:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c995e041-0e0a-3e62-8ad4-0c49e90e7092 | -3.81032 | -55.89904 | 2026-09-06 00:26:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ceb0e3ed-2784-346e-9de0-d5fb9c1a8458 | -4.66954 | -55.63749 | 2026-09-06 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7557d62a-8a50-36fd-bece-0b069ce3d23b | -4.3541 | -56.28765 | 2026-09-06 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8596d95f-defe-31c5-8a22-313e5cdd46ba | 3.65896 | -61.14388 | 2026-09-06 00:28:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bbc5b99b-93ef-3497-80c7-ba0fbd43d91e | 4.23599 | -60.91412 | 2026-09-06 00:28:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| da2505b7-d8a8-3233-8f59-dd6bc285de23 | 3.36362 | -60.71009 | 2026-09-06 00:28:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 97e11d53-2a76-3758-b61d-fee68fa8c387 | 3.65032 | -61.1494 | 2026-09-06 00:28:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2d864aec-3511-3c5e-8d5e-8f922a6468b0 | 3.79267 | -59.65023 | 2026-09-06 00:28:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2caf3665-b433-3572-8fce-a26f001b3616 | 3.79125 | -59.66023 | 2026-09-06 00:28:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b42d5c52-89da-3424-bb03-6dc1cdd7ea80 | -3.2239 | -53.1742 | 2026-09-06 00:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 192dd1b7-0119-362d-ac2d-39c3bf39fbc2 | -10.701 | -45.9471 | 2026-09-06 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 06538a34-340a-328f-8627-4ae006f9dfba | -9.3665 | -67.8263 | 2026-09-06 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 22490e98-a2d2-391b-ad7a-419c171cf195 | -13.7608 | -51.6495 | 2026-09-06 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| c0cb3868-a642-3718-9afe-d2fddff82228 | -14.9246 | -44.6744 | 2026-09-06 00:30:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0607523c-505f-378c-889d-d8f6565f01f6 | -6.6514 | -59.945 | 2026-09-06 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b45c6d0d-b637-345d-a5f5-1e773aaad955 | -20.4586 | -57.3864 | 2026-09-06 00:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 213f7890-ed60-3622-b96a-7bd3cfb9e0f0 | -13.3296 | -61.1259 | 2026-09-06 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 73ee67de-7bf7-32c5-bd68-8c2ffa19eab3 | -13.7605 | -51.6708 | 2026-09-06 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 6b08b583-4642-304e-9703-75685b28845a | -3.5406 | -48.1889 | 2026-09-06 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 86e23234-65dc-3a5b-bc46-0cb50182213e | -13.3298 | -61.1064 | 2026-09-06 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a96d805e-2efb-36cd-8e6a-c3da44cd6972 | -5.1438 | -55.9741 | 2026-09-06 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d9a736d5-1cfe-3788-987f-7103c3cf249a | -13.3486 | -61.1245 | 2026-09-06 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 129.6 |
| fc3a3897-7f93-3c2a-90bd-294b15f04031 | -14.905 | -44.6782 | 2026-09-06 00:30:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| bc251063-2986-347d-b5d9-aa85661905fe | -5.1439 | -55.9543 | 2026-09-06 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 768fa591-bbf8-301c-b85a-0e64b5083db7 | -6.8813 | -55.619 | 2026-09-06 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| bf4a26d0-2b23-3d02-9aaf-9d119e45dfb9 | -3.5591 | -48.1882 | 2026-09-06 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 92bf06f4-1edc-3c67-900e-7e595d2ec75a | -13.3488 | -61.105 | 2026-09-06 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 86.6 |
| c92d4e15-c000-38fb-902c-8ea20b8a5cf3 | -10.6823 | -45.9268 | 2026-09-06 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| ef162d07-6319-3432-808a-9ec305895c45 | -10.7492 | -60.7097 | 2026-09-06 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| d7442ad3-2d8f-3adc-83c9-705cbe753c28 | -13.7801 | -51.647 | 2026-09-06 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 46a69a3a-285f-333f-b3b2-483112918730 | -10.7013 | -45.9244 | 2026-09-06 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.8 |
| b7f2a5bb-6ed5-3bce-bf59-1caaec9891bf | -20.4384 | -57.3893 | 2026-09-06 00:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 7186b2d9-784b-3534-88bc-d6b39a2a98f8 | -10.749 | -60.729 | 2026-09-06 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| f4832cda-d305-3f19-9d37-7d71c998ffce | -3.5591 | -48.1882 | 2026-09-06 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 0650ab65-6400-3b8c-a913-737983e031cd | -7.0971 | -56.5204 | 2026-09-06 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8d4081ce-8876-3097-aa71-f9d66777514e | -5.1439 | -55.9543 | 2026-09-06 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 0be7f4c2-d762-336e-b06e-5da16582d082 | -5.3462 | -56.0256 | 2026-09-06 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| a6e6f0a4-6660-3f88-91e5-ca2a2abd434c | -6.8627 | -55.6199 | 2026-09-06 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1d0ae330-9eea-3dfb-a26f-ab8f055fd043 | -10.7492 | -60.7097 | 2026-09-06 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 154.7 |
| e8c17244-c519-3740-a0ba-4e21d8362622 | -13.7608 | -51.6495 | 2026-09-06 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 1663f626-b729-3cd7-84be-69989a00ca21 | -5.3647 | -56.0051 | 2026-09-06 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| bf347bb8-55cf-330b-96c0-2b9d8da55dbb | -10.6823 | -45.9268 | 2026-09-06 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 4c33f113-3e96-3e28-9bae-2ea4e2a53a8a | -3.2239 | -53.1742 | 2026-09-06 00:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b8967e31-5e07-3b98-97be-ffdd55e3de12 | -10.7017 | -45.9016 | 2026-09-06 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 61af989e-7cdd-3016-8d6c-7b4618cb10fc | -10.7013 | -45.9244 | 2026-09-06 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 7e6473ff-4522-3e99-858e-df9ed31e6f67 | -14.905 | -44.6782 | 2026-09-06 00:40:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1ea74dae-7eda-3db5-8966-20c32c8c37f5 | -5.3646 | -56.0249 | 2026-09-06 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 322.9 |
| 2db79b11-70e9-3a89-8f5b-765f2f3b692a | -10.749 | -60.729 | 2026-09-06 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 9871e91d-2bc8-3c30-b2e9-09f909266a06 | -5.3645 | -56.0447 | 2026-09-06 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 180.9 |
| 5d8f63e9-9a71-3306-8cd1-248a81147191 | -14.9246 | -44.6744 | 2026-09-06 00:40:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 90.9 |
| ebe9dad4-4f30-352b-a236-099ad99f5e1c | -13.7801 | -51.647 | 2026-09-06 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c0248d2b-6799-38f5-97c1-4894d8875a14 | -5.383 | -56.0242 | 2026-09-06 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 993fb349-c606-33bd-be67-32660745d91f | -6.8813 | -55.619 | 2026-09-06 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 9d357030-886d-3ef1-8f00-16995949f76d | -6.6514 | -59.945 | 2026-09-06 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 747a70b8-34d8-3fbe-a62d-8e8ea1484d17 | -6.6698 | -59.9443 | 2026-09-06 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| c5320809-2638-3b98-893a-2009cee6fb20 | -5.1438 | -55.9741 | 2026-09-06 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 39082696-5de5-3f27-b655-930b47c4f217 | -13.3488 | -61.105 | 2026-09-06 00:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 7654fa5d-6c44-3b08-9579-0b890bf72d90 | -6.8813 | -55.619 | 2026-09-06 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e60479b8-5839-3235-9f8f-555fba757d65 | -5.3646 | -56.0249 | 2026-09-06 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 328.3 |
| 2909eedb-2525-3642-8323-4ab19a79f0d7 | -10.7013 | -45.9244 | 2026-09-06 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 318.0 |
| 048a6893-4bd1-3dba-b667-cd2a0be0ba68 | -5.1438 | -55.9741 | 2026-09-06 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 9f357a50-1244-3e04-8df1-20012a4cedb0 | -3.5591 | -48.1882 | 2026-09-06 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 49645303-70bf-383d-9e3b-210385ac909d | -10.701 | -45.9471 | 2026-09-06 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3585547e-be43-3340-993f-a678aa6a193d | -13.3296 | -61.1259 | 2026-09-06 00:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 122.6 |
| e618e9cf-6ee4-314d-88a2-e31c4e7fcac8 | -13.3486 | -61.1245 | 2026-09-06 00:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 157.6 |
| e22cb569-387d-33b7-a5ce-864487e9d0de | -13.3484 | -61.144 | 2026-09-06 00:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c0e0d7a3-2ec0-335b-8bdb-1fdc4afd8081 | -5.3462 | -56.0256 | 2026-09-06 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 8169fdee-d2fd-3d56-8920-e0ac176151e7 | -14.905 | -44.6782 | 2026-09-06 00:50:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 01b340df-c511-3e11-bb2f-1870b5302382 | -10.6823 | -45.9268 | 2026-09-06 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 6f14d95a-8032-3c67-9fc2-f482e9b1f8f6 | -14.9246 | -44.6744 | 2026-09-06 00:50:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 4b6afd3b-97cc-31f9-b521-15b15f37c6fd | -5.1439 | -55.9543 | 2026-09-06 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |


[Clique aqui para ver as próximas entradas](README7.md)
