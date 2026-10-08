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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7027cb2d-e4a9-3ccd-a5ab-e37d79d9e579 | -3.2822 | -54.061798 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0e8d45b-facf-317b-88bc-f117370847a0 | -3.8693 | -50.414398 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c1e1494-fcdf-36f2-8305-8134e864b471 | -3.6972 | -54.2113 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a85242f7-1d4c-3389-b6c2-82d85a8fd5ad | -0.0867 | -49.485901 | 2026-10-08 00:48:00 | METOP-C | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ef77959-2f26-3c81-b8d7-29dc5bc59d4a | -3.2587 | -54.003502 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4198fd35-494e-30df-932f-b98121171f1d | -2.9414 | -54.1931 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99b43a0a-6dde-3896-ab15-460b6a168699 | -3.714 | -54.240101 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 250a27c7-fc8c-3486-a540-6d2552ea1a0f | -2.7928 | -54.083099 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90460ede-77b5-38bb-979c-8986b18474b2 | -3.0094 | -54.130199 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6a6a892-5b80-3f09-bde0-9ea767f19f3f | -1.5215 | -54.516102 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36f649af-dad3-3e23-a01e-e6674965f293 | -4.3038 | -50.777401 | 2026-10-08 00:48:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e23b3f7a-4bc2-3840-a624-9b70579c432e | -2.8624 | -54.162701 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fed4f59-3f6f-30b6-bdb8-22b2cc2dbc84 | -6.2041 | -52.869301 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4ba4b56-00da-3236-a92c-f4a15f9c8e79 | -5.8125 | -53.826599 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea2920c6-e577-3cd8-92da-460054bb7553 | -4.2858 | -50.7887 | 2026-10-08 00:48:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dcf28ac-1944-3382-aff8-78bcb52cea67 | -5.8394 | -50.144798 | 2026-10-08 00:48:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c43bf3b-8f8c-3e33-b923-655226d6a7dd | -3.566 | -54.495399 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6edbc916-67d8-36d6-a7a4-6bb145194879 | -2.8872 | -54.181198 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65088e2e-312d-3565-8ae7-4057758aaa67 | -11.0021 | -45.4258 | 2026-10-08 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ffa772cb-4155-3af5-a5b9-da606b39f05c | -1.5004 | -54.828701 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b14d7c0d-8802-37b0-bc59-d7f3ea3fa4ab | -8.0827 | -55.318901 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c985199-e958-3090-93ef-b799bfc66950 | -6.0296 | -51.736801 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d249678-0cc2-3583-b660-c206e595d78c | -11.7845 | -46.7841 | 2026-10-08 00:48:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d67a4c4-cb8a-3425-ae5f-6a08034e8bbd | -6.4584 | -55.482899 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b66d45b-2ec3-3d4d-bcfc-9d87126d334e | -3.1744 | -54.085602 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f523862-da46-3e88-8f20-3e6bee5a959c | -2.6884 | -49.0588 | 2026-10-08 00:48:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5318ee9e-ab7c-3c88-aae4-057f91753011 | -3.006 | -54.2509 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f20c395-d669-3d63-aefb-27da8be4af01 | -3.0179 | -51.016201 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46cb4d43-b80d-3cc0-9b39-c0e96ba540ee | -3.0129 | -54.145401 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb6099cb-488f-3f57-9cc0-543f142a4072 | -6.353 | -43.349098 | 2026-10-08 00:48:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afb87fd1-d6bc-3cdd-b6d1-a57a9c989195 | -2.9431 | -54.200699 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d33d9dff-821b-36a9-acd3-fefa9d385f6b | -5.1288 | -47.109901 | 2026-10-08 00:48:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 013aca03-c20e-3518-8b45-fad229409119 | -17.117701 | -41.337898 | 2026-10-08 00:48:00 | METOP-C | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 955fdfdd-48ef-35d1-b92b-712b9cb15d72 | -3.0567 | -53.930302 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2148608-1505-35ea-b130-9aaacba3da5b | -3.1813 | -50.562302 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3565dc53-cc24-3f5b-8d67-2a956f0ef8b0 | -3.219 | -53.965 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d43404d-b186-3377-92c3-5ad73e31e29c | -8.9064 | -49.978901 | 2026-10-08 00:48:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10c13386-7e20-380e-8522-fe064c3daac5 | -10.4352 | -47.281601 | 2026-10-08 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81bb787d-7711-38c3-b78e-0b5e882f4d66 | -3.1548 | -54.09 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aa69387-57de-311e-9d49-703038c20358 | -2.7962 | -54.098099 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68b6484d-5694-3f38-86e4-d8779f5ed338 | -6.1385 | -47.933201 | 2026-10-08 00:48:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1651f2a-8680-3f17-b4ee-ec8fe6a1dfef | -2.9036 | -54.027 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f96f8302-a65f-37ed-b80b-3c1e0f51cc8d | -5.0872 | -49.7038 | 2026-10-08 00:48:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ddea54c-75af-3f5a-8579-8fad17e62b86 | -6.0566 | -44.028099 | 2026-10-08 00:48:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6dc4a91a-da70-32da-b90b-8b0e41b9f8ff | -7.3832 | -55.212299 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b0d2870-0f23-39e5-9677-c42294029d49 | -3.3082 | -53.858898 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00961339-e762-35f3-88e9-207e15c0f9e1 | -3.4737 | -54.633202 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3d8c4a2-ab67-330b-b0b5-aa89c3b05903 | -3.2216 | -53.885899 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db2c52d-4f7e-3d25-a74e-6dc028d7bf22 | -5.2833 | -60.105701 | 2026-10-08 00:48:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fbd12376-7d83-3049-adea-1867ea8b2544 | -1.5222 | -54.563999 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fc532f6-ba50-3525-a769-b3dcd3153303 | -7.3853 | -55.221901 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38dbcd5f-95b2-3f9a-be1a-dc0e0057d3b6 | -13.8398 | -49.6852 | 2026-10-08 00:48:00 | METOP-C | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aae3b3c8-fd29-3102-b598-1bde78897fcc | -3.0251 | -54.063202 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 984e83d0-eb43-3a69-a67f-ebbf3c34c13f | -7.603 | -46.753201 | 2026-10-08 00:48:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac1857a5-ba75-301a-b838-121650fa2ece | -6.2123 | -52.859901 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b259db93-e87c-3e62-bd15-dae31c0983dd | -3.2719 | -54.016499 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f19f11b-002b-361e-9cf5-2f6557b2bf65 | -5.1732 | -45.3531 | 2026-10-08 00:48:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c30aaeea-40c0-3642-a40e-83ad5ba45376 | -3.5859 | -54.583199 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a08b475f-c6a1-304b-a102-277d6972042c | -3.8469 | -51.93 | 2026-10-08 00:48:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e902aa28-f37a-309d-88bc-e64f51bc96e6 | -3.5362 | -54.636299 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d2d44cd-b75b-3dbf-a6ad-b954c8172bae | -9.284 | -50.321602 | 2026-10-08 00:48:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459e6b1f-beb0-33d1-ae9e-7e3752072956 | -10.2472 | -49.663601 | 2026-10-08 00:48:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfbcfb14-a63a-3a40-b6c0-32d2aae4600e | -11.5314 | -47.591999 | 2026-10-08 00:48:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 944a456c-e04e-37c9-9677-4cf5384cd27c | -4.2685 | -54.872601 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9e6a6ce-4cf9-3a72-ae52-0360a540f5d8 | -4.2956 | -50.786499 | 2026-10-08 00:48:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6c81007-a043-32cb-b436-d36ead3c1761 | -6.2286 | -52.6586 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcc938eb-2105-3828-bb6d-80e0543199f9 | -3.1436 | -53.724499 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a578b2-4e25-3de9-bb53-a0e32da8042a | -3.0167 | -54.750999 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48bae71c-910f-341d-8182-07c5531842b1 | -3.5416 | -54.6605 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd03dc72-9482-365a-ae9a-a1ab02d54a0a | -2.9812 | -54.7757 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29c7ca30-aa9f-3a83-a1aa-b5faaa92c6e5 | -3.8301 | -55.983799 | 2026-10-08 00:48:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ba6c35b-6790-3c0e-9a00-8e3bbe51b557 | -10.6776 | -51.984901 | 2026-10-08 00:48:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4596bef2-875c-3156-9f03-8ff3e46495ca | -6.3239 | -43.356201 | 2026-10-08 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44481b67-8065-3950-8300-831218805e40 | -6.9377 | -43.6745 | 2026-10-08 00:48:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a3b16dc2-8159-3616-be1d-a9fe914a0aef | -2.9766 | -54.121601 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 964bf85c-60c0-3e37-8c1e-18c349751039 | -3.1017 | -54.173599 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60899bf5-59c4-3a9c-9f82-f3dfd008fbb5 | -2.9258 | -54.124802 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0296383-0617-38f8-81b4-946c65ac05a7 | -16.8706 | -40.600498 | 2026-10-08 00:48:00 | METOP-C | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2e95ba82-f186-3714-9f63-d1d94d80619c | -17.6299 | -46.671902 | 2026-10-08 00:48:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b106cddd-c974-3245-b86a-d702df4f1f5b | -2.7065 | -57.465099 | 2026-10-08 00:48:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28b31d93-e127-35e2-a84d-4604070008f4 | -4.0523 | -55.327499 | 2026-10-08 00:48:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d553bdb-cff8-36fa-8445-b473e55db02a | -2.1234 | -54.806198 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 913ca5cb-6c6e-36fd-be68-3825a5c13300 | -3.0118 | -54.050301 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fec8c66b-f748-337e-bbf4-4759110891d0 | -14.7532 | -47.143101 | 2026-10-08 00:48:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df4e11be-e743-3b1e-9c3f-cf7426777fe1 | -2.9374 | -54.130299 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee852029-842a-3b76-a920-c6de684eeac8 | -7.848 | -49.2831 | 2026-10-08 00:48:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de441c89-cbfc-3f45-9f9f-2d901760f957 | -5.2686 | -45.406601 | 2026-10-08 00:48:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6a47650-84b1-3706-b5f3-9e2d97cce5b2 | -5.9714 | -55.367901 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03754cb6-6d28-3974-ab45-d21b3b89f895 | -5.6726 | -46.361099 | 2026-10-08 00:48:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d97776c-ba45-31d7-8d67-7572e698dabe | -2.983 | -54.783798 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45ffbb21-01f3-362e-80f7-00fee0c6174b | -7.2031 | -45.348999 | 2026-10-08 00:48:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fec4619f-55f0-3d6e-988d-00524307bf99 | -5.8378 | -50.137798 | 2026-10-08 00:48:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9e31353-48a9-3b4e-ae3d-567d65d5be56 | -8.908 | -49.985802 | 2026-10-08 00:48:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e61bb263-1100-3c1a-bbe6-5c7842082a34 | -2.8781 | -54.095798 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69d82dfa-2970-3d18-96fe-b5fa5512b26a | 1.7562 | -55.5895 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd598b7-72a1-3ed9-af71-026af3ba35b4 | -9.59 | -48.9174 | 2026-10-08 00:48:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0297581a-9dab-32ea-aa29-1b09fcd31db5 | -1.5182 | -54.816502 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8fd3079-b978-356c-aa08-cc73590abda6 | -3.5827 | -54.659901 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e155fbf-c99d-3bc0-9962-ae70fc318e4b | -2.8728 | -54.208302 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db586c7c-8448-386e-afb4-676e391d20ff | -2.8423 | -54.119598 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README31.md)
