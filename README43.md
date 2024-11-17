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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00ba3cb6-a252-3119-b263-730a906f68dc | -2.84033 | -46.65753 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1b8246f-df7f-37a8-b662-67f79cd5dc2e | -2.99143 | -52.60534 | 2024-11-17 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c76708cb-17fe-3735-8a28-6f2ff3e041a1 | -1.82384 | -47.87051 | 2024-11-17 04:29:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42f4086d-d735-39ba-894f-924636c96c12 | -2.68645 | -46.05548 | 2024-11-17 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36e667bc-7a42-3754-9bfa-0b2a0e0858fa | -2.93091 | -48.06495 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1b6166e-5088-3c6e-bc69-e987266f246a | -2.09041 | -48.27065 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 42c7e9ca-efa6-3577-8d8c-b54a944233a4 | -2.643 | -46.83121 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9580e60-7f59-3659-9201-0fcb252fbc03 | -6.94924 | -46.39946 | 2024-11-17 04:29:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fafe2928-f2a6-3f92-82aa-6e77453a70a8 | -1.19541 | -52.0307 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7fb39e6-075b-36bc-a6d5-adf235474f11 | -2.67253 | -46.21039 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a5908ef2-d7bd-3204-9235-16b3aaa25208 | -2.65015 | -49.75358 | 2024-11-17 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8230ff20-ca37-3758-b21d-9331efd67a25 | -3.13069 | -45.88954 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d17e9f0-1f36-31ce-9c91-63b21395093a | -1.49707 | -47.39841 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e26c39b3-cde7-326e-a52f-a44d07dbaf59 | -2.35788 | -48.53348 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 159fa580-a960-3224-bbde-6a810ac11007 | -3.97774 | -46.7044 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c037ca5e-e42e-378d-aaf0-87130d24d6f5 | -3.85978 | -46.89468 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09dd9ac2-a8a1-3293-8dd1-659137c6c5ab | -3.3281 | -50.49619 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5a506c23-e47b-3f3d-b317-73cedad89049 | -1.46933 | -51.13318 | 2024-11-17 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 466c9cb3-fe95-3d4d-8158-3d2fa15ea109 | -2.93368 | -48.06898 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 20aeb7c2-c90b-3200-9b18-5b12e46c4303 | -3.81464 | -46.50877 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd81d345-600e-33c6-8b78-ff96bdfded8e | -1.94926 | -53.33532 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f343c72b-6fca-3e6e-bc0a-3f852b6a8442 | -6.37773 | -45.88162 | 2024-11-17 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81b23c45-2aed-370f-aeb8-4e0c921d6d08 | -2.16177 | -48.9086 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73bb4c11-435c-3d00-bf6e-12ad12c4cdf9 | -3.89313 | -46.48533 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b1cb603-0885-3884-ab03-729a59a71ecf | -4.11548 | -46.93141 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43604c61-7031-38c9-9f85-eaf3d6118037 | -3.14947 | -45.98304 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c7873ea-8fd5-3c7b-9996-8b6a823cc3c1 | -3.52143 | -50.24342 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c91785ab-db74-3b7c-badb-5e9c6ca4c329 | -2.09634 | -50.60838 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 266f6054-7c1e-31bf-a1d8-29a52e75ea48 | -3.81733 | -49.25827 | 2024-11-17 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f4e8e48-7467-3d3a-a57e-79561e75d0f9 | -4.03338 | -50.88463 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3d70462-378b-372e-b13e-71f36144512c | -1.90856 | -46.57514 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c12687b8-8733-3e10-8eb9-d3327f01ff2b | -5.33781 | -44.99945 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3cfa93c-11fe-3586-bd5f-3b0fd456f3e8 | -3.57645 | -50.51158 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1580dc6f-10f9-360b-90d1-d7b9c91230b9 | -5.58462 | -44.87645 | 2024-11-17 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6704a1e2-8f47-3fb4-ac76-a406e2f46f43 | -2.15467 | -50.70675 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 91fb8b58-22c0-3c5d-8030-3e52a21b662a | -3.95455 | -46.70078 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ad89bbc-d5ca-398e-b52f-9805ec6d3a20 | -3.7775 | -44.65713 | 2024-11-17 04:29:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb1e3cde-2f29-3d4c-b521-6f7b51b98d73 | -2.10921 | -50.74354 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ae19592-ca8c-31ca-812a-93ef36f5fdce | -4.00686 | -47.42892 | 2024-11-17 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d35c8827-4016-35ae-91e2-a78bbc9ba742 | -1.75894 | -45.88318 | 2024-11-17 04:29:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dce3b0b8-a19c-37f5-b917-e99a3170bd59 | -3.41812 | -46.13636 | 2024-11-17 04:29:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f5c88f0-1adb-3093-8798-48552e804c71 | -2.70378 | -49.1181 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 778aa758-ec7e-3202-8550-2b7d0612bc25 | -3.58169 | -49.88549 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37798a02-7816-3ec1-acd0-8eac9e86d70b | -2.71534 | -46.0671 | 2024-11-17 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29c89192-3b4e-333f-a7e5-6f8e4de705e9 | -2.67863 | -46.21489 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c0a7d05-2d6b-3b63-ae04-d023ababcb10 | -3.14613 | -45.98253 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 124833d0-32d2-3492-9f46-306fbcbfc30c | -3.8797 | -46.65749 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34986959-358c-3ad7-bdc8-5bfc307165a3 | -3.56594 | -50.25388 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 59a8c9a8-5e7e-3f21-bbb6-9b348d5277af | -3.39085 | -50.73371 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7304de63-baf2-3701-9e5b-aa4d5dce2956 | -3.78247 | -50.39621 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bac8582c-40ac-3f1d-bad0-4fe31054dc95 | -2.90954 | -46.86559 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68c1aa4a-5bf2-3577-b3de-5def1102e0bf | -3.89368 | -46.48186 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e753c74b-0164-3905-bc3f-4b85f3d15465 | -4.03707 | -50.88524 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 092fad48-e27a-311e-b043-28cee331697f | -5.18016 | -37.99798 | 2024-11-17 04:29:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dbd683fe-4e4e-3462-9d38-788ae33a2612 | -4.10658 | -46.90174 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8547242d-e29c-39cf-86e9-d4382bdca639 | -4.2315 | -50.67753 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd7bfa9c-1798-3efa-9d40-c4e5e1f1cc7e | -2.34924 | -47.46798 | 2024-11-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 685e0551-7517-303a-9e16-801c3bc522b7 | -2.26013 | -46.30607 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f12c25a-dc92-3bad-b00b-5c2020de2ac1 | -2.62555 | -46.18503 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c28df93-c38c-344c-a91a-2a8df4a4d588 | -2.66812 | -46.21684 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d22a76a7-ae59-344f-a82d-61cd3ae04c5c | -0.90414 | -51.74327 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3494080c-151c-36be-840c-b8a05ea29ce1 | -4.03449 | -45.47044 | 2024-11-17 04:29:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a78fc4a-22d4-334a-a97a-98b42d1d2581 | -3.21718 | -42.09194 | 2024-11-17 04:29:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2201b753-6b54-3bd2-b1a6-50a2707846b7 | -1.2033 | -51.77542 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6a18212-d962-3d3f-bb56-9d35d3f737a6 | -2.86475 | -46.7177 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b6ea2712-1745-353a-a3b3-550c08157796 | -3.78609 | -46.03763 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 540b179a-7067-3b8b-9813-030fb5d0be81 | -1.11619 | -48.35672 | 2024-11-17 04:29:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a529ecc3-7601-339b-8131-65dbc8c65436 | -3.34153 | -53.30807 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 437253be-9e2e-3a0f-8a86-932780b4347f | -2.25755 | -48.41423 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 082aec00-3239-36d6-9bf7-431afccdc7ae | -2.67697 | -46.85418 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeedb9dd-54dc-398c-8710-3b8b12536d15 | -3.58399 | -50.53453 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f81f96b-7417-3046-b56b-9621c994724d | -1.20972 | -51.78744 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ff704f-3438-32bd-80d3-44c712aeabc0 | -2.6587 | -46.21182 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e145123-b33c-396c-a844-ff99d4c82a92 | -6.48081 | -47.5107 | 2024-11-17 04:29:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec430510-afb9-34cf-a5ae-3be60c312751 | -2.14734 | -48.53412 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f3c6bb3-d587-3729-8e26-66070974aca0 | -0.93053 | -51.73577 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d59a8f41-8de0-394c-8e7e-acad852bd12b | -2.89655 | -53.05378 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82e10247-492b-36dc-ab1d-f3e8c606d18c | -2.34939 | -49.11795 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce796e38-3c0e-3e7c-9443-b4f2b2a12612 | -3.85542 | -46.66082 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| effc0186-3caa-3d2d-9b08-dee0757a0dc3 | -7.04894 | -40.41554 | 2024-11-17 04:29:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e889bc28-a843-3f91-b802-1b9da5f1996a | -3.18935 | -46.51078 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 183a84f3-203f-3752-9f3d-e08521d6d317 | -2.08377 | -50.49786 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 216f02bf-4e40-3e69-b709-711438b2e4f0 | -3.20857 | -46.47475 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d4915f0-e4d2-38ae-ad1c-60be591b1a12 | -2.92745 | -48.32458 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30bea432-4e25-35ae-a68c-1e159479e11d | -4.21293 | -50.70042 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e93de47-e073-390b-83d6-64954aa139ee | -3.57875 | -50.52054 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d7e090d1-3aa4-305e-a881-a8e26371dde2 | -1.21028 | -51.78387 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cad13a49-bfd7-30c7-805a-e6a6e44fad91 | -2.50126 | -46.39282 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d148f83d-7be4-3c81-a98c-bd655621df59 | -4.1088 | -46.90916 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 525d1048-1f0a-3206-8cfb-dc035cc10253 | -3.52796 | -50.24863 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 1037bb76-7932-31e8-8cdf-9aa9ecb3032e | -4.11211 | -46.90968 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f2855d3-889f-3c11-a77e-96a19a569909 | -2.64877 | -46.5574 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5295c021-15ab-3112-a6d7-88a772a45221 | -2.63255 | -46.83311 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c80bdb8-449a-3175-a34d-044c930fc680 | -2.67029 | -46.20292 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce1bfdd6-8022-35fb-a739-9814f22fcfe2 | -2.18932 | -49.21788 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd8fb674-64ae-38f5-9754-6ec0f54a757a | -2.51148 | -46.28464 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80e13306-f5b2-3f78-b538-3adb3b7989ef | -3.73744 | -44.53897 | 2024-11-17 04:29:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b78f928-22be-3148-a9ba-082df1b2a701 | -3.95124 | -46.70027 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c040b584-7bff-391f-9e12-a0a8aa359a79 | -2.62446 | -46.19198 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f699d01f-f881-38fa-bed9-9a94d3409257 | -2.22695 | -46.81889 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README44.md)
