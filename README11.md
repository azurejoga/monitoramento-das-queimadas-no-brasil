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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9d9e6be-084a-3896-b51b-429e91a09e60 | -5.4655 | -60.1465 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4860ae3a-72ec-3cb5-a4d6-e7e9a68f71cd | -6.773 | -59.649101 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce1fbedd-2390-3c57-9469-16e84f3c06dc | -9.1694 | -60.754101 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 571da3b7-23e6-3392-a4e9-3a74a0a73904 | -7.4272 | -60.591999 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3a14d69-aea5-30b5-ad59-6e9a81ad6bce | -6.8346 | -58.9426 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3139c5bb-66db-3833-b20c-bef3b2f33e00 | -7.4805 | -61.3214 | 2025-08-26 00:42:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83f1756e-a637-392b-90d0-ed1f032c1c2b | -6.2649 | -60.001801 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32fdc2ca-dc8c-3046-a7e1-ff21df28ab8d | -10.5324 | -57.959702 | 2025-08-26 00:42:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a096de3f-331f-3b5b-a8cc-64136ce70b9b | -9.1836 | -60.7733 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4181457-a324-3c9b-a7ab-f677b136292c | -6.7172 | -58.547001 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad2d3ace-fd26-3428-b817-5e52e3d9d0c1 | -9.1765 | -59.433102 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d331aec-c2a1-3832-9f2e-41b7182f1823 | -10.7493 | -60.694801 | 2025-08-26 00:42:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec329901-9c57-3838-b055-8f08e2b6f8cd | -9.1955 | -59.522301 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4bea1f7b-0f20-3a76-bcfc-4300d151d7ae | -6.8266 | -58.952499 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d580088-0ecd-3ab4-9cab-d91c4a5842a4 | -7.4782 | -61.310501 | 2025-08-26 00:42:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c364328-92f7-3cb2-84f0-129c3ee721e8 | -6.7205 | -58.562199 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f58895ef-ce14-3ebd-91ff-37ddc7b961cd | -6.8185 | -58.962601 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7344e1f8-6910-3123-b8d2-0634497bdeec | -4.9674 | -55.821999 | 2025-08-26 00:42:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f95ba0fb-da6f-37e3-b550-e2152b72ff92 | -7.3937 | -64.306999 | 2025-08-26 00:42:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70b5f3da-be52-3aea-8558-c75ff85eb68e | -18.804199 | -47.581501 | 2025-08-26 00:42:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c2eeee70-c22a-3f1c-8e5e-d2ce236f0ad5 | -6.8133 | -58.938999 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c6446e7-52bc-338f-9a19-d3ede7952f76 | -4.9643 | -55.808201 | 2025-08-26 00:42:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4894d8ea-43af-351a-9fff-243be6d28189 | -9.1618 | -60.7668 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1f45c43-ea1d-3e25-989c-fc93a3e2c88b | -8.8996 | -62.447601 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8c6efbff-bb03-3b73-bc2b-da4f3d09099c | -9.1933 | -60.771198 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e01b3db1-15bb-38d5-b4f6-17e7dfab341a | -7.3742 | -64.310997 | 2025-08-26 00:42:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a210b1e3-edf2-37be-9a3c-4c74a709dd63 | -7.4829 | -61.332199 | 2025-08-26 00:42:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fc47bcd6-6edf-38d6-bf99-eace076371f3 | -9.2138 | -59.415901 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03ff0d11-68b5-3247-bca6-f3bf9376c65a | -6.7908 | -59.636398 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e445e0d-9e81-35aa-bd0b-0d26b691b6da | -9.2745 | -56.8979 | 2025-08-26 00:42:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0588ed73-b70b-30f5-a425-75fc5cb82253 | -8.887 | -62.4361 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9f7db975-c423-3c77-ab74-019ccac66f9c | -3.3983 | -59.437801 | 2025-08-26 00:42:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de17b057-3965-3cbf-a09e-161e1c59b42a | -9.0226 | -65.657097 | 2025-08-26 00:42:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 038350b7-8d7f-3b41-a7b3-085ff0b30b14 | -7.8919 | -62.986698 | 2025-08-26 00:42:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6188295e-8b1b-3472-a14f-a7e28b36d46f | -8.8745 | -62.424599 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17eb53e9-7727-320a-919c-d4b49bfcb871 | -7.4314 | -60.6115 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b4dce48-fd0b-3a16-af1b-becd51e5a9d9 | -9.6473 | -59.625401 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08a48c9d-950d-35a3-802f-ca3605306f29 | -9.2729 | -56.8908 | 2025-08-26 00:42:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de2fd070-1f0b-3775-ad29-79e7ddd743ac | -9.6571 | -59.623299 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd0a137-8f91-3e79-9db5-dbb0e8fb6ef5 | -3.975 | -47.880798 | 2025-08-26 00:42:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb156c0-3298-34d9-a278-ac94f70246b4 | -6.8248 | -58.944698 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8dd58cc-77ee-3fbf-b72d-361f4384a362 | -8.3277 | -50.564098 | 2025-08-26 00:42:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc60be2a-814f-3388-bb50-584d4bfa367a | -5.4538 | -60.139999 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78a13110-e84d-3123-8c32-2bb29e58d7cd | -9.1784 | -59.442001 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b8f0cf4-b7a9-35cf-aaf0-2d4943c28cef | -4.7024 | -56.062901 | 2025-08-26 00:42:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d092d76e-6983-3d97-ab10-d6173cb72d4c | -10.4005 | -57.680901 | 2025-08-26 00:42:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 607e01f1-93b5-30ee-aafb-9edeedf0f078 | -22.896799 | -49.049099 | 2025-08-26 00:42:00 | METOP-B | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 75d72378-9e3e-322f-9cd5-d9a89c4d9238 | -7.4195 | -60.603802 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf2c008-40a0-3cf0-a3f0-e03130aadecd | -9.5832 | -55.3666 | 2025-08-26 00:42:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1128783-5bb2-3e8b-81dd-1733f8a47274 | -8.3304 | -50.5751 | 2025-08-26 00:42:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43fdc69d-7b66-386f-9a24-e57467a212d5 | -9.6552 | -59.614101 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d495d72b-7f82-3d0b-9605-c42151fbcae2 | -7.1962 | -45.291901 | 2025-08-26 00:42:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22daaacf-58fa-3df4-992f-5b2ca4d5aa1c | -10.427 | -64.341599 | 2025-08-26 00:42:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 607023b9-fb70-3b07-8612-4d205a6fe4f9 | -9.2392 | -60.794899 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 928f8aff-49a3-3f33-be69-f47c2b13c64a | -9.1641 | -59.5196 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3211a3dd-e293-34e1-be1e-9c1dcb4b0f99 | -6.83 | -58.9683 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a498f8f1-23d0-3390-976d-7a37f64511af | -6.7791 | -59.6301 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee0a53c2-7358-33cc-9de8-771b6b775796 | -6.8841 | -59.8778 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c594179b-5eb5-3d32-9873-f883f5d2659f | -7.8792 | -62.974499 | 2025-08-26 00:42:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb7ca010-aa7a-3509-bec5-6049e9f5db79 | -22.356001 | -48.3932 | 2025-08-26 00:42:00 | METOP-B | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9aad9804-bc9f-3a03-94f6-6e206a42eee9 | -9.3318 | -63.168598 | 2025-08-26 00:42:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e9c13667-d489-3295-a2f6-054442d4bebc | -8.8425 | -62.417198 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 193e2ca3-b2ca-3de2-a1dd-f2aa6f26b8d6 | -9.2532 | -56.8951 | 2025-08-26 00:42:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b600c52d-d142-30f2-a768-9c35faeca2ab | -7.3692 | -59.655399 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a507ed9a-0c06-3715-a3c6-984cb8404486 | -6.6563 | -58.784901 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff60af17-2d1e-365a-a385-74e5ca139c99 | -7.5262 | -50.530998 | 2025-08-26 00:42:00 | METOP-B | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7945a717-bd33-3a3e-8775-bb4197ab2f8e | -6.5511 | -44.1987 | 2025-08-26 00:42:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a59383e5-eb96-3c3c-9dbc-a680fa981e0d | -6.9243 | -59.353699 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7886376d-918d-3b4c-b778-f60c6b215cea | -2.9263 | -53.687401 | 2025-08-26 00:42:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9e2d847-352b-3a59-89ba-1de3fdae50cd | -8.3563 | -62.9207 | 2025-08-26 00:42:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68230adc-44cd-3003-97bc-8e341eae13de | -7.4174 | -60.594101 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fff0366c-6b98-319a-a5ac-294df26777a0 | -8.9094 | -62.445599 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5f96d162-c8fa-3f87-9165-2f281f5fc851 | -6.7767 | -59.6661 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b46d4b4-8251-35bd-94e2-f37a8faba7ad | -7.6599 | -61.444 | 2025-08-26 00:42:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bbaa3e83-13f7-373b-87a3-420f2571c0ed | -8.8773 | -62.438099 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 13955714-c69a-397b-8f89-d97ea34988e6 | -9.1799 | -59.497501 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 308140ec-0f59-3a2f-b397-b13b5a107f48 | -9.2398 | -60.8955 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab7e0a49-6f3e-3395-84cb-1d5d92c2a466 | -9.1667 | -59.4352 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94d450e5-7586-35ff-8d72-384ca1333006 | -4.9611 | -55.7943 | 2025-08-26 00:42:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e22f856d-9fe7-32d1-b418-14aee3cfb111 | -6.5415 | -44.201199 | 2025-08-26 00:42:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 743ccf15-35cd-3812-a708-ced7e550460b | -9.276 | -56.904999 | 2025-08-26 00:42:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 296b5b85-f2cf-3bd2-86cb-b877851cbe97 | -9.1935 | -59.513302 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bcad843-97bd-3373-ae5a-f16d6bb71688 | -6.3169 | -59.863602 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7b8b5b1-926b-3d08-bcb8-6950d1f13574 | -9.6208 | -55.350899 | 2025-08-26 00:42:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a040e606-8a7d-3f9d-960f-5b615f6c1988 | -9.1942 | -59.420101 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adade602-49de-3223-a5f7-ac9104e7f310 | -22.3536 | -48.3834 | 2025-08-26 00:42:00 | METOP-B | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 858e6544-9fd5-3073-a13a-d10b8b138d9c | -4.8909 | -55.802601 | 2025-08-26 00:42:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97a0bf93-fd47-3bcb-9ab0-200aa7683855 | -8.1183 | -62.851898 | 2025-08-26 00:42:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 01731017-3a3b-3ea7-973e-196d20da9a37 | -6.6895 | -58.842701 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2da8998c-3710-3727-93a1-178aaeaac2fc | -9.0271 | -65.679802 | 2025-08-26 00:42:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3d6dfd2-16e0-372c-abfc-280bade00d5b | -7.3972 | -64.324203 | 2025-08-26 00:42:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67971fa9-7afd-3df8-9c6f-6ae9925eef8d | -7.5513 | -63.012798 | 2025-08-26 00:42:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5df9c61d-3101-3a36-94ee-5e569b1d9d47 | -4.9658 | -55.815102 | 2025-08-26 00:42:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05b62fea-3a20-3e1d-b24f-b21934a40cfa | -6.886 | -59.8866 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab73a871-32b8-355b-9989-4b94567b4cc6 | -3.164 | -49.473499 | 2025-08-26 00:42:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8072d09-c56e-3503-b21e-69263acc45cd | -9.0043 | -65.362396 | 2025-08-26 00:42:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8cbb328d-b988-3bdc-9ff6-1b2a87021cf2 | -10.4172 | -64.343597 | 2025-08-26 00:42:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4b58a831-12cc-3a61-9b12-053cf3ca2b1a | -10.3907 | -57.682999 | 2025-08-26 00:42:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3b68d14-b081-39aa-beaa-27130b7953a5 | -9.2693 | -59.7733 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36b96b57-87fc-3161-90a7-ab9345ba37e5 | -8.8452 | -62.430599 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
