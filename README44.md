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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4eda201c-d7c1-3878-96b0-03dcac85f112 | -3.10483 | -53.74643 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7d4e161-d88a-35c9-8585-e8236af4bfd4 | -3.23126 | -45.5631 | 2024-11-20 04:50:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6f95cf8-2f6a-3525-91e9-261b9f7a5e29 | -1.71087 | -48.02287 | 2024-11-20 04:50:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7a047859-9da3-35c7-85d6-2490dbae6fa2 | -2.28249 | -48.48741 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07722340-8ba4-3ab7-a58f-9537b4dded8c | -2.72128 | -49.34652 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4511f72a-c7e1-3e3c-9542-e1eddac06c4e | -2.14695 | -49.53871 | 2024-11-20 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bd8ba12-df95-3fc4-a509-952e2c559086 | -3.48413 | -48.23784 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8eb004e-8d48-322b-999f-65b565480473 | -4.19709 | -46.81246 | 2024-11-20 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 407b70f9-6182-3255-b990-23d1db6463fc | -1.24267 | -51.75097 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 695fe03b-cdfb-30f7-bb17-5a28f0b0e94e | -3.03106 | -51.52611 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64995e35-a74b-32ae-99a8-e8c392a10f63 | -1.37026 | -55.37415 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d7ab0ca-9e0c-327e-bd45-43e5382d73f3 | -1.5587 | -52.28135 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7f6df76-7e08-3081-aec8-58890235f40a | -1.25046 | -51.61777 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3091734c-a109-3f02-8dcc-7739174cbd21 | -2.79055 | -51.72112 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6fb0f68-fd75-3015-890d-c8797f1d4e41 | -1.14435 | -53.40568 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7a3040d-28f5-3fbd-be21-d2ad9fd29bb1 | -2.21678 | -46.47958 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78a1bc01-6af2-3fd9-8ab1-907b2c9a7ba6 | -0.96205 | -51.72812 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62a65ee3-06af-3bc0-9baa-332c550dcc21 | -1.62272 | -52.25899 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e849e24d-3cdf-3d1b-aee0-19d51aea0374 | -3.43018 | -53.2855 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ddc15cd-16d6-37eb-88d2-43c9a7218b75 | -3.04902 | -54.40912 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e14b8c3e-e57e-3a87-b05c-0533aea9a98d | -3.20266 | -54.32754 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8405aade-825c-3448-8ecd-2194502cd607 | -1.13565 | -53.6652 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f271242e-9bdc-3fab-b625-ed7a1243df3f | -1.77294 | -46.13679 | 2024-11-20 04:50:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4258fa3e-735f-3ea7-9625-5e2cd2add89c | -4.06208 | -54.05154 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ad6d37f-4ba1-3cde-a6d5-7ff49a6669da | -1.98582 | -53.14071 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e91e74ba-c86b-3ea6-b113-f8e2029339f9 | -1.70322 | -46.23406 | 2024-11-20 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87cd1c03-34e1-37c7-b18b-a81d344ad67b | -2.14753 | -49.535 | 2024-11-20 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 125d35ef-0d3e-3421-9d59-f9e868891760 | -3.84954 | -49.43707 | 2024-11-20 04:50:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c4cf6da-3832-3dce-b272-7d6268f9703d | -1.33835 | -52.51365 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8dfaf97-4fce-3a5a-a1a2-7dc1e7d16359 | -3.08975 | -54.67078 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 698bd3f5-949d-3a25-a3f4-32d2aa3a54d1 | -3.9876 | -49.9168 | 2024-11-20 04:50:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbcd908e-e05d-3cd7-b1f8-ffc6a2c38c95 | -1.63425 | -52.62188 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52b6a6f9-8bf9-3a3c-9a9b-1e8893f9995a | -1.33184 | -52.23846 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 975f16cb-02ad-3d05-8220-a2ba64a79116 | -2.22138 | -46.47665 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d552bb5-30fa-31f8-8c35-b9f62e9cae83 | -1.64205 | -52.6665 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f7484bd-d774-3208-b9d4-ae22ef3c8e8b | -2.58378 | -51.7243 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b6360ba-90df-3190-860d-3fdb84e0d5d2 | -1.46289 | -48.1985 | 2024-11-20 04:50:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14e35672-e0df-3f2d-b9ae-ca4de12e59df | -2.71528 | -47.97694 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6af9ad0-7880-398a-a659-47c3cc586dcc | -9.17267 | -44.72712 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2993cacc-043c-33c6-9e23-16b8f5a3738f | -2.86476 | -51.78561 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63c04dcb-8c5f-3753-95ee-d856f09ba8ca | -3.58104 | -53.72041 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46de3b05-22f7-3038-93fe-f7ec8fc46fda | -2.69826 | -51.36433 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c28cc3c9-cc30-325f-9970-cf58533ace65 | -1.62869 | -52.67936 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1089e92-2341-3a3c-9788-bd2b2028eb72 | -2.31815 | -46.85387 | 2024-11-20 04:50:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97c19ab3-90a8-3ab0-b91d-bb47ca297ee1 | -2.45155 | -53.70068 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0413db24-e060-3b6c-b1b5-e93f3810089d | -1.50507 | -52.12264 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcf6935a-b90a-3876-9677-48e94886d302 | -2.66129 | -46.60826 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4eecd5ab-8e94-3f6a-8d63-fe2f450ee26a | -2.35073 | -54.78768 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1600159e-acd9-3482-bd8d-29d28dee146c | -3.19913 | -54.327 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ce020ee2-dc05-370a-b070-ea52d5132843 | -2.14022 | -50.6519 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64f51928-2da7-3091-a156-5a6b8a1b16d0 | -4.04971 | -54.3754 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e04e874-9636-327e-8e39-f61f4a6ff670 | -5.05986 | -49.86195 | 2024-11-20 04:50:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a2666d7-035d-3817-a74f-847069938b45 | -4.06412 | -46.84041 | 2024-11-20 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f9e5a3c-2160-3b7c-a653-370fe013998d | -3.11487 | -53.70588 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 900cf7d1-33f9-3ba6-bf1f-ec9bfb8f65e0 | -6.24443 | -47.27252 | 2024-11-20 04:50:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5b566ee-1876-3683-86d2-6701eb2ddecd | -2.09406 | -51.09641 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da335a90-39b8-339c-859f-d7bdaeac063e | -6.24003 | -47.30531 | 2024-11-20 04:50:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9910baa-573c-3100-95e5-a3f2c97c6d90 | -3.90587 | -45.08764 | 2024-11-20 04:50:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6830f356-da83-321d-84dc-754b2ccdbc29 | -5.12841 | -49.44045 | 2024-11-20 04:50:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e744bd1a-07a5-3ef4-b360-71bbc7fb4248 | -0.93932 | -51.72104 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f686867-b313-3f56-be99-d6814c8e3ec5 | -3.77664 | -47.48349 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48a1ad2c-0253-3f32-bafb-21cf51c494f5 | -3.52007 | -54.48384 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf23e3c1-558f-333c-a44f-cdb6bc236f82 | -1.13472 | -51.68829 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a89301d1-a016-3a30-9aad-a68bbab1dd86 | -2.19231 | -48.92137 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4240c99-7be1-3a42-9617-e19e57158401 | -2.03548 | -48.08738 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd9e6b44-6053-3268-a9f7-d554a5d0762a | -1.83189 | -55.04662 | 2024-11-20 04:50:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f75bf9ac-e2ea-3d8f-9072-2b9b637dc8e9 | -0.77618 | -51.74897 | 2024-11-20 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a23fdd0c-7f78-3d83-ab7e-67bc0ab62a1c | -2.61884 | -51.80393 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2945e8d-b5bc-3338-8b37-11aaa8831995 | -1.1485 | -53.51483 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a2c54a8-776c-34e6-a620-507e6069b3c3 | -1.61564 | -52.47748 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55e6dea3-303d-3b19-8bf8-09bbfc0a0243 | -1.23999 | -51.78951 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32717157-aa17-3cbe-ad19-59174ee63a17 | -0.81862 | -52.48414 | 2024-11-20 04:50:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d91acb5f-7001-3e19-bd92-5a9fccc66581 | -3.74256 | -52.40139 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c86dbb7-3cf8-3642-b7d2-f347f9df240b | -3.7288 | -47.37955 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43a3ee36-bd01-36a8-9f48-21edd53c62f6 | -2.68612 | -51.80367 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e57babd6-907c-380d-8732-53a3474a03f9 | -2.6183 | -51.80738 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7ac8451-164c-3141-abe6-7c4d2873bc25 | -3.08775 | -53.26165 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d473f02-9290-3331-8721-6116b0208e5c | -1.04462 | -51.74154 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ddb420c-7d71-364c-a869-412bfddebd68 | -2.663 | -46.24178 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb0165e8-d728-3507-ae5a-cbb8424f6f44 | -3.80618 | -47.79653 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bb12a9b-f60a-3cce-9179-77023f4e10bc | -1.90613 | -53.33524 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd374c72-5275-382b-a3fb-3f3eda09aa16 | -2.26573 | -50.81808 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8f78a99-deea-3a6c-a7e4-27352c7ad81e | -4.13404 | -47.73061 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04a3d12d-f269-35bf-9b6a-d4b290f1138c | -1.19984 | -51.97861 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 107be2fa-cbe7-3ced-a05c-701f3fb52034 | -6.36215 | -55.36705 | 2024-11-20 04:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cdc33f8-107a-3368-a7c8-f0ad10d51441 | -1.24124 | -53.36648 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d878a16c-9c6e-37da-bc26-238c75c079fa | -1.33731 | -51.8577 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f596a090-c765-33b7-ab4c-aaf2b624237e | -2.63253 | -54.28225 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 723d4e9f-ea5f-3c08-9830-286b5dbf6616 | -0.80289 | -51.60081 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 033c6a3f-b731-3363-8b84-26f7d3ed58df | -1.25155 | -51.75943 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f633c5f-816d-3926-863b-a2c15b6377e3 | -3.26367 | -45.13664 | 2024-11-20 04:50:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b66eef1-e4b1-3a89-bed4-11ae44efc323 | -2.45429 | -52.16019 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef7ad22f-06d2-352e-9e54-211ef058326e | -2.95236 | -53.71977 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd9c9538-8699-3f7d-a5b2-76682689d883 | -1.0989 | -51.74289 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 925d7632-8f2e-3413-b9f1-8303b1caa576 | -4.97557 | -49.636 | 2024-11-20 04:50:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fee8ae66-b5c6-3563-9515-ce378352501b | -2.75092 | -48.56941 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f70f4a51-b816-381e-b649-012f50d80db5 | -7.219 | -45.0831 | 2024-11-20 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75be06ec-d4df-30b2-af44-edd7d73eac69 | -1.48135 | -51.15972 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 58602803-5105-33b2-bd70-ac3fe1471454 | -1.66585 | -52.09422 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39f3c308-5b16-33e0-88cf-c72c0f778487 | -2.84574 | -46.67617 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README45.md)
