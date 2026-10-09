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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4f89f09-f75e-3200-946a-ea9c68bd6fdc | -7.218 | -55.1617 | 2026-10-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 9a34dba7-198d-317e-86be-400a65fa4220 | -3.1787 | -50.5807 | 2026-10-09 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| f61408db-3085-3be4-80da-0d7490b23c5f | -2.499 | -56.0675 | 2026-10-09 01:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c3c480eb-b619-3757-a54c-73463bd29e4c | -3.1879 | -58.6433 | 2026-10-09 01:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2b64f611-e566-34a7-9a14-14a49bbfaabb | -3.11 | -54.1862 | 2026-10-09 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f7fbb198-8d94-3be6-a5d9-49b56c11751d | -9.297 | -47.4313 | 2026-10-09 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 2a8343c1-b280-3838-8a4b-32c5df48c2a7 | -3.5493 | -54.6951 | 2026-10-09 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 8f16be1b-0c20-3c9f-a7ff-4d32e1312715 | -4.2953 | -49.1021 | 2026-10-09 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e4b93a70-d7b9-3e83-94aa-a6a3dabfb616 | -3.5677 | -54.6746 | 2026-10-09 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| ad86ac8e-3b5d-3a45-8026-bc30a26710d2 | -3.0002 | -54.0684 | 2026-10-09 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 07ccc172-259e-3aaf-a1af-da21ce0dd667 | -8.7423 | -45.1334 | 2026-10-09 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.3 |
| bc4129ca-0cea-336a-9f1c-03d00e654168 | -6.4903 | -62.8554 | 2026-10-09 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 682b3756-9ffe-3563-9dbc-9fba69910e96 | -6.0024 | -40.935 | 2026-10-09 01:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 8d43bc61-fcf3-357b-88ff-447a6bbe06a0 | -13.1668 | -43.2673 | 2026-10-09 01:00:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 66.6 |
| edc2696a-a0f3-3d49-820a-65e0d64fd848 | -8.742 | -45.1563 | 2026-10-09 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 764fa4b5-a7d6-3457-b3a9-a316dae758ce | -3.1114 | -53.7839 | 2026-10-09 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 87e7fac9-3bee-337b-9985-5e6e0fc827ed | -12.0054 | -43.4878 | 2026-10-09 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 80398bd8-8c61-36e7-aa1c-60a89c488d48 | -11.6562 | -43.6846 | 2026-10-09 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 41d7546f-07a2-36c5-b2ec-df846bdf4985 | -13.1636 | -54.3591 | 2026-10-09 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 085b1ca9-579c-30dc-ba15-49af3c8d3321 | -10.6199 | -60.4852 | 2026-10-09 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 3ce8123e-620b-34ad-b9f0-23cb65a4694a | -8.9107 | -45.2519 | 2026-10-09 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| cb96c5d4-381b-3868-a216-f6c1c824af14 | -5.7117 | -53.4862 | 2026-10-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 2ae52c2e-cac0-3338-974b-7e16ad56721c | -5.7116 | -53.5065 | 2026-10-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| eac71a2e-a181-3edf-8a76-c0802d897a64 | -3.1971 | -50.5801 | 2026-10-09 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 60628cd6-42e3-3476-8236-6ecd57c47f94 | -6.0739 | -47.2922 | 2026-10-09 01:00:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 49e375ae-805e-30e9-b481-be2003a5159f | -1.1094 | -54.1601 | 2026-10-09 01:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 35606326-1522-3904-9659-2ae4500a0291 | -5.6932 | -53.487 | 2026-10-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 234e696a-41da-3387-8fba-248a3eb1806d | -7.1825 | -52.6283 | 2026-10-09 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| ae2b88d8-e187-310c-8bc4-f28700003985 | -3.364 | -50.4072 | 2026-10-09 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| f9aea875-cda1-38dc-9a60-e1200ba5f95e | -9.2973 | -47.4092 | 2026-10-09 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e3faf11f-1b06-3547-8f8f-47e0d4db11a6 | -3.1786 | -50.6016 | 2026-10-09 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| d9192347-792d-34b8-b51e-85785e79e8c6 | -6.4949 | -55.2995 | 2026-10-09 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2b916717-3cec-304c-9511-161966f26a22 | -3.2577 | -54.0217 | 2026-10-09 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 51e40ebb-2752-3097-a622-e771ffa5ef06 | -3.5676 | -54.6946 | 2026-10-09 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 706df79d-1eb5-3ad3-b3c1-ce8ab1a0c07f | -7.2187 | -55.0815 | 2026-10-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 75574132-b2d6-37e3-977f-e2984d465630 | -6.0019 | -40.9837 | 2026-10-09 01:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 5f16b25e-0766-375f-b09c-7fc795e8a00c | -7.2182 | -55.1416 | 2026-10-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 75408973-1bb4-30a9-adeb-41ab33cbd5b4 | -8.911 | -45.229 | 2026-10-09 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 365.2 |
| 5af868ac-e1c5-369e-9ecb-1b6d0354c8fc | -4.2954 | -49.0807 | 2026-10-09 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 7fb59845-77b5-34a3-8b6f-93906558c97d | -3.1284 | -54.1857 | 2026-10-09 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 9bd62d48-aade-32c5-893f-506e8d2d8db6 | -4.6096 | -49.2156 | 2026-10-09 01:00:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d3236747-d6e3-3464-b6c8-f7b61b1199d5 | -2.7428 | -54.1146 | 2026-10-09 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 76bd93f5-5d58-317b-9cf7-308cd12944f1 | -6.7365 | -55.1474 | 2026-10-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ce383007-3b2c-3697-b48c-d619953c74fb | -13.2015 | -54.3757 | 2026-10-09 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 6acd3bf6-64b9-3e50-9f2f-6d1bece0d67f | -3.0925 | -53.9455 | 2026-10-09 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| c288511e-1a50-30a5-ad0b-37fd16d55f93 | -15.4287 | -43.2373 | 2026-10-09 01:00:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 113.9 |
| c96b2d43-ea7e-3d69-a715-1111c2b979df | -11.7601 | -61.0743 | 2026-10-09 01:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 99a42b3f-a852-311e-bfa1-874816df5376 | -8.8921 | -45.2311 | 2026-10-09 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 219.0 |
| cd839a66-91e9-3ecc-a9d9-dbca38e5bff8 | -6.4948 | -55.3195 | 2026-10-09 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 99288deb-e2b6-330b-a0e3-8bb55f1c2e18 | -11.6562 | -43.6846 | 2026-10-09 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 14316d17-1f37-390c-b037-2dcf02ea1345 | -3.1972 | -50.5592 | 2026-10-09 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 8b0bf760-4675-3665-8dd9-5bbda74ff5d0 | -7.1995 | -55.1627 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 7068569b-4abf-303c-ad83-6a2568990ffc | -8.7231 | -45.1583 | 2026-10-09 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 239.2 |
| a4971745-1928-386f-aecb-f037f7735e27 | -3.1284 | -54.1857 | 2026-10-09 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| c82d1588-89e2-34d1-a8ba-d7200d77e3be | -3.1114 | -53.7839 | 2026-10-09 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 2d32ac2b-14be-398c-a331-fdee6af0e992 | -11.6177 | -43.6906 | 2026-10-09 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 80c22dd1-be12-3148-9407-e99028ac2162 | -3.1971 | -50.5801 | 2026-10-09 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 1cf70379-414d-361f-802a-23e33dcbfe17 | -15.4287 | -43.2373 | 2026-10-09 01:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 80525a41-a038-3067-ac2d-d882c731726f | -8.8918 | -45.2539 | 2026-10-09 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| ed6a6eef-4ff3-3609-910a-028fc13623e9 | -1.1094 | -54.1802 | 2026-10-09 01:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a6c033a8-d8f2-3078-a56c-804699cb3f60 | -3.11 | -54.1862 | 2026-10-09 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 17c1dab2-5f41-35a9-82d6-79508f30b73c | -4.2767 | -49.1029 | 2026-10-09 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 25adadea-a4af-3837-9a65-cfe2bb13e6f4 | -2.7428 | -54.1146 | 2026-10-09 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 4e449ff0-ceb5-3d3e-836e-38fb04bfa479 | -8.911 | -45.229 | 2026-10-09 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 248.3 |
| 4f69d260-4bc0-3bb2-86a1-dbcddfadc731 | -6.0019 | -40.9837 | 2026-10-09 01:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 116.1 |
| 49625efa-871b-3fc3-9511-2bbb12802703 | -9.2973 | -47.4092 | 2026-10-09 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| af2a0ce7-32b8-3fb3-9d78-10d1d42797da | -3.5493 | -54.6752 | 2026-10-09 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 18198536-1519-3267-9e93-da70d4d690bd | -9.297 | -47.4313 | 2026-10-09 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 66ff44c4-e7fd-3b76-a068-15298f1d32cd | -5.6932 | -53.487 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 28d488ec-787c-37d0-b7a8-51ff8fba76af | -13.1827 | -54.3571 | 2026-10-09 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| a0759a0a-6490-3ce5-8cdb-0da302fa8a2f | -13.1636 | -54.3591 | 2026-10-09 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 7caffd88-5382-3838-a98c-d9b52b151779 | -5.7116 | -53.5065 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 6e1f3faa-0e58-30c5-96b5-2e40683ce331 | -12.2156 | -57.1087 | 2026-10-09 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| bc30169b-2b70-33c5-b47e-5dcdf8b4de1e | -13.2015 | -54.3757 | 2026-10-09 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 52651b97-726f-3d2d-a7a7-a9afaed2dc59 | -13.1639 | -54.3385 | 2026-10-09 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| c71ef86a-7dae-3de6-83f5-7e1903e73d9e | -11.7603 | -61.0549 | 2026-10-09 01:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| c05a02af-db67-34dd-b347-80639090574a | -5.9587 | -55.3448 | 2026-10-09 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6694945f-a19e-3904-b4f5-ae0aad020695 | -8.9107 | -45.2519 | 2026-10-09 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| d831d9ab-454c-327d-ae55-085c6a7846b2 | -12.2158 | -57.0887 | 2026-10-09 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| d2de7d54-567d-3d7b-a339-ccfff09f1f6d | -7.218 | -55.1617 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 4a6d08c3-05ad-33fb-bb01-adc940484e2c | -3.1879 | -58.6433 | 2026-10-09 01:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 61849e0e-e98e-3852-ab70-978714c5f872 | -7.2182 | -55.1416 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 71dcc443-2127-3e7a-8298-f7d8e8626a35 | -5.7119 | -53.4658 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 85034447-2f7b-3b63-9c38-37c47f9d7fc9 | -3.1786 | -50.6016 | 2026-10-09 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0e3ab998-2c21-3a97-b123-1f07c69b5cb9 | -8.7234 | -45.1355 | 2026-10-09 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 229.0 |
| 331e9910-d126-31ab-8396-594f73bd9453 | -12.2154 | -57.1287 | 2026-10-09 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| cd7abee4-52b5-3175-b4a1-6ffe7b610584 | -3.2576 | -54.0418 | 2026-10-09 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b475ce15-1ca8-3f66-b944-6370877b122b | -5.7117 | -53.4862 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| ad9df4fb-73f1-378c-bcf3-9d54baadc406 | -13.1668 | -43.2673 | 2026-10-09 01:10:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 4c136048-df82-36d8-8cfb-66e6be75554d | -8.9113 | -45.2062 | 2026-10-09 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 80a6a964-31cd-3062-8e91-bf2e19367080 | -3.5493 | -54.6951 | 2026-10-09 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 27bff9d5-08fc-3b1a-97ee-9c845cec68cf | -6.4903 | -62.8554 | 2026-10-09 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 6952c6c9-3c11-3b0b-a62c-c19876474dcb | -10.6199 | -60.4852 | 2026-10-09 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 026cdb71-ca2f-3009-a2dd-e19d1f3f6596 | -11.6369 | -43.6876 | 2026-10-09 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c049aa2b-8cbe-3035-be76-c569c609264f | -5.6934 | -53.4667 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| bc33c9d2-9ea1-3737-be08-e30a41aa1f84 | -3.2577 | -54.0217 | 2026-10-09 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 371a3d0c-d292-3f52-8850-be055e20138d | -4.2954 | -49.0807 | 2026-10-09 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 3fc67183-0980-3ca0-a671-b3884eb28157 | -7.2187 | -55.0815 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 69dd9a12-2b0f-30db-a2f2-a056e2130642 | -11.7414 | -61.0561 | 2026-10-09 01:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 2581e662-8b4c-3c93-9bae-aebd5b443e05 | -11.8499 | -43.5835 | 2026-10-09 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |


[Clique aqui para ver as próximas entradas](README47.md)
