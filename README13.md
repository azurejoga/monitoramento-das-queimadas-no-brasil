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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efea3b0e-b25a-3df6-894e-44f70cd6792a | -11.41597 | -54.32572 | 2025-05-16 06:08:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a6a7d820-43f0-3951-9471-eb57de409527 | -15.25989 | -51.46244 | 2025-05-16 06:08:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 35ed8e20-76ef-3391-a5fa-507083acbb3a | -19.06025 | -53.44818 | 2025-05-16 06:10:00 | AQUA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 12d6c5b0-4dbe-3ce0-bb1e-50ee193f99d9 | -19.05886 | -53.45809 | 2025-05-16 06:10:00 | AQUA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0ee3d964-2564-3d23-aef0-54a2533d0b47 | -11.9648 | -63.51751 | 2025-05-16 06:16:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 442a571e-b5a8-397c-a90f-dcd6452363cb | -11.96564 | -63.51909 | 2025-05-16 06:16:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62ae33ab-3dc6-371b-b0f2-b5605a9bcffe | -11.96512 | -63.52361 | 2025-05-16 06:16:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1218cdc-b665-3a77-91bb-823c30bd242e | -11.96425 | -63.52201 | 2025-05-16 06:16:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c28c8cfc-63ee-382c-9ec0-6484b66d15de | -11.96369 | -63.52652 | 2025-05-16 06:16:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d63b5fd4-e514-30f9-8f54-03f8c8185c0d | -11.96459 | -63.52812 | 2025-05-16 06:16:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0dccbe89-c47e-335f-ac77-5dcc752500ed | -12.3519 | -49.9617 | 2025-05-16 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 7f1c823c-084b-3239-b61d-06f9aed1ed81 | -12.3519 | -49.9617 | 2025-05-16 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a3346c45-eccb-32aa-8dab-e7fdb9670f63 | -12.3519 | -49.9617 | 2025-05-16 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 93d2726b-67ed-3de2-bf7e-7db1d4c0a436 | -12.3515 | -49.9833 | 2025-05-16 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 425b0cf1-808d-38e6-83ba-5008952cab59 | -12.3519 | -49.9617 | 2025-05-16 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| c1e76521-859f-31ac-9697-7eee2c1710db | -12.3519 | -49.9617 | 2025-05-16 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 1a2c70fc-d779-3e40-a3cf-0a85b1a3404a | -12.4608 | -57.2079 | 2025-05-16 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 273a9397-b251-3735-b95f-af8e780961ed | -12.3515 | -49.9833 | 2025-05-16 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| d18ca908-1adc-377c-8dcb-f20e93e0a5e6 | -12.3519 | -49.9617 | 2025-05-16 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 4109aef9-9cdc-3bc2-bedb-0d3477ffcc91 | -12.3515 | -49.9833 | 2025-05-16 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| bc1eb9a5-be8b-3a27-8b98-6c289fd86904 | -12.4608 | -57.2079 | 2025-05-16 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 0d3589c3-5658-3813-86a4-9f738b8bcd7e | -12.3519 | -49.9617 | 2025-05-16 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 197.8 |
| e59bbc9d-9572-37ac-abc8-1863dd5e38e4 | -12.4608 | -57.2079 | 2025-05-16 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| f2fbae63-ae4c-32c0-bd68-4e890b40075c | -12.3515 | -49.9833 | 2025-05-16 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 791d61f0-0db0-32f0-b28b-4f7690c87b94 | -12.3515 | -49.9833 | 2025-05-16 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| b66b6f49-cc7a-330d-b156-dc9947e5d228 | -12.4418 | -57.2096 | 2025-05-16 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 8116546a-fbc6-338c-89cb-2a33c484d2d3 | -12.4608 | -57.2079 | 2025-05-16 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 51732aa7-f943-3caf-9041-6f5bde4afa25 | -12.3519 | -49.9617 | 2025-05-16 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 249.5 |
| 8456ac56-2b2b-3c14-9114-23f6126c9b14 | -12.3515 | -49.9833 | 2025-05-16 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| b8d424cc-87ff-3c44-bb77-722dac71bee8 | -12.4608 | -57.2079 | 2025-05-16 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 170.4 |
| e124b49c-85ae-3754-9901-2c348addfc64 | -12.4418 | -57.2096 | 2025-05-16 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 058a3446-f925-3e16-8ecf-b981dc07afd5 | -12.3519 | -49.9617 | 2025-05-16 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 246.4 |
| 1d34ef3e-fe36-3fb2-9a53-70e6a34fad04 | -12.4418 | -57.2096 | 2025-05-16 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 5e868964-c44a-3066-9f53-268202f56024 | -12.4608 | -57.2079 | 2025-05-16 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 210.2 |
| 65e48d62-3a1c-3f08-af2f-3e48ab44d7d6 | -12.3515 | -49.9833 | 2025-05-16 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| e0469be5-7950-3652-b255-1f309ba1e215 | -12.3519 | -49.9617 | 2025-05-16 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 250.1 |
| cb3ded37-180d-30c0-9238-841e3a3ff04a | -12.7706 | -48.9279 | 2025-05-16 13:20:00 | GOES-19 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 16809fc1-d856-3a25-9f25-e0f8efedfda1 | -12.3515 | -49.9833 | 2025-05-16 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 38bb0e94-5a6e-3785-b9d3-d2927978d2ad | -12.4418 | -57.2096 | 2025-05-16 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 14413b99-a382-3d44-912e-f0c1e62402bf | -12.7706 | -48.9279 | 2025-05-16 13:30:00 | GOES-19 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 18d21086-028f-3a3f-a65c-7e9c587c1899 | -12.4608 | -57.2079 | 2025-05-16 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 234.9 |
| f3ad287a-2bc9-38cb-bbad-55370914a7da | -12.3519 | -49.9617 | 2025-05-16 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 9bd6e430-46a2-39c6-9d6e-eb656e2173f5 | -12.4608 | -57.2079 | 2025-05-16 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 196.5 |
| b82ee8bf-0cc1-35d4-9b70-55308c8b703d | -17.4953 | -53.8329 | 2025-05-16 13:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8022bb7f-ac0d-3acc-9933-910964603967 | -12.3706 | -49.981 | 2025-05-16 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 2170d005-37e1-3724-94fc-8b79babc0a64 | -11.6203 | -48.0005 | 2025-05-16 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| da89b7e2-7260-31db-895b-71ae54dad754 | -12.4418 | -57.2096 | 2025-05-16 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| ce535989-0aaa-3a31-b578-8e9283acb520 | -12.3515 | -49.9833 | 2025-05-16 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 410f9049-2fcc-3444-b568-332c81c66cb3 | -12.3519 | -49.9617 | 2025-05-16 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 167.9 |
| afa978ff-1ecb-3b49-abc1-589c6ceb310b | -12.3515 | -49.9833 | 2025-05-16 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| fd00136e-4a3b-3139-aac5-e0c8d2d86d31 | -12.7706 | -48.9279 | 2025-05-16 13:50:00 | GOES-19 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ae77e23f-57c7-3c1f-ab84-2a93afa7f65a | -12.4608 | -57.2079 | 2025-05-16 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 242.5 |
| 895b62e7-4d24-3a0b-b26b-1148f9f47a2e | -12.3519 | -49.9617 | 2025-05-16 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 156.9 |
| b19d6c94-21c4-34f5-ae7f-009d650e149a | -13.5683 | -52.8783 | 2025-05-16 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 1e61054f-450f-363e-a246-8aed04d1056c | -17.4953 | -53.8329 | 2025-05-16 13:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a8328da5-018d-3449-ac83-d7302112a2c6 | -12.4418 | -57.2096 | 2025-05-16 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 71146a80-b999-339c-81a8-80749c92de23 | -11.6203 | -48.0005 | 2025-05-16 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 4b98cca5-bdfd-3a0b-8f37-e2d1f342f0da | -10.4154 | -49.9254 | 2025-05-16 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1fc2ec55-db7e-3233-a372-07b835dd5c8b | -13.5683 | -52.8783 | 2025-05-16 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 62d62829-3f16-34ac-b1b1-858845615372 | -13.549 | -52.8806 | 2025-05-16 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e34cff70-543c-314e-b26b-491e20c993ea | -12.4608 | -57.2079 | 2025-05-16 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 250.9 |
| 69fd0b15-b042-3486-b6ef-108f120e0139 | -11.6203 | -48.0005 | 2025-05-16 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 1126ec77-78f8-399d-aae9-d81218da0bb1 | -17.4953 | -53.8329 | 2025-05-16 14:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b1cdd49b-cf3e-38a5-8da7-99022abff432 | -10.4156 | -49.9039 | 2025-05-16 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| de0bafe9-67aa-3051-ace3-6eeba2fe35e2 | -12.3515 | -49.9833 | 2025-05-16 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 93bbe094-9382-3a04-95bf-f0e77a7e7799 | -12.3519 | -49.9617 | 2025-05-16 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 62cb0de2-b550-3465-85ed-13dda01ab995 | -12.4418 | -57.2096 | 2025-05-16 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| e093179b-052b-30f8-8398-823fec085d78 | -11.6203 | -48.0005 | 2025-05-16 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 25def158-6c05-3d7a-93bc-fa2e15724101 | -12.4608 | -57.2079 | 2025-05-16 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 249.7 |
| 8a3771dd-bc1f-37cb-98da-bc56df5a3761 | -10.4154 | -49.9254 | 2025-05-16 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 3b4fc291-1645-33d6-82d6-42a180b5e044 | -10.4156 | -49.9039 | 2025-05-16 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 4a945e5b-0d03-309f-bf66-a0471a56303f | -17.4953 | -53.8329 | 2025-05-16 14:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e44896f6-67c3-3e0c-a5a5-cc1dc140d544 | -12.4418 | -57.2096 | 2025-05-16 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| ca377317-f4a8-3239-9035-a3dcb2d9236d | -10.6802 | -49.9187 | 2025-05-16 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 655865e2-d725-3eb4-885a-b741018fb3aa | -12.3519 | -49.9617 | 2025-05-16 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 35af04bd-1011-3220-8c4e-e23dd2f41666 | -12.3515 | -49.9833 | 2025-05-16 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5fa26138-fa2e-3976-ae98-f596325e8d23 | -13.5683 | -52.8783 | 2025-05-16 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e9f89dd6-40bc-3835-9515-8d54fee20163 | -13.549 | -52.8806 | 2025-05-16 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4bda4bc0-6eb1-3258-9cc5-e6d8199d7428 | -12.4608 | -57.2079 | 2025-05-16 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 202.2 |
| 1af859b6-0f0a-3866-8c1b-47911a706f44 | -13.549 | -52.8806 | 2025-05-16 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 69cd94ec-a4cd-30c3-9e49-fd16945d760f | -10.8379 | -49.4706 | 2025-05-16 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 44891c3f-ce3e-3a33-a852-ca54e430c388 | -11.6203 | -48.0005 | 2025-05-16 14:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 44e86764-c622-34e3-a9cf-26e9d81f2bd2 | -13.5683 | -52.8783 | 2025-05-16 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 666854c7-3cf8-384b-921a-91068173d581 | -12.3519 | -49.9617 | 2025-05-16 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| d60f8a97-6a13-395a-9073-4bfb9f0e3bc5 | -10.4156 | -49.9039 | 2025-05-16 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| ab3d126a-03e9-3535-9294-7ba2cba1b549 | -12.4418 | -57.2096 | 2025-05-16 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 3ff8aee5-8625-3f5f-b3cc-9ac1bf10efda | -12.3515 | -49.9833 | 2025-05-16 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 073877fe-9811-36ff-a2b2-8db27d372d3e | -17.4953 | -53.8329 | 2025-05-16 14:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 84f9ca48-2f89-3dbd-b4cd-ee73a75c8a13 | -12.4418 | -57.2096 | 2025-05-16 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| c1289810-0e83-3056-9ac1-9c6aecff21d9 | -10.4156 | -49.9039 | 2025-05-16 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8d8c6130-13f8-3083-a2dd-48d0da330a97 | -13.549 | -52.8806 | 2025-05-16 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4955eeff-92b6-3049-b4aa-43a234c60c99 | -13.5683 | -52.8783 | 2025-05-16 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| d8c7c01b-b295-3ded-ac9f-da1517a9b97a | -10.4154 | -49.9254 | 2025-05-16 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 2d7ff458-98b9-3dc6-b3b0-ed49e385e372 | -12.3519 | -49.9617 | 2025-05-16 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| bb797295-8cfe-34e2-834e-f1593e51f4b3 | -12.4608 | -57.2079 | 2025-05-16 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 217.1 |
| f7e75839-61e9-3faf-8324-1c4a1c6717e2 | -10.815 | -49.7536 | 2025-05-16 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c5a98028-48cc-35ca-b00f-e02c8e3b5f50 | -17.4953 | -53.8329 | 2025-05-16 14:30:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 69d0255e-171a-35e1-b66f-f09db747576e | -12.3515 | -49.9833 | 2025-05-16 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9b38c8ff-844a-3b67-b234-304d38ca8013 | -12.3515 | -49.9833 | 2025-05-16 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 7846b86c-63ca-3641-9210-c6f76a6e8af9 | -12.3519 | -49.9617 | 2025-05-16 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |


[Clique aqui para ver as próximas entradas](README14.md)
