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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebe29ae0-fbbb-3f93-89d7-76f57802faf2 | -3.6124 | -54.3074 | 2024-12-10 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cce1481-f14e-3574-9ca7-b9bccf656b92 | -7.6074 | -46.642399 | 2024-12-10 00:51:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 479b4d8b-2159-3122-9b33-d9c808b3a5de | -3.8411 | -50.658298 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1591de26-486d-357c-8f8e-c8232519f4ce | -11.5434 | -56.437801 | 2024-12-10 00:51:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c496f8b-0c7b-3dfe-a274-6194c1f45839 | -2.8346 | -53.061501 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ec62807-9b34-3bd6-86f7-49d15d348940 | -4.5619 | -48.915199 | 2024-12-10 00:51:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dcb187e-2a21-3d07-9ac5-4e7744bf3821 | -2.9884 | -53.0126 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3cd5722-cf49-33a0-acd0-bfd615578694 | -4.6766 | -49.497002 | 2024-12-10 00:51:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2716132-4116-388c-a44a-72fc1756005f | -2.9948 | -53.0406 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9e32d26-17d8-3e1b-9f97-6c4dcccd4ddc | -13.2082 | -56.886101 | 2024-12-10 00:51:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1de2b27-bdb9-3ade-b53b-1eb720f295c3 | -1.6971 | -55.665699 | 2024-12-10 00:51:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 628ddf4b-3845-324e-8526-caa46cbea9b3 | -3.1081 | -53.764599 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0ce8b1b-39d1-372a-9bbd-dc5328f88948 | -3.532 | -54.680099 | 2024-12-10 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c82dd4a0-da00-321e-876e-e303bd020751 | -12.2015 | -46.709999 | 2024-12-10 00:51:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2a26bfc-5b28-396e-aaa5-c4dc867b41f8 | -10.0351 | -53.746799 | 2024-12-10 00:51:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed544ab9-50c0-3016-81a7-a96aef22a6c8 | -3.6833 | -49.573799 | 2024-12-10 00:51:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba606aeb-1ebd-3edc-8a99-abfdf095504c | -3.0607 | -54.236198 | 2024-12-10 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d7316fd-7305-3e21-8bea-8c5405c95800 | -2.9911 | -52.844101 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7acdeda-2c0f-3a03-974c-b17ae3d58246 | -2.863 | -52.5541 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 890442fa-8e7c-359f-9bdf-cdae21162534 | -3.0837 | -54.064999 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1731c339-7641-3ecb-914d-9e04fa0ecbd2 | 2.4269 | -60.630798 | 2024-12-10 00:51:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e216ee60-c29a-3bbd-9a19-66cf14da165f | -2.9152 | -52.9631 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b2a7d89-ac95-327d-968a-06122cd3893f | -3.7823 | -50.045898 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 365a0d76-aaa1-3458-a144-cc28e7407056 | -3.5318 | -54.5882 | 2024-12-10 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbefb9ee-92ec-380d-92ec-873926889369 | -2.4725 | -47.606701 | 2024-12-10 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77330e91-6419-391e-b111-7c8e7998bfad | -3.602 | -53.127102 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b56b3a8-ed58-3903-8395-9b807921cdb8 | -4.2689 | -50.679001 | 2024-12-10 00:51:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a411293-94c4-3212-ba90-1bf4f4595790 | -3.0025 | -52.848801 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d95a1e22-1402-30cd-abe9-920cd590addb | -3.1065 | -53.757301 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97290262-24eb-35e8-9e96-bc5694b659cf | -3.0429 | -54.248199 | 2024-12-10 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e645e7ac-b9f9-3765-bf90-f68ad9ee93eb | -3.0918 | -54.055401 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 185fead4-b61b-339b-b31d-53829110988c | -13.2052 | -56.871101 | 2024-12-10 00:51:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 855e174a-5a8b-349b-970b-ded2410c9d4b | -3.53 | -54.5802 | 2024-12-10 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7061d23-a76c-35f1-a18c-446846d81aaf | -3.0291 | -54.187599 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af5d2dcf-a0bc-3df9-ae63-07b12348658e | -9.8449 | -48.152199 | 2024-12-10 00:51:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ff38ed5-32dc-3b4e-8c7b-b78f56570fe7 | -3.0509 | -54.2384 | 2024-12-10 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f193f15-8d17-3a19-bb88-0e5cf03d474b | -12.8627 | -51.923599 | 2024-12-10 00:51:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0dcc8500-e930-31cc-9495-f67ebd9f02aa | -3.0061 | -53.0453 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae84929-4ced-3aa9-a8fe-5f6347a41414 | -11.0263 | -44.929798 | 2024-12-10 00:51:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a57133d9-9619-3506-934d-ef9aff1bbef2 | -3.1161 | -54.026402 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60b29054-66d3-3b60-bae2-6481a9ab19a9 | -6.8336 | -44.380402 | 2024-12-10 00:51:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 185669e3-52a3-3fb9-9491-399338ea4f17 | -15.2601 | -53.576801 | 2024-12-10 00:51:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5be1ed8-7fea-3dca-b666-eac6173579f8 | -2.8362 | -53.068501 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07a651cd-7c68-33e0-a82e-3cbfc92ea03c | -2.452 | -53.644001 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9473f63b-87b8-374c-90fe-def28d7175a3 | -10.7568 | -54.770901 | 2024-12-10 00:51:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62834f86-38cf-3a4e-b9ae-729082621056 | -1.7088 | -52.603001 | 2024-12-10 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9342c8a7-11e7-3cfc-b958-13cd774483de | -2.4602 | -53.634602 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b281033e-9573-322a-b346-e6ebb3ef7070 | -2.8168 | -53.028801 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db92510b-68b8-3e28-b17c-e5df76e73fbe | -2.4798 | -53.630299 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23d8af2c-675d-3707-9875-e22d8295e7f5 | -3.6993 | -50.938202 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 426deae3-127b-3044-96e0-212a223302e1 | -1.7103 | -52.609798 | 2024-12-10 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeba91a9-1843-308a-bdab-d680fb3c7a92 | -10.4548 | -44.876301 | 2024-12-10 00:51:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 75d22d15-a0e3-3f9b-895b-446c91efa089 | -3.113 | -53.243 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc6ad931-7489-3e5e-a5ad-12e65794b74b | -9.8492 | -48.568298 | 2024-12-10 00:51:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbfc24c7-c0a9-33ac-9a2b-c4e94b7e6162 | -2.7536 | -54.153702 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c403f5e6-3405-3597-b361-965752910f89 | -3.1114 | -53.236 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb195c66-4694-38da-a37e-05582e39d360 | -5.7185 | -46.554001 | 2024-12-10 00:51:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d490414-7a73-3117-90ae-7af08060fc75 | -5.9261 | -48.041801 | 2024-12-10 00:51:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f08ce4ee-7d58-30de-8d8a-7966ddfc8123 | -4.6098 | -48.501202 | 2024-12-10 00:51:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a888c84-384d-3043-80a1-ad0074842974 | -3.1229 | -54.056301 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4689768-d085-374d-9e4e-eb9165b65b29 | -3.3418 | -53.251801 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 429858db-cba8-3ec8-b288-4466b5531815 | -2.8332 | -53.010502 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19372e30-3ee2-3f96-8ca7-c0e3e3e19745 | -3.8359 | -52.344501 | 2024-12-10 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82628a6e-970d-3ef4-bb10-e9bb5866d964 | -2.7912 | -53.233101 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f24be17f-e077-375e-bd04-401eedede5e2 | -3.0803 | -54.049999 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d119b07b-0de1-35e2-acf8-7f1d083fd80b | -3.3537 | -53.8027 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2854a696-1125-3a9b-9e6c-51b0bcec9632 | -4.547 | -48.012798 | 2024-12-10 00:51:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bde122c-e12c-33a3-99df-25592f6c6798 | -5.9182 | -48.052399 | 2024-12-10 00:51:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2e11cd7-ee6a-30bc-b719-764a33ca8da2 | -17.4755 | -47.023499 | 2024-12-10 00:51:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 71232b66-1469-3282-9638-c06f20238d8e | -10.0253 | -53.748901 | 2024-12-10 00:51:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfc0630c-cf9b-3664-97e6-7db0f888b35a | -17.473801 | -47.016102 | 2024-12-10 00:51:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bbcebcea-8e3e-3e81-a21a-02226545e946 | -2.9927 | -52.851002 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0d1d31b-30c3-39d0-a8ea-d8dd45d26f72 | -8.8628 | -47.665901 | 2024-12-10 00:51:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6df5d14f-51b1-3206-ba16-e3b0baa158df | -3.8225 | -51.25 | 2024-12-10 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f6834e1-ce21-369e-936a-cad9e45e5ec0 | -9.9951 | -47.955601 | 2024-12-10 00:51:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fec7b023-894c-3e24-acf0-01ec06c125ff | -2.1757 | -53.652599 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 467e10c2-a079-3ab4-8b6a-7000518f37e9 | -10.0234 | -53.740299 | 2024-12-10 00:51:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d32b26a8-6cc1-3a31-92ce-67ca6b134433 | -4.6783 | -49.504398 | 2024-12-10 00:51:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f23adfb1-3da7-337c-98c7-910a69d599e3 | -3.1084 | -54.083099 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 371d4751-3ed4-3be4-af3c-445ca8663acd | -15.3709 | -53.121498 | 2024-12-10 00:51:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be6c72df-cbdb-3d6d-8b09-6d86a023152c | -3.0046 | -53.038399 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58dfaa21-f74d-3454-b470-84d657de293e | -3.7888 | -50.9688 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29fc11c3-d4fd-31ba-8e91-6e8666a34b55 | -9.8475 | -48.561001 | 2024-12-10 00:51:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96b9e23f-1598-39cc-aa38-4f711e346099 | -3.3016 | -51.632198 | 2024-12-10 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef2ca441-d2c2-37b6-9409-8e59600596e8 | -2.7901 | -52.866901 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52f34123-3eb6-3a04-9bd6-c41c36cc2ca0 | -7.5955 | -46.635201 | 2024-12-10 00:51:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d68a5a9-a97d-3c0b-aae5-34384ce87fa9 | -2.9998 | -53.017399 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7011abee-7bdb-3269-98c4-e1ff517a4d65 | -2.8216 | -53.049702 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17855842-fc8b-3459-b021-367a55043981 | -12.3786 | -54.168598 | 2024-12-10 00:51:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54f529bc-0e48-39c5-b81c-5262468e302e | -2.8155 | -52.977901 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b453ee2e-feb0-3820-9fe0-6d577e3fe583 | -2.7928 | -53.240101 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34608ef0-9137-307e-8c04-cade07367b34 | -2.8139 | -52.971001 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9649662-ac1c-3025-bba7-b59e73cc6197 | -4.1277 | -50.4244 | 2024-12-10 00:51:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9500e897-851f-343e-95dd-83e044b54b1e | -3.3521 | -53.7953 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7949ddc9-14d3-3eae-a5dd-d22574e39ee7 | -3.8025 | -50.2225 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd381b21-11df-32ef-95c6-86b4cc122514 | -10.3641 | -47.679798 | 2024-12-10 00:51:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e66b94e5-9bde-358e-bee9-28d4093d046f | -3.5194 | -52.1777 | 2024-12-10 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a99ef807-411c-3010-ab26-b551ed3622f3 | -3.3143 | -51.507599 | 2024-12-10 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 824c6091-78ed-373a-90c2-34d55c53f9fc | -4.8338 | -47.303398 | 2024-12-10 00:51:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9ea59aa-d8ca-3ac7-aeda-7e6f7cb265ea | -3.1067 | -54.075699 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
