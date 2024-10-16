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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c69390a7-7c67-38df-992a-fd7f2528fd92 | -3.2536 | -46.883099 | 2024-10-16 00:42:41 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b40f28de-5824-3879-875a-771d3ee97e88 | -3.2417 | -46.876099 | 2024-10-16 00:42:41 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 671a7b59-f181-336d-b8a3-9e0c2a70abbe | -3.2438 | -46.8853 | 2024-10-16 00:42:41 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51af9696-fe7b-3c2f-a5c1-dd39f8666865 | -3.2861 | -47.113701 | 2024-10-16 00:42:41 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ada5c56-0b1a-3b64-8618-f065fe30a734 | -3.2881 | -47.122601 | 2024-10-16 00:42:41 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c1fc06c-e97b-3361-9f32-9b53b50abe4c | -3.2763 | -47.115898 | 2024-10-16 00:42:42 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeb85fbc-ccc9-34d1-9dce-ff0c4e99ba6e | -4.1824 | -51.2355 | 2024-10-16 00:42:42 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 527c60f0-9282-3f0e-81b9-c939bf31badc | -4.1839 | -51.242401 | 2024-10-16 00:42:42 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d98d6d1-a9b5-35c4-911c-8aa823a5ac5e | -3.9202 | -50.209499 | 2024-10-16 00:42:43 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83351810-f787-303e-9780-6293b68cfdd8 | -3.9217 | -50.2164 | 2024-10-16 00:42:43 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 251f9f54-391c-33de-827e-db6b68ebe51f | -3.9104 | -50.2117 | 2024-10-16 00:42:43 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22ad1d49-5459-3806-9190-46ce711303f9 | -4.1077 | -51.086601 | 2024-10-16 00:42:43 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39f89159-1da2-3683-a81e-5e1e749f94b1 | -3.9792 | -50.699299 | 2024-10-16 00:42:43 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 568acf0f-bc1a-3841-bc0e-ea24520ac4c7 | -3.9808 | -50.7061 | 2024-10-16 00:42:43 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7a0d769-34df-3c8e-b8e8-813451340c64 | -3.9823 | -50.712898 | 2024-10-16 00:42:43 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55aaaf3d-c19c-35b7-9642-56aaace4cdb2 | -3.4415 | -49.734001 | 2024-10-16 00:42:49 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 574d0f5f-d261-3227-bc4c-cbb250d55d03 | -3.7718 | -51.333599 | 2024-10-16 00:42:49 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 225f122c-f8a5-3637-95a3-c40224625136 | -3.7733 | -51.340401 | 2024-10-16 00:42:49 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbc215e3-1fb8-3fa1-991e-92510d8c4df2 | -3.7749 | -51.347301 | 2024-10-16 00:42:49 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5013459-d6f9-3171-9772-9bf8dafbca23 | -3.2128 | -48.909199 | 2024-10-16 00:42:49 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0385a9c7-9bd7-34b2-9632-0b0020f34bd0 | -3.2145 | -48.916599 | 2024-10-16 00:42:49 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a6eff4f-efcb-30c2-9f3d-a5bb5e464e7b | -3.2162 | -48.924 | 2024-10-16 00:42:49 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc3fee0d-dbf1-320d-9360-709660f44a62 | -3.5752 | -50.552502 | 2024-10-16 00:42:49 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9af1c68e-b28f-3209-b30c-ab258e26f0bf | -3.5768 | -50.559399 | 2024-10-16 00:42:49 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d23a597f-0d7e-35b5-a61f-68d081a69707 | -3.5783 | -50.5662 | 2024-10-16 00:42:49 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acd60de2-d5d0-31cf-b5c9-a271c4304369 | -3.5798 | -50.573002 | 2024-10-16 00:42:49 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00d1a6d2-7ccf-3699-a231-19c78b8c46f9 | -2.9619 | -47.990601 | 2024-10-16 00:42:50 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1d7d717-fc75-3ec7-a19d-bd1c9949454e | -2.9638 | -47.998699 | 2024-10-16 00:42:50 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4fd7a58-bf59-3a57-8594-100ba42d6bde | -2.9656 | -48.006802 | 2024-10-16 00:42:50 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f69a8242-49ac-34ec-b7ac-03fb91f86e0f | -2.954 | -48.0009 | 2024-10-16 00:42:50 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66cf1570-da63-37b5-95df-0ae5beb28644 | -3.5823 | -50.995201 | 2024-10-16 00:42:51 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04412f56-3e45-390d-adf3-bb0cc40bd226 | -3.7504 | -51.926498 | 2024-10-16 00:42:52 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d94216b-2e4d-3c15-ba75-67540df8b909 | -3.6148 | -51.368401 | 2024-10-16 00:42:52 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e00294f6-f048-3b2d-ad81-576e194c820f | -3.6106 | -51.441299 | 2024-10-16 00:42:52 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ac9cfb7-c210-3446-839f-cc301e3427e9 | -3.5065 | -51.298801 | 2024-10-16 00:42:53 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b8baa10-45ab-32a2-8528-5357be195d73 | -3.508 | -51.305698 | 2024-10-16 00:42:53 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88ee4434-f265-3686-af4d-922ec8c90d50 | -3.5095 | -51.3125 | 2024-10-16 00:42:53 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1659f4e-2f7e-38e7-9657-a2291d64ed3a | -3.2322 | -50.1749 | 2024-10-16 00:42:54 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c38b8dfa-bc0b-348a-8b79-8b79afb8e0e9 | -3.547 | -51.570999 | 2024-10-16 00:42:54 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f6d1eda-51d8-3d61-a541-4e701f461b67 | -3.5486 | -51.577801 | 2024-10-16 00:42:54 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02ed0343-f0bf-3447-9485-0133f5720aa6 | -3.498 | -51.581799 | 2024-10-16 00:42:54 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9687a09-bb2f-3ee2-9eee-7c60554d4dc4 | -2.9689 | -49.286701 | 2024-10-16 00:42:55 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da7d576a-4f55-38fe-9515-5b5a9da6a73e | -3.4954 | -51.661999 | 2024-10-16 00:42:55 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c70a162-0ae4-3256-8f8b-d84a69efe32b | -3.2769 | -50.919701 | 2024-10-16 00:42:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93f7ba11-89b8-3714-b91b-227391c10c29 | -3.2784 | -50.926498 | 2024-10-16 00:42:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35c29215-08e4-3d19-8a68-93fa8f10ea69 | -3.28 | -50.9333 | 2024-10-16 00:42:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bfabb0f-87e1-37c8-b80e-74a0c9cc46ec | -3.2815 | -50.940102 | 2024-10-16 00:42:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77e81676-117e-3abc-8d91-be61bd463067 | -3.5021 | -52.150799 | 2024-10-16 00:42:56 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46483fd7-8f15-3c27-bea2-38359a3e5730 | -3.5037 | -52.157902 | 2024-10-16 00:42:56 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffa8ba54-f214-3781-a0bc-875b3b84f46d | -2.6999 | -48.693001 | 2024-10-16 00:42:57 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7544d0a-76ce-3fab-b1c2-fbd4c7cd4156 | -2.7016 | -48.7006 | 2024-10-16 00:42:57 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 863e47ac-bac3-38fa-80db-28394da9adcf | -2.8513 | -49.358601 | 2024-10-16 00:42:57 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e924a3f-2f05-3cd0-a8c0-f7d4b54cb8d4 | -3.0671 | -50.3563 | 2024-10-16 00:42:57 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7d5e74c-6b46-3073-8ba3-3522963f347d | -3.0687 | -50.363201 | 2024-10-16 00:42:57 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a05f2bf-dec8-3234-915b-9bf5d9a29cfa | -2.3399 | -47.252701 | 2024-10-16 00:42:57 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1c693ad-e648-39b0-b031-fbd9e083ef34 | -2.8381 | -49.527199 | 2024-10-16 00:42:58 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afb3b87c-846d-3e12-9971-7dcab551b407 | -2.385 | -47.5849 | 2024-10-16 00:42:58 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deb9174e-2438-38a5-9684-596ac20d3afd | -3.277 | -51.515099 | 2024-10-16 00:42:58 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8948409c-afcb-37d3-a430-b29e776fd714 | -2.8201 | -49.538799 | 2024-10-16 00:42:58 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf411390-5756-3eda-8648-b658d8d428b4 | -2.8217 | -49.545898 | 2024-10-16 00:42:58 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7b93ba8-44c0-3c52-8099-40d6d0e3fff5 | -3.1559 | -51.297501 | 2024-10-16 00:42:59 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aa61281-743d-3877-a70e-b30d95f0d7e9 | -2.5011 | -48.543999 | 2024-10-16 00:42:59 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13f4da52-1c20-3e72-8cd3-b38144c55c7c | -2.6117 | -49.0751 | 2024-10-16 00:43:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d032f07f-8451-35a2-8506-2848e80bcace | -2.6134 | -49.0825 | 2024-10-16 00:43:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95493222-4a38-3fc1-a6da-58966eae4d7f | -2.615 | -49.089901 | 2024-10-16 00:43:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd08da1a-9c44-3bc3-8d87-1c000d5e8a0a | -2.6086 | -49.1068 | 2024-10-16 00:43:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b12036cf-286b-3f21-8d2a-d0f44a9dd3fe | -3.059 | -51.233002 | 2024-10-16 00:43:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b339b464-9879-3523-b334-48c64060eb38 | -3.0605 | -51.239799 | 2024-10-16 00:43:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31e53cbf-269a-3ee6-a5c7-d02af0b188c9 | -2.6012 | -49.482498 | 2024-10-16 00:43:01 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 321544c9-e110-3117-bee4-a574218e1577 | -2.4954 | -49.062199 | 2024-10-16 00:43:01 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b3c4298-345e-3c8f-9c9c-ff47cb7c2c65 | -2.4971 | -49.069599 | 2024-10-16 00:43:01 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f1367f0-d340-3884-9e61-531cb01e8d68 | -3.6164 | -54.648899 | 2024-10-16 00:43:04 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c37cee2-f753-38e7-a93f-9b8b1bc7c532 | -3.6184 | -54.657799 | 2024-10-16 00:43:04 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7f2b9d-bb4a-3fb2-81ab-463a03d50f8d | -3.6204 | -54.666698 | 2024-10-16 00:43:04 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1a28c02-6a64-3127-a5ea-ca9dbaafd41c | -3.336 | -53.5257 | 2024-10-16 00:43:04 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efa394e4-195f-3da9-baf2-8510739f2c01 | -3.3377 | -53.533501 | 2024-10-16 00:43:04 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45faa8c7-0135-3944-a577-ad42ba83bac8 | -3.3394 | -53.541302 | 2024-10-16 00:43:04 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d5b46e4-4281-389e-b6bb-d94dc01f7c34 | -2.8788 | -51.668098 | 2024-10-16 00:43:05 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bde17da-1d86-3224-a3e2-39fb626685c2 | -2.8803 | -51.674999 | 2024-10-16 00:43:05 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0a72958-96af-302c-94f9-febd60a3c01b | -3.4893 | -54.4464 | 2024-10-16 00:43:05 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffe8f210-493e-3600-b786-1ee6ff1b5f10 | -3.0466 | -53.243198 | 2024-10-16 00:43:08 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e981402-020c-3f86-8463-9b1bc20e3f07 | -3.0483 | -53.250702 | 2024-10-16 00:43:08 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0e75613-af7c-357c-af2f-f63fc06533a4 | -3.1108 | -53.715 | 2024-10-16 00:43:08 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4bea528-8724-347b-8447-057dc35b87d3 | -3.1126 | -53.7229 | 2024-10-16 00:43:08 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebe5ade3-ca10-3c5a-aa6a-bdf3ae52a396 | -3.1143 | -53.730801 | 2024-10-16 00:43:08 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 817eb5ed-579e-3a4c-9401-5e193710bd6b | -3.1161 | -53.738701 | 2024-10-16 00:43:08 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaf46961-c076-399b-936f-7aee302b7144 | -3.1473 | -53.9249 | 2024-10-16 00:43:09 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e4b49de-ab59-3768-9199-b03b4569a765 | -3.1157 | -54.198502 | 2024-10-16 00:43:10 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73e9ad94-7e1b-3a07-a7f8-faf6307a04dd | -3.1176 | -54.206799 | 2024-10-16 00:43:10 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a37c86a-dbcc-3c26-90d8-afcb3536322f | -3.1195 | -54.215199 | 2024-10-16 00:43:10 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc83c351-0094-36c9-8697-8ea8023c7036 | -3.1213 | -54.223499 | 2024-10-16 00:43:10 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e92fde5-b73a-36b4-bc61-032f96394930 | -3.1232 | -54.231899 | 2024-10-16 00:43:10 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3794456b-b4ff-3198-b25c-7a6d0532e864 | -3.1325 | -54.2738 | 2024-10-16 00:43:10 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16fd3727-b679-35aa-a5d1-ffcc9f4cb5eb | -3.1344 | -54.2822 | 2024-10-16 00:43:10 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 994ba79c-c25f-35fa-a3d7-485efec1660b | -3.1059 | -54.200699 | 2024-10-16 00:43:10 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a407f27e-b636-3568-9668-60d0f9d0cbe5 | -3.1078 | -54.209 | 2024-10-16 00:43:10 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 609cf97d-ba3d-38f0-9fd7-8bf227cd44ce | -3.1097 | -54.2174 | 2024-10-16 00:43:10 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 583e6248-175c-3427-ad5f-f49502baa62e | -3.1115 | -54.2257 | 2024-10-16 00:43:10 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b61da1c1-9ae7-3ea1-a38a-c4f9bfdd15b6 | -3.1134 | -54.2341 | 2024-10-16 00:43:10 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00c7278d-b523-35a5-982a-904a6f1b3418 | -3.1208 | -54.267601 | 2024-10-16 00:43:10 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
