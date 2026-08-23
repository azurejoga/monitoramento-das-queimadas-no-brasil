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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9ddcf17-3cd6-3b67-a72b-a0a4e75aa92c | -6.67388 | -58.72838 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 10a29036-ab25-33f7-ab48-9d2beead29e9 | -6.80781 | -58.67256 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 5ea0019c-98a9-3bca-aa00-afa93413d9f3 | -7.77778 | -61.43224 | 2026-08-23 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 29b2267c-821a-34aa-ac7f-96cfc0e4b13e | -6.80547 | -58.98505 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 5fd7b0b4-b998-3aeb-8cd8-50e7a9f74938 | -8.40349 | -62.68676 | 2026-08-23 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 92f0aaff-cf79-3feb-b1fb-4fb8703448b2 | -7.56256 | -61.18306 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b3db968a-ce6e-34f6-80e0-29622ea400cd | -6.97789 | -59.0784 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 598112d6-2a2e-3add-ae1b-f6a354aaf9a5 | -6.96342 | -59.07423 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.1 |
| baace711-88c3-3230-ad58-a06bd1cb3c52 | -6.97486 | -59.05807 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 506f53a5-6b2e-3f68-bdad-53548cffd624 | -6.80076 | -62.92013 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| ed3ed690-2dd4-3e91-bf49-7fc13e0dffae | -6.67731 | -58.75051 | 2026-08-23 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 189.5 |
| 1f718aa0-308c-33bc-92f3-a50e7a645808 | -7.5665 | -61.21035 | 2026-08-23 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 3d652cf8-efb7-34bb-9aea-40662a8d2fb0 | -6.79483 | -59.5977 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5a6792bc-86f4-358f-b4e7-53d16870b77a | -5.7758 | -57.57512 | 2026-08-23 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 60332926-6e6d-3eba-9f8f-d4aaca4879d0 | -8.40491 | -63.80122 | 2026-08-23 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d597822e-1926-3d82-8feb-6b2eaccde8da | -9.04951 | -65.44897 | 2026-08-23 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6ba90717-765a-3194-a3d3-06a866648d4f | -6.12101 | -57.83654 | 2026-08-23 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 242.3 |
| 33db348f-fa31-3b24-9e4c-2aff7eaf37ff | -7.78832 | -61.43062 | 2026-08-23 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 16af80a3-9350-3f22-be27-1a375a1ae13e | -6.95371 | -59.09644 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 1f0315e1-a571-3422-9dd4-d33e089ae37c | -6.77758 | -59.75713 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 32c5a8c4-d816-3816-b736-d2543cb5054b | -7.44337 | -59.78576 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| e9616a71-3258-3f2e-97f4-a915dd1a913f | -6.79392 | -59.42433 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 2d0318ea-6d91-399a-a48e-8ea78d44717c | -6.7976 | -62.89864 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 515d9db2-ca96-303f-a8dd-104c350fbc86 | -6.1225 | -57.83088 | 2026-08-23 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 262.1 |
| 4aeff441-271b-32e8-b8ae-1f5b52085f66 | -7.66476 | -63.32514 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2c96198-de51-3cea-979a-c927c58d0712 | -6.93603 | -59.06409 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 848dbbcd-5d19-3d6f-a53b-4cd2e6bc2444 | -6.88569 | -59.42292 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 42227b04-8bb0-3ecb-9c8b-f1a5b47a3821 | -7.86438 | -63.76219 | 2026-08-23 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3ab4ff4c-b9da-3467-bc5c-5fb233fb3ae2 | -7.66618 | -63.33516 | 2026-08-23 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 08db4357-3b9d-3e18-ba63-2173083c3be8 | -6.80726 | -59.59589 | 2026-08-23 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| aec91c6b-8585-308b-974b-98f8c6d593bb | -6.13553 | -57.83442 | 2026-08-23 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| f66af37a-3030-33d0-9074-3bc729b993ae | -8.17796 | -63.89148 | 2026-08-23 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a896324-100f-3e11-bef4-fd59ad29f979 | -7.78345 | -61.43723 | 2026-08-23 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e271463e-6a59-3f0c-8dd4-428c834470c3 | -5.7615 | -57.5807 | 2026-08-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 96ee2c66-6bb5-3f72-b018-c8e6ca88b784 | -6.9699 | -59.0658 | 2026-08-23 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 7e8fa1df-bd1b-3189-b5dd-d0c9e5b5bec2 | -2.982 | -48.9598 | 2026-08-23 01:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| c7154dde-3401-36ed-ab2d-2530062e9e98 | -6.8188 | -59.6696 | 2026-08-23 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 796bba99-1e86-3b62-b5b0-35d6750cdcd5 | -9.1909 | -59.4619 | 2026-08-23 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c21f3d98-fcff-3718-9882-fda0322c0a25 | -5.7799 | -57.58 | 2026-08-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a833c763-6eaa-3060-81fd-60891c2cbf4d | -21.4532 | -46.1613 | 2026-08-23 01:10:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.0 |
| 661b831b-807d-386f-aaa5-35ef40353a6d | -6.8008 | -59.5934 | 2026-08-23 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 1f41fb0c-d687-3f7c-b458-e0c6f75c385e | -6.1286 | -57.8198 | 2026-08-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 32c16112-9951-3c8e-859d-9bdf8c5c0614 | -10.7982 | -50.973 | 2026-08-23 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 795d38fd-1cb5-355e-9d4c-b9eed3361189 | -6.1925 | -53.5231 | 2026-08-23 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 6ddc21e9-e66a-3b3e-9b00-a063f1854484 | -6.9698 | -59.0852 | 2026-08-23 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 2abbac60-bee8-3f59-964c-265d7ece6b87 | -6.5487 | -58.522 | 2026-08-23 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 9bb0a832-5a70-3d66-a272-24d7992c0559 | -21.454 | -46.1371 | 2026-08-23 01:10:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 154.5 |
| 196bad32-f155-3144-ade1-290b4b62abc4 | -3.0005 | -48.9592 | 2026-08-23 01:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 187.8 |
| b4ff1831-e840-32a3-b3ed-911aefce6707 | -21.4748 | -46.1316 | 2026-08-23 01:10:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.8 |
| 96a6ab57-98da-35a9-b56e-30ee9acde168 | -9.191 | -59.4425 | 2026-08-23 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 071dfa40-247e-3110-a177-31eb7b29178e | -12.2613 | -43.1845 | 2026-08-23 01:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 72.1 |
| bc2bf7ba-3ccf-3480-bf20-c65877b57fdb | -10.8172 | -50.9711 | 2026-08-23 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 604752f8-1b5c-363f-a15e-7816d54fe545 | -6.9513 | -59.0859 | 2026-08-23 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 3b3f69f6-7b91-39c8-b5cb-4efaa0cd3d8d | -10.8358 | -50.9903 | 2026-08-23 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 52df5948-ad72-386c-ba85-43fc5c762849 | -6.8027 | -62.9024 | 2026-08-23 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 70211a1d-b8b6-3a9a-97b4-a4b814c9e17e | -6.1285 | -57.8393 | 2026-08-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| fda74cf3-444a-34d5-8dee-0f39043ca450 | -6.8061 | -58.6663 | 2026-08-23 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 5cd38175-ed38-3b0b-8623-7e41dbf01bc6 | -10.8169 | -50.9923 | 2026-08-23 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| fd9b6a94-3892-368f-a08b-dea3859bf522 | -10.8361 | -50.9691 | 2026-08-23 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 148.9 |
| e0bb48b3-ee3c-3d5d-99e5-8ce47cffd984 | -5.78 | -57.5605 | 2026-08-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 9e3bb7f4-3598-3bfe-8ff1-5920217b2742 | -6.8062 | -58.6469 | 2026-08-23 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 473195db-cd64-31d7-88de-d1d47d7826fb | -6.9514 | -59.0666 | 2026-08-23 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 4762f93d-6527-3f6f-8677-8a7bd403deb5 | -7.5669 | -61.1906 | 2026-08-23 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b0c02df9-a0e2-3510-97aa-037d4c4a2edd | -6.68 | -58.68 | 2026-08-23 01:15:00 | MSG-03 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0379c139-d278-30c9-99c6-424b26e915a5 | -6.68 | -58.75 | 2026-08-23 01:15:00 | MSG-03 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd219a3-14c3-3393-a30b-1b7151be9773 | -9.1909 | -59.4619 | 2026-08-23 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 06804833-54d8-3b7e-a811-06e3faa5b99d | -6.8008 | -59.5934 | 2026-08-23 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| dfd7277d-22af-3912-ac31-b524c327299b | -2.982 | -48.9598 | 2026-08-23 01:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 8686f046-74e7-3727-b1c4-4421d1551953 | -6.5487 | -58.522 | 2026-08-23 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e9ed48fd-2e16-306d-bb33-4349b99babde | -6.1285 | -57.8393 | 2026-08-23 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1645c777-719f-3a84-a371-a5ae51b25f25 | -21.4748 | -46.1316 | 2026-08-23 01:20:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.7 |
| d471f27d-a889-3559-9eff-440841de7e0f | -3.0005 | -48.9592 | 2026-08-23 01:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 205.9 |
| fe3981e5-4637-3eda-8e16-5b44757e5a68 | -6.8061 | -58.6663 | 2026-08-23 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 8c8e816b-7987-3ff6-b0f2-75da969fd4a9 | -6.8062 | -58.6469 | 2026-08-23 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 6c4f8f23-64de-3cfa-9063-43fd5e92dbd0 | -6.9513 | -59.0859 | 2026-08-23 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a939ec12-8d82-3607-a609-fe28701cfa52 | -6.8026 | -62.9212 | 2026-08-23 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 389cf05b-a6ea-351f-8961-afdba1acdb3a | -9.191 | -59.4425 | 2026-08-23 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b5d15504-fb19-3883-92cc-8d60bdc9838c | -6.9698 | -59.0852 | 2026-08-23 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fe62876e-cc57-3dcb-8092-174996a8b26a | -6.8027 | -62.9024 | 2026-08-23 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a831f8ba-0e4b-3744-85d3-76ea3572c682 | -21.454 | -46.1371 | 2026-08-23 01:20:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.1 |
| de0d8c2e-7344-335e-9a16-ba93d7d24b86 | -10.0667 | -46.4544 | 2026-08-23 01:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| d432b74c-25cd-3d74-b1b9-dc5f66324056 | -6.9699 | -59.0658 | 2026-08-23 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.7 |
| dfeb78a4-894e-3af0-9202-9775e6367c4d | -6.1925 | -53.5231 | 2026-08-23 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f1e49ba9-1244-33ef-a509-d8a917bc793c | -12.2613 | -43.1845 | 2026-08-23 01:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 76.3 |
| fadfe511-a9de-3007-8287-4d7b23acfd15 | -6.8188 | -59.6696 | 2026-08-23 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 5c791a49-f3c6-390c-ae7b-2441b3aa0c9e | -13.1886 | -51.4447 | 2026-08-23 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 5515f7ea-5199-3c60-af7f-f0b492124a9a | -10.8172 | -50.9711 | 2026-08-23 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 5811a2bb-a14d-394e-bd09-d688f189c464 | -6.9514 | -59.0666 | 2026-08-23 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| e16e4897-80d1-30a6-a74f-1e2647d1b9a9 | -6.1925 | -53.5231 | 2026-08-23 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 1e49204c-0b55-38e8-9802-569952a41a09 | -21.454 | -46.1371 | 2026-08-23 01:30:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 134.9 |
| da567418-282c-3936-8d3f-f7fac6590b4a | -6.9514 | -59.0666 | 2026-08-23 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 85f0ffde-29a2-3e63-8894-eead10732d88 | -10.8172 | -50.9711 | 2026-08-23 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| da0a97d9-3053-36e0-a6e1-cde910c38757 | -6.5487 | -58.522 | 2026-08-23 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 76e16377-67e9-3452-9d4d-9e73e47a9436 | -6.9699 | -59.0658 | 2026-08-23 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.9 |
| cc977e57-5621-3641-a829-db2094c0c1c4 | -10.8169 | -50.9923 | 2026-08-23 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b3bdc20c-bda6-3981-a4ce-36a574a99b0d | -9.1909 | -59.4619 | 2026-08-23 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4a06f654-7cf5-3a66-93b5-59dbc808bcc5 | -21.4532 | -46.1613 | 2026-08-23 01:30:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.0 |
| b19d9ab6-33ff-3a08-bd34-b9a3e7512354 | -2.982 | -48.9598 | 2026-08-23 01:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 155.0 |
| b30c1845-a031-3f87-845a-11e2c995f6cd | -6.8188 | -59.6696 | 2026-08-23 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 4f58a08f-5298-36f5-b55a-785942218673 | -6.9698 | -59.0852 | 2026-08-23 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |


[Clique aqui para ver as próximas entradas](README6.md)
