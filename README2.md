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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76b92d49-8037-34e9-a5ff-0f3a13bbf34f | -4.2409 | -45.7848 | 2024-11-29 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ce406e57-4f88-3641-b6e1-703abb6045c1 | -15.0867 | -59.6288 | 2024-11-29 00:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| f658a28f-0553-3392-b239-1d3780f3610c | -2.8851 | -45.5298 | 2024-11-29 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| ce74cb31-1ec1-3857-8152-75eadf13dd49 | -2.1351 | -54.906 | 2024-11-29 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 489715ca-bf9d-3916-a692-c26b4bb557fc | -2.6684 | -48.7767 | 2024-11-29 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 228.5 |
| 8ed45727-0b12-3ac1-b474-360ac8646cf4 | -2.8425 | -46.8193 | 2024-11-29 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e4de4bdc-6464-32b3-a56c-1ee381816272 | -2.885 | -45.5522 | 2024-11-29 00:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 02c67630-894f-3494-bdd0-581b47cedf82 | -2.8664 | -45.5528 | 2024-11-29 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 303.6 |
| 03c2e349-8bca-3b7e-9a2b-cee8faa1048d | -1.6081 | -52.2912 | 2024-11-29 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| fff713f0-62e6-3488-a47d-0769eb1b72c1 | -17.6453 | -57.5874 | 2024-11-29 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.8 |
| cefddc3b-cb59-3495-a5f2-e3a7f123d5b0 | -2.8478 | -45.5535 | 2024-11-29 00:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 6db8973f-967d-3b46-afd8-fdcf5a6c7449 | -8.1242 | -47.9843 | 2024-11-29 00:20:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| eff094b7-a4ca-3af1-880d-0ff64373c366 | -1.5897 | -52.271 | 2024-11-29 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b8dce19e-9a32-30cc-b3f3-0d8cbad7975d | -3.1818 | -45.6533 | 2024-11-29 00:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 8aa968f8-699f-3563-a146-d153cbce9802 | -4.6753 | -42.3799 | 2024-11-29 00:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 9f7ac45c-cd1b-3a55-85ba-83bbae901917 | -4.2669 | -47.6156 | 2024-11-29 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 01f33d0b-d09b-34da-b826-3ad310127c54 | -2.6499 | -48.7772 | 2024-11-29 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 233.0 |
| 651db2b0-c4b8-3e67-879c-22a2ebaa01e0 | -17.5805 | -42.7483 | 2024-11-29 00:20:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 7b49c0e7-511c-3dd7-ab04-1310fe2cab0d | -4.2411 | -45.7625 | 2024-11-29 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| ab954901-e829-368b-a807-34db76615266 | -1.5897 | -52.2915 | 2024-11-29 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 92adf547-8259-3c30-a69b-b43edac6b354 | -1.2556 | -54.5389 | 2024-11-29 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4fd06c74-8d92-3be6-b59c-8137fafb0002 | -2.8479 | -45.531 | 2024-11-29 00:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 193.0 |
| badf4c73-7249-3bae-b9d5-efe797c0dab4 | -2.8665 | -45.5304 | 2024-11-29 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 444.3 |
| 64fab034-fd0c-3d5e-943a-847ac917db18 | -2.6683 | -48.7981 | 2024-11-29 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 227.1 |
| 1d705c76-b4ec-31f6-a4cd-d5c182844d97 | -1.5868 | -53.8537 | 2024-11-29 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ade54778-9f2c-3c8c-8b33-f8317fe6b058 | -17.6457 | -57.5668 | 2024-11-29 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| f008844b-7d37-3e89-b6d4-858e40fddb9b | -4.2223 | -45.7858 | 2024-11-29 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4c1ce9ac-6bde-362d-80a8-a51284367e37 | -3.2739 | -49.8844 | 2024-11-29 00:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1f15042d-7d8c-3df0-bf50-e0c714761895 | -5.6291 | -46.9699 | 2024-11-29 00:20:00 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 778a80df-3828-3ec3-bbf5-242c1991353e | -8.1429 | -47.9826 | 2024-11-29 00:20:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a8f6ae01-6aff-3d22-91cb-54712807e4d3 | -1.6997 | -52.4535 | 2024-11-29 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 26361124-44a6-3c1a-b7d7-a70cd5b3e265 | -4.2669 | -47.6156 | 2024-11-29 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 5d66ad40-d987-38f3-920a-eea80bbc5510 | -2.6684 | -48.7767 | 2024-11-29 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 255.4 |
| 9b53b0a3-8729-33b5-a19d-ecf628a138c3 | -2.6499 | -48.7772 | 2024-11-29 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 257.0 |
| 4d31e999-28e8-373c-b78f-5f4e1d525173 | -1.5897 | -52.271 | 2024-11-29 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1db7a2d2-5a3b-383a-a974-7d6d2c395b78 | -11.4018 | -45.0746 | 2024-11-29 00:30:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| e52666ef-09d2-3934-9a5c-b59dd9836423 | -17.6457 | -57.5668 | 2024-11-29 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| cbdf9b5e-13b1-3a5c-82e9-f39c63d92d9b | -3.0544 | -45.0734 | 2024-11-29 00:30:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 6e1953e3-108a-3a89-bd31-c774353d6013 | -17.5805 | -42.7483 | 2024-11-29 00:30:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 115.9 |
| a06b7d21-f581-3284-aa55-c9ba8e50fcb4 | -5.0399 | -43.6205 | 2024-11-29 00:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 72624dd7-0cc3-34c6-bfe2-f5054067edd2 | -2.1351 | -54.906 | 2024-11-29 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 44da8238-c4fd-303f-a3a2-a822a073bfe1 | -17.6007 | -42.7434 | 2024-11-29 00:30:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 56.1 |
| b26fe10e-04f4-319c-8296-31ba3fe77a90 | -1.9688 | -55.4841 | 2024-11-29 00:30:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| da1bd5ab-6356-3c36-b9f3-d566acbea401 | -1.5358 | -51.6142 | 2024-11-29 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 18c8048e-9b82-365b-becc-a20dda936f91 | -2.6498 | -48.7986 | 2024-11-29 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 200.2 |
| e35fab61-d80d-3a4d-bc2e-02296ab58aa2 | -17.3873 | -40.4343 | 2024-11-29 00:30:00 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 79.3 |
| 333f6f2c-70ba-3513-a6bc-e9b50eb8cb6b | -0.2666 | -51.6248 | 2024-11-29 00:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 3978add9-0c75-3e1f-bd7e-b5a922aaa585 | -2.6683 | -48.7981 | 2024-11-29 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 175.7 |
| 9c757a49-b656-339f-809d-7eda106eda64 | -2.8795 | -46.84 | 2024-11-29 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 8d5dc966-aa4d-331f-aaec-1a8dd94593a0 | -2.1351 | -54.8861 | 2024-11-29 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 25f4b5bb-6ed0-30c6-88ed-49996d83b781 | -8.1242 | -47.9843 | 2024-11-29 00:30:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 64f89946-281c-30bf-9b36-62ebbbe00204 | -2.6869 | -48.7762 | 2024-11-29 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| da771d0e-0ab4-3157-b292-f02d6e2bbfc3 | -2.8425 | -46.8193 | 2024-11-29 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e3283e19-a255-35dd-b7e0-91a159ef5ee2 | -2.8479 | -45.531 | 2024-11-29 00:30:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 74a28098-5406-3044-a80c-b6aef4f1e5a1 | -1.5897 | -52.2915 | 2024-11-29 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 307ee8a8-5e72-399a-8fd2-41da457f5e8e | -4.4405 | -46.5754 | 2024-11-29 00:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 68db756e-1762-3315-a74b-3b76dbad1e6b | -4.2225 | -45.7634 | 2024-11-29 00:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 21001f60-15c5-3d31-98e6-70db15475786 | -1.5869 | -53.8336 | 2024-11-29 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 3f8f0645-e191-3a95-8c3c-7f3391a51e95 | -1.6997 | -52.4535 | 2024-11-29 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c626c6a8-27b9-3bcb-9c19-251188c64a7b | -4.2411 | -45.7625 | 2024-11-29 00:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| d3fd0a2a-eba3-3202-aa0b-52ad70beb902 | -1.092 | -53.3954 | 2024-11-29 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1c3f9266-b883-3aa3-a8fa-bcecc5499007 | -2.8664 | -45.5528 | 2024-11-29 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 245.6 |
| d927c16a-f5c4-3af7-9a21-4c87539ad430 | -1.6081 | -52.2912 | 2024-11-29 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8bb109dc-d888-3c34-883f-700ad481ddec | -3.259 | -53.6388 | 2024-11-29 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 954d3dc0-f6c7-3aa4-be24-a74fe82c9af4 | -1.5868 | -53.8537 | 2024-11-29 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 408e7303-f7c3-3c7c-b32d-5b9f784d5f5c | -2.8478 | -45.5535 | 2024-11-29 00:30:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 941042c6-a135-3274-b4ca-e9f90ffaaa15 | -2.8665 | -45.5304 | 2024-11-29 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 315.4 |
| a03a3174-fe45-3405-acb8-ee03950cbe79 | -8.1429 | -47.9826 | 2024-11-29 00:30:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 7f67f077-5248-3d59-9196-2119c9b692b3 | -4.6753 | -42.3799 | 2024-11-29 00:30:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 6322164b-6a39-30ab-86d8-b25c4720becb | -9.9279 | -36.422 | 2024-11-29 00:30:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.2 |
| b5c93ced-0ae6-3c8d-ba89-fc0da590ec1b | -1.2556 | -54.5389 | 2024-11-29 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 7d6ddded-a4ef-38cf-8207-c73ef11b0423 | -7.553 | -35.1143 | 2024-11-29 00:40:00 | GOES-16 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| b45110f2-1dc3-35ad-a053-3380379e16ac | -1.5897 | -52.2915 | 2024-11-29 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 29c2842f-8f0c-33b2-ba20-cf2912005be9 | -2.8425 | -46.8193 | 2024-11-29 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 811a28fb-4d0f-3484-bab7-9652f0ad7a4b | -2.8478 | -45.5535 | 2024-11-29 00:40:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 05f5fd9d-f077-3ae5-82df-46e0693d9ffc | -1.5358 | -51.6142 | 2024-11-29 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 7c6a0677-53d6-3f35-afe8-d2333b7fcaf6 | -3.259 | -53.6388 | 2024-11-29 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 42902cec-887b-35e0-91e0-f668deb0085f | -1.2556 | -54.5389 | 2024-11-29 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 443f1906-8cdc-30da-9ca9-fc9f20edde43 | -2.6683 | -48.7981 | 2024-11-29 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 238.6 |
| 45b87b82-0e3e-3901-9fe1-cf9115dd8396 | -2.1351 | -54.906 | 2024-11-29 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 54dee032-d087-377c-960c-9bca9b018890 | -2.1351 | -54.8861 | 2024-11-29 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 94a20493-a899-3fc1-ac41-9c3f8a05f3b1 | -2.6684 | -48.7767 | 2024-11-29 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 309.1 |
| fd39475e-395b-328b-9bf9-9304c2a58359 | -4.8527 | -41.2687 | 2024-11-29 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 2a13f8eb-c40a-3998-8cf8-ebe804419578 | -8.1242 | -47.9843 | 2024-11-29 00:40:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 854487a5-52ba-3466-ba0b-8c13d4ba8ce7 | -2.6498 | -48.7986 | 2024-11-29 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 25bdbda7-aa7b-3bea-8524-b0fc1f3375c2 | -1.5897 | -52.271 | 2024-11-29 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9a219d09-ff1d-3f95-bf0c-14d10953b782 | -17.5805 | -42.7483 | 2024-11-29 00:40:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 2a21a5c7-bd4b-396b-9cbf-e3e1b5810429 | -1.092 | -53.3954 | 2024-11-29 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 90b490d1-ad21-3700-9e32-402c38ef36af | 1.8583 | -55.8018 | 2024-11-29 00:40:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 9327c65b-b40a-36f0-b752-ad3c6d5ece81 | -2.8479 | -45.531 | 2024-11-29 00:40:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 1071bc4c-e277-31c2-9417-fdc58c6fcdab | -4.8529 | -41.2445 | 2024-11-29 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 02829b37-a2c4-3f2a-af4b-74f1d3f88d8d | -2.8664 | -45.5528 | 2024-11-29 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 203.4 |
| 8999b6b0-ecbf-3650-a315-fbd0a694a9ff | -2.6499 | -48.7772 | 2024-11-29 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 183.5 |
| 440ab6fb-4895-352d-a3c6-68d82efe5057 | -17.6007 | -42.7434 | 2024-11-29 00:40:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 64.9 |
| a2d5140d-7930-3553-ab14-0b5a4502920e | -1.5869 | -53.8336 | 2024-11-29 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b26699f5-6591-309f-b138-10801f0a32a7 | -8.1429 | -47.9826 | 2024-11-29 00:40:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 5fc9e5e0-a84d-39d4-bf61-57cb86c0e22c | -2.8665 | -45.5304 | 2024-11-29 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 308.9 |
| 0f452b23-389e-337e-b928-0b06dce6a3bd | -4.2411 | -45.7625 | 2024-11-29 00:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| a8db8036-858f-338e-b3f4-8dabda1913fb | -4.4405 | -46.5754 | 2024-11-29 00:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 1515769d-29e9-3e21-b404-bbc533ed6a7c | -17.58531 | -42.77194 | 2024-11-29 00:47:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README3.md)
