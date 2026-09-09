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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dd8ad49-e719-30b6-abf8-b57d8f5b07f1 | -10.5404 | -47.1036 | 2026-09-09 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18de3ed6-e681-357b-96f0-78da32d7cfb1 | -6.173 | -44.6563 | 2026-09-09 00:48:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 734a64a4-b10a-3368-b343-9f6395d58d41 | -6.26 | -47.343899 | 2026-09-09 00:48:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bfc4bfaa-090a-3e55-b7d8-42946a2a886b | -2.935 | -50.474899 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e47836a-8888-30ae-8ca8-cfe56b431442 | -10.3051 | -46.8965 | 2026-09-09 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b045e659-2399-3fe6-b438-b107f643e889 | -10.3149 | -46.894199 | 2026-09-09 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 903f6078-6f2e-3286-bf1b-31b5e67def19 | -6.157 | -44.6325 | 2026-09-09 00:48:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7118ba0-4d7a-371d-a062-091b83f3dbb2 | -5.7793 | -45.072601 | 2026-09-09 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4201e05-3fcc-3f5c-849a-065073e80607 | -3.1536 | -60.663601 | 2026-09-09 00:48:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20a662f3-1913-3220-ab8b-23bbc6d39321 | -4.0102 | -51.0228 | 2026-09-09 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4ec55ae-db8b-3b86-bc41-beb9f2e144fe | -5.6738 | -50.093498 | 2026-09-09 00:48:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00f8f20a-a963-3c15-b6d5-8f109c265d11 | -1.6101 | -54.911598 | 2026-09-09 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a8b57c0-3ff5-3222-884f-fb82e23cc5f3 | -10.7372 | -45.939098 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd1436ac-7ad1-30cb-885e-4b5c73ff79be | -5.8245 | -53.793999 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a43cbff6-b7b4-37b5-9703-502881b787de | -6.3919 | -55.237499 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eaacc54-3a29-362d-a2e4-2fc8fa5a904f | -11.0044 | -45.0807 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3db09e8b-7ba8-3c86-a713-3c3a6ecb2fd5 | -3.1493 | -60.644402 | 2026-09-09 00:48:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d211d4c6-5221-3d85-9de2-0f135668ade0 | -6.3578 | -43.599098 | 2026-09-09 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d64c2d5-5aee-3d3b-9c4a-bf35b33e340a | -9.698 | -43.433102 | 2026-09-09 00:48:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9b06c2f6-f229-3f43-bdc1-2ac80eedbc66 | -6.262 | -47.352798 | 2026-09-09 00:48:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9b9825c-7d0f-39dc-ac42-00ea4a6a672d | -6.0303 | -42.646198 | 2026-09-09 00:48:00 | METOP-C | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e28e4e48-ffc8-30d7-bc29-394a8e452aa7 | -6.7599 | -44.569599 | 2026-09-09 00:48:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06e35735-67bb-30e2-bb32-e52b192d5949 | -10.3072 | -46.9049 | 2026-09-09 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48d21c2f-b5b2-3baf-b42a-52de78ef61c9 | -4.002 | -51.031799 | 2026-09-09 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87eefdba-83d3-3d37-8f21-62073664a343 | -11.0069 | -45.091099 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71f26e5d-de0e-3d83-aae3-5c28c92d1d9b | -4.4976 | -45.9142 | 2026-09-09 00:48:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11c670cf-9b6d-3330-a1d2-0d8aeca8eaa8 | -12.8519 | -44.390999 | 2026-09-09 00:48:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec1b7400-ddb4-38cb-8c18-8006776d5d18 | -5.7568 | -45.0648 | 2026-09-09 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13096b50-c250-3201-92fa-db69026487e7 | -4.2969 | -49.093498 | 2026-09-09 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99e2ea82-d62b-3b99-b434-6cf82eee4124 | -8.0901 | -45.6721 | 2026-09-09 00:48:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ab652d2-d70b-30f7-92ae-85ebd90f3b6a | -5.3622 | -56.008801 | 2026-09-09 00:48:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33bd74d8-42a2-328d-b923-66bf82bc0be8 | -11.0018 | -45.070301 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c5bd6522-9528-3c72-b0c6-22f9b046a670 | -5.8003 | -53.823799 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6e2157-2af3-35f6-b134-8f074468b189 | -1.6083 | -54.903702 | 2026-09-09 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f9efd47-8065-3e1f-8793-2d83ba24b8ba | -10.5384 | -47.095402 | 2026-09-09 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91b3b4a2-58bf-3aee-957d-ed3d33c0d29f | -10.7334 | -46.0089 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ddb1593f-8495-367e-a806-c33eeaec1adc | -5.7666 | -45.0625 | 2026-09-09 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b37118dc-7dba-3897-b60a-62b73368718c | -10.7417 | -45.957699 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 128b4da2-13a7-37db-aa96-1e9b75685dd9 | -7.1961 | -43.616402 | 2026-09-09 00:48:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2640f767-063a-3c00-b769-a38318f930ec | -9.7638 | -43.489601 | 2026-09-09 00:48:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 953a3909-a0cb-31c3-b490-f3d0bbc6a381 | -1.6119 | -54.919498 | 2026-09-09 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95fe2146-5860-3e34-baa0-c8becc5896eb | -2.8021 | -54.765099 | 2026-09-09 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d585a9c4-124a-3cca-818a-3bd5cbeb25fb | -12.269 | -45.816299 | 2026-09-09 00:48:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23826e45-5f69-32d9-8701-145933fe688b | -3.2646 | -50.070099 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 139cde15-f390-319c-8b3b-2a21726ef03b | -6.8633 | -46.021 | 2026-09-09 00:48:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08b6ab19-c998-349b-adbc-8f5959162d76 | -2.9334 | -50.467899 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfb587df-53e1-3492-ada3-c692fb767220 | -4.3049 | -49.0835 | 2026-09-09 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41a95f3d-773e-3082-aa20-f59baf60f772 | -4.0118 | -51.029598 | 2026-09-09 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb475dee-c615-3abe-9adc-286ba310c634 | -6.0259 | -42.6283 | 2026-09-09 00:48:00 | METOP-C | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 242e054f-0808-32f3-b775-77b445e8441a | -4.2933 | -49.078098 | 2026-09-09 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5d1de7e-bf55-3bef-8a6c-717e820ecae0 | -2.9481 | -50.486801 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa16555-4412-3ea4-894a-e6d6bcc29cd9 | -1.3155 | -54.658501 | 2026-09-09 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fbcb74d-1137-39ad-b5a1-4fad18727f2e | -12.2668 | -45.807201 | 2026-09-09 00:48:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 35421c09-8c66-33aa-aa0f-1c9c5dd7e90f | -6.8731 | -46.0186 | 2026-09-09 00:48:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93f98e45-f308-303f-b0b4-15843918d27b | -9.7049 | -43.460701 | 2026-09-09 00:48:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ce3ae23-6644-3ad5-b846-73b9d4fa145d | -5.2141 | -55.9883 | 2026-09-09 00:48:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a5eec0a-e103-320b-a64e-ca0715c9d4d2 | -10.7395 | -45.948399 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb76b98f-04fe-3d95-84c6-d9979b026545 | -7.5223 | -45.929298 | 2026-09-09 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f7d52f9-bf3a-3eee-9bbc-e2539a9de931 | 0.6175 | -50.811001 | 2026-09-09 00:48:00 | METOP-C | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d0ad6071-594c-3538-82aa-b338914354eb | -10.756 | -45.9739 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0dea438f-36a5-32e1-b21c-9c1baf099603 | -1.195 | -55.7099 | 2026-09-09 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8046ff7f-45a0-3e09-83a4-1be583b84aa8 | -6.1665 | -44.6716 | 2026-09-09 00:48:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9c17eb8-297c-3d7d-8c53-e4ad9d843f18 | -9.262 | -45.650101 | 2026-09-09 00:48:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c72e30b-7417-30d9-9c7b-cedcec024090 | -6.7869 | -58.942699 | 2026-09-09 00:48:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83da58d4-636f-3e7f-b6af-c8b4302570ed | -2.7655 | -49.473099 | 2026-09-09 00:48:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdebf65b-db8a-3cf0-8155-89dd13b328ad | -3.9643 | -47.581799 | 2026-09-09 00:48:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad38a0d-4884-3fb2-8ed5-b64f1aee7693 | -2.8899 | -48.2775 | 2026-09-09 00:48:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d9bf228-b177-32d5-9ad6-f597da2d867e | 2.0127 | -55.8279 | 2026-09-09 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2650ff5a-4c4c-3346-b30c-ed2e4e67bb7d | -3.2662 | -50.077301 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5868453b-3149-3af2-b32e-d33e6981f59e | -9.7672 | -43.5033 | 2026-09-09 00:48:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 862ce223-c358-314b-8d57-ee09043420cb | -1.1872 | -55.7206 | 2026-09-09 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d10143ec-921d-34fc-a179-a67995cf835f | -5.6081 | -44.832699 | 2026-09-09 00:48:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db8c8e54-7f46-30c6-bce3-b7b7b05453fb | -1.1931 | -55.701401 | 2026-09-09 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95076467-7c4a-3a73-b2a7-6776552f7b3d | -5.8227 | -53.786201 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd9eae30-cea7-3c34-9c46-1fd188b654c4 | -4.4879 | -45.9165 | 2026-09-09 00:48:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc11776a-0fa2-3c6e-bec1-e7e12efce9ae | -1.1833 | -55.703602 | 2026-09-09 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6dfd880-35d1-3dd5-ac55-b33e56e5731f | -6.04 | -42.643799 | 2026-09-09 00:48:00 | METOP-C | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ff2bb6c-4834-3377-b998-b7f854f57ac7 | -6.1536 | -44.6609 | 2026-09-09 00:48:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a437d112-cb50-3779-b5d7-1f2c2454ff30 | -3.9534 | -59.354198 | 2026-09-09 00:48:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49356a48-7697-31a1-8dcb-167985f186b6 | -3.8008 | -52.4058 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdaf37d8-175e-3e8d-8762-4d4a3fbe5b99 | -10.7613 | -45.9529 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58e82934-1ad5-38b0-93f8-2f6cf998b595 | -10.735 | -45.929699 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c590fa61-3e0d-3d8c-b15f-c0837a001ec3 | -2.9318 | -50.4608 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aecb36e-c1b7-36a0-9425-0ad355375af9 | -10.3129 | -46.885799 | 2026-09-09 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dda1e03f-6528-366e-be4e-f5e5530dfcf5 | -6.2502 | -47.346199 | 2026-09-09 00:48:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1fdc4188-9cc4-3aa5-a374-0bf22466a495 | -5.6015 | -44.8479 | 2026-09-09 00:48:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ddfa6b5-f3f0-3ff9-8cdd-f965a655d2b8 | -8.1023 | -45.680199 | 2026-09-09 00:48:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1a99e89-e2fb-3f49-8e6a-6e1ad68d71a5 | -3.9631 | -59.3521 | 2026-09-09 00:48:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55adaba0-8779-3abe-8f1e-e72d7315db9f | -5.8164 | -53.803902 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c95d8b3-2f10-3f90-9549-9fc91adf0987 | -6.394 | -55.246899 | 2026-09-09 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5f34cd-b69b-3335-8c84-247da31b228a | -14.2853 | -44.577999 | 2026-09-09 00:48:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cdf10c30-047b-3276-a67b-1b197c6de9dc | -3.4488 | -47.273701 | 2026-09-09 00:48:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95e47272-d246-3a69-8d93-4dc759b0e8e4 | -9.7477 | -43.508202 | 2026-09-09 00:48:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2a13c9b-6e22-3df0-8605-dce1ce523757 | -10.3031 | -46.8881 | 2026-09-09 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70b5914f-6d02-30aa-85a5-81c3dc5db4c4 | -10.7515 | -45.955299 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c1f9612a-a3fa-3b38-8007-a01d2669812e | -2.5585 | -54.735199 | 2026-09-09 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17f6bb03-b6f7-332a-8ffc-8511d9625db8 | -5.7696 | -45.074902 | 2026-09-09 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8855b45-78ca-3ae1-a2f1-c026c36e8213 | -1.1852 | -55.712101 | 2026-09-09 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a49940de-1f73-3e41-bf6e-6aef7221cf53 | -3.546 | -48.173199 | 2026-09-09 00:48:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efce6558-6b7e-3a30-9cbb-9c7ab4640fc5 | -4.3067 | -49.091202 | 2026-09-09 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
