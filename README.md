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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b6c155e-8cd1-3869-a79f-f321e5ad7bd7 | 0.0456 | -60.6584 | 2025-01-18 00:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 28654be9-1299-3d82-8040-26562c4769e1 | 0.082 | -60.6584 | 2025-01-18 00:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 116.2 |
| da4ba8c2-8e48-3c29-9e19-d8ca29c6c233 | -22.8382 | -53.4765 | 2025-01-18 00:00:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 9f15016a-d3fb-34df-8054-968b257358de | 0.0638 | -60.6584 | 2025-01-18 00:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 313.1 |
| 97b0a912-be38-3dd4-9e03-a18fe0867550 | 0.0638 | -60.6773 | 2025-01-18 00:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 106.9 |
| d3248b21-ec2f-34b8-b91c-f30e020f2403 | 0.082 | -60.6773 | 2025-01-18 00:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 249d9565-8afb-3aa9-a2df-8741cc287ca8 | 0.0638 | -60.6394 | 2025-01-18 00:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 22d541b6-e91c-3b97-9e1e-b4b78cf4c2f7 | 0.082 | -60.6773 | 2025-01-18 00:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 700837ba-fd92-3d41-b39f-227e6a678f4e | 0.0638 | -60.6584 | 2025-01-18 00:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 250.5 |
| b70b0e6b-7141-3199-841e-4e6abc4ccf80 | 0.0638 | -60.6394 | 2025-01-18 00:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 3187ba7c-25c5-3dff-a767-6db69ae0147e | 0.0456 | -60.6584 | 2025-01-18 00:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 9e35c15d-0961-3fb6-a0fb-6ea52f52c3b7 | 0.0638 | -60.6773 | 2025-01-18 00:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 78.5 |
| cee7ca7b-c189-3b36-88d3-223bac09a085 | 0.082 | -60.6584 | 2025-01-18 00:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 144.6 |
| bd0a83d5-db78-3492-8a75-0a68b7113027 | 0.0638 | -60.6773 | 2025-01-18 00:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 0b85610d-6ed9-368a-a3df-d71ffdec05d3 | 0.0638 | -60.6394 | 2025-01-18 00:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 91.3 |
| c2756b48-f220-39d9-84bc-ea1e78a3cd34 | 0.082 | -60.6584 | 2025-01-18 00:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 84b06ed5-3a34-3faf-9baf-96c6950f6259 | 0.0638 | -60.6584 | 2025-01-18 00:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 234.4 |
| d3e68f96-c0a7-36ce-8acb-f2d3a5ad956b | -22.8585 | -53.4947 | 2025-01-18 00:20:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| 50bd57b2-600e-37c2-aada-98d11a7a1f66 | 0.0456 | -60.6584 | 2025-01-18 00:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e3e99a72-aa50-3f8b-a01f-05935bf2e9b6 | 0.0456 | -60.6584 | 2025-01-18 00:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| b0c00d71-7700-3e17-a060-191cc2e712ba | 0.0638 | -60.6773 | 2025-01-18 00:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 8b6ee1f4-d997-39de-9687-5fdcad8a2b99 | 0.0638 | -60.6394 | 2025-01-18 00:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a258b98f-7257-3ac5-8d4e-e05c1693ec1f | -10.7245 | -37.0797 | 2025-01-18 00:30:00 | GOES-16 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 99.8 |
| 2e82011c-c41c-3df9-91ec-bf5d47388f61 | -22.8585 | -53.4947 | 2025-01-18 00:30:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 93.9 |
| 5ad165a8-f0ba-38e9-b021-ba08bb9f90b6 | 0.082 | -60.6584 | 2025-01-18 00:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 101.8 |
| aabcde1f-22ae-3004-a2ec-c16aabf586c0 | 0.0638 | -60.6584 | 2025-01-18 00:30:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 174.4 |
| 846fdca5-3319-34b2-9a29-c6d69b2bfe2a | -21.8888 | -56.1091 | 2025-01-18 00:40:00 | GOES-16 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 4d78f0e3-0c69-37c9-bd60-1bfc999fad8c | 0.0638 | -60.6394 | 2025-01-18 00:40:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 847a9303-303a-3f2b-8e72-50e636d02183 | 0.082 | -60.6584 | 2025-01-18 00:40:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 98.3 |
| cc69a655-c90c-3f6c-abd8-ff894de307a3 | 0.0638 | -60.6584 | 2025-01-18 00:40:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 165.3 |
| b02cfb04-4599-3e44-98cb-78f9893f162a | 0.0638 | -60.6773 | 2025-01-18 00:40:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| df34af83-2d41-3501-9a5f-59b057aa2723 | 0.0456 | -60.6584 | 2025-01-18 00:40:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 303b5a1a-c661-350b-aa03-3512c6f7538a | -10.6806 | -37.0494 | 2025-01-18 00:41:00 | METOP-C | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2950fafa-f845-3439-90a1-0b2593d41292 | -9.9233 | -36.337502 | 2025-01-18 00:41:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 471d6501-080c-38a8-a9d5-671a28774d36 | -10.6901 | -37.046799 | 2025-01-18 00:41:00 | METOP-C | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6166291f-2d6d-3b36-8b74-3bd4ea7c8656 | -9.9319 | -36.369202 | 2025-01-18 00:41:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd4787f4-2821-38e1-a5be-719c25624544 | -22.8552 | -53.497101 | 2025-01-18 00:44:00 | METOP-C | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e96d2d04-5a60-3afb-b3c7-f14d2e9cc9d5 | -22.8524 | -53.480499 | 2025-01-18 00:44:00 | METOP-C | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dfd0e1ec-e791-35a3-9d82-3fd2424221ff | -21.8853 | -56.136501 | 2025-01-18 00:44:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 67a1afd6-5216-3541-ba11-c599d642407a | -22.845501 | -53.498901 | 2025-01-18 00:44:00 | METOP-C | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| be1faab4-c75d-3b5c-a073-853251329bc8 | 3.273 | -59.9813 | 2025-01-18 00:44:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9f3e71fc-cea2-398c-baa4-15f5d6a27268 | 3.2772 | -59.963501 | 2025-01-18 00:44:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e49e7b4a-7f23-3a86-8ab1-aba8ef5b5489 | -22.8608 | -53.5303 | 2025-01-18 00:44:00 | METOP-C | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4584807d-8add-3ff6-8b97-4f3096bff7e0 | -21.894899 | -56.1348 | 2025-01-18 00:44:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 487874c3-7a44-31cb-8b19-99b510d45b6f | 0.0683 | -60.657902 | 2025-01-18 00:44:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 55f3d59c-ab5c-30ff-91a6-c5d33d1d9608 | -22.858 | -53.513699 | 2025-01-18 00:44:00 | METOP-C | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 412565c5-41c7-3448-a27f-41ed63bcfe5f | -20.2472 | -40.266701 | 2025-01-18 00:44:00 | METOP-C | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fbaa8f21-ece5-3550-b582-cdd439269dfa | 0.0456 | -60.6584 | 2025-01-18 00:50:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 41a8330e-1732-3646-92a8-b5e54a33e9d8 | 0.082 | -60.6584 | 2025-01-18 00:50:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 88.1 |
| d1578242-0e68-3133-a89f-ef7d0d921330 | 0.0638 | -60.6394 | 2025-01-18 00:50:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ab645e69-aae2-3023-9c3d-d725c049e545 | 0.0638 | -60.6584 | 2025-01-18 00:50:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 7c16d002-7e6d-3b41-8b15-88a4e5a03348 | 0.0638 | -60.6584 | 2025-01-18 01:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 143.9 |
| e744d3d6-054e-3b11-8833-7cb445c8d939 | 0.0638 | -60.6773 | 2025-01-18 01:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e921cb4e-c3fe-39b7-9193-0777480b5669 | 0.082 | -60.6584 | 2025-01-18 01:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c506071e-c658-3a0f-92a6-b74cfbff5480 | 0.0638 | -60.6394 | 2025-01-18 01:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 464be053-c1e4-3a13-abe5-c402387d31db | 0.082 | -60.6584 | 2025-01-18 01:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| c8cb3483-970f-3af3-a01c-cc3567fdc036 | 0.0638 | -60.6394 | 2025-01-18 01:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e99539d8-567d-3363-bb9b-b6826ff4a2a8 | 4.9039 | -60.2886 | 2025-01-18 01:10:00 | GOES-16 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 5dc48ec6-8290-3ad1-a143-df56b2a513d8 | 0.0638 | -60.6773 | 2025-01-18 01:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c060e060-dd2a-3be3-af4a-4d3045ec3d76 | 0.0638 | -60.6584 | 2025-01-18 01:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 172.5 |
| e4a1c497-7ffd-339c-97cf-13395393f1d7 | -22.84083 | -53.48148 | 2025-01-18 01:11:00 | TERRA_M-M | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 4a677754-c71b-332f-9e2c-06988244230a | -21.88777 | -56.11575 | 2025-01-18 01:13:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 3d3fcfc8-90f0-3397-866c-0d14412e787d | -21.88613 | -56.10149 | 2025-01-18 01:13:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4b6eb3bd-2335-3091-8380-5620de763ef1 | -21.87706 | -56.11685 | 2025-01-18 01:13:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c6b6f3cb-5b08-368e-b247-d46a364fe8d4 | -9.25451 | -60.31207 | 2025-01-18 01:17:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ec7812ee-0ddc-304c-87a8-c5725624f7c0 | -9.25664 | -60.32968 | 2025-01-18 01:17:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 36980556-b178-3bc7-b7c9-288734a1b508 | -9.26248 | -60.31654 | 2025-01-18 01:17:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 55258992-0fc4-397b-868a-009ee5707251 | 3.79203 | -60.09292 | 2025-01-18 01:19:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f5b36ab5-d948-3e0b-8bf9-260d2d56caea | 3.27612 | -59.9713 | 2025-01-18 01:19:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 154d0b5d-bcfc-370e-8947-2beff2e01cc0 | 0.06164 | -60.6634 | 2025-01-18 01:19:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 32f9c64f-22b5-3f03-8b01-2fe1c9af73d5 | 4.82662 | -60.59254 | 2025-01-18 01:19:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 637a6d11-f6c0-3036-971f-b47f050d7fed | 0.06345 | -60.65015 | 2025-01-18 01:19:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 545d3109-7b67-3715-8f4b-8e1a47fdc36d | 3.27461 | -59.98205 | 2025-01-18 01:19:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1499ca04-600b-3c83-a8fe-497828fd6efc | 2.55264 | -60.5953 | 2025-01-18 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0eb62737-e91b-3f33-b942-0ee79553653e | 4.10903 | -60.01441 | 2025-01-18 01:19:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7facfe6e-9460-361d-8c37-0af1ca70ef21 | 4.12165 | -60.02242 | 2025-01-18 01:19:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 07a2e0e1-04fd-326a-8103-dae5ee871b27 | 3.5774 | -60.59235 | 2025-01-18 01:19:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 662bbd3f-9cda-3f7b-a4ff-08e8a288d4ec | 3.11266 | -60.76186 | 2025-01-18 01:19:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 33225751-8573-3661-adbd-e704710e778a | 0.06916 | -60.64321 | 2025-01-18 01:19:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0450893c-0c6a-3c2f-ad0f-04af32fc9d95 | 0.06726 | -60.65642 | 2025-01-18 01:19:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 164.3 |
| 7e5e2abe-a990-30b5-8610-3ae1fe851abe | 4.91333 | -60.28587 | 2025-01-18 01:19:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 061ccc1f-78e9-3f82-a6c7-5e1c72e8d7f1 | 2.61643 | -61.31151 | 2025-01-18 01:19:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 58a74198-d529-3c68-92d3-0e8c59ff4706 | 4.91166 | -60.29728 | 2025-01-18 01:19:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 18.4 |
| bd5c69a4-b5f3-3f18-8603-6f38c8edef65 | 2.36997 | -61.2581 | 2025-01-18 01:19:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0c91b27a-a4e4-3c19-910f-426cc8073f03 | 2.19941 | -61.82113 | 2025-01-18 01:19:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a444d621-7c45-3e86-b5be-63c5010052d3 | 1.88332 | -60.48773 | 2025-01-18 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e76f9970-7c9a-3ad8-9a5c-fbdb7dcd0a88 | 0.06536 | -60.66967 | 2025-01-18 01:19:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| db5c72fe-6cd9-317e-b313-e26f7429bf53 | 2.37313 | -61.26417 | 2025-01-18 01:19:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1152c312-871b-3428-9b32-508a886e3873 | 3.10064 | -60.77254 | 2025-01-18 01:19:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d36a08b9-8aac-3b40-87b6-333ea44767a5 | 3.1024 | -60.7604 | 2025-01-18 01:19:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a4fb7821-13b5-347e-b364-ac6cfef2be95 | 4.12319 | -60.01179 | 2025-01-18 01:19:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 433e9ee2-60a8-38bf-9fe1-dfffe644b339 | 3.67521 | -60.62477 | 2025-01-18 01:19:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7c0554ac-8117-32dd-90a1-89d10f56b468 | 3.29115 | -59.95723 | 2025-01-18 01:19:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 769bc893-13d9-3702-b106-61d6839aa64e | 2.55521 | -60.58942 | 2025-01-18 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eaf88ac8-d1e2-3ea6-9dcd-84595ab82e9a | 3.28731 | -59.96196 | 2025-01-18 01:19:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 13dc32a7-8aab-3058-b49f-6183d783b7c2 | 0.0638 | -60.6584 | 2025-01-18 01:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 109.9 |
| c9558b90-9a54-3bac-80cf-6b82744d5874 | 0.0638 | -60.6394 | 2025-01-18 01:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 1412a375-8db7-3c5a-a4ac-e68e58260fb2 | 0.0638 | -60.6773 | 2025-01-18 01:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 686afd25-8dad-389d-8909-77ad60614f5c | 0.082 | -60.6584 | 2025-01-18 01:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b9162410-acde-3986-b283-f7c249157101 | -22.8585 | -53.4947 | 2025-01-18 01:20:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |


[Clique aqui para ver as próximas entradas](README2.md)
