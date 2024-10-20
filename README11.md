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
| 0d21358c-3a48-30bb-8ae8-ab25ba6b141a | -2.6938 | -53.994701 | 2024-10-20 01:00:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10fea2ff-081b-3439-821b-968baca729b9 | -2.6137 | -54.323101 | 2024-10-20 01:00:38 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80f90801-917a-3aaf-b646-ce85c8696aed | -2.6153 | -54.330002 | 2024-10-20 01:00:38 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6db77ba7-ef25-3fe8-8484-bf5b7da84512 | -3.7304 | -59.308899 | 2024-10-20 01:00:38 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6ebb9bd-af67-3776-b814-01b75f326c8a | -2.6039 | -54.325199 | 2024-10-20 01:00:39 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e537413-fe55-3cb9-ac13-0db1f1661a51 | -2.6055 | -54.332199 | 2024-10-20 01:00:39 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5927e4f-5881-3a3f-af7f-09762e0f7cf1 | -2.5112 | -54.2798 | 2024-10-20 01:00:40 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 529d043b-99ff-36da-925d-0fc5243a8592 | -2.2512 | -53.724201 | 2024-10-20 01:00:42 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44a8feb2-7504-37aa-8a3b-dedfe677354b | -2.2528 | -53.731499 | 2024-10-20 01:00:42 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e9f8c52-674f-3183-bf01-06169b989ad7 | -2.1938 | -53.698898 | 2024-10-20 01:00:43 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32c89bcf-20e0-3100-ac9e-d30ae3a80259 | -3.4227 | -59.3564 | 2024-10-20 01:00:44 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3758e7f5-b8b0-3905-b696-d15c91e70044 | -1.7671 | -52.050701 | 2024-10-20 01:00:44 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc86f1be-a660-343d-9f06-91869624ed2b | -1.7691 | -52.059299 | 2024-10-20 01:00:44 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f69ef76a-d551-3ab2-93d2-de8d3630ae70 | -2.2966 | -54.379002 | 2024-10-20 01:00:44 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5616cb02-b19a-30c2-a04c-054cf9011f43 | -2.2981 | -54.386002 | 2024-10-20 01:00:44 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6c96117-8ab9-3788-a1f7-35c3035439b8 | -1.7573 | -52.052898 | 2024-10-20 01:00:44 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a539d40-ca8f-3c52-960d-3966548dc903 | -1.7593 | -52.061501 | 2024-10-20 01:00:44 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c8eb799-8df4-3a85-a456-bfec4cec5545 | -0.9833 | -48.852699 | 2024-10-20 01:00:45 | METOP-B | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c648b39-8e12-378f-92ff-af84f3b68f2e | -1.6339 | -52.053299 | 2024-10-20 01:00:46 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3408c53a-d6b7-3b53-b506-34f3fcc36ff1 | -1.6359 | -52.061901 | 2024-10-20 01:00:46 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdca9b31-4672-370c-8133-ae8c91063099 | -1.6826 | -52.537701 | 2024-10-20 01:00:47 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea4de78a-a97e-3306-9d6b-070b7b4212d9 | -1.6844 | -52.545898 | 2024-10-20 01:00:47 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50d2d3d2-c0b0-3e6b-8092-14f0353d79c8 | -1.5101 | -51.9618 | 2024-10-20 01:00:48 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 620b58e7-0f42-3d4c-8005-e71243407805 | -1.5121 | -51.9706 | 2024-10-20 01:00:48 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd6f21f5-0870-367b-80e0-4d7043c72b42 | -2.0942 | -54.8965 | 2024-10-20 01:00:49 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8001aad-aa10-379b-990a-edcdd8e47f07 | -2.0958 | -54.903301 | 2024-10-20 01:00:49 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f75e6035-cf40-3744-b1ae-a938153bba5a | -2.089 | -54.9193 | 2024-10-20 01:00:49 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b21ce86-e627-3f78-8bff-64a93731bc66 | -2.0906 | -54.926102 | 2024-10-20 01:00:49 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f691a1bf-af10-3123-8af2-d2750568ac69 | -1.8819 | -54.595699 | 2024-10-20 01:00:51 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03b27c39-ffd9-32f5-8796-42bc288067da | -2.4386 | -57.5243 | 2024-10-20 01:00:53 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73a86140-9032-3259-bc50-e7333d57e00b | -2.4402 | -57.5317 | 2024-10-20 01:00:53 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 641dcc3b-d6d3-3b62-b218-137c0464d30a | -1.1012 | -52.154499 | 2024-10-20 01:00:55 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| aa0d0947-b804-3236-a823-95a7b241f8df | -1.1817 | -53.370098 | 2024-10-20 01:00:58 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d7fcd6-72fc-3283-8e1f-3bf73ebf79af | -1.1834 | -53.377701 | 2024-10-20 01:00:58 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e1f5ac1-68a0-3d9c-bb8d-ba9844702ab9 | -3.0398 | -61.6586 | 2024-10-20 01:00:58 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c095b27-b772-3b72-b3cb-034c86bba9ac | -3.0301 | -61.660702 | 2024-10-20 01:00:58 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 806859ce-51da-3a74-8118-0e624390f11c | -1.145 | -53.662498 | 2024-10-20 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e8bafbc-26a5-3aa7-90cd-f485fbce0316 | -1.249 | -54.5313 | 2024-10-20 01:01:01 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9f5d03f-e53f-3e11-bfed-a3fd074c1452 | -1.2506 | -54.5383 | 2024-10-20 01:01:01 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d995c281-aa21-361a-8714-830b990f3546 | -1.2522 | -54.5453 | 2024-10-20 01:01:01 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7082c9d-fa7b-3c85-bd9f-b274792683d9 | -1.0611 | -54.1563 | 2024-10-20 01:01:03 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2d71c55-db01-38c6-8dc0-5d82be97b2e3 | -0.3436 | -52.0359 | 2024-10-20 01:01:07 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f18c2b62-dd41-3c9d-8b5c-28bd305fe5a3 | -0.3318 | -52.029099 | 2024-10-20 01:01:07 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 618a7256-89b1-36fb-a0cc-108ffb6fbc1a | -0.3338 | -52.038101 | 2024-10-20 01:01:07 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b561d436-9028-3076-8f6e-b1c39105b886 | 0.6718 | -51.864101 | 2024-10-20 01:01:23 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 10aa9098-4dd2-3c57-8356-f74ff7b1fe69 | 0.6697 | -51.8736 | 2024-10-20 01:01:23 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c329ab73-fea5-332f-aa16-b3cb72d8e406 | 0.6816 | -51.866299 | 2024-10-20 01:01:23 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 184b3a15-f788-3661-8cab-c3085eb2ef4f | 0.6795 | -51.875801 | 2024-10-20 01:01:23 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee6ad5d-5ed0-38ae-8192-b7466ab82c7d | -2.2993 | -48.5936 | 2024-10-20 01:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| b53b16b7-8eea-3b95-adde-f1104ffa77fe | -2.2994 | -48.5722 | 2024-10-20 01:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 61aa80e7-2821-3594-8f07-4a6444a23f9b | -2.3178 | -48.5932 | 2024-10-20 01:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d2c4a583-257b-355f-9eb1-26f6858b7382 | -2.7773 | -49.3067 | 2024-10-20 01:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 5942f499-7c81-3ad4-8e12-8b50d0237a93 | -2.7774 | -49.2854 | 2024-10-20 01:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7d0ebbf4-c7af-3808-b6aa-818242229f7e | -2.7958 | -49.3062 | 2024-10-20 01:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 70722774-ccaa-3406-9d0e-78cc49310db1 | -2.7959 | -49.2849 | 2024-10-20 01:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 38f5295f-b3b6-3183-9438-988498a6bf5f | -2.7981 | -48.6873 | 2024-10-20 01:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 2e631ffa-ca17-344f-9426-d335a945b809 | -2.7982 | -48.6659 | 2024-10-20 01:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d5964bbc-e65c-3e8a-963c-fdcae570807f | -3.0478 | -51.0226 | 2024-10-20 01:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a7e5af8d-b34d-3bf4-aced-fe9a31ca770c | -3.1462 | -54.3658 | 2024-10-20 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 0f5b15fd-9b38-36d6-be66-a965e3238a6b | -3.1462 | -54.3457 | 2024-10-20 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fefd40b1-4149-32e8-8e72-2ad99671229b | -3.3813 | -50.6788 | 2024-10-20 01:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 7fff66b7-8a55-37ad-bb56-52f735408b57 | -3.3814 | -50.6579 | 2024-10-20 01:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| c700d9ce-6c96-30f3-ae8f-c213edb1c222 | -3.3997 | -50.6782 | 2024-10-20 01:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 4c0e913d-9d4d-32a8-ac3a-5ea77e886450 | -3.3998 | -50.6573 | 2024-10-20 01:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| b74cb754-59fc-3df9-93da-04838cd6d3dc | -3.815 | -48.866 | 2024-10-20 01:05:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 1df74603-0fb0-340f-a107-066ac1367a42 | -3.8686 | -45.8254 | 2024-10-20 01:05:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 77f94c6d-f2b0-3333-a6a5-efd9d3835164 | -3.9018 | -49.9884 | 2024-10-20 01:05:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 57eb3254-1dc3-3d0a-9992-d88c9ac9562f | -4.1985 | -46.6318 | 2024-10-20 01:05:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 756bcb03-0c2d-3998-87e5-372d644cabfb | -4.4899 | -44.7564 | 2024-10-20 01:05:31 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| e5679685-e5a6-3eb7-bd37-0be5ffb0896d | -4.9112 | -45.8151 | 2024-10-20 01:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 8aaaa635-2056-3447-a1de-fd2a8fdccf5d | -4.911 | -45.8374 | 2024-10-20 01:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a7a44809-ca1a-3ee3-bebe-4f6e761f47ea | -5.226 | -46.0865 | 2024-10-20 01:05:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 84fadec2-daa8-39be-a236-9c1c4fdc1c5b | -5.721 | -68.6862 | 2024-10-20 01:05:39 | GOES-16 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 43a82a5e-f3f8-32d3-bfd7-0c70fe638e84 | -7.3638 | -72.8628 | 2024-10-20 01:05:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1c27755f-a633-38c8-bc21-c3abb4de26de | -7.7679 | -73.079 | 2024-10-20 01:05:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a0ac08c9-6de6-330a-9902-9a3ca9dac6a6 | -12.5147 | -63.3014 | 2024-10-20 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 46fe7d28-4f3e-304b-b787-55e0c47cf965 | -2.2993 | -48.5936 | 2024-10-20 01:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 1e590be0-b06e-3004-8bdf-f48ec7b128e0 | -2.2994 | -48.5722 | 2024-10-20 01:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 678171fa-4b39-3783-a626-f4e6270ad280 | -2.3178 | -48.5932 | 2024-10-20 01:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 14e8dc86-e931-36d8-b481-b7ecfadb56b6 | -2.7981 | -48.6873 | 2024-10-20 01:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 2e6a3084-ad38-3822-8d25-6833d7dbe96a | -3.0478 | -51.0226 | 2024-10-20 01:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 184229b9-77ca-3cc8-a255-62dbad6c29a3 | -3.1462 | -54.3658 | 2024-10-20 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 3e5098dc-546e-3c2b-b392-e34635a68fd3 | -3.1462 | -54.3457 | 2024-10-20 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1955c8ae-3a21-3867-b891-b24f39f516e1 | -3.3813 | -50.6788 | 2024-10-20 01:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f648c7ce-2e48-329a-a1f7-fba6d3720e7f | -3.3814 | -50.6579 | 2024-10-20 01:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| c71dfcdd-e29c-34d8-a6e9-1cf562f9ffd0 | -3.3997 | -50.6782 | 2024-10-20 01:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 3f4b3f1a-0193-3c6b-b61e-2d3ccc449de9 | -3.3998 | -50.6573 | 2024-10-20 01:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 4607fd8d-3892-3997-8516-c3684fa2e81a | -3.586 | -54.6941 | 2024-10-20 01:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| dc86dbcc-d9e1-3aec-b955-5397977fb690 | -3.5861 | -54.6741 | 2024-10-20 01:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 405e00e5-be72-3c27-9095-d9c0f7b3c2e9 | -3.6045 | -54.6736 | 2024-10-20 01:15:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ebe8fda9-7459-3d98-af6e-db4ed8bf35c6 | -3.8334 | -48.8866 | 2024-10-20 01:15:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 917299c9-0c1e-3df2-8041-20c47952ac71 | -3.8686 | -45.8254 | 2024-10-20 01:15:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 1909d305-0012-3500-b99d-ee0f52128ea2 | -3.8688 | -45.803 | 2024-10-20 01:15:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5a781a30-a876-39a5-b0db-3d66500c9138 | -4.1985 | -46.6318 | 2024-10-20 01:15:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 85cae457-2d12-381c-b274-288e4e26a2f6 | -4.911 | -45.8374 | 2024-10-20 01:15:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 087a7532-f088-3689-840a-43895e00ee9f | -4.9112 | -45.8151 | 2024-10-20 01:15:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| bc0694ff-29d4-3663-a1a6-b8bb58273783 | -5.2073 | -46.0876 | 2024-10-20 01:15:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 57c481a2-4a68-3357-8808-f2986e4661d2 | -5.226 | -46.0865 | 2024-10-20 01:15:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 653d2a65-aabe-31c7-a3c0-a7a52202a609 | -5.721 | -68.6862 | 2024-10-20 01:15:39 | GOES-16 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| b1acdc2d-4c27-3431-9453-77fecc187b06 | -7.3637 | -72.881 | 2024-10-20 01:15:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |


[Clique aqui para ver as próximas entradas](README12.md)
