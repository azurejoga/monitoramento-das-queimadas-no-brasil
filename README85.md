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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ee572ff-237a-373b-a4d0-a245c297e4b5 | -5.27705 | -56.11489 | 2025-09-03 05:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 439d2de1-3bda-35db-a2fe-7922244e5b94 | -6.84796 | -45.54771 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ca7c603-3927-33a1-8a59-b36750d772b5 | -7.79708 | -45.44775 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7489133-f4d0-37c5-bc3e-c1dc03b8c8b5 | -4.15791 | -46.78557 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 808098c2-fb88-3b78-a4a7-b3d3b46a9d8c | -7.48279 | -44.80996 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92334329-e741-3528-9c82-508cc27fceb0 | -7.92616 | -46.54692 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7a245b53-34e3-3390-8aa9-e77a9c74bb52 | -4.1627 | -46.78281 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3939223f-0b60-376b-a233-751e3833aa52 | -6.45518 | -44.68013 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ca08481-cbb1-3628-a3d6-0f6e3a80dca2 | -6.05203 | -57.99907 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 240c0039-82f2-36d5-9b99-c7767ed17cc7 | -6.27212 | -44.50636 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e0ec113-2763-3854-ad17-397c491a3352 | -4.15596 | -46.78901 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 16a6f87d-38a8-3994-979a-91e1c4dbf339 | -7.69405 | -48.74297 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 254ad18a-cbdd-35c3-a70d-547fa7772c4b | -6.34521 | -45.66384 | 2025-09-03 05:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1043248f-ba71-30c3-8eb8-6af97269d0e5 | -7.71712 | -48.72322 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7ac9bc1-da52-365d-9d88-4b9b39b3b3d7 | -7.59531 | -46.22736 | 2025-09-03 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01cccc81-9004-3e38-81da-2710c7d57728 | -6.274 | -44.51035 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34c794a8-6a91-3ae1-b6a4-890a2e531546 | -5.90976 | -57.74722 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c173cdc3-f136-3ffb-9639-51621e0a7d93 | -5.89698 | -57.74162 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 01dfe58a-64f1-38a7-a9c5-34ebe6596a7d | -5.80558 | -43.2269 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 56a45696-4b2c-3131-ab60-08257e586be7 | -7.70537 | -48.73868 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 19bf34f7-5db5-3600-a065-af0e4cbb3b6e | -6.43752 | -58.12547 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 548db3fc-5e26-3468-b0bf-87ed009cf3b4 | -5.81276 | -43.22832 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5c061528-be0f-36da-bf11-9cc81d79749e | -7.4761 | -44.80858 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ac7edb9-20fb-32c1-ad7e-f2aaeaa8047d | -4.89308 | -43.20081 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8ef919a9-a8f1-3deb-9f4b-391abdd2e962 | -5.9142 | -57.74078 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ad85eb47-4404-3d29-8c4e-2200b1f0f17f | -5.92196 | -57.71341 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3ed76fbe-0f9c-374c-a096-22dcea39f574 | -7.5085 | -45.34232 | 2025-09-03 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58874cbb-23d8-34fc-814d-50f3d1b27e22 | -7.91027 | -46.42907 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2544292c-ed90-38e7-8805-93db40d5acbb | -6.82709 | -52.83815 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ab6ecd9-31a1-3d1a-b062-6a03201066ac | -7.10609 | -50.77868 | 2025-09-03 05:12:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5697a58b-d290-3236-85e4-f9b94997bfc8 | -6.47064 | -45.40924 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4700bc8-f5f6-3f8c-b6f6-71069c23c272 | -4.16216 | -46.78644 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d5df7c3-2080-3a28-b763-27502906fe33 | -4.15118 | -46.79207 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 991684cd-9b86-3bf6-9aa4-17e04a4b097c | -4.48508 | -48.11987 | 2025-09-03 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1cfa442-c525-3f90-a08c-61e8b49f8abd | -7.70144 | -48.72844 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| db151f8b-da21-333d-b42c-ab253a33a5c5 | -5.87144 | -57.77335 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b526d68-a1fa-381f-990a-1d01e7d9dde1 | -5.89921 | -57.74912 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5344efd7-44c2-30be-864c-8278e1edad50 | -6.47104 | -45.40979 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20dd9363-4243-301f-acc3-2115fbdaf25b | -7.48947 | -44.81134 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 015ca753-49ac-399e-aecc-2b651d4740eb | -7.93125 | -46.45947 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4a3cf95-0d01-345e-9572-8794052aee53 | -6.22555 | -43.38619 | 2025-09-03 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb964643-170d-3a6c-98a5-3c4dbc8e3217 | -5.86366 | -57.75778 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1043e474-9a86-3b21-a049-f04b44b93e02 | -2.13767 | -48.00647 | 2025-09-03 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 129df866-bf0a-3dc9-9bed-892c04f6c771 | -6.82749 | -52.8078 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58d03d0b-13ac-33e2-9bd0-0270663e1a27 | -7.47936 | -44.81544 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4c77f592-be8b-397c-90a6-499199b8ff38 | -7.89369 | -46.45955 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5998b90-d834-3cfd-8f90-eac5efe12f79 | -7.90341 | -46.47999 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b79aaa3-2e85-391b-9db0-28f2ec0263db | -6.27123 | -44.5128 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 801a9222-dbde-33f5-a3f6-b1956d8ea3a7 | -7.02067 | -44.36465 | 2025-09-03 05:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1cefb92-fe4a-314e-a3dc-f13919a2bea3 | -5.91308 | -57.72631 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 354e997b-e2a2-3c0f-8087-44db677b384f | -6.80028 | -52.83253 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b83a33ff-1574-37dd-88cb-441791498616 | -7.92507 | -46.45911 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 960d857e-cd16-3acc-ab31-8db0484e5cb4 | -7.93006 | -46.46875 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6ad13610-bef7-3710-a60a-df19cdf0f4a6 | -6.33781 | -53.44523 | 2025-09-03 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d311e38a-d6fa-3901-8653-9ff8a14ca3c5 | -6.8042 | -52.82988 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7504db4d-d07b-39bb-8164-8fa00ba3a751 | -5.86866 | -57.76932 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4003bbd4-6942-35e1-a3d2-99944026b114 | -6.80253 | -52.81762 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0113622e-8ca9-35ea-a621-55151277970c | -6.81432 | -52.81942 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 601a8dc7-13e4-39cb-aea6-7f3a1b82a0b8 | -6.03128 | -46.00933 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0b1bbaf-85a3-3be7-8431-6cb86ac58548 | -6.8482 | -52.83122 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f25af9c7-d247-3860-87b8-359a2399cdd1 | -8.07091 | -45.36458 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92753f52-f64d-3b62-a92d-fed1e6b4f6d7 | -5.92696 | -57.72491 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8c30132-bed0-3650-8488-b1d2db8bf9bd | -6.43695 | -58.12898 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac8c9116-7ae7-3f27-8839-233cf406ff3b | -6.05147 | -58.00257 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8786d034-4be7-3ec9-b5c1-e3a101038a56 | -6.46289 | -53.40572 | 2025-09-03 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91bd7d37-12ef-3fc3-a83c-bca2bc9364e0 | -4.15686 | -46.79296 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e4f5d5a5-b070-3413-b387-af6010686033 | -7.69846 | -48.7498 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 988becf7-3041-378a-95dc-7cd3ae6254e9 | -7.50263 | -45.33644 | 2025-09-03 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 018fbf70-ed9c-32ba-9d86-4323fb0cc086 | -7.50193 | -45.34173 | 2025-09-03 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c841358-4c1a-33c0-8e78-ff7ac0cd8a5d | -7.90037 | -46.45621 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 982df578-d092-396b-8ab6-4b4b4ea1cb4c | -6.34227 | -45.66167 | 2025-09-03 05:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 940936fb-d464-33f7-b02d-eb5765d61905 | -7.69447 | -48.73997 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 8787696a-f1b8-3aec-a621-b884cb5a71b7 | -8.20392 | -44.80015 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 83c31574-b1e4-36ae-89f1-5bd95bb1792f | -8.06584 | -45.36139 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7674feb9-2422-3361-98a2-ac5c401052dc | -5.90532 | -57.75365 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82a1bd84-a240-37e4-bfcc-cd9b99963bba | -4.89541 | -43.1993 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e6d792d-e726-3741-9dc9-d065dcc8a1aa | -6.85824 | -52.81761 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbf52929-d83f-3ca2-83e6-ff57e4dcfaf2 | -6.81631 | -45.68555 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a7db9fd-a32d-34f2-8181-8c546fbdf382 | -7.93285 | -46.54317 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d1b8f70-3f07-32a1-9685-8c547e1f91bd | -4.42556 | -56.13344 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb3f08e4-c1c9-3b12-b7fd-ca9b04ad410c | -4.89109 | -43.21471 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a6aab6e-fb96-318e-8354-793bb5d7e622 | -6.84033 | -52.83002 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cddb0b07-3e2a-3932-9ab5-851270900869 | -5.32022 | -55.8823 | 2025-09-03 05:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2cd1065-a54f-3187-8dcc-9f3759c2e2e7 | -6.69418 | -44.18599 | 2025-09-03 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 292774e7-24b6-3f84-a07c-87b972078b0b | -6.85586 | -45.54425 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ac5bbaa-17ff-3d5a-9998-256dbb56a52b | -6.7971 | -52.82695 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f5f2448-4ec9-31cb-ba4e-09953ae9348a | -8.2107 | -44.80701 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 319a059a-2d5f-31fb-8166-bc262135402a | -6.7986 | -52.817 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e90494c-6faa-36e4-9a21-72ad206a71ea | -6.80886 | -52.82893 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1384eb7a-1a16-32ac-be3f-8dd566c472b6 | -6.79296 | -52.80103 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2105871-fd08-356b-b99c-fd6082a7cfcd | -6.33849 | -53.4407 | 2025-09-03 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46e9bc8e-7b26-3ed5-8387-534180698a34 | -6.52666 | -56.20649 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4dda228b-29dd-3b89-af4a-b2b481b993d1 | -7.71725 | -48.73048 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb47fe87-5776-341d-963f-75bd8e8c0df7 | -6.42997 | -55.61086 | 2025-09-03 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61400b45-4db0-3a12-891f-8f541aff9df9 | -7.71292 | -48.75473 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b360e08-b3ce-30f4-9913-91f07bcbcda3 | -6.02513 | -46.00846 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a3ebfbc-75ea-3540-9db5-c19ca8db8a04 | -7.90377 | -46.47947 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 300551ab-c66e-3c20-9cbc-38a24af81a2b | -5.92474 | -57.71741 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 98f1f95b-eec6-3a41-b1c7-f32611119ae4 | -5.87018 | -51.71733 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b9357c95-d52b-3142-951e-b1b73699b69f | -5.90476 | -57.73568 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |


[Clique aqui para ver as próximas entradas](README86.md)
