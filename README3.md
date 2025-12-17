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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5284372c-e9e5-3165-aef8-ed126f25af51 | -1.4214 | -46.0774 | 2025-12-17 00:54:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a371a096-531f-31f1-a450-cf50eac39a62 | -3.2177 | -49.3577 | 2025-12-17 00:54:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2336cc66-086c-3c9d-8a0a-982d2ce4e454 | -2.6958 | -51.648899 | 2025-12-17 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dfa8947-a6cd-3b09-839c-89a313b2d75e | -7.2315 | -43.0928 | 2025-12-17 00:54:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5677a4c0-b41a-3e7b-996c-8af0e53e0b1d | -2.9097 | -45.597599 | 2025-12-17 00:54:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a4fe44a-962e-38a4-85c7-f7a464045ae2 | -3.312 | -45.518902 | 2025-12-17 00:54:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b0d9bf8-dd00-3637-8e2b-ca6f1325205f | -3.1246 | -45.120701 | 2025-12-17 00:54:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 713b3584-d18f-3a86-9a35-0310dc8e3a2e | -3.1112 | -45.107498 | 2025-12-17 00:54:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 448799ea-49b6-31c4-8705-29cbbd1dce79 | -10.9688 | -50.522701 | 2025-12-17 00:54:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ea8cf71-8248-3921-abd3-02282a3b7589 | -2.7945 | -51.405201 | 2025-12-17 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa74a6e-99e9-32aa-9f22-6b3746ecacda | -0.7015 | -51.992401 | 2025-12-17 00:54:00 | METOP-C | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0a17c7cb-7278-3803-951b-49864ebf0f8b | -1.4181 | -46.063202 | 2025-12-17 00:54:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 719ed5dd-4c9a-396d-a9b4-772bf6783d97 | -2.6942 | -51.641899 | 2025-12-17 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dad9ead-e368-367f-88f1-2641bcc0a7d2 | -2.6832 | -53.077301 | 2025-12-17 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01543dce-d465-3238-afb1-d5742f0432c9 | -0.6999 | -51.985401 | 2025-12-17 00:54:00 | METOP-C | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 18a92ba5-1779-312b-ac22-8284b8a4796e | -2.9942 | -52.363899 | 2025-12-17 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 380b4801-0be9-3564-b169-b5d10b14c201 | -2.9844 | -52.3661 | 2025-12-17 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 952e3c6a-fb95-305a-a038-ed0ba5975a4f | -3.0259 | -45.352901 | 2025-12-17 00:54:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 941cb670-0eda-34da-b8d9-f0a28661c431 | -2.6816 | -53.070499 | 2025-12-17 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1023d537-9975-3b3a-9125-a9f5c782c532 | -0.7031 | -51.999401 | 2025-12-17 00:54:00 | METOP-C | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 11162e59-75ea-3993-8924-57a8cb851541 | -2.487 | -49.318699 | 2025-12-17 00:54:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b21d7eff-a9ff-37e3-9118-b77e309b6bd8 | -2.485 | -49.3102 | 2025-12-17 00:54:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70bdd62a-d648-3952-9130-a8e43ba7a9db | -3.1149 | -45.123001 | 2025-12-17 00:54:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92eb4820-041b-3d2e-8a97-9d7e6985ce46 | -3.3824 | -45.986599 | 2025-12-17 00:54:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| edd531f7-e95b-31e4-a1e5-2be0264a349d | -3.2196 | -49.366001 | 2025-12-17 00:54:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21e8e34b-1727-3095-b43a-06424137fbae | -3.3336 | -45.437099 | 2025-12-17 00:54:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a639e82c-28e1-3ee9-834f-c9194c5ec2ad | -11.0938 | -48.256199 | 2025-12-17 00:54:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 884bf39a-8bd1-328a-b5cb-4e51d7adae35 | -2.8999 | -45.599899 | 2025-12-17 00:54:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b88b9aa-3100-35bb-a86d-2ec2a22241d7 | -3.0357 | -45.350601 | 2025-12-17 00:54:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8badf696-3375-3822-9bab-d26ce99b0aca | -2.2288 | -51.950901 | 2025-12-17 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41e626c2-c31f-36e6-b6e7-b423274aa88d | 1.32044 | -60.70932 | 2025-12-17 00:54:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 97dc48cb-fdac-3d9f-9dac-ae46f78c5c72 | -1.708 | -52.62561 | 2025-12-17 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1b1ebd17-152d-3176-85d8-583e9b32feb6 | -1.7652 | -53.96543 | 2025-12-17 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 835956ba-a07b-3dd2-a523-f826fb0d522b | -0.70635 | -51.99286 | 2025-12-17 00:54:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e5bfb844-156a-3177-b494-4de57b7c1de0 | -1.41845 | -52.57463 | 2025-12-17 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7d89cdb2-8547-3ff0-a8b8-29f5448a700c | -0.7084 | -52.00179 | 2025-12-17 00:54:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 26.8 |
| f584ed0c-6794-3c06-afae-55fe0fb69ada | -0.70629 | -51.98715 | 2025-12-17 00:54:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 32.2 |
| b7d8c32a-985a-3e26-9daf-77a8a4a65111 | -2.22864 | -51.94715 | 2025-12-17 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| d8662d6c-85a1-37e1-992c-61480989d8f9 | -1.77474 | -53.96406 | 2025-12-17 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4b6de257-df52-36be-8320-81c2755bedde | -2.17303 | -53.86579 | 2025-12-17 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a62a0f7d-6ad8-36d9-b038-0a96ff748f2d | -2.9875 | -52.3859 | 2025-12-17 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| b866d721-7d01-3dde-9922-ffa4635b46cd | -9.4165 | -35.9978 | 2025-12-17 01:00:00 | GOES-19 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 123.4 |
| 7d636a22-571a-3fde-b7f4-f0f4a9255da4 | -2.9876 | -52.3654 | 2025-12-17 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 11927d8f-b0d9-3265-824a-8a212dfd076d | -0.7077 | -51.9931 | 2025-12-17 01:00:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 3b4ba3a1-b39d-3032-921d-62952e8acc49 | -3.3316 | -45.423 | 2025-12-17 01:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 3293ae9d-9b8e-3090-aa76-cc62e8d322a5 | -9.3972 | -36.0011 | 2025-12-17 01:00:00 | GOES-19 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.7 |
| 696116fd-b362-3fac-b791-dc597b21df94 | -2.9875 | -52.3859 | 2025-12-17 01:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| ae1e274f-4a6f-3313-9764-788112487c49 | -2.9876 | -52.3654 | 2025-12-17 01:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b51087cd-4738-3013-a727-f4907de17700 | -3.3316 | -45.423 | 2025-12-17 01:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d1d8f7a3-039e-33e8-bb06-a06ff6d13849 | -1.8777 | -47.2835 | 2025-12-17 01:20:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8173c26d-0cfa-3215-bafc-f29481dd4a3d | -1.8961 | -47.3049 | 2025-12-17 01:20:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 984dc645-bd61-3456-a11d-a786235ba141 | -0.7077 | -51.9931 | 2025-12-17 01:20:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2284965f-25fa-3a1d-afd6-cc64315c5750 | -1.8776 | -47.3053 | 2025-12-17 01:20:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 33ab6522-d7f9-3619-85cf-1cf993ca0ed7 | -1.8962 | -47.2831 | 2025-12-17 01:20:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fac265a9-a2be-3ece-8f30-b55eb246ea6a | -0.7077 | -51.9931 | 2025-12-17 01:30:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 694dd989-f53c-3a89-b8c8-abd7a8a7c167 | -2.9876 | -52.3654 | 2025-12-17 01:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 88752593-90e6-3973-a8a1-c53d220baf3d | -6.5631 | -51.1126 | 2025-12-17 01:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 89f8531d-bbec-3446-9a5c-fe8a90420a69 | -2.9875 | -52.3859 | 2025-12-17 01:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 518e0cd8-6c58-3db6-bc1e-be83bedd007a | -6.5631 | -51.1126 | 2025-12-17 01:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a40e3804-a4d5-34b6-9649-16f3f85a4027 | -0.7077 | -51.9931 | 2025-12-17 01:50:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 93372bf3-dca0-3419-9ac3-6dfd716fbf0a | -2.9876 | -52.3654 | 2025-12-17 01:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c1979b30-f41e-321d-a528-6b400bc53233 | -0.7077 | -51.9931 | 2025-12-17 02:00:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f7614a74-8ba2-3a38-a03f-37b6d91a7ab4 | -2.6245 | -45.6729 | 2025-12-17 02:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3b37078f-399c-3423-961d-d37a76211079 | -0.7077 | -51.9931 | 2025-12-17 02:10:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f2213baa-28de-365d-8bbc-a75316dfab8e | -10.473 | -37.1256 | 2025-12-17 02:20:00 | GOES-19 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 113.0 |
| f7de0ca9-e845-30bd-90ec-17541d04f2f9 | -0.7077 | -51.9931 | 2025-12-17 02:20:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5099475b-f321-3c2e-aa54-a829edc5d28f | -0.7077 | -51.9931 | 2025-12-17 02:30:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 59.0 |
| d99a2bb1-cdc0-3dd5-967c-a8f57a76c5da | -2.6245 | -45.6729 | 2025-12-17 02:40:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5b25776a-60ea-33c4-b15e-7bd9fad07f91 | -0.7077 | -51.9931 | 2025-12-17 02:40:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d9f96824-e9d6-3bce-8ae8-19e789504146 | -9.66033 | -35.94588 | 2025-12-17 02:47:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3c018a91-de79-31a6-bb8e-6065dd8d8079 | -9.66165 | -35.93937 | 2025-12-17 02:47:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9a21bbe6-93f9-39cd-b40f-41df7c481d03 | -0.7077 | -51.9931 | 2025-12-17 02:50:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 59.0 |
| de9bb166-8452-34e4-8100-88cf840ff8b3 | -0.7077 | -51.9931 | 2025-12-17 03:00:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 477c6194-56a5-343c-8448-568a19aa8d57 | -0.7077 | -51.9931 | 2025-12-17 03:10:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 4d8293c2-b894-388f-b277-b0d8e9036761 | -0.7077 | -51.9931 | 2025-12-17 03:20:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 89822fb0-85f9-31a8-b83c-4e8d4a00656e | -4.99227 | -38.05793 | 2025-12-17 03:36:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60cb047e-ab4a-37b8-b5db-086606cde20e | -2.63162 | -45.66425 | 2025-12-17 03:36:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a1bb302-41b8-3f3c-8197-11af0f07944a | -1.42127 | -46.06815 | 2025-12-17 03:36:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 52fb8cdd-e216-311f-800b-a5cb530cdc90 | -4.33437 | -39.14892 | 2025-12-17 03:36:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 48906bf5-d0f9-3440-bb77-d308611d098f | -4.33502 | -39.14487 | 2025-12-17 03:36:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e5846b23-ddf8-345c-826c-d2284ea0ccb7 | -8.84096 | -35.67888 | 2025-12-17 03:36:00 | NOAA-21 | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a83745a6-2e80-37af-95c5-e7c0cde0add9 | -9.16588 | -35.69061 | 2025-12-17 03:36:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 0987b04a-2f4a-3ec8-a760-a90aa2140be4 | -2.94498 | -40.44428 | 2025-12-17 03:36:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 899fdb10-53d3-316b-a9cf-27d18cd82b5c | -9.16251 | -35.69007 | 2025-12-17 03:36:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 752cdc69-6d72-33aa-b764-ab5e33b37f64 | -2.93986 | -41.05695 | 2025-12-17 03:36:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c4a4b24e-ea53-3d01-a380-19a0c1d80bc7 | -6.814 | -39.50727 | 2025-12-17 03:36:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f017c99d-c8da-3ce7-992a-2aefac1c54ed | -9.1631 | -35.68646 | 2025-12-17 03:36:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 0371f5d4-8b91-305c-8673-3352754793a8 | -4.32911 | -45.88017 | 2025-12-17 03:36:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf600451-99ba-3010-af91-29fb9ef298dd | -2.9098 | -45.58803 | 2025-12-17 03:36:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ee6a1537-3a7e-317b-963f-10e8a04d2684 | -6.19103 | -43.40384 | 2025-12-17 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abcf77d9-c3a3-3ca0-8803-7ae0d7ac2a07 | -5.57529 | -44.89241 | 2025-12-17 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0cec486-5326-3ced-b86f-d59d30013b2b | -1.41536 | -46.06031 | 2025-12-17 03:36:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04c7566e-9a02-3450-9e88-98bd0e34db68 | -3.02585 | -45.35222 | 2025-12-17 03:36:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a22b48c-1460-36e1-9a1f-238b6391c7c9 | -6.70441 | -41.19731 | 2025-12-17 03:36:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f5057edb-e0b9-3f8f-b759-de3a247f2646 | -3.64686 | -46.89506 | 2025-12-17 03:36:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 894cfa4b-c246-3bbe-9e4c-6d3ec430b2ba | -8.5893 | -39.44497 | 2025-12-17 03:36:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2808da3f-b153-3099-a782-03211fc2fa5d | -9.16193 | -35.69367 | 2025-12-17 03:36:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e4190ad6-a577-30a1-b481-6b81d65a78f6 | -1.42238 | -46.06144 | 2025-12-17 03:36:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac95c639-d1a5-37fb-beb8-d1964adcd943 | -2.90535 | -45.59248 | 2025-12-17 03:36:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1dcf47ec-5016-3597-91a9-2e884d2cf9e3 | -3.95385 | -40.93758 | 2025-12-17 03:36:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README4.md)
