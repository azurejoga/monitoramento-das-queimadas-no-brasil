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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f91f406-5120-3647-a3bf-8a3dd66296b9 | -1.6478 | -45.86715 | 2024-12-29 04:42:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96fba86a-fbb6-3bb7-a994-ac07980f8b25 | -7.37794 | -45.83743 | 2024-12-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8333c26b-79eb-356e-b3bb-ab0f611b6a08 | -12.63955 | -38.56946 | 2024-12-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 62c24b1d-96b0-308f-bba3-5de3d178701c | -8.95884 | -47.30792 | 2024-12-29 04:44:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c685f8e-56a2-3206-a1c3-0f006609efa6 | -6.70949 | -44.32002 | 2024-12-29 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9427f01-7e57-3cde-bd89-6144cdb4b633 | -7.58601 | -46.46117 | 2024-12-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71c7efc8-da53-3915-8402-c31a37a2fee2 | -12.64031 | -38.56245 | 2024-12-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| be891268-41c9-3441-af3a-f852e37e2ea2 | -12.63673 | -38.56513 | 2024-12-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fd734ce8-8fc9-3c8f-b0fd-c4f8a261eadf | -10.43552 | -44.89304 | 2024-12-29 04:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d64cdeb3-c539-3cf0-87a6-094810b966c9 | -7.37519 | -45.83706 | 2024-12-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b9b9320d-bf97-3a2a-861f-1a9fec764e90 | -12.3887 | -43.67074 | 2024-12-29 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ecbda38-b1d5-3d5e-8687-990815e23d84 | -7.37382 | -45.83684 | 2024-12-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f78dc28-b690-3c1f-90a6-da1a7aaebd68 | -12.64384 | -38.56583 | 2024-12-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c34d86c8-5488-3c14-b2cc-48af9df3978c | -10.43616 | -44.88826 | 2024-12-29 04:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 108e1eb5-0166-37c7-9cc1-5de49516f68a | -15.09425 | -59.63058 | 2024-12-29 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6ed655b-a136-3b39-8b29-288c168e698f | -18.51205 | -53.39997 | 2024-12-29 04:46:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c418433a-edc5-3fa0-86e8-9d2eb6c5b451 | -19.08204 | -57.71627 | 2024-12-29 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 41fe5e95-7743-3403-b732-c3ac9ebe49b6 | -19.02225 | -57.6236 | 2024-12-29 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e69f8867-73ba-3861-9dcf-671debc4c0c2 | -15.09865 | -59.63153 | 2024-12-29 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3e4d756-dfcb-35dc-a0b9-95ab568d9b83 | -19.76373 | -55.41079 | 2024-12-29 04:46:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a5a3ce03-43e9-3193-9b9f-b1f504bca1e3 | -19.08455 | -57.71367 | 2024-12-29 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5293a5fe-481f-315a-b60b-0842d8e8cc27 | -19.08087 | -57.71291 | 2024-12-29 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 7b5a5736-fd2c-3712-b1aa-94e39f76439c | -18.78621 | -52.58437 | 2024-12-29 04:46:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd46f310-c7ad-30e5-8ba4-0d17ea680fcf | -18.78957 | -52.58494 | 2024-12-29 04:46:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3af7044e-ae6a-3f22-a75f-f3a2d56a000c | -15.09342 | -59.63507 | 2024-12-29 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65bb3011-4563-3177-a56f-9b9feaf6ab67 | -19.76435 | -55.40701 | 2024-12-29 04:46:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 94473716-b8c9-38e2-8f0d-3f56bf9f7d95 | -19.08284 | -57.71169 | 2024-12-29 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9e070028-07e4-3597-91ad-de3635328c04 | -20.47775 | -53.67743 | 2024-12-29 04:48:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59955766-380c-3d43-b1c5-9a17c060d4d9 | -20.99566 | -51.79305 | 2024-12-29 04:48:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 47efd8a2-0408-35ae-8ad0-48642fedafad | -20.9194 | -55.40866 | 2024-12-29 04:48:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b556271-cb82-3e76-9b1e-44183f7feef2 | -20.73204 | -54.41737 | 2024-12-29 04:48:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5364644-fe34-39ea-a4ef-7e861c2b6dae | -23.97999 | -54.19191 | 2024-12-29 04:48:00 | NOAA-20 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 82b7ab59-027f-307d-8500-b41f71dccc61 | -22.54076 | -48.81287 | 2024-12-29 04:48:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 656f437a-7f47-35cb-9d94-30849d22d615 | -21.39864 | -55.75984 | 2024-12-29 04:48:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f7a6a0c-a916-3ae9-a67e-37b99e0b1331 | -23.59216 | -47.43851 | 2024-12-29 04:48:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5a519262-b355-3a0e-979e-fa20dd035793 | -23.40527 | -46.55688 | 2024-12-29 04:48:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e0314bc-559b-3635-90b3-57319e4f73a8 | -29.58097 | -51.98645 | 2024-12-29 04:50:00 | NOAA-20 | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d2175e37-9023-3fe8-9820-012ab2399d09 | 1.03356 | -59.51637 | 2024-12-29 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5edfe5b7-6adb-3dcf-a99e-c1157ce52af0 | 1.10639 | -59.1989 | 2024-12-29 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 925c328a-cab7-39b7-8c2e-ca2bcff0c38a | 3.62887 | -60.51486 | 2024-12-29 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9af424cd-f0b0-3a74-8b45-5f1e1b58cdba | 1.57806 | -55.84236 | 2024-12-29 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d9ffd345-ea4d-3519-a9d3-b59f9e5369bb | 1.03434 | -59.73474 | 2024-12-29 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7b6600c-98b5-341b-b2de-83ca7fae6bee | 1.13848 | -60.08855 | 2024-12-29 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b7a6ad7-a2ec-3857-9b3f-e12adeb0c644 | 1.10996 | -59.19835 | 2024-12-29 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42488fc9-1f81-387c-884d-4f491a0f4bb9 | 1.10932 | -59.19429 | 2024-12-29 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f4035ff-f638-39aa-97dd-b50e30542a70 | 0.67951 | -59.8035 | 2024-12-29 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eabf0130-9530-326f-89c4-be658341964e | 1.10868 | -59.19024 | 2024-12-29 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c304755d-0220-320a-94ef-725d8048d6d3 | 0.6504 | -59.57201 | 2024-12-29 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61f34ff3-be1b-3ba4-ba6e-b13c55ff6bf5 | 1.57068 | -55.85217 | 2024-12-29 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bf72a99-9bf3-39a0-927c-eb7451221c9d | 0.65393 | -59.57148 | 2024-12-29 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5887c899-cf82-3852-88f3-fa13f4e229de | 1.52788 | -60.67455 | 2024-12-29 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d04415f9-f14b-3c41-8b07-85098e798525 | 0.9709 | -60.25117 | 2024-12-29 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1b89217-46d5-306e-b3ad-1acb49dd8490 | 1.57437 | -55.84726 | 2024-12-29 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9b9b4f7e-7d46-308d-8e00-ab28525b341c | 0.96689 | -60.24798 | 2024-12-29 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 884c6036-68b7-3948-8532-44753d42067f | 4.33046 | -60.6916 | 2024-12-29 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89f50238-ccd7-3f9b-b3dc-45650c934e6b | 3.57867 | -60.26165 | 2024-12-29 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7fa8e41-0f77-3e14-bde8-f00a919dea3e | 1.6274 | -60.33884 | 2024-12-29 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd5e8f76-740c-3e7b-a5e4-94d2f0a5e15a | 1.57001 | -55.84798 | 2024-12-29 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f93cb9d2-630a-32b9-977e-8bde869b8adf | 1.5737 | -55.84307 | 2024-12-29 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 882decd4-0356-3b64-8e57-e6f89fa3dfda | 1.57873 | -55.84654 | 2024-12-29 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7807132a-88a6-362c-8572-f6f146ab6249 | 1.10575 | -59.19485 | 2024-12-29 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bc03085-94c9-353d-a458-9e2039438c95 | 0.96747 | -60.25169 | 2024-12-29 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b1a47cc-06a0-3689-bbb4-1874c1509c69 | 2.85417 | -60.56704 | 2024-12-29 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4878cd18-5f17-3150-b7b0-a2c594bbdbe0 | -1.94512 | -53.34924 | 2024-12-29 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97fe1b5e-e01f-325b-86cd-121497a1a626 | -1.27325 | -53.45647 | 2024-12-29 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 590ae74c-3e32-3237-a1e2-5c2e66f24a75 | -1.89743 | -53.33078 | 2024-12-29 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f1f22cc-ad8b-3fe3-97f9-6a731aafafc8 | -1.27273 | -53.45991 | 2024-12-29 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29266f06-c911-3d89-8ee1-28272c32dc1b | -2.0725 | -54.70272 | 2024-12-29 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d701858f-ad90-3ceb-8ca2-3c1ea06ba1de | -2.38916 | -51.90723 | 2024-12-29 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca7b5328-f70c-323c-bbc0-79adfec93017 | -1.27812 | -53.46065 | 2024-12-29 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de2c135a-b6ba-3a1f-834c-9c292f193105 | -3.07971 | -54.62325 | 2024-12-29 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86b5a58b-7625-3697-9244-66e86fe6fa63 | -11.8918 | -63.97507 | 2024-12-29 05:37:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa12df81-a262-3e61-bf02-1bba4d29155b | -11.89234 | -63.97149 | 2024-12-29 05:37:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56d04d40-acde-3c64-ab9a-a8812047c53c | -11.889 | -63.97096 | 2024-12-29 05:37:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ac472f8-95ec-3138-b464-6402ea7fc4d8 | -11.90432 | -64.05066 | 2024-12-29 05:37:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8282de99-98e5-3294-88f7-cd49edee2278 | -15.09588 | -59.62711 | 2024-12-29 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e37da843-c29a-3130-a630-66116a7d5a33 | -15.09535 | -59.63138 | 2024-12-29 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d2260b7-ed16-37a0-9173-db008797e1cc | -19.08409 | -57.71579 | 2024-12-29 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 61a0de48-309d-384e-bf33-e9afb00b9577 | -19.08443 | -57.71247 | 2024-12-29 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| fd31a094-035f-316a-ab26-4fa6293826eb | -15.09968 | -59.63194 | 2024-12-29 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2761e779-4d7c-3796-b262-ee309422a163 | -15.09439 | -59.62482 | 2024-12-29 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcd0127a-b59b-3bcc-b78c-2275e2d9caec | -15.09155 | -59.62655 | 2024-12-29 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ca4adab-31c9-3f2a-9d09-a3ddc6600c8c | -15.09482 | -59.6356 | 2024-12-29 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8347f782-b2a3-375d-b1b3-6d2266885fe1 | -15.10021 | -59.62769 | 2024-12-29 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aebd08a2-9846-339c-b9ec-621791725c02 | -15.09327 | -59.63332 | 2024-12-29 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68387465-5591-33cd-913b-b1d338bcb92f | -15.09102 | -59.63083 | 2024-12-29 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a997930-910d-34cc-a8b5-37ef96e46af0 | -15.09383 | -59.62911 | 2024-12-29 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c82305a-b1b8-3b4a-9084-9907343acb84 | 1.57888 | -55.83823 | 2024-12-29 05:52:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9a2542f0-6a09-34cd-bbc8-c7bbbb58bad8 | -1.68881 | -45.83216 | 2024-12-29 05:54:00 | AQUA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 4f1f4abf-fa1e-32da-8845-09c09d6ab559 | -1.26824 | -53.45467 | 2024-12-29 05:54:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5940dca4-627c-361f-8a40-612704383526 | -1.27729 | -53.45602 | 2024-12-29 05:54:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8ffcf039-ab1f-34d0-93db-9cd936506709 | 1.11024 | -59.19221 | 2024-12-29 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b037f66-1f5d-3b7b-83ae-fbb354f21b85 | 1.57143 | -55.85295 | 2024-12-29 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bbca246-b2ad-3ff5-8305-8335c0d4d907 | 1.57428 | -55.84646 | 2024-12-29 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c5f2e47-6225-33ad-b3ce-f5ff72bdff42 | 1.56859 | -55.85333 | 2024-12-29 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a05877b-1a85-3699-9d39-e0b221aeb672 | 1.57051 | -55.84723 | 2024-12-29 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d28f5e0f-2601-3fee-a82d-bef16dd7976a | 1.10536 | -59.19652 | 2024-12-29 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d7bd576-9e17-3bae-9d1f-c4d541920217 | 1.11079 | -59.19566 | 2024-12-29 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95e2d421-e2b8-3d37-a3f7-924618b560e5 | 3.57557 | -60.26339 | 2024-12-29 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba12f9d7-6c44-37c6-8c40-cd7436a97523 | 1.57523 | -55.85217 | 2024-12-29 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README5.md)
