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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46bc024c-9cd0-3eac-9498-9b0e8369417d | -4.11403 | -45.6006 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c279f16d-7897-335c-873d-f26073e86a6b | -3.99392 | -45.8349 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7139644-e3e1-37eb-9277-9c327e55e288 | -3.89202 | -45.66183 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bfca09e-e1e2-3996-883d-546db454bcc1 | -4.7787 | -45.11875 | 2024-10-23 03:57:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3681f98-f62d-3e6a-8575-396d0581f278 | -4.77453 | -45.11811 | 2024-10-23 03:57:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee793a20-12e9-3dfd-8bfb-362cada99908 | -4.77388 | -45.12194 | 2024-10-23 03:57:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9b3ff11-6d56-36f4-a9f0-cceb60b63313 | -4.77305 | -45.11865 | 2024-10-23 03:57:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d97c9eb-71bb-3db0-8f90-53ae49ab6901 | -4.77244 | -45.12247 | 2024-10-23 03:57:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e60f9bf8-a4ae-3a9b-ad3b-2235e38a1b98 | -4.64189 | -45.07413 | 2024-10-23 03:57:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76ed7959-04ac-31e7-b3bd-f4cec3371b81 | -4.75563 | -46.11371 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a87ab4e7-8dea-3ff1-9634-e94697702c16 | -4.66035 | -46.20086 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6103096-c2e9-37c4-91df-9d8bfc54b7c9 | -4.65584 | -46.20019 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e1766086-62c1-3e42-94c7-79db1a9eab62 | -4.63644 | -46.06881 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db8d659e-2cfe-3a33-bdd9-e3456604d883 | -4.01505 | -46.03685 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d90013a-c926-314c-95a0-6f1a8db35639 | -4.01058 | -46.03601 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da9a5c22-1a31-3d45-99b3-dbd1f489eac9 | -4.00761 | -46.0261 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9083b997-d033-3261-8b3e-bf4b3789d530 | -4.00463 | -46.01635 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53379d12-319f-3c1c-96ad-498fb9a738fd | -4.00391 | -46.02067 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afc71154-bafb-399e-a0b2-45f66e13766f | -4.00315 | -46.0252 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3b3a508-ffdd-3ab7-9dfb-57b36c74d4e2 | -4.00089 | -46.01119 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c890c85-7659-3c83-b326-c0dd4768fd91 | -4.00016 | -46.01557 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b063ba7b-72ad-3dff-ab0e-5bcd2a7724ca | -4.13482 | -45.58249 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b220269-3047-300d-a766-3f262b5ef994 | -4.13048 | -45.58178 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23a4205e-23b0-3807-bb26-17bed39eb37f | -4.12614 | -45.58104 | 2024-10-23 03:57:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f33867c9-d401-3045-8ea1-041e7a94d930 | -4.1218 | -45.5803 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09163e34-3017-324b-9205-7615773300cc | -4.00564 | -44.7534 | 2024-10-23 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9aa34b7c-f3f9-3235-a550-43c4f6e357f4 | -3.97684 | -44.74868 | 2024-10-23 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6d3aac8-6937-3fed-ae54-739fbcc2ec22 | -3.97273 | -44.74801 | 2024-10-23 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 607edd4b-b85a-3cf6-8eab-499d6e4af051 | -3.68141 | -45.40699 | 2024-10-23 03:57:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fc046d1-ad7d-3866-a28d-3f5f5edec9b2 | -5.11199 | -45.32942 | 2024-10-23 03:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d753142e-c0b1-36fa-aafc-730605306783 | -5.10481 | -45.75647 | 2024-10-23 03:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91cd2951-f9a4-3ff9-ab46-34902ad5f529 | -5.10303 | -45.75772 | 2024-10-23 03:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b3be291-f36a-3d74-bd4e-1d5b12ee8c09 | -5.08463 | -45.44176 | 2024-10-23 03:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5458e90-7b3c-3b3d-bf3a-6af7adaa6202 | -5.22079 | -45.14715 | 2024-10-23 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 251ae2b7-862c-325a-abce-e35a51a751f2 | -2.03925 | -46.97541 | 2024-10-23 03:57:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 899af315-681e-3586-83b8-05afa5dd6e3e | -2.03431 | -46.97463 | 2024-10-23 03:57:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 70f8c20c-eccf-38f8-8b5c-af76034176a4 | -1.68389 | -47.07766 | 2024-10-23 03:57:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b101bfd4-bbd8-316a-972d-326d3d22f61a | -3.54907 | -46.41063 | 2024-10-23 03:57:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93067b35-6c7a-311b-a4d1-bcd4ca245e32 | -3.31343 | -47.19255 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf9aa773-7862-3cc1-b93f-0f2daba56711 | -3.31253 | -47.19805 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f00115be-4119-379c-8a1d-a3cfb625dbf3 | -3.30852 | -47.19171 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 964a57a0-0238-3688-9730-ae2e6e08fcc0 | -3.30762 | -47.19718 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| db114af9-c499-38ec-af8f-e0d2b2e8c703 | -3.30615 | -47.02345 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 586fb847-8d79-380e-828e-14d9d913c14d | -3.30129 | -47.02264 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cedc73a8-85dc-359b-bbc7-d8b922d607c0 | -3.29952 | -47.03328 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f15a0a0d-f306-347a-a5b2-b2bf7c773113 | -3.28308 | -46.08192 | 2024-10-23 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 86db5961-bbbb-35c9-a4da-e33c76b4005a | -3.11711 | -46.65408 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f8b074f-3966-366c-8b3a-8f919d1e543b | -3.11625 | -46.6592 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a76c0fa9-c432-3060-8392-dabdb74ddd42 | -3.11595 | -46.65666 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ba618532-bd45-3e88-988b-bcf8a8626a8c | -3.05648 | -47.38207 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e4fab17-abb5-3fd1-8c3a-d2f46cf6efd1 | -2.95625 | -47.36635 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e572472-df97-39b4-baa3-ca11fb4a934f | -2.60317 | -46.12985 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6238e92b-ccba-3b50-b6ad-c2b5dd794564 | -2.6024 | -46.13459 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1281090-fc79-3325-b4e9-250c792c9e88 | -2.57772 | -46.14036 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a777ece1-8fc5-38e5-9aff-38deebda9395 | -2.5217 | -47.35506 | 2024-10-23 03:57:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a554edaf-850b-3fad-9b0d-4be11cff5e9b | -2.48371 | -46.28823 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3972df3-5e3b-3fa4-9ff9-4287273aacb8 | -2.47983 | -46.2825 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a8e320d-bc7f-34d0-816b-db1281f3967f | -2.47903 | -46.28745 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 344c88a1-8c4a-3b9d-b18c-ffcb7d2d26af | -2.37898 | -46.42556 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8826518d-80b8-3e33-b80e-096ce2c037be | -2.37829 | -46.42374 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 760692bd-e4d3-34e0-a8be-9cf61214169f | -2.37244 | -46.97737 | 2024-10-23 03:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 49df3f2f-28b8-32d0-a648-d1dde92c72aa | -2.36205 | -46.16632 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61d2e45c-5560-378c-beb2-a52f666c52e1 | -2.33531 | -46.47909 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b84a331-bf1e-31c7-bad0-87e68fcbdb4f | -2.33053 | -46.24161 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5f92a94-eb4f-368a-b945-8cc9277d6ab0 | -2.32585 | -46.24084 | 2024-10-23 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a9257a7b-faa6-31ac-9539-73f1fc23a4ce | -2.28807 | -46.44 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b24fca2-1735-3ba3-ad67-f5b9cdfe8e3c | -2.28757 | -46.43754 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62bad471-387e-3254-b5b1-9bf6a08a66e0 | -2.28332 | -46.43924 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2d8b42e-cb27-38fc-b71e-5b6f41bf9ec9 | -2.28249 | -46.44425 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7566c1f8-7e43-3424-922e-50bd9fbafad2 | -2.28203 | -46.44178 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f56214f1-7d6f-3f2d-9189-d5bd5478b498 | -2.28164 | -46.44932 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0c674bd-caea-3b87-95f0-ce6537ff8066 | -2.28123 | -46.44682 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb7f247c-81e9-33ad-aa38-131efdc42ea8 | -2.2769 | -46.44854 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cf457d1-a2e6-3ec0-adcf-8dbf7f964fc6 | -2.25696 | -46.7781 | 2024-10-23 03:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e9de924-6620-3834-80c6-5f1ba32a5a42 | -2.2521 | -46.77729 | 2024-10-23 03:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bca73f4a-c562-388f-9fbb-6e70066fd803 | -2.17965 | -46.83557 | 2024-10-23 03:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28c2d86f-336b-3173-a1f8-10335a3eeaf8 | -2.76834 | -45.97975 | 2024-10-23 03:57:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 261a226e-8029-3d01-a740-2034a18e5451 | -2.76453 | -45.97437 | 2024-10-23 03:57:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1306ba6e-a84f-3cc9-adb9-e9812dd190c7 | -2.76378 | -45.97901 | 2024-10-23 03:57:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e53413a4-34ce-3a51-a471-13bfd8bf986e | -4.69685 | -47.49391 | 2024-10-23 03:57:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ceb647c-5a69-3d62-af5e-dba457089786 | -4.60787 | -47.54206 | 2024-10-23 03:57:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3bf297b-c2dd-3daa-8d42-43109df235a6 | -4.60478 | -47.53046 | 2024-10-23 03:57:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5d055691-fe51-3b44-b1c6-6bef0b893ea8 | -4.60388 | -47.53576 | 2024-10-23 03:57:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28c4fa5a-2b1a-3c7c-bb86-2bd2441a0fed | -4.59986 | -47.52961 | 2024-10-23 03:57:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fedacfeb-51d1-3413-b9de-7675dd1198b4 | -4.59859 | -47.52822 | 2024-10-23 03:57:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c368525-e5db-3788-8c67-38df7943a67b | -4.59771 | -47.5336 | 2024-10-23 03:57:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1192872b-2a00-3141-b51b-a1df6207a506 | -4.59495 | -47.52873 | 2024-10-23 03:57:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75fddbb2-68fe-34c7-bb94-7d5996c81994 | -4.76389 | -46.62417 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7926025a-ee62-3bf1-80f9-3c3cdfd0eb9b | -4.76306 | -46.62905 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| fe2fb2d6-1e0e-30d8-b67a-ab81220a4d7b | -4.76011 | -46.61842 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0894930c-1602-33b9-bfd8-92ee5545b461 | -4.75929 | -46.62331 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 898e0119-02c4-3eba-826b-f9af3aeb79d0 | -4.75846 | -46.62817 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a54b7cc8-4e2c-3170-9141-ce581cc5d1c1 | -4.75468 | -46.62246 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5d7da005-dbd2-3d72-8346-bb6f9181ce0e | -4.75387 | -46.62727 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8916e87-8148-3f6f-b4a9-a3c5b23c9aa4 | -4.75009 | -46.62154 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2e271d65-221b-3f7b-976a-625dcb579cd0 | -2.28509 | -48.45679 | 2024-10-23 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 592f1463-dc09-3638-af48-85cac56cac54 | -4.74929 | -46.62626 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 92c60143-6279-3587-80d8-addf76276557 | -4.73908 | -46.66658 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6bd8b100-7dc2-30f9-9931-244d4f0b92ff | -4.73829 | -46.67146 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f600a9c-05b7-376f-aab1-a3a908afd67e | -4.73747 | -46.67646 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README22.md)
