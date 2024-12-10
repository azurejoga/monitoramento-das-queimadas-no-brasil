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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5743c71e-9a37-3602-adbd-c0450685233c | -2.41519 | -53.67632 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5feac9bb-15d3-3976-a098-8e70f037e558 | -1.74517 | -52.8092 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c97df3c4-03ea-36e3-9e74-b17e6e12370d | -1.27131 | -52.12037 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 683f642d-9b8b-3988-b84c-9f4280deac2f | -2.99511 | -53.03973 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 021d3661-f360-3cd2-b4fa-2e16bba8d6f0 | -6.83281 | -44.38336 | 2024-12-10 04:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ebfc9b13-d6a4-3bf3-b438-5b26a2398c6e | -3.53727 | -54.59079 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebd10f46-26a3-3821-93d9-a0af343271f3 | -3.06679 | -53.79576 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87eae0e6-613a-3045-9ff8-b47b4bfbca0c | -10.89969 | -45.06327 | 2024-12-10 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a09523b5-b8eb-325d-a8bf-aaaebb44082a | -3.86399 | -54.79089 | 2024-12-10 04:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8d8e830-fe75-3844-b891-0d4135a05f4c | -2.99178 | -53.03921 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1b1d62f-bfc1-3fd9-a287-10a928d91257 | -3.52879 | -54.68814 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 55de4fbe-1b9f-35fa-96c6-8241f1d77bea | -3.85785 | -54.0794 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42d5dc00-86ad-3e0d-aa27-e0347d54f76e | -6.91641 | -43.51138 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e31027b3-df97-35ce-a98e-3c4ea78a708a | -4.1159 | -50.2136 | 2024-12-10 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3f9dfc0-bef2-3f10-bda3-82342f7193c6 | -3.87153 | -54.3474 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1b77b57-e8ee-303d-b5f4-1925cdb39257 | -5.92213 | -48.05228 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e7bec8f2-6f34-37a4-ab9e-cf08986a58da | -2.76569 | -54.05805 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b549a5a-db0d-3793-9d94-b87009a1e69b | -3.94268 | -51.04085 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38d6afe1-845e-3e91-a037-8485d53de362 | -13.10279 | -43.3155 | 2024-12-10 04:53:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 86d2fe57-90db-35e6-8a69-80cb9453192c | -3.47405 | -53.7104 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c637fa9-947e-3c48-b2c6-9f3b6d37c269 | -2.47276 | -53.69292 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1308ef0d-0bb8-3c3a-a3ca-e1f445123b18 | -7.10237 | -48.96349 | 2024-12-10 04:53:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13dd8189-e11c-360e-94f2-362e06428712 | -12.8578 | -51.93028 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2349c727-4770-34f5-8f9a-6ba3972887ee | -3.06962 | -53.79993 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3da8a858-b9e6-329b-a963-25446666cf4e | -3.11441 | -54.07352 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9427090-a56e-3e32-a519-33eb9ff586f1 | -6.9169 | -43.50785 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6900d447-1bd4-3315-9aad-a5cd6ba58d8a | -2.82012 | -53.07003 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0e917934-c98b-3f2e-a6d4-249ea19e5949 | -3.83777 | -50.65807 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73ae4dbc-e2f7-3d63-ad6c-2b9b9c408c6d | -2.79438 | -52.86573 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6b67cc5-6e0b-3bdc-9004-b219b2b91d8c | -3.11301 | -54.12675 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4d7aa8e-7baf-3cef-861c-438259306826 | -3.30406 | -42.47778 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee8416f6-e378-339d-aec5-02a3b88231e6 | -3.6297 | -52.6808 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 610b32d0-693b-346f-a250-8e08143f9630 | -2.78287 | -53.24111 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ca3b13e-85d4-3eef-bc65-df2f30e08bbe | -3.73491 | -51.9857 | 2024-12-10 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad6a9ab6-536b-3c59-82eb-6d459a9a5969 | -13.10229 | -43.3201 | 2024-12-10 04:53:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a5284c27-182f-3386-a439-e731ff5cdda0 | -1.97311 | -48.43221 | 2024-12-10 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7205528-92ff-3cba-8963-84458b4ea812 | -2.0036 | -53.28415 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4be42c25-2f03-3b01-8d01-721b0d142265 | -3.90778 | -53.4457 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f60ef0de-7da3-3adf-b87f-355b61357c9a | -3.80308 | -50.0168 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d916f903-fe8e-3ec7-bf34-6e202062b727 | -3.79963 | -50.01626 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8a26032-3197-383f-ab47-00256cc4f1a6 | -11.82685 | -57.82514 | 2024-12-10 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1591a690-6bce-3a0b-b9dd-ecf6bb4c4620 | -2.79384 | -52.86924 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e48eba9-a3d1-3217-9e57-f67c0ce4a266 | -3.20901 | -46.81485 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 380392da-2114-3a6e-b204-6edd83f4a777 | -11.41596 | -54.32567 | 2024-12-10 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c90bd45-8cf3-3aa5-b4b5-1b12f56d7ff5 | -2.96637 | -53.72058 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3f54e09-5e00-31de-9ea6-2eea06e9ef49 | -6.56239 | -46.58004 | 2024-12-10 04:53:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d21a18c7-b7da-3744-b2fc-6ce0157d08f2 | -3.08928 | -53.34689 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a17f9b14-575a-31c2-8344-fd85766b9d18 | -3.10826 | -53.24845 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3318518b-5726-3d74-bdf3-c6f56dd9b1f1 | -2.46955 | -53.63998 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7127ccb4-1051-37fe-ab2d-467516ca29d6 | -1.28517 | -48.44788 | 2024-12-10 04:53:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45d407be-6434-3a98-8b0e-bb026b55a7fd | -3.78408 | -50.0023 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12016221-82ee-3b0e-9f6a-da7e6e48de32 | -3.81953 | -52.35839 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9eab74e0-a568-37a2-b21f-46adc67e596b | -2.81511 | -53.05847 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b6b216e-81ef-35bd-8ab0-d72b8078b8d3 | -3.88992 | -53.4285 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee92b595-a609-3420-9ee1-c85f7ce278e7 | -3.00377 | -48.04137 | 2024-12-10 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af2efdd8-e66b-3820-a94e-391758e35678 | -4.3997 | -47.7668 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13cb1f50-b86d-357c-84d0-c7f7e5da1de1 | -3.94603 | -51.04137 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8389f0e-9975-3854-bf77-a02f7a95a311 | -3.68239 | -54.32121 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea8f0403-838f-304d-be47-545e34e368d4 | -3.10436 | -53.25146 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fa02bed-48bb-32ee-9fa5-d3f98a0b8ccd | -2.22573 | -53.71872 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b735a446-9646-3f7e-ac23-7bbeb205275a | -1.4081 | -52.42138 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e36d3d3a-06c8-3d0a-b9a6-b3b930843d5d | -1.33268 | -52.22877 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c96401af-76bb-3b42-9e01-db86629909b2 | -6.06657 | -47.38219 | 2024-12-10 04:53:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67e1e2c5-a62a-33a0-b291-813a6e7fe62a | -2.83457 | -53.06506 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c70eaad9-903a-330e-98a8-0fec850bb729 | -6.91146 | -43.50706 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06c72400-53de-3053-b95b-1f9961054e56 | -3.02242 | -53.87839 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6666a031-81b3-3ceb-90fc-aeb6bbf4e37d | -5.71183 | -46.54943 | 2024-12-10 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e1e0791c-56bc-3487-ae2c-759057ea57b5 | -3.31414 | -51.16802 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 420fe509-67c9-3ef5-acef-51d5d97c47f0 | -3.10548 | -53.24442 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf6b4170-1cf0-3c9c-b595-a97236d161bf | -3.17679 | -53.96621 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 890f0590-cae3-36a1-8bdf-51be86da9f28 | -3.83436 | -52.35012 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7b790ec-043e-3970-ba60-a50443c79038 | -2.81787 | -53.04094 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9f8d0933-710a-3b93-88ec-475bd5549084 | -2.99227 | -53.01426 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 19903bef-234e-32e6-ba76-2f36f67e62b1 | -3.79874 | -50.22403 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c165bf18-107d-3ccc-beb8-881dcab35305 | -9.14901 | -62.7215 | 2024-12-10 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ab1e647-bbf3-3983-a58c-cd9c89a1209e | -12.24954 | -52.45206 | 2024-12-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7389aab-aa63-35e6-be40-5ce019bf5596 | -4.54999 | -48.01852 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 227c5086-6187-3547-98b2-783a590a802e | -3.86049 | -54.79033 | 2024-12-10 04:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85daff1d-7683-3ecb-99d0-50bb8c457667 | -4.70942 | -43.79303 | 2024-12-10 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd58694d-4b95-3fb7-8211-f3ef18a6a3d3 | -3.83739 | -54.29619 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8150ec2b-3aaf-313d-b9d9-bfa758fd239e | -3.11901 | -54.06661 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a23c167-d6f9-3db5-a837-5a6bc73fd0e2 | -1.57612 | -54.92722 | 2024-12-10 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ed9faa6-b8d1-397b-bd05-2e19e8addc6f | -2.14767 | -45.6574 | 2024-12-10 04:53:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74ab725e-59a6-3afc-bc9a-71a3e3b22826 | -2.94969 | -53.11169 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 763ff315-1c51-3d9d-bc9b-9a6a1fd74238 | -3.23291 | -42.42396 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5c4fc00-abb5-3db3-a0fd-a4d4a8fe5fae | -2.45202 | -53.64101 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c65a129d-f08a-3233-81e6-c5304f7aafeb | -3.28094 | -51.07632 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2456250f-2119-3a0e-9769-1219bbd20920 | -1.64604 | -45.90817 | 2024-12-10 04:53:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a504ee9c-4fef-3cf9-b73b-9b5dd1b26f62 | -4.03934 | -50.80725 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d8fb773d-8a06-32f1-bd79-979e98777363 | -4.56868 | -48.91765 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50a55344-a081-308b-a5a6-d08dd95eb882 | -2.79292 | -53.24265 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 750e1d16-b898-3c17-95f8-48fa7e99c8ca | -2.79051 | -52.8687 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 773ad99a-7b4f-3e64-8390-ce18b59cb548 | -3.08713 | -54.04656 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c49eeefe-b586-3070-8ed7-9ecc52fb656d | -3.15613 | -54.4742 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22987ebe-7f62-3006-a772-a10b04f94180 | -3.12077 | -54.05547 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcd62819-2bf3-3612-8784-6655659052e4 | -2.8212 | -53.04145 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21c49dfa-3033-3098-b2d0-73ddfcc9320e | -3.43487 | -50.15047 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e9dd96d-fe24-3d44-99bf-4eeb04664ad5 | -4.55003 | -48.00049 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79db1473-de9f-3d3d-b12f-9f36e8e2f41e | -4.34908 | -48.46895 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20f23e1e-3ac4-3a88-a6e9-e61108d8e4e1 | -2.44863 | -53.64049 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README20.md)
