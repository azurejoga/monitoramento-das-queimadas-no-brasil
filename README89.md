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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4872e2d-76c1-3ff2-aeb0-46404d2b0c30 | -9.1717 | -59.5405 | 2025-08-26 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 548b9864-037c-320d-909a-324a7ea85412 | -8.8548 | -62.4503 | 2025-08-26 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 149.0 |
| b005a976-676d-3773-bef2-95fa5cf557ad | -9.1715 | -59.5599 | 2025-08-26 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 7f2c2951-af85-3b12-921f-8fe0be14bea4 | -6.2275 | -60.018 | 2025-08-26 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c33751b1-0090-37a0-ab21-68b3bf4f2653 | -6.7635 | -59.6718 | 2025-08-26 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 43dc9791-3619-3291-828f-fcc9cfb98cf2 | -4.9605 | -55.8226 | 2025-08-26 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a3e8bc19-c0f5-3f3f-83a4-a1ff9e53a7fd | -8.8734 | -62.4495 | 2025-08-26 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b9b1fa18-0e25-3113-8a25-db7718f25c6a | -9.1903 | -59.5395 | 2025-08-26 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0ce0d587-5f04-3188-b2da-c01ce50ef1c0 | -9.1722 | -59.4629 | 2025-08-26 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8f6055dc-b3f1-3f0f-b0f1-2e5084714cf4 | -8.8364 | -62.4321 | 2025-08-26 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 429023e5-620d-34bc-a9a3-bda7dfb0c27a | -8.8363 | -62.451 | 2025-08-26 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| e9743618-ade9-3dc3-b960-f58e2ae842c2 | -8.855 | -62.4313 | 2025-08-26 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c222c628-d602-3695-853a-c021bf5524bf | -6.2459 | -60.0174 | 2025-08-26 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| dffd33d5-f5d4-38de-a065-6d71c3edfb4e | -6.26112 | -60.01205 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8528a4f4-41d7-333b-a3f8-4572eae24959 | -6.69957 | -58.55219 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f0db748-752c-3071-832d-0911590b4789 | -6.69335 | -58.55121 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 212f3202-fd77-3741-a62d-947e724592e2 | -4.96342 | -55.82419 | 2025-08-26 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cd54dcfe-946b-37a4-a783-329e2ac33714 | -4.95723 | -55.81619 | 2025-08-26 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d668155-66c5-3427-b637-36b4ef5631e7 | -5.31408 | -60.20451 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd33127e-8495-3230-9b9a-fd818eaf80f1 | -6.77721 | -59.65213 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db61f075-282f-3732-b84a-0e12b9891eaf | -6.91864 | -59.36438 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6946551b-5b64-3321-b2c8-189f8b16f69f | -6.24773 | -60.02542 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e68f352-c2c0-381b-b02e-966403d93ac7 | -6.91331 | -59.35918 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72961aaa-6ab3-3725-802e-d435fbb82af9 | -6.76973 | -59.67038 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 18db43c0-2f41-3201-985b-d76d309f46f5 | -4.96538 | -55.81034 | 2025-08-26 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 875fc172-4543-3a1e-9623-795a91c8a4c2 | -6.76393 | -59.66947 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ff8f5324-6189-3ccf-8ccf-2caf540c219c | -6.71186 | -58.57484 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a617c596-d5ca-336d-8ddc-2f52072180d3 | -6.76861 | -59.67204 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2e80ecb3-e924-3ea7-8d81-f6177c3c1c25 | -5.31512 | -60.19747 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae25162c-0b4f-3ce0-8f08-81768a16fe76 | -4.9666 | -55.8152 | 2025-08-26 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0958392a-2575-373f-9212-fcc94ed6e277 | -5.52638 | -60.2122 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4fd820d-709a-38c2-9871-74774beac676 | -6.76917 | -59.66784 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b8b16950-1855-3751-bb1c-1b86899f736c | -6.78084 | -59.66917 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 947cf948-1c07-3298-81af-bf019ca1038f | -6.24367 | -60.01337 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7d496bb0-258a-3c57-a11c-cd403d528c4a | -5.44383 | -60.15919 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a71dba8d-7c11-38fc-bead-c96e42d3789d | -6.26166 | -60.00826 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6b94858-7af1-3a97-bd30-5a0b5765c2c9 | -6.23749 | -60.01644 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| feec9d97-4157-3598-a8ea-498d91990366 | -6.70694 | -58.56457 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c1d69b46-3739-32e7-93f6-1b2eb15d0c98 | -6.69515 | -58.55796 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9c8d815-e3b5-3dec-912b-ee8c4037c8bb | -6.69895 | -58.55695 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a2d2a0d8-515c-3cce-8434-1188cacf89d7 | -5.52591 | -60.21489 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9298508e-0cd5-3901-ab3b-709cced83b6d | -6.9105 | -59.36089 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 027cf82a-c3e8-31c0-b65f-11de67d4adb4 | -5.5324 | -60.20939 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e756d44-3755-340b-a286-e44577fcde4b | -6.77775 | -59.64806 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 806793ed-d815-32e0-abbf-dcacc563350a | -5.30308 | -60.203 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 103907ed-97b7-33c6-8f1a-171e369e77a3 | -5.44434 | -60.15559 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dae4ee2b-d6e2-3a29-b0f9-85d334ccab86 | -6.71316 | -58.5655 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2b95f15-e3a7-3068-87e1-ee20f500bafb | -6.78555 | -59.67818 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a49afa81-f363-3edb-af68-534fb4557107 | -6.70951 | -58.57306 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3b5b3950-a766-3395-a3da-fdd188b61923 | -6.76915 | -59.67451 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 997b1563-1ed8-3eaa-bf5b-74871bec15c9 | -5.31514 | -60.19998 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3f82116-9454-327a-8d24-251ab3609b7a | -5.30412 | -60.19589 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66bdcb2c-2dc0-3f32-be20-7b3e6d2023b2 | -3.3955 | -59.45137 | 2025-08-26 06:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bd9ecee-8827-3350-a924-50701d4dd601 | -4.96438 | -55.81739 | 2025-08-26 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02345d8c-720b-3d6c-8525-42c6936befd9 | -5.52588 | -60.21579 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ece48671-0ff5-3cc2-850a-d40187aa5e18 | -5.30364 | -60.20196 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93f720b4-fca7-3e3b-8bb6-5a26556b3bf6 | -5.44986 | -60.15639 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c3ebe36-b463-30fe-ac7a-2d6de9f85540 | -5.30414 | -60.19839 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89300f84-a600-34bb-91cf-b9b53006cd67 | -5.29815 | -60.20114 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4467e93a-7140-3bea-a85b-cdb4019595af | -4.96038 | -55.80708 | 2025-08-26 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 994acb92-0be5-3c46-b9c6-0d510e4537a5 | -6.7894 | -59.64966 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 967f5ada-1778-3f5d-8263-178cfedb3b16 | -5.52697 | -60.20771 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa2abab3-6a50-3686-9863-b1126b4f9aae | -6.76806 | -59.67616 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 5ea67a5b-9eaf-363a-9423-35b0d10459d4 | -6.24314 | -60.01712 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bf93306d-3ea6-36d8-a415-4160c8ea14ba | -6.68841 | -58.54044 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bde0b144-5a70-389d-b21c-f522b37dfdcb | -6.77092 | -59.66194 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 40f0bc52-2bb6-3a1f-a890-c808daace526 | -6.78665 | -59.67006 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 174d085e-5d2f-3d11-96a7-e9d9eb253c2b | -3.39277 | -59.44975 | 2025-08-26 06:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1f02ad6-cbeb-3ae4-a0a1-335a965d8a80 | -6.25443 | -60.01872 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 027b9087-e12b-3c14-89f7-45c72614bdb0 | -6.23801 | -60.01273 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 164caf21-088e-359c-9c6d-a056c850d427 | -6.79191 | -59.67496 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23b692ba-37ce-3f9b-8ed3-12334624fb71 | -5.32064 | -60.20076 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac5ce487-45a8-36b9-890f-bfa93f5c6e99 | -5.29811 | -60.19864 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4773c364-17ee-3b4a-be45-cde3583d7e63 | -5.30914 | -60.20274 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71db388f-163e-3227-bd0d-fbdb6d8b1c7e | -6.70138 | -58.55888 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fd28ecb0-9b2c-38b5-8dfe-c523c238852a | -5.40388 | -60.16898 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5ae7877-615b-347d-96d5-5b1e89815b67 | -6.91803 | -59.36869 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c19d55b4-4b18-3dc2-ab60-cffc726e6088 | -6.68472 | -58.54146 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a93ca50-4ae3-3200-9ace-3bf2a6f1598d | -6.25601 | -60.00748 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89b9e01a-ec13-35fa-82b9-f41301f9b622 | -6.9121 | -59.36781 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1730254-84e7-31f2-a7ed-d6ddd1ebc0ef | -6.69582 | -58.55318 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c8709cb-d78f-395e-a4af-61d2800a49a2 | -6.78029 | -59.67327 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e96b5d45-6adc-3267-b6e7-1612f2ba2cf9 | -3.38988 | -59.45054 | 2025-08-26 06:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c3fcd1e-c62b-3dff-a298-357006e5603d | -6.76335 | -59.67361 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 910f8a93-344d-3134-85a1-91a34ae56a10 | -5.5334 | -60.20218 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07d12af9-c4d0-392f-a488-981f55d2692f | -6.23905 | -60.00522 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b9faa65-089f-362c-ac11-ee8a97fd60d3 | -5.52738 | -60.20499 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8b40590-a0c8-3e89-bfa9-21294ce44b1b | -6.76281 | -59.67112 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31792cf1-3db2-38e1-b75f-181fef4315fb | -6.91586 | -59.36609 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4885d9ae-0f62-32d4-b149-030c9a3d886e | -6.71014 | -58.56837 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0226b3d4-ecd4-394a-b0b7-21e0845862da | -5.40887 | -60.17339 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d8d14ff-8c07-3784-aee2-69cf5582e205 | -6.23289 | -60.00814 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3a4d008-ddfe-3230-b446-2d5908f56cde | -5.52644 | -60.21131 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5241c2cc-81a3-3058-be9b-a2208261fcc1 | -4.9582 | -55.80931 | 2025-08-26 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38f533de-eeb3-35ea-9dbf-01a7b14be2f3 | -5.5329 | -60.20577 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e3c98c3-a1bc-3df8-b262-50040b9ae45e | -4.95849 | -55.82106 | 2025-08-26 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 30f4e3ad-8550-3375-90a6-e9b648fce610 | -6.25496 | -60.01493 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26c8a2df-2957-3719-8fb2-7c0489894fd4 | -5.29759 | -60.20219 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b018f2f-f626-3533-8c1b-36d087c06914 | -6.70628 | -58.56932 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 18d408d5-b5f9-392c-9d08-4d7591100391 | -6.2447 | -60.00602 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README90.md)
