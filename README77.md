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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac3f1189-e55d-39ea-b012-8d2acc3e2b35 | -2.45993 | -49.05762 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5bc6358-5513-34e5-8de9-292e7092755d | -2.36984 | -49.19859 | 2024-11-03 05:08:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fc7b7eb-176e-3ce3-9a98-f332623ddda7 | -2.36746 | -49.0253 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 461489eb-d949-3e3c-81ee-22c6faf10dbf | -2.36348 | -49.0195 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b02babda-6371-3d0a-92c4-2d3a80e2c6f6 | -2.3595 | -49.0137 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79fea909-5d89-3338-ac99-5424518549de | -2.35874 | -49.01877 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d846811a-1f86-312b-9407-e2f9333214d7 | -2.33368 | -49.61363 | 2024-11-03 05:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c592344-4f85-3894-bf04-c4592c249db8 | -2.33337 | -49.61515 | 2024-11-03 05:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d62c94f-91fd-36cb-99fb-893f3aec0e57 | -2.32647 | -49.03968 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 08bb1a9b-b024-3365-9159-c67f5f4b59c2 | -2.32572 | -49.0447 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c2274c7e-db9c-3516-a2b7-90cf5d00ebcd | -2.32176 | -49.00127 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d13dc4ee-3072-37e3-94be-90aac831258d | -2.32173 | -49.03897 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6980d641-146d-3f7a-961f-86281051ab89 | -2.27817 | -48.96857 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4fe36a2-3dd7-3741-9ec1-3f31c0f8b642 | -2.27739 | -48.97363 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c117ab68-4a9d-3b41-8364-15edf28dbacd | -2.27282 | -49.67593 | 2024-11-03 05:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a88edfa-51e6-3175-99cf-a363bb7c65b6 | -3.53234 | -50.11632 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee9c43ca-3f6b-3cf2-8cde-4855ecbe1a31 | -3.47978 | -50.1309 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b3f34f4-9d3d-3654-a5f2-f38b9268d556 | -3.47556 | -50.21963 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74df8f24-d30e-35bf-bdff-64bc1d501f0e | -3.4753 | -50.13024 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56e5d309-c4ac-3544-ae99-76179904294c | -3.44346 | -50.37298 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 746dee02-302b-38a8-abec-a292f8560488 | -3.4354 | -49.28351 | 2024-11-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| be08eaf7-84fc-3634-894e-e6d4b6df2b43 | -3.43462 | -49.28862 | 2024-11-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 676bbe08-f7cd-3ae0-a7e8-f4b7f4a599d4 | -3.43143 | -49.2777 | 2024-11-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2b0bdf82-9c5f-3c8a-957c-ec23c3309d43 | -3.42172 | -50.22289 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d820939-9225-3327-8dc0-9101d01c6cf9 | -3.42104 | -50.22725 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17c6790f-44eb-354a-8f21-8caf1f726569 | -3.42028 | -50.22493 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b43fe406-45c2-3314-81e0-5dfaf98f5e8b | -3.37653 | -50.25138 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65ac5b5c-6602-3203-b315-fdd7724e5204 | -3.37209 | -50.25078 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35d0bc1a-bec8-305b-ba13-1dc1607341ab | -3.37143 | -50.25518 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8691eec7-5fb4-32df-8ae5-4abee617392b | -3.30107 | -50.33823 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0c3f076-3ffd-3acc-ac86-f62f92d62a26 | -3.30069 | -50.33607 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fd3585f-755e-3e8f-8bbb-4510e59888ca | -3.29942 | -50.34464 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fd8e324-2e02-3702-a948-b642747fb9a4 | -3.29628 | -50.33546 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf6aa1f3-9833-31c0-9bbd-629db376ef43 | -3.27926 | -49.69303 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87619dd7-305c-32b6-9644-2b5f1d36a91c | -3.27908 | -49.69138 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8067106f-eea1-3c89-a4d6-dffece08497f | -3.27839 | -49.69609 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be4d330c-8cc0-37c5-9cb6-236d95d02ffd | -3.243 | -50.24604 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96ad1dba-ac80-3db3-8d7b-6a2a70348c8b | -3.23856 | -50.24552 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6c1f3f4-1aee-388c-b656-3fc7b3c4e455 | -3.2379 | -50.24992 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e6a9442-74b9-3d70-b717-f54a870eb3e8 | -3.20569 | -50.22848 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4293fd0e-e45c-305a-96c4-fce24ffce025 | -3.20126 | -50.22781 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dad096b-d8ea-392b-b1de-839c7fcb52c1 | -3.20064 | -50.22681 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61a92be0-5422-38d1-8acc-6bd23ab91d7c | -3.16016 | -50.23043 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 519f82c4-1ef0-3655-96ae-db696593158d | -3.1595 | -50.23473 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3778adca-301c-3534-b3ea-6366b49c4cbc | -3.15574 | -50.22975 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84940622-2c8a-344e-814e-d9c1a8f1709a | -3.15508 | -50.23407 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 693689b9-733c-34b4-b912-c82a7d5a6207 | -3.13063 | -49.99141 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a3bc1a3-b2c7-3f74-8f11-dadbd4a07d06 | -3.12859 | -49.98411 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 057f5ac6-d40b-370f-8ece-9060ccf31c51 | -3.12794 | -49.98857 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1709c1a-9425-3629-a2dc-cb02624b908f | -3.12728 | -49.99303 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8b29b874-7266-39ea-a5fd-8fab3c758915 | -3.12683 | -49.98628 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51e29bea-98be-3f9a-9fea-e2e0f66463e1 | -3.12619 | -50.04964 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0769f6b6-c3f4-3e6c-8fe7-b2e8a361ea7c | -3.12614 | -49.99073 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f63bd613-5145-3cdc-b015-a30bc02817f2 | -3.12545 | -49.99519 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6fa12a6d-24fe-3276-9ee6-64a3b35ba211 | -3.1241 | -49.98343 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cf8cd8f-65e0-312d-8dc0-b94078b13fcb | -3.12303 | -49.98115 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3007d168-59aa-35da-8ea9-a62d09294e75 | -3.12279 | -49.99235 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01eee14e-a30a-336a-9702-3ffa3984edf5 | -3.12234 | -49.98559 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf652583-834d-36bb-a784-3c86caca02db | -3.12165 | -49.99004 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c191ec3-d5b7-3235-974e-3843aa84daeb | -3.10639 | -50.31823 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61c0660e-f252-3453-b844-9a7fba7922b7 | -3.102 | -50.31758 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e102d1f-0f7e-3229-834a-11c59f52b86e | -3.10013 | -50.29997 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2cc3aa4-bfcc-3a61-9cfc-63b762bee01c | -3.0995 | -50.30417 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3cb92c2-9341-3544-b2d9-60b462c837bd | -3.09887 | -50.30843 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eabc8035-e12c-3699-8ef7-acecd76ca747 | -3.09573 | -50.2993 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fae5df7-f76c-39fe-8365-325a162f0fc1 | -3.09511 | -50.3035 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 734f5c13-19dd-343c-a46e-c6173195fdd2 | -3.09168 | -50.30062 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a34720b4-656b-3f94-9150-9b2f6127d4ab | -3.09134 | -50.29865 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ae9bd0e-fcc4-3675-8499-36330310c99c | -3.09103 | -50.30484 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 565d4f19-d76e-3eb1-aac8-6d5488cece87 | -3.08236 | -50.00684 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c80aa7cc-c064-3a8b-82ee-efb69b20b004 | -3.08159 | -50.30772 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90511653-5784-33de-a848-7d69564fb5a9 | -3.07851 | -50.2986 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 422ad60d-3db8-3d00-9640-e973dee2a87d | -3.07788 | -50.00615 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d8e21a8-39eb-34e0-b4e5-485677c25a80 | -3.07786 | -50.30279 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b0a1345-595e-36cf-8881-2c344ebbab49 | -3.07654 | -50.01503 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ab76250-ea57-3ac3-968a-de19574382cd | -3.06478 | -50.50795 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3a15288-d8fc-3b3e-babc-3ac6c28fdad0 | -3.04517 | -50.16228 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aff17bb1-e729-3c5a-9021-78e40458945c | -3.04173 | -50.24484 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2fc54e5d-24dc-39c2-94a4-7b1c1db1aded | -3.03794 | -50.24014 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 625516c3-09f5-3519-9e24-b4c5b87b6c24 | -3.03731 | -50.2443 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 197e825b-b569-3583-b004-99337a673dec | -3.03667 | -50.2485 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e03c504c-3b71-3f11-bd10-da62e198635b | -3.03288 | -50.24374 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 29650bd0-ae85-3307-a23e-709f726bc301 | -3.03225 | -50.24795 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d240c030-b2e4-3f10-b498-1c55b3108d56 | -3.03161 | -50.25216 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 88135990-e769-37a1-95b0-3e692d54eaa0 | -3.03098 | -50.25632 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ebd5bf3-f949-3d59-9e83-d014376ff5fe | -3.02783 | -50.24734 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0eb6257d-5c8f-36d1-99c8-be93090c6410 | -3.0272 | -50.25154 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cc690a3-00a8-3251-9763-379590943525 | -3.00976 | -50.5428 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4999b223-5a10-3fb3-b5c5-5b824b3cfbbd | -3.00915 | -50.54678 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e09dc98f-d635-3fc7-810c-616d32a3eb2a | -3.00544 | -50.54215 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56952229-ad0f-31b7-98e5-4ed226758786 | -2.89815 | -49.52392 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5f2b3956-4e9e-3ab1-8487-d282f7d49257 | -2.89353 | -49.52323 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5374d720-aeb2-3fcd-8bd9-ae1287972906 | -2.82835 | -49.20024 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe1b573b-f1d3-3bb9-a68c-560c269b50b1 | -2.8248 | -49.19606 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3356104e-9948-3019-bf52-5728093e447e | -2.82407 | -49.20105 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f75b7ee1-87e3-3f3c-8d9a-3b54cd1755f9 | -2.82363 | -49.19953 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2c7014f-7dd3-3e7e-b0b8-36fcb5aed553 | -2.82011 | -49.48453 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a592690f-8f5a-397c-a336-f12aedde29b2 | -2.8194 | -49.48929 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| dff798f4-1a24-3a4d-80ce-97ec7408e133 | -2.8162 | -49.47905 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| da1c00ea-984d-3a27-bcb3-1233a603492f | -2.81549 | -49.48381 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |


[Clique aqui para ver as próximas entradas](README78.md)
