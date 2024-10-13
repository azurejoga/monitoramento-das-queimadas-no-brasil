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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2b016a0-67ea-3191-a153-404fd9ea68c9 | -11.89044 | -56.20788 | 2024-10-13 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76783653-72ea-323e-8b6c-df09d880c035 | -11.88879 | -56.21856 | 2024-10-13 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75d5d69d-398d-3d02-80e0-f4237f6efb52 | -6.45627 | -56.11674 | 2024-10-13 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0ebd625-4bba-3c2a-903a-196c16ce22af | -9.33974 | -57.60403 | 2024-10-13 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17ba37b7-dc85-3dbf-a7f8-170ebd5fa16b | -9.33916 | -57.60765 | 2024-10-13 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e89e7563-448b-33de-8555-5bbad3ad96d6 | -10.58136 | -57.51428 | 2024-10-13 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9085b7c5-bc32-37c7-a757-b5fd088f05ed | -10.12436 | -57.76802 | 2024-10-13 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6845a627-1e10-32b9-b85d-bae73b65f258 | -9.95504 | -58.01357 | 2024-10-13 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4369ad00-67d1-3c1c-a889-9dad9242fd39 | -9.92917 | -58.10759 | 2024-10-13 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91afc748-b6a4-30bd-8290-4cd58c1008f6 | -9.68012 | -57.20445 | 2024-10-13 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b069134-eca3-3a11-8012-75f4d6135af6 | -9.67621 | -57.20744 | 2024-10-13 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe41dece-7f5d-33b9-bdbe-3894480a0556 | -9.67564 | -57.21098 | 2024-10-13 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49bd8785-0a92-3783-ae38-4daf431e8a05 | -9.6723 | -57.21045 | 2024-10-13 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da57a01f-60a2-3f6f-90d2-e4bacd36e34d | -11.89835 | -57.46948 | 2024-10-13 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05839649-4e0f-39dc-8a85-839fb842e638 | -11.89559 | -57.46539 | 2024-10-13 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4e979f6-db08-3e46-ac9e-0177d34beffe | -11.89502 | -57.46894 | 2024-10-13 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ec4177e-43a2-32a6-bd62-909faefa3ad7 | -11.89445 | -57.47248 | 2024-10-13 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c56cc307-cd01-3f5b-bb8c-bc65124b9347 | -11.38598 | -58.32533 | 2024-10-13 05:04:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cde352ab-0c57-3a03-83ff-cbc3f28c5a85 | -11.38538 | -58.32901 | 2024-10-13 05:04:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6b90e25-f51a-3252-812f-0b788220ddb9 | -11.3786 | -58.32786 | 2024-10-13 05:04:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36f6aa19-6cc6-3417-9846-a7cd32d1ca5a | -11.378 | -58.33156 | 2024-10-13 05:04:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f0387b7-6ab0-33cd-8e1d-6e9e757ed9cf | -11.36693 | -57.27766 | 2024-10-13 05:04:00 | NPP-375D | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 220c584d-885c-32de-a124-0fd7d85f05df | -5.72356 | -57.53988 | 2024-10-13 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5b34a44a-e440-3cf8-b5eb-ccca75ab96d4 | -6.74856 | -58.88107 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ebfebeb-ac67-3204-988a-b5488e6b94ea | -9.12172 | -59.02006 | 2024-10-13 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3db28df0-f266-3725-bf6a-49e215b7ab54 | -10.65934 | -58.82082 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 932ba086-0e14-370a-8219-5936b0bb3779 | -10.41502 | -58.75015 | 2024-10-13 05:04:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cee051f1-8ffa-3f67-8822-1839e5beef9e | -10.41156 | -58.74955 | 2024-10-13 05:04:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36314054-10a3-3312-ad63-281fbe58b863 | -10.35183 | -58.89451 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dae79569-38b9-32fc-b621-e2f65be23561 | -10.35118 | -58.8984 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a04be76-3514-3517-a55d-49a680df910f | -10.05516 | -59.00424 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2f0e8b2-c36e-38ec-beac-171be3a080f2 | -10.05451 | -59.00817 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47daafd1-09de-3c94-b3ee-780fc16e8a29 | -10.05165 | -59.00365 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 993b6358-5d71-39c5-a9a4-8978ce0efca2 | -10.051 | -59.00759 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e315089-9dc7-3799-8b75-117b68bcf7d2 | -10.0444 | -59.45759 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fea201e6-7f9e-3756-a046-ed339f69845d | -10.0437 | -59.4617 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cefc37d5-0838-3bc3-9f59-2dde263af4af | -10.04081 | -59.45696 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b13db783-0b3d-37a2-af1c-8c18fb9c8d11 | -10.04012 | -59.46107 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a38be24c-0aea-381b-97c1-6bb5ef3a22f8 | -9.78163 | -59.21555 | 2024-10-13 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8ef766b-4429-30d8-acb8-eddd95b2ecd0 | -12.31243 | -59.15772 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 154149a0-530e-3994-b0f9-5269a35c63cf | -12.31115 | -59.16545 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 273ca753-9e9b-3d2d-81db-860405306357 | -12.30897 | -59.15716 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f379afe2-154a-3624-9783-b69685be301e | -12.30833 | -59.16103 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20599707-2d61-3d7a-8adf-e4c499f26fad | -12.30769 | -59.16489 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 261932b6-3759-3ad9-bf28-dcf900918bcd | -12.3055 | -59.1566 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1edb9927-3178-3bd2-be5d-528da1d96476 | -12.30486 | -59.16045 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b8a8af8-9401-36ff-8a2e-f56c8efc4f7f | -12.27165 | -59.21037 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 02bd4778-7f3a-35d4-a790-062ecbd0bdf1 | -12.26818 | -59.20978 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec7bf494-399f-31f1-8d02-d02186e2771f | -12.26753 | -59.21363 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fcb7878-1694-3bbb-bd77-2bcae3053cf4 | -12.26689 | -59.21749 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c429ebe-0f4a-30f5-8db6-33a2ede9c519 | -12.26406 | -59.21306 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6c8896c-0f13-3d96-89e4-4fcae9f7f899 | -12.26342 | -59.21692 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6e48789-c0cd-38fd-8efb-ae0df9ffcd64 | -12.26148 | -59.22852 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a868c21-eadb-3cb3-9fd9-4ac6867edaa6 | -12.25801 | -59.22794 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5fdd207-c278-345f-9e8c-f914d07003fc | -12.09879 | -58.71304 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b4d9a39-f6f5-3138-9acb-8d9853a064c7 | -12.09758 | -58.72052 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75495e9e-be75-3189-9596-422aea4ba425 | -12.09697 | -58.72425 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae5e04a8-d521-334e-9eee-67041bc7a736 | -11.8943 | -59.02156 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55b30ca0-69f8-3045-8532-2ba383cc4686 | -11.87605 | -59.04596 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7d5e4c9-adb6-36ab-8ea0-5c862ec21dda | -11.87542 | -59.04978 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ffd10609-3c5c-3634-abcf-755e14874cd4 | -11.8615 | -58.89841 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d36a3e45-1cdb-3a2d-b0b7-74c2021ce1fc | -11.8524 | -58.87412 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d49be1b-be97-3073-9a55-90185b39e04c | -11.84712 | -58.88484 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f1b2210-8bbf-3a39-b701-4cfc068e2c19 | -11.84368 | -58.88422 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8329ce5-90b3-3910-8742-eca6f0300256 | -11.84307 | -58.888 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c69048e0-9335-35ed-8384-2625b2a1ff9d | -11.83957 | -58.84447 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96106eee-bb47-3493-b7ff-8221bad59fec | -11.83895 | -58.84827 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 640375d4-5c28-3a4c-9445-3131a33929b9 | -11.83676 | -58.84005 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 549c6541-ed86-3ed5-aa15-640c67e4202c | -11.82803 | -58.85023 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b4349bf-d3e8-392d-a34d-6e330214c6dc | -11.82741 | -58.85403 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4889ef4-c861-3525-94b3-9e2446d84836 | -11.72281 | -59.16418 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8eac3faf-9ab0-3c44-9545-b73c601ac082 | -11.72217 | -59.16805 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 310d1312-a1b6-3fa7-9507-b48c61e7d133 | -12.15862 | -59.88418 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 980b4a02-9d86-3a7b-b8e8-d29c33ad4296 | -12.15219 | -59.71097 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5170f349-9826-3b77-85fd-a74b321b403c | -11.76441 | -59.95774 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9467eec3-ffc4-3518-a82d-cf875f2fb16a | -11.7637 | -59.96196 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 343dee21-1a1f-3164-9ff4-2db8d8bc637e | -11.66271 | -59.89431 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1ba417b-9f8f-3b48-b023-7ca728633918 | -11.65842 | -59.89786 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91a6fdf2-e1cd-32b3-863b-1cb4885d5f99 | -11.65773 | -59.902 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f516581-9458-3645-bd54-bb4aed7f0b87 | -11.63148 | -60.01455 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cc569e1-afed-3633-a3ce-c3e899e69aea | -11.58743 | -59.98907 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 620b1024-8aa7-3621-a1b1-0445a5f420e3 | -11.58672 | -59.99323 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adc8e060-04a6-30dd-be5d-3e0514fb8ede | -11.58453 | -59.98426 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6edab51-5fa5-3981-9ec3-9af0e08129d7 | -11.58383 | -59.9884 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93b5615e-e54f-3fef-8a00-43fad3f91fd3 | -11.5831 | -59.99264 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3782201e-92c0-3ea5-96cf-55cfabd87ca6 | -11.58238 | -59.99688 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39b4d055-1ab4-3a21-850f-6c0f3fb02a1a | -11.57018 | -59.9786 | 2024-10-13 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e58ef4d-d6d3-3e83-82d5-0d4c8282e6c1 | -12.66228 | -59.83657 | 2024-10-13 05:04:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fe0bd20-6fd9-37a7-8bf3-c7395558e3cd | -12.65874 | -59.83591 | 2024-10-13 05:04:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bac27b15-c0d2-3534-8e95-045c5980ee8d | -12.65656 | -59.82711 | 2024-10-13 05:04:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a67728ff-0997-3da6-b097-67b68fcab8b4 | -12.31478 | -59.81682 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7eaf7308-aa5b-3fc9-9b41-7df428d3f140 | -7.40112 | -59.71308 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 375af1e1-03b3-3172-a9fe-f7c6e83fa980 | -7.40036 | -59.7176 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0e7e939-c9ce-3a75-b7ff-6da1a11da874 | -7.39736 | -59.71246 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 662d3f02-f8fd-30da-b355-0a28e16b7e30 | -7.39674 | -59.7145 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 519131a8-3cb3-3b2c-9f7c-d399aaf975ba | -7.3966 | -59.71696 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d3ee358-9bbf-3d57-8602-3bfb02f4896c | -7.39601 | -59.71901 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b58ba5cf-a1fd-326c-8cfa-71d8b44a1c83 | -7.39208 | -59.72085 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd3f876a-2494-368d-b9ee-f7d75da5dee6 | -7.39151 | -59.72292 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63c0b4bc-efed-3855-8780-cb48f2d233e5 | -7.38849 | -59.71777 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README87.md)
