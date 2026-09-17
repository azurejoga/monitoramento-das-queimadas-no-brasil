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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2585a8e9-53ae-3a43-8950-7ce4949d6bce | -9.4102 | -62.7113 | 2026-09-17 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 104.5 |
| d027eada-d4b7-303f-80f0-aba974d29891 | -1.6022 | -55.5682 | 2026-09-17 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7e094e32-d6dd-3515-9de2-a602ccf4a87f | -2.6966 | -57.6084 | 2026-09-17 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3969887c-3292-31ff-8930-5c998a4ce12a | -3.4757 | -54.7171 | 2026-09-17 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 082feaed-5702-3ef5-8d70-6c8dff04db63 | -6.8031 | -59.1886 | 2026-09-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4c111958-43e6-3240-8d34-224cb30d2073 | -9.2753 | -60.6355 | 2026-09-17 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 5933c2ae-3da1-3ce9-b0bc-82a72356f576 | -12.8543 | -44.386 | 2026-09-17 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| dfb29817-aeff-31a4-9f18-a309f8b65b7a | -9.1123 | -45.7067 | 2026-09-17 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| b0fd47ea-3ae7-3775-8d09-2a549295a1d8 | -6.8215 | -59.1879 | 2026-09-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 730b1709-c8ea-3543-842d-5e5f72a1ebc9 | -9.1056 | -60.9703 | 2026-09-17 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 99d2f957-e70c-3e33-bc44-642bc9f62958 | -12.5101 | -50.8236 | 2026-09-17 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| ec7b5c4f-9a88-3e1e-834f-708f83a78031 | -4.5045 | -54.9646 | 2026-09-17 00:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| f723617e-2ef5-350c-8f66-e08ce2935872 | -6.3657 | -58.2771 | 2026-09-17 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d9a0da5c-b3b8-324e-b6bd-d1432e9d10a9 | -2.9581 | -50.3359 | 2026-09-17 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| daa34645-6501-3327-9ae6-502c22dab922 | -8.7604 | -66.5623 | 2026-09-17 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 931abb19-bb3e-3ddd-abf5-3267b1d95837 | -8.4982 | -57.6468 | 2026-09-17 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 6796d9cb-69cc-33da-9b83-e36f51e8b17d | -6.8216 | -59.1686 | 2026-09-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| cdf12061-5ed5-3d23-ba18-d4f34b83debe | -12.5289 | -50.8427 | 2026-09-17 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 9f7315fe-f3cb-3872-a6d2-ff9653b0c074 | -10.8532 | -54.0916 | 2026-09-17 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 37a4c5b7-be0e-39c5-a223-fd3efe5850e8 | -4.5587 | -42.9523 | 2026-09-17 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d68516e0-2c46-3a86-8fc1-a13fce7a2fa9 | -10.8154 | -54.0949 | 2026-09-17 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 47aeb72d-0d9a-30f4-a70f-4f357b424c6d | -9.1057 | -60.9511 | 2026-09-17 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 63971edd-645f-38fa-a478-a9dd666758bd | -3.494 | -54.7166 | 2026-09-17 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 0c6680f5-ad28-3f44-86e9-ad13e07d899b | -6.9309 | -63.0301 | 2026-09-17 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a1f4b25a-e73a-3e8f-a0de-216aefb14912 | -2.9079 | -54.1911 | 2026-09-17 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| c53c912f-0eec-3b88-b54f-efa86c928758 | -8.4796 | -57.6478 | 2026-09-17 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 27e28be6-3e8e-3151-9b6b-e57b53f767e8 | -3.4941 | -54.6967 | 2026-09-17 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 7df92021-e507-32db-a4a3-5de0c4dfc557 | -10.834 | -54.1138 | 2026-09-17 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 3b277812-5db6-333e-b4d1-e3fe506930b3 | -6.8032 | -59.1693 | 2026-09-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e2b89618-4deb-307c-8507-246204d68a39 | -9.131 | -45.7273 | 2026-09-17 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 43b70df4-e994-33ce-be0e-64f8b20ebba9 | -2.908 | -54.171 | 2026-09-17 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 5eefce1b-1d50-3bad-995b-dc08c3003b23 | -6.8962 | -59.0303 | 2026-09-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| cc50122c-1073-3ae4-b9a7-b83a3fb30bc1 | -12.5097 | -50.845 | 2026-09-17 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 145.0 |
| e259fff6-63bc-39fc-973a-1bc40ae2502a | -9.112 | -45.7294 | 2026-09-17 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 63a29a67-94ff-3c71-b1fb-03464b00f28b | -10.8343 | -54.0933 | 2026-09-17 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 5e4401bf-f933-33c5-abf4-06d4d648c241 | -10.8152 | -54.1154 | 2026-09-17 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d0e9479e-2b44-3221-9790-a03e54f94e02 | -6.9147 | -59.0295 | 2026-09-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ff43f5ef-db2e-373b-ad35-4111fa842a22 | -10.8529 | -54.1121 | 2026-09-17 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 0c38bb50-c9cb-3c88-a74a-1172ea9d0338 | -5.6472 | -44.7964 | 2026-09-17 00:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 9ca584a1-f66b-3095-b74f-58a94d829188 | -2.9582 | -50.3149 | 2026-09-17 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 3a0fe25a-a62c-3e01-916c-088acfc703bc | -2.6965 | -57.6278 | 2026-09-17 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| fd2818fc-2902-341f-a029-91eeae56652a | -3.4757 | -54.6972 | 2026-09-17 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 6ac92513-c8fd-31ff-856d-b229d420ed78 | -6.3656 | -58.2966 | 2026-09-17 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8b15a5e0-f129-3b7d-88a5-02d62c474861 | -13.66082 | -60.55651 | 2026-09-17 00:58:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 14e5d260-056f-3c79-b269-ba8151706cd1 | -14.86744 | -59.51002 | 2026-09-17 00:58:00 | TERRA_M-M | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4c58ef68-0626-33b9-88fa-2e4902175d04 | -3.4757 | -54.7171 | 2026-09-17 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 2491f198-f332-3226-ac2f-a5099958620d | -5.7752 | -45.128 | 2026-09-17 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 2ab3e71a-2726-3926-a58c-c36d2449cbfe | -5.7567 | -45.1067 | 2026-09-17 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 243.1 |
| 527de37d-ee3e-35d0-8545-574e61300419 | -4.54 | -42.9535 | 2026-09-17 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 2cb3e703-b78e-3038-91ea-32f913301492 | -9.112 | -45.7294 | 2026-09-17 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 9ac20aaf-3909-3cb3-a62b-6ee9d47687a1 | -13.3758 | -57.026 | 2026-09-17 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ee316527-e399-37f9-9aae-904dee7d0bb9 | -9.1056 | -60.9703 | 2026-09-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 0c3aeac4-8ce6-34e0-802c-29b65f639a3c | -3.4941 | -54.6967 | 2026-09-17 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 594785d1-5d5c-3bb6-94f8-049d1ce4e238 | -4.5587 | -42.9523 | 2026-09-17 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 312911ba-233e-3692-b7f7-29de7cf2c889 | -1.6022 | -55.5682 | 2026-09-17 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ce916d76-00a5-35c8-9e2c-e178187e486d | -6.9147 | -59.0295 | 2026-09-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 7655ed2f-d583-3848-8a88-031ad4796fd0 | -6.8032 | -59.1693 | 2026-09-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e556f778-38bf-3ea0-a8a7-ca8366563208 | -8.7604 | -66.5623 | 2026-09-17 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| c520d1b7-505a-398f-ac98-9cca99511f1f | -9.2753 | -60.6355 | 2026-09-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c16010ac-51ff-32a6-a407-df0f11a2aa3e | -6.8215 | -59.1879 | 2026-09-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9aea6dec-7226-3156-845a-6a9d2ddf33cf | -5.7754 | -45.1053 | 2026-09-17 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 470.2 |
| b4b425df-9200-3f97-b12b-9e9a808ddf6f | -10.834 | -54.1138 | 2026-09-17 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e979976a-00a1-33ec-bd13-518370ee396e | -2.9582 | -50.3149 | 2026-09-17 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 38f53073-f067-3f2e-ac37-2e52509e278c | -14.1405 | -48.7317 | 2026-09-17 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 0e06f8e6-d3e2-3e14-b4a0-28a588611ffd | -8.481 | -44.9102 | 2026-09-17 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| aa3af583-ab1d-3980-b6ef-8713deaf1c45 | -9.4102 | -62.7113 | 2026-09-17 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |
| ba7ffd29-0568-30e0-b9ee-51761aba0363 | -4.5589 | -42.9289 | 2026-09-17 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| d8784869-0204-3a16-85c0-d0fbdab758e9 | -9.131 | -45.7273 | 2026-09-17 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| da4543d4-1098-3d8e-9378-ef41523e8528 | -5.7756 | -45.0826 | 2026-09-17 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 61cf9356-1239-31f5-b56f-98731116dd77 | -12.8543 | -44.386 | 2026-09-17 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 71413923-3f27-30a3-8ce8-9421354d9e2c | -6.8216 | -59.1686 | 2026-09-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 31a3abfa-bf2b-36b9-b2c9-8e210e90881a | -6.8031 | -59.1886 | 2026-09-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 78f1be9b-80df-330f-95cd-d8ff52dc889e | -4.5045 | -54.9646 | 2026-09-17 01:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| e106172f-3e5f-3bc5-974e-6b7d6431fb33 | -6.8962 | -59.0303 | 2026-09-17 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| dd4561e8-6564-3bb4-a4b9-6dee80fcd1e2 | -2.908 | -54.171 | 2026-09-17 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| ddc68d9f-68c5-38c4-bce0-87e85e5c584a | -8.4621 | -44.9122 | 2026-09-17 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 5cb36ce0-28d7-36a2-89d2-d14249a13d6e | -8.4982 | -57.6468 | 2026-09-17 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 059bda95-1a42-3c60-bc99-bbfcd139b614 | -5.7565 | -45.1293 | 2026-09-17 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ab2671c8-ac03-367d-8066-4393aab79281 | -13.3949 | -57.0242 | 2026-09-17 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e3dc06bc-f3fa-3f36-a5bf-50d35d2464e7 | -2.6965 | -57.6278 | 2026-09-17 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| a3080303-74c8-3f3d-8a8d-d9eb0d083ecf | -5.6285 | -44.7977 | 2026-09-17 01:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 51be318f-c159-37d8-8a58-3bd3127db1eb | -3.4757 | -54.6972 | 2026-09-17 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| d2062b86-5c28-35d7-bf8c-da7ff3922b84 | -5.6472 | -44.7964 | 2026-09-17 01:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 0d7bf2c0-c0df-3b2c-b26c-44fa8bbc62a5 | -8.4983 | -57.6271 | 2026-09-17 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 135d4390-5851-35c3-aefd-f44934055b5a | -9.2939 | -60.6345 | 2026-09-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 669273d7-d203-33f4-b04a-f5d66eed6ec6 | -6.75 | -58.8043 | 2026-09-17 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 30d9d2d2-b668-3a19-9b4b-554a0139bb99 | -9.1057 | -60.9511 | 2026-09-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| bf6bc398-d8fe-34a3-b842-be5b18f20a38 | -9.087 | -60.9712 | 2026-09-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| db9d5bf5-ee3a-33eb-8b11-add166445ddb | -5.7941 | -45.104 | 2026-09-17 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 00b0809c-ebc8-3a2b-9389-92d6fb1788f7 | -10.8343 | -54.0933 | 2026-09-17 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 72840e34-eb03-3472-93f0-2442eb63cbba | -8.4796 | -57.6478 | 2026-09-17 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4ebdd581-672d-3dd1-b56f-f183dbc15ee5 | -2.6966 | -57.6084 | 2026-09-17 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d7121d3b-3e4a-3f9c-8c41-0445a112651d | -9.0871 | -60.952 | 2026-09-17 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| bc5f68ee-fa94-3a02-91aa-8f0c32446757 | -6.9309 | -63.0301 | 2026-09-17 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 3d0caa0e-7e3f-36ee-8b11-0eda898d56fe | -2.9581 | -50.3359 | 2026-09-17 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 70849108-99b1-3685-a04e-5ff24ba901cb | -3.494 | -54.7166 | 2026-09-17 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 108d4160-be21-37af-9f52-f9f737b4675d | -10.72297 | -54.02219 | 2026-09-17 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 5947a0c3-faaf-3546-97a9-a7e6048a8815 | -10.57983 | -57.70451 | 2026-09-17 01:00:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| af96dd8b-a3a3-3a42-babf-7ae491f05bae | -10.69239 | -54.18172 | 2026-09-17 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| d615ba4e-8649-3b63-a3c2-d0fd89473cf8 | -10.82229 | -65.0313 | 2026-09-17 01:00:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README5.md)
