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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 402003c6-5627-3048-aae7-df2cf0963b65 | -3.56769 | -54.68264 | 2024-10-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0178ca4-f37a-314f-9275-090cefb4240a | -3.56579 | -54.6701 | 2024-10-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fad5a644-6723-364e-8ec5-9f7f13ecffb6 | -3.56502 | -54.67519 | 2024-10-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faf00748-0262-3066-9b0d-ffd6be1c2fb0 | -3.56426 | -54.68031 | 2024-10-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf8bae78-8b8a-3004-8665-d043f23eae5c | -3.42665 | -54.58659 | 2024-10-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb493d7d-f77d-3e5f-9704-db82239509c7 | -3.4259 | -54.59171 | 2024-10-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 232178f5-9e9d-31b6-977b-e247925a072c | -3.40858 | -54.4896 | 2024-10-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 839e5ac9-f871-3bce-83d0-60929d0b05ea | -3.40783 | -54.49472 | 2024-10-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ca3f6e14-87ff-38af-872c-2b1339268575 | -3.40709 | -54.49986 | 2024-10-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 91143cbe-a823-3dd4-a479-33eb6409aca1 | -3.1668 | -53.9183 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21f0adef-56c6-30df-807f-34791f0b2fcd | -3.16679 | -53.91553 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87273932-23d1-3351-aafb-a01db2a49420 | -3.166 | -53.92097 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d501049-0bcb-35b3-b241-2dbb77998d4b | -3.16029 | -53.91718 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc652ce8-e1ce-3557-81f4-03e04202909a | -3.16028 | -53.91433 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4d7f1c5-ae61-373c-9540-59b1e2467560 | -3.15949 | -53.91982 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e29e9d8a-329b-389b-8240-ccbf554c1f4b | -3.15947 | -53.92258 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c061bd74-48b7-38ec-89ce-990c5d33912a | -3.1538 | -53.91599 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a72a2e13-a25c-3670-8847-f7358a72290d | -3.15377 | -53.91321 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d706b4d4-9385-3468-8dab-fe7961571d3b | -3.15301 | -53.91853 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61e71941-d366-31f2-ab85-fb478ddaa18e | -3.1403 | -59.16696 | 2024-10-28 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac529a81-d26f-31dd-84fc-da5602b11c07 | -3.12783 | -54.27369 | 2024-10-28 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 965d9e89-be93-37ce-9017-adbe1f4c5330 | -3.12705 | -54.279 | 2024-10-28 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98263817-4635-39d5-bca8-9480ce0cff06 | -3.11352 | -54.28236 | 2024-10-28 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 13d0f79c-d392-3b52-8da2-53b85f235024 | -3.11276 | -54.28755 | 2024-10-28 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d065d15b-ad47-37ac-a6ec-0019441724d9 | -3.11187 | -54.27903 | 2024-10-28 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3fa9b6e4-f202-3528-80a5-4994b4a3d2d1 | -3.11109 | -54.2842 | 2024-10-28 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8423d839-885b-3863-8a29-9de5e3f97922 | -3.09544 | -53.72139 | 2024-10-28 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 54a1f8d3-baae-3096-b3ed-bb2bd6820718 | -2.89097 | -57.67759 | 2024-10-28 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e3cb7d2-7890-3c25-80ad-084afe8aea53 | -2.89051 | -57.68058 | 2024-10-28 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 048adcf4-d4d2-3f3d-bf3e-5e583371d561 | -2.89005 | -57.68357 | 2024-10-28 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3da4841d-9cba-3e7e-82d7-d3e8463862c6 | -2.86193 | -53.33291 | 2024-10-28 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 03dc797f-bee8-32cd-8df1-a99b2aef511b | -2.86102 | -53.33907 | 2024-10-28 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 778824f7-baca-30f1-b7e2-07e558b0f88a | -2.84842 | -53.33111 | 2024-10-28 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ccc1108-b78f-34e7-8115-2c336b9476e6 | -2.84169 | -53.33007 | 2024-10-28 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 118683fd-4302-3dd1-8fb6-d60fa9aa4d28 | -2.83819 | -52.55133 | 2024-10-28 05:46:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 405b9900-79e7-3e9b-b7a0-5898758fda8b | -2.69038 | -58.08589 | 2024-10-28 05:46:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f627c576-adb4-3d35-8fff-5f1e80445864 | -2.68542 | -58.08527 | 2024-10-28 05:46:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a0598f3c-ebae-307b-b67b-1c60d0e99ea0 | -2.64431 | -54.29772 | 2024-10-28 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8e495202-7a7c-3974-93ec-fe97079c40e9 | -2.64117 | -54.29482 | 2024-10-28 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fb8f9d3c-2b72-3bd1-8a04-629a50c9e3bd | -2.64043 | -54.29993 | 2024-10-28 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b2be1985-2cab-38ad-91ad-b630b2e0f77d | -2.63798 | -54.2967 | 2024-10-28 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 71a03b29-71db-3b4b-b638-01eebe6ded9b | -2.55998 | -54.02308 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff84c702-53d8-3aa0-ac79-4bdc160bbfc9 | -2.55832 | -58.11529 | 2024-10-28 05:46:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c4bc459-9565-3dcd-adca-06c7d7465b7b | -2.27801 | -53.77701 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0c95f601-af57-3733-851e-598367109f08 | -2.27718 | -53.78246 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 04ba925f-685a-38d7-bcfc-caa06b877a4f | -2.27555 | -53.79327 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8cf4affb-0858-3625-9bd3-61c11e6860b4 | -2.2715 | -53.77602 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5a191e0b-9485-38ca-bef9-087021b3938d | -2.27069 | -53.78141 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 19c23a11-0926-3b94-96b0-8f9e65ceb508 | -2.26989 | -53.78667 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 7b2b48e4-eb2c-3257-b0ed-86115d3c5818 | -2.26909 | -53.792 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 6876d0d3-b463-39f4-8c8d-7e043a252a05 | -2.20502 | -53.691 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f2ddfe2a-a21a-31aa-b5ee-26a5be93c2ac | -2.20461 | -60.16871 | 2024-10-28 05:46:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae75d258-1519-3caf-9b84-24c55cef0124 | -2.20441 | -60.16825 | 2024-10-28 05:46:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1234539c-4b3b-3a7b-ad08-f7b7ce251fc3 | -2.20396 | -53.69204 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e6bd6752-d876-33d9-9781-0c53f33db488 | -2.19846 | -53.69022 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e62c0855-741a-3f86-9189-4425a950a5ef | -2.19817 | -53.68593 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 55bfc46a-f048-3ab4-bd38-8f9cc6a8688c | -2.19764 | -53.69556 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53ad45a3-80f3-3fe8-a19a-0f5ef4ec0891 | -2.19738 | -53.69136 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 94f20fd6-d05f-352f-9608-8b69d8a6b40d | -2.1966 | -53.69671 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| aa048cf8-de4c-3449-9310-c812f60e15c7 | -2.05882 | -56.86966 | 2024-10-28 05:46:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0334676d-0492-3708-ba55-958172aab3ea | -2.05861 | -52.16743 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39cdb888-3dde-3b93-83ad-72fbc96fec93 | -2.05831 | -56.87295 | 2024-10-28 05:46:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00f216f9-1e1d-39b0-9c16-c60788e87632 | -2.05793 | -56.86715 | 2024-10-28 05:46:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fe6099b-2b6f-3ba3-8675-192ed8a666db | -2.05756 | -52.17413 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c679d5d-3473-34ba-9acd-58498e04f655 | -2.05745 | -56.8704 | 2024-10-28 05:46:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b521aac0-02b7-3233-9985-123016323b64 | -2.05427 | -52.16991 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0e87c1ce-564e-3979-a2b4-cc9802f706b8 | -2.05349 | -56.86895 | 2024-10-28 05:46:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d016357a-857d-3cc3-ae8c-d333626844eb | -2.05211 | -56.86973 | 2024-10-28 05:46:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17e0d9b9-30b1-36e7-a410-d803fa5276ec | -2.05147 | -52.16641 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80c7cc62-2402-345e-8706-125144a60e66 | -2.05041 | -52.17318 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4803bde9-c1eb-3cc8-b43d-75eb6b1ed5be | -1.92511 | -52.13358 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a4860ad-c7e5-36b3-88c8-dfb78f5b13d4 | -1.9217 | -52.13175 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c1afa937-eaae-36f9-a8c2-48e9a896cf54 | -1.92063 | -52.13864 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cca8bd91-4670-3f23-936d-6872f062606e | -1.91798 | -52.13246 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adb2cec7-327a-3e35-b16f-8cd924fea12f | -1.90497 | -52.3331 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46a971f5-d4d9-36d2-a5f9-1e3f3ba7ccbf | -1.90316 | -53.53539 | 2024-10-28 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0994b076-8935-3f30-b3ac-43da454473e1 | -1.90254 | -52.33427 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d694cfed-c0d2-3cd4-829d-68a0639dece7 | -1.89793 | -52.33194 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f0d45d3e-b208-3ae8-a4d7-efecfb4ca12f | -1.8955 | -52.33313 | 2024-10-28 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ccc304be-2bed-39ee-a042-857791772362 | -1.75692 | -54.00641 | 2024-10-28 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46cce4c7-4761-3c1e-9aed-5ebd18f5c0a3 | -1.73503 | -55.00119 | 2024-10-28 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ba1e8a8-614f-3463-b74e-a5c47157ac7e | -1.72906 | -55.00021 | 2024-10-28 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 107edfad-84da-3d0c-b524-2d4d272fa595 | -1.69267 | -55.08009 | 2024-10-28 05:46:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 004a201e-1d9d-3fba-8615-e601cc914b06 | -1.69202 | -55.08442 | 2024-10-28 05:46:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f040418c-0afe-3c08-907e-8096b41c447d | -1.68911 | -55.08046 | 2024-10-28 05:46:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b830bcd2-096c-3f2b-90ae-59afdd979b86 | -1.60502 | -55.70599 | 2024-10-28 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3c88355-8d08-347e-856e-847b2148e1fb | -1.60445 | -55.70977 | 2024-10-28 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14d998c8-d79d-304d-a31c-29aec290341a | -1.60292 | -55.70579 | 2024-10-28 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aeb98817-b72c-3cbc-be93-5fb606b591d2 | -1.60232 | -55.70959 | 2024-10-28 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a496c20-9f1d-39fe-81eb-b03cb34322ba | -1.54174 | -52.08911 | 2024-10-28 05:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 45395761-5fed-3181-82a0-17e7c968b74d | -1.53881 | -52.08669 | 2024-10-28 05:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3b42d3cd-f4ac-30e3-a547-3477eda58357 | -1.37372 | -55.85908 | 2024-10-28 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fe081ca-b8c8-3f4a-84a6-b731dbfd2756 | -1.37314 | -55.86287 | 2024-10-28 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbc47107-0219-3fe4-a39f-2d4e4563df9d | -1.29886 | -55.72192 | 2024-10-28 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1f13f4d-64e9-3438-9425-05b7c13f88ba | -1.29828 | -55.72576 | 2024-10-28 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c066174e-cbbf-32cb-b64b-6909733d614d | -1.29376 | -55.71728 | 2024-10-28 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c42ceb3e-690c-333f-a6d4-77b192acd506 | -1.29318 | -55.7211 | 2024-10-28 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 943557bc-e8c2-3f8a-84dc-45a106c275ed | -1.29259 | -55.72495 | 2024-10-28 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc64a4d8-ac1e-3544-acfe-893a63db81ef | -1.18299 | -53.50599 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a965d521-22e4-392b-bc21-3e9310b3686e | -1.18293 | -53.50992 | 2024-10-28 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README85.md)
