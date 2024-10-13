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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4736beda-fb15-3daa-9140-6655c6933b6a | -17.1764 | -57.438 | 2024-10-13 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 06bd9738-cefe-3f77-8c00-48faf492aeda | -17.1761 | -57.4585 | 2024-10-13 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| c382920c-4e27-3868-94fe-de4219b48589 | -17.6478 | -56.2668 | 2024-10-13 04:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.7 |
| 5d86cde0-8607-3944-9505-a66c79e65f3f | -17.6474 | -56.2876 | 2024-10-13 04:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.6 |
| 9c98c392-e3e9-372d-af07-2ebd561a6f0c | -17.628 | -56.2694 | 2024-10-13 04:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| dce5abc2-cf90-3cbd-aab8-230b44a20646 | -17.6277 | -56.2902 | 2024-10-13 04:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.8 |
| f697b818-c270-38d3-84bf-325c1b965b3b | -17.6675 | -56.2643 | 2024-10-13 04:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| ac2df131-5fad-32fb-b7c6-6f32667e2f12 | -17.6672 | -56.2851 | 2024-10-13 04:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 2520d772-de4b-358d-afdf-63db9f8e965e | -17.9841 | -57.3612 | 2024-10-13 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.3 |
| ac193604-20db-3b56-a548-e125e25fadcc | -17.964 | -57.3843 | 2024-10-13 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.7 |
| f0d7eda9-2ed9-378b-90b5-d72692b9a797 | -17.9643 | -57.3637 | 2024-10-13 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.0 |
| 8ee0c995-0656-302a-b34a-92f36688f4c2 | -3.18481 | -51.24832 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 794e5761-ecc2-3007-a5ae-3a859aa75d20 | -3.09027 | -51.22556 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73769c00-a3a0-3793-88cc-317f6bdaa052 | -3.07234 | -51.339 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0ced258-420f-3e3d-b0f7-3356189d1a0a | -3.05423 | -51.45358 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 531be721-3a5a-3465-834f-c329acbe21b1 | -3.0445 | -51.13118 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4107595-2ffb-33c3-b85e-e34910d230fd | -3.04102 | -51.13063 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c87168a0-90ac-3372-b915-011c94710374 | -3.03984 | -51.47579 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1da50e1c-7913-3b46-9dc1-fd4b1ad401f5 | -3.03754 | -51.13009 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c52edb8b-5e0c-380a-a831-2ab598c932cb | -3.01809 | -51.20635 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fab5bb6-35df-38f0-8b69-368316441156 | -3.01746 | -51.21024 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d21c90fb-af65-39e5-8874-621529434ebc | -3.01683 | -51.21415 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 428066ca-0773-3007-92f4-556a651e40be | -3.01397 | -51.2097 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| daade428-f209-3b09-927c-af1030c0fc67 | -2.96569 | -51.03276 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2434443e-3ae2-328a-8ee8-ebc18a62235c | -3.03591 | -50.57085 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ac0b164-8fb8-3dd8-abc9-36b963f208e6 | -3.03308 | -50.56666 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 686f01a2-da8e-3a70-9616-f7e8bc96061e | -3.0325 | -50.57031 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 223170a7-0366-3c94-adc3-e11f6130f146 | -3.02968 | -50.56612 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 771277f0-2ed6-3c75-886a-c842acbdb6c9 | -3.02909 | -50.56977 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7525e97b-17ff-3539-93bd-48a35a256856 | -3.66402 | -50.94997 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3aafb14c-1557-313f-b830-a7f3993ca7d5 | -3.62009 | -50.91623 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfa643ee-9b10-3658-bc8a-2ef27186e7a6 | -3.47406 | -51.21307 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ca7b5bab-feea-3564-96d4-b956ad4c3163 | -3.3045 | -51.11227 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6c9ff04-ba62-3af7-b692-4cf2d34a9f8f | -3.28443 | -50.94935 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33e48cbf-5836-3637-b441-b379f55247a5 | -3.28098 | -50.94881 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdd49391-9ffd-3d3e-9487-b6635a14daa2 | -3.27386 | -50.77497 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3f4f8a9-4b12-3c74-a82a-f0cab94730d8 | -3.23739 | -50.84979 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87361ed1-15a2-3a82-9120-baf86114ca24 | -3.23396 | -50.84924 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a8128c7-296c-353e-9919-5f90323ba9f2 | -3.23336 | -50.853 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2520621c-66ec-35c7-847c-ed745bf1a5cf | -3.22248 | -51.28952 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc810013-45a2-34d9-9b28-bb2fdb7e998a | -3.20363 | -51.15213 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 786c1430-4d22-3b86-af75-b3726fb53062 | -3.19573 | -51.26997 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63957a75-9da2-3daa-af26-7c981e759a60 | -3.18543 | -51.24446 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 121b4456-0bfc-3dea-af06-d740dafdcf1f | -3.07586 | -51.33954 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07f26316-b215-30dd-bc62-f546aca73acb | -3.07296 | -51.33506 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2525ac19-941c-357b-85c7-6c9f9af4315e | -3.89888 | -52.20818 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aed61fd6-da37-3333-8b60-f9342cba5df8 | -3.8982 | -52.21239 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0020168-4744-31b2-8aa9-31ef0db1e5f9 | -3.89092 | -51.95902 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39183be0-c28e-349b-a9e9-0a59cb6c0e90 | -3.88707 | -51.93745 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 680e85c2-e80e-388b-aa91-71ee9a5c3d70 | -3.8864 | -51.94156 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26f7e65f-232d-3bcd-97e8-48596457d98f | -3.88216 | -51.94505 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd5b038a-3597-3baf-99fe-131cb86cdf11 | -3.87746 | -51.97389 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a33d69f5-66b5-3164-bc7e-d8ca7a97b53b | -3.87679 | -51.97802 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bdd7a83-2f1f-3cfc-9d1b-ff023e24ef8b | -3.86307 | -51.88874 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b24417a1-18f6-3674-bda1-abfbadd23c12 | -3.86098 | -52.18907 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5eacdea-3475-3e9e-a6a6-e6d9e67a7cc1 | -3.84457 | -51.75276 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3fee8e9-1c41-3eb3-aade-21387353d751 | -3.83219 | -51.87549 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a0628d4-9254-3359-aea6-423a82bc3641 | -3.77675 | -51.83331 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a277aaaf-49fd-3eda-9095-5cc8ae31f57a | -3.72952 | -51.81451 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f67af28-92fb-3726-afdc-d5740bb6759e | -3.68708 | -52.00996 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd2a2869-ca1e-3a57-ad7e-183bc231a4e7 | -3.64062 | -52.04536 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14f290ea-36a4-3d7e-8221-1def99b9bf6a | -3.64014 | -52.01592 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dec8cdc5-34e9-3156-bcc3-52fcef211e69 | -3.78858 | -51.98651 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5efc69b8-1895-3fc5-a80b-301587f6e3fc | -3.78791 | -51.99066 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 601a0ec5-9a93-3cf1-b597-0d9c2d0f6353 | -3.78313 | -51.32332 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e58e4d9-63a8-3266-adde-fa0a6c0e86a8 | -3.7809 | -51.31496 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58b08479-cad5-3a42-beb1-af40fec18232 | -3.78027 | -51.31887 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efa52559-8904-3cfc-82e6-56b960482ca7 | -3.77964 | -51.32277 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37d2b523-34c7-39cb-8cca-10b189d477b1 | -3.77758 | -51.83443 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87701dd6-53cc-35ad-b422-3759de9f2059 | -3.77401 | -51.83387 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3ea8a8d-67df-3ea2-9442-a9cfdd494a4d | -3.77261 | -51.97134 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc13b7fa-a8e0-3bb0-ac43-8536531d8f6e | -3.75422 | -51.88944 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3891fe58-6197-39c8-a369-da07df598110 | -3.75064 | -51.88888 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12107107-a7ff-3e93-a90c-5df7676334a7 | -3.72887 | -51.81857 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dcc67ac-3fc1-3a43-a8b1-d29a94fe64ac | -3.71495 | -51.79141 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 292a41fe-b691-3af7-8e32-c7ec3bb0d0c8 | -3.7143 | -51.79548 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6dccebca-c941-322b-8340-623f7a0e340d | -3.71139 | -51.79084 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ab19ac9-3a28-3e0c-b047-ebdcb0434276 | -3.71073 | -51.79491 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8fd9830d-ab6d-3117-9d81-578be9413910 | -3.70384 | -51.40665 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8acc8c06-88aa-35bf-a973-755e87e6155a | -3.69928 | -51.07887 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 146bb27d-80f8-3848-85fb-a25c5c168605 | -3.68286 | -51.07665 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f5f01b2-b427-3309-b02f-43c42494b011 | -3.6814 | -51.07993 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c8e92e0-ddae-32b8-ace6-eab559c0875f | -3.6794 | -51.07611 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0f3641a-c48c-3ea1-9559-f3362ea0ddeb | -3.64178 | -52.0156 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a04f2a04-dca0-3c4e-ba39-cc8f8a6b9aca | -4.04202 | -51.11189 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43654c43-3517-3d28-94e5-dfd48c10f86d | -4.04142 | -51.11561 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b79ace1d-7dab-391f-915f-d6125d4fc475 | -4.04096 | -51.09641 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e08a09fc-4129-351e-954f-0e1456a8e1d9 | -4.04083 | -51.11933 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2cb8006-e185-3a7a-ab39-fd4bda0d659a | -4.04036 | -51.10019 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 898d4bd2-0c72-3848-a217-ab662aab970c | -4.03752 | -51.09586 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bd05181-ea9c-3abe-a25b-9a9036023ce3 | -4.02457 | -51.00119 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95a5eb89-f7bb-3b7b-bb29-2ed5b0c860ec | -3.97296 | -51.0168 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb7f7a1f-120e-3df2-8cca-5e6af130df4e | -3.97235 | -51.0206 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 214775e4-2677-3bd7-b684-38010f25bc67 | -3.92526 | -51.22691 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 185543bd-001a-3f8a-86a7-31409b2efea4 | -3.92465 | -51.23073 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14d1126c-b085-315d-a18d-dc7af330201c | -3.9224 | -51.22257 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41a48661-10b4-34de-bee7-9cafe7250e3b | -3.92179 | -51.22638 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4116d12d-baa5-3175-902d-9986ece1b5ba | -3.92118 | -51.23019 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2b5286e-7889-3c10-8460-e9a2efee6f0f | -3.92056 | -51.23402 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 768b2b00-4164-37ec-997e-acdeb4a6ae3e | -3.91771 | -51.22965 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README49.md)
