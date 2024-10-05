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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f1c8af6-1a3e-3642-a101-88c39bbe3a26 | -10.85066 | -48.13918 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb558287-dde8-3818-ad8e-37b1445d60eb | -10.85009 | -48.14303 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 515e76b2-53a9-387e-a882-0a183825e1eb | -10.7777 | -47.99503 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f35a408-421c-37e7-b9dc-07e4d1df3d6c | -10.77714 | -47.99881 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0afab5ea-96c4-3ef0-9c18-acc00f4added | -10.7702 | -47.99763 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aefe9336-1aaf-3b43-81b7-a8e8afef8f09 | -10.76905 | -48.00541 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0377b49-822e-36b0-ac86-4448b2994b98 | -10.76614 | -48.00107 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e2ff4b0-6a4e-3608-9b85-61fe5b60e20a | -10.76556 | -48.00498 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25a27037-f111-3dd5-8d59-7ba7c85c530d | -10.74062 | -47.73177 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c154a4a2-2001-397a-a74c-f37b42b3421b | -10.73356 | -47.73085 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c14d3706-dd96-3844-8067-b1e07834183a | -10.73003 | -47.73041 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d5d1e1a-f2c8-3b7c-ab7b-161d73269dc3 | -10.72945 | -47.73436 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 214eb514-4a7b-33ac-9a3c-4e66840fcb2f | -10.72886 | -47.73831 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5691d00-4fc1-38a9-af71-78badbf99235 | -10.72829 | -47.7422 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2d974b8-797b-3ca1-b959-8ff0d7d48e25 | -10.72711 | -47.7259 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d77b8db7-c062-3cba-a3d5-ffd2c70a222e | -10.72652 | -47.72989 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad65a4b9-6a6f-3fab-83ed-a21e86df470a | -10.72594 | -47.73382 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 014f5d0b-4015-3a61-ade4-e3cecf3aa1cf | -10.72536 | -47.73774 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a8e39c5-0e6b-3dea-ad57-3fd4b94af4eb | -10.7236 | -47.72534 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ddfce9b-f147-3407-b444-a2225cdc81f5 | -10.72301 | -47.72935 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21224a61-f8c3-33e7-9753-7e50340317c5 | -10.72243 | -47.73326 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b83f8cb-954d-3181-9f48-51862d2cd738 | -10.72008 | -47.72478 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1abc68e7-8718-30e3-9c9c-f774de6bfb95 | -10.71949 | -47.72882 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05a4bb6f-cf9e-3d62-a483-b689782ecebe | -10.71891 | -47.73277 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c10722a0-6928-332d-b480-61d7107e0748 | -10.71657 | -47.72425 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98f23ba2-07f5-376d-ae9d-85eeab4b5c44 | -10.71597 | -47.72831 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80f8b1a2-bb92-3904-a9ae-b4617f281aa8 | -10.71245 | -47.72781 | 2024-10-05 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5c6b724-b453-3229-8676-0bed9dc8e920 | -10.61645 | -48.05039 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a80d3e8-ec3b-3ecd-8e6e-50921b88a93c | -10.61589 | -48.05411 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebb472c0-8094-3825-81d9-f9082e58a3e6 | -10.59849 | -48.05199 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 634be290-8d28-3617-a0ec-81e07839ece6 | -10.59793 | -48.05578 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09c7b1d1-048c-3801-9387-85fc2f2efecc | -10.59503 | -48.05149 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3920f91-d2e3-3c17-8396-53fdad01530f | -10.59157 | -48.05094 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58660de4-712d-361f-8691-e124224d663e | -10.58192 | -48.1152 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e9891e2-87be-37bd-b53d-4b923a23dce3 | -10.58135 | -48.11902 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 584c3bb0-eefb-3b85-8702-d52750099bc9 | -10.58077 | -48.12284 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b328536f-035d-3933-a4a4-1f58c0cef600 | -10.57366 | -48.02856 | 2024-10-05 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7152cc46-6ee9-3c69-a3a6-ab771f1cb88c | -10.45977 | -48.346 | 2024-10-05 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 8ec83b90-bb79-345f-afd5-cdef7ac22f5d | -10.45635 | -48.34547 | 2024-10-05 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e6e9f3d7-8191-31cc-9db2-1a407b241553 | -10.25293 | -47.71047 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f6ef83e8-e7c0-3585-843f-bacedb1863e0 | -10.25239 | -47.70695 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e7de9cb-85b8-393e-b99a-b1f28e1dc57a | -10.2518 | -47.71086 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2cd86bd-74d5-3e47-aefd-595666c44cd6 | -10.24062 | -47.7374 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee188b96-928c-32a2-b54b-7f6bee883164 | -10.23891 | -47.72504 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76b2363d-cd9c-3f15-8c25-549c63718a7f | -10.23832 | -47.72899 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b082906-199b-334a-a03b-199718496614 | -10.23772 | -47.73296 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8321d22-266a-3bff-9dd1-9dbf735d8fc6 | -10.23712 | -47.73692 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b8e9070-2f82-36e4-942e-c7302d35a30f | -10.03866 | -48.21478 | 2024-10-05 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4911bc3-302e-34d3-8444-b08ca55093aa | -10.03638 | -48.22981 | 2024-10-05 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7aa66824-11d4-36cf-b2ad-6c83d5d4384b | -10.03581 | -48.21047 | 2024-10-05 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87d50430-aefd-3b4f-b73f-58c48780e0c5 | -10.03239 | -48.20992 | 2024-10-05 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f349321-ad53-30b0-88f1-851c8ce7d6d5 | -9.93245 | -47.91858 | 2024-10-05 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c577dcb1-42ce-3620-a2ae-7b483b800c74 | -9.46072 | -48.07781 | 2024-10-05 04:38:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8cf64ff-b79b-349f-8bf9-11e504b4db6f | -11.71059 | -47.81558 | 2024-10-05 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5aef64b-4520-3e50-a4ea-7c17ef56992d | -13.18196 | -48.61829 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5ff150f-1493-3d8e-865a-920f1a67dd0d | -11.39837 | -47.89909 | 2024-10-05 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc16d987-ee23-30e5-8e6a-b91389853fd6 | -11.39719 | -47.90702 | 2024-10-05 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66d7f1d4-5331-3ef2-a4bf-4fecc9fa9d71 | -11.71592 | -47.80396 | 2024-10-05 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab647beb-c745-3263-834a-192d0414c340 | -11.71118 | -47.81155 | 2024-10-05 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af58ce0d-3780-3ce8-b5e5-62da9fe60a56 | -13.53005 | -48.60596 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ae5509a-e405-3f67-a7bc-810d6eccf1e8 | -13.5283 | -48.61784 | 2024-10-05 04:38:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3e1b96d-d050-33ae-9584-8c32521e1df8 | -13.52483 | -48.61726 | 2024-10-05 04:38:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e721f488-8d4b-30b9-a3f4-5c3eef4f420e | -13.52311 | -48.60481 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66afa0c0-d890-305e-bc30-0cddb4e2e10f | -13.52137 | -48.61665 | 2024-10-05 04:38:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3cb0833-f443-3bfd-8d2a-45c35b46f07f | -13.51158 | -48.63487 | 2024-10-05 04:38:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a46e30e0-473f-3aa6-8b3b-69091e31e462 | -13.50811 | -48.63433 | 2024-10-05 04:38:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e2a64029-e53f-3359-a19e-b2b433c6169d | -13.33782 | -49.33292 | 2024-10-05 04:38:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97748388-bccc-37ce-b23a-698a38147b3a | -13.33442 | -49.33246 | 2024-10-05 04:38:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb4934ed-8b7d-3458-9147-22b23434764b | -13.3333 | -49.31694 | 2024-10-05 04:38:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd45cc95-2f4c-378b-bb0f-b682f5770a36 | -13.33272 | -49.32074 | 2024-10-05 04:38:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f662cf6-865b-31dd-9176-3f2ebbe1181f | -13.33102 | -49.33199 | 2024-10-05 04:38:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0db19ae9-7040-3283-874a-a7f2c210f77f | -13.3299 | -49.31644 | 2024-10-05 04:38:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3564da15-cdc5-3911-88f0-84523c9acd6f | -13.30556 | -49.31688 | 2024-10-05 04:38:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b903d7e-fa2d-3ae0-bb52-369bf1aa9b91 | -13.30273 | -49.31261 | 2024-10-05 04:38:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ec8082b-4833-36d2-b446-9bc1e5a82112 | -13.21828 | -48.54037 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b07c37f8-3131-336b-9045-456c030488eb | -13.2177 | -48.54434 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4132fa4e-25af-3494-b57d-568dda4c8fe2 | -13.21494 | -48.65883 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e9078fe-1046-34be-8c9f-01add903291e | -13.21437 | -48.66269 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95dd7f08-28f2-38ed-b149-4d22ebbd7938 | -13.21014 | -48.52323 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d35c0be-7775-3cf1-9f12-0940bdb9a8d1 | -13.20956 | -48.52717 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e295e02-6a87-3523-861f-50cf2d9801a9 | -13.20859 | -48.65393 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d7301d0-44f5-3622-b2e2-e5ae47b2eb27 | -13.20665 | -48.52271 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66ae7288-a4d8-31f8-a8f6-00601cf7d8c4 | -13.20607 | -48.5267 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86d079db-a0fb-3b55-85a9-bae9854479e3 | -13.18956 | -48.6629 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9402ce18-9ae6-3734-93a8-0f39cbcf1a27 | -13.18898 | -48.66684 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc8d30cb-6e20-32a2-9b0d-ed29ac146d23 | -13.18551 | -48.66634 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eae7a528-c059-3d81-8bb7-30cd5a046e81 | -13.17849 | -48.61774 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab062129-b012-3e28-837e-d584a42721de | -13.17225 | -48.6843 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95c52ba1-3090-3d79-b831-f6ba426bac7b | -13.1688 | -48.68375 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cc24468-6c79-3bf7-9e9e-a029db875f79 | -13.16534 | -48.68319 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a87d653d-ee56-3ead-842b-430ca13da0e6 | -13.16479 | -48.68699 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 524a5181-3e27-387d-9943-70f0e232bc8d | -13.16245 | -48.67883 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8715dcc-990d-3f85-b148-a34cba36bf73 | -13.10227 | -48.19864 | 2024-10-05 04:38:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75b95e07-03da-37e6-bfc7-6f8c4874527f | -13.09934 | -48.19404 | 2024-10-05 04:38:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c801df4e-c762-3c0c-a089-6e72eccf629b | -12.72755 | -48.04522 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 97c6cd62-e512-3598-a9a9-f545f3ab2426 | -6.56507 | -48.36386 | 2024-10-05 04:38:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99030594-b1c9-3314-9909-4ed43f12fb2b | -6.26508 | -49.06659 | 2024-10-05 04:38:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d879a55-1a1c-3888-8a3d-ef8eeef2ffdd | -6.03533 | -49.23188 | 2024-10-05 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d40ac81d-996a-3f1c-90ec-7ac26cb146c1 | -6.03479 | -49.23534 | 2024-10-05 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8adcf062-718c-34bd-856b-9d8e20b61704 | -7.94858 | -48.98505 | 2024-10-05 04:38:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README101.md)
