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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31c04034-7b08-33ce-9ef6-470f225a4a0e | -10.48114 | -67.91225 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb891c4c-4508-3d2b-8ad0-ed6c2c5dc8de | -10.47563 | -68.08198 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b328145-1365-3719-b5bc-c67c9ab5313b | -10.46206 | -68.04389 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35534347-961d-3c35-9dd2-fd38fae59326 | -10.43652 | -67.92519 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 130bfd22-6bbf-3d5a-a9f4-426a51cfe0ce | -10.41529 | -67.84568 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f95fc1a2-1e0b-3ce9-9cfd-a4c15f948f64 | -10.41365 | -67.94643 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c5ce700-7e13-3de7-9e9b-4c866636dfb3 | -10.39243 | -67.88772 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40d85034-fffc-3ed3-95e6-099a182edec5 | -10.38995 | -67.9573 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cde9a20-9ec0-3d20-a3fb-7f865a8f5fb6 | -10.38729 | -68.1688 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c28172be-f02a-3c60-a948-6298314f2eab | -10.38673 | -68.17172 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfea3dae-fe4a-3f1a-9032-b4c92c9cefac | -10.38244 | -68.16917 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41ae80bb-26e4-3bf8-9fca-52cc046d9e07 | -10.38226 | -68.16793 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 149ccecc-3a0d-3591-815b-7c298f16a359 | -10.38192 | -68.1721 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a90ed8ff-63c6-3f77-af8d-d378c0aad8bd | -10.38172 | -68.17084 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c2542d4-7c53-3620-b5c0-399e379f8601 | -10.33535 | -67.97616 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e2926ef-b928-395e-8c5a-0d43ef5f58f4 | -10.33471 | -67.7487 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b36c42e-2418-371d-b2e3-265eb17c3ada | -10.33372 | -67.75419 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0e2df4c-3d98-304d-ba70-a491b7fcc3a1 | -10.3152 | -68.00183 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e336140-3bea-3101-9410-d28dd21ed501 | -10.31415 | -68.00747 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 204fe341-6ab3-3d55-b1a9-b82a74c642fc | -10.31388 | -68.00643 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b204822-f771-36d3-8f99-7b1f287afcc0 | -10.31026 | -68.00079 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b6a1f16-2cfa-3867-8b89-d792ae87669e | -10.30893 | -68.00545 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 642fc71b-a082-368c-b7a5-6821f86ae70e | -10.26612 | -68.01509 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ceb6b91-0654-3a5b-a468-82104f4e7075 | -10.26116 | -68.01415 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 806621af-cc7b-33fe-b19e-c8d28b712563 | -10.26011 | -68.0199 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efb236fa-428d-367a-ad58-e5d24666d99b | -10.16913 | -68.17614 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74b0943f-7f6f-3670-80c1-b0334c43f9a5 | -10.13654 | -68.01846 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c88e8cde-ccbe-3608-8766-feff0175ad1e | -10.13155 | -68.01755 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee6a3eff-2d81-3db0-9ca5-ff8327232bd5 | -10.12657 | -68.01663 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37d111dc-168b-3705-b48b-49a590065adc | -10.12266 | -68.00993 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75f2d19b-9db1-3143-9d0e-7d5c256b3cf1 | -10.11187 | -67.72742 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88d7c5bd-9dac-3098-a545-f87d46859606 | -10.11086 | -67.733 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2e41a7f-88de-3245-8bf2-8260f2fdd8e0 | -10.10985 | -67.73861 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16faec4d-6379-3015-bd9f-fbb3aba42d8d | -10.10597 | -67.73212 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0f57ccd4-2e34-3026-a642-764eb38904e5 | -10.10306 | -67.91796 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7db6f316-3466-3952-be50-8d90d9a5528e | -10.09889 | -67.91675 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53c5fc75-208f-30ac-adf4-99e7e6f8ad9f | -10.06668 | -68.03462 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a45d4904-257f-338d-a88b-785016257c0b | -10.0617 | -68.03364 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6a7f537-34f4-3c0a-b053-53f771583644 | -10.97767 | -68.45905 | 2024-10-03 05:16:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adb6f31c-55ca-341c-8fca-abc054b23d1f | -8.85408 | -45.51416 | 2024-10-03 05:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81ed36d7-23f2-3e3a-ae56-84b8bcc901c8 | -8.85105 | -45.51236 | 2024-10-03 05:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0824970-a395-30b4-8b29-fe413bb064ac | -8.85015 | -45.51949 | 2024-10-03 05:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40a733e0-1f0a-3a2f-b7a7-add7a919c737 | -8.84691 | -45.51327 | 2024-10-03 05:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f6b4eab-a7b4-3e07-bc49-98ae1e3f9549 | -14.19747 | -46.46581 | 2024-10-03 05:16:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 00824606-4acc-38c6-be11-25aef0e3d3cc | -14.1968 | -46.47223 | 2024-10-03 05:16:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a54d80e-f9e2-32ad-b3a8-407c29c8522d | -14.19325 | -46.46297 | 2024-10-03 05:16:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb3f4b71-6d71-3cfe-8691-fd1e429ef7e6 | -14.19263 | -46.4693 | 2024-10-03 05:16:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6c62969-9f41-36b4-80c4-b732d62ac36b | -14.192 | -46.47575 | 2024-10-03 05:16:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c688f08-7f27-38e3-b1d7-76a491d9f5ff | -14.18964 | -46.47113 | 2024-10-03 05:16:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 279b05d3-cb11-33d0-ab08-69e45dd19fc5 | -9.09949 | -46.9055 | 2024-10-03 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1903c154-cae1-3819-b991-e5d09ac4f302 | -8.60423 | -46.53093 | 2024-10-03 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52f35cf7-4303-3268-a755-0d1c98a1d98c | -8.59742 | -46.53059 | 2024-10-03 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49cd0108-29f7-38d9-b7dc-d7187eea09f2 | -8.43256 | -46.85254 | 2024-10-03 05:16:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79908f11-c110-3a7a-9599-d82727d6de1a | -13.21921 | -48.63803 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6aae7cf-8d1b-3891-bce9-49b0c85d4a05 | -8.42598 | -46.85152 | 2024-10-03 05:16:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9878e148-78de-3ff9-a225-ef86681cbfca | -10.7268 | -46.17675 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ecb779b3-2f23-394c-95f7-105187c99a14 | -10.72604 | -46.18356 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5534ff91-53c7-3d34-90a7-b14bbeee1992 | -10.72211 | -46.17752 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 06b7ea30-9dbc-3a59-804d-f2e5f173fdec | -10.10822 | -46.56952 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 124d8cf9-992b-3175-9298-72c6dbb103d4 | -10.10135 | -46.5689 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8ddfde2-9e91-3d83-bc30-dfd6b5b549d7 | -12.19476 | -46.76055 | 2024-10-03 05:16:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38f28251-593a-3bf8-9aac-d11bec34ce4b | -12.18782 | -46.75982 | 2024-10-03 05:16:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6674ba60-23dd-357a-9d1f-f0cfc698605d | -11.99974 | -47.35552 | 2024-10-03 05:16:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba8c672e-099d-3476-8b20-fb5c5017819a | -11.80185 | -47.57523 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2d51db14-e6bf-302f-ab25-c08a24e2900e | -11.80127 | -47.58022 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ddb05bf4-fd75-30f1-b23c-c91205258554 | -11.7016 | -47.69911 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c9469fd-5a74-356a-8f13-e2b09879521c | -11.70149 | -47.70187 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 844f5994-3fd1-3977-8407-e2ddd4283b54 | -11.7011 | -47.70365 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cb2abc55-a686-3d9b-896d-2a2e4484e809 | -11.70099 | -47.70613 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ed520a7-7d75-3af6-806e-757976bf1096 | -11.70065 | -47.70773 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a3e2d41d-1c11-325e-a9ff-bf2168cb6108 | -11.70053 | -47.71009 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c6a4b440-6182-33c1-b952-cef8ef988e38 | -11.6883 | -47.70155 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b8a9461d-002c-3ea6-a1fc-7b00afe47618 | -11.68691 | -47.71348 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3feca916-1600-3838-a0e9-37d5be5acb87 | -11.68644 | -47.71757 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be88254a-4175-35f3-9e38-f195fbd702f5 | -11.68191 | -47.69959 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9230abef-01ce-36f5-b5e4-9c1421521457 | -11.68136 | -47.7044 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34715184-fc66-370c-b774-cef5f83d35e5 | -11.68091 | -47.70824 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a739b614-a087-3cca-ae31-251303c03f6b | -11.68047 | -47.71205 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 11a6e999-a3b7-302e-b086-0805ebd0f4b9 | -11.67996 | -47.71646 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| be26d6a7-c6b1-3408-8022-b3bf74aba3a8 | -11.67447 | -47.70676 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0f49df82-34fd-39e5-b859-4f03464f627d | -11.67402 | -47.71069 | 2024-10-03 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| df09d726-2465-3d11-9e16-f0cb1f3e431a | -11.31889 | -46.8322 | 2024-10-03 05:16:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 97a76eb3-f187-3391-a249-852079c40ce5 | -11.31207 | -46.83117 | 2024-10-03 05:16:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1c567c3-1da9-3b63-9a92-10b2b91774c0 | -11.01327 | -46.5016 | 2024-10-03 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b43a843-8e2a-3fc5-b9b2-9fe3997526c5 | -11.01271 | -46.50306 | 2024-10-03 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 78c2cf0f-ddbb-3d3e-95f1-cb899fc201da | -15.23548 | -47.50393 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 974e1d54-0d43-3f87-a676-651bb3476d61 | -15.23494 | -47.50349 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa5ad880-55fe-3f3a-991d-d1ad8a260af7 | -15.22798 | -47.50984 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29954d80-7742-3f82-9675-f8117a6c098e | -15.22739 | -47.50946 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdd470f1-97db-3efe-949e-99e469e2b5c4 | -15.15159 | -48.08762 | 2024-10-03 05:16:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b9b52952-4b36-338d-b6e8-72c64c6c91ea | -15.14738 | -48.08627 | 2024-10-03 05:16:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 843d91fd-0c03-30ad-902b-328bb505a91e | -15.14679 | -48.09198 | 2024-10-03 05:16:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56871ecc-d631-3744-a361-ad616842a113 | -15.1462 | -48.09765 | 2024-10-03 05:16:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c2d0c3b-2cc8-3a9c-ac42-c6bbd5908c00 | -15.14443 | -48.09232 | 2024-10-03 05:16:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6125512d-626d-36f8-baa3-762a6a33c05f | -8.35691 | -47.54561 | 2024-10-03 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9669beac-d4b9-3c08-ac27-60cc83d15aad | -8.3544 | -47.54049 | 2024-10-03 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9605fd67-7d9b-3c1f-8831-2abd42777899 | -8.35378 | -47.54549 | 2024-10-03 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7499241-d6a8-3d6e-9e11-b5be9026afc8 | -8.35123 | -47.53992 | 2024-10-03 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86e70d38-4eaa-3e9a-9072-f116c6f1215b | -8.35058 | -47.5449 | 2024-10-03 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f67ca7f9-4cdb-36e6-bb1a-5c6420276b5d | -9.89207 | -47.76194 | 2024-10-03 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README158.md)
