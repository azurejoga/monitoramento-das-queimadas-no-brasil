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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82d2d60a-dc1a-3687-bcf5-cba15a87fc30 | -3.1504 | -54.472599 | 2024-11-03 01:09:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3583ce9-39d5-30a7-b0ca-1034f5db6479 | -3.0635 | -54.1385 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df564a59-a74c-3c30-bc52-711b57d203fd | -3.0655 | -54.147301 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f23b84df-3cb3-343a-ad5d-38fa3d16ff6c | -3.0675 | -54.156101 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5634c32-4b9d-39c4-a2eb-27886d2eecf2 | -3.0696 | -54.164902 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b31406c-d5f1-3731-8852-62bf57ea62f0 | -3.0976 | -54.2869 | 2024-11-03 01:09:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cca3cf62-146f-3f72-9fd3-193c5d5b6ddf | -3.0537 | -54.140701 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd594996-13c6-3d94-892b-c00fcef1da0f | -3.0557 | -54.149502 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9be24163-4530-341c-999b-251a3fc48d31 | -3.0577 | -54.158298 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5b806fe-3659-332e-b8f6-75331f166a94 | -3.0598 | -54.167099 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1c57f00-f0b0-3a68-a1b5-ecc8a81dd190 | -3.0439 | -54.142899 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 713dc414-e380-3bae-a9b5-842f7d5370f7 | -3.0459 | -54.151699 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a8573fd-01ce-3feb-9b8d-dfcae0818002 | -2.8502 | -53.345501 | 2024-11-03 01:09:23 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9338b008-c559-3b98-a9f0-f99e8c006492 | -3.1074 | -54.4646 | 2024-11-03 01:09:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 596f4e36-d029-3c40-8ff1-2904ee9a97f7 | -3.1094 | -54.473099 | 2024-11-03 01:09:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec6b3418-f466-3bdb-ab99-bd519ef83bd3 | -3.0121 | -54.094299 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44321035-1e46-35d7-8a84-d50673b43786 | -3.0142 | -54.103199 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac96c87-3a3a-38b9-8f45-910b79b97d57 | -3.0344 | -54.191299 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a522c93-a459-3f66-af20-6bf745371ad6 | -3.0364 | -54.200001 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34e948c2-044b-3fed-98ab-f107ddd99a43 | -3.0384 | -54.208801 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91f93917-d12c-3175-ba58-881cde53d683 | -3.0996 | -54.4753 | 2024-11-03 01:09:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e440ac7b-913e-357b-a691-ec1bd0c0c8c3 | -3.2069 | -54.943901 | 2024-11-03 01:09:23 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a78a4ff-82f7-3a6d-8835-6a65ae112634 | -3.2087 | -54.9519 | 2024-11-03 01:09:23 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf255c7-ee8f-3927-aa5d-a0c1ebe46b18 | -3.0247 | -54.1936 | 2024-11-03 01:09:24 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acb0cbb1-6443-3f05-b738-67c39dd2167c | -3.0267 | -54.202301 | 2024-11-03 01:09:24 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce22646d-8dce-37f3-b52e-2933eb9b68b5 | -2.7473 | -53.211899 | 2024-11-03 01:09:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3655d01d-1402-3507-8f5f-323e6fb09af3 | -2.7376 | -53.2141 | 2024-11-03 01:09:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad632838-241f-3578-9d53-24675f250fa7 | -3.031 | -54.490799 | 2024-11-03 01:09:25 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7f0e64e-20f4-3fe8-82c6-fa6487f14c3e | -3.0212 | -54.493 | 2024-11-03 01:09:25 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cdf1bb8-3b72-390d-b8e5-e9fe5c0b9c7b | -2.974 | -54.556801 | 2024-11-03 01:09:26 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c9012d9-b457-3c49-874e-4c1302c071de | -3.4423 | -56.929699 | 2024-11-03 01:09:27 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df4cef97-84d8-3c3e-b6a5-caf03883e418 | -2.5892 | -53.373699 | 2024-11-03 01:09:28 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69df9b77-d6fa-3edb-83e8-e5ac95eac675 | -2.5771 | -53.366001 | 2024-11-03 01:09:28 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62582a70-a46d-3a87-906b-d71644cf06c6 | -2.5794 | -53.3759 | 2024-11-03 01:09:28 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d26dc1eb-a3be-32d3-b926-09394a538206 | -2.5816 | -53.385799 | 2024-11-03 01:09:28 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9532f960-10b4-3a26-a404-d285decbc781 | -2.5696 | -53.378101 | 2024-11-03 01:09:28 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 198e18ae-55ea-3e1a-b5b4-48ca6e112f1f | -2.5719 | -53.388 | 2024-11-03 01:09:28 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3edf5ac8-f50a-3f59-942e-1797e6dfe5f3 | -2.5741 | -53.3979 | 2024-11-03 01:09:28 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70254565-9c03-3c27-9b86-16e69210fda3 | -2.5598 | -53.380299 | 2024-11-03 01:09:28 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 843339ac-d692-3a9c-8d3e-51564ad3cfeb | -2.5621 | -53.390202 | 2024-11-03 01:09:28 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77313b2a-0891-3f4c-ab38-af7fd4c20d9b | -2.7451 | -54.4119 | 2024-11-03 01:09:29 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 922e12bf-a1e0-3cfb-9be2-c9f46e508ec4 | -2.7471 | -54.420502 | 2024-11-03 01:09:29 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92dc2907-3514-30a1-b340-3a0526b6097d | -2.7491 | -54.4291 | 2024-11-03 01:09:29 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8389989f-e272-33bf-ad71-7c59c5cd6725 | -2.751 | -54.437599 | 2024-11-03 01:09:29 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b24272-99d6-36b1-a8b4-8a4e89625ac7 | -2.7373 | -54.422798 | 2024-11-03 01:09:29 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c30c53f8-a142-3ab8-b6a8-3e983f4decee | -2.7393 | -54.431301 | 2024-11-03 01:09:29 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac898894-917b-3a16-a7b5-d9afb3ca1f71 | -2.5934 | -54.019402 | 2024-11-03 01:09:30 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05de6cad-ca8b-374b-ae3e-0cce1c519649 | -2.548 | -54.000999 | 2024-11-03 01:09:31 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76a660c0-96cc-30e7-ba5a-243d1713f940 | -2.5121 | -54.113701 | 2024-11-03 01:09:32 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64ece96d-dc62-35e6-8416-2743fe974c7b | -2.5141 | -54.122601 | 2024-11-03 01:09:32 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2d45367-b889-3d91-86ac-51d2526f7500 | -2.4795 | -54.016499 | 2024-11-03 01:09:32 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04b20fd6-f9b7-3afa-9a89-968afd0f6f70 | -2.4682 | -54.057201 | 2024-11-03 01:09:32 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b6e5547-eb4a-3c1c-998b-2f0ee9c55ace | -2.9524 | -56.768799 | 2024-11-03 01:09:34 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03df160f-a5b2-3ad9-95e0-0ae779cf3336 | -1.879 | -52.120998 | 2024-11-03 01:09:34 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11707c19-f31c-36b7-84c5-7d1bf741ee47 | -1.8818 | -52.133099 | 2024-11-03 01:09:34 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c97b4de-4d99-343a-a376-51a45195468a | -2.172 | -53.663101 | 2024-11-03 01:09:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 641b71e5-cfbc-3c3f-b693-429fc5be970b | -2.1742 | -53.672699 | 2024-11-03 01:09:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9174fc4-a492-361a-953f-ae9a58420ff8 | -2.1764 | -53.682301 | 2024-11-03 01:09:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da7411d2-1c89-3e3d-87d2-ec37a10a2934 | -2.1786 | -53.691898 | 2024-11-03 01:09:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8e7f78a-af0d-38c4-a8c8-8ae749e0d9a0 | -2.1644 | -53.674999 | 2024-11-03 01:09:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e061969d-3f60-31ce-951b-82010048e6d5 | -2.1666 | -53.684601 | 2024-11-03 01:09:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67a88461-6fa9-3089-973c-da03badd83b5 | -2.1688 | -53.694199 | 2024-11-03 01:09:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef24febc-c875-38d5-8210-be243ff63d44 | -2.1754 | -53.722801 | 2024-11-03 01:09:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 987a1b12-bbd3-3b67-acbb-ba7e85b6135d | -1.5654 | -52.1409 | 2024-11-03 01:09:40 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66f31f67-cc6f-326a-a140-c0c460d40f92 | -1.5682 | -52.153198 | 2024-11-03 01:09:40 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccd6f817-a800-3ce7-9358-9fe88fd49c2f | -1.571 | -52.165401 | 2024-11-03 01:09:40 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c71a9cf3-a6af-3b39-acd7-48ee7ce35bcf | -1.5242 | -52.006901 | 2024-11-03 01:09:40 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd8aa333-b165-312d-8a3e-a958c8f6837f | -2.8232 | -57.701199 | 2024-11-03 01:09:40 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 353814ae-ab19-3c83-a415-a2139488c121 | -2.8248 | -57.708 | 2024-11-03 01:09:40 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77b7c2c3-ea6c-3a2d-a372-1bc324a4fdea | -2.8263 | -57.714802 | 2024-11-03 01:09:40 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97c47227-9a95-3cad-836a-8f069492528a | -2.6933 | -57.400101 | 2024-11-03 01:09:41 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d3e8917-362b-3663-bc29-e78ae02af054 | -2.6949 | -57.406898 | 2024-11-03 01:09:41 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e23bae3f-39ee-3c9d-8e76-0e0fc7ef1075 | -2.59 | -56.988602 | 2024-11-03 01:09:41 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e678897-45df-3db6-a8f0-3a6c7e66042c | -2.5916 | -56.995602 | 2024-11-03 01:09:41 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69d98442-198f-3592-ba73-b0ae8c82c7b9 | -2.5931 | -57.002499 | 2024-11-03 01:09:41 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b698774e-9dc7-38e0-a0c8-1338b76bc841 | -2.7601 | -57.7868 | 2024-11-03 01:09:41 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 733d378c-1e3f-3229-84e7-05d3df725b49 | -2.6173 | -57.2005 | 2024-11-03 01:09:41 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e118e096-67ea-317b-982a-42d2ce6487b9 | -2.566 | -57.1105 | 2024-11-03 01:09:42 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e04b1c0-fa5f-3e74-99eb-daafacb40524 | -2.5675 | -57.117401 | 2024-11-03 01:09:42 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3dd55287-ceb5-3941-bdc2-fd8d5853f236 | -2.636 | -57.419998 | 2024-11-03 01:09:42 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4cd4e6dc-d1a5-3fb4-a183-a5c650a8c997 | -1.4022 | -52.1908 | 2024-11-03 01:09:42 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 777da193-c22f-3587-a0e5-25f3627ab077 | -1.4051 | -52.202999 | 2024-11-03 01:09:42 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ef72490-44df-3ca0-ac60-13a23346ff32 | -1.8716 | -54.689701 | 2024-11-03 01:09:44 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4788cc8-d71a-35ac-a0ec-c404f87b2926 | -1.8618 | -54.691898 | 2024-11-03 01:09:44 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcb09811-0ed0-32aa-a879-645e223cf1b3 | -2.0152 | -55.863201 | 2024-11-03 01:09:46 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67ed7c56-285a-309e-91ef-5b8d620cd9f4 | -2.0169 | -55.870701 | 2024-11-03 01:09:46 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e87bb00-8f9c-3867-86d3-964d8e15c9c1 | -2.0396 | -56.061298 | 2024-11-03 01:09:46 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f8098c0-7333-3433-9d1a-7025962e9fd4 | -2.0413 | -56.068699 | 2024-11-03 01:09:46 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79f5a3bd-2e89-3c3d-ac9a-087bf3a3a022 | -2.043 | -56.076099 | 2024-11-03 01:09:46 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb70b744-d062-35b9-a3ca-6b6b8957468b | -1.5651 | -54.203499 | 2024-11-03 01:09:47 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c60eafdc-6b4f-3dc4-ad9e-bd06e1f3aa71 | -1.5553 | -54.2057 | 2024-11-03 01:09:47 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 548bde77-3910-3374-93d7-471509994e70 | -1.3651 | -53.5984 | 2024-11-03 01:09:48 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9732054-574b-332a-bcec-7ceccf10b0cd | -1.5152 | -54.300499 | 2024-11-03 01:09:48 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2348504e-e43c-3e16-851e-7c669f9bd649 | -1.2677 | -53.397099 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66231d71-00f5-3c44-87dd-739c15b8d9ae | -1.5013 | -54.284599 | 2024-11-03 01:09:49 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a43a83d6-5a47-309a-8530-27d114dd0af5 | -1.3013 | -53.454102 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d31fae47-06af-3e53-a71a-c5c5c807c958 | -1.2705 | -53.364101 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 237f6967-24dd-333d-b10c-0a493c04bf9f | -1.2728 | -53.374401 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a8e0700-44c7-3b94-866f-8665b7aea536 | -1.2752 | -53.384701 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbda4c19-77c7-3a05-b16d-d6aefe1d8fe5 | -1.2775 | -53.394901 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
