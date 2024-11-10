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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91afc940-6b2b-32b2-8d6c-b71c8086d63f | -8.40614 | -44.17078 | 2024-11-10 01:17:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 56c35653-a53b-301e-a7df-2b73c577b22e | -8.39989 | -44.13482 | 2024-11-10 01:17:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c224adb8-1db8-33ba-bd08-812536a2a6e4 | -8.37786 | -44.1439 | 2024-11-10 01:17:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 1e1c9fec-353c-33ab-8287-79c36121c6a2 | -8.39436 | -44.14115 | 2024-11-10 01:17:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 7eeda5b6-89fc-363c-88a1-229b53c0f440 | -14.12703 | -60.44478 | 2024-11-10 01:17:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0e316f02-681c-3edf-9bbf-80c462d42d47 | -1.83848 | -52.06283 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 26156aa0-807f-3949-b7c5-3f4e3db9bfdb | -5.06094 | -44.30151 | 2024-11-10 01:19:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| fe17d4ad-5089-3ca2-a229-d91ad504c79d | -0.91252 | -51.66087 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e0576c71-3a7b-318c-a337-b2426201bf07 | -4.86879 | -49.98304 | 2024-11-10 01:19:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4fc788ad-6d97-35e3-83d9-fe8645d89c13 | -3.16092 | -54.48943 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b0b5ca22-bbca-365b-bbfe-57e5c3d70b9e | -3.09746 | -53.31153 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 813b5bc3-9587-3dcd-bcdd-bc1b1045c866 | -1.14588 | -53.78213 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| fe175e69-d976-3490-a32e-06dc07d33d08 | -2.74055 | -49.02322 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 84eb2262-888c-35ac-9017-11907d451693 | -2.30303 | -53.82328 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e5bae9c1-ced3-3a06-b39d-1954aeb74729 | -2.81747 | -52.96793 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5ee13ce8-c13b-3329-89f0-a39a52906ace | -2.26747 | -48.74583 | 2024-11-10 01:19:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f9c15af7-c92e-368d-b4f8-f9281723de8c | -2.86813 | -51.82441 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a185bc6b-6f9a-3650-b6cf-6a1d98b8d1a2 | -4.12902 | -53.50641 | 2024-11-10 01:19:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 51e8edf4-37c5-3a46-8d6e-1e3e4ea076c4 | -2.80443 | -52.53529 | 2024-11-10 01:19:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| cd1b4b25-d5fe-36ea-9169-1df558e346f8 | -1.24445 | -51.77716 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 0a33b04c-2482-3523-b6e7-7f36ef8e0e3e | -2.23418 | -53.79216 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1d671691-dd49-38c9-b5aa-b4c4cadb78ec | -3.30047 | -53.70843 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0108f5db-5648-3a17-a257-a5648ba051c6 | -2.20692 | -53.7297 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d89cb859-7130-349d-adee-cb254e8c435f | -1.83375 | -54.35376 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c9ac2007-89b3-3913-8edf-e05365ef3608 | -2.87149 | -50.40485 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8ba1a124-aa1f-3d3f-b27f-fe6c0887ff68 | -3.66712 | -50.26192 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a2822fab-60d9-330c-aa9e-7817b8cfa473 | -2.92257 | -51.48715 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| fac38138-1244-3df5-948d-17f84cd3b215 | -2.6829 | -51.81653 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0439dafd-ff61-3ed1-a1ec-3c3cec830702 | -3.89054 | -52.40078 | 2024-11-10 01:19:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9c18c7da-2af2-3a41-9f22-12da939a72b7 | -3.23522 | -50.2976 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 9eb199ae-bc1a-3c0e-81ac-a4e555e01396 | -4.62387 | -49.09033 | 2024-11-10 01:19:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 01b6fa51-3414-3b47-b8ea-fde20167ae6a | -2.94973 | -54.68476 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 9a251e37-c096-3ff6-9ae4-314ecba66203 | -2.46882 | -50.39921 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 2c4e1652-41b4-360b-9e96-9cf2914ad84b | -2.63903 | -46.77698 | 2024-11-10 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| a673bbed-53ca-31ac-8f04-3d64ec0a690a | -2.87353 | -50.41924 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f23f831c-2c2d-3db2-b199-422a9efcdc57 | -1.20007 | -53.71009 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 42011981-5ac7-39e1-94e5-43c060f5d980 | -3.2361 | -53.05362 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c646b2cf-64c4-3855-8586-345593017d01 | -3.4518 | -51.47103 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 083cff6d-0ef0-38c8-8b0c-585ce1ffd9f4 | -5.06231 | -44.2941 | 2024-11-10 01:19:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| e96779a5-dc56-3159-98a4-9c6cf73ea4cb | -3.1974 | -49.4706 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 041dabf7-ca9a-3ccf-966b-0499df67b0a4 | -3.36132 | -49.50195 | 2024-11-10 01:19:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8edabe6b-a354-331f-b0e6-acd7de0c0fe3 | -1.48649 | -51.74258 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 4f5e1291-a39e-390e-8ca5-a5102c54a2fe | -3.23057 | -53.28032 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 35beb5e3-e92d-33c4-9cba-4d1a2fff8621 | -2.84044 | -53.97818 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 5af8b766-7f2d-3c3f-ad00-0a837fc43b0c | -3.34968 | -50.1339 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e52ca282-96a7-3cbe-999f-2f8f4928e9e2 | -3.76333 | -52.66948 | 2024-11-10 01:19:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 644a2a35-bd8e-36cb-a2f7-0218aa1549be | -3.35459 | -53.43881 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0764b1c8-709d-3e4e-8e86-8dd42b9ba395 | 1.57642 | -55.93048 | 2024-11-10 01:19:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ddec5522-465b-3003-ba3a-605064871a42 | -3.78012 | -53.7117 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b2ebb27f-f84e-37fa-b266-bb7dc3beea73 | -1.40027 | -52.36829 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 1caedc07-734e-3e82-a2fe-aa8d13eb3258 | -2.71861 | -51.99658 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 61bcebfa-c407-3f0b-bbb7-addc5150caa9 | -2.18597 | -53.64682 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d6a0fd9f-4948-360d-97ac-cbdc9e29974f | -2.27826 | -50.67862 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 60aafc9a-e060-3b70-9848-b30ebb168a55 | -3.26382 | -53.71021 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| a21e2201-c659-377d-8fb1-884246548316 | -3.82427 | -55.67576 | 2024-11-10 01:19:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b7f4f810-abe3-3583-a8fa-7ccbafa2e71b | -1.13183 | -54.21013 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 4395f142-15eb-3845-8c0a-16334c30d7ab | -5.16817 | -50.68412 | 2024-11-10 01:19:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8c36645b-0a70-3422-b64a-553fb86b524a | -3.2443 | -50.27484 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| bef73aea-370c-3c4d-b11a-40d764dea90a | -2.92137 | -54.41798 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 50e9f9a0-eec6-31d4-935d-efdfeeed40ee | -3.09431 | -54.27237 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 88b85464-01a5-366a-a79a-ec07d86cb9fe | -2.06245 | -53.29046 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f853de3e-72ed-381a-af76-fd59b09f4f01 | -3.10102 | -49.43981 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 033ca242-2b2c-34e1-be34-ee2c1426170d | -2.76584 | -49.36704 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| d86c6e33-0042-3493-bc8b-af8db44835b7 | -2.92981 | -52.77236 | 2024-11-10 01:19:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 8f906214-cd80-3718-96e9-295c2db6375f | -4.88339 | -48.61213 | 2024-11-10 01:19:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| d6802c72-0c62-3580-9a78-dece783b8afd | -1.84014 | -52.07427 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| cf14b3e0-330a-3a2b-bae6-881006ff5596 | -1.26194 | -55.87706 | 2024-11-10 01:19:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 07799a2b-c762-3edb-a161-2ced17b364c6 | -2.31984 | -53.87732 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 92ad8ffa-0d47-3a5a-adda-fcfb5729056f | -1.32046 | -54.63706 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9ee43cac-0b61-330f-806d-017b26c63a9f | -4.62892 | -49.08377 | 2024-11-10 01:19:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 2e0b43b9-ed70-3f22-906f-3e506e814943 | -4.20824 | -48.13732 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| e85b402f-2a65-37fa-84a5-8cce3efefbdc | -1.31383 | -52.1862 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e8451f39-8b31-3fc5-aa91-de8e079229aa | -3.01699 | -53.26051 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 27e2f71c-d739-3b22-956c-f65e71bfa586 | -3.08292 | -53.2746 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0ea22e81-b6a6-3c92-96d2-93c318f661c0 | -3.43898 | -53.05197 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 5eeee74c-15d9-389d-9dd0-0f64743cf548 | -2.10157 | -46.5384 | 2024-11-10 01:19:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 454488a7-4a74-310e-ab62-5aa248505694 | -2.40068 | -50.32472 | 2024-11-10 01:19:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6687160d-0fc4-3663-8340-887ea2801da5 | -3.82612 | -49.85804 | 2024-11-10 01:19:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 34a145ca-b9ab-3881-b269-282913bdb862 | -4.10226 | -45.70232 | 2024-11-10 01:19:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 42.1 |
| a72b53de-11c5-359b-8ead-e7332a70e47e | -1.45176 | -55.32012 | 2024-11-10 01:19:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| db8e9ed5-cffa-3b9d-965f-197513969150 | -3.54467 | -49.97051 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e3061965-eedb-3f70-bf42-c100a7cbe131 | -1.29876 | -54.67631 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 930f105b-f850-36a9-bdee-31189127c80e | -1.54209 | -52.21062 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 3350b2e6-5f25-32ef-9ce5-f37c7c1931bc | -3.0291 | -54.20581 | 2024-11-10 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a1da8779-8166-3c8d-ab14-5939a84f4f89 | -3.62854 | -54.79771 | 2024-11-10 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80d437e8-cce3-3d9e-b764-2abda2e88441 | -3.02509 | -53.26336 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 92940f51-ca40-3bc2-9037-70cb0daa64fe | -3.51276 | -54.03635 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 762ff482-8f2f-36dc-a692-0cf60f036ced | -1.28585 | -52.20821 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 30507e0f-0e9b-379b-a608-779af135dfa1 | -2.81235 | -52.99882 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a595e86e-7b4c-31b6-846a-da03dfd5c4e4 | -2.56795 | -54.73354 | 2024-11-10 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b5011bac-2ec9-3a56-a791-99f7fee3753b | -1.47772 | -55.44185 | 2024-11-10 01:19:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ee1b9236-3058-3e43-8d53-6acae2a59de5 | -4.85599 | -46.99332 | 2024-11-10 01:19:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 223.3 |
| 5be42909-1ccc-3259-91d7-2724676cca2a | -1.97907 | -49.01151 | 2024-11-10 01:19:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3a4bcc2d-a7d4-3491-9bb1-d623e056fe2e | -1.6438 | -52.06275 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 220dc74a-7794-3910-9a0a-e244a8bfc9c8 | -3.06532 | -48.01835 | 2024-11-10 01:19:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 03ad51e8-a724-3315-b7a4-97a05f7279cc | -1.61791 | -52.23964 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6278f292-401d-3a96-9ea6-cb171e5a0373 | -3.29648 | -45.65275 | 2024-11-10 01:19:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 66997547-dc80-34a6-b7ea-805dc06a2fd0 | -4.04878 | -51.06993 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 37eb6883-c3b7-30d5-9aa5-3aeb0bea9313 | -2.36292 | -46.86531 | 2024-11-10 01:19:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| c3ed76d0-7ba2-3158-862e-6af44ee7678d | -1.46048 | -51.48161 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |


[Clique aqui para ver as próximas entradas](README9.md)
