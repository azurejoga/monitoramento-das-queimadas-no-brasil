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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3db61c1-de6e-3cc4-b293-7b1e0f4eef28 | -20.99472 | -51.79355 | 2024-10-16 04:10:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 826f736d-5c56-3f62-9d31-75c54303d079 | -23.66426 | -55.24741 | 2024-10-16 04:12:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f25c4705-c42f-36e8-8da3-53fbc4e2fc06 | -23.66131 | -55.23602 | 2024-10-16 04:12:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1ff1ff1c-f185-3265-bc47-1ca175781156 | -23.66055 | -55.23938 | 2024-10-16 04:12:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ec809ad0-0a1f-3093-a044-e582b07456d8 | -23.6598 | -55.24277 | 2024-10-16 04:12:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aebf6812-7de4-3f54-9452-c2ac0a299032 | -23.65533 | -55.23816 | 2024-10-16 04:12:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84a99f1b-0c0f-3881-835e-b24b770e856a | -21.89173 | -56.10927 | 2024-10-16 04:12:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4849ec2-5639-3256-8c69-113f885db660 | -21.89077 | -56.11342 | 2024-10-16 04:12:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7e286fb-324e-34b1-b37f-2536df3cac18 | -23.27034 | -50.87102 | 2024-10-16 04:12:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1dd3b79e-bed7-3a89-990f-5cf96a4825be | -23.26632 | -50.87005 | 2024-10-16 04:12:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1701333c-8e1b-356b-8b04-5ebfa4c9fb5a | -23.0137 | -51.85992 | 2024-10-16 04:12:00 | NPP-375D | SANTA FÉ | PARANÁ | Brasil | 4123402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fa857ac0-70b4-371f-8ba0-fcc754f32a72 | -23.01254 | -51.861 | 2024-10-16 04:12:00 | NPP-375D | SANTA FÉ | PARANÁ | Brasil | 4123402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 817f1783-1413-365f-94be-d0c799931319 | -29.92044 | -51.1117 | 2024-10-16 04:14:00 | NPP-375D | CACHOEIRINHA | RIO GRANDE DO SUL | Brasil | 4303103 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| aceb4560-e8bd-3515-9f16-bf4e55a25d9a | -29.8165 | -51.17406 | 2024-10-16 04:14:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 29049568-d842-3687-942d-d13e9fc756ac | -29.69726 | -51.16059 | 2024-10-16 04:14:00 | NPP-375D | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| bd9e266e-867c-301b-9c89-05d27d4bc7bc | -3.1099 | -54.2263 | 2024-10-16 04:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| f0dd3e35-ce88-3171-9c41-0c472e73f08c | -3.1283 | -54.2259 | 2024-10-16 04:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 95951a2f-a075-37e2-80d0-8634c1fb4860 | -3.958 | -46.4442 | 2024-10-16 04:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| cdd1d11c-6a6d-3c4f-a722-cbf8fc84768e | -3.9581 | -46.422 | 2024-10-16 04:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| f3e7f1c0-a337-33ff-9844-355e157e76bd | -9.1728 | -65.3945 | 2024-10-16 04:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 52a6d984-e15a-3bc7-ac33-ff0c12046c52 | -11.7103 | -65.2424 | 2024-10-16 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| b3207968-5a8a-33d0-832d-4f8d8c444f86 | -11.7104 | -65.2235 | 2024-10-16 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 80c4172c-b88b-3f1d-bd97-e0385128310e | -11.7292 | -65.2227 | 2024-10-16 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2838c7b7-91d5-3455-9f96-9e44c600d623 | -11.6917 | -65.2243 | 2024-10-16 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| c55e5aba-5a0c-320b-826b-07f6bbf4b5f1 | -17.1664 | -56.8439 | 2024-10-16 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 77238bcd-c8b8-345e-ada6-0bf2091d8077 | -17.2081 | -56.6946 | 2024-10-16 04:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| d270dcc7-c48b-3f5f-b990-cb6a57a78dc2 | -18.254 | -56.6029 | 2024-10-16 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.1 |
| 004f4f8d-0839-3cc2-a7c3-886f3815f81a | -18.2544 | -56.5821 | 2024-10-16 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.0 |
| b83e737d-60ee-375e-bcfc-53502ac1461d | -18.2739 | -56.6003 | 2024-10-16 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.4 |
| 5b614719-a2e6-35bf-9d8a-1be001c3c929 | -18.2742 | -56.5795 | 2024-10-16 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.7 |
| 8bca7c34-b8bb-3da7-8c49-622d4f6d04a6 | -19.5812 | -56.9862 | 2024-10-16 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 224.4 |
| 07756d9c-0b7b-3251-b5aa-60b9a3637df5 | -19.5816 | -56.9653 | 2024-10-16 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.4 |
| 25f965db-d42f-32dc-975e-bbc186941293 | -19.6013 | -56.9834 | 2024-10-16 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.4 |
| 861452d9-1958-3f90-add4-d969f644e0e0 | -19.5808 | -57.0071 | 2024-10-16 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.8 |
| f82ee52c-78b3-3a32-a723-213be4c6f4db | -6.56392 | -35.11877 | 2024-10-16 04:19:00 | AQUA_M-M | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 625977ed-eab7-3e70-964d-ba03b792723a | -8.19185 | -40.99738 | 2024-10-16 04:19:00 | AQUA_M-M | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 42.0 |
| 108b288d-3b42-305b-9a52-ea4dab86bd8f | -8.18118 | -41.00046 | 2024-10-16 04:19:00 | AQUA_M-M | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 139399cb-210f-31d4-b2f9-688a149c2a24 | 1.0016 | -52.2164 | 2024-10-16 04:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 9fb126cc-dd7f-3f20-adac-18d90c195265 | -3.5107 | -43.2429 | 2024-10-16 04:25:26 | GOES-16 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 7c4c332e-5358-3f1a-b8ce-37cbd24371eb | -3.958 | -46.4442 | 2024-10-16 04:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| c0573e83-a631-335b-b6d7-5e00e78ec9c9 | -3.9581 | -46.422 | 2024-10-16 04:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 2b649080-522f-3622-b689-0a9522a127d5 | -9.1728 | -65.3945 | 2024-10-16 04:25:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 7bbeadc6-9125-3bfa-90d2-3f86d2bb2311 | -10.2439 | -47.3046 | 2024-10-16 04:26:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 8f57f265-e77f-37d8-87ee-5e27fa2bee20 | -10.2442 | -47.2824 | 2024-10-16 04:26:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| eae804f5-f6e1-380c-ad18-9998b8d51d4d | -11.7292 | -65.2227 | 2024-10-16 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 60720752-4ced-30c4-b406-915e3d4c21d4 | -11.7104 | -65.2235 | 2024-10-16 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| fcb45fcc-ac1d-34bb-90e4-32c26a54798c | -17.0188 | -57.4973 | 2024-10-16 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 5ea14910-e28b-3cc5-b887-f42cd18accce | -16.9995 | -57.4791 | 2024-10-16 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| a28dca99-9a08-316d-8115-131175729639 | -16.9992 | -57.4995 | 2024-10-16 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 794c77f8-619a-3cc1-b4eb-a20b48ac3ac8 | -17.1667 | -56.8232 | 2024-10-16 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| ba88a9a1-4211-39ca-a8fe-e2a8a6d4be0a | -17.1664 | -56.8439 | 2024-10-16 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 144.0 |
| 46a89454-5605-352c-98f9-6b5ed49572fe | -17.1467 | -56.8463 | 2024-10-16 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| e524b620-8d4e-3a6d-9098-0a4fe45b673f | -17.0387 | -57.4745 | 2024-10-16 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| ebcf913e-855a-3c59-a2a8-d269d009f2b1 | -17.0194 | -57.4563 | 2024-10-16 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 0cd7dd98-c6c9-3644-8db7-4ac0aa4384e0 | -17.0191 | -57.4768 | 2024-10-16 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| 4a0d545e-9f62-38c1-8fdc-08e77188bd19 | -18.2742 | -56.5795 | 2024-10-16 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| b077a7fc-544b-346b-bc78-9b3ce7d4e0a2 | -18.2739 | -56.6003 | 2024-10-16 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 01f59cc6-6166-3ec8-a146-d36bb9c8593b | -18.2544 | -56.5821 | 2024-10-16 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.2 |
| dae5639b-049e-339d-ab4c-787016cfabe4 | -18.254 | -56.6029 | 2024-10-16 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.1 |
| ebd23b9d-ee1a-3e60-9733-e7bf2c0fe073 | -19.6013 | -56.9834 | 2024-10-16 04:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 600662a8-3084-363c-a5bb-66e06533ccd1 | -19.5816 | -56.9653 | 2024-10-16 04:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.3 |
| 9c986b71-d3c5-3003-a66f-453c75ad829d | -19.5812 | -56.9862 | 2024-10-16 04:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.6 |
| e667c810-2ca9-33b7-a5c1-3de55434b433 | 2.28699 | -50.85561 | 2024-10-16 04:27:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a414fbdf-1700-3d69-8af4-4a368c200da0 | 2.28646 | -50.85213 | 2024-10-16 04:27:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6a596d5-53e0-3ddd-8f80-1996d8b149c0 | 2.28245 | -50.85275 | 2024-10-16 04:27:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98046a58-62d3-3b59-a750-827611d78817 | 3.55368 | -51.42549 | 2024-10-16 04:27:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11275231-c22a-3df2-851f-b80d11fb547a | 1.31004 | -51.24623 | 2024-10-16 04:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9379c6b6-69d7-3c95-95ce-c4bf1d4779f5 | 1.14078 | -52.73495 | 2024-10-16 04:27:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4e64842-e820-3c09-ac0b-64cffe6f93ed | 1.13816 | -52.73313 | 2024-10-16 04:27:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28a02038-e4b8-38f3-95a7-2cc68938b280 | 1.1363 | -52.73565 | 2024-10-16 04:27:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccff3d0d-b48a-3789-965a-ae001f4fb389 | 1.01213 | -52.21902 | 2024-10-16 04:27:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 19.2 |
| ff0b5731-f907-3311-a75a-e0c3972b231f | 1.01149 | -52.21494 | 2024-10-16 04:27:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 2cbd2007-629e-3d44-920c-4773f02ab039 | 1.00779 | -52.21957 | 2024-10-16 04:27:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 19.2 |
| e080e648-00af-3bca-a2d0-f3bf1423eaa5 | -3.93207 | -42.88118 | 2024-10-16 04:29:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 471f713e-8797-37a3-8327-eb06168e4559 | -3.66376 | -42.26501 | 2024-10-16 04:29:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d2d6614e-4865-3429-933c-76b8aef28a83 | -3.65975 | -42.26441 | 2024-10-16 04:29:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f33ada8e-4ed8-341f-a575-a42206332594 | -3.59828 | -42.81008 | 2024-10-16 04:29:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b989ceb4-1ca6-39a1-8e96-975fb6ad702b | -3.51652 | -43.2493 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b11bb32b-d8a4-313d-b29a-b2d60fd39118 | -3.51413 | -43.23959 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ee2a9f77-e8a2-3184-9d4b-17e475b9768f | -3.40881 | -42.76199 | 2024-10-16 04:29:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b3822e4-33db-33c8-8661-9450f5f16570 | -3.51344 | -43.24416 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7728dc91-db52-388c-8fba-19a8388334ac | -3.51276 | -43.24872 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62c49eca-bac7-351f-955d-1d3bac7ea666 | -3.51207 | -43.25329 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c6492a4e-c1cf-33e7-966c-0b89c4a973dc | -5.22753 | -46.15405 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a028c6d2-b276-340f-8f59-f021107599b6 | -4.98601 | -37.4149 | 2024-10-16 04:29:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8ad2803c-cc3c-39cb-9d83-41378b018111 | -4.72169 | -38.45842 | 2024-10-16 04:29:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 31994663-7e28-312d-8a76-2c41517e28c2 | -3.51036 | -43.23901 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 839f8df1-4c39-3dee-a3c3-0af8012b7455 | -3.50967 | -43.24358 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d64548d3-14dd-3e88-a691-c15d304a5f41 | -3.50899 | -43.24815 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0785043c-eced-39b3-80dd-463bcda4bdaa | -3.5083 | -43.25272 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0bc0adc8-7634-3da4-8401-57da1e6963f7 | -3.50737 | -42.97959 | 2024-10-16 04:29:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdf93cd8-e112-392e-a663-72a09742ee40 | -3.50659 | -43.23844 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 707892b6-757c-3c3b-9259-2515ae738afe | -3.50651 | -43.23562 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db9a6618-29ad-3cff-9f11-0fa8741dc233 | -3.5058 | -43.24018 | 2024-10-16 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e04a803-b7c6-35e4-9a5b-c125580d4398 | -3.29795 | -43.5126 | 2024-10-16 04:29:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbfdb2d2-061a-3dac-be91-84629a6fc993 | -4.72122 | -38.46163 | 2024-10-16 04:29:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a6f25b1-3fae-304f-a10b-6fb62d5750de | -4.79042 | -39.77923 | 2024-10-16 04:29:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 508b7740-9e62-3779-9c80-5d9895134ad0 | -4.78966 | -39.78457 | 2024-10-16 04:29:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3afaa34f-6515-37bf-b330-f3db07b70b56 | -4.78614 | -39.78369 | 2024-10-16 04:29:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5466b812-1458-3b2d-84f8-48fbbf70f16e | -4.78533 | -39.789 | 2024-10-16 04:29:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README41.md)
