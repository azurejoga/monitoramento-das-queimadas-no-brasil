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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0a81dab-3a0f-31c3-863c-4d1c55793905 | -7.73304 | -43.0409 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| dbc17ed3-6906-3352-bd64-39faaca277f2 | -7.72793 | -43.04467 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 53fb0745-cf74-3792-9dcd-6b8f261aaf3b | -7.72732 | -43.04911 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9f9e37be-e778-3705-8220-7461a396b9ca | -7.7267 | -43.05353 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d1d81358-121c-397c-91bc-a6a827e071f6 | -7.72345 | -43.04399 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a7511fc1-7615-3f9a-8dd4-c68aac297ae4 | -7.72284 | -43.04842 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c77214f4-19dc-348c-8727-42e7466ff134 | -7.72223 | -43.05285 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 82829af0-3223-3d99-8124-fb58965b83be | -7.72081 | -43.04598 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 03c64acf-2814-3151-8fcb-bd2654c872a3 | -7.72017 | -43.05037 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 460f3938-f2f2-38dd-9724-442206993eeb | -7.69265 | -42.98722 | 2024-10-09 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2b39f909-f7c6-38ec-81ba-9f1dd28f98ba | -7.68879 | -42.98209 | 2024-10-09 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 30c8f982-eb70-3eb7-b4eb-b16b8e30a364 | -7.68815 | -42.98658 | 2024-10-09 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 963da0ed-7ff8-35f0-834d-9938d5ef60c6 | -7.68752 | -42.99098 | 2024-10-09 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ed1e3930-3b46-3c71-bc30-25a6b4736dfd | -7.68429 | -42.98143 | 2024-10-09 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3d45d3fa-1204-33f0-9a92-793aa15209c4 | -7.68366 | -42.9859 | 2024-10-09 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ae7935f3-99ae-3734-802d-79cf629ebddb | -7.68303 | -42.99029 | 2024-10-09 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| fec0ff91-48c8-37b9-a00b-c70c2c4df760 | -7.66988 | -42.49926 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13a8b8a5-231e-3ff3-8592-92ba93d553c7 | -7.6678 | -42.51373 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e042f6e9-3447-30e5-a991-7d6a8e74954a | -7.6659 | -42.49385 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ecb541fb-3ecf-3a03-b410-3d54d9bda2f6 | -7.66522 | -42.49867 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e040a092-48b9-3dc7-9fea-3f40d8800e8a | -7.66313 | -42.51318 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b8d071e-aa82-3288-9c60-9aeb75a38eac | -7.66244 | -42.51799 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9fc6997a-0292-3cb4-8bcc-ca19f3e54afe | -7.66193 | -42.4884 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 69239425-e897-37da-8e9d-b3f4305947a0 | -7.66176 | -42.52275 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 61cb3e3c-1b2e-3e10-9454-1cda1dd2f0e5 | -7.65848 | -42.51252 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f558581d-2f95-35e8-940b-099a5b463987 | -7.65841 | -42.41279 | 2024-10-09 04:38:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9b4543a3-008b-3a20-b96b-8709b9d5d91e | -7.6578 | -42.51733 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dfbfb3d9-0c2c-3fe1-96df-ff8378ab2a8b | -7.65711 | -42.52211 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0b16b11b-90d5-35cf-bd8f-d8fb2dca76af | -7.65576 | -42.53156 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 97ccd104-fc26-3510-9680-90ce4bd493ab | -7.65442 | -42.40723 | 2024-10-09 04:38:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0b1ca536-1c85-3af0-acd8-ad091dfc8e70 | -7.64975 | -42.4065 | 2024-10-09 04:38:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a8f35a39-82ae-33c8-a3a9-d328696a0312 | -7.6273 | -43.7015 | 2024-10-09 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1c92661e-1d71-376b-a714-3a6459e74697 | -7.6243 | -43.70256 | 2024-10-09 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 70735d29-d68f-3427-bd58-1609b42f75de | -7.62033 | -42.41205 | 2024-10-09 04:38:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7f218bc7-66d8-3c25-aef4-321d18e8e38a | -7.61894 | -42.42202 | 2024-10-09 04:38:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 20f5136b-9de4-3a8d-b8e0-1c12f98db863 | -7.61428 | -42.42123 | 2024-10-09 04:38:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 007dbd7c-9462-333c-b66d-af6cb056c05d | -7.61358 | -42.42628 | 2024-10-09 04:38:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5cdbfe2d-fa69-3296-9e7e-54d90c501be2 | -7.61289 | -42.43126 | 2024-10-09 04:38:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4f0e6589-0499-31dd-9dcf-1657b63f5d49 | -7.61221 | -42.43613 | 2024-10-09 04:38:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d2b857f2-4688-36d6-bc64-e1f9b00c28f2 | -7.35848 | -42.19328 | 2024-10-09 04:38:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a4128f68-96ec-35bf-bedd-18712e4bf085 | -7.30433 | -42.23601 | 2024-10-09 04:38:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 00bf72bf-8331-3f26-ae8a-3ee6bdc3ad64 | -7.30307 | -42.2382 | 2024-10-09 04:38:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f205ec03-4cf3-37e5-9877-23e2e3ecb2f6 | -7.23737 | -42.29464 | 2024-10-09 04:38:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 26796092-0389-3864-9423-0bcc8a6f929e | -7.23669 | -42.29948 | 2024-10-09 04:38:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 990caa42-0a64-3988-a774-81f380a900c5 | -7.23269 | -42.29392 | 2024-10-09 04:38:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7c754fc3-0d6d-364c-8891-60aedb2440b7 | -7.232 | -42.29882 | 2024-10-09 04:38:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ecfb275e-2216-3bdf-83e4-a539ccbdcd16 | -7.22801 | -42.2932 | 2024-10-09 04:38:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 068ffad8-d02a-30cc-b0ab-79caa4d4af8e | -7.22731 | -42.29815 | 2024-10-09 04:38:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d5bc7def-e389-3dcc-959a-3b82b9c98bb6 | -7.225 | -40.16742 | 2024-10-09 04:38:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5e4ea04c-f44e-3856-b793-9f05fad94d66 | -7.1504 | -42.60991 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa9dcb05-67a0-3a23-86fd-35a3beaa19bf | -7.14975 | -42.61462 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 154c2ce6-9b39-389f-b228-6130c28d154f | -7.13606 | -42.64582 | 2024-10-09 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 35d442b7-00da-333d-b09b-ef48160914ce | -7.13542 | -42.65043 | 2024-10-09 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64f70b00-a21c-3ceb-ad27-43c79d9558cb | -7.13539 | -42.64833 | 2024-10-09 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a9736cc1-9fe0-352b-a150-c10407c91109 | -7.1315 | -42.6451 | 2024-10-09 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4216e11a-cfb1-397b-ab39-920feb66dc70 | -7.13086 | -42.6497 | 2024-10-09 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| be94f6e4-77a5-3538-85b7-99811d6a1206 | -7.13084 | -42.64761 | 2024-10-09 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 74544d92-7081-3c87-959d-9449d56a3e03 | -7.12693 | -42.64439 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 18adc0ea-0e9e-3c69-84b2-d1e2f8d3f56d | -7.12629 | -42.64901 | 2024-10-09 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2632d6ff-a4d9-34e6-8086-15d64e53d807 | -7.12627 | -42.64692 | 2024-10-09 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9213fcfb-da6c-3084-9ef1-67f386761cb5 | -7.12172 | -42.64833 | 2024-10-09 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f0a9b10d-aed1-377d-a6f3-68c780fbfbef | -7.12171 | -42.64626 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 204fe14c-2f19-3d60-a9c4-3314a34bf506 | -7.10746 | -42.61578 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1b0b2b30-3aa0-3cd8-88dc-6aed1c431018 | -7.10474 | -42.63457 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f56146ea-5eba-378e-9e29-b68fa534cb37 | -7.1022 | -42.6199 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 46948f0f-0f59-3108-9aa5-482d005816da | -7.10018 | -42.63389 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e649a66f-0d5b-3c1a-8677-2975145edc10 | -7.09763 | -42.61917 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 52485101-a0d1-3f1c-b045-795ae6ac5ed1 | -7.09695 | -42.62388 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 368f4dbe-713d-376a-8bb5-37731e86c178 | -7.09628 | -42.62857 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd7474bd-1f52-3559-9edc-f8398f76ae7b | -6.83623 | -42.81549 | 2024-10-09 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1d00c88e-7d95-3ea3-aaa6-fa2534a680f5 | -6.83558 | -42.82005 | 2024-10-09 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4d18703c-10ad-32cc-a29e-526231030d30 | -6.83368 | -42.80132 | 2024-10-09 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c4ee25ba-8507-3a0a-adbb-f38bfe066fb6 | -6.67061 | -42.09814 | 2024-10-09 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 982f8e51-e270-3f3c-b140-c6332313833e | -6.65236 | -42.13248 | 2024-10-09 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 303f2304-5d97-30a6-8e9c-fb8c6e8a5aaa | -6.65137 | -42.1311 | 2024-10-09 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 917b8ff8-1725-3a94-bf9b-ccdf53a1fbd7 | -6.65067 | -42.13592 | 2024-10-09 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 73c14d65-43b1-30fc-aeae-081d29c08724 | -6.64595 | -42.13541 | 2024-10-09 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a78bc587-865a-3162-a19e-18de3805384d | -6.48209 | -41.95544 | 2024-10-09 04:38:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 85392d46-6f2b-3d2c-97c7-bb7484eebdc8 | -6.48199 | -41.95694 | 2024-10-09 04:38:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b809ae4a-aa84-3219-858d-513c5189b8d5 | -6.48137 | -41.96036 | 2024-10-09 04:38:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 35902cc4-0a0a-3221-9cec-a023313644b4 | -6.47738 | -41.95454 | 2024-10-09 04:38:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e361241a-6f76-360f-9e2f-84000fc67332 | -6.47727 | -41.95603 | 2024-10-09 04:38:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3b828211-3650-32c6-813b-c7b9fa677838 | -6.47667 | -41.95936 | 2024-10-09 04:38:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 07bf82ee-d354-34d0-a073-5f63535098af | -6.4766 | -41.96084 | 2024-10-09 04:38:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f90be9a3-73a0-3161-a272-d0213e740179 | -6.41789 | -42.41504 | 2024-10-09 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4e30ed0f-f626-3047-b0c6-8bb0098ceeb0 | -6.41385 | -42.41751 | 2024-10-09 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5630138a-1beb-39a2-b220-c0dffd9f7acc | -6.41326 | -42.41466 | 2024-10-09 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f856b022-7e19-3b0f-b00a-97b73a88e375 | -6.29805 | -41.84674 | 2024-10-09 04:38:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2544960d-63bf-3eaa-97fa-7f5306165fa8 | -6.29328 | -41.84608 | 2024-10-09 04:38:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 57fb77b8-e40d-3387-86bf-b82b37cf2c03 | -6.25473 | -42.51407 | 2024-10-09 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 66713c29-1b72-3b08-bb51-8dbd9f1da725 | -6.18606 | -42.60521 | 2024-10-09 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eb2f4872-09eb-3134-9a96-956515b10472 | -6.18542 | -42.60967 | 2024-10-09 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ef164a0-577d-33c6-b259-d93aacbfff13 | -6.18221 | -42.59983 | 2024-10-09 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ec2885e-6eec-35c7-bb43-226cc5b67413 | -6.18156 | -42.60442 | 2024-10-09 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 738adec4-d8f7-323f-af90-f7b8b996adfe | -6.18092 | -42.60888 | 2024-10-09 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 698801c3-bd6b-352a-adae-219a12280502 | -6.17161 | -43.14209 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7da83811-dac1-3241-b2de-50de68120fb2 | -11.23964 | -41.59451 | 2024-10-09 04:38:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ff82c625-28b6-317c-93ad-f21e0035b12f | -9.26158 | -43.52516 | 2024-10-09 04:38:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3865785b-915b-303d-8443-8c9d996006c8 | -9.26016 | -43.52256 | 2024-10-09 04:38:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7dfb87f8-976b-39f2-ab99-453de088901f | -9.25957 | -43.52688 | 2024-10-09 04:38:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |


[Clique aqui para ver as próximas entradas](README114.md)
