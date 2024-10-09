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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f7b50f5-a990-33e2-ba1a-25140fe76623 | -16.774599 | -56.6931 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6283cfb7-3f99-337b-90b8-ebc1346f7d09 | -16.776501 | -56.701099 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 97496894-0c3d-3a6d-8ca6-931baa520757 | -16.761101 | -56.6796 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6cb23b67-407a-31a5-ad1e-7448bc79a5ea | -16.763 | -56.687599 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea9a807b-b6b0-3e62-9bf8-eaa30a4930e4 | -16.764799 | -56.695599 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7867fe7c-649b-38aa-9bac-c916fff9f474 | -16.7514 | -56.681999 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aeb6563f-8f3f-3148-a345-4bc779a3f78e | -16.7533 | -56.689999 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b3ec4846-2dc0-31bd-b6f3-2f931983be5b | -16.7551 | -56.698002 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 29146bcb-c90e-3303-bf90-136454ca387f | -16.757 | -56.706001 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3231fb88-2de7-3a4e-bd61-e9a67d3ae9b9 | -16.9268 | -57.4422 | 2024-10-09 01:24:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ce2e21a-64d9-3c44-801e-29db42939fb4 | -16.928499 | -57.449699 | 2024-10-09 01:24:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 181fba9e-29eb-3f90-85a0-fcaf4ff8f778 | -16.7416 | -56.684399 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fb0c8d6b-8b19-3743-9452-71f0547aa6c2 | -16.7435 | -56.692402 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7c976c8-8b80-3d89-87c2-735ae975131a | -16.7453 | -56.700401 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8b5fb867-5a7e-34b6-af33-f25ef00c1c1a | -16.7472 | -56.708401 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7bbf7a16-0645-3d0b-86f1-923e21a7111d | -16.427099 | -55.918098 | 2024-10-09 01:24:59 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 25cce974-9c36-330f-80b9-14a29121bb5d | -16.429199 | -55.9268 | 2024-10-09 01:24:59 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b78ef375-e9fd-34bc-beda-bf1f803da671 | -16.4153 | -55.9119 | 2024-10-09 01:24:59 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8af26c18-6b44-31a6-b75e-b71166164a0f | -16.4174 | -55.920601 | 2024-10-09 01:24:59 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0680715c-955e-3da3-a9ad-b309e03aaf6d | -16.419399 | -55.929199 | 2024-10-09 01:24:59 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 833e9bcd-fdee-3620-b97e-21be912c238e | -16.421499 | -55.937901 | 2024-10-09 01:24:59 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d06f9269-4534-3d3b-a6da-ba5867f0a655 | -16.4235 | -55.946499 | 2024-10-09 01:24:59 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6821ed5a-5361-36d4-845a-05bc1ae4c2c1 | -16.4076 | -55.9231 | 2024-10-09 01:25:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33924ee1-aaf4-3184-b085-e4dd0af6951e | -16.409599 | -55.931702 | 2024-10-09 01:25:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f4a4df4d-c2e6-3231-bec8-9f9312fc71aa | -16.411699 | -55.940399 | 2024-10-09 01:25:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d98e1672-b5e0-32d1-8d7d-bed68a3adb36 | -16.678301 | -57.124401 | 2024-10-09 01:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dff9fc71-48f9-371d-bed8-21e5a085617d | -16.680099 | -57.132099 | 2024-10-09 01:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b7f2ad7e-0fe4-3c30-bee0-b57f281a4ba6 | -16.6703 | -57.134499 | 2024-10-09 01:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a142462-b365-3fea-9636-149d00af4615 | -16.660601 | -57.136902 | 2024-10-09 01:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4725a560-cec2-3119-b95e-bee44319bf09 | -16.7113 | -57.447399 | 2024-10-09 01:25:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9ecbf67a-5927-3eec-b5f5-3efd25fb5d1a | -16.712999 | -57.454899 | 2024-10-09 01:25:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 13790eb4-3a40-3cc8-b98d-3477de3a58b9 | -16.6206 | -57.097801 | 2024-10-09 01:25:01 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d82f42e-9f6d-3506-adea-886e2a2f4ae1 | -16.622299 | -57.105499 | 2024-10-09 01:25:01 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e54b63b9-e339-34ca-9f20-afcf89e28ce8 | -16.698 | -57.434601 | 2024-10-09 01:25:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b55decd9-365b-3b66-8528-e7c4f8df48e2 | -16.699699 | -57.4422 | 2024-10-09 01:25:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2a691df-a564-3c9f-93f4-4c6fe64d6039 | -16.7015 | -57.449799 | 2024-10-09 01:25:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6a9df51-86b4-31da-9a88-b43495ad284d | -16.703199 | -57.457298 | 2024-10-09 01:25:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 277eff79-f027-3379-8013-7e3880030856 | -16.689899 | -57.444599 | 2024-10-09 01:25:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e79fd8be-eecc-3306-af4c-1fbd8edeb7a0 | -16.6917 | -57.452202 | 2024-10-09 01:25:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4d100435-fd1f-3aff-adfd-76a989a3a3af | -16.6063 | -57.1259 | 2024-10-09 01:25:01 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 49ba3606-6381-3103-b0f6-cf08d16884a9 | -16.608101 | -57.133598 | 2024-10-09 01:25:01 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 98845d3a-7f51-31d3-8440-d1de0c009680 | -16.655399 | -57.4291 | 2024-10-09 01:25:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33774b8e-f1ba-3a7c-8c5a-b1bbd83b0a98 | -16.6572 | -57.436699 | 2024-10-09 01:25:01 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 15c39bf6-76e0-3f70-939f-d216aae52ea9 | -15.9162 | -54.995098 | 2024-10-09 01:25:04 | METOP-B | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0d844a-c877-36f5-8ba7-83900961dc3e | -15.9186 | -55.004902 | 2024-10-09 01:25:04 | METOP-B | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d42fd13-4ffa-3d0d-b4a7-c54921470bba | -16.1208 | -55.847801 | 2024-10-09 01:25:04 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa859ed4-4b92-3202-9e27-5b32aa87d6eb | -16.4331 | -57.314999 | 2024-10-09 01:25:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d7e35cd1-7d78-35ff-b1e3-a58806a715a0 | -16.434799 | -57.322601 | 2024-10-09 01:25:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c51f979-1be5-3fca-9d02-fdc12107c8e1 | -16.4366 | -57.330299 | 2024-10-09 01:25:04 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41c9fa5e-13d3-3ff8-8fc9-ab061054dbdd | -16.4233 | -57.317402 | 2024-10-09 01:25:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d8c7026b-bde7-3894-8958-b47e46aad2fb | -16.424999 | -57.325001 | 2024-10-09 01:25:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1df1ebf8-fd16-3190-bfb4-ce0be8a80614 | -16.4118 | -57.312199 | 2024-10-09 01:25:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 833b2ac4-fd5c-3e41-9050-b281de5d92cd | -16.4135 | -57.319801 | 2024-10-09 01:25:05 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9122fdc-e86a-3cd5-a1aa-a631bd1eb68a | -16.572701 | -58.245998 | 2024-10-09 01:25:06 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6baf9093-b873-3034-8b65-56fd0904f4bc | -1.11 | -53.6173 | 2024-10-09 01:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 0259570c-c9f4-3a48-aa72-6ed5afff6483 | -1.1284 | -53.6171 | 2024-10-09 01:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f615982f-ec6f-323f-a3db-d8170da1e442 | -15.9533 | -57.2052 | 2024-10-09 01:25:12 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e611ad7e-80b5-3e89-8c96-fde780ad546f | -15.9418 | -57.199902 | 2024-10-09 01:25:12 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e259593-a29e-3829-bac9-b5fc1dfa0197 | -15.6044 | -57.348301 | 2024-10-09 01:25:18 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec611196-d26a-3c04-9777-5e65e3e1d831 | -15.6061 | -57.355999 | 2024-10-09 01:25:18 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f6e81fb-43ca-3c6d-9f97-853346de76b9 | -15.5946 | -57.3507 | 2024-10-09 01:25:18 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dcc0da19-4dfd-356e-9316-25c7294faa90 | -15.5963 | -57.358398 | 2024-10-09 01:25:18 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc43bb82-a7d2-3445-b62e-43ffa498d51d | -15.5981 | -57.3661 | 2024-10-09 01:25:18 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b61e768-cd7c-324c-92f2-6266f0408d34 | -15.9751 | -59.0765 | 2024-10-09 01:25:18 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b28de7c0-203d-3efa-819e-3e2bb946b4cb | -15.9653 | -59.0788 | 2024-10-09 01:25:18 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac344dd8-8022-3721-8332-404567bf74e7 | -15.8065 | -59.198601 | 2024-10-09 01:25:21 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9987dd5-2c27-31d3-ace2-2e8cf0b63395 | -15.7092 | -59.3633 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 770ffd23-09b6-30a4-8c9b-bab7936de34f | -15.7107 | -59.370399 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 897bfcc0-bc15-35a0-ba2c-7e2a376f7264 | -15.6994 | -59.365601 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 132564e4-e56d-330d-a8bd-da59fdb13469 | -15.7009 | -59.3727 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5c31e19-1057-32f4-bffb-09a1ddbed87c | -15.715 | -59.436501 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df855352-a0f3-3b13-9fdc-99c21f8c9c76 | -15.6896 | -59.367901 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7669e7c-65f8-3972-899a-a44b84b53d9f | -15.6911 | -59.375 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c1b7484-bea3-38db-b393-17c04508ad27 | -15.6927 | -59.382 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 633fa17b-643b-3105-b95d-2543fba9a6bd | -15.6943 | -59.389099 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3e1c918-6994-3ffc-99a8-a6339df3b786 | -15.6958 | -59.396198 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98674f2e-2a39-3bd4-bc37-81b5b1570e6b | -15.6974 | -59.403301 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3620ae08-8b03-31cf-b041-372dd8cdd42d | -15.6813 | -59.377201 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dbf22c9c-5622-381e-8801-e8fc31d79f1e | -15.6829 | -59.3843 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc8885e5-6ef3-326c-ad2e-3b38a7271c3a | -15.6845 | -59.391399 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74c0100f-8493-307f-a128-dd6abbe53bdb | -15.6731 | -59.3866 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d3a6a72-8883-3739-a381-21539df365f9 | -15.6747 | -59.3937 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5a37413-07ac-3ca0-b286-10e7d3b4da1b | -15.6762 | -59.400799 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8c3a8c0-837b-3dd4-9806-7a392e72de30 | -15.6633 | -59.388901 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bfcbe812-89d2-3765-885b-3bf3c9417930 | -15.6649 | -59.396 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38c7d342-3728-31dc-8b7f-c60f8bd0cc83 | -15.6664 | -59.403099 | 2024-10-09 01:25:24 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c78ce418-d9f8-3a50-84d9-c226a40c0b75 | -15.6551 | -59.3983 | 2024-10-09 01:25:25 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6c8711a-99dc-3592-9f87-e9545db79f70 | -15.6566 | -59.405399 | 2024-10-09 01:25:25 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f0e2279-ac4d-359b-a87b-f9d1bf615181 | -15.6582 | -59.412498 | 2024-10-09 01:25:25 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5a729b6-41b6-31f1-86b5-fb55a7d13cc3 | -15.6598 | -59.419498 | 2024-10-09 01:25:25 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa1a83e5-21ae-3df3-a9ae-aee88ce45aa9 | -15.6629 | -59.433701 | 2024-10-09 01:25:25 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db6d766d-b0c4-34bc-b01e-232b00483899 | -15.65 | -59.421799 | 2024-10-09 01:25:25 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7c02b5b-3a0f-39cd-9230-e2d9692cfb61 | -15.6515 | -59.428902 | 2024-10-09 01:25:25 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54dd6734-5199-345a-bfd1-0b756bce5438 | -15.6531 | -59.436001 | 2024-10-09 01:25:25 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c89b213-d411-3ad1-990d-cf015b75d711 | -14.7848 | -55.9692 | 2024-10-09 01:25:26 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 320d8669-3391-3988-818c-7498a116ea0d | -3.8007 | -41.6229 | 2024-10-09 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 8cdd3877-421a-3535-9561-d395d9efde76 | -3.8008 | -41.5989 | 2024-10-09 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 9a226dfe-6cb1-3ded-b8c6-5084528d96f3 | -15.5215 | -59.585999 | 2024-10-09 01:25:27 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09bd0f86-2ef9-3c28-bd4d-a717e6f5ebad | -15.5231 | -59.593102 | 2024-10-09 01:25:27 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2dbe60ed-fa3e-3cbe-94ba-ee4fa3c07833 | -15.5246 | -59.600201 | 2024-10-09 01:25:27 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README39.md)
