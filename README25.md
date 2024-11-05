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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a99b69e7-63b7-3f94-ae7e-565c865eeaa1 | -5.19822 | -48.24206 | 2024-11-05 04:55:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4092eef3-9de7-35bd-b9c1-f5eaea11044c | -3.54832 | -47.37148 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d927f82-9b97-326f-aa97-e16364aa423d | -5.09367 | -47.86897 | 2024-11-05 04:55:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6c8a779-b9d9-301d-a38f-cd9eb0d6fb66 | -5.80932 | -44.13484 | 2024-11-05 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4c4d2fb-dd0d-348d-a5d1-0902cfe1bf6c | -2.46328 | -48.48719 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f849742-1136-3274-935a-f547f692794b | -3.2156 | -53.09951 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| ba484db1-92db-3529-92c7-1f4d3d869674 | -2.28029 | -50.45432 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ac1b19a-1560-3b17-98ce-c8791b1cd343 | -2.84392 | -48.45652 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58493f08-efe5-387a-b81a-aad9be1c1198 | -3.011 | -53.23336 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fe7060e-c115-3e94-94c1-e2c8804e9062 | -3.54455 | -47.39658 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49703a2b-d450-3a5d-87c1-5c8c51b5f615 | -6.12963 | -44.70196 | 2024-11-05 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4dec92f8-d109-349b-80f4-750f1cc6415c | -3.89253 | -48.37136 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9d53427-333f-33da-8423-96d4d6291eeb | -5.12067 | -45.15934 | 2024-11-05 04:55:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a3fd1d6-2cda-3985-8f91-3a75614ff7fc | -4.26505 | -50.7244 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fe61f3c-c1b1-392a-ab09-fca82070c100 | -4.08011 | -48.3169 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2067e2b6-419c-3c40-aba0-6402bf190f0b | -5.2933 | -46.26105 | 2024-11-05 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca8b7ac0-7e5b-31bd-8f84-6f61adb6e7e5 | -6.11446 | -43.97537 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b1d259e-a118-3c06-9475-3dcc8cf11322 | -2.16308 | -50.51052 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6450b556-2bdb-3290-aaf1-a9d6bd30a832 | -3.22046 | -53.06851 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23a24ed1-0420-3a78-bf9a-fbf6cd1ff14f | -7.80573 | -46.57714 | 2024-11-05 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccdb2cf7-760e-3f20-9c54-44d1427ea2dc | -2.10172 | -51.09402 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 430c9551-b0f1-3ddb-980e-28b34abe5548 | -3.70486 | -47.62133 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98649ef4-d46f-346e-ac7a-6e215fa60980 | -8.49616 | -42.09327 | 2024-11-05 04:55:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 482a716d-a167-38da-9fd5-6382a999db5d | -3.54331 | -47.37511 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ee8fe4c-85db-3797-9cd2-d2576ae79478 | -3.53767 | -47.38301 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3210a48f-90e7-3066-89b5-91e9d6f9eb71 | -2.67142 | -48.51586 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92aa5d3c-6bfc-3819-a302-c4cb72413ba1 | -2.84058 | -51.34646 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f9b0138-c636-393f-938e-0a3fb5b82826 | -2.18388 | -48.86034 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af6cef9e-6f98-3697-aaa5-4784f4538eea | -2.83696 | -51.80014 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41633fec-dbde-3f0d-8dab-eb467fe32110 | -4.78222 | -48.90859 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89bea3d4-226b-318e-8e69-a644024c4d00 | -2.65425 | -48.57368 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8948b232-6a9d-3c5f-9c14-b1dfecf233bc | -2.18312 | -48.86515 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a19a6eac-41b9-3b31-a5aa-8947328d79a4 | -3.47559 | -50.38293 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58dd917b-ac1d-32e8-a6e1-6f90ad3ff3a0 | -3.09858 | -50.2608 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb734844-6800-328e-8201-81d76c3c7dbe | -3.09602 | -50.27747 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71d09a66-e640-3da9-978e-136fd9775ac5 | -2.53116 | -47.52594 | 2024-11-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50d0e3d7-0523-30df-baba-bdbbbcaa3100 | -2.6634 | -48.56718 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 802f8dd0-d022-3292-bf8b-d4530ec1670a | -3.04229 | -53.27351 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0da4f07f-dc2c-3002-81e2-e5b4e50dcad6 | -2.99377 | -51.05861 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b91e3866-228d-31c5-b151-d35640b2d8cc | -3.08481 | -54.51109 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1135cbdd-1f9e-3378-80cb-11c297861531 | -3.96269 | -48.15434 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e9e1570-773a-3d5d-90c6-072a5640d881 | -3.80662 | -48.8782 | 2024-11-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0a62d4f-1803-3ce7-b28a-3ccc7fd630e3 | -2.93098 | -48.62154 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9599e9e3-cf8f-3ed6-bc68-a415a2f5ec77 | -2.90213 | -48.6241 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb516dd1-ed0a-375b-8b10-aa9683ab8152 | -2.91489 | -49.33417 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68422342-fbfc-3dd0-b0dc-5c38c821666a | -3.9591 | -48.14988 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1de113c0-6a7e-34d6-9204-6c1846f35080 | -5.0653 | -44.23026 | 2024-11-05 04:55:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da9d5a34-289c-3ef9-a7fb-9b63ad57921f | -3.95854 | -48.15362 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7ab6132-5e66-3f16-b1e6-591d03cc39dd | -2.84687 | -51.35126 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59528ecc-7692-3e4e-9a0f-4f4ef1586d96 | -5.98737 | -43.43194 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d11f50c3-c5f0-33e3-bf85-d173e9c3de97 | -3.08592 | -54.50407 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0a51764a-b6b9-36e9-8f7b-2a88459f50e4 | -2.8399 | -48.4559 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98d0a9b0-f30e-3b91-91a4-c50d46d7654e | -3.10792 | -50.29633 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46cbabf6-6e6c-3afd-a276-6d41dd723a22 | -3.54238 | -51.47316 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fe55f0b-85cd-349e-adce-0612eed71621 | -4.60744 | -46.87106 | 2024-11-05 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f2602f60-024c-3fbe-ac8e-e64da7824b1b | -2.17149 | -48.86343 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 651393a7-7ceb-354e-9701-67b0b2ced5e2 | -4.5846 | -48.0698 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c3b152f-3916-3c26-ab77-313e96ff02e0 | -6.10875 | -43.97448 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d972ebfc-130b-31f3-b49f-e9e30d4017c6 | -4.42955 | -46.28712 | 2024-11-05 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 313fcd72-12c0-34ff-be6c-fd34abbcebe8 | -3.21452 | -53.1064 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 76c79fce-3a92-3b5c-b521-a0a617999e4d | -4.90273 | -46.71737 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d077bb4-6322-3613-9dc5-8997a0772b48 | -3.10494 | -50.29163 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c664541-9db3-3059-ae50-b68298194745 | -3.03936 | -50.41867 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dbb8b06-33ca-3baa-81b4-f5690b0cc30c | -8.49194 | -42.09454 | 2024-11-05 04:55:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 42ca509a-1e6f-3102-9573-4ab70a8d9c5f | -5.8337 | -43.6529 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5daea2a8-87f4-3122-b7ca-6a473b61ee57 | -3.71096 | -53.75077 | 2024-11-05 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bca6b9dd-d526-3c25-babe-b206b1fa6770 | -6.10928 | -43.97066 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dc838e06-9463-36f3-8495-fe9128255d7e | -2.82277 | -52.93945 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e15fa254-6ad9-3cb2-87ce-dbf716ea4500 | -4.41142 | -43.11374 | 2024-11-05 04:55:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4b86dca-9d0c-33b0-a40b-14273308fa23 | -3.48424 | -50.38287 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 789f1df9-7e74-35cd-82e8-fcd155762234 | -2.7145 | -52.95756 | 2024-11-05 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cc229cf-6842-34d0-a218-b3e92ae20e9a | -2.92035 | -49.34937 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1f6e9b3-c8a0-3c3d-88f7-164e10f7f1a4 | -3.27377 | -52.81487 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2083a13f-ca40-3d8e-9118-dd30edf083de | -2.88959 | -48.73405 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2f563e0-0c62-338b-8b2e-af1aaff5922c | -3.62391 | -51.12719 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da6a1373-21e1-3b85-ab49-81af5309d5c1 | -5.22469 | -45.80417 | 2024-11-05 04:55:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4963c81-d4f1-3724-8ca4-b4861d10aa2a | -2.17612 | -48.8592 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7537f86e-6d17-3903-bf3f-6d9ca372b3b7 | -2.82223 | -52.9429 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88e1e56a-d8ab-37f7-a59f-8676c2663822 | -2.91727 | -49.34414 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fd322a4-91e9-3f2e-82de-5172ad64bfee | -2.79585 | -51.47655 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbb513d8-ca6e-3560-97cc-5771befaffdf | -2.43649 | -51.57966 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd012794-dcd4-3161-8015-64bc4fd04514 | -4.26419 | -50.6107 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14e829ab-82a2-3862-afe1-ce3c2693557c | -2.22099 | -48.72594 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c2fe09a-be7e-338b-b07b-6d33098c8044 | -2.22177 | -48.72222 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 579674be-05d7-3168-9fbd-5f3a434b3cc7 | -2.4586 | -48.14474 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e59d4738-076e-3990-8120-15c67c16f504 | -2.39971 | -50.31005 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d16862c-6e67-37fd-b8bd-72011a5281c8 | -2.97757 | -53.27391 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 779bfc92-0d45-3d5d-9f0a-31e792549b33 | -3.10197 | -50.28691 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d615455-33a8-3513-829a-3e4153858dd9 | -3.1092 | -50.28799 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3566f889-4eb4-39cf-a00c-65119200100c | -2.89353 | -48.73465 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43b5d417-cdd8-3083-a94d-11bfa72bc3b2 | -3.55136 | -47.38094 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 4b508632-7faf-37b5-a4f3-eb45a85878cb | -4.38718 | -43.11451 | 2024-11-05 04:55:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e4746e4-f4da-309d-af1f-8aac6d26e0cb | -2.81946 | -52.93893 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47b10fe0-625b-344c-bfc2-dc3d4717093f | -4.71797 | -46.42337 | 2024-11-05 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9f6cfb2-efca-3174-a6b6-6250e8b9cce5 | -3.40592 | -50.28258 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ffc9828c-922c-3096-b306-5a67654b9e6d | -3.27349 | -50.2935 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25c19801-1b00-35ec-aa3d-e3f295fc78ae | -4.10168 | -50.23124 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b69f3a24-8a0c-3442-a599-026d0878aa95 | -5.98401 | -43.42896 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5c154fa-3a30-314b-aa71-5ec2f06f2cb7 | -4.61058 | -48.91128 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd2d46d5-cbf3-3356-8a89-339cd48cf6d7 | -2.82553 | -52.94341 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README26.md)
