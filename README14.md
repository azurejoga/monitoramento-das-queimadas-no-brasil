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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 190399df-641b-30ca-85e8-c04c7e4aef50 | -2.7561 | -45.2646 | 2024-12-04 01:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e1181d0a-35f8-30c6-8590-18d9ef54d76a | -2.6428 | -45.7394 | 2024-12-04 01:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 73a9e3cc-bacc-3326-b980-f552ce94d20d | -1.7544 | -52.6363 | 2024-12-04 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| ae1e98d5-103f-3bf7-8256-e534a28b6b86 | -6.086 | -48.0557 | 2024-12-04 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 582eec9d-2766-3bc6-81ec-23999b670e30 | -2.8197 | -53.0425 | 2024-12-04 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 0938074d-419e-30dd-9c56-fc733ac7c268 | -1.6241 | -53.5308 | 2024-12-04 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| f460e336-81ed-3508-9180-266c0edf6d36 | -2.2111 | -47.2321 | 2024-12-04 01:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| cc65ec8e-fcfe-3de4-91b3-1a849f2f1de1 | -3.259 | -53.6388 | 2024-12-04 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 5be5b4f9-220b-376e-97e2-54022cd9bbd3 | -2.8975 | -51.8133 | 2024-12-04 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1620eb87-2a17-3ee8-a39d-3b54687c9c79 | -1.7361 | -52.6162 | 2024-12-04 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 642b30d6-1ff8-3168-bc94-11a093ee4afb | -2.6242 | -45.7399 | 2024-12-04 01:10:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 848e845a-8ad9-345d-b85c-07145f7151ba | -3.0765 | -53.2593 | 2024-12-04 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e4eb2f03-d90b-3899-9fc7-8fb7b87c0186 | -3.586 | -50.3158 | 2024-12-04 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c6e2ac79-e090-37ae-af06-189aabe0253e | -2.1925 | -47.2544 | 2024-12-04 01:10:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| a8b5a5ff-e854-36b9-bf72-078bd4b893f6 | -2.0682 | -45.4871 | 2024-12-04 01:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f2bf0901-fbc4-3f18-ae26-78433f70c6be | -2.756 | -45.2871 | 2024-12-04 01:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 7e50eddd-5cad-3280-aabb-eeedc194ace5 | -1.5087 | -46.7647 | 2024-12-04 01:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 483b849f-f72c-312e-ac5c-7a6e85f8706c | -2.8012 | -53.0633 | 2024-12-04 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6d3fde9b-1ca0-3ba9-91f0-d065047c2b3c | -1.7545 | -52.6159 | 2024-12-04 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| f736cf3d-b9f5-320e-bcfb-48fe17d89f3e | -3.0764 | -53.2796 | 2024-12-04 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d4e7611b-9247-37f4-8b95-962fa102ccb6 | -3.1969 | -50.6428 | 2024-12-04 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 55e89224-1d65-3e55-83b6-1ebacc9d62ea | -3.2021 | -45.2932 | 2024-12-04 01:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 391a1786-2c65-3c08-bd67-43b4b6f91d4f | -2.8196 | -53.0629 | 2024-12-04 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3ddc1fd8-cc7d-3a57-ac0a-60695c8322d2 | -1.6623 | -52.7599 | 2024-12-04 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9459fc42-4e39-3fde-996d-0595c562d057 | -3.5675 | -50.3164 | 2024-12-04 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| bbfa4dc2-c420-3e7c-8ea4-bbfac93991d5 | -1.7361 | -52.6366 | 2024-12-04 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f8665c58-cd80-3b39-b7aa-fcbbd965a98f | -2.9549 | -51.414398 | 2024-12-04 01:12:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55c68381-37ac-31c4-a8ee-45a54189c5f0 | -3.816 | -51.662498 | 2024-12-04 01:12:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd4d8307-0f86-37b1-b71c-4943b6881c52 | -3.6847 | -50.253899 | 2024-12-04 01:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8a90ec6-fa66-3f24-87ea-cdb7f7f21c0a | -2.9043 | -51.808701 | 2024-12-04 01:12:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e3c9e00-8e60-304f-813c-e4fa4e778842 | -3.5853 | -50.310299 | 2024-12-04 01:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45f09395-17d6-3bf9-a21c-cb0a12cc1106 | -3.7424 | -52.436199 | 2024-12-04 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66872262-299f-3635-b04b-b9fad2f16461 | -2.942 | -51.403301 | 2024-12-04 01:12:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5287deb1-8b56-363c-9ef4-9fffb2587a24 | -3.206 | -50.656601 | 2024-12-04 01:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f6de617-98c7-3ea0-8846-61a6c465a75a | -3.4396 | -54.083401 | 2024-12-04 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4525c367-66f1-301c-afc3-c3a2957851f2 | -3.5719 | -50.2971 | 2024-12-04 01:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 163477b2-0752-315e-9b85-2f08959596ec | -3.852 | -52.159901 | 2024-12-04 01:12:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d930b01-9f80-34de-8336-1221c9477cf8 | -6.0884 | -48.0359 | 2024-12-04 01:12:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5dfd8dca-234c-3879-b570-7adc57ca564a | -2.8819 | -51.800701 | 2024-12-04 01:12:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f08a2c2a-555b-38ab-a5bd-b5a8e361c95c | -3.1928 | -50.644001 | 2024-12-04 01:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c218ffde-553c-3402-9430-c2e8effd8917 | -3.4494 | -54.0812 | 2024-12-04 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c92f22f-3b4d-3b0f-8fd2-eff5d1fb4021 | -6.0787 | -48.0383 | 2024-12-04 01:12:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50c34bc2-7dca-36bf-b51c-dc9a1b9b4c84 | -2.638 | -45.738098 | 2024-12-04 01:12:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 606132c3-2c9e-343c-9466-07555326109f | -3.3236 | -53.5443 | 2024-12-04 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dfd34f1-c0a4-38c4-a2a4-c13e3beb5ae9 | -2.9517 | -51.4011 | 2024-12-04 01:12:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da397a94-8587-32cb-bfde-5651199f0051 | -2.8878 | -51.825802 | 2024-12-04 01:12:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef402c8a-c916-3c61-89cb-ae04cabf67d6 | -3.6382 | -54.315201 | 2024-12-04 01:12:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c453bdc8-96c8-3b35-86ff-69486d5cfe94 | -2.8789 | -51.787998 | 2024-12-04 01:12:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 141a1d03-ee6b-31b2-9a28-e9926a655b1a | -2.8945 | -51.811001 | 2024-12-04 01:12:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c66b1a4-0932-3a53-819b-25f890f792e8 | -3.4515 | -54.090099 | 2024-12-04 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa6049dd-0c31-3487-8690-06891b72a85e | -3.5756 | -50.312599 | 2024-12-04 01:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80b65f1c-9c3a-3e15-af59-233f4f98a582 | -3.8492 | -52.148399 | 2024-12-04 01:12:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d257338-1f13-3966-8e0b-23521fed669f | -3.5205 | -52.151299 | 2024-12-04 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40e46b5d-8a65-3095-a1ae-04af69497d74 | -2.6285 | -45.740398 | 2024-12-04 01:12:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a70b7ae3-425d-3910-bf9f-d5270da1dc51 | -6.0838 | -48.058601 | 2024-12-04 01:12:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea2d43a7-46bd-3ac2-8bd9-ee91166a5992 | -3.2025 | -50.641701 | 2024-12-04 01:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aca1236-dd28-3b9f-9104-fa09c2d34c57 | -3.5232 | -52.162998 | 2024-12-04 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00d15d4b-1c4c-3bf1-b001-5c5aea34a92c | -6.0935 | -48.056198 | 2024-12-04 01:12:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10af06c7-2649-32f1-931e-1dd6bb910bc5 | -2.9073 | -51.821301 | 2024-12-04 01:12:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c812d775-287f-3789-8f70-cb24638890a8 | -2.8848 | -51.813202 | 2024-12-04 01:12:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e788dff3-4eda-3a4e-b3ef-174da3aff3fe | -3.1989 | -50.626801 | 2024-12-04 01:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fa6b102-6142-3c53-a8c9-8110870f2da7 | -3.1111 | -54.044899 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a641bc4-b0b5-3e27-aa02-d60371f160d9 | -3.12 | -54.6134 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 232d14dd-c2d1-3a62-83e1-dfa0fe5bc50a | -3.2202 | -53.718399 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 879f6c72-0185-30bd-bb4b-2b210dd20616 | -3.0699 | -54.0448 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57a01c15-d2a5-31e9-b290-9fb9e002cd68 | 1.0487 | -59.5298 | 2024-12-04 01:15:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0cae5c24-f0ca-378b-a6e2-9fa00dee8f2a | -3.0741 | -54.062901 | 2024-12-04 01:15:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 930b6c0d-6a79-3092-a58a-7c176c6e4824 | 3.0231 | -60.501202 | 2024-12-04 01:15:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bbb71a68-322a-34a4-9284-c43dd8f17a18 | 1.1334 | -60.5079 | 2024-12-04 01:15:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6ad13864-abcb-32b2-b385-de6971b35ae4 | -2.8133 | -53.037701 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac077d37-5e75-3cd2-9e33-c93935820d1e | -2.8084 | -53.060799 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10e02877-e3ee-3c5b-ac69-6bda916037aa | -3.1181 | -54.6049 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa856f55-f302-39b0-acf0-5e62c5f58d22 | -3.1755 | -54.320499 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4c2e29f-fdb3-330c-b11f-1e034f840034 | -3.1132 | -54.054001 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a86fd376-4919-3828-8098-311491c29ffb | -3.1102 | -54.615601 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec93506c-d2ff-38f3-b3c8-df37c90bb5d6 | -1.6617 | -53.749802 | 2024-12-04 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d809e185-bf26-3091-bb9b-a8b4a2323d8b | -3.1795 | -54.337898 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 804e24ee-b072-3761-95e9-9108fc24847c | -3.0552 | -54.511799 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 344e435e-1f94-3471-b16d-82731a808a9a | -2.978 | -53.872501 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aee8f0d3-176a-31ae-b575-9bd367005553 | -3.1158 | -53.976799 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b8e4aba-c6b3-3285-9301-601ecee2359e | -2.7327 | -51.821899 | 2024-12-04 01:15:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d62559f-6dd4-3516-9f23-6b8c9ab3b8d0 | -3.2918 | -53.6721 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fe6f00c-174a-3078-8f54-86fad32fb504 | -3.0512 | -54.494598 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e36b8ef6-743e-364b-8b11-6cb999028dfe | -3.1904 | -54.516899 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1efbab-0d6e-3880-a25f-28b0bc54b272 | -3.1318 | -54.619499 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05b408bc-98c9-3f7a-9e87-5baec1ae9220 | -1.7358 | -52.611599 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb1e916c-533c-3443-a742-c600e88e3a20 | -1.6415 | -52.384499 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f81a033-714b-3c87-aae5-0cc85c6176f1 | -2.9845 | -53.900299 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75ea63ae-1acc-38c9-9352-e2f30b09cd7c | -3.2993 | -53.6604 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49af7407-2850-3dbd-9687-c2a491bda904 | -3.0875 | -53.372101 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 302db157-6771-3cb6-ae38-9ee874968576 | 1.1244 | -55.959301 | 2024-12-04 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d7bb56-4962-3a89-b85b-bc6ec41d144f | -1.6301 | -53.525398 | 2024-12-04 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5859325f-4959-3d17-8b26-c5cdc09c4837 | -1.7537 | -52.644001 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 678251de-de0d-31ae-8de4-0065eb144f27 | -3.0664 | -53.282299 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273f0dec-ad0c-3a79-bfb0-aa317c3ec705 | 1.0597 | -60.604401 | 2024-12-04 01:15:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a9367a32-103c-3d23-b43f-3b8ce894860a | -1.6203 | -53.527599 | 2024-12-04 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 493a37fd-9462-30e9-9ca4-b2138d2f4aa3 | -2.828 | -53.056301 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c53cbcd-695a-3ee4-b0c5-3a472663ea68 | 2.4221 | -60.646999 | 2024-12-04 01:15:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7c5dd56e-8e3b-3d89-8ff1-5183f5582d93 | -2.7986 | -53.063 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5992553c-2f3d-3376-8505-d5829c88db9d | -3.1179 | -53.985901 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
