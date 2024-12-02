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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab7bee8c-6544-3e95-8ad5-a150c9c3701f | -2.5632 | -53.383801 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bee625e-f491-3fa9-9f1d-4f5f395d202a | -4.6259 | -45.451599 | 2024-12-02 00:18:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b6fe478-806c-3a4c-abfd-6bd892ddb3b1 | -3.3273 | -50.239101 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bfb567c-68b3-38ee-89f1-f74688468223 | -2.23 | -46.3727 | 2024-12-02 00:18:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4bbf58-0588-323e-b8c7-c56182b4177c | -3.3988 | -50.238899 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a2b6540-d680-3fe8-a145-c8fb3a73ac63 | -2.9179 | -45.819698 | 2024-12-02 00:18:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1449545-9e34-3188-af03-e53b68fbb692 | -5.578 | -45.201401 | 2024-12-02 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62942d79-edb7-3bd6-9f41-5915b9ee9ecd | -5.1258 | -43.202 | 2024-12-02 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fbe9b60-3cec-3538-8ef2-57f148e6c102 | -3.1454 | -45.4753 | 2024-12-02 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a5af4443-f1bb-36f7-8b61-dc789db95966 | -4.267 | -50.8551 | 2024-12-02 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8031a9c5-828f-38c7-b6a3-e19c3b8673b4 | -3.4769 | -46.0879 | 2024-12-02 00:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f6f76028-f24e-392d-88c6-fa699151c642 | -1.8985 | -46.4263 | 2024-12-02 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a9e1188b-7a05-31db-83d6-60abf930252b | -2.5796 | -53.3927 | 2024-12-02 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 341da59c-45f3-3d06-a44a-f9eee6722b19 | -2.8013 | -53.043 | 2024-12-02 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9517e1f9-adfc-36e1-8c6b-6e6f664347c2 | -2.6348 | -53.3712 | 2024-12-02 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 21818559-1ec9-328a-ac48-afee8b2b4fef | -2.8197 | -53.0425 | 2024-12-02 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ccc9f128-22b6-37f2-9470-8e1efbe167b4 | -3.2591 | -53.6186 | 2024-12-02 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 504e3c90-05b9-3514-a712-d094f21176a7 | -2.9208 | -45.8417 | 2024-12-02 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e1ee36ac-a4b3-31ba-b2d5-1f3301d8dd8e | -3.1453 | -45.4978 | 2024-12-02 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bfe07ce3-c4c0-3f42-a511-0893a68b25a1 | -2.5428 | -53.3935 | 2024-12-02 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6c6fa889-4153-3c71-a4b6-507c08e425bd | -3.4017 | -50.2171 | 2024-12-02 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 0a86244b-efea-3f8b-8260-fc61d7f5cfe2 | -4.8174 | -48.6272 | 2024-12-02 00:20:00 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1899739f-5383-3e8e-a241-2a21047b66dc | -3.4017 | -50.2381 | 2024-12-02 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| f2e4d4f2-12f0-3637-9247-9aad88db86dc | -12.2493 | -63.4688 | 2024-12-02 00:20:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c9a7b8ab-c773-35df-9c44-357e2748e089 | -10.6674 | -44.4835 | 2024-12-02 00:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| dee18d0f-c5df-30a9-bbae-1d11568dacdb | -2.9824 | -53.8879 | 2024-12-02 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6d8185e2-5fd0-39ce-a9e6-ec1b24d5e5a9 | -1.9171 | -46.4037 | 2024-12-02 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 521e3f97-e9ef-3977-9b10-1fb02abe2476 | -3.259 | -53.6388 | 2024-12-02 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 794c2045-0883-3372-9248-fcc24bcf8ccf | -1.9171 | -46.4258 | 2024-12-02 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 68b6a424-7fe5-314b-a4cc-ffaf3c1651f4 | -3.7522 | -54.5093 | 2024-12-02 00:20:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 08424705-66a6-36fc-9b89-7de4af6fa0c4 | -3.3848 | -49.8596 | 2024-12-02 00:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6ed1f707-2b89-3d61-8c99-e5d6f5ecf7bc | -3.4955 | -46.0871 | 2024-12-02 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e785bd03-ee68-30dc-b681-34107d9aea76 | -1.0735 | -53.4562 | 2024-12-02 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| f946e179-d688-37cf-a852-cce25919d0ef | -2.0263 | -54.3088 | 2024-12-02 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 4c432538-086b-3992-801a-49d4a6d010e8 | -3.3664 | -49.8602 | 2024-12-02 00:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6553ab28-cbd5-35c8-a292-9493dc1476f3 | -3.4201 | -50.2375 | 2024-12-02 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 8e8c1083-9c17-3b6b-a34b-1b9d39f262a8 | -2.6533 | -53.3506 | 2024-12-02 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ce524aa9-b056-3b10-885e-4e65c0713354 | -6.0674 | -48.0569 | 2024-12-02 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 13d7a714-1aa4-3c0e-8bc5-f91967fc99f0 | -2.5428 | -53.4137 | 2024-12-02 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 12b91e47-3879-3e83-9154-ec3a06df0477 | -2.9871 | -52.5086 | 2024-12-02 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 93847037-a054-3643-89e4-52395613a160 | -4.5745 | -43.3483 | 2024-12-02 00:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3a6df988-7320-3c87-a4b7-aaac4680b5f6 | -5.118 | -43.2198 | 2024-12-02 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f72b51ef-d5bb-301c-9915-f94a460e1b1b | -3.2774 | -53.6383 | 2024-12-02 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| adf7a733-0c53-3aaf-8699-012cfd60f6e4 | -3.2184 | -45.7637 | 2024-12-02 00:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a68cdcd9-44f6-38f7-ae7e-6ccbc91a6dae | -2.5612 | -53.3931 | 2024-12-02 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| ab411ac3-7c11-3c8e-97bf-d95b6dc1700c | -2.5612 | -53.4133 | 2024-12-02 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| a713792c-6c88-3ad1-91ad-ac06fadffd6b | -2.8196 | -53.0629 | 2024-12-02 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 794a9041-fd2d-397a-984c-f9c66a81e7b4 | -4.5743 | -43.3716 | 2024-12-02 00:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 5db55b6a-f897-3fbc-aabf-ad7907fcdb9e | -1.8986 | -46.4041 | 2024-12-02 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 8b27cba2-5aef-3e6b-aadc-8be835058d2a | -6.086 | -48.0557 | 2024-12-02 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 277.6 |
| 7fec38aa-4794-354b-9ff4-59e8b6151ff2 | -6.0862 | -48.0339 | 2024-12-02 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 135.2 |
| d2cdfd40-7709-3588-be84-75500a750afb | 3.3841 | -60.5135 | 2024-12-02 00:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b9fb60e2-2989-36b3-8e65-a8c41366e444 | -2.008 | -54.3091 | 2024-12-02 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 081eab77-d0a8-3d12-bdc9-d29ada2d22fd | -2.6349 | -53.351 | 2024-12-02 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| ade74cd5-3614-3990-8c85-20e8d3a88c83 | -2.8012 | -53.0633 | 2024-12-02 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1c2276b5-8835-344e-8cc2-b2f88d15ec14 | -5.1181 | -43.1964 | 2024-12-02 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| bb325c70-93d7-36b0-a3b8-f009353e1207 | -3.371 | -53.2107 | 2024-12-02 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3401ddbe-afba-3dc1-8ca7-ad67e3ecb330 | -5.1181 | -43.1964 | 2024-12-02 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 0caa0e4c-a061-3915-af79-44cc76c44bc0 | -2.8196 | -53.0629 | 2024-12-02 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 82c76483-7ab6-3845-a6b5-bcb5f70c7393 | -4.5745 | -43.3483 | 2024-12-02 00:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 7320f1f2-7e5e-3f97-a1c6-28ff944ef54f | -3.4017 | -50.2381 | 2024-12-02 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| ce10807a-d4d2-3532-9479-b6246b8437f4 | -12.4359 | -63.7264 | 2024-12-02 00:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| cbe404ba-3e74-3597-acb9-e1376f52792d | -2.5796 | -53.3927 | 2024-12-02 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 877f5cf5-9aeb-39a6-9ac4-b7d5d52c2cfa | -3.4955 | -46.0871 | 2024-12-02 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f105443e-ea5b-3a6b-b320-689ba8f3e694 | -2.8013 | -53.043 | 2024-12-02 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 46d0a83f-51f1-30a8-bbfb-ab9fc5ea5c18 | -2.6349 | -53.351 | 2024-12-02 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 58f5553d-f8a7-346c-8917-d5059488cb04 | -2.5428 | -53.3935 | 2024-12-02 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 332575ba-d1cf-3a48-9d3e-17e5826af342 | -3.7522 | -54.5093 | 2024-12-02 00:30:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 96f52a38-0bb3-3f02-b593-f2443a046786 | -5.1367 | -43.2185 | 2024-12-02 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 02734740-bed5-3757-ae81-eb0611834685 | -3.4017 | -50.2171 | 2024-12-02 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 129dd4d7-1ffe-3e90-bb19-993e122b230f | -2.9208 | -45.8417 | 2024-12-02 00:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 8a7d0dee-fcf2-3bfa-80ad-5f0a284c813d | -1.9171 | -46.4258 | 2024-12-02 00:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| c4db5b48-a780-3eb9-85be-d62064743c8f | -4.5932 | -43.3471 | 2024-12-02 00:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 918a6d19-4f77-3455-8d50-0f13cc8903e8 | -2.6348 | -53.3712 | 2024-12-02 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| b5b6bd6b-b083-392e-b9a9-800ca8c1200d | -1.9171 | -46.4037 | 2024-12-02 00:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| da969c3e-7b61-330a-bd9e-fa9294bfe6d0 | -5.118 | -43.2198 | 2024-12-02 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 7d4e796d-2098-3b6b-a46a-0520469d875d | -2.9871 | -52.5086 | 2024-12-02 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 4dc8b631-d210-3e07-b3ed-30f6f220c3e2 | -6.0674 | -48.0569 | 2024-12-02 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5f55e969-f0af-3744-b785-8ec63788b68d | -12.4171 | -63.7274 | 2024-12-02 00:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 271b4068-7f31-37ae-a117-830db1c24e15 | -2.5612 | -53.4133 | 2024-12-02 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 1d0375d6-338b-3557-9235-83e331233de3 | -3.4755 | -50.2566 | 2024-12-02 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 90356578-ed31-3c0d-8a66-d67e9220e35f | -12.4358 | -63.7455 | 2024-12-02 00:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| cf3858a9-7bd1-3d1c-82f7-453f70da9ac8 | -4.593 | -43.3704 | 2024-12-02 00:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 3694a316-a96a-374f-9794-3d144d3bfdbf | -12.4169 | -63.7465 | 2024-12-02 00:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 80.6 |
| d2770a2e-e301-32e2-b4df-6e8158605032 | -2.5428 | -53.4137 | 2024-12-02 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1362bdb6-572b-3bb4-97db-87bdcdd708e6 | -5.1369 | -43.1951 | 2024-12-02 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| d7e8d932-3412-33a6-90ae-a6062dcc12bc | 3.3841 | -60.5135 | 2024-12-02 00:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c6734f9a-84a8-3f44-b135-a447a9bb8e95 | -3.2591 | -53.6186 | 2024-12-02 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 0858f110-052e-3c68-8944-197e5c5a2c9f | -2.8197 | -53.0425 | 2024-12-02 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 119d184c-b549-39a7-ad50-a4d08f6cbc8b | -3.259 | -53.6388 | 2024-12-02 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 3b17f080-eb85-3924-9b56-ae65dbb3bb0c | -2.8012 | -53.0633 | 2024-12-02 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 28ccb188-2d36-3ed7-958b-36d184256f1d | -3.2775 | -53.6181 | 2024-12-02 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9aeaeb99-5dae-3805-b796-4653aff1dda9 | -6.086 | -48.0557 | 2024-12-02 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 256.6 |
| 4dd861f3-9a4c-381d-9361-e51b509875e5 | -3.3848 | -49.8596 | 2024-12-02 00:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2f13be96-f749-391b-acd5-71fbb2a59840 | -4.8174 | -48.6272 | 2024-12-02 00:30:00 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e2359080-04fd-3468-8065-8cdc60b3c543 | -4.5743 | -43.3716 | 2024-12-02 00:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 4a33f992-4e0e-31c3-99f2-376567eded87 | -2.008 | -54.3091 | 2024-12-02 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 90445898-215f-35c5-b5a3-17de3a5c44f9 | -12.2493 | -63.4688 | 2024-12-02 00:30:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 7a351aa0-4d7e-3d0d-b3ee-cfbaa4b97a92 | -2.0263 | -54.3088 | 2024-12-02 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 866046a0-da95-3c39-9e33-22e739402e86 | -2.5612 | -53.3931 | 2024-12-02 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |


[Clique aqui para ver as próximas entradas](README6.md)
