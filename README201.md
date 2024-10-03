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

## Dados Diários - Página 201

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59eea8d5-5b62-3ebd-bc6a-3cc1384f862e | -8.78825 | -68.79861 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 135e53ce-260f-3e3f-9d1a-1c062b9968cb | -8.78874 | -68.79498 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bce47491-3047-38f0-9d91-e1542b9d8b18 | -8.79217 | -68.80156 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 495d24e2-533c-3c06-ba87-7944ec44f944 | -8.85013 | -70.56985 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85c79009-ab2f-31bd-9f76-715cf1cf7045 | -8.87372 | -70.85464 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d648b9e-dc06-3ce8-9559-2c3ed4dd8ecd | -8.87442 | -70.84946 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ae4a806-979e-3285-ac65-69f90441064d | -8.87511 | -70.84431 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5b50ec5-9a04-33a0-8de3-edaa32d068a8 | -8.88618 | -71.37375 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a43f8592-94e5-3226-bfc0-18fde66710c8 | -8.8867 | -71.25232 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9420057e-2eaa-3434-9b4f-75175fb198a1 | -8.8914 | -71.25298 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c68f811-b910-3b10-b338-dad20fb9ad0e | -9.01056 | -67.74213 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a20271a-ff71-3eb1-ba3d-6b79c5c5cbe9 | -9.01595 | -67.74728 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b5d47750-582f-37d4-b3d4-9d5c45015bd1 | -9.01652 | -67.74294 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 76f64d4c-a000-3302-a8cb-9b70be981ac0 | -9.02247 | -67.74376 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 30c80866-0624-3e12-9284-1a049b187b6c | -9.04158 | -67.50299 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e66a971-df14-397b-8887-9735fbbebbe3 | -9.04217 | -67.49848 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5a67026-2ccb-35ee-a361-2e12704dcc4d | -9.04611 | -67.8696 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7ae59a72-b3a2-30bb-8889-ae274e0304e8 | -9.04665 | -67.86535 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b2cf09b0-03a6-3588-a6de-0c42550bfd18 | -9.05202 | -67.87041 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8726fbf2-1c64-3be7-ae32-b22f99963ab4 | -9.05256 | -67.86617 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be9e56e5-80ed-3669-b7d8-31389b7dbed7 | -9.05309 | -67.86192 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5da4a41d-0f7d-3c6f-a8a7-aa6935ac0939 | -9.05901 | -67.86271 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68a5c1c3-5350-3677-a39a-ab9289376622 | -9.07726 | -67.67104 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d35fa678-c111-374b-8c2a-1069cb519eea | -9.07782 | -67.6666 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15d2c855-7326-3654-9537-6cb98c50d456 | -9.09037 | -67.51831 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03bfa6a8-ec4a-3dff-b57a-affdca02667f | -9.09094 | -67.51379 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cedfc6e-dd29-31eb-939c-c3743b6cb7bc | -9.09641 | -67.51916 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 890bb701-9fcc-3409-8fa6-887457a16ade | -9.09698 | -67.51463 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e6b0a7d-c0b0-3371-962f-c7d12e0bdf9e | -9.09756 | -67.51007 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 59a12992-6d66-38fb-990d-d3a6db7617a0 | -9.18933 | -67.85624 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d346a49a-dfdf-3ff4-9933-e8fc8052438b | -9.18988 | -67.85194 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a20a77a5-b749-3e38-b4b1-b28bc7b7f698 | -9.19111 | -71.83734 | 2024-10-03 06:31:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a16c7e4d-254d-3245-8b87-fa79e187b65d | -9.19525 | -67.85706 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbc5d1a3-0697-3feb-8bcb-92b43f67f0db | -9.20075 | -71.80119 | 2024-10-03 06:31:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ca48ded-a7ed-3637-bdf3-e34ed81a254c | -9.20138 | -71.79663 | 2024-10-03 06:31:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd71fcbc-7fb1-384c-a166-03ac2a1d5106 | -9.24027 | -65.60638 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 986b3ea1-ed90-3846-ba6b-f41afa8b59b5 | -9.24103 | -65.60014 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23e75499-3bab-3e71-874c-2ca110d78ea6 | -9.24893 | -67.81592 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1843c09a-c3d7-3d6d-a578-e0ab27d0e14a | -9.25373 | -67.82536 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f328625-c6e2-3c5e-9102-0934aec00dff | -9.2543 | -67.82101 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 826524fc-511a-31df-8dbf-6d8da00e5092 | -9.25737 | -67.82368 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90b42cd3-8d4e-3658-932b-0a5c38ed7cc6 | -9.25791 | -67.81935 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d604f76b-1081-329e-ac5c-a11f41dd6898 | -9.25929 | -67.59721 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e484e6d-09ac-3549-a210-98a8e126a84f | -9.26024 | -67.82182 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac5ea361-f2a5-3b6b-8f9a-08e97dd4518d | -9.26084 | -67.59943 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| feecd261-2463-33dd-896f-b94cd06416c8 | -9.26139 | -67.59492 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12a33f58-ec9a-37eb-9344-0c469fa16f9f | -9.26219 | -67.88136 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e502d30-7468-34f9-9452-0d9e0724774d | -9.26385 | -67.82018 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4993c177-f43d-3253-b0c9-d7beeb9b649f | -9.26472 | -67.60256 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d1920e3-5d22-3d89-84e2-e02855752517 | -9.26531 | -67.59805 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f410f58-8b89-308a-b5b1-bee034b5545d | -9.26686 | -67.6003 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ab860ef-3508-3059-a397-ddfb9754537c | -9.26756 | -67.8865 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2e6f303-47c6-3744-b154-c4b81d98f671 | -9.2681 | -67.88219 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35afe878-5f28-3b77-861f-dbc3606bcd8e | -9.26979 | -67.82103 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc0ef823-fcd2-3a76-b274-5194331d793b | -9.27035 | -67.8166 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 320c6ad6-56e5-396c-b8d5-57aef36e2cca | -9.27349 | -67.88721 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e5c0250-ba52-379a-9b97-a235e07df155 | -9.27952 | -67.83967 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3758a7b9-8e36-3558-a5ca-95e1185cb28d | -9.28008 | -67.83529 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10d693e3-cae1-3b94-8155-411d1957bcbb | -9.28171 | -68.3714 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdf12fde-21b9-36da-bdbe-637566f45267 | -9.28224 | -68.36739 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d99de8-beb5-3647-85d7-fb8dd406d01a | -9.30359 | -65.37328 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dcdc8844-ded9-3df5-a9d2-cbcc90141f22 | -9.30438 | -65.36686 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d886e97-5575-355c-a4f9-92c3aaea5933 | -9.30515 | -65.36051 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b0c0df7-3b25-3a4d-84bd-15d49f13279e | -9.31006 | -65.37727 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 615da637-ada1-3f5e-979e-2784d1c39208 | -9.31045 | -65.37456 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5fbfff67-841a-3ee4-b3d4-93d9c53111c7 | -9.31078 | -65.37111 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7747130-1e71-3000-812a-776b8849878a | -9.31122 | -65.36831 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 573eaed0-01ea-3f18-aba8-4c794516d904 | -9.31153 | -65.36469 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c01bc217-b98b-355d-8dbc-de0e52a4f4e4 | -9.31154 | -66.63371 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2247bd6-d4f4-3d1a-93d7-2a65e9d3e84a | -9.31201 | -65.36192 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f5e6d05-f3d6-3dc4-a5af-ef15d65d3811 | -9.31218 | -66.62853 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61f1867a-9fd1-3475-9d5a-a715d484d00b | -9.32193 | -68.24351 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 413f6af3-b7cf-37fc-957f-8f14138f6a8b | -9.32823 | -68.2403 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9accf8ad-5cf6-3b14-bf8e-823bb9b910d1 | -9.3307 | -68.92021 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ae06a14-d9c6-30e3-9aaa-7d7291aa4d60 | -9.33117 | -68.91649 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8819179d-5d55-35e1-acdb-f1e86f77652c | -9.35663 | -68.20269 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6058030-fa92-33f6-baa6-bedd9383c9d3 | -9.36001 | -67.39879 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2c2a0b1-eaab-3c8e-9e7d-8b030df6bb88 | -9.36058 | -67.39428 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9d3508e-4da2-346f-9a20-bcc2d5794f23 | -9.36191 | -68.20761 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 249aa8a8-da0f-3e97-9d0b-97c2f02e109f | -9.36244 | -68.20348 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 995c097e-26ec-39c0-a293-8b31ce18a6ef | -9.36771 | -68.2084 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee71de15-d986-364a-b1bd-4fd08153339f | -9.36825 | -68.20423 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3bf6fd8-c216-3119-b49a-4b26cd3bd7c3 | -9.3802 | -68.33804 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0e5a7574-f3a1-3316-bc29-7ca7de3d7dd4 | -9.38073 | -68.33398 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b9b7631d-9e8a-306d-91e3-b103d083a0e9 | -9.38089 | -68.34004 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74a22a76-c184-3fd5-8b8c-03855cca0b12 | -9.38127 | -68.32991 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b16762af-457e-32c4-893d-971ab36355ee | -9.3814 | -68.33595 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1823c1c2-1671-365f-b46c-68d97f4a2afe | -9.38191 | -68.33187 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2d52dc15-8862-3045-aeb4-520955483ef7 | -9.38241 | -68.3278 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b7a65558-f70e-3bf7-8485-4a1933f7dbd7 | -9.38597 | -68.33874 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffca3489-7745-3a4a-abe0-e1cfe205f77b | -9.38704 | -68.33061 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bb52258-f7ed-36b3-828b-531500c56fd8 | -9.39085 | -68.25713 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e55b0d8-bc14-3f16-a48f-ef4861473139 | -9.39097 | -68.25899 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc1811a2-ba81-31e7-9ec1-eb005d5c2690 | -9.39174 | -68.33939 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55d09e34-9bf0-3b98-8288-bed650202c60 | -9.39602 | -68.30707 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6938d410-b938-3af4-92c3-a68c32cf355c | -9.3961 | -68.26198 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b48f7ac-4de5-3753-b698-d33cad818542 | -9.39625 | -68.26384 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38a1e513-c4b7-39aa-94f6-4c85ce09941e | -9.39649 | -68.30901 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5cec0f4-2dea-3395-9792-e3db2948fda0 | -9.39663 | -68.25795 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9c238dd-8d85-3f6c-baab-163bdd37c089 | -9.39675 | -68.25982 | 2024-10-03 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README202.md)
