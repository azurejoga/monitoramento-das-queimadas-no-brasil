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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65824aab-ab53-3405-8cb6-a96a11d64978 | -3.25514 | -41.41834 | 2025-12-17 04:25:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0cfb40f3-e8b0-3763-8e19-97f6b28341bb | -2.23291 | -45.65601 | 2025-12-17 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f92b5fe-8c09-37c9-9df0-abd21763c9f6 | -4.39687 | -45.76454 | 2025-12-17 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92c5d633-2355-3f1d-8581-874bc3dcf4b1 | -3.49539 | -41.69233 | 2025-12-17 04:25:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3782e2ac-8003-3c16-863f-9d15d106d944 | -3.21021 | -45.57729 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a68c9e1-ba08-307e-aed5-8532aed9fb76 | -5.98503 | -44.593 | 2025-12-17 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99795880-43e7-3765-8218-80b96eef5b9e | -5.4752 | -45.4082 | 2025-12-17 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f671e2b-fdd0-32d4-b7c6-0386a312ccb0 | -1.76892 | -53.96373 | 2025-12-17 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aa386a9-27fc-387c-a411-3f0b4cd471f8 | -4.43 | -46.28502 | 2025-12-17 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21a28338-375c-31a2-b339-88dbe88f8ee4 | -3.33334 | -51.52668 | 2025-12-17 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bedc116-36d6-365b-9fea-55467e6a620c | -3.57822 | -52.11401 | 2025-12-17 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08ff6234-09fe-31b2-aed1-f520001292de | -3.04159 | -45.35378 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 766f9bf0-93c4-3c2e-8554-3c4a2a3b72dd | -1.41648 | -46.06894 | 2025-12-17 04:25:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 947ab651-044a-3592-9496-64a0b2faef23 | -3.25898 | -41.41895 | 2025-12-17 04:25:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ecdf3944-eacd-3e95-bc00-f1f95138ae0d | -3.74394 | -50.94027 | 2025-12-17 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 903439c2-d736-30f9-84e3-342c6e60dd1a | -1.72022 | -52.04716 | 2025-12-17 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18887c5f-2d22-3ba2-baee-34216c7fe085 | -4.14534 | -48.9209 | 2025-12-17 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f56a79d3-a57e-335a-b654-235ec6884af3 | -2.4842 | -49.31414 | 2025-12-17 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5a39425-2d70-3389-bc25-f5aab5813200 | -4.42945 | -46.28848 | 2025-12-17 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d54ebf5f-ed3d-3d16-858b-4646a1684115 | -5.47465 | -45.4117 | 2025-12-17 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3de6446a-1f3b-334a-ad85-0631421a6abd | -2.48571 | -47.76962 | 2025-12-17 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d0dfa76-9521-3c74-99af-5a28d58688f9 | -2.51397 | -49.10136 | 2025-12-17 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59e33895-e913-3148-9a15-7a7e97b9d5aa | -2.43355 | -47.19441 | 2025-12-17 04:25:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6015dbf7-6abc-3ae5-8840-203da39edebf | -3.03443 | -45.35619 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31f18e59-74f4-3922-a40a-4e911038822f | -2.99027 | -47.76941 | 2025-12-17 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83b1c6d3-8aff-3172-a715-19d8d176c600 | -1.41813 | -46.05852 | 2025-12-17 04:25:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2afe5fac-7a00-3bba-aa82-9d4d38540616 | -2.8993 | -45.58863 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f36c0cd-067b-33a0-bfa0-21a35dcb7ed5 | -3.844 | -47.06177 | 2025-12-17 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1960ca02-78a5-332b-98f0-fc5cc9fd7b3e | -2.93727 | -48.23356 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1eb66a38-9d7f-3a37-9f37-b0bbf227cfc2 | -5.57661 | -44.89285 | 2025-12-17 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 790d94d4-9586-30be-a8d0-cba10dedefbd | -2.69457 | -51.645 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1e4185b-5bca-3975-80d5-e65247b058fd | -5.57772 | -44.88574 | 2025-12-17 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27624f50-799a-388b-af2a-affe0a42388d | -2.43636 | -47.19862 | 2025-12-17 04:25:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59d3b238-688a-3dac-911e-2382e4716f6a | -3.02505 | -45.3512 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22c134e4-f73f-3bfd-b28b-b00730488b2d | -2.76989 | -48.57692 | 2025-12-17 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bcd645a-fd03-39b6-bf16-ccafe2161230 | -2.8938 | -45.01922 | 2025-12-17 04:25:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8135af6f-03d4-30e0-ab6b-6b2f66cd0d36 | -2.4835 | -49.31863 | 2025-12-17 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d09f32ef-f24f-3086-a801-9d6c6fc86c93 | -3.57068 | -45.33811 | 2025-12-17 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a03a802-6ff5-33b6-8803-881e574f6d0b | -2.05309 | -50.7219 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2fddab6f-727c-37d3-98bc-8ab79666d838 | -2.90645 | -45.58622 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e807f5dc-90ac-311b-8d9b-8589b33bfed1 | -3.03112 | -45.35567 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 370606bb-466f-3b09-a434-89320b074590 | -1.76843 | -53.96674 | 2025-12-17 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83e9ce48-f3c5-30e9-8849-f8d01f685e0a | -2.51094 | -48.1817 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f14c279-4f73-3fe1-b083-17c58719aa06 | -3.02836 | -45.35172 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8c67e62-ec20-3836-9471-0e15342c7627 | -4.30309 | -45.60468 | 2025-12-17 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3357a36f-f8d3-31a9-973c-0715c9b567f2 | -2.69467 | -45.70044 | 2025-12-17 04:25:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 173f5175-1a60-3745-982f-d8b32c60547c | -2.23237 | -45.65945 | 2025-12-17 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1debef3d-5930-3933-8098-182b0ccef684 | -2.6636 | -51.6442 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80836fb1-34ab-3a32-9f8c-036267158f54 | -2.44206 | -49.26616 | 2025-12-17 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92230906-adc4-3161-ad72-1bbc9405ec00 | -1.88794 | -47.29469 | 2025-12-17 04:25:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07ae0269-3df1-3939-b1eb-a80ad7d51ab3 | -3.11659 | -45.11456 | 2025-12-17 04:25:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a04e446-c467-3bc1-ba1d-a6c99c16aff2 | -1.72121 | -52.04962 | 2025-12-17 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6696dfb9-abf4-3f52-8e74-b99cb79dd894 | -2.41125 | -48.28439 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aefc6e7d-5b4e-392f-b7f4-5ec5b0c63433 | -1.90482 | -46.59102 | 2025-12-17 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f51a1aa5-3415-3ddf-93c3-11cabfbb3246 | -3.65696 | -47.54927 | 2025-12-17 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d84c58ba-712f-3804-90d1-a82a4ec4709c | -5.57363 | -43.59491 | 2025-12-17 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45e0bf9c-7b72-3dc9-a0b9-1d483a071ba7 | -3.03221 | -45.34879 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dae9b242-3366-3ebe-84d6-16e13d7b983a | -2.68673 | -52.07421 | 2025-12-17 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b34502e-b2c6-3db4-9e91-8ca642c431fa | -1.80762 | -54.05183 | 2025-12-17 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9278a852-650b-369d-b467-66efd643b0ef | -1.65889 | -45.89008 | 2025-12-17 04:25:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6315b56-d622-3185-9d80-3328fa771478 | -3.39816 | -46.19253 | 2025-12-17 04:25:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ec44a47-ffdc-375a-91d5-5cb1c85aab4c | -3.3586 | -44.56554 | 2025-12-17 04:25:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3f18d9f-d5a5-3d39-b2d1-8dfadf0b21c2 | -1.4577 | -47.15606 | 2025-12-17 04:25:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c90a1b4-41b8-3081-8e7f-28ec4620567d | -2.63468 | -45.67012 | 2025-12-17 04:25:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02dcedf4-ae22-3936-adb1-42c528d85ebc | -2.20274 | -45.7182 | 2025-12-17 04:25:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a9817dc-51b1-3f67-80c3-d645de552783 | -3.6462 | -46.8961 | 2025-12-17 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66f8f7f2-5456-3ca0-9a02-26ea0c533d5b | -3.64954 | -46.89663 | 2025-12-17 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9999d70f-8abf-391f-8e41-dd31b0fcd37c | -3.65579 | -47.55655 | 2025-12-17 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9767792e-6663-3632-9eab-ef6f8828a142 | -3.65356 | -47.54873 | 2025-12-17 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9185dd1c-e056-3c90-b351-0c56446d1eeb | -2.22643 | -45.71839 | 2025-12-17 04:25:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24bc60b6-c63c-3634-8489-d9d70204dd01 | -2.94192 | -45.6833 | 2025-12-17 04:25:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7876055-a6d8-38c4-9347-260bd7a98d2d | -3.4649 | -44.93067 | 2025-12-17 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8c20aa7-4527-3ca5-b2f0-6a69cfa283d3 | -2.93861 | -45.68279 | 2025-12-17 04:25:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85aaebb2-cd0b-360c-8ae6-842b2a1eb81d | -3.5597 | -44.88823 | 2025-12-17 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dae2b5ac-0369-322b-80ff-0e6435094186 | -3.58161 | -40.96806 | 2025-12-17 04:25:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2f3d0db6-107e-3c83-b4c0-6ad4b727fd75 | -3.58067 | -40.96497 | 2025-12-17 04:25:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 522e27ef-4eb6-358f-8b23-360af724a4d6 | -4.33455 | -39.14373 | 2025-12-17 04:25:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 31c500dd-83c0-3a94-8ef0-d57aec0897fe | -2.92798 | -48.22403 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41d9b827-0e24-3d90-8490-d89b3982d6e7 | -2.46769 | -49.03602 | 2025-12-17 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a106ecf1-d37a-3d99-adf8-584b1ce81952 | -2.61652 | -45.22717 | 2025-12-17 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0fba6f36-3793-3e2f-b89b-d33562658e5f | -3.05586 | -47.00328 | 2025-12-17 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9de8b63c-3259-34a1-bbbc-618eca61ac30 | -3.0289 | -45.34827 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb4c2ea6-7479-30e5-a90e-626e9f01b405 | -3.34022 | -41.79468 | 2025-12-17 04:25:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c8e5851-1be4-3f37-8cf1-74e3156ed6f0 | -1.80811 | -54.04875 | 2025-12-17 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f8b9356-b5ce-3bad-9894-5d9f70e32d0b | -4.42921 | -43.69292 | 2025-12-17 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffda5b2b-6337-3eca-b738-b0b666c0a8a7 | -0.93587 | -46.91082 | 2025-12-17 04:25:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a23e404-ad6a-3339-9a26-d72be5b73e46 | -6.31495 | -46.93189 | 2025-12-17 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fb06e5e-70ad-3976-8485-9760e4bfc8b3 | -2.43878 | -47.16168 | 2025-12-17 04:25:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9b55db4-1b0a-3c91-9419-df268c9e8860 | -2.66491 | -46.89123 | 2025-12-17 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4afe852-9194-3fb0-8cf1-ba0bc245442f | -4.43055 | -46.28157 | 2025-12-17 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb98a878-87e3-32bd-bf47-31db3f3e661f | -2.92446 | -48.22351 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f417eab9-e70b-3bfd-bf73-1847d2d275be | -4.29978 | -45.60416 | 2025-12-17 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76dc0bfa-62e7-3cab-b2ea-5015e59100cb | -2.66792 | -51.64494 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d88ba4d7-881c-3f22-aa7b-54fd465dca3b | -2.47053 | -48.11883 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61012a04-65c6-3fbc-8084-12c260a37bf2 | -2.36483 | -47.89223 | 2025-12-17 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8fec09c-eb32-30d4-9360-15263dc62f00 | -2.61983 | -45.22768 | 2025-12-17 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 83dac883-c76f-3733-b036-d662350f7fd6 | -3.32966 | -45.42365 | 2025-12-17 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c971164b-855b-3d2a-9748-3783050d821b | -2.93258 | -41.14492 | 2025-12-17 04:25:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 225e6962-0d41-39de-bdc2-0480cf28d94c | -5.98843 | -44.59351 | 2025-12-17 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9270f712-a79f-3101-951f-0eb2325a3a57 | -2.83948 | -46.69371 | 2025-12-17 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README9.md)
