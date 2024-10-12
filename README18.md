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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d53bfb3f-7678-39e7-b910-7b9ffab94f76 | -6.8196 | -60.128201 | 2024-10-12 01:19:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92dcf6c4-6e97-3cbd-966f-ac914e6b0a63 | -6.8039 | -60.103298 | 2024-10-12 01:19:52 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 308995a2-2759-3d84-8059-1738f7d7ba9e | -6.3529 | -58.173199 | 2024-10-12 01:19:52 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf8d8a8-a8ef-343f-8dc9-0e99b7af8d22 | -6.3546 | -58.1805 | 2024-10-12 01:19:52 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e730d53a-e123-3683-bc97-c0a961ba3cda | -6.5422 | -59.755699 | 2024-10-12 01:19:55 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05f81625-2409-3fb9-8d58-e94c66a8da5f | -6.5441 | -59.764301 | 2024-10-12 01:19:55 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 744e699a-b2d0-39c2-9ce0-ac580caa5be9 | -6.5491 | -60.018398 | 2024-10-12 01:19:55 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d7db67e6-81aa-3aa2-864a-360d5551e1b8 | -6.5511 | -60.027302 | 2024-10-12 01:19:55 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd4764d2-11a2-346f-a140-099f71e946ab | -3.7163 | -47.914902 | 2024-10-12 01:19:56 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b42f836-a15e-3f53-acd0-86302bad88b6 | -3.721 | -47.934502 | 2024-10-12 01:19:56 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9121aec-cfd0-3323-ac2d-7122fe20ce00 | -3.7066 | -47.917301 | 2024-10-12 01:19:56 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f58b0e9e-d0c3-326f-bc06-64f84a666772 | -3.7113 | -47.936901 | 2024-10-12 01:19:56 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f23e6fba-ab82-3a50-9b21-0d0bfa30b2d6 | -4.3909 | -50.798302 | 2024-10-12 01:19:56 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 818c1bb1-73ab-3afd-840a-e35e60c1a899 | -4.3938 | -50.810398 | 2024-10-12 01:19:56 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c60647ea-81be-3912-baba-26773983a3d1 | -4.3812 | -50.800598 | 2024-10-12 01:19:56 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2159605-7848-3cc2-8bf9-7fd4284b12f6 | -4.3841 | -50.812698 | 2024-10-12 01:19:56 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48761cba-3373-3b05-a117-f0129b435e24 | -5.9648 | -57.685799 | 2024-10-12 01:19:56 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 776739d0-476c-3797-8e11-f414a8413648 | -5.9664 | -57.692902 | 2024-10-12 01:19:56 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ddd32d1-ef56-3431-b937-dbcf14616ab8 | -4.2831 | -50.9505 | 2024-10-12 01:19:58 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b615a3dd-95d5-3c90-9e7b-bf22db4ee392 | -4.286 | -50.962299 | 2024-10-12 01:19:58 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a88bda1e-ad8b-31ac-804c-1e64bcb41d8e | -5.8522 | -57.688599 | 2024-10-12 01:19:58 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2970d640-f282-33e1-b7dd-6f369e868dbf | -5.8538 | -57.695702 | 2024-10-12 01:19:58 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 654a1f5a-c4f3-396e-bdde-58dbda202464 | -5.8554 | -57.702702 | 2024-10-12 01:19:58 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ecd4695-cc50-35ae-9984-beb2cef208af | -5.8424 | -57.6908 | 2024-10-12 01:19:58 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a8d5b00-aec0-3ed2-b65b-7d80dbef9e90 | -5.844 | -57.697899 | 2024-10-12 01:19:58 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81cee307-b770-3bb8-882e-b7eb527ac37d | -3.2334 | -46.772598 | 2024-10-12 01:19:59 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 07d2285d-c02a-308e-b930-12d31ceadf35 | -3.2238 | -46.774899 | 2024-10-12 01:19:59 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 063ae4de-f915-30ad-ad27-37a9a02b563d | -3.2297 | -46.798801 | 2024-10-12 01:19:59 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f885be12-9d3d-3d06-90ea-92a83a94278a | -5.8096 | -57.727798 | 2024-10-12 01:19:59 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9732176-d3b1-3a5a-9e1a-68d27e4b1696 | -5.2629 | -55.966 | 2024-10-12 01:20:01 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c2d67cb-389f-3888-a44d-c8a4225646c1 | -4.0337 | -50.9837 | 2024-10-12 01:20:02 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ef6a9a9-88c1-3ee4-86f5-c038d2296809 | -4.0366 | -50.995602 | 2024-10-12 01:20:02 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a512631e-46c9-35c0-9d1f-f6e073babaaf | -4.0394 | -51.0075 | 2024-10-12 01:20:02 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f853b6d9-8f89-3434-94d0-0df6570d8e16 | -3.7091 | -50.097599 | 2024-10-12 01:20:04 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4a34c70-ec59-34cb-a30f-868029ee3cc8 | -3.7124 | -50.111401 | 2024-10-12 01:20:04 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d1e9ddd-2228-31eb-97d4-d5df6d8decd4 | -3.7157 | -50.125198 | 2024-10-12 01:20:04 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae1ba813-e47d-3ca2-925f-599b056d5159 | -3.7027 | -50.113701 | 2024-10-12 01:20:04 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8b93e21-6d0a-39b7-95ba-626684e76337 | -3.706 | -50.127499 | 2024-10-12 01:20:04 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78b1c948-46d8-3501-ac78-794b3b41101c | -5.1288 | -56.234699 | 2024-10-12 01:20:05 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef5fc4e-a39a-36e5-b537-10bbab182f12 | -5.1303 | -56.2416 | 2024-10-12 01:20:05 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddf99eb0-83ba-3e94-99bd-316e938e9bdc | -5.1079 | -56.1889 | 2024-10-12 01:20:05 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 615c4f9e-e489-39af-b00d-7b42d1d9c795 | -5.1095 | -56.195801 | 2024-10-12 01:20:05 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fd7587c-282d-3e78-9620-35a2a8e8110b | -3.935 | -51.217602 | 2024-10-12 01:20:05 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 205e0cd5-84c0-35a0-a3c0-0733d7365b05 | -3.9378 | -51.229198 | 2024-10-12 01:20:05 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2463f59b-48e9-3f0a-adbf-954e43aad584 | -3.9253 | -51.219799 | 2024-10-12 01:20:05 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb0ba99b-abcc-3036-9bcf-4f67092be61a | -4.9542 | -56.013901 | 2024-10-12 01:20:07 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59956121-aad1-3e5c-b529-4c90881ef496 | -4.906 | -55.894001 | 2024-10-12 01:20:07 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cc86908-0481-3896-b9d5-eb68536f8cab | -4.9076 | -55.900902 | 2024-10-12 01:20:07 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23f578ee-73f1-3a78-8351-2ea8fbb3adc7 | -4.9092 | -55.907799 | 2024-10-12 01:20:07 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b3ce753-5ea5-3d73-835a-ff650907be4a | -4.8978 | -55.903099 | 2024-10-12 01:20:07 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a2dec99-9155-301b-a30e-1637e7bbd387 | -3.7926 | -51.311501 | 2024-10-12 01:20:08 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd1bd26d-014b-3576-8042-5c63041b1298 | -3.7953 | -51.322899 | 2024-10-12 01:20:08 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32902a7e-5e52-3aa7-ae8a-eb736b4433ed | -3.7828 | -51.313801 | 2024-10-12 01:20:08 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c748290e-b422-3254-8f4d-8b973d29598b | -3.7856 | -51.325199 | 2024-10-12 01:20:08 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c668a90-d422-3d61-9422-1501ae0e1a91 | -4.8679 | -55.997101 | 2024-10-12 01:20:08 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f5ce8bb-7c19-3614-bd59-0840298a0a00 | -4.8694 | -56.004002 | 2024-10-12 01:20:08 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8ef2b82-54c5-3087-bdc0-05d97409de41 | -3.4561 | -50.157101 | 2024-10-12 01:20:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c088fe8-70cf-3e5d-99b7-20e3e03bc376 | -3.4594 | -50.170898 | 2024-10-12 01:20:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24c56897-172a-3d20-9e9d-514f0f1c789b | -4.8568 | -56.173401 | 2024-10-12 01:20:09 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d65daf4b-0483-3668-b2ac-2f0f2119d535 | -4.8584 | -56.180199 | 2024-10-12 01:20:09 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 319c7613-a416-3239-83c7-d1c6445d09d7 | -4.8195 | -56.145599 | 2024-10-12 01:20:09 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c1597b3-3479-3b1f-823f-8c33351276d2 | -4.8211 | -56.1525 | 2024-10-12 01:20:09 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01837475-313d-39d0-9de5-7b5103c737ba | -4.8227 | -56.159401 | 2024-10-12 01:20:09 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 958538eb-395b-33af-bc8b-259e093b26ae | -4.8113 | -56.154701 | 2024-10-12 01:20:09 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8598071-3c41-3630-8fb5-73b79026c072 | -4.6995 | -55.714199 | 2024-10-12 01:20:10 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a39d690a-5728-3f76-bb21-1de503e1b632 | -4.4784 | -55.069901 | 2024-10-12 01:20:11 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c1257f-e98c-335e-b8b0-686421235fe8 | -4.4263 | -54.889999 | 2024-10-12 01:20:11 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a2808df-4ca3-3546-b3b0-36d5905b2cb6 | -4.428 | -54.8974 | 2024-10-12 01:20:11 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b396904-9a9f-3bb0-8797-6cca9a986762 | -4.654 | -56.008999 | 2024-10-12 01:20:11 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f5a382c-ecef-352d-9822-99a02d88353d | -4.6556 | -56.0159 | 2024-10-12 01:20:11 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91e020dd-0909-32ce-8fb1-3762564a6d57 | -4.3705 | -54.871799 | 2024-10-12 01:20:12 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 242ae342-bd0c-30e0-89ce-779e0fc9b56e | -4.6174 | -56.118801 | 2024-10-12 01:20:12 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff0fe1fe-b03e-33f6-982c-92abd4b70b50 | -3.4763 | -51.540401 | 2024-10-12 01:20:14 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8a19cf7-f606-3b26-a46d-dcb4b7ac0f75 | -3.4789 | -51.551498 | 2024-10-12 01:20:14 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 557616ab-977d-30d3-9348-39e9d3b8e844 | -3.4692 | -51.553799 | 2024-10-12 01:20:14 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36f8e179-e1be-3186-924c-f9d51cf0fe4d | -3.1708 | -50.339699 | 2024-10-12 01:20:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d59f5980-f441-3469-bfff-64181bc8ef13 | -3.1741 | -50.353298 | 2024-10-12 01:20:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afe9e66d-8d95-35f3-8bc7-fe04c931fa49 | -3.1773 | -50.366798 | 2024-10-12 01:20:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f08cf8e5-52bd-32ae-bbf1-d4e216c17f7d | -3.161 | -50.3419 | 2024-10-12 01:20:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c8af30e-4408-3d96-94aa-fecf2bef8c77 | -3.1643 | -50.355499 | 2024-10-12 01:20:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa0df0f-a212-3419-ad41-312ebc32b9cd | -3.1675 | -50.368999 | 2024-10-12 01:20:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 143808d2-1be9-3407-a3dd-dce84eabdb7c | -3.1546 | -50.3578 | 2024-10-12 01:20:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e396864-f4e0-3e1b-ab09-f8f91c7a2094 | -3.1578 | -50.3713 | 2024-10-12 01:20:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 632e03b3-b325-35ba-9bf7-0a582997816e | -3.2927 | -50.939201 | 2024-10-12 01:20:14 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8478be-7d98-3577-a5d4-b49574bc7cff | -3.2956 | -50.9515 | 2024-10-12 01:20:14 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| accfc1c6-44d4-3667-851e-110569d7b1f3 | -4.3451 | -55.742802 | 2024-10-12 01:20:15 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb6bb450-2138-35c3-8701-a30cfb4b3a1b | -5.3387 | -60.1171 | 2024-10-12 01:20:15 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec5140e-d281-34b3-b91d-5898747e72e3 | -5.3407 | -60.125801 | 2024-10-12 01:20:15 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d963db66-584d-370d-8340-a77187fc7829 | -2.8432 | -49.5247 | 2024-10-12 01:20:16 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e571bc8b-024f-3b65-b37f-ac33b326a42c | -5.2955 | -60.199299 | 2024-10-12 01:20:16 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09caa9c1-b8f6-35d3-9b10-46b7f201812d | -5.2974 | -60.208099 | 2024-10-12 01:20:16 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0947ca57-7fe9-33c2-8763-3f10f17c42f8 | -3.0498 | -50.565601 | 2024-10-12 01:20:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d07caf73-8f63-324f-9b05-eceadee4cd14 | -3.037 | -50.5546 | 2024-10-12 01:20:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0f48cd9-62c9-364f-95ad-5f20634d7403 | -3.0401 | -50.567799 | 2024-10-12 01:20:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd91126-4e30-3a65-90e4-62e7d09256aa | -5.2622 | -60.188301 | 2024-10-12 01:20:17 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a34d8322-4c63-310b-894f-9ae84aadc9ce | -5.1861 | -60.123402 | 2024-10-12 01:20:18 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3759e6d5-7566-3961-874c-de56993df344 | -5.188 | -60.132 | 2024-10-12 01:20:18 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7550c2e8-c043-3615-9cc2-36e8695f9249 | -5.1899 | -60.140598 | 2024-10-12 01:20:18 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 15de9a81-4a17-3605-ac34-9c4706cd2484 | -3.4908 | -52.825699 | 2024-10-12 01:20:18 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e83a608b-7778-31ac-bebc-864dd8c02779 | -3.0584 | -51.122398 | 2024-10-12 01:20:19 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
