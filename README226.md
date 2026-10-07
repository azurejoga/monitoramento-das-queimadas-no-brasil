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

## Dados Diários - Página 226

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c457ff72-ca7f-3e44-8cb9-b56a47bbc313 | -1.61548 | -55.11761 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 211db4a9-433e-33bc-a061-c074dbcb2e73 | -3.12977 | -53.69912 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b4feaaf3-2399-3c42-8ebd-d2603a23039d | -3.17356 | -54.6123 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4d3a59ce-5054-3fe6-aed4-1e47b752c86b | -1.6302 | -55.41739 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e1f371e9-16e0-3e96-b391-0b03c7e3df29 | -2.58237 | -56.15803 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 0a19de38-7cb6-3072-8aca-e150e5c4a77f | -3.09601 | -53.72184 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f25fe1e-b43a-3c0c-9c5d-19d3f854812d | -2.50226 | -49.31182 | 2026-10-07 16:39:00 | NPP-375 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8e5618e-273e-3d4d-9b9a-10f92639c5fe | -3.98979 | -56.24136 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ea0a8635-9d6f-380b-b09a-91eab00fa9c1 | -3.31467 | -49.13515 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2eef6d77-00b0-3e1a-9c45-bf5f5966af2c | -1.99124 | -56.25425 | 2026-10-07 16:39:00 | NPP-375 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e178f765-15a4-3c98-8122-23cebd0f65fd | 1.76783 | -55.58231 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b458bc39-c72d-336c-9439-0b3564b12b8e | -2.79147 | -54.07892 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 234.7 |
| c6eee7fc-69af-33e8-bb1a-a19047ebe058 | -1.27722 | -55.86356 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| eaee416d-a2bf-3a4c-9e6e-1ade894d1b0c | -3.5055 | -54.65427 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 06af3a73-0bc8-30f9-b89b-b4629d1da999 | -4.12228 | -50.80977 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 89ec3a74-58ab-3a99-8929-7c6ca63a6610 | -1.42673 | -49.10904 | 2026-10-07 16:39:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9013251e-c3aa-3930-83bc-5a558109b8eb | -1.42459 | -55.4234 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7bb75f62-4ab4-3de2-8339-e97de4890910 | -3.70961 | -51.14169 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 56781977-3034-3a8b-a2ba-076ab74af253 | -2.76032 | -57.66151 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 1e98164d-b3d7-3294-aa79-9dd163db4e41 | -3.29778 | -53.85882 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 857210b0-9af8-377f-9abe-5a58d39a6b2f | -3.01872 | -54.05942 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 89aa9950-a375-37d2-9e59-4b862332fc2f | -1.14737 | -54.10051 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 844b8ea8-fca0-3148-a0a7-fbc9677af5f5 | -3.27632 | -50.41425 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4f78bba8-b917-3212-9c15-585b4e720596 | -1.4688 | -54.51981 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c053fab9-7658-33d0-8eb9-2b2c7b4117e7 | -3.35912 | -50.76722 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2ad60db7-305f-33f5-8f90-1ca4e694fb55 | -3.10812 | -55.24888 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 21a9a46f-9b9c-3812-bf74-4d71f9893d4d | -2.93794 | -53.22976 | 2026-10-07 16:39:00 | NPP-375 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e7937656-b625-39f7-ab03-29de989e476f | -3.30225 | -54.03751 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| e2f07df1-255f-3c12-97c0-5c8519b8de6f | -3.47849 | -54.62731 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e7eaa818-732f-346e-ada5-667ed5f87bd9 | -3.19686 | -50.54813 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| efa9028c-e02e-321d-b7cd-7f49700f92d1 | -3.04851 | -53.91285 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| f0762262-3016-3b84-b393-6cad5f57b2fc | 1.34448 | -56.13419 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d5c8cf93-5bf7-35f7-bf12-1a91ac5cf742 | -3.54874 | -54.65928 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 56b0b38e-b69d-30f9-bfce-bca7bdf376a7 | -2.59039 | -49.62628 | 2026-10-07 16:39:00 | NPP-375 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 8bd24fbc-f7e9-3301-8e4b-69cfb5c9886f | -4.12532 | -54.24873 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 679c5da4-f2a0-3af0-8bd2-d9a1eb3937f3 | -1.28449 | -55.8574 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| ee3386e8-10d6-3272-9fe0-78c29868c51c | 1.75675 | -55.58055 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 19d41020-86b3-39fe-9ee3-07a095bc7ac6 | -2.76858 | -54.11008 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 9de61aeb-3246-3be2-87bd-3a76b2cffcf1 | -3.28009 | -54.03708 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1077b731-a10c-31df-9832-5a50b9776a1a | -3.4345 | -56.9352 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 261915cd-1348-3286-844c-6a6766638623 | 1.75492 | -55.59158 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 230a4914-bae8-35a4-bdb8-c5516ad2f038 | -1.28669 | -55.41436 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f3aca8cc-7b31-3cb2-b692-1f76843327dd | -3.02142 | -47.46625 | 2026-10-07 16:39:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bbe54cf3-321a-387c-bbf4-92faf8ce8bee | -3.04414 | -53.92028 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 64537f61-899f-3e59-9bcb-bada2e365022 | -4.57127 | -54.95551 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0a6ddd0e-ccd8-3397-b000-e150247d876b | -3.16223 | -48.58191 | 2026-10-07 16:39:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 9880471c-275d-39aa-8999-477253821fa5 | -1.7314 | -54.83916 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b7ebc969-3660-32b8-be27-b444dccba8a9 | -3.85528 | -55.98115 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 8da76411-393d-30be-b102-1e0e3bb06216 | -3.40291 | -58.02394 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bec6fb4d-d6f4-3d00-8fb3-2fea9ecf6983 | -2.99986 | -54.11797 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2dfc3a2c-821e-398d-99ca-596d36340341 | -4.07831 | -55.33233 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| befb6059-40b0-3078-82b0-51a8ce2279e9 | -3.05738 | -57.52406 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| ce4b2945-36aa-3c95-acc8-93167bdca87d | -3.07019 | -54.25224 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c1b2ff52-9dae-336d-9cbb-8a194c669790 | -3.64593 | -54.51084 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 24b1b57e-f9d5-3270-833f-6b9c25418164 | 1.70491 | -55.62433 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8743050a-4cb4-3d00-88ee-386fbb53c5de | -2.43922 | -56.54743 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d729a847-1653-39d6-aba8-cf8a4a190d33 | -3.30326 | -54.04436 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| e34d633a-7254-3875-a7fc-1306a013e896 | -3.00099 | -42.87101 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| dd747c2f-e732-32b0-a740-97b0a2df8370 | -2.41432 | -56.53386 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa0c86a4-15b3-3532-b6b1-c5829ce2b323 | -2.45442 | -44.53859 | 2026-10-07 16:39:00 | NPP-375 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff1a570a-eda7-3088-a690-361f0e22d23d | -3.05014 | -54.15168 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3af6441b-7ef6-32d9-8928-638abb4bc40d | -3.04242 | -54.25426 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 7fd57e60-07f4-354c-b0c3-10b6e18678b0 | -2.97261 | -56.62232 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| f2f6789b-15f1-3fdd-b618-2933db52fd22 | -2.99074 | -54.05655 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 739c6cab-860a-3aab-a057-a4d329c2997a | -2.8822 | -54.12162 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b9365514-8bd2-3d79-94e8-5598561ad701 | -3.44839 | -56.93895 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 422.0 |
| ef8384c2-0cbb-39a8-aa01-5600a936a7be | -3.27368 | -54.03101 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ae125866-e234-3c6c-b1fe-b01aa817a740 | -3.97997 | -56.21704 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 14230126-b811-3538-b0ce-e310f5df3e8f | -3.54524 | -50.10748 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c23a6966-66b0-3e93-a5a7-33331931c8ae | -3.11468 | -53.78092 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b74ccfdc-88c4-34d0-8551-ad5b0ed50857 | -3.11441 | -54.9709 | 2026-10-07 16:39:00 | NPP-375 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 589b6aa6-0377-3281-a882-349bf5d036fa | -4.1229 | -50.81399 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dce60a61-480e-3a3a-9d75-8a1e09523827 | -3.64645 | -55.49306 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1777ba9e-8fa4-3f02-8acf-a771f652c5b1 | -3.2855 | -54.03635 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| edd1a87c-b71e-3c01-8b69-3226cefe1a25 | -3.09969 | -54.149 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b12e70fa-ee11-32a8-885a-db3926948ae2 | -2.76605 | -54.09299 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 378e2fa8-9d71-363c-8655-430759582e75 | -2.78507 | -54.07291 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 41c9298b-894c-3883-8fb0-a2daf4b950c5 | -3.4982 | -54.64388 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b8436a8a-bb00-3729-8f5a-dce4e5a6cc7e | -2.80224 | -54.07735 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d00f3b80-8991-3d5f-bf96-4e8e76a84f1b | -1.27923 | -55.8625 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 83213cfa-7dcb-33f5-b68a-abd00374cca6 | -3.76523 | -51.33291 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 60095aa6-c18e-3d27-b4d1-3be51800690f | 1.05669 | -50.035 | 2026-10-07 16:39:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 88f2da2c-48ab-3b0c-a84d-ed75e561f41b | -2.03844 | -54.30434 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5cfbf915-32ca-3bcf-b879-6736936b8846 | -3.81081 | -51.03485 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 27008649-50db-39d5-a085-4e74f51d50ef | -0.66378 | -49.54608 | 2026-10-07 16:39:00 | NPP-375 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 057f3a7b-885c-378f-98f4-74cd9db98fc4 | -3.49432 | -54.61733 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 771836de-1168-3c3c-91c7-2d3e6504a423 | -3.72693 | -55.48708 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 179.3 |
| afb2259e-20c5-3cf5-a452-e39735d64f6c | -3.69627 | -55.48648 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 2bf4ebee-917b-3fb4-9762-3f7441c723e8 | -3.1901 | -50.56115 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| bc8d3a1e-ce7a-3986-a4bc-8d4c7f8a7c76 | -3.18412 | -50.54998 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 67b0175c-fd68-3789-acf5-e8ede1f0068d | 1.98097 | -55.86807 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 842826cd-1fc2-36f4-aa26-4a462ee917b6 | -4.92854 | -55.86422 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5f6495c3-0026-3ef4-994c-5e0fd94c14f6 | -3.93217 | -54.57975 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2d09929a-b9e3-3912-8ed1-b324626ae0db | -2.60925 | -57.58232 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 13677270-f26b-35a1-a477-338931a84a77 | -2.39081 | -56.1273 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| f541ed6c-4c5c-3284-a434-1d51817d376c | -3.29194 | -53.85628 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 55e7b3d0-aeeb-3a78-addb-7b35eb4af120 | 1.06485 | -52.54298 | 2026-10-07 16:39:00 | NPP-375 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 310cf8e5-6442-3026-a1a7-4ba7f67dbb5b | -3.28351 | -54.02269 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5ab10be5-3c44-3c01-ab83-1c44bab6d872 | -1.42445 | -55.42741 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 134f2bbc-e9b7-35a8-9484-6452cff1eec1 | -2.0906 | -56.62251 | 2026-10-07 16:39:00 | NPP-375 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |


[Clique aqui para ver as próximas entradas](README227.md)
