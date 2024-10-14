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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa61cb68-de50-3cdc-ae1a-8509bfb64e9f | -4.6296 | -44.86789 | 2024-10-14 01:20:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c245d007-57f2-3450-b9c4-854eb8f83e00 | -4.62302 | -44.87575 | 2024-10-14 01:20:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| c48dbf47-c936-3327-a272-9a9463394a32 | -4.48554 | -50.46938 | 2024-10-14 01:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 353eb500-d273-3018-9767-7c17f2d63bd8 | -4.45879 | -55.07731 | 2024-10-14 01:20:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b93bce35-bf36-3882-8a68-f34f42cb15c7 | -4.45757 | -55.06841 | 2024-10-14 01:20:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2efa4862-ed5a-3ccc-aafc-5fc252ae1305 | -4.4369 | -50.54726 | 2024-10-14 01:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e0d4c163-e4bb-3177-a89c-385cc94a0ec2 | -4.43509 | -50.53467 | 2024-10-14 01:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 74d3a239-4f0e-33b9-85ac-ff0eb1234464 | -4.43372 | -49.72901 | 2024-10-14 01:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f2a8164c-8d52-358f-8dfd-92726e724f6c | -4.40767 | -54.98208 | 2024-10-14 01:20:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0b7ff51d-b94c-3666-a86b-31e5eddb439e | -4.40457 | -49.76297 | 2024-10-14 01:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 21993b65-aa9b-35fc-b335-c5a19ff8ddc6 | -4.36373 | -53.67004 | 2024-10-14 01:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a1dd1e5f-c083-30cd-b717-a3c5bc874d9c | -4.35567 | -55.14043 | 2024-10-14 01:20:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 997af2f6-4654-3507-86b8-4ccf4f14660e | -4.35443 | -55.13148 | 2024-10-14 01:20:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| f08f22d6-cce6-3dfa-a0a9-5068ba53726f | -4.35074 | -50.51454 | 2024-10-14 01:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 04ac0ec7-78f5-3968-b7e9-8fcf197e1e23 | -4.34893 | -50.50188 | 2024-10-14 01:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 5e28899d-5f52-391b-bd6d-7c501a8d9c8a | -4.34555 | -55.13274 | 2024-10-14 01:20:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c4ed8fd3-4c69-33e6-9741-be658982d535 | -4.34025 | -50.51608 | 2024-10-14 01:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| a880858c-5fbc-3638-9dd6-1f35b7c88382 | -4.32413 | -55.43843 | 2024-10-14 01:20:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| edad1fe8-e53f-30ea-bec6-159cefe469cd | -4.3224 | -50.46651 | 2024-10-14 01:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 3af294f0-de37-3a0c-9e18-3f4102761044 | -4.2947 | -55.43042 | 2024-10-14 01:20:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c3b373e-58ff-3dbf-87b5-86eaa5469597 | -4.25762 | -54.95482 | 2024-10-14 01:20:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 786b48ee-d47e-3b92-9137-6525d74d34f9 | -4.20992 | -45.77118 | 2024-10-14 01:20:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 28e952a8-c2b7-3817-880c-c428ced2dce1 | -4.20635 | -45.765 | 2024-10-14 01:20:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 1b3841d6-f5c7-30d3-b778-a58a27f23329 | -4.12889 | -51.11261 | 2024-10-14 01:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4a22c50f-10a6-39f8-86e4-5248faef75ea | -4.12267 | -48.27761 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 8865f19e-a6e4-3300-af00-49c6c2dc2227 | -4.12186 | -48.28371 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2945b3c1-f7c5-3626-848a-85af6ad790a3 | -4.11688 | -48.23975 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9045a3e0-2593-38c4-b270-afbb800d5799 | -4.11636 | -48.24587 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| b5b4d60f-befb-311b-9bcc-47f1834e5d78 | -4.1135 | -48.22614 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 4ed0b906-3ea9-3286-b083-d28dccbd18c9 | -4.11301 | -48.29841 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 5406553d-b5a4-329a-9374-d5fa3a25267d | -4.11005 | -48.27921 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 054aeff5-938b-3391-bc95-73f37cf72618 | -4.10922 | -48.28521 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 5b4a7cc2-5e11-3515-8964-a5ee58a62ede | -4.10427 | -48.2417 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f8aefc1b-9fa3-352e-9456-0866f104c408 | -4.07308 | -51.07892 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 34c0278b-ccdb-31a2-882d-ba7791f29122 | -4.07157 | -51.07281 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 21d9925c-fc16-3c91-8842-9a07bc1a8dbb | -4.05322 | -48.25499 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2d350f46-577a-3722-b296-1e25466b57d7 | -3.98732 | -55.73934 | 2024-10-14 01:20:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 8daf8466-c337-31b0-ae3b-3b456ef03362 | -3.98606 | -55.73023 | 2024-10-14 01:20:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3d0830a7-a63a-388b-8c36-1d2556508a07 | -3.96688 | -55.65838 | 2024-10-14 01:20:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0eb6a80a-e0b4-30ae-b643-740f14cdddda | -3.92605 | -46.42342 | 2024-10-14 01:20:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 695a1775-18d3-38af-afdf-b95cb230b423 | -3.92425 | -48.36339 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 60b8d54e-ce93-3c25-82b5-abba15ebc2b9 | -3.91172 | -48.36531 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| a7cfd84e-a0ce-3caa-ade1-b48e03c4805d | -3.90898 | -48.34679 | 2024-10-14 01:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b59a38c1-a608-31f0-ba24-f4df8af3bec5 | -3.90649 | -45.70577 | 2024-10-14 01:20:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 36e209f8-ab3f-37d9-9305-ea0e3c41f636 | -3.89567 | -45.71295 | 2024-10-14 01:20:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| b2b962c1-3a74-317f-91a1-e5f15fd459e7 | -3.87207 | -52.27068 | 2024-10-14 01:20:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 1dfa6375-c5e9-3c21-99b7-067f17736087 | -3.86549 | -52.29212 | 2024-10-14 01:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 2d4ca9c4-2e48-3923-a570-dc30b18da4e7 | -3.84985 | -46.91496 | 2024-10-14 01:20:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 32.8 |
| be1136fe-159d-34bf-8a69-e1c2ae0baaeb | -3.84573 | -46.92198 | 2024-10-14 01:20:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| ef1fd966-905b-3be4-be57-d967abf82611 | -3.81729 | -54.11646 | 2024-10-14 01:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1d0372c8-5433-3e28-a81b-37e7a475325e | -3.75132 | -51.33288 | 2024-10-14 01:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b97382af-2930-3229-8e83-dc1be533eaf0 | -3.69833 | -54.58516 | 2024-10-14 01:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4019018e-086b-35f7-8262-2ee00e3c5815 | -3.69785 | -50.11915 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0a3b8ae5-3ad8-3b55-8a03-39a2d79a9fee | -3.6971 | -54.57637 | 2024-10-14 01:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 51504215-f3df-3906-b740-1dd70940d069 | -3.62289 | -52.0156 | 2024-10-14 01:20:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 99f28cb8-da1c-34e5-a2fa-36f4047c12dc | -3.61678 | -54.13009 | 2024-10-14 01:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 88b2681c-6606-35ac-be5a-859a2de9767b | -3.51649 | -54.66793 | 2024-10-14 01:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 36311ad6-e122-38a8-a68c-d67f4e43ccbd | -3.51527 | -54.65915 | 2024-10-14 01:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 36dfcde7-21e5-33e8-bc03-23cab32b7463 | -3.48794 | -50.49838 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| f6deaf19-3ad2-368d-bfd7-62ac5ee0890b | -3.47729 | -50.49992 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| b5670ba0-b184-3832-8f7f-791dd7b706cd | -3.4611 | -51.59497 | 2024-10-14 01:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 3b1d5c4c-660d-3add-8e46-0fd94f2bc51d | -3.46102 | -50.31197 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 18ac99b0-b43a-3239-96e5-0775ba299d14 | -3.46072 | -50.60861 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dbf8ff52-4a20-3868-8155-96640f08cbfb | -3.45022 | -50.31359 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6660eb0f-5148-3d9f-ace3-572280c11eaf | -3.43509 | -52.77568 | 2024-10-14 01:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 60c636a9-ecb1-3484-8481-f3e010023b10 | -3.42588 | -52.77699 | 2024-10-14 01:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 19f50453-b38c-32aa-86fd-04af310d936d | -3.42451 | -52.76738 | 2024-10-14 01:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8877b1ee-7fb4-3e2d-aa19-9d7b0c6de462 | -3.42059 | -50.26224 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d7ce9769-c65d-37c1-9ad9-8b4ca98c9591 | -3.37165 | -50.33152 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 5d5f205f-4724-305a-8a08-f323ffb794b8 | -3.36173 | -49.94042 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f847a441-2c8a-3853-ae22-4c91611a6e66 | -3.36083 | -50.33295 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d5c87810-7791-3ba3-90cb-fff2ae58a4f3 | -3.35958 | -49.92599 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f85474c5-37e7-357b-a25d-42abbc52b6c2 | -3.35948 | -49.93261 | 2024-10-14 01:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 11e78227-6a38-3c66-89b5-376844c1f7b0 | -3.34694 | -51.65165 | 2024-10-14 01:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7f6d2040-f76c-3ca1-aa99-2be9b1bf497d | -3.34533 | -51.64052 | 2024-10-14 01:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bc04e2f4-a026-317b-9127-137056a4bd15 | -3.33728 | -49.16278 | 2024-10-14 01:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| be00b664-851c-3f32-8c8b-958be823aec6 | -3.30202 | -53.85838 | 2024-10-14 01:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ac2e48d-b41f-359c-9e25-fdaa74565b65 | -3.30077 | -53.84944 | 2024-10-14 01:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 28365f6a-096f-361f-8c27-dc75bee17c5d | -3.29187 | -53.8507 | 2024-10-14 01:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b8a26810-af0c-3941-b214-7cf5f0820030 | -3.26503 | -54.18637 | 2024-10-14 01:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 62b22a26-4427-39f4-8115-d65d10d0ba01 | -3.22214 | -48.92462 | 2024-10-14 01:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| f31d3ba1-8afb-3b06-b553-da39362555c4 | -3.21949 | -54.85973 | 2024-10-14 01:20:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 33523606-6423-32dd-be87-88fc283d2551 | -3.21783 | -48.93183 | 2024-10-14 01:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| eb460770-1e12-3215-adc4-0e640df29cfa | -18.2321 | -56.613602 | 2024-10-14 01:20:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 967d9b6e-b356-3037-b409-ed4af1a2717d | -18.215599 | -56.586201 | 2024-10-14 01:20:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e6fcf46f-0589-3852-87d8-3232f35536d6 | -18.2173 | -56.5937 | 2024-10-14 01:20:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ab931e45-8425-315d-8d3f-ee5649411355 | -18.260401 | -56.464699 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 888b8e50-0b55-36a4-93a6-3204d1bb49a4 | -18.2621 | -56.472099 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a1138f12-1a96-39af-bef4-c62a193a8988 | -18.2638 | -56.479599 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f87720a0-ec8d-3b44-8fb0-8ffde23daf9f | -18.2386 | -56.414501 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c780dc3f-e202-3876-a82a-03ecf626c740 | -18.240299 | -56.422001 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1ee441c9-f960-3650-b41a-36e4621bbf6f | -18.2472 | -56.452099 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 507b5a7f-e9a0-3462-af1b-df1be67e5d76 | -18.248899 | -56.459599 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d7622a77-5d03-3093-842a-6b4883d40f52 | -18.250601 | -56.467098 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d5d0b29f-6b56-3299-ad04-354170b8cd17 | -18.2523 | -56.474499 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 707b47e8-2934-3ac9-a1db-91db631b4e2d | -18.254 | -56.481998 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8cc3be47-9ea9-36ec-bea3-323c7176650c | -18.255699 | -56.489498 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e4560779-487c-3e1d-b210-5dd17413a919 | -18.257401 | -56.497002 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0bbee47a-3e29-3046-a5e8-576596151fcf | -18.2591 | -56.504501 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0d8fd15f-ba15-30dc-bf01-509b37a8c854 | -18.228901 | -56.417 | 2024-10-14 01:20:40 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README21.md)
