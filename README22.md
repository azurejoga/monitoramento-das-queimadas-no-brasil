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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6aa4526b-7fff-3f22-91a8-1dabae4d7c97 | -9.5063 | -60.54212 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10792a8c-cd0a-318b-b34b-e93d6545b1a7 | -11.6879 | -51.62265 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fae967c-b3f5-3f0e-a050-4dc7b49b38c7 | -12.31221 | -46.05785 | 2025-08-14 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c23bdc77-5a27-3d68-9ce6-f99a0c77ea45 | -9.15399 | -59.64556 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c48f7d7d-6f0c-3d39-955c-0a7c030c93f7 | -7.87648 | -61.81703 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 752c225c-5c48-3999-8ea0-e4eb2463981b | -9.34669 | -60.32782 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3d20523-ae5b-3f8d-b76b-2cc8de8f7185 | -11.31472 | -49.95645 | 2025-08-14 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17e35fe1-c1f4-3310-b170-074894b7287f | -7.60166 | -63.51139 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9a5d21b-d025-374b-bbea-7cd97863ffe7 | -10.3679 | -50.81049 | 2025-08-14 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 871990de-146c-34ba-becd-5ffa8d43aebf | -10.00674 | -59.21769 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d020822-dfec-3cc2-8d90-047a180ba707 | -12.57718 | -46.95568 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b1c56b0-9f6f-3881-a05a-99ce02fcf07b | -9.83178 | -60.76453 | 2025-08-14 04:49:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cbf475a-a0c1-3c7f-a6c0-1866f409ffd3 | -10.34408 | -57.59312 | 2025-08-14 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 50d97a62-a9c2-3c23-a899-1ffec51f1e3c | -8.10223 | -61.20563 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c73b239d-e637-3dd7-a036-9cf6406c79c2 | -12.31656 | -46.05852 | 2025-08-14 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a561c90-223a-384d-b315-ad9286ac46b4 | -9.49935 | -60.52414 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db4636cf-b59a-32f2-a21f-6fbef296c9bc | -8.10362 | -61.19816 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a49393cb-42c1-3aba-b24c-f4388f7045c9 | -11.689 | -51.61557 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50eabb3d-2473-3ac8-9071-2d776ec8e359 | -7.86905 | -61.81836 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 37304989-f108-30fe-9a85-efd5b633923f | -9.50169 | -60.53787 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aeb8c442-6974-30a6-8ba2-325c4b54a537 | -9.1994 | -59.67759 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a734269-6727-3d4f-ae66-0473db89387f | -11.28244 | -52.75101 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eeb2e7ca-3acc-3f61-96f8-7729d6c5fe5b | -7.87574 | -61.82114 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 283c422c-e526-3fa0-8d13-b04547c88228 | -12.02001 | -43.62924 | 2025-08-14 04:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a48490b-bf67-317c-b77b-084842af1c04 | -7.87139 | -61.81179 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ed4447de-4b2d-3f8e-8417-96bd3625c29e | -9.15297 | -59.65117 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6099b1a7-0469-3614-934b-1073bfe7c9fc | -7.88149 | -61.81641 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 842a89db-ac4c-30fc-9586-e585ca405dbe | -9.49829 | -60.52717 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a6a6cafa-4889-3830-88f6-3504fe30d8cf | -9.82651 | -60.76352 | 2025-08-14 04:49:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| deb6027f-2bab-3ced-914f-56e681a20b16 | -7.87917 | -61.8288 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1a08341d-6d01-3dc3-88ab-7a151a71ccb7 | -11.68179 | -51.61803 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8d52630-827f-3120-9e5e-9561a1aa479c | -9.60336 | -55.14526 | 2025-08-14 04:49:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d543939-90db-3dbe-beea-e61dfcff884e | -7.88225 | -61.81232 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae6fac39-b31c-3395-b372-46fba9ae4529 | -12.58226 | -46.94916 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 485f8a30-9d88-3bc3-b8c9-c6c6f38ea381 | -10.36399 | -50.81354 | 2025-08-14 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3da4b12f-8456-343b-bd1e-1869cc863ba2 | -9.15873 | -59.67581 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 165cf75d-6721-32fc-a6a6-c01a7b1cf739 | -7.62637 | -63.51575 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e95ef61f-fadf-3584-b223-eee571e28b9c | -10.12334 | -51.66127 | 2025-08-14 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 859790f3-a7bc-3ad4-ad5d-e8ab42057632 | -11.04177 | -55.37168 | 2025-08-14 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31504eaf-087f-3be7-a83e-54792b8c9d4b | -9.50109 | -60.5445 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1783033c-7431-3dc5-9497-05327fbae51e | -9.05524 | -60.64962 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7869977e-b5c0-3e4c-bb10-68addffaa42b | -7.87721 | -61.81295 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 758f6ca7-d68d-39c0-98af-cf01bb7eebf8 | -7.60712 | -63.51816 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07f0c2ab-32c0-3051-a6e1-ccb4e0fbc2cb | -7.87065 | -61.81592 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6eaddfce-4f79-3eeb-a704-6680be398f4f | -12.32468 | -46.06408 | 2025-08-14 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 677b503a-d2f5-3014-97a5-7c7d9e08ae98 | -7.8772 | -61.80709 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ce44b78b-d248-343c-8815-d15d6300c6f2 | -7.56022 | -63.4848 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36e862fc-b673-3a61-b2c1-3a1c127f8d08 | -11.28187 | -52.75455 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5257d4aa-73f4-31c6-b39c-951dd5a7167d | -12.58177 | -46.95281 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ab9d6f78-3365-3f1a-8067-7457e3589032 | -8.10782 | -61.20668 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a50bc157-a142-3ce4-8cae-e1bd94592cf4 | -9.50109 | -60.54106 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13e44c30-13ca-3b3a-801b-96cab4d7324a | -9.15688 | -59.65782 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c76a4955-779a-373d-89f3-6107da945644 | -7.6253 | -63.52124 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 921760b7-e407-3a96-8e85-d0005c460e96 | -11.69233 | -51.6161 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab5ba076-83f4-321d-8359-9a75ed62b044 | -10.00581 | -59.22282 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| df85fdc8-80a9-3f3e-8a00-f59c6226de4c | -12.30052 | -50.00745 | 2025-08-14 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03ece27b-59f9-3330-b6dd-055626abf256 | -9.4995 | -60.52077 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8353ac32-4832-34f5-8782-3eb8b737b433 | -12.29994 | -50.01133 | 2025-08-14 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b912e2c0-43d0-3a50-8861-de6599ad3cab | -9.49877 | -60.52736 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a867a0e-eaa8-3b86-9d60-7f6c35d1aaec | -7.8699 | -61.82006 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c0f69c8a-9faf-3021-9eae-5cb8bda94d97 | -13.07756 | -49.33104 | 2025-08-14 04:49:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e823101b-5fe1-3631-b699-511406a402c6 | -12.42507 | -48.69951 | 2025-08-14 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1972c3e2-3b40-3d6c-ac40-05463a875bca | -10.1006 | -59.65808 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 804fdd26-bb14-3f96-96b1-ee4c0b65fbc1 | -10.002 | -59.21681 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21f9c361-887c-3597-b754-55fca607f0ec | -8.10292 | -61.2019 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc80edc8-c044-362b-8de0-d95a633a0359 | -11.68567 | -51.61502 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4eac74e3-4130-3857-bb7e-fc69b8810d10 | -9.20843 | -59.65678 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ead5785c-390e-3306-92d8-544321169acc | -9.50068 | -60.51445 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5102bbd8-472b-3979-801f-e7ddae04db59 | -9.19259 | -59.65842 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 236289ae-53ec-30ce-9de3-5af83ba7124d | -12.42705 | -48.69732 | 2025-08-14 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04cc98a6-05c5-34d8-819d-71c60910212b | -12.69117 | -44.9542 | 2025-08-14 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76b38072-9324-313a-9999-b7c8d86705c9 | -8.10644 | -61.21411 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da5029da-cd89-32f2-8da5-dad0e4d035ae | -10.34723 | -57.59687 | 2025-08-14 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31879f58-e8cc-3681-a5db-a4761740a6ee | -8.1057 | -61.1869 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0cc3456-9ece-3a5b-8fc3-1c9b05208e7f | -7.62661 | -63.52198 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db1919c3-0435-3f8f-b40c-4e4e6b099465 | -9.1381 | -59.64849 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27ba2eec-d439-35af-b0cf-8bbf01041f2b | -7.87796 | -61.80879 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b809879-3951-3eb6-98ed-6c11387c152c | -9.15089 | -59.6626 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f306c56a-e98f-3915-9aa8-9273ccd7bd7b | -10.3476 | -57.59797 | 2025-08-14 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d79c86d-ae5b-3522-8b9b-8a9e1423537c | -9.50689 | -60.53893 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6c015e2-7a15-3ee6-bc8e-41d5cba59bf6 | -9.60779 | -55.1415 | 2025-08-14 04:49:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77efcc69-c70f-399b-bff8-b08d39b85428 | -7.87059 | -61.81012 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8888b115-8bee-38eb-b5fe-af117e4c20b3 | -9.05992 | -60.65399 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 954caae1-6dd9-33de-a9ae-d91cf3b9d2de | -9.13002 | -59.66461 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5016e70-2746-3ff9-a95f-e788d55000dd | -12.57619 | -46.96311 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4295bd93-a132-3f1f-8a47-52f4399da954 | -12.58077 | -46.96021 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cac3941-a02f-360f-ae91-b3816f0ed3da | -9.19156 | -59.66415 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 503a9e04-735b-3fd0-a1b6-070007724cc6 | -12.34651 | -49.91484 | 2025-08-14 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d497ef44-ec4a-3967-b1a4-d8920b8bafd6 | -11.68234 | -51.61449 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efe4654d-ee08-3f68-aa04-e67f786bd8b7 | -9.50398 | -60.52842 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a749a74f-e808-3ab4-a2d8-424533394b58 | -9.0593 | -60.65731 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8665822-2189-318b-bc9e-d5a2422c2c93 | -10.34828 | -57.59401 | 2025-08-14 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3718629b-529b-3bde-b977-e2dacf217496 | -10.36119 | -50.80944 | 2025-08-14 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d1e4708-250a-30b5-aa40-7caa68396dea | -9.71898 | -56.18185 | 2025-08-14 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18c0c63a-827a-31f2-84e1-24664856b911 | -11.68289 | -51.61095 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4e7b820-a577-3d5a-af22-b4a51a7ecb4d | -9.18766 | -59.6574 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 267a81b7-9132-34ce-85cf-f41a56d8c1b5 | -9.64396 | -63.1539 | 2025-08-14 04:49:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97eec6b3-c053-3c7f-b445-a4551ced4444 | -7.87871 | -61.80459 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8e5c1ee-c699-33d2-b792-d17e8b082c46 | -9.21434 | -59.65117 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8694b51-c931-369f-a6da-9bb98b998872 | -12.31598 | -46.06278 | 2025-08-14 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README23.md)
